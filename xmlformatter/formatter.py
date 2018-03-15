"""XmlFormatter format or compress XML documents 

Copyright (c) 2011, 2012 P. Andreas Moeller
see License for more details
"""
import re, sys
import xml.parsers.expat

class Formatter():
	# don't compress this elements descendants
	preserving = []
	# indent = indent*level*indentChar
	indent = 2
	# comression
	compress = False
	# indent by this char
	indentChar = " "
	# encoding
	encoding_input = None
	# internal encoding
	encoding_internal = None
	# out encoding
	encoding_output = None
	# list of tokens
	TokenList = None
	# create parser object
	parser = None

	class TokenList:
		# being in a cdata section
		cdataSection = False
		# count levels
		levelCnt = 0
		# don't remove whitespaces while level > preserveLevel
		preserveLevel = None
		# don't remove leading whitespace for level > descMixedLevel
		descMixedLevel = None
		# don't indent while level > indentLevel
		indentLevel = None

		def __init__(self, formatter):
			self.formatter = formatter
			self._list = []
			self.parser = xml.parsers.expat.ParserCreate(encoding=self.formatter.encoding_input)
			self.parser.returns_unicode = False
			self.parser.specified_attributes = 1
			self.parser.buffer_text = True
			# push tokens to buffer
			for pattern in ['XmlDecl%s', 'ElementDecl%s', 'AttlistDecl%s',\
							'EntityDecl%s', 'StartElement%s', 'EndElement%s',\
							'ProcessingInstruction%s', 'CharacterData%s', \
							'Comment%s', 'Default%s', 'StartDoctypeDecl%s',\
							'EndDoctypeDecl%s', 'StartCdataSection%s', \
							'EndCdataSection%s', 'NotationDecl%s']:
				setattr(self.parser, pattern %'Handler', self.handler(pattern %''))		

		def handler(self, key):
			""" returns lambda function thats adds token to token list"""
			return lambda *arg: self.append(getattr(self.formatter, key)(self, arg))

		def __iter__(self):
			return iter(self._list)
			
		def __len__(self):
			return len(self._list)

		def __getitem__(self, pos):
			if 0 <= pos < len(self._list):
				return self._list[pos]
			else:
				raise IndexError

		def __setitem__(self, pos, value):
			if 0 <= pos < len(self._list):
				self._list[pos] = value
			else:
				raise IndexError

		def __str__(self):
			""" returns formatted document """
			for step in ["tree", "pre", "post"]:
				for tk in iter(self):
					getattr(tk, step)()
			result = ""
			for tk in iter(self):
				result += str(tk)
			return result.decode('utf-8').encode(self.formatter.encoding_effective)

		def append(self, tk):
			tk.pos = len(self._list)
			self._list.append(tk)

		def increment(self):
			self.levelCnt += 1

		def decrement(self):
			self.levelCnt -= 1

		def descendant_mixed(self, tk):
			if tk.name == "StartElement":
				""" block indenting for descendants of text! and mixed content!"""
				if (tk.contentModel in [2,3] and self.descMixedLevel is None):
					self.descMixedLevel = tk.level
					return False
				return (self.descMixedLevel is not None)
			elif tk.name == "EndElement":
				""" unblock indenting for descendants of text and mixed content!"""
				if (tk.level is self.descMixedLevel):	
					self.descMixedLevel = None
				elif (self.descMixedLevel is not None):
					return True
				return False
			return (self.descMixedLevel >= tk.level-1)

		def sequence(self, tk, scheme = None):
			if (scheme == "EndElement" or (scheme is None and tk.end)):
				return reversed(self._list[:tk.pos])
			return self._list[(tk.pos + 1):]

		def model(self, tk):
			""" Return code for content model: 0: empty, 1: element, 2: text, 3 mixed """
			eflag = tflag = 0
			for itk in iter(self.sequence(tk)):
				# element boundary found
				if (itk.level <= tk.level):
					break
				# direct child
				elif ((itk.level - 1) == tk.level):
					if (itk.start):
						eflag = 1
					elif (itk.not_empty):
						tflag = 2
			return (eflag + tflag)
		
		def preserving(self, tk):
			if tk.name == "StartElement":
				""" Returns code for preserving locking: 0: not locked, 1: just locked,  2: locked """
				if (self.preserveLevel is not None):
					return 2
				if (tk.arg[0] in self.formatter.preserving):
					self.preserveLevel = tk.level
					return 1			
				return 0
			elif tk.name == "EndElement":
				""" Returns code for preserving unlocking: 0: not locked, 1: just unlocked, 2: locked """
				if (tk.arg[0] in self.formatter.preserving and tk.level == self.preserveLevel):
					self.preserveLevel = None
					return 1
				elif (self.preserveLevel is None):
					return 0
				return 2
			return (self.preserveLevel is not None)
			
		def indent(self, tk):
			if tk.name == "StartElement":
				""" block indenting for descendants of text and mixed content!"""
				if (tk.contentModel in [2,3] and self.indentLevel is None):
					self.indentLevel = tk.level
				elif (self.indentLevel is not None):
					return False
				return True
			elif tk.name == "EndElement":
				""" unblock indenting for descendants of text and mixed content!"""
				if (tk.level == self.indentLevel):	
					self.indentLevel = None
				elif (self.indentLevel is None):
					return True
				return False
			return (self.indentLevel is None)
			
		def append_trailing(self, tk):
			""" add a trailing space to previous character data """
			if (tk.leading and tk.not_empty):
				self.append_whitespace(tk, "EndElement", "StartElement", True)

		def append_leading(self, tk):
			""" add a trailing space to previous character data """
			if (tk.trailing and tk.not_empty):
				self.append_whitespace(tk)

		def append_whitespace(self, tk, start = "StartElement", stop = "EndElement", direct = False):
			for itk in self.sequence(tk, start):
				if (itk.empty or (itk.name == stop and itk.descendantMixed is False) or (itk.name == start and abs(tk - itk) == 1)):
					break
				elif (itk.not_empty or (itk.name == start and itk.descendantMixed)):
					self.insert_empty(itk, direct)
					break
			
		def delete_leading(self, tk):
			"""Returns True, if no next token or all empty (up to next end element)"""
			if (tk.leading and not tk.preserve and not tk.cdataSection):
				for itk in self.sequence(tk, "EndElement"):
					if (itk.trailing):
						return True
					elif (itk.name in ["EndElement", "CharacterData", "EndCdataSection"]):
						return False
				return True
			return False
		
		def delete_trailing(self, tk):
			"""Returns True, if no next token or all empty (up to next end element)"""
			if (tk.trailing and not tk.preserve and not tk.cdataSection):
				for itk in self.sequence(tk, "StartElement"):
					if (itk.end):
						return True
					elif (itk.name in ["StartElement", "StartCdataSection"] or itk.not_empty):
						return False
				return True
			return False

		def insert_empty(self, tk, before = True):
			if (not (0 < tk.pos < (len(self) - 1))):
				return False
			ptk = self[tk.pos-1]
			ntk = self.formatter.CharacterData(self, [" "])
			ntk.level= max(ptk.level, tk.level)
			ntk.descendantMixed = tk.descendantMixed
			ntk.preserve = ptk.preserve*tk.preserve
			ntk.cdataSection = (ptk.cdataSection or tk.cdataSection)
			if (before):
				self._list.insert(tk.pos+1, ntk)
			else:
				self._list.insert(tk.pos, ntk)
			for i in range((tk.pos - 1), len(self._list)):
				self._list[i].pos = i

	class Token(object):
		def __init__(self, tklist, arg):
			# token type
			self.name = self.__class__.__name__
			# ref formatter
			self.formatter = tklist.formatter
			# ref tokenlist
			self.list = tklist
			# token datas
			self.arg= list(arg)
			# position in token list
			self.pos = None
			# n-th generation of roots children
			self.level = self.list.levelCnt
			# insert indenting white spaces
			self.indent = False
			# preserve white spaces within token
			self.preserve = False
			# remove trailing wihtespaces
			self.deleteTrailing = False
			# remove leading whitespaces
			self.deleteLeading = False
			# token is descendant of text or mixed content element
			self.descendantMixed = False
			# content model
			self.contentModel = None
			# content with in cdata section
			self.cdataSection = False

		def __sub__(self, other):
			return self.pos - other.pos

		def __str__(self):
			return ""

		@property
		def end(self):
			return (self.name == "EndElement")

		@property
		def empty(self):
			return (self.name == "CharacterData" and re.match(r'^[\t\s\n]*$', self.arg[0]))

		@property
		def leading(self):
			return (self.name == "CharacterData" and re.search(r'^[\t\s\n]+', self.arg[0]))

		@property
		def not_empty(self):
			return (self.name == "CharacterData" and not self.cdataSection and not re.match(r'^[\t\s\n]+$', self.arg[0]))

		@property
		def trailing(self):
			return (self.name == "CharacterData" and re.search(r'[\t\s\n]+$', self.arg[0]))

		@property
		def start(self):
			return (self.name == "StartElement")

		def attribute(self, key, value):
			if (key and value):
				return " %s=\"%s\"" %(key, value)
			return ""

		def format_indent(self):
			# child of root and no empty node	
			if ((self.level > 0 and not (self.end and self.list[self.pos - 1].start))\
				# not empty node
			or (self.end and not self.list[self.pos-1].start)):
				return self.get_indent(self.level)
			return ""

		def get_indent(self, times = 1):
			if (not self.formatter.compress and self.formatter.indent):
				return "\n%s" %((times * self.formatter.indent) * self.formatter.indentChar)
			return ""

		def identifier(self, systemid, publicid):
			""" TODO add base parameter """
			if (publicid and systemid):
				return ' PUBLIC "%s" "%s"' %(publicid, systemid)
			elif (publicid):
				return ' PUBLIC "%s"' %publicid
			elif (systemid):
				return ' SYSTEM "%s"' %systemid
			return ""

		def tree(self):
			self.descendantMixed = self.list.descendant_mixed(self)
			self.preserve = self.list.preserving(self)
			self.cdataSection = self.list.cdataSection

		def pre(self):
			pass

		def post(self):
			pass

	class AttlistDecl(Token):
		def __str__(self):
			str = self.get_indent()
			str += "<!ATTLIST %s %s" %(self.arg[0], self.arg[1])
			if (self.arg[2] is not None):
				str += " %s" %self.arg[2] 
			if (self.arg[4] and not self.arg[3]):
				str += " #REQUIRED"
			elif (self.arg[3] and self.arg[4]):
				str += " #FIXED"
			elif(not self.arg[4] and not self.arg[3]):
				str += " #IMPLIED"
			if (self.arg[3]):
				str += ' "%s"' %self.arg[3]
			str += ">"
			return str

	class CharacterData(Token):
		def __str__(self):
			str = self.arg[0]
			if (not self.preserve and not self.cdataSection):
				# remove empty tokens always in element content!
				if (self.empty and not self.descendantMixed):
					str = ""
				else:
					str = re.sub(r'\r\n', '\n', str)	
					str = re.sub(r'\r|\n|\t', ' ', str)
					str = re.sub(r'\s+', ' ', str)
					if (self.deleteLeading):
						str = re.sub(r'^\s', '', str)
					if (self.deleteTrailing):
						str = re.sub(r'\s$', '', str)
			if not self.cdataSection:
				str = re.sub(r'&', '&amp;', str)
				str = re.sub(r'<', '&lt;', str)	
			return str
	
		def pre(self):
			self.list.append_trailing(self)
			self.list.append_leading(self)

		def post(self):
			self.deleteLeading = self.list.delete_leading(self)
			self.deleteTrailing = self.list.delete_trailing(self)
	
	class Comment(Token):
		def __str__(self):
			str = ""
			if (self.preserve in [0,1] and self.indent):
				str += self.format_indent()
			str += "<!--%s-->" %re.sub(r'^[\r\n]+$', '\n', re.sub(r'^[\r\n]+', '\n', self.arg[0]))
			return str

		def tree(self):
			super(Formatter.Comment, self).tree()
			self.indent = self.list.indent(self)

	class Default(Token):
		pass
	
	class EndCdataSection(Token):
		def __str__(self):
			return "]]>"

		def tree(self):
			self.list.cdataSection = False
		
	class ElementDecl(Token):
		def __str__(self):
			str = self.get_indent()
			str += "<!ELEMENT %s%s>" %(self.arg[0], self.evaluate_model(self.arg[1]))
			return str

		def evaluate_model(self, model, modelStr = "", concatStr = ""):
			childSeq = []
			mixed = (model[0] == xml.parsers.expat.model.XML_CTYPE_MIXED)
			hasChilds = (len(model[3]) or mixed)
			if (model[0] == xml.parsers.expat.model.XML_CTYPE_EMPTY): #1
				modelStr += " EMPTY"
			elif (model[0] == xml.parsers.expat.model.XML_CTYPE_ANY): #2
				modelStr += " ANY"
			elif (model[0] == xml.parsers.expat.model.XML_CTYPE_NAME): #4
				modelStr = "%s" %model[2] # new start
			elif (model[0] in (xml.parsers.expat.model.XML_CTYPE_CHOICE, xml.parsers.expat.model.XML_CTYPE_MIXED)): #5
				concatStr = "|"
			elif (model[0] == xml.parsers.expat.model.XML_CTYPE_SEQ): #6
				concatStr = ","
			if (hasChilds):
				modelStr += " ("
			if (mixed):
				childSeq.append("#PCDATA")
			for child in model[3]:
				childSeq.append(self.evaluate_model(child))
			modelStr += concatStr.join(childSeq)
			if (hasChilds):
				modelStr += ")"
			modelStr += {xml.parsers.expat.model.XML_CQUANT_NONE:"", \
		             xml.parsers.expat.model.XML_CQUANT_OPT:"?", \
		             xml.parsers.expat.model.XML_CQUANT_PLUS:"+", \
		             xml.parsers.expat.model.XML_CQUANT_REP:"*"\
		             }[model[1]]
			return modelStr

	class EndDoctypeDecl(Token):
		def __str__(self):
			str = ""
			if (self.list[self.pos - 1].name != "StartDoctypeDecl"):
				str += self.get_indent(0)
				str += "]"
			str += ">"
			str += self.get_indent(0)
			return str
	
	class EndElement(Token):
		def __init__(self, list, arg):
			list.decrement()
			super(Formatter.EndElement, self).__init__(list, arg)

		def __str__(self):
			str = ""
			# don't close empty nodes on compression mode!
			if (not self.formatter.compress or self.list[self.pos-1].name != "StartElement"):
				if (self.preserve in [0] and self.indent):
					str += self.format_indent()
				str += "</%s>" %self.arg[0]
			return str
		
		def tree(self):
			self.descendantMixed = self.list.descendant_mixed(self)
			self.preserve = self.list.preserving(self)
			self.indent = self.list.indent(self)

	class EntityDecl(Token):
		def __str__(self):
			str = self.get_indent()
			str += "<!ENTITY "
			if (self.arg[1]):
				str += "% "
			str += "%s " %self.arg[0]
			if (self.arg[2]):
				str += '"%s"' %self.arg[2]
			else:
				str += "%s " %self.identifier(self.arg[4], self.arg[5])
				if (self.arg[6]):
					str += "NDATA %s" %self.arg[6]
			str += ">"	
			return str

	class NotationDecl(Token):
		def __str__(self):
			str = self.get_indent()
			str += "<!NOTATION %s%s>" %(self.arg[0], self.identifier(self.arg[2], self.arg[3]))
			return str

	class ProcessingInstruction(Token):
		def __str__(self):
			str = ""
			if (self.preserve in [0,1] and self.indent):
				str += self.format_indent()
			str += "<?%s %s?>" %(self.arg[0], self.arg[1])
			return str

		def tree(self):
			super(Formatter.ProcessingInstruction, self).tree()
			self.indent = self.list.indent(self)

	class StartCdataSection(Token):
		def __str__(self):
			return "<![CDATA["

		def tree(self):
			self.list.cdataSection = True
	
	class StartDoctypeDecl(Token):
		def __str__(self):
			str = "<!DOCTYPE %s" %(self.arg[0])
			if (self.arg[1]):
				str += self.identifier(self.arg[1], self.arg[2])
			if (self.arg[3]):
				str += " ["
			return str

	class StartElement(Token):
		def __init__(self, list, arg):
			super(Formatter.StartElement, self).__init__(list, arg)
			self.list.increment()

		def __str__(self):
			str = ""
			if (self.preserve in [0, 1] and self.indent):
				str += self.format_indent()
			str += "<%s" %self.arg[0]
			for attr in sorted(self.arg[1].keys()):
				str += self.attribute(attr, self.arg[1][attr])
			if (self.list[self.pos+1].end and self.formatter.compress):
				str += "/>"
			else:
				str += ">"
			return str

		def tree(self):
			self.contentModel = self.list.model(self)
			self.descendantMixed = self.list.descendant_mixed(self)
			self.preserve = self.list.preserving(self)
			self.indent = self.list.indent(self)
	
	class XmlDecl(Token):
		def __init__(self, list, arg):
			super(Formatter.XmlDecl, self).__init__(list, arg)
			if (len(self.arg) > 1):
				self.formatter.encoding_internal = self.arg[1]

		def __str__(self):
			str = "<?xml%s%s" %(self.attribute('version', self.arg[0]), self.attribute('encoding', self.formatter.encoding_effective)) 
			if (self.arg[2] > -1):
				str += self.attribute("standalone", "yes")
			str += "?>\n"
			return str

	def __init__(self, indent = 2, preserving = [], compress = False, indentChar = ' ', encoding_input = None, encoding_output = None):
		self.preserving = preserving
		self.indent = int(indent)
		self.compress = compress
		self.indentChar = indentChar
		self.encoding_input = self.encoding_string(encoding_input)
		self.encoding_output = self.encoding_string(encoding_output)

	@property	
	def encoding_effective(self, enc = None):
		if (self.encoding_output):
			return self.encoding_output
		elif (self.encoding_internal):
			return self.encoding_internal
		elif (self.encoding_input):
			return self.encoding_input
		else:
			return 'UTF-8'

	def encoding_string(self, string):
		if (isinstance(string, str)):
			return string.upper()
		return None

	def format_string(self, xmldoc=""):
		self.TokenList = Formatter.TokenList(self)
		self.TokenList.parser.Parse(xmldoc)
		return str(self.TokenList)

	def format_file(self, file):
		self.TokenList = Formatter.TokenList(self)
		self.TokenList.parser.ParseFile(open(file))
		return str(self.TokenList)