# .\myTest_test_myVer_config_mda_cfg.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:dcdf8d1ed05d02f39642babbee5437ff85312bd6
# Generated 2013-10-24 12:29:55.758000 by PyXB version 1.2.3
# Namespace http://myTest.com/ns/yang/myTest-test-myVer-config-mda-cfg

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:39a1cc40-3c97-11e3-9dc0-3c970e99f68c')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import _myVer as _ImportedBinding__myVer
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://myTest.com/ns/yang/myTest-test-myVer-config-mda-cfg', create_if_missing=True)
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
        Per-node configuration for active nodes
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-config-mda-cfg.xsd', 49, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-config-mda-cfg}active-node uses Python identifier active_node
    __active_node = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'active-node'), 'active_node', '__httpmyTest_comnsyangmyTest_test_myVer_config_mda_cfg_CTD_ANON_httpmyTest_comnsyangmyTest_test_myVer_config_mda_cfgactive_node', True, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-config-mda-cfg.xsd', 51, 8), )

    
    active_node = property(__active_node.value, __active_node.set, None, u'\n              The configuration for an active node\n            ')

    _HasWildcardElement = True
    _ElementMap.update({
        __active_node.name() : __active_node
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """
              The configuration for an active node
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-config-mda-cfg.xsd', 57, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-config-mda-cfg}node-name uses Python identifier node_name
    __node_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'node-name'), 'node_name', '__httpmyTest_comnsyangmyTest_test_myVer_config_mda_cfg_CTD_ANON__httpmyTest_comnsyangmyTest_test_myVer_config_mda_cfgnode_name', False, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-config-mda-cfg.xsd', 59, 14), )

    
    node_name = property(__node_name.value, __node_name.set, None, u'\n                    The identifier for this node\n                  ')

    _HasWildcardElement = True
    _ElementMap.update({
        __node_name.name() : __node_name
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """
        preconfigured nodes
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-config-mda-cfg.xsd', 86, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-config-mda-cfg}preconfigured-node uses Python identifier preconfigured_node
    __preconfigured_node = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'preconfigured-node'), 'preconfigured_node', '__httpmyTest_comnsyangmyTest_test_myVer_config_mda_cfg_CTD_ANON_2_httpmyTest_comnsyangmyTest_test_myVer_config_mda_cfgpreconfigured_node', True, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-config-mda-cfg.xsd', 88, 8), )

    
    preconfigured_node = property(__preconfigured_node.value, __preconfigured_node.set, None, u'\n              The configuration for a non-active node\n            ')

    _HasWildcardElement = True
    _ElementMap.update({
        __preconfigured_node.name() : __preconfigured_node
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """
              The configuration for a non-active node
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-config-mda-cfg.xsd', 94, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-config-mda-cfg}node-name uses Python identifier node_name
    __node_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'node-name'), 'node_name', '__httpmyTest_comnsyangmyTest_test_myVer_config_mda_cfg_CTD_ANON_3_httpmyTest_comnsyangmyTest_test_myVer_config_mda_cfgnode_name', False, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-config-mda-cfg.xsd', 96, 14), )

    
    node_name = property(__node_name.value, __node_name.set, None, u'\n                    The identifier for this node\n                  ')

    _HasWildcardElement = True
    _ElementMap.update({
        __node_name.name() : __node_name
    })
    _AttributeMap.update({
        
    })



active_nodes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'active-nodes'), CTD_ANON, documentation=u'\n        Per-node configuration for active nodes\n      ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-config-mda-cfg.xsd', 43, 2))
Namespace.addCategoryObject('elementBinding', active_nodes.name().localName(), active_nodes)

preconfigured_nodes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'preconfigured-nodes'), CTD_ANON_2, documentation=u'\n        preconfigured nodes\n      ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-config-mda-cfg.xsd', 80, 2))
Namespace.addCategoryObject('elementBinding', preconfigured_nodes.name().localName(), preconfigured_nodes)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'active-node'), CTD_ANON_, scope=CTD_ANON, documentation=u'\n              The configuration for an active node\n            ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-config-mda-cfg.xsd', 51, 8)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-config-mda-cfg.xsd', 51, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-config-mda-cfg.xsd', 71, 8))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active-node')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-config-mda-cfg.xsd', 51, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://myTest.com/ns/yang/myTest-test-myVer-config-mda-cfg')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-config-mda-cfg.xsd', 71, 8))
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




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'node-name'), _ImportedBinding__myVer.Node_id, scope=CTD_ANON_, documentation=u'\n                    The identifier for this node\n                  ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-config-mda-cfg.xsd', 59, 14)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-config-mda-cfg.xsd', 66, 14))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'node-name')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-config-mda-cfg.xsd', 59, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://myTest.com/ns/yang/myTest-test-myVer-config-mda-cfg')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-config-mda-cfg.xsd', 66, 14))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'preconfigured-node'), CTD_ANON_3, scope=CTD_ANON_2, documentation=u'\n              The configuration for a non-active node\n            ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-config-mda-cfg.xsd', 88, 8)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-config-mda-cfg.xsd', 88, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-config-mda-cfg.xsd', 108, 8))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'preconfigured-node')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-config-mda-cfg.xsd', 88, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://myTest.com/ns/yang/myTest-test-myVer-config-mda-cfg')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-config-mda-cfg.xsd', 108, 8))
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




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'node-name'), _ImportedBinding__myVer.Node_id, scope=CTD_ANON_3, documentation=u'\n                    The identifier for this node\n                  ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-config-mda-cfg.xsd', 96, 14)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-config-mda-cfg.xsd', 103, 14))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'node-name')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-config-mda-cfg.xsd', 96, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://myTest.com/ns/yang/myTest-test-myVer-config-mda-cfg')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-config-mda-cfg.xsd', 103, 14))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_3()

