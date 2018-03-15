# .\myTest_test_myVer_crypto_sam_cfg.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:d23c6b1ac312b723b897ace3be6b6eb784085108
# Generated 2013-10-24 15:04:06.900000 by PyXB version 1.2.3
# Namespace http://myTest.com/ns/yang/myTest-test-myVer-crypto-sam-cfg

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:c3c9a35e-3cac-11e3-a1cd-3c970e99f68c')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://myTest.com/ns/yang/myTest-test-myVer-crypto-sam-cfg', create_if_missing=True)
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


# Atomic simple type: {http://myTest.com/ns/yang/myTest-test-myVer-crypto-sam-cfg}Crypto-sam-action
class Crypto_sam_action (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        Crypto sam action
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Crypto-sam-action')
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-crypto-sam-cfg.xsd', 39, 2)
    _Documentation = u'\n        Crypto sam action\n      '
Crypto_sam_action._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Crypto_sam_action, enum_prefix=None)
Crypto_sam_action.proceed = Crypto_sam_action._CF_enumeration.addEnumeration(unicode_value=u'proceed', tag=u'proceed')
Crypto_sam_action.terminate = Crypto_sam_action._CF_enumeration.addEnumeration(unicode_value=u'terminate', tag=u'terminate')
Crypto_sam_action._InitializeFacetMap(Crypto_sam_action._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'Crypto-sam-action', Crypto_sam_action)

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.unsignedInt):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-crypto-sam-cfg.xsd', 89, 22)
    _Documentation = None
STD_ANON._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON, value=pyxb.binding.datatypes.unsignedInt(300L))
STD_ANON._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON, value=pyxb.binding.datatypes.unsignedInt(0L))
STD_ANON._InitializeFacetMap(STD_ANON._CF_maxInclusive,
   STD_ANON._CF_minInclusive)

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """
        Crypto configuration
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-crypto-sam-cfg.xsd', 58, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-crypto-sam-cfg}sam uses Python identifier sam
    __sam = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sam'), 'sam', '__httpmyTest_comnsyangmyTest_test_myVer_crypto_sam_cfg_CTD_ANON_httpmyTest_comnsyangmyTest_test_myVer_crypto_sam_cfgsam', False, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-crypto-sam-cfg.xsd', 60, 8), )

    
    sam = property(__sam.value, __sam.set, None, u'\n              Software Authentication Manager (SAM) Config\n            ')

    _HasWildcardElement = True
    _ElementMap.update({
        __sam.name() : __sam
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """
              Software Authentication Manager (SAM) Config
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-crypto-sam-cfg.xsd', 66, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-crypto-sam-cfg}prompt-interval uses Python identifier prompt_interval
    __prompt_interval = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'prompt-interval'), 'prompt_interval', '__httpmyTest_comnsyangmyTest_test_myVer_crypto_sam_cfg_CTD_ANON__httpmyTest_comnsyangmyTest_test_myVer_crypto_sam_cfgprompt_interval', False, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-crypto-sam-cfg.xsd', 68, 14), )

    
    prompt_interval = property(__prompt_interval.value, __prompt_interval.set, None, u'\n                    Set prompt interval at reboot time\n                  ')

    _HasWildcardElement = True
    _ElementMap.update({
        __prompt_interval.name() : __prompt_interval
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """
                    Set prompt interval at reboot time
                  """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-crypto-sam-cfg.xsd', 74, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-crypto-sam-cfg}action uses Python identifier action
    __action = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'action'), 'action', '__httpmyTest_comnsyangmyTest_test_myVer_crypto_sam_cfg_CTD_ANON_2_httpmyTest_comnsyangmyTest_test_myVer_crypto_sam_cfgaction', False, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-crypto-sam-cfg.xsd', 76, 20), )

    
    action = property(__action.value, __action.set, None, u'\n                          Respond to SAM prompt either Proceed/Terminate\n                        ')

    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-crypto-sam-cfg}prompt-time uses Python identifier prompt_time
    __prompt_time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'prompt-time'), 'prompt_time', '__httpmyTest_comnsyangmyTest_test_myVer_crypto_sam_cfg_CTD_ANON_2_httpmyTest_comnsyangmyTest_test_myVer_crypto_sam_cfgprompt_time', False, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-crypto-sam-cfg.xsd', 83, 20), )

    
    prompt_time = property(__prompt_time.value, __prompt_time.set, None, u'\n                          Prompt time from 0 - 300 seconds\n                        ')

    _HasWildcardElement = True
    _ElementMap.update({
        __action.name() : __action,
        __prompt_time.name() : __prompt_time
    })
    _AttributeMap.update({
        
    })



crypto = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'crypto'), CTD_ANON, documentation=u'\n        Crypto configuration\n      ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-crypto-sam-cfg.xsd', 52, 2))
Namespace.addCategoryObject('elementBinding', crypto.name().localName(), crypto)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sam'), CTD_ANON_, scope=CTD_ANON, documentation=u'\n              Software Authentication Manager (SAM) Config\n            ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-crypto-sam-cfg.xsd', 60, 8)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-crypto-sam-cfg.xsd', 60, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-crypto-sam-cfg.xsd', 106, 8))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sam')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-crypto-sam-cfg.xsd', 60, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://myTest.com/ns/yang/myTest-test-myVer-crypto-sam-cfg')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-crypto-sam-cfg.xsd', 106, 8))
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




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'prompt-interval'), CTD_ANON_2, scope=CTD_ANON_, documentation=u'\n                    Set prompt interval at reboot time\n                  ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-crypto-sam-cfg.xsd', 68, 14)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-crypto-sam-cfg.xsd', 68, 14))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-crypto-sam-cfg.xsd', 101, 14))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'prompt-interval')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-crypto-sam-cfg.xsd', 68, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://myTest.com/ns/yang/myTest-test-myVer-crypto-sam-cfg')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-crypto-sam-cfg.xsd', 101, 14))
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




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'action'), Crypto_sam_action, scope=CTD_ANON_2, documentation=u'\n                          Respond to SAM prompt either Proceed/Terminate\n                        ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-crypto-sam-cfg.xsd', 76, 20)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'prompt-time'), STD_ANON, scope=CTD_ANON_2, documentation=u'\n                          Prompt time from 0 - 300 seconds\n                        ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-crypto-sam-cfg.xsd', 83, 20)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-crypto-sam-cfg.xsd', 96, 20))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'action')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-crypto-sam-cfg.xsd', 76, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'prompt-time')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-crypto-sam-cfg.xsd', 83, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://myTest.com/ns/yang/myTest-test-myVer-crypto-sam-cfg')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-crypto-sam-cfg.xsd', 96, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()

