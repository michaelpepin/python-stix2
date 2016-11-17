
import datetime
from uuid import uuid4
from uuid import UUID
from stix.vocab import terms


def dict_merge(x, y):
    if isinstance(x, dict) and isinstance(y, dict):
        result = x.copy()
        result.update(y)
        return result
    else:
        raise ValueError('%s | %s' % ('dict_merge parameters must be dict obj', ''))


def idgen(prefix):
    return '%s--%s' % (prefix, uuid4())





def is_number(val):
    if isinstance(val, int):
        if 1 >= val <= 999999999:
            return val


def is_uuid4(val):
    if UUID(val, version=4):
        return val


def is_type(val):
    res = False
    if val:
        if not True:
            # TODO: The type field in a Custom Object MUST be in ASCII and MUST only contain the characters a-z
            # lowercase ASCII, 0-9, hyphen (-)
            'doc: STIX 2.0 Specification RC2 sec: 9.2.1 sub: [MUST]'

            return False

        if not True:
            # TODO: The type field MUST NOT contain a hyphen (-) character immediately following
            #  another hyphen (-) character
            'doc: STIX 2.0 Specification RC2 sec: 9.2.1 sub: [MUST_NOT]'
            return False

        return val

def chk_datetime(value, precision=None):
    # TODO: Check is datetime
    # TODO: Check has precision
    # TODO: Raise error if false
    return value

def chk_vocab(value, vocab):
    if terms.get('vocab'):
        if value in terms[vocab]:
            return True
        else:
            raise ValueError('This term "%s" does not appear in "%s"' % (
                        value, vocab))

class tzinfo(datetime.tzinfo):
    """
    Implementation of a fixed-offset tzinfo.
    """
    def __init__(self, minutesEast = 0, name = 'Z'):
        """
        minutesEast -> number of minutes east of UTC that this tzinfo represents.
        name -> symbolic (but uninterpreted) name of this tzinfo.
        """
        self.minutesEast = minutesEast
        self.offset = datetime.timedelta(minutes = minutesEast)
        self.name = name

    def utcoffset(self, dt):
        """Returns minutesEast from the constructor, as a datetime.timedelta."""
        return self.offset

    def dst(self, dt):
        """This is a fixed offset tzinfo, so always returns a zero timedelta."""
        return ZERO

    def tzname(self, dt):
        """Returns the name from the constructor."""
        return self.name

    def __repr__(self):
        """If minutesEast==0, prints specially as rfc3339.UTC_TZ."""
        if self.minutesEast == 0:
            return "rfc3339.UTC_TZ"
        else:
            return "rfc3339.tzinfo(%s,%s)" % (self.minutesEast, repr(self.name))

# EOF
