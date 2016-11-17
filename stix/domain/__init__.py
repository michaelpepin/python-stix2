
from stix.utils import *
from stix.utils import errors
from stix.common import DomainObject


class AttackPattern(DomainObject):
    _TYPE_ = 'attack-pattern'
    _VERSION_ = "2.0.0-rc.3"

    def __init__(self, name, created, modified, id_=None):
        super(AttackPattern, self).__init__(
            version=AttackPattern._VERSION_,
            type_=AttackPattern._TYPE_,
            id_=id_,
            name=name,
            created=created,
            modified=modified,)

        self.kill_chain_phases = []

    def from_dict(self, data):
        super(AttackPattern, self).from_dict(data)
        if isinstance(data, dict):
            if data.get('kill_chain_phases'):
                if isinstance(data['kill_chain_phases'], list):
                    for phase in data['kill_chain_phases']:
                        if chk_vocab(phase, 'kill_chain_phases'):
                            self.kill_chain_phases.append = phase
                else:
                    e = errors.value_errors
                    raise ValueError('%s | %s' % (e['kill_chain_phases']['msg'],
                                                  e['kill_chain_phases']['ref'][0]))

    def to_dict(self):
        return dict_merge(super(AttackPattern, self).to_dict(), {
            'kill_chain_phases': self.kill_chain_phases,
        })


class Campaign(DomainObject):
    _TYPE_ = 'campaign'
    _VERSION_ = "2.0.0-rc.3"

    def __init__(self, name, created, modified, id_=None):
        super(Campaign, self).__init__(
            version=Campaign._VERSION_,
            type_=Campaign._TYPE_,
            id_=id_,
            name=name,
            created=created,
            modified=modified,)

        self.aliases = []
        self.first_seen = None
        self.first_seen_precision = None
        self.objective = None

    def from_dict(self, data):
        super(Campaign, self).from_dict(data)
        if isinstance(data, dict):
            if data.get('first_seen'):
                if chk_datetime(data['first_seen']):
                    pass




    def to_dict(self):
        return dict_merge(super(Campaign, self).to_dict(), {
            'name': self.name,
            'description': self.description
        })

class CourseOfAction(DomainObject):
    _TYPE_ = 'course-of-action'
    _VERSION_ = "2.0.0-rc.3"

    def __init__(self, name, created, modified, id_=None):
        super(CourseOfAction, self).__init__(
            version=CourseOfAction._VERSION_,
            type_=CourseOfAction._TYPE_,
            id_=id_,
            name=name,
            created=created,
            modified=modified,)

        self.action = None


class Identity(DomainObject):
    _TYPE_ = 'identity'
    _VERSION_ = "2.0.0-rc.3"

    def __init__(self, name, created, modified, identity_class, id_=None):
        super(Identity, self).__init__(
            version=Identity._VERSION_,
            type_=Identity._TYPE_,
            id_=id_,
            name=name,
            created=created,
            modified=modified,)

        self.identity_class = identity_class
        self.sectors = None
        self.regions = []
        self.nationalities = []
        self.contact_information = None


class IntrusionSet(DomainObject):
    _TYPE_ = 'intrusion-set'
    _VERSION_ = "2.0.0-rc.3"

    def __init__(self, name, created, modified, id_=None):
        super(IntrusionSet, self).__init__(
            version=IntrusionSet._VERSION_,
            type_=IntrusionSet._TYPE_,
            id_=id_,
            name=name,
            created=created,
            modified=modified,)

        self.aliases = []
        self.first_seen = None
        self.first_seen_precision = None
        self.goals = []
        self.resource_level = None
        self.primary_motivation = None
        self.secondary_motivations = []
        self.region = None
        self.country = None


class Malware(DomainObject):
    _TYPE_ = 'malware'
    _VERSION_ = "2.0.0-rc.3"

    def __init__(self, name, created, modified, id_=None):
        super(Malware, self).__init__(
            version=Malware._VERSION_,
            type_=Malware._TYPE_,
            id_=id_,
            name=name,
            created=created,
            modified=modified,)

        self.kill_chain_phases = []


class Report(DomainObject):
    _TYPE_ = 'report'
    _VERSION_ = "2.0.0-rc.3"

    def __init__(self, name, created, modified, published, object_refs, id_=None):
        super(Report, self).__init__(
            version=Report._VERSION_,
            type_=Report._TYPE_,
            id_=id_,
            name=name,
            created=created,
            modified=modified,)

        self.published = published
        self.object_refs = object_refs
        
        
class ThreatActor(DomainObject):
    _TYPE_ = 'threat-actor'
    _VERSION_ = "2.0.0-rc.3"

    def __init__(self, name, created, modified, id_=None):
        super(ThreatActor, self).__init__(
            version=ThreatActor._VERSION_,
            type_=ThreatActor._TYPE_,
            id_=id_,
            name=name,
            created=created,
            modified=modified,)

        self.aliases = []
        self.roles = []
        self.goals = []
        self.sophistication = None
        self.resource_level = None
        self.primary_motivation = None
        self.secondary_motivations = []
        self.personal_motivations = []


class Tool(DomainObject):
    _TYPE_ = 'tool'
    _VERSION_ = "2.0.0-rc.3"

    def __init__(self, name, created, modified, id_=None):
        super(Tool, self).__init__(
            version=Tool._VERSION_,
            type_=Tool._TYPE_,
            id_=id_,
            name=name,
            created=created,
            modified=modified,)

        self.kill_chain_phases = []
        self.tool_version = None


class Vulnerability(DomainObject):
    _TYPE_ = 'vulnerability'
    _VERSION_ = "2.0.0-rc.3"

    def __init__(self, name, created, modified, id_=None):
        super(Vulnerability, self).__init__(
            version=Vulnerability._VERSION_,
            type_=Vulnerability._TYPE_,
            id_=id_,
            name=name,
            created=created,
            modified=modified,)

# EOF
