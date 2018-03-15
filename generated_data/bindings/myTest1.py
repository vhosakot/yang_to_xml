# .\myTest_test_myVer_ip_domain_cfg.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:deca0eef03249a3819bb87df2d2a8ac646fe003e
# Generated 2013-10-30 10:34:25.454000 by PyXB version 1.2.3
# Namespace http://myTest.com/ns/yang/myTest-test-myVer-ip-domain-cfg

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:771703c0-4146-11e3-8334-3c970e99f68c')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import _myVer as _ImportedBinding__myVer
import _inet as _ImportedBinding__inet
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://myTest.com/ns/yang/myTest-test-myVer-ip-domain-cfg', create_if_missing=True)
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
        IP domain configuration
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 51, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-ip-domain-cfg}vrfs uses Python identifier vrfs
    __vrfs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'vrfs'), 'vrfs', '__httpmyTest_comnsyangmyTest_test_myVer_ip_domain_cfg_CTD_ANON_httpmyTest_comnsyangmyTest_test_myVer_ip_domain_cfgvrfs', False, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 53, 8), )

    
    vrfs = property(__vrfs.value, __vrfs.set, None, u'\n              VRF table\n            ')

    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-ip-domain-cfg}ipv6-host-table uses Python identifier ipv6_host_table
    __ipv6_host_table = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ipv6-host-table'), 'ipv6_host_table', '__httpmyTest_comnsyangmyTest_test_myVer_ip_domain_cfg_CTD_ANON_httpmyTest_comnsyangmyTest_test_myVer_ip_domain_cfgipv6_host_table', False, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 201, 8), )

    
    ipv6_host_table = property(__ipv6_host_table.value, __ipv6_host_table.set, None, u'\n              IPv6 host\n            ')

    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-ip-domain-cfg}ipv4-host-table uses Python identifier ipv4_host_table
    __ipv4_host_table = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ipv4-host-table'), 'ipv4_host_table', '__httpmyTest_comnsyangmyTest_test_myVer_ip_domain_cfg_CTD_ANON_httpmyTest_comnsyangmyTest_test_myVer_ip_domain_cfgipv4_host_table', False, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 209, 8), )

    
    ipv4_host_table = property(__ipv4_host_table.value, __ipv4_host_table.set, None, u'\n              IPv4 host\n            ')

    _HasWildcardElement = True
    _ElementMap.update({
        __vrfs.name() : __vrfs,
        __ipv6_host_table.name() : __ipv6_host_table,
        __ipv4_host_table.name() : __ipv4_host_table
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """
              VRF table
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 59, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-ip-domain-cfg}vrf uses Python identifier vrf
    __vrf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'vrf'), 'vrf', '__httpmyTest_comnsyangmyTest_test_myVer_ip_domain_cfg_CTD_ANON__httpmyTest_comnsyangmyTest_test_myVer_ip_domain_cfgvrf', True, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 61, 14), )

    
    vrf = property(__vrf.value, __vrf.set, None, u'\n                    VRF specific data\n                  ')

    _HasWildcardElement = True
    _ElementMap.update({
        __vrf.name() : __vrf
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """
                    VRF specific data
                  """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 67, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-ip-domain-cfg}vrf-name uses Python identifier vrf_name
    __vrf_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'vrf-name'), 'vrf_name', '__httpmyTest_comnsyangmyTest_test_myVer_ip_domain_cfg_CTD_ANON_2_httpmyTest_comnsyangmyTest_test_myVer_ip_domain_cfgvrf_name', False, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 69, 20), )

    
    vrf_name = property(__vrf_name.value, __vrf_name.set, None, u'\n                          Name of the VRF instance\n                        ')

    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-ip-domain-cfg}ipv6-hosts uses Python identifier ipv6_hosts
    __ipv6_hosts = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ipv6-hosts'), 'ipv6_hosts', '__httpmyTest_comnsyangmyTest_test_myVer_ip_domain_cfg_CTD_ANON_2_httpmyTest_comnsyangmyTest_test_myVer_ip_domain_cfgipv6_hosts', False, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 76, 20), )

    
    ipv6_hosts = property(__ipv6_hosts.value, __ipv6_hosts.set, None, u'\n                          IPv6 host\n                        ')

    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-ip-domain-cfg}lookup uses Python identifier lookup
    __lookup = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'lookup'), 'lookup', '__httpmyTest_comnsyangmyTest_test_myVer_ip_domain_cfg_CTD_ANON_2_httpmyTest_comnsyangmyTest_test_myVer_ip_domain_cfglookup', False, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 120, 20), )

    
    lookup = property(__lookup.value, __lookup.set, None, u'\n                          Disable Domain Name System hostname\n                          translation\n                        ')

    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-ip-domain-cfg}source-interface uses Python identifier source_interface
    __source_interface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'source-interface'), 'source_interface', '__httpmyTest_comnsyangmyTest_test_myVer_ip_domain_cfg_CTD_ANON_2_httpmyTest_comnsyangmyTest_test_myVer_ip_domain_cfgsource_interface', False, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 129, 20), )

    
    source_interface = property(__source_interface.value, __source_interface.set, None, u'\n                          Interface name\n                        ')

    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-ip-domain-cfg}ipv4-hosts uses Python identifier ipv4_hosts
    __ipv4_hosts = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ipv4-hosts'), 'ipv4_hosts', '__httpmyTest_comnsyangmyTest_test_myVer_ip_domain_cfg_CTD_ANON_2_httpmyTest_comnsyangmyTest_test_myVer_ip_domain_cfgipv4_hosts', False, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 136, 20), )

    
    ipv4_hosts = property(__ipv4_hosts.value, __ipv4_hosts.set, None, u'\n                          IPv4 host\n                        ')

    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-ip-domain-cfg}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'name'), 'name', '__httpmyTest_comnsyangmyTest_test_myVer_ip_domain_cfg_CTD_ANON_2_httpmyTest_comnsyangmyTest_test_myVer_ip_domain_cfgname', False, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 180, 20), )

    
    name = property(__name.value, __name.set, None, u'\n                          Default domain name\n                        ')

    _HasWildcardElement = True
    _ElementMap.update({
        __vrf_name.name() : __vrf_name,
        __ipv6_hosts.name() : __ipv6_hosts,
        __lookup.name() : __lookup,
        __source_interface.name() : __source_interface,
        __ipv4_hosts.name() : __ipv4_hosts,
        __name.name() : __name
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """
                          IPv6 host
                        """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 82, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-ip-domain-cfg}ipv6-host uses Python identifier ipv6_host
    __ipv6_host = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ipv6-host'), 'ipv6_host', '__httpmyTest_comnsyangmyTest_test_myVer_ip_domain_cfg_CTD_ANON_3_httpmyTest_comnsyangmyTest_test_myVer_ip_domain_cfgipv6_host', True, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 84, 26), )

    
    ipv6_host = property(__ipv6_host.value, __ipv6_host.set, None, u'\n                                Host name and up to 4 host IPv6 addresses\n                              ')

    _HasWildcardElement = True
    _ElementMap.update({
        __ipv6_host.name() : __ipv6_host
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """
                                Host name and up to 4 host IPv6 addresses
                              """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 90, 28)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-ip-domain-cfg}host-name uses Python identifier host_name
    __host_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'host-name'), 'host_name', '__httpmyTest_comnsyangmyTest_test_myVer_ip_domain_cfg_CTD_ANON_4_httpmyTest_comnsyangmyTest_test_myVer_ip_domain_cfghost_name', False, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 92, 32), )

    
    host_name = property(__host_name.value, __host_name.set, None, u'\n                                      A hostname\n                                    ')

    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-ip-domain-cfg}address uses Python identifier address
    __address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'address'), 'address', '__httpmyTest_comnsyangmyTest_test_myVer_ip_domain_cfg_CTD_ANON_4_httpmyTest_comnsyangmyTest_test_myVer_ip_domain_cfgaddress', True, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 99, 32), )

    
    address = property(__address.value, __address.set, None, u'\n                                      Host IPv6 addresses\n                                    ')

    _HasWildcardElement = True
    _ElementMap.update({
        __host_name.name() : __host_name,
        __address.name() : __address
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """
                          Disable Domain Name System hostname
                          translation
                        """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 127, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """
                          IPv4 host
                        """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 142, 22)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-ip-domain-cfg}ipv4-host uses Python identifier ipv4_host
    __ipv4_host = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ipv4-host'), 'ipv4_host', '__httpmyTest_comnsyangmyTest_test_myVer_ip_domain_cfg_CTD_ANON_6_httpmyTest_comnsyangmyTest_test_myVer_ip_domain_cfgipv4_host', True, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 144, 26), )

    
    ipv4_host = property(__ipv4_host.value, __ipv4_host.set, None, u'\n                                Host name and up to 8 host IPv4 addresses\n                              ')

    _HasWildcardElement = True
    _ElementMap.update({
        __ipv4_host.name() : __ipv4_host
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """
                                Host name and up to 8 host IPv4 addresses
                              """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 150, 28)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-ip-domain-cfg}host-name uses Python identifier host_name
    __host_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'host-name'), 'host_name', '__httpmyTest_comnsyangmyTest_test_myVer_ip_domain_cfg_CTD_ANON_7_httpmyTest_comnsyangmyTest_test_myVer_ip_domain_cfghost_name', False, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 152, 32), )

    
    host_name = property(__host_name.value, __host_name.set, None, u'\n                                      A hostname\n                                    ')

    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-ip-domain-cfg}address uses Python identifier address
    __address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'address'), 'address', '__httpmyTest_comnsyangmyTest_test_myVer_ip_domain_cfg_CTD_ANON_7_httpmyTest_comnsyangmyTest_test_myVer_ip_domain_cfgaddress', True, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 159, 32), )

    
    address = property(__address.value, __address.set, None, u'\n                                      Host IPv4 addresses\n                                    ')

    _HasWildcardElement = True
    _ElementMap.update({
        __host_name.name() : __host_name,
        __address.name() : __address
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """
              IPv6 host
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 207, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """
              IPv4 host
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 215, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })



ip_domain = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ip-domain'), CTD_ANON, documentation=u'\n        IP domain configuration\n      ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 45, 2))
Namespace.addCategoryObject('elementBinding', ip_domain.name().localName(), ip_domain)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'vrfs'), CTD_ANON_, scope=CTD_ANON, documentation=u'\n              VRF table\n            ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 53, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ipv6-host-table'), CTD_ANON_8, scope=CTD_ANON, documentation=u'\n              IPv6 host\n            ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 201, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ipv4-host-table'), CTD_ANON_9, scope=CTD_ANON, documentation=u'\n              IPv4 host\n            ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 209, 8)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 53, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 201, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 209, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 218, 8))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'vrfs')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 53, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ipv6-host-table')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 201, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ipv4-host-table')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 209, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://myTest.com/ns/yang/myTest-test-myVer-ip-domain-cfg')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 218, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'vrf'), CTD_ANON_2, scope=CTD_ANON_, documentation=u'\n                    VRF specific data\n                  ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 61, 14)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 61, 14))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 192, 14))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'vrf')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 61, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://myTest.com/ns/yang/myTest-test-myVer-ip-domain-cfg')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 192, 14))
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




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'vrf-name'), _ImportedBinding__myVer.myTest_test_myVer_string, scope=CTD_ANON_2, documentation=u'\n                          Name of the VRF instance\n                        ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 69, 20)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ipv6-hosts'), CTD_ANON_3, scope=CTD_ANON_2, documentation=u'\n                          IPv6 host\n                        ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 76, 20)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'lookup'), CTD_ANON_5, scope=CTD_ANON_2, documentation=u'\n                          Disable Domain Name System hostname\n                          translation\n                        ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 120, 20)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'source-interface'), _ImportedBinding__myVer.Interface_name, scope=CTD_ANON_2, documentation=u'\n                          Interface name\n                        ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 129, 20)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ipv4-hosts'), CTD_ANON_6, scope=CTD_ANON_2, documentation=u'\n                          IPv4 host\n                        ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 136, 20)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), _ImportedBinding__myVer.myTest_test_myVer_string, scope=CTD_ANON_2, documentation=u'\n                          Default domain name\n                        ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 180, 20)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 76, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 120, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 129, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 136, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 180, 20))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 187, 20))
    counters.add(cc_5)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'vrf-name')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 69, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ipv6-hosts')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 76, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'lookup')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 120, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'source-interface')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 129, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ipv4-hosts')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 136, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'name')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 180, 20))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://myTest.com/ns/yang/myTest-test-myVer-ip-domain-cfg')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 187, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ipv6-host'), CTD_ANON_4, scope=CTD_ANON_3, documentation=u'\n                                Host name and up to 4 host IPv6 addresses\n                              ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 84, 26)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 84, 26))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 111, 26))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ipv6-host')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 84, 26))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://myTest.com/ns/yang/myTest-test-myVer-ip-domain-cfg')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 111, 26))
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
CTD_ANON_3._Automaton = _BuildAutomaton_3()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'host-name'), pyxb.binding.datatypes.string, scope=CTD_ANON_4, documentation=u'\n                                      A hostname\n                                    ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 92, 32)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'address'), _ImportedBinding__inet.ipv6_address, scope=CTD_ANON_4, documentation=u'\n                                      Host IPv6 addresses\n                                    ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 99, 32)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1L, max=4L, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 99, 32))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 106, 32))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'host-name')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 92, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'address')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 99, 32))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://myTest.com/ns/yang/myTest-test-myVer-ip-domain-cfg')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 106, 32))
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
CTD_ANON_4._Automaton = _BuildAutomaton_4()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ipv4-host'), CTD_ANON_7, scope=CTD_ANON_6, documentation=u'\n                                Host name and up to 8 host IPv4 addresses\n                              ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 144, 26)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 144, 26))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 171, 26))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ipv4-host')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 144, 26))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://myTest.com/ns/yang/myTest-test-myVer-ip-domain-cfg')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 171, 26))
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
CTD_ANON_6._Automaton = _BuildAutomaton_5()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'host-name'), pyxb.binding.datatypes.string, scope=CTD_ANON_7, documentation=u'\n                                      A hostname\n                                    ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 152, 32)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'address'), _ImportedBinding__inet.ipv4_address, scope=CTD_ANON_7, documentation=u'\n                                      Host IPv4 addresses\n                                    ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 159, 32)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1L, max=8L, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 159, 32))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 166, 32))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'host-name')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 152, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'address')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 159, 32))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://myTest.com/ns/yang/myTest-test-myVer-ip-domain-cfg')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-ip-domain-cfg.xsd', 166, 32))
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
CTD_ANON_7._Automaton = _BuildAutomaton_6()

