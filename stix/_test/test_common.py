
from uuid import UUID
from stix.utils import idgen
from stix.common import Entity
from stix.common import Object
from stix.common import DomainObject


def main():
    data = {
        'created_by_ref': None,
        'external_references': [],
        'created': '',
        'granular_markings': [],
        'labels': [],
        'modified': '',
        'version': 1,
        'object_marking_refs': [],
        'revoke': False,
        'type': 'object',
        'id': 'object--94116ae0-2bef-40c3-b34d-1752494d5767'}
    ### These are ONLY happy path tests
    #print test_Entity()
    print test_Object()


def test_DomainObject(data):

    res = list()
    type_ = 'domain-object'
    obj = DomainObject(
        type_=data['type'],
        created=data['created'],
        modified=data['modified'],
        version=data['version'],
        name=data['name'])

    obj.from_dict(data)
    d = obj.to_dict()

def test_Object(data):

    res = list()
    type_ = 'object'
    obj = Object(type_=data['type'],
                 created=data['created'],
                 modified=data['modified'],
                 version=data['version'])

    obj.from_dict(data)
    d = obj.to_dict()

    res.append(False)
    if check_entity(d, type_):
        res[0] = True

    res.append(False)
    if check_object(d, data):
        res[1] = True

    if False not in res:
        return True
    else:
        print res

def test_Entity():

    res = list()
    type_ = "entity"
    entity = Entity(idgen(type_), type_)

    d = entity.to_dict()
    res = check_entity(d, type_)
    return res

# ## --------------------------------------------

def check_object(d, data):

    res = list()
    res.append(False)
    if isinstance(d, dict) and isinstance(data, dict):
        if d == data:
            res[0] = True

    return res


def check_entity(d, type_):

    res = list()
    res.append(False)
    if d.get('type'):
        if d['type'] == type_:
            res[0] = True

    res.append(False)
    if d.get('id'):
        if "--" in d['id']:
            prefix, guid = d['id'].split("--")
            if UUID(guid, version=4) and prefix == type_:
                res[1] = True

    if False not in res:
        return True

if __name__ == '__main__':
    main()

# EOF