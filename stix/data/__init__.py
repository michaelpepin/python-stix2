
from stix.common import Object


class ObservedData(Object):
    _TYPE_ = 'observed-data'
    _VERSION_ = "2.0.0-rc.2"

    def __init__(self, created, modified, first_observed, last_observed, cybox_, number_observed=1, id_=None):
        super(ObservedData, self).__init__(
            version=ObservedData._VERSION_,
            type_=ObservedData._TYPE_,
            id_=id_,
            created=created,
            modified=modified,)

        self.first_observed = first_observed
        self.last_observed = last_observed
        self.number_observed = number_observed
        self.cybox = cybox_


class Sighting(Object):
    _TYPE_ = 'observed-data'
    _VERSION_ = "2.0.0-rc.2"

    def __init__(self, created, modified, sighting_of_ref, id_=None):
        super(Sighting, self).__init__(
            version=Sighting._VERSION_,
            type_=Sighting._TYPE_,
            id_=id_,
            created=created,
            modified=modified,)

        self.first_seen = None
        self.first_seen_precision = None
        self.last_seen = None
        self.last_seen_precision = None
        self.count = None
        self.sighting_of_ref = sighting_of_ref
        self.observed_data_refs = None
        self.where_sighted_refs = None
        self.summary = None

# EOF
