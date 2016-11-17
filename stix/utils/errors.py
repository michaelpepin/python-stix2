
value_errors = {
    'num_1': {
        'msg': 'value provided is not a integer or is not between 1 and 999,999,999 ',
        'ref': {
            0: 'doc: STIX 2.0 Specification RC2, sec: 5.8.1, sub: number_observed',
            1: 'doc: STIX 2.0 Specification RC2, sec: 3.1, sub: version',
            2: 'doc: STIX 2.0 Specification RC2, sec: 3.1, sub: count'
        },
        'help': {
            0: ''
        }
    },
    'type_1': {
        'msg': 'value provided does not appear to be a valid object-type',
        'ref': {
            0: 'doc: STIX 2.0 Specification RC2, sec: 2.4, flag:is_RequiredProperty,',
            1: 'doc: STIX 2.0 Specification RC2 sec: 9.2.1 sub: [MUST]',
            2: 'doc: STIX 2.0 Specification RC2 sec: 9.2.1 sub: [MUST_NOT]',
        },
        'help': {
            0: ''
        }
    },
    'id_1': {
        'msg': 'value provided does not appear to be a valid object-id',
        'ref': {
            0: 'doc: STIX 2.0 Specification RC2, sec: 2.4, flag:is_RequiredProperty,',
            1: 'doc: STIX 2.0 Specification RC2, sec: 2.4, sub: object-type,',
            2: 'doc: STIX 2.0 Specification RC2, sec: 2.4, sub: UUIDv4,'
        },
        'help': {
            0: ''
        }
    },
    'uuid_1': {
        'msg': 'value provided does not appear to be a valid version 4 UUID',
        'ref': {
            0: 'doc: RFC 4122, sec: 4.4, sub: version 4 UUID'
        },
        'help': {
            0: ''
        }
    },
    'version': {
        'msg': 'doc: STIX 2.0 Specification RC2, sec: ?.?, flag:is_RequiredProperty',
        'ref': {
            0: 'doc:, sec: , sub:,'
        },
        'help': {
            0: ''
        }
    },
    'name': {
        'msg': 'doc: STIX 2.0 Specification RC2, sec: ?.?, flag:is_RequiredProperty',
        'ref': {
            0: 'doc:, sec: , sub:,'
        },
        'help': {
            0: ''
        }
    },
    'kill_chain_phase': {
        'msg': 'doc: STIX 2.0 Specification RC2, sec: ?.?, flag:Not-in-Vocab',
        'ref': {
            0: 'doc:, sec: , sub:,'
        },
        'help': {
            0: ''
        }
    },
    'kill_chain_phases': {
        'msg': 'doc: STIX 2.0 Specification RC2, sec: ?.?, flag:Must-be-List',
        'ref': {
            0: 'doc:, sec: , sub:,'
        },
        'help': {
            0: ''
        }
    },

}