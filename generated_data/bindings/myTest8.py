# .\_myVer.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:3f7da95b9403b91b8711528bc3f7ed0745e7a010
# Generated 2013-10-30 10:34:25.451000 by PyXB version 1.2.3
# Namespace http://myTest.com/ns/yang/myTest-myVer-types [xmlns:myVer]

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
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://myTest.com/ns/yang/myTest-myVer-types', create_if_missing=True)
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


# Atomic simple type: {http://myTest.com/ns/yang/myTest-myVer-types}Route-dist
class Route_dist (pyxb.binding.datatypes.string):

    """
        Route distinguisher in hexadecimal notation.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Route-dist')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-types.xsd', 35, 2)
    _Documentation = u'\n        Route distinguisher in hexadecimal notation.\n      '
Route_dist._CF_pattern = pyxb.binding.facets.CF_pattern()
Route_dist._CF_pattern.addPattern(pattern=u'[a-fA-F0-9]{8}')
Route_dist._InitializeFacetMap(Route_dist._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Route-dist', Route_dist)

# Atomic simple type: {http://myTest.com/ns/yang/myTest-myVer-types}Bgp-l2vpn-evpn-addrs
class Bgp_l2vpn_evpn_addrs (pyxb.binding.datatypes.string):

    """
        L2VPN EVPN Address in hexadecimal notation.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Bgp-l2vpn-evpn-addrs')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-types.xsd', 46, 2)
    _Documentation = u'\n        L2VPN EVPN Address in hexadecimal notation.\n      '
Bgp_l2vpn_evpn_addrs._CF_pattern = pyxb.binding.facets.CF_pattern()
Bgp_l2vpn_evpn_addrs._CF_pattern.addPattern(pattern=u'[a-fA-F0-9]{29}')
Bgp_l2vpn_evpn_addrs._InitializeFacetMap(Bgp_l2vpn_evpn_addrs._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Bgp-l2vpn-evpn-addrs', Bgp_l2vpn_evpn_addrs)

# Atomic simple type: {http://myTest.com/ns/yang/myTest-myVer-types}Bgp-ls-addr
class Bgp_ls_addr (pyxb.binding.datatypes.string):

    """
        BGP link state unicast address in hexadecimal
        notation.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Bgp-ls-addr')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-types.xsd', 57, 2)
    _Documentation = u'\n        BGP link state unicast address in hexadecimal\n        notation.\n      '
Bgp_ls_addr._CF_pattern = pyxb.binding.facets.CF_pattern()
Bgp_ls_addr._CF_pattern.addPattern(pattern=u'[a-fA-F0-9]{1000}')
Bgp_ls_addr._InitializeFacetMap(Bgp_ls_addr._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Bgp-ls-addr', Bgp_ls_addr)

# Atomic simple type: {http://myTest.com/ns/yang/myTest-myVer-types}Bgp-ipv6-mvpn-addr
class Bgp_ipv6_mvpn_addr (pyxb.binding.datatypes.string):

    """
        An IPV6 MVPN address in decimal notation.
        An IPv6 MVPN address should be of the form 
        [x:x:x:x].
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Bgp-ipv6-mvpn-addr')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-types.xsd', 69, 2)
    _Documentation = u'\n        An IPV6 MVPN address in decimal notation.\n        An IPv6 MVPN address should be of the form \n        [x:x:x:x].\n      '
Bgp_ipv6_mvpn_addr._CF_pattern = pyxb.binding.facets.CF_pattern()
Bgp_ipv6_mvpn_addr._CF_pattern.addPattern(pattern=u'(([0-9]{10}):([0-9]{5}):(((([1-9]?[0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([1-9]?[0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))|([0-9]{10})):([0-9]{10}))')
Bgp_ipv6_mvpn_addr._InitializeFacetMap(Bgp_ipv6_mvpn_addr._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Bgp-ipv6-mvpn-addr', Bgp_ipv6_mvpn_addr)

# Atomic simple type: {http://myTest.com/ns/yang/myTest-myVer-types}Bgp-ipv4-mvpn-addr
class Bgp_ipv4_mvpn_addr (pyxb.binding.datatypes.string):

    """
        An IPV4 MVPN address in decimal notation.
        An IPv4 MVPN address should be of the form
        [x:x:x:x].
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Bgp-ipv4-mvpn-addr')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-types.xsd', 82, 2)
    _Documentation = u'\n        An IPV4 MVPN address in decimal notation.\n        An IPv4 MVPN address should be of the form\n        [x:x:x:x].\n      '
Bgp_ipv4_mvpn_addr._CF_pattern = pyxb.binding.facets.CF_pattern()
Bgp_ipv4_mvpn_addr._CF_pattern.addPattern(pattern=u'(([0-9]{10}):([0-9]{5}):(((([1-9]?[0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([1-9]?[0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))|([0-9]{10})):([0-9]{10}))')
Bgp_ipv4_mvpn_addr._InitializeFacetMap(Bgp_ipv4_mvpn_addr._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Bgp-ipv4-mvpn-addr', Bgp_ipv4_mvpn_addr)

# Atomic simple type: {http://myTest.com/ns/yang/myTest-myVer-types}Bgp-rt-constrt-addr
class Bgp_rt_constrt_addr (pyxb.binding.datatypes.string):

    """
        An IPV4 RTConstraint address in decimal notation.
        An IPv4 RT Constraint address should be of the form 
        a:b:c:d or x:y:a.b.c.d:z
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Bgp-rt-constrt-addr')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-types.xsd', 95, 2)
    _Documentation = u'\n        An IPV4 RTConstraint address in decimal notation.\n        An IPv4 RT Constraint address should be of the form \n        a:b:c:d or x:y:a.b.c.d:z\n      '
Bgp_rt_constrt_addr._CF_pattern = pyxb.binding.facets.CF_pattern()
Bgp_rt_constrt_addr._CF_pattern.addPattern(pattern=u'(([0-9]{10}):([0-9]{5}):(((([1-9]?[0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([1-9]?[0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))|([0-9]{10})):([0-9]{10}))')
Bgp_rt_constrt_addr._InitializeFacetMap(Bgp_rt_constrt_addr._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Bgp-rt-constrt-addr', Bgp_rt_constrt_addr)

# Atomic simple type: {http://myTest.com/ns/yang/myTest-myVer-types}Bgp-ipv4-mdt-addr
class Bgp_ipv4_mdt_addr (pyxb.binding.datatypes.string):

    """
        An IPV4 MDT address in dotted decimal notation.
        An IPv4 MDT address should be of the form 
        0000006400000065-129.29.83.45. This datatype 
        restricts the value of each field 16 digits in 
        hexadecimal for RD field and between 0 and 255
        for IPv4 address field, i.e. 
        [0000000000000000-ffffffffffffffff]-
        [0-255].[0-255].[0-255].[0-255].
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Bgp-ipv4-mdt-addr')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-types.xsd', 108, 2)
    _Documentation = u'\n        An IPV4 MDT address in dotted decimal notation.\n        An IPv4 MDT address should be of the form \n        0000006400000065-129.29.83.45. This datatype \n        restricts the value of each field 16 digits in \n        hexadecimal for RD field and between 0 and 255\n        for IPv4 address field, i.e. \n        [0000000000000000-ffffffffffffffff]-\n        [0-255].[0-255].[0-255].[0-255].\n      '
Bgp_ipv4_mdt_addr._CF_pattern = pyxb.binding.facets.CF_pattern()
Bgp_ipv4_mdt_addr._CF_pattern.addPattern(pattern=u'(([a-f0-9]{16}-)(([1-9]?[0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([1-9]?[0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))')
Bgp_ipv4_mdt_addr._InitializeFacetMap(Bgp_ipv4_mdt_addr._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Bgp-ipv4-mdt-addr', Bgp_ipv4_mdt_addr)

# Atomic simple type: {http://myTest.com/ns/yang/myTest-myVer-types}Bgp-ipv4-tunnel-addr
class Bgp_ipv4_tunnel_addr (pyxb.binding.datatypes.string):

    """
        An IPV4 tunnel address in dotted decimal notation.
        An IPv4 tunnel address should be of the form 
        65535:129.29.83.45. This datatype restricts the 
        value of each field between 0 and 65535 for prefix
        field and 0 and 255 for IPv4 address field, i.e.
        [0-65535]:[0-255].[0-255].[0-255].[0-255]
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Bgp-ipv4-tunnel-addr')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-types.xsd', 126, 2)
    _Documentation = u'\n        An IPV4 tunnel address in dotted decimal notation.\n        An IPv4 tunnel address should be of the form \n        65535:129.29.83.45. This datatype restricts the \n        value of each field between 0 and 65535 for prefix\n        field and 0 and 255 for IPv4 address field, i.e.\n        [0-65535]:[0-255].[0-255].[0-255].[0-255]\n      '
Bgp_ipv4_tunnel_addr._CF_pattern = pyxb.binding.facets.CF_pattern()
Bgp_ipv4_tunnel_addr._CF_pattern.addPattern(pattern=u'((0:|[1-9][0-9]{0,4}:)(([1-9]?[0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([1-9]?[0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))')
Bgp_ipv4_tunnel_addr._InitializeFacetMap(Bgp_ipv4_tunnel_addr._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Bgp-ipv4-tunnel-addr', Bgp_ipv4_tunnel_addr)

# Atomic simple type: {http://myTest.com/ns/yang/myTest-myVer-types}myTest-test-myVer-port-number
class myTest_test_myVer_port_number (pyxb.binding.datatypes.unsignedShort):

    """
        Port number of range from 1 to 65535
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'myTest-test-myVer-port-number')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-types.xsd', 142, 2)
    _Documentation = u'\n        Port number of range from 1 to 65535\n      '
myTest_test_myVer_port_number._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=myTest_test_myVer_port_number, value=pyxb.binding.datatypes.unsignedShort(65535L))
myTest_test_myVer_port_number._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=myTest_test_myVer_port_number, value=pyxb.binding.datatypes.unsignedShort(1L))
myTest_test_myVer_port_number._InitializeFacetMap(myTest_test_myVer_port_number._CF_maxInclusive,
   myTest_test_myVer_port_number._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'myTest-test-myVer-port-number', myTest_test_myVer_port_number)

# Atomic simple type: {http://myTest.com/ns/yang/myTest-myVer-types}Interface-name
class Interface_name (pyxb.binding.datatypes.string):

    """
        An interface name specifying an interface type and 
        instance.
        Interface represents a string defining an interface
        type and instance, e.g. MgmtEth0/4/CPU1/0
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Interface-name')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-types.xsd', 154, 2)
    _Documentation = u'\n        An interface name specifying an interface type and \n        instance.\n        Interface represents a string defining an interface\n        type and instance, e.g. MgmtEth0/4/CPU1/0\n      '
Interface_name._CF_pattern = pyxb.binding.facets.CF_pattern()
Interface_name._CF_pattern.addPattern(pattern=u'(\\w*\\d+/){3}\\d+')
Interface_name._InitializeFacetMap(Interface_name._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Interface-name', Interface_name)

# Atomic simple type: {http://myTest.com/ns/yang/myTest-myVer-types}myTest-test-myVer-string
class myTest_test_myVer_string (pyxb.binding.datatypes.string):

    """
        Special characters are not allowed.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'myTest-test-myVer-string')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-types.xsd', 168, 2)
    _Documentation = u'\n        Special characters are not allowed.\n      '
myTest_test_myVer_string._CF_pattern = pyxb.binding.facets.CF_pattern()
myTest_test_myVer_string._CF_pattern.addPattern(pattern=u'[\\w\\-]+')
myTest_test_myVer_string._InitializeFacetMap(myTest_test_myVer_string._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'myTest-test-myVer-string', myTest_test_myVer_string)

# Atomic simple type: {http://myTest.com/ns/yang/myTest-myVer-types}Ipv4-prefix-length
class Ipv4_prefix_length (pyxb.binding.datatypes.unsignedByte):

    """
        An IPv4 address prefix length. 
        Must lie between 0 and 32 inclusive.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Ipv4-prefix-length')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-types.xsd', 179, 2)
    _Documentation = u'\n        An IPv4 address prefix length. \n        Must lie between 0 and 32 inclusive.\n      '
Ipv4_prefix_length._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=Ipv4_prefix_length, value=pyxb.binding.datatypes.unsignedByte(32L))
Ipv4_prefix_length._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=Ipv4_prefix_length, value=pyxb.binding.datatypes.unsignedByte(0L))
Ipv4_prefix_length._InitializeFacetMap(Ipv4_prefix_length._CF_maxInclusive,
   Ipv4_prefix_length._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'Ipv4-prefix-length', Ipv4_prefix_length)

# Atomic simple type: {http://myTest.com/ns/yang/myTest-myVer-types}Ipv6-prefix-length
class Ipv6_prefix_length (pyxb.binding.datatypes.unsignedByte):

    """
        An IPv6 address prefix length. 
        Must lie between 0 and 32 inclusive.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Ipv6-prefix-length')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-types.xsd', 192, 2)
    _Documentation = u'\n        An IPv6 address prefix length. \n        Must lie between 0 and 32 inclusive.\n      '
Ipv6_prefix_length._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=Ipv6_prefix_length, value=pyxb.binding.datatypes.unsignedByte(128L))
Ipv6_prefix_length._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=Ipv6_prefix_length, value=pyxb.binding.datatypes.unsignedByte(0L))
Ipv6_prefix_length._InitializeFacetMap(Ipv6_prefix_length._CF_maxInclusive,
   Ipv6_prefix_length._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'Ipv6-prefix-length', Ipv6_prefix_length)

# Atomic simple type: {http://myTest.com/ns/yang/myTest-myVer-types}Rack-id
class Rack_id (pyxb.binding.datatypes.string):

    """
        Names the rack portion of a NodeID 
        Rack/Slot/Instance triple
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Rack-id')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-types.xsd', 205, 2)
    _Documentation = u'\n        Names the rack portion of a NodeID \n        Rack/Slot/Instance triple\n      '
Rack_id._CF_pattern = pyxb.binding.facets.CF_pattern()
Rack_id._CF_pattern.addPattern(pattern=u'\\w*\\d+')
Rack_id._InitializeFacetMap(Rack_id._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Rack-id', Rack_id)

# Atomic simple type: {http://myTest.com/ns/yang/myTest-myVer-types}Slot-id
class Slot_id (pyxb.binding.datatypes.string):

    """
        Names the slot portion of a NodeID 
        Rack/Slot/Instance triple
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Slot-id')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-types.xsd', 217, 2)
    _Documentation = u'\n        Names the slot portion of a NodeID \n        Rack/Slot/Instance triple\n      '
Slot_id._CF_pattern = pyxb.binding.facets.CF_pattern()
Slot_id._CF_pattern.addPattern(pattern=u'\\w*\\d+')
Slot_id._InitializeFacetMap(Slot_id._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Slot-id', Slot_id)

# Atomic simple type: {http://myTest.com/ns/yang/myTest-myVer-types}Instance-id
class Instance_id (pyxb.binding.datatypes.string):

    """
        Names the instance portion of a NodeID 
        Rack/Slot/Instance triple
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Instance-id')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-types.xsd', 229, 2)
    _Documentation = u'\n        Names the instance portion of a NodeID \n        Rack/Slot/Instance triple\n      '
Instance_id._CF_pattern = pyxb.binding.facets.CF_pattern()
Instance_id._CF_pattern.addPattern(pattern=u'\\w*\\d+')
Instance_id._InitializeFacetMap(Instance_id._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Instance-id', Instance_id)

# Atomic simple type: {http://myTest.com/ns/yang/myTest-myVer-types}Sub-instance-id
class Sub_instance_id (pyxb.binding.datatypes.string):

    """
        Names the sub-instance portion of an extended
        NodeID Rack/Slot/Instance/SubInstance
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Sub-instance-id')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-types.xsd', 241, 2)
    _Documentation = u'\n        Names the sub-instance portion of an extended\n        NodeID Rack/Slot/Instance/SubInstance\n      '
Sub_instance_id._CF_pattern = pyxb.binding.facets.CF_pattern()
Sub_instance_id._CF_pattern.addPattern(pattern=u'\\w*\\d+')
Sub_instance_id._InitializeFacetMap(Sub_instance_id._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Sub-instance-id', Sub_instance_id)

# Atomic simple type: {http://myTest.com/ns/yang/myTest-myVer-types}Encryption-type
class Encryption_type (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        The type of encryption used on a password string.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Encryption-type')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-types.xsd', 253, 2)
    _Documentation = u'\n        The type of encryption used on a password string.\n      '
Encryption_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Encryption_type, enum_prefix=None)
Encryption_type.none = Encryption_type._CF_enumeration.addEnumeration(unicode_value=u'none', tag=u'none')
Encryption_type.md5 = Encryption_type._CF_enumeration.addEnumeration(unicode_value=u'md5', tag=u'md5')
Encryption_type.proprietary = Encryption_type._CF_enumeration.addEnumeration(unicode_value=u'proprietary', tag=u'proprietary')
Encryption_type._InitializeFacetMap(Encryption_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'Encryption-type', Encryption_type)

# Atomic simple type: {http://myTest.com/ns/yang/myTest-myVer-types}Hex-integer
class Hex_integer (pyxb.binding.datatypes.string):

    """
        An unsigned 32-bit integer represented in
        hexadecimal format.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Hex-integer')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-types.xsd', 266, 2)
    _Documentation = u'\n        An unsigned 32-bit integer represented in\n        hexadecimal format.\n      '
Hex_integer._CF_pattern = pyxb.binding.facets.CF_pattern()
Hex_integer._CF_pattern.addPattern(pattern=u'[0-9a-fA-F]{1,8}')
Hex_integer._InitializeFacetMap(Hex_integer._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Hex-integer', Hex_integer)

# Atomic simple type: {http://myTest.com/ns/yang/myTest-myVer-types}Osi-system-id
class Osi_system_id (pyxb.binding.datatypes.string):

    """
        An OSI system ID should be of the form 
        0123.4567.89ab. This data type restricts each
        character to a hex character.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Osi-system-id')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-types.xsd', 278, 2)
    _Documentation = u'\n        An OSI system ID should be of the form \n        0123.4567.89ab. This data type restricts each\n        character to a hex character.\n      '
Osi_system_id._CF_pattern = pyxb.binding.facets.CF_pattern()
Osi_system_id._CF_pattern.addPattern(pattern=u'[a-fA-F0-9]{4}(\\.[a-fA-F0-9]{4}){2}')
Osi_system_id._InitializeFacetMap(Osi_system_id._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Osi-system-id', Osi_system_id)

# Atomic simple type: {http://myTest.com/ns/yang/myTest-myVer-types}Osi-area-address
class Osi_area_address (pyxb.binding.datatypes.string):

    """
        An OSI area address should consist of an odd number
        of octets, and be of the form 01 or 01.2345 etc up
        to 01.2345.6789.abcd.ef01.2345.6789. This data type
        restricts each character to a hex character.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Osi-area-address')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-types.xsd', 291, 2)
    _Documentation = u'\n        An OSI area address should consist of an odd number\n        of octets, and be of the form 01 or 01.2345 etc up\n        to 01.2345.6789.abcd.ef01.2345.6789. This data type\n        restricts each character to a hex character.\n      '
Osi_area_address._CF_pattern = pyxb.binding.facets.CF_pattern()
Osi_area_address._CF_pattern.addPattern(pattern=u'[a-fA-F0-9]{2}(\\.[a-fA-F0-9]{4}){0,6}')
Osi_area_address._InitializeFacetMap(Osi_area_address._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Osi-area-address', Osi_area_address)

# Atomic simple type: {http://myTest.com/ns/yang/myTest-myVer-types}Isis-node-id
class Isis_node_id (pyxb.binding.datatypes.string):

    """
        An ISIS node ID should be of the form 
        0123.4567.89ab.cd. This data type restricts each
        character to a hex character.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Isis-node-id')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-types.xsd', 305, 2)
    _Documentation = u'\n        An ISIS node ID should be of the form \n        0123.4567.89ab.cd. This data type restricts each\n        character to a hex character.\n      '
Isis_node_id._CF_pattern = pyxb.binding.facets.CF_pattern()
Isis_node_id._CF_pattern.addPattern(pattern=u'[a-fA-F0-9]{4}(\\.[a-fA-F0-9]{4}){2}\\.[a-fA-F0-9]{2}')
Isis_node_id._InitializeFacetMap(Isis_node_id._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Isis-node-id', Isis_node_id)

# Atomic simple type: {http://myTest.com/ns/yang/myTest-myVer-types}Isis-lsp-id
class Isis_lsp_id (pyxb.binding.datatypes.string):

    """
        An ISIS LSP ID should be of the form 
        0123.4567.89ab.cd-ef. This data type restricts each
        character to a hex character.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Isis-lsp-id')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-types.xsd', 318, 2)
    _Documentation = u'\n        An ISIS LSP ID should be of the form \n        0123.4567.89ab.cd-ef. This data type restricts each\n        character to a hex character.\n      '
Isis_lsp_id._CF_pattern = pyxb.binding.facets.CF_pattern()
Isis_lsp_id._CF_pattern.addPattern(pattern=u'[a-fA-F0-9]{4}(\\.[a-fA-F0-9]{4}){2}\\.[a-fA-F0-9]{2}\\-[a-fA-F0-9]{2}')
Isis_lsp_id._InitializeFacetMap(Isis_lsp_id._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Isis-lsp-id', Isis_lsp_id)

# Atomic simple type: {http://myTest.com/ns/yang/myTest-myVer-types}Osi-net
class Osi_net (pyxb.binding.datatypes.string):

    """
        An OSI NET should consist of an even number of 
        octets, and be of the form 01.2345.6789.abcd.ef etc
        up to 
        01.2345.6789.abcd.ef01.2345.6789.abcd.ef01.2345.67.
        This data type restricts each character to a hex
        character.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Osi-net')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-types.xsd', 331, 2)
    _Documentation = u'\n        An OSI NET should consist of an even number of \n        octets, and be of the form 01.2345.6789.abcd.ef etc\n        up to \n        01.2345.6789.abcd.ef01.2345.6789.abcd.ef01.2345.67.\n        This data type restricts each character to a hex\n        character.\n      '
Osi_net._CF_pattern = pyxb.binding.facets.CF_pattern()
Osi_net._CF_pattern.addPattern(pattern=u'[a-fA-F0-9]{2}(\\.[a-fA-F0-9]{4}){3,9}\\.[a-fA-F0-9]{2}')
Osi_net._InitializeFacetMap(Osi_net._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Osi-net', Osi_net)

# Atomic simple type: {http://myTest.com/ns/yang/myTest-myVer-types}String-identifier
class String_identifier (pyxb.binding.datatypes.string):

    """
        A string for specifying identifier.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'String-identifier')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-types.xsd', 347, 2)
    _Documentation = u'\n        A string for specifying identifier.\n      '
String_identifier._CF_pattern = pyxb.binding.facets.CF_pattern()
String_identifier._CF_pattern.addPattern(pattern=u'[a-zA-Z][\\w\\-]*')
String_identifier._InitializeFacetMap(String_identifier._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'String-identifier', String_identifier)

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-types.xsd', 367, 6)
    _Documentation = None
STD_ANON._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON._CF_pattern.addPattern(pattern=u'.')
STD_ANON._InitializeFacetMap(STD_ANON._CF_pattern)

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.unsignedByte):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-types.xsd', 372, 6)
    _Documentation = None
STD_ANON_._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-types.xsd', 388, 6)
    _Documentation = None
STD_ANON_2._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_2._CF_pattern.addPattern(pattern=u'.|(DEFAULT)|(BREAK)|(NONE)')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_pattern)

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.unsignedByte):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-types.xsd', 393, 6)
    _Documentation = None
STD_ANON_3._InitializeFacetMap()

# Atomic simple type: {http://myTest.com/ns/yang/myTest-myVer-types}Extended-node-id
class Extended_node_id (pyxb.binding.datatypes.string):

    """
        A location used as value information and specified
        as a Rack/Slot/Instance/SubInstance, e.g. 
        0/1/CPU0/NPU0
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Extended-node-id')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-types.xsd', 399, 2)
    _Documentation = u'\n        A location used as value information and specified\n        as a Rack/Slot/Instance/SubInstance, e.g. \n        0/1/CPU0/NPU0\n      '
Extended_node_id._CF_pattern = pyxb.binding.facets.CF_pattern()
Extended_node_id._CF_pattern.addPattern(pattern=u'(\\w*\\d+/){3}(\\w*\\d+)')
Extended_node_id._InitializeFacetMap(Extended_node_id._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Extended-node-id', Extended_node_id)

# Atomic simple type: {http://myTest.com/ns/yang/myTest-myVer-types}Node-id
class Node_id (pyxb.binding.datatypes.string):

    """
        A location used as value information and specified
        as a Rack/Slot/Instance triple, e.g. F0/SC1/0.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Node-id')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-types.xsd', 412, 2)
    _Documentation = u'\n        A location used as value information and specified\n        as a Rack/Slot/Instance triple, e.g. F0/SC1/0.\n      '
Node_id._CF_pattern = pyxb.binding.facets.CF_pattern()
Node_id._CF_pattern.addPattern(pattern=u'(\\w*\\d+/){2}(\\w*\\d+)')
Node_id._InitializeFacetMap(Node_id._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Node-id', Node_id)

# Atomic simple type: {http://myTest.com/ns/yang/myTest-myVer-types}Pq-node-id
class Pq_node_id (pyxb.binding.datatypes.string):

    """
        Partially qualified location which is used for 
        wildcarding location specifications, e.g. 1/*/*
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Pq-node-id')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-types.xsd', 424, 2)
    _Documentation = u'\n        Partially qualified location which is used for \n        wildcarding location specifications, e.g. 1/*/*\n      '
Pq_node_id._CF_pattern = pyxb.binding.facets.CF_pattern()
Pq_node_id._CF_pattern.addPattern(pattern=u'(((\\w*\\d+)|(\\*))/){2}((\\w*\\d+)|(\\*))')
Pq_node_id._InitializeFacetMap(Pq_node_id._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Pq-node-id', Pq_node_id)

# Union simple type: {http://myTest.com/ns/yang/myTest-myVer-types}Char-num
# superclasses pyxb.binding.datatypes.anySimpleType
class Char_num (pyxb.binding.basis.STD_union):

    """
        Takes a character or its ASCII decimal equivalent
        (0-255).
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Char-num')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-types.xsd', 358, 2)
    _Documentation = u'\n        Takes a character or its ASCII decimal equivalent\n        (0-255).\n      '

    _MemberTypes = ( STD_ANON, STD_ANON_, )
Char_num._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Char_num)
Char_num._CF_pattern = pyxb.binding.facets.CF_pattern()
Char_num._InitializeFacetMap(Char_num._CF_enumeration,
   Char_num._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Char-num', Char_num)

# Union simple type: {http://myTest.com/ns/yang/myTest-myVer-types}Tty-escape-char-num
# superclasses pyxb.binding.datatypes.anySimpleType
class Tty_escape_char_num (pyxb.binding.basis.STD_union):

    """
        Escape character or its ASCII decimal equivalent
        (0-255) or one of the three string DEFAULT, BREAK,
        NONE.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Tty-escape-char-num')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\myTest-test-myVer-types.xsd', 378, 2)
    _Documentation = u'\n        Escape character or its ASCII decimal equivalent\n        (0-255) or one of the three string DEFAULT, BREAK,\n        NONE.\n      '

    _MemberTypes = ( STD_ANON_2, STD_ANON_3, )
Tty_escape_char_num._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Tty_escape_char_num)
Tty_escape_char_num._CF_pattern = pyxb.binding.facets.CF_pattern()
Tty_escape_char_num._InitializeFacetMap(Tty_escape_char_num._CF_enumeration,
   Tty_escape_char_num._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Tty-escape-char-num', Tty_escape_char_num)
