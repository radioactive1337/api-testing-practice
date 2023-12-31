schema = {'$defs': {'Detail1': {'properties': {'loc': {'items': {'anyOf': [{'type': 'string'},
                                                                           {'type': 'integer'}]},
                                                       'title': 'Loc',
                                                       'type': 'array'},
                                               'msg': {'title': 'Msg', 'type': 'string'},
                                               'type': {'title': 'Type',
                                                        'type': 'string'}},
                                'required': ['loc', 'msg', 'type'],
                                'title': 'Detail1',
                                'type': 'object'},
                    'Detail2': {'properties': {'reason': {'title': 'Reason',
                                                          'type': 'string'}},
                                'required': ['reason'],
                                'title': 'Detail2',
                                'type': 'object'}},
          'properties': {'detail': {'anyOf': [{'items': {'$ref': '#/$defs/Detail1'},
                                               'type': 'array'},
                                              {'$ref': '#/$defs/Detail2'}],
                                    'title': 'Detail'}},
          'required': ['detail'],
          'title': 'ErrorModel',
          'type': 'object'}
