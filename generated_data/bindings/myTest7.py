# .\_inet.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e55fca38e31992943f7050fa8652a64dcb7a410f
# Generated 2013-10-30 10:34:25.452000 by PyXB version 1.2.3
# Namespace urn:ietf:params:xml:ns:yang:ietf-inet-types [xmlns:inet]

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
Namespace = pyxb.namespace.NamespaceForURI(u'urn:ietf:params:xml:ns:yang:ietf-inet-types', create_if_missing=True)
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


# Atomic simple type: {urn:ietf:params:xml:ns:yang:ietf-inet-types}ip-version
class ip_version (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        This value represents the version of the IP protocol.

        In the value set and its semantics, this type is equivalent
        to the InetVersion textual convention of the SMIv2.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ip-version')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\ietf-inet-types.xsd', 45, 2)
    _Documentation = u'\n        This value represents the version of the IP protocol.\n\n        In the value set and its semantics, this type is equivalent\n        to the InetVersion textual convention of the SMIv2.\n      '
ip_version._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ip_version, enum_prefix=None)
ip_version.unknown = ip_version._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
ip_version.ipv4 = ip_version._CF_enumeration.addEnumeration(unicode_value=u'ipv4', tag=u'ipv4')
ip_version.ipv6 = ip_version._CF_enumeration.addEnumeration(unicode_value=u'ipv6', tag=u'ipv6')
ip_version._InitializeFacetMap(ip_version._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ip-version', ip_version)

# Atomic simple type: {urn:ietf:params:xml:ns:yang:ietf-inet-types}dscp
class dscp (pyxb.binding.datatypes.unsignedByte):

    """
        The dscp type represents a Differentiated Services Code Point
        that may be used for marking packets in a traffic stream.
        In the value set and its semantics, this type is equivalent
        to the Dscp textual convention of the SMIv2.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dscp')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\ietf-inet-types.xsd', 61, 2)
    _Documentation = u'\n        The dscp type represents a Differentiated Services Code Point\n        that may be used for marking packets in a traffic stream.\n        In the value set and its semantics, this type is equivalent\n        to the Dscp textual convention of the SMIv2.\n      '
dscp._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=dscp, value=pyxb.binding.datatypes.unsignedByte(63L))
dscp._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=dscp, value=pyxb.binding.datatypes.unsignedByte(0L))
dscp._InitializeFacetMap(dscp._CF_maxInclusive,
   dscp._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'dscp', dscp)

# Atomic simple type: {urn:ietf:params:xml:ns:yang:ietf-inet-types}ipv6-flow-label
class ipv6_flow_label (pyxb.binding.datatypes.unsignedInt):

    """
        The ipv6-flow-label type represents the flow identifier or Flow
        Label in an IPv6 packet header that may be used to
        discriminate traffic flows.

        In the value set and its semantics, this type is equivalent
        to the IPv6FlowLabel textual convention of the SMIv2.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ipv6-flow-label')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\ietf-inet-types.xsd', 76, 2)
    _Documentation = u'\n        The ipv6-flow-label type represents the flow identifier or Flow\n        Label in an IPv6 packet header that may be used to\n        discriminate traffic flows.\n\n        In the value set and its semantics, this type is equivalent\n        to the IPv6FlowLabel textual convention of the SMIv2.\n      '
ipv6_flow_label._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=ipv6_flow_label, value=pyxb.binding.datatypes.unsignedInt(1048575L))
ipv6_flow_label._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=ipv6_flow_label, value=pyxb.binding.datatypes.unsignedInt(0L))
ipv6_flow_label._InitializeFacetMap(ipv6_flow_label._CF_maxInclusive,
   ipv6_flow_label._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'ipv6-flow-label', ipv6_flow_label)

# Atomic simple type: {urn:ietf:params:xml:ns:yang:ietf-inet-types}port-number
class port_number (pyxb.binding.datatypes.unsignedShort):

    """
        The port-number type represents a 16-bit port number of an
        Internet transport-layer protocol such as UDP, TCP, DCCP, or
        SCTP.  Port numbers are assigned by IANA.  A current list of
        all assignments is available from <http://www.iana.org/>.

        Note that the port number value zero is reserved by IANA.  In
        situations where the value zero does not make sense, it can
        be excluded by subtyping the port-number type.
        In the value set and its semantics, this type is equivalent
        to the InetPortNumber textual convention of the SMIv2.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'port-number')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\ietf-inet-types.xsd', 93, 2)
    _Documentation = u'\n        The port-number type represents a 16-bit port number of an\n        Internet transport-layer protocol such as UDP, TCP, DCCP, or\n        SCTP.  Port numbers are assigned by IANA.  A current list of\n        all assignments is available from <http://www.iana.org/>.\n\n        Note that the port number value zero is reserved by IANA.  In\n        situations where the value zero does not make sense, it can\n        be excluded by subtyping the port-number type.\n        In the value set and its semantics, this type is equivalent\n        to the InetPortNumber textual convention of the SMIv2.\n      '
port_number._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=port_number, value=pyxb.binding.datatypes.unsignedShort(65535L))
port_number._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=port_number, value=pyxb.binding.datatypes.unsignedShort(0L))
port_number._InitializeFacetMap(port_number._CF_maxInclusive,
   port_number._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'port-number', port_number)

# Atomic simple type: {urn:ietf:params:xml:ns:yang:ietf-inet-types}as-number
class as_number (pyxb.binding.datatypes.unsignedInt):

    """
        The as-number type represents autonomous system numbers
        which identify an Autonomous System (AS).  An AS is a set
        of routers under a single technical administration, using
        an interior gateway protocol and common metrics to route
        packets within the AS, and using an exterior gateway
        protocol to route packets to other ASes.  IANA maintains
        the AS number space and has delegated large parts to the
        regional registries.

        Autonomous system numbers were originally limited to 16
        bits.  BGP extensions have enlarged the autonomous system
        number space to 32 bits.  This type therefore uses an uint32
        base type without a range restriction in order to support
        a larger autonomous system number space.

        In the value set and its semantics, this type is equivalent
        to the InetAutonomousSystemNumber textual convention of
        the SMIv2.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'as-number')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\ietf-inet-types.xsd', 114, 2)
    _Documentation = u'\n        The as-number type represents autonomous system numbers\n        which identify an Autonomous System (AS).  An AS is a set\n        of routers under a single technical administration, using\n        an interior gateway protocol and common metrics to route\n        packets within the AS, and using an exterior gateway\n        protocol to route packets to other ASes.  IANA maintains\n        the AS number space and has delegated large parts to the\n        regional registries.\n\n        Autonomous system numbers were originally limited to 16\n        bits.  BGP extensions have enlarged the autonomous system\n        number space to 32 bits.  This type therefore uses an uint32\n        base type without a range restriction in order to support\n        a larger autonomous system number space.\n\n        In the value set and its semantics, this type is equivalent\n        to the InetAutonomousSystemNumber textual convention of\n        the SMIv2.\n      '
as_number._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'as-number', as_number)

# Atomic simple type: {urn:ietf:params:xml:ns:yang:ietf-inet-types}ipv4-address
class ipv4_address (pyxb.binding.datatypes.string):

    """
        The ipv4-address type represents an IPv4 address in
        dotted-quad notation.  The IPv4 address may include a zone
        index, separated by a % sign.

        The zone index is used to disambiguate identical address
        values.  For link-local addresses, the zone index will
        typically be the interface index number or the name of an
        interface.  If the zone index is not present, the default
        zone of the device will be used.

        The canonical format for the zone index is the numerical
        format
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ipv4-address')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\ietf-inet-types.xsd', 162, 2)
    _Documentation = u'\n        The ipv4-address type represents an IPv4 address in\n        dotted-quad notation.  The IPv4 address may include a zone\n        index, separated by a % sign.\n\n        The zone index is used to disambiguate identical address\n        values.  For link-local addresses, the zone index will\n        typically be the interface index number or the name of an\n        interface.  If the zone index is not present, the default\n        zone of the device will be used.\n\n        The canonical format for the zone index is the numerical\n        format\n      '
ipv4_address._CF_pattern = pyxb.binding.facets.CF_pattern()
ipv4_address._CF_pattern.addPattern(pattern=u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])')
ipv4_address._InitializeFacetMap(ipv4_address._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'ipv4-address', ipv4_address)

# Atomic simple type: {urn:ietf:params:xml:ns:yang:ietf-inet-types}ipv6-address
class ipv6_address (pyxb.binding.datatypes.string):

    """
        The ipv6-address type represents an IPv6 address in full,
        mixed, shortened, and shortened-mixed notation.  The IPv6
        address may include a zone index, separated by a % sign.

        The zone index is used to disambiguate identical address
        values.  For link-local addresses, the zone index will
        typically be the interface index number or the name of an
        interface.  If the zone index is not present, the default
        zone of the device will be used.

        The canonical format of IPv6 addresses uses the textual
        representation defined in Section 4 of RFC 5952.  The
        canonical format for the zone index is the numerical
        format as described in Section 11.2 of RFC 4007.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ipv6-address')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\ietf-inet-types.xsd', 184, 2)
    _Documentation = u'\n        The ipv6-address type represents an IPv6 address in full,\n        mixed, shortened, and shortened-mixed notation.  The IPv6\n        address may include a zone index, separated by a % sign.\n\n        The zone index is used to disambiguate identical address\n        values.  For link-local addresses, the zone index will\n        typically be the interface index number or the name of an\n        interface.  If the zone index is not present, the default\n        zone of the device will be used.\n\n        The canonical format of IPv6 addresses uses the textual\n        representation defined in Section 4 of RFC 5952.  The\n        canonical format for the zone index is the numerical\n        format as described in Section 11.2 of RFC 4007.\n      '
ipv6_address._CF_pattern = pyxb.binding.facets.CF_pattern()
ipv6_address._CF_pattern.addPattern(pattern=u'([0-9a-fA-F]{0,4}:){7}[0-9a-fA-F]{0,4}')
ipv6_address._InitializeFacetMap(ipv6_address._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'ipv6-address', ipv6_address)

# Atomic simple type: {urn:ietf:params:xml:ns:yang:ietf-inet-types}ipv4-prefix
class ipv4_prefix (pyxb.binding.datatypes.string):

    """
        The ipv4-prefix type represents an IPv4 address prefix.
        The prefix length is given by the number following the
        slash character and must be less than or equal to 32.

        A prefix length value of n corresponds to an IP address
        mask that has n contiguous 1-bits from the most
        significant bit (MSB) and all other bits set to 0.

        The canonical format of an IPv4 prefix has all bits of
        the IPv4 address set to zero that are not part of the
        IPv4 prefix.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ipv4-prefix')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\ietf-inet-types.xsd', 276, 2)
    _Documentation = u'\n        The ipv4-prefix type represents an IPv4 address prefix.\n        The prefix length is given by the number following the\n        slash character and must be less than or equal to 32.\n\n        A prefix length value of n corresponds to an IP address\n        mask that has n contiguous 1-bits from the most\n        significant bit (MSB) and all other bits set to 0.\n\n        The canonical format of an IPv4 prefix has all bits of\n        the IPv4 address set to zero that are not part of the\n        IPv4 prefix.\n      '
ipv4_prefix._CF_pattern = pyxb.binding.facets.CF_pattern()
ipv4_prefix._CF_pattern.addPattern(pattern=u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))')
ipv4_prefix._InitializeFacetMap(ipv4_prefix._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'ipv4-prefix', ipv4_prefix)

# Atomic simple type: {urn:ietf:params:xml:ns:yang:ietf-inet-types}ipv6-prefix
class ipv6_prefix (pyxb.binding.datatypes.string):

    """
        The ipv6-prefix type represents an IPv6 address prefix.
        The prefix length is given by the number following the
        slash character and must be less than or equal to 128.

        A prefix length value of n corresponds to an IP address
        mask that has n contiguous 1-bits from the most
        significant bit (MSB) and all other bits set to 0.

        The IPv6 address should have all bits that do not belong
        to the prefix set to zero.

        The canonical format of an IPv6 prefix has all bits of
        the IPv6 address set to zero that are not part of the
        IPv6 prefix.  Furthermore, the IPv6 address is represented
        as defined in Section 4 of RFC 5952.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ipv6-prefix')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\ietf-inet-types.xsd', 297, 2)
    _Documentation = u'\n        The ipv6-prefix type represents an IPv6 address prefix.\n        The prefix length is given by the number following the\n        slash character and must be less than or equal to 128.\n\n        A prefix length value of n corresponds to an IP address\n        mask that has n contiguous 1-bits from the most\n        significant bit (MSB) and all other bits set to 0.\n\n        The IPv6 address should have all bits that do not belong\n        to the prefix set to zero.\n\n        The canonical format of an IPv6 prefix has all bits of\n        the IPv6 address set to zero that are not part of the\n        IPv6 prefix.  Furthermore, the IPv6 address is represented\n        as defined in Section 4 of RFC 5952.\n      '
ipv6_prefix._CF_pattern = pyxb.binding.facets.CF_pattern()
ipv6_prefix._CF_pattern.addPattern(pattern=u'(((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8]))))|((([^:]+:){6}(([^:]+:[^:]+)|(.*\\..*)))|((([^:]+:)*[^:]+)?::(([^:]+:)*[^:]+)?)(/.+))')
ipv6_prefix._InitializeFacetMap(ipv6_prefix._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'ipv6-prefix', ipv6_prefix)

# Atomic simple type: {urn:ietf:params:xml:ns:yang:ietf-inet-types}uri
class uri (pyxb.binding.datatypes.string):

    """
        The uri type represents a Uniform Resource Identifier
        (URI) as defined by STD 66.

        Objects using the uri type MUST be in US-ASCII encoding,
        and MUST be normalized as described by RFC 3986 Sections
        6.2.1, 6.2.2.1, and 6.2.2.2.  All unnecessary
        percent-encoding is removed, and all case-insensitive
        characters are set to lowercase except for hexadecimal
        digits, which are normalized to uppercase as described in
        Section 6.2.2.1.

        The purpose of this normalization is to help provide
        unique URIs.  Note that this normalization is not
        sufficient to provide uniqueness.  Two URIs that are
        textually distinct after this normalization may still be
        equivalent.

        Objects using the uri type may restrict the schemes that
        they permit.  For example, 'data:' and 'urn:' schemes
        might not be appropriate.

        A zero-length URI is not a valid URI.  This can be used to
        express 'URI absent' where required.

        In the value set and its semantics, this type is equivalent
        to the Uri SMIv2 textual convention defined in RFC 5017.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'uri')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\ietf-inet-types.xsd', 386, 2)
    _Documentation = u"\n        The uri type represents a Uniform Resource Identifier\n        (URI) as defined by STD 66.\n\n        Objects using the uri type MUST be in US-ASCII encoding,\n        and MUST be normalized as described by RFC 3986 Sections\n        6.2.1, 6.2.2.1, and 6.2.2.2.  All unnecessary\n        percent-encoding is removed, and all case-insensitive\n        characters are set to lowercase except for hexadecimal\n        digits, which are normalized to uppercase as described in\n        Section 6.2.2.1.\n\n        The purpose of this normalization is to help provide\n        unique URIs.  Note that this normalization is not\n        sufficient to provide uniqueness.  Two URIs that are\n        textually distinct after this normalization may still be\n        equivalent.\n\n        Objects using the uri type may restrict the schemes that\n        they permit.  For example, 'data:' and 'urn:' schemes\n        might not be appropriate.\n\n        A zero-length URI is not a valid URI.  This can be used to\n        express 'URI absent' where required.\n\n        In the value set and its semantics, this type is equivalent\n        to the Uri SMIv2 textual convention defined in RFC 5017.\n      "
uri._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'uri', uri)

# Atomic simple type: {urn:ietf:params:xml:ns:yang:ietf-inet-types}t0
class t0 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u't0')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\ietf-inet-types.xsd', 425, 2)
    _Documentation = None
t0._CF_pattern = pyxb.binding.facets.CF_pattern()
t0._CF_pattern.addPattern(pattern=u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.')
t0._InitializeFacetMap(t0._CF_pattern)
Namespace.addCategoryObject('typeBinding', u't0', t0)

# Atomic simple type: [anonymous]
class STD_ANON (ipv4_address):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\ietf-inet-types.xsd', 152, 6)
    _Documentation = None
STD_ANON._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_ (ipv6_address):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\ietf-inet-types.xsd', 156, 6)
    _Documentation = None
STD_ANON_._InitializeFacetMap()

# Atomic simple type: {urn:ietf:params:xml:ns:yang:ietf-inet-types}ipv4-address-no-zone
class ipv4_address_no_zone (ipv4_address):

    """
        An IPv4 address without a zone index.  This type, derived from
        ipv4-address, may be used in situations where the zone is
        known from the context and hence no zone index is needed.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ipv4-address-no-zone')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\ietf-inet-types.xsd', 230, 2)
    _Documentation = u'\n        An IPv4 address without a zone index.  This type, derived from\n        ipv4-address, may be used in situations where the zone is\n        known from the context and hence no zone index is needed.\n      '
ipv4_address_no_zone._CF_pattern = pyxb.binding.facets.CF_pattern()
ipv4_address_no_zone._CF_pattern.addPattern(pattern=u'[0-9\\.]*')
ipv4_address_no_zone._InitializeFacetMap(ipv4_address_no_zone._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'ipv4-address-no-zone', ipv4_address_no_zone)

# Atomic simple type: {urn:ietf:params:xml:ns:yang:ietf-inet-types}ipv6-address-no-zone
class ipv6_address_no_zone (ipv6_address):

    """
        An IPv6 address without a zone index.  This type, derived from
        ipv6-address, may be used in situations where the zone is
        known from the context and hence no zone index is needed.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ipv6-address-no-zone')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\ietf-inet-types.xsd', 243, 2)
    _Documentation = u'\n        An IPv6 address without a zone index.  This type, derived from\n        ipv6-address, may be used in situations where the zone is\n        known from the context and hence no zone index is needed.\n      '
ipv6_address_no_zone._CF_pattern = pyxb.binding.facets.CF_pattern()
ipv6_address_no_zone._CF_pattern.addPattern(pattern=u'[0-9a-fA-F:\\.]*')
ipv6_address_no_zone._InitializeFacetMap(ipv6_address_no_zone._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'ipv6-address-no-zone', ipv6_address_no_zone)

# Atomic simple type: [anonymous]
class STD_ANON_2 (ipv4_prefix):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\ietf-inet-types.xsd', 266, 6)
    _Documentation = None
STD_ANON_2._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_3 (ipv6_prefix):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\ietf-inet-types.xsd', 270, 6)
    _Documentation = None
STD_ANON_3._InitializeFacetMap()

# Atomic simple type: {urn:ietf:params:xml:ns:yang:ietf-inet-types}domain-name
class domain_name (t0):

    """
        The domain-name type represents a DNS domain name.  The
        name SHOULD be fully qualified whenever possible.

        Internet domain names are only loosely specified.  Section
        3.5 of RFC 1034 recommends a syntax (modified in Section
        2.1 of RFC 1123).  The pattern above is intended to allow
        for current practice in domain name use, and some possible
        future expansion.  It is designed to hold various types of
        domain names, including names used for A or AAAA records
        (host names) and other records, such as SRV records.  Note
        that Internet host names have a stricter syntax (described
        in RFC 952) than the DNS recommendations in RFCs 1034 and
        1123, and that systems that want to store host names in
        schema nodes using the domain-name type are recommended to
        adhere to this stricter standard to ensure interoperability.

        The encoding of DNS names in the DNS protocol is limited
        to 255 characters.  Since the encoding consists of labels
        prefixed by a length bytes and there is a trailing NULL
        byte, only 253 characters can appear in the textual dotted
        notation.

        The description clause of schema nodes using the domain-name
        type MUST describe when and how these names are resolved to
        IP addresses.  Note that the resolution of a domain-name value
        may require to query multiple DNS records (e.g., A for IPv4
        and AAAA for IPv6).  The order of the resolution process and
        which DNS record takes precedence can either be defined
        explicitly or may depend on the configuration of the
        resolver.

        Domain-name values use the US-ASCII encoding.  Their canonical
        format uses lowercase US-ASCII characters.  Internationalized
        domain names MUST be A-labels as per RFC 5890.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'domain-name')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\ietf-inet-types.xsd', 322, 2)
    _Documentation = u'\n        The domain-name type represents a DNS domain name.  The\n        name SHOULD be fully qualified whenever possible.\n\n        Internet domain names are only loosely specified.  Section\n        3.5 of RFC 1034 recommends a syntax (modified in Section\n        2.1 of RFC 1123).  The pattern above is intended to allow\n        for current practice in domain name use, and some possible\n        future expansion.  It is designed to hold various types of\n        domain names, including names used for A or AAAA records\n        (host names) and other records, such as SRV records.  Note\n        that Internet host names have a stricter syntax (described\n        in RFC 952) than the DNS recommendations in RFCs 1034 and\n        1123, and that systems that want to store host names in\n        schema nodes using the domain-name type are recommended to\n        adhere to this stricter standard to ensure interoperability.\n\n        The encoding of DNS names in the DNS protocol is limited\n        to 255 characters.  Since the encoding consists of labels\n        prefixed by a length bytes and there is a trailing NULL\n        byte, only 253 characters can appear in the textual dotted\n        notation.\n\n        The description clause of schema nodes using the domain-name\n        type MUST describe when and how these names are resolved to\n        IP addresses.  Note that the resolution of a domain-name value\n        may require to query multiple DNS records (e.g., A for IPv4\n        and AAAA for IPv6).  The order of the resolution process and\n        which DNS record takes precedence can either be defined\n        explicitly or may depend on the configuration of the\n        resolver.\n\n        Domain-name values use the US-ASCII encoding.  Their canonical\n        format uses lowercase US-ASCII characters.  Internationalized\n        domain names MUST be A-labels as per RFC 5890.\n      '
domain_name._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(253L))
domain_name._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
domain_name._InitializeFacetMap(domain_name._CF_maxLength,
   domain_name._CF_minLength)
Namespace.addCategoryObject('typeBinding', u'domain-name', domain_name)

# Union simple type: {urn:ietf:params:xml:ns:yang:ietf-inet-types}ip-address
# superclasses pyxb.binding.datatypes.anySimpleType
class ip_address (pyxb.binding.basis.STD_union):

    """
        The ip-address type represents an IP address and is IP
        version neutral.  The format of the textual representation
        implies the IP version.  This type supports scoped addresses
        by allowing zone identifiers in the address format.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ip-address')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\ietf-inet-types.xsd', 141, 2)
    _Documentation = u'\n        The ip-address type represents an IP address and is IP\n        version neutral.  The format of the textual representation\n        implies the IP version.  This type supports scoped addresses\n        by allowing zone identifiers in the address format.\n      '

    _MemberTypes = ( STD_ANON, STD_ANON_, )
ip_address._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ip_address)
ip_address._CF_pattern = pyxb.binding.facets.CF_pattern()
ip_address._InitializeFacetMap(ip_address._CF_enumeration,
   ip_address._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'ip-address', ip_address)

# Atomic simple type: [anonymous]
class STD_ANON_4 (ipv4_address_no_zone):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\ietf-inet-types.xsd', 220, 6)
    _Documentation = None
STD_ANON_4._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_5 (ipv6_address_no_zone):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\ietf-inet-types.xsd', 224, 6)
    _Documentation = None
STD_ANON_5._InitializeFacetMap()

# Union simple type: {urn:ietf:params:xml:ns:yang:ietf-inet-types}ip-prefix
# superclasses pyxb.binding.datatypes.anySimpleType
class ip_prefix (pyxb.binding.basis.STD_union):

    """
        The ip-prefix type represents an IP prefix and is IP
        version neutral.  The format of the textual representations
        implies the IP version.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ip-prefix')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\ietf-inet-types.xsd', 256, 2)
    _Documentation = u'\n        The ip-prefix type represents an IP prefix and is IP\n        version neutral.  The format of the textual representations\n        implies the IP version.\n      '

    _MemberTypes = ( STD_ANON_2, STD_ANON_3, )
ip_prefix._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ip_prefix)
ip_prefix._CF_pattern = pyxb.binding.facets.CF_pattern()
ip_prefix._InitializeFacetMap(ip_prefix._CF_enumeration,
   ip_prefix._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'ip-prefix', ip_prefix)

# Atomic simple type: [anonymous]
class STD_ANON_6 (domain_name):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\ietf-inet-types.xsd', 380, 6)
    _Documentation = None
STD_ANON_6._InitializeFacetMap()

# Union simple type: {urn:ietf:params:xml:ns:yang:ietf-inet-types}ip-address-no-zone
# superclasses pyxb.binding.datatypes.anySimpleType
class ip_address_no_zone (pyxb.binding.basis.STD_union):

    """
        The ip-address-no-zone type represents an IP address and is
        IP version neutral.  The format of the textual representation
        implies the IP version.  This type does not support scoped
        addresses since it does not allow zone identifiers in the
        address format.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ip-address-no-zone')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\ietf-inet-types.xsd', 208, 2)
    _Documentation = u'\n        The ip-address-no-zone type represents an IP address and is\n        IP version neutral.  The format of the textual representation\n        implies the IP version.  This type does not support scoped\n        addresses since it does not allow zone identifiers in the\n        address format.\n      '

    _MemberTypes = ( STD_ANON_4, STD_ANON_5, )
ip_address_no_zone._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ip_address_no_zone)
ip_address_no_zone._CF_pattern = pyxb.binding.facets.CF_pattern()
ip_address_no_zone._InitializeFacetMap(ip_address_no_zone._CF_enumeration,
   ip_address_no_zone._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'ip-address-no-zone', ip_address_no_zone)

# Union simple type: {urn:ietf:params:xml:ns:yang:ietf-inet-types}host
# superclasses pyxb.binding.datatypes.anySimpleType
class host (pyxb.binding.basis.STD_union):

    """
        The host type represents either an IP address or a DNS
        domain name.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'host')
    _XSDLocation = pyxb.utils.utility.Location(u'c:\\Users\\test_dir\\Documents\\eclipse\\XSD_netconf\\test\\ietf-inet-types.xsd', 367, 2)
    _Documentation = u'\n        The host type represents either an IP address or a DNS\n        domain name.\n      '

    _MemberTypes = ( STD_ANON, STD_ANON_, STD_ANON_6, )
host._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=host)
host._CF_pattern = pyxb.binding.facets.CF_pattern()
host._InitializeFacetMap(host._CF_enumeration,
   host._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'host', host)
