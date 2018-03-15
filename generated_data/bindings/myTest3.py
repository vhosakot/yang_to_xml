# .\myTest_test_myVer_aaa_lib_cfg.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:ef0c03cf2b9def40ca419afc84caa28c6581adfb
# Generated 2013-10-23 12:19:12.929000 by PyXB version 1.2.3
# Namespace http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:900216b0-3bcc-11e3-9593-3c970e99f68c')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import _myVer as _ImportedBinding__myVer
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg', create_if_missing=True)
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


# Atomic simple type: {http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg}Aaa-port-range
class Aaa_port_range (pyxb.binding.datatypes.unsignedInt):

    """
        Aaa port range
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Aaa-port-range')
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 43, 2)
    _Documentation = u'\n        Aaa port range\n      '
Aaa_port_range._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=Aaa_port_range, value=pyxb.binding.datatypes.unsignedInt(65535L))
Aaa_port_range._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=Aaa_port_range, value=pyxb.binding.datatypes.unsignedInt(1L))
Aaa_port_range._InitializeFacetMap(Aaa_port_range._CF_maxInclusive,
   Aaa_port_range._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'Aaa-port-range', Aaa_port_range)

# Atomic simple type: {http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg}Aaa-accounting
class Aaa_accounting (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        Aaa accounting
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Aaa-accounting')
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 55, 2)
    _Documentation = u'\n        Aaa accounting\n      '
Aaa_accounting._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Aaa_accounting, enum_prefix=None)
Aaa_accounting.not_set = Aaa_accounting._CF_enumeration.addEnumeration(unicode_value=u'not-set', tag=u'not_set')
Aaa_accounting.start_stop = Aaa_accounting._CF_enumeration.addEnumeration(unicode_value=u'start-stop', tag=u'start_stop')
Aaa_accounting.stop_only = Aaa_accounting._CF_enumeration.addEnumeration(unicode_value=u'stop-only', tag=u'stop_only')
Aaa_accounting._InitializeFacetMap(Aaa_accounting._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'Aaa-accounting', Aaa_accounting)

# Atomic simple type: {http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg}Aaa-method
class Aaa_method (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        Aaa method
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Aaa-method')
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 70, 2)
    _Documentation = u'\n        Aaa method\n      '
Aaa_method._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Aaa_method, enum_prefix=None)
Aaa_method.not_set = Aaa_method._CF_enumeration.addEnumeration(unicode_value=u'not-set', tag=u'not_set')
Aaa_method.none = Aaa_method._CF_enumeration.addEnumeration(unicode_value=u'none', tag=u'none')
Aaa_method.local = Aaa_method._CF_enumeration.addEnumeration(unicode_value=u'local', tag=u'local')
Aaa_method.radius = Aaa_method._CF_enumeration.addEnumeration(unicode_value=u'radius', tag=u'radius')
Aaa_method.tacacs_plus = Aaa_method._CF_enumeration.addEnumeration(unicode_value=u'tacacs-plus', tag=u'tacacs_plus')
Aaa_method.dsmd = Aaa_method._CF_enumeration.addEnumeration(unicode_value=u'dsmd', tag=u'dsmd')
Aaa_method.sgbp = Aaa_method._CF_enumeration.addEnumeration(unicode_value=u'sgbp', tag=u'sgbp')
Aaa_method.acct_d = Aaa_method._CF_enumeration.addEnumeration(unicode_value=u'acct-d', tag=u'acct_d')
Aaa_method.error = Aaa_method._CF_enumeration.addEnumeration(unicode_value=u'error', tag=u'error')
Aaa_method.if_authenticated = Aaa_method._CF_enumeration.addEnumeration(unicode_value=u'if-authenticated', tag=u'if_authenticated')
Aaa_method.server_group = Aaa_method._CF_enumeration.addEnumeration(unicode_value=u'server-group', tag=u'server_group')
Aaa_method.server_group_not_defined = Aaa_method._CF_enumeration.addEnumeration(unicode_value=u'server-group-not-defined', tag=u'server_group_not_defined')
Aaa_method.line = Aaa_method._CF_enumeration.addEnumeration(unicode_value=u'line', tag=u'line')
Aaa_method.enable = Aaa_method._CF_enumeration.addEnumeration(unicode_value=u'enable', tag=u'enable')
Aaa_method.kerberos = Aaa_method._CF_enumeration.addEnumeration(unicode_value=u'kerberos', tag=u'kerberos')
Aaa_method.last = Aaa_method._CF_enumeration.addEnumeration(unicode_value=u'last', tag=u'last')
Aaa_method._InitializeFacetMap(Aaa_method._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'Aaa-method', Aaa_method)

# Atomic simple type: {http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg}Aaa-accounting-update
class Aaa_accounting_update (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        Aaa accounting update
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Aaa-accounting-update')
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 96, 2)
    _Documentation = u'\n        Aaa accounting update\n      '
Aaa_accounting_update._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Aaa_accounting_update, enum_prefix=None)
Aaa_accounting_update.none = Aaa_accounting_update._CF_enumeration.addEnumeration(unicode_value=u'none', tag=u'none')
Aaa_accounting_update.newinfo = Aaa_accounting_update._CF_enumeration.addEnumeration(unicode_value=u'newinfo', tag=u'newinfo')
Aaa_accounting_update.periodic = Aaa_accounting_update._CF_enumeration.addEnumeration(unicode_value=u'periodic', tag=u'periodic')
Aaa_accounting_update._InitializeFacetMap(Aaa_accounting_update._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'Aaa-accounting-update', Aaa_accounting_update)

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.unsignedInt):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 273, 16)
    _Documentation = None
STD_ANON._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON, value=pyxb.binding.datatypes.unsignedInt(35791394L))
STD_ANON._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON, value=pyxb.binding.datatypes.unsignedInt(0L))
STD_ANON._InitializeFacetMap(STD_ANON._CF_maxInclusive,
   STD_ANON._CF_minInclusive)

# Complex type {http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg}Aaa-accounting-rp-failover with content type EMPTY
class Aaa_accounting_rp_failover (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg}Aaa-accounting-rp-failover with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Aaa-accounting-rp-failover')
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 68, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Aaa-accounting-rp-failover', Aaa_accounting_rp_failover)


# Complex type {http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg}Aaa-accounting-broadcast with content type EMPTY
class Aaa_accounting_broadcast (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg}Aaa-accounting-broadcast with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Aaa-accounting-broadcast')
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 69, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Aaa-accounting-broadcast', Aaa_accounting_broadcast)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """
        Authentication, Authorization and Accounting
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 116, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg}accountings uses Python identifier accountings
    __accountings = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'accountings'), 'accountings', '__httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfg_CTD_ANON_httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfgaccountings', False, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 118, 8), )

    
    accountings = property(__accountings.value, __accountings.set, None, u'\n              AAA accounting\n            ')

    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg}authorizations uses Python identifier authorizations
    __authorizations = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'authorizations'), 'authorizations', '__httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfg_CTD_ANON_httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfgauthorizations', False, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 192, 8), )

    
    authorizations = property(__authorizations.value, __authorizations.set, None, u'\n              AAA authorization\n            ')

    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg}accounting-update uses Python identifier accounting_update
    __accounting_update = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'accounting-update'), 'accounting_update', '__httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfg_CTD_ANON_httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfgaccounting_update', False, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 252, 8), )

    
    accounting_update = property(__accounting_update.value, __accounting_update.set, None, u"\n              Configuration related to 'update' accounting\n            ")

    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg}authentications uses Python identifier authentications
    __authentications = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'authentications'), 'authentications', '__httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfg_CTD_ANON_httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfgauthentications', False, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 285, 8), )

    
    authentications = property(__authentications.value, __authentications.set, None, u'\n              AAA authentication\n            ')

    _HasWildcardElement = True
    _ElementMap.update({
        __accountings.name() : __accountings,
        __authorizations.name() : __authorizations,
        __accounting_update.name() : __accounting_update,
        __authentications.name() : __authentications
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """
              AAA accounting
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 124, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg}accounting uses Python identifier accounting
    __accounting = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'accounting'), 'accounting', '__httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfg_CTD_ANON__httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfgaccounting', True, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 126, 14), )

    
    accounting = property(__accounting.value, __accounting.set, None, u'\n                    Configurations related to accounting\n                  ')

    _HasWildcardElement = True
    _ElementMap.update({
        __accounting.name() : __accounting
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """
                    Configurations related to accounting
                  """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 132, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'type'), 'type', '__httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfg_CTD_ANON_2_httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfgtype', False, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 134, 20), )

    
    type = property(__type.value, __type.set, None, u'\n                          exec:Account exec sessions, commands: Account\n                          CLI commands\n                        ')

    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg}listname uses Python identifier listname
    __listname = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'listname'), 'listname', '__httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfg_CTD_ANON_2_httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfglistname', False, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 142, 20), )

    
    listname = property(__listname.value, __listname.set, None, u'\n                          Named accounting list\n                        ')

    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg}rp-failover uses Python identifier rp_failover
    __rp_failover = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'rp-failover'), 'rp_failover', '__httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfg_CTD_ANON_2_httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfgrp_failover', False, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 149, 20), )

    
    rp_failover = property(__rp_failover.value, __rp_failover.set, None, u'\n                          rpfailover\n                        ')

    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg}broadcast uses Python identifier broadcast
    __broadcast = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'broadcast'), 'broadcast', '__httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfg_CTD_ANON_2_httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfgbroadcast', False, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 156, 20), )

    
    broadcast = property(__broadcast.value, __broadcast.set, None, u'\n                          Broadcast\n                        ')

    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg}method uses Python identifier method
    __method = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'method'), 'method', '__httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfg_CTD_ANON_2_httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfgmethod', True, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 163, 20), )

    
    method = property(__method.value, __method.set, None, u'\n                          Method Types\n                        ')

    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg}server-group-name uses Python identifier server_group_name
    __server_group_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'server-group-name'), 'server_group_name', '__httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfg_CTD_ANON_2_httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfgserver_group_name', True, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 170, 20), )

    
    server_group_name = property(__server_group_name.value, __server_group_name.set, None, u'\n                          Server group names\n                        ')

    _HasWildcardElement = True
    _ElementMap.update({
        __type.name() : __type,
        __listname.name() : __listname,
        __rp_failover.name() : __rp_failover,
        __broadcast.name() : __broadcast,
        __method.name() : __method,
        __server_group_name.name() : __server_group_name
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """
              AAA authorization
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 198, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg}authorization uses Python identifier authorization
    __authorization = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'authorization'), 'authorization', '__httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfg_CTD_ANON_3_httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfgauthorization', True, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 200, 14), )

    
    authorization = property(__authorization.value, __authorization.set, None, u'\n                    Configurations related to authorization\n                  ')

    _HasWildcardElement = True
    _ElementMap.update({
        __authorization.name() : __authorization
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """
                    Configurations related to authorization
                  """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 206, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'type'), 'type', '__httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfg_CTD_ANON_4_httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfgtype', False, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 208, 20), )

    
    type = property(__type.value, __type.set, None, u'\n                          network: Authorize IKE requests, commands:\n                          Authorize CLI commands\n                        ')

    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg}listname uses Python identifier listname
    __listname = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'listname'), 'listname', '__httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfg_CTD_ANON_4_httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfglistname', False, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 216, 20), )

    
    listname = property(__listname.value, __listname.set, None, u'\n                          List name for AAA authorization\n                        ')

    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg}method uses Python identifier method
    __method = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'method'), 'method', '__httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfg_CTD_ANON_4_httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfgmethod', True, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 223, 20), )

    
    method = property(__method.value, __method.set, None, u'\n                          Methods\n                        ')

    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg}server-group-name uses Python identifier server_group_name
    __server_group_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'server-group-name'), 'server_group_name', '__httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfg_CTD_ANON_4_httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfgserver_group_name', True, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 230, 20), )

    
    server_group_name = property(__server_group_name.value, __server_group_name.set, None, u'\n                          Server group names\n                        ')

    _HasWildcardElement = True
    _ElementMap.update({
        __type.name() : __type,
        __listname.name() : __listname,
        __method.name() : __method,
        __server_group_name.name() : __server_group_name
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """
              Configuration related to 'update' accounting
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 258, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'type'), 'type', '__httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfg_CTD_ANON_5_httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfgtype', False, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 260, 14), )

    
    type = property(__type.value, __type.set, None, u'\n                    newinfo/periodic\n                  ')

    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg}periodic-interval uses Python identifier periodic_interval
    __periodic_interval = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'periodic-interval'), 'periodic_interval', '__httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfg_CTD_ANON_5_httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfgperiodic_interval', False, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 267, 14), )

    
    periodic_interval = property(__periodic_interval.value, __periodic_interval.set, None, u'\n                    Periodic update interval in minutes\n                  ')

    _HasWildcardElement = True
    _ElementMap.update({
        __type.name() : __type,
        __periodic_interval.name() : __periodic_interval
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """
              AAA authentication
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 291, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg}authentication uses Python identifier authentication
    __authentication = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'authentication'), 'authentication', '__httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfg_CTD_ANON_6_httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfgauthentication', True, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 293, 14), )

    
    authentication = property(__authentication.value, __authentication.set, None, u'\n                    Configurations related to authentication\n                  ')

    _HasWildcardElement = True
    _ElementMap.update({
        __authentication.name() : __authentication
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """
                    Configurations related to authentication
                  """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 299, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'type'), 'type', '__httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfg_CTD_ANON_7_httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfgtype', False, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 301, 20), )

    
    type = property(__type.value, __type.set, None, u'\n                          login: Authenticate login sessions, ppp:\n                          Authenticate ppp sessions\n                        ')

    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg}listname uses Python identifier listname
    __listname = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'listname'), 'listname', '__httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfg_CTD_ANON_7_httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfglistname', False, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 309, 20), )

    
    listname = property(__listname.value, __listname.set, None, u'\n                          List name for AAA authentication\n                        ')

    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg}method uses Python identifier method
    __method = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'method'), 'method', '__httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfg_CTD_ANON_7_httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfgmethod', True, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 316, 20), )

    
    method = property(__method.value, __method.set, None, u'\n                          Methods\n                        ')

    
    # Element {http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg}server-group-name uses Python identifier server_group_name
    __server_group_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'server-group-name'), 'server_group_name', '__httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfg_CTD_ANON_7_httpmyTest_comnsyangmyTest_test_myVer_aaa_lib_cfgserver_group_name', True, pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 323, 20), )

    
    server_group_name = property(__server_group_name.value, __server_group_name.set, None, u'\n                          Server group names\n                        ')

    _HasWildcardElement = True
    _ElementMap.update({
        __type.name() : __type,
        __listname.name() : __listname,
        __method.name() : __method,
        __server_group_name.name() : __server_group_name
    })
    _AttributeMap.update({
        
    })



aaa = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'aaa'), CTD_ANON, documentation=u'\n        Authentication, Authorization and Accounting\n      ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 110, 2))
Namespace.addCategoryObject('elementBinding', aaa.name().localName(), aaa)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accountings'), CTD_ANON_, scope=CTD_ANON, documentation=u'\n              AAA accounting\n            ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 118, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'authorizations'), CTD_ANON_3, scope=CTD_ANON, documentation=u'\n              AAA authorization\n            ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 192, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accounting-update'), CTD_ANON_5, scope=CTD_ANON, documentation=u"\n              Configuration related to 'update' accounting\n            ", location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 252, 8)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'authentications'), CTD_ANON_6, scope=CTD_ANON, documentation=u'\n              AAA authentication\n            ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 285, 8)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 118, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 192, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 252, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 285, 8))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 345, 8))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accountings')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 118, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'authorizations')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 192, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accounting-update')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 252, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'authentications')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 285, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 345, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accounting'), CTD_ANON_2, scope=CTD_ANON_, documentation=u'\n                    Configurations related to accounting\n                  ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 126, 14)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 126, 14))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 182, 14))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accounting')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 126, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 182, 14))
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




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'type'), _ImportedBinding__myVer.myTest_test_myVer_string, scope=CTD_ANON_2, documentation=u'\n                          exec:Account exec sessions, commands: Account\n                          CLI commands\n                        ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 134, 20)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'listname'), _ImportedBinding__myVer.myTest_test_myVer_string, scope=CTD_ANON_2, documentation=u'\n                          Named accounting list\n                        ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 142, 20)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'rp-failover'), Aaa_accounting_rp_failover, scope=CTD_ANON_2, documentation=u'\n                          rpfailover\n                        ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 149, 20)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'broadcast'), Aaa_accounting_broadcast, scope=CTD_ANON_2, documentation=u'\n                          Broadcast\n                        ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 156, 20)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'method'), Aaa_method, scope=CTD_ANON_2, documentation=u'\n                          Method Types\n                        ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 163, 20)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'server-group-name'), _ImportedBinding__myVer.myTest_test_myVer_string, scope=CTD_ANON_2, documentation=u'\n                          Server group names\n                        ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 170, 20)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 149, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 156, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=1L, max=4L, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 163, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=1L, max=4L, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 170, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 177, 20))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'type')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 134, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'listname')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 142, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'rp-failover')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 149, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'broadcast')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 156, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'method')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 163, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'server-group-name')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 170, 20))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 177, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'authorization'), CTD_ANON_4, scope=CTD_ANON_3, documentation=u'\n                    Configurations related to authorization\n                  ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 200, 14)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 200, 14))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 242, 14))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'authorization')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 200, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 242, 14))
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




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'type'), _ImportedBinding__myVer.myTest_test_myVer_string, scope=CTD_ANON_4, documentation=u'\n                          network: Authorize IKE requests, commands:\n                          Authorize CLI commands\n                        ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 208, 20)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'listname'), _ImportedBinding__myVer.myTest_test_myVer_string, scope=CTD_ANON_4, documentation=u'\n                          List name for AAA authorization\n                        ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 216, 20)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'method'), Aaa_method, scope=CTD_ANON_4, documentation=u'\n                          Methods\n                        ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 223, 20)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'server-group-name'), _ImportedBinding__myVer.myTest_test_myVer_string, scope=CTD_ANON_4, documentation=u'\n                          Server group names\n                        ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 230, 20)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1L, max=4L, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 223, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=1L, max=4L, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 230, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 237, 20))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'type')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 208, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'listname')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 216, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'method')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 223, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'server-group-name')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 230, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 237, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
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
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_4()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'type'), Aaa_accounting_update, scope=CTD_ANON_5, documentation=u'\n                    newinfo/periodic\n                  ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 260, 14)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'periodic-interval'), STD_ANON, scope=CTD_ANON_5, documentation=u'\n                    Periodic update interval in minutes\n                  ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 267, 14)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 267, 14))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 280, 14))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'type')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 260, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'periodic-interval')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 267, 14))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 280, 14))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
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
CTD_ANON_5._Automaton = _BuildAutomaton_5()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'authentication'), CTD_ANON_7, scope=CTD_ANON_6, documentation=u'\n                    Configurations related to authentication\n                  ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 293, 14)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 293, 14))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 335, 14))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'authentication')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 293, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 335, 14))
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
CTD_ANON_6._Automaton = _BuildAutomaton_6()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'type'), _ImportedBinding__myVer.myTest_test_myVer_string, scope=CTD_ANON_7, documentation=u'\n                          login: Authenticate login sessions, ppp:\n                          Authenticate ppp sessions\n                        ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 301, 20)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'listname'), _ImportedBinding__myVer.myTest_test_myVer_string, scope=CTD_ANON_7, documentation=u'\n                          List name for AAA authentication\n                        ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 309, 20)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'method'), Aaa_method, scope=CTD_ANON_7, documentation=u'\n                          Methods\n                        ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 316, 20)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'server-group-name'), _ImportedBinding__myVer.myTest_test_myVer_string, scope=CTD_ANON_7, documentation=u'\n                          Server group names\n                        ', location=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 323, 20)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1L, max=4L, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 316, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=1L, max=4L, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 323, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 330, 20))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'type')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 301, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'listname')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 309, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'method')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 316, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'server-group-name')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 323, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://myTest.com/ns/yang/myTest-test-myVer-aaa-lib-cfg')), pyxb.utils.utility.Location('c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-aaa-lib-cfg.xsd', 330, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
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
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_7()

