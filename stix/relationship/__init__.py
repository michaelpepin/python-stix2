
from stix.common import Object


class Relationship(Object):
    _TYPE_ = 'relationship'
    _VERSION_ = "2.0.0-rc.3"

    def __init__(self, created, modified, relationship_type, source_ref, target_ref, id_=None):
        super(Relationship, self).__init__(
            version=Relationship._VERSION_,
            type_=Relationship._TYPE_,
            id_=id_,
            created=created,
            modified=modified,)

        self.relationship_type = relationship_type
        self.description = None
        self.source_ref = source_ref
        self.target_ref = target_ref

# EOF
