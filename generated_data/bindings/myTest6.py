# .\myTest_test_myVer_parser_cfg.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:882b31104256afe99632ac3bde4dd4404a7fcb1d
# Generated 2013-10-21 11:05:19.427000 by PyXB version 1.2.3
# Namespace http://myTest.com/ns/yang/myTest-test-myVer-parser-cfg

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:e8b0030f-3a2f-11e3-82e4-3c970e99f68c')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import _myVer as _ImportedBinding__myVer

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://myTest.com/ns/yang/myTest-test-myVer-parser-cfg', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, unicode):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """
        Parser configuration
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-parser-cfg.xsd', 48, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-parser-cfg}alias uses Python identifier alias
    __alias = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'alias'), 'alias', '__httpmyTest_comnsyangmyTest_test_myVer_parser_cfg_CTD_ANON_httpmyTest_comnsyangmyTest_test_myVer_parser_cfgalias', False, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-parser-cfg.xsd', 50, 8), )

    
    alias = property(__alias.value, __alias.set, None, u'\n              Alias for command mapping\n            ')

    _HasWildcardElement = True
    _ElementMap.update({
        __alias.name() : __alias
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """
              Alias for command mapping
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-parser-cfg.xsd', 56, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-parser-cfg}commands uses Python identifier commands
    __commands = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'commands'), 'commands', '__httpmyTest_comnsyangmyTest_test_myVer_parser_cfg_CTD_ANON__httpmyTest_comnsyangmyTest_test_myVer_parser_cfgcommands', False, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-parser-cfg.xsd', 58, 14), )

    
    commands = property(__commands.value, __commands.set, None, u'\n                    Table of all aliases configured\n                  ')

    _HasWildcardElement = True
    _ElementMap.update({
        __commands.name() : __commands
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """
                    Table of all aliases configured
                  """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-parser-cfg.xsd', 64, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-parser-cfg}command uses Python identifier command
    __command = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'command'), 'command', '__httpmyTest_comnsyangmyTest_test_myVer_parser_cfg_CTD_ANON_2_httpmyTest_comnsyangmyTest_test_myVer_parser_cfgcommand', True, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-parser-cfg.xsd', 66, 20), )

    
    command = property(__command.value, __command.set, None, u'\n                          Alias name to command mapping\n                        ')

    _HasWildcardElement = True
    _ElementMap.update({
        __command.name() : __command
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """
                          Alias name to command mapping
                        """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-parser-cfg.xsd', 72, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-parser-cfg}alias-name uses Python identifier alias_name
    __alias_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'alias-name'), 'alias_name', '__httpmyTest_comnsyangmyTest_test_myVer_parser_cfg_CTD_ANON_3_httpmyTest_comnsyangmyTest_test_myVer_parser_cfgalias_name', False, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-parser-cfg.xsd', 74, 26), )

    
    alias_name = property(__alias_name.value, __alias_name.set, None, u'\n                                Alias Name\n                              ')

    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-parser-cfg}command uses Python identifier command
    __command = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'command'), 'command', '__httpmyTest_comnsyangmyTest_test_myVer_parser_cfg_CTD_ANON_3_httpmyTest_comnsyangmyTest_test_myVer_parser_cfgcommand', True, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-parser-cfg.xsd', 81, 26), )

    
    command = property(__command.value, __command.set, None, u'\n                                The actual command\n                              ')

    _HasWildcardElement = True
    _ElementMap.update({
        __alias_name.name() : __alias_name,
        __command.name() : __command
    })
    _AttributeMap.update({
        
    })



parser = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'parser'), CTD_ANON, documentation=u'\n        Parser configuration\n      ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-parser-cfg.xsd', 42, 2))
Namespace.addCategoryObject('elementBinding', parser.name().localName(), parser)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'alias'), CTD_ANON_, scope=CTD_ANON, documentation=u'\n              Alias for command mapping\n            ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-parser-cfg.xsd', 50, 8)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-parser-cfg.xsd', 50, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-parser-cfg.xsd', 107, 8))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'alias')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-parser-cfg.xsd', 50, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://myTest.com/ns/yang/myTest-test-myVer-parser-cfg')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-parser-cfg.xsd', 107, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'commands'), CTD_ANON_2, scope=CTD_ANON_, documentation=u'\n                    Table of all aliases configured\n                  ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-parser-cfg.xsd', 58, 14)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-parser-cfg.xsd', 58, 14))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-parser-cfg.xsd', 102, 14))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'commands')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-parser-cfg.xsd', 58, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://myTest.com/ns/yang/myTest-test-myVer-parser-cfg')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-parser-cfg.xsd', 102, 14))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'command'), CTD_ANON_3, scope=CTD_ANON_2, documentation=u'\n                          Alias name to command mapping\n                        ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-parser-cfg.xsd', 66, 20)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-parser-cfg.xsd', 66, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-parser-cfg.xsd', 93, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'command')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-parser-cfg.xsd', 66, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://myTest.com/ns/yang/myTest-test-myVer-parser-cfg')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-parser-cfg.xsd', 93, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'alias-name'), pyxb.binding.datatypes.string, scope=CTD_ANON_3, documentation=u'\n                                Alias Name\n                              ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-parser-cfg.xsd', 74, 26)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'command'), _ImportedBinding__myVer.myTest_test_myVer_string, scope=CTD_ANON_3, documentation=u'\n                                The actual command\n                              ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-parser-cfg.xsd', 81, 26)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1L, max=3L, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-parser-cfg.xsd', 81, 26))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-parser-cfg.xsd', 88, 26))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'alias-name')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-parser-cfg.xsd', 74, 26))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'command')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-parser-cfg.xsd', 81, 26))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://myTest.com/ns/yang/myTest-test-myVer-parser-cfg')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-parser-cfg.xsd', 88, 26))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_3()

