
from stix.common import Entity


class Bundle(Entity):
    _TYPE_ = 'bundle'
    _VERSION_ = "2.0.0-rc.2"

    def __init__(self, spec_version, id_=None, ):
        super(Bundle, self).__init__(
            id_=id_,
            type_=Bundle._TYPE_
        )

        self.spec_version = spec_version
        self.attack_patterns = []
        self.campaigns = []
        self.courses_of_action = []
        self.identities = []
        self.indicators = []
        self.intrusion_sets = []
        self.malware = []
        self.marking_definitions = []
        self.observed_data = []
        self.relationship = []
        self.reports = []
        self.sightings = []
        self.threat_actors = []
        self.tools = []
        self.vulnerabilities = []
        self.custom_objects = []

    def to_dict(self):
        d = super(Bundle, self).to_dict()
        d.update(
            {'spec_version': self.spec_version}
        )
        return d

# EOF
