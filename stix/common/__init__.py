
from stix.utils import *
from stix.utils import errors


class Entity(object):
    _TYPE_ = 'entity'
    _VERSION_ = "2.0.0-rc.3"

    def __init__(self, type_, id_=None):
        self.type = self._chk_type(type_)
        self.id = self._chk_id(id_)

    @staticmethod
    def _chk_type(val):
        if val:
            return val
        else:
            e = errors.value_errors
            raise ValueError('%s | %s' % (e['type_1']['msg'],
                                          e['type_1']['ref'][0]))

    def _chk_id(self, val):
        res = False
        if val:
            if '--' in val:
                prefix, uuid = val.split('--')
                if not prefix == self.type:
                    e = errors.value_errors
                    raise ValueError('%s | %s' % (e['id_1']['msg'],
                                                  e['id_1']['ref'][1]))
                elif not is_uuid4(uuid):
                    e = errors.value_errors
                    raise ValueError('%s | %s' % (e['id_1']['msg'],
                                                  e['id_1']['ref'][2]))
                else:
                    res = True
        else:
            return idgen(self.type)

        if res:
            return val
        else:
            e = errors.value_errors
            raise ValueError('%s | %s' % (e['num_1']['msg'],
                                          e['num_1']['ref'][1]))

    def from_dict(self, data):
        if isinstance(data, dict):
            if data.get('type'):
                self.type = self._chk_type(data['type'])

            if data.get('id'):
                self.id = data['id']
            else:
                self.id = idgen(self.type)

    def to_dict(self):
        return {'id': self.id, 'type': self.type}


class Object(Entity):
    _TYPE_ = 'object'
    _VERSION_ = "2.0.0-rc.3"

    def __init__(self, type_, created, modified, version, id_=None):
        super(Object, self).__init__(
            id_=id_,
            type_=type_,
        )
        self.created = is_datetime(created, 'full')
        self.modified = is_datetime(modified, 'full')
        self.version = self._chk_version(version)
        self.created_by_ref = None
        self.revoke = False
        self.labels = []
        self.external_references = []
        self.object_marking_refs = []
        self.granular_markings = []

    @staticmethod
    def _chk_version(val):
        if not val:
            e = errors.value_errors
            raise ValueError('%s | %s' % (e['version']['msg'],
                                          e['version']['ref'][0]))
        if is_number(val):
            return val
        else:
            e = errors.value_errors
            raise ValueError('%s | %s' % (e['num_1']['msg'],
                                          e['num_1']['ref'][1]))

    def from_dict(self, data):
        super(Object, self).from_dict(data)
        if isinstance(data, dict):
            if data.get('created'):
                self.created = data['created']
            if data.get('modified'):
                self.modified = data['modified']
            if data.get('version'):
                self.version = self._chk_version(data['version'])
            if data.get('created_by_ref'):
                self.created_by_ref = data['created_by_ref']
            if data.get('revoke'):
                self.revoke = data['revoke']
            if data.get('labels'):
                self.labels = data['labels']
            if data.get('external_references'):
                self.external_references = data['external_references']
            if data.get('object_marking_refs'):
                self.object_marking_refs = data['object_marking_refs']
            if data.get('granular_markings'):
                self.granular_markings = data['granular_markings']

    def to_dict(self):
        return dict_merge(super(Object, self).to_dict(), {
            'created': self.created,
            'modified': self.modified,
            'version': self.version,
            'revoke': self.revoke,
            'labels': self.labels,
            'created_by_ref': self.created_by_ref,
            'external_references': self.external_references,
            'object_marking_refs': self.object_marking_refs,
            'granular_markings': self.granular_markings,
        })


class DomainObject(Object):
    _TYPE_ = 'domain-object'
    _VERSION_ = "2.0.0-rc.3"

    def __init__(self, type_, name, created, modified, version, id_=None):
        super(DomainObject, self).__init__(
            id_=id_,
            type_=type_,
            created=created,
            version=version,
            modified=modified,
        )
        self.name = self._chk_name(name),
        self.description = None

    @staticmethod
    def _chk_name(val):
        if not val:
            e = errors.value_errors
            raise ValueError('%s | %s' % (e['name']['msg'],
                                          e['name']['ref'][0]))

    def from_dict(self, data):
        super(DomainObject, self).from_dict(data)
        if isinstance(data, dict):
            if data.get('name'):
                self.name = self._chk_name(data['name'])
            if data.get('name'):
                self.description = data['description']

    def to_dict(self):
        return dict_merge(super(DomainObject, self).to_dict(), {
            'name': self.name,
            'description': self.description
        })


# EOF
