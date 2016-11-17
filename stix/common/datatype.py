

class String(basestring):
    _TYPE_ = 'string'
    _VERSION_ = "2.0.0-rc.3"
    """
    SOURCE: https://docs.google.com/document/d/1IcA5KhglNdyX3tO17bBluC5nqSf70M5qgK9nuAoYJgw
    doc: STIX 2.0 Specification - Part 1 - RC3
    The string data type represents a finite-length string of valid characters from the Unicode coded character
    set [REF:ISO.10646]. Unicode incorporates ASCII [REF: RFC20] and the characters of many other international
    character sets.


    The JSON MTI serialization uses the JSON string type [TODO: Add reference], which mandates the UTF-8 encoding
    for supporting Unicode.
    """
    def __init__(self, *args):
        super(String, self).__init__(*args)

    # TODO: convert_to/enforce UTF-8 string encoding


class List(list):
    _TYPE_ = 'list'
    _VERSION_ = "2.0.0-rc.3"
    """
    SOURCE: https://docs.google.com/document/d/1IcA5KhglNdyX3tO17bBluC5nqSf70M5qgK9nuAoYJgw
    doc: STIX 2.0 Specification - Part 1 - RC3
    The list type defines an ordered sequence of one or more values. The phrasing "list of type <type>" is used to
    indicate that all values within the list must conform to a specific type. For instance, list of type integer means
    that all values of the list must be of the integer type. This specification does not specify the maximum number of
    allowed values in a list, however every instance of a list MUST have at least one value. Specific STIX object
    properties may define more restrictive upper and/or lower bounds for the length of the list.

    Empty lists are prohibited in STIX and MUST NOT be used as a substitute for omitting the property if it is optional.
     If the property is required, the list MUST be present and MUST have at least one value.

    The JSON MTI serialization uses the JSON array type [TODO: Add ref?], which is an ordered list of zero or more
    values.
    """

    def __init__(self, type_, vals=None):
        super(List, self).__init__(iterable=vals)
        self.type = type_

    def is_valid(self):
        return True


class Boolean(bool):
    _TYPE_ = 'boolean'
    _VERSION_ = "2.0.0-rc.3"
    """
    SOURCE: https://docs.google.com/document/d/1IcA5KhglNdyX3tO17bBluC5nqSf70M5qgK9nuAoYJgw
    doc: STIX 2.0 Specification - Part 1 - RC3

    A boolean is a value of either true or false. Properties with this type MUST have a value of true or false.

    The JSON MTI serialization uses the JSON boolean type <TODO: add reference>, which is a literal
    (unquoted) true or false.
    """

    def __init__(self, flag):
        super(Boolean, self).__init__(x=flag)

    # TODO: I do not understand the reason for this stix type


class Float(float):
    _TYPE_ = 'float'
    _VERSION_ = "2.0.0-rc.3"
    """
    SOURCE: https://docs.google.com/document/d/1IcA5KhglNdyX3tO17bBluC5nqSf70M5qgK9nuAoYJgw
    doc: STIX 2.0 Specification - Part 1 - RC3

    The float data type represents an IEEE 754 [TODO add ref] double-precision number
    (e.g., a number with a fractional part). However, because the values +/-Infinity and NaN are not representable in
    JSON, they are not valid values in STIX.

    In the JSON MTI serialization, floating point values are represented by the JSON number type
    [REF: https://tools.ietf.org/html/rfc7159].
    """

    def __init__(self, val):
        super(Float, self).__init__(x=val)

    # TODO: Check for compliance

