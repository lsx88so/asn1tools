BAR = {'Bar': {'extensibility-implied': False,
               'imports': {},
               'tags': 'EXPLICIT',
               'types': {'AcceptTypes': {'members': [{'element': {'type': 'BIT '
                                                                  'STRING'},
                                                      'name': 'standardTypes',
                                                      'optional': True,
                                                      'size': None,
                                                      'tag': {'kind': 'IMPLICIT',
                                                              'number': 0},
                                                      'type': 'SEQUENCE OF'},
                                                     {'element': {'type': 'OCTET '
                                                                  'STRING'},
                                                      'name': 'otherTypes',
                                                      'optional': True,
                                                      'size': None,
                                                      'tag': {'kind': 'IMPLICIT',
                                                              'number': 1},
                                                      'type': 'SEQUENCE OF'}],
                                         'tag': {'class': 'APPLICATION',
                                                 'kind': 'IMPLICIT',
                                                 'number': 1},
                                         'type': 'SEQUENCE'},
                         'GetRequest': {'members': [{'name': 'headerOnly',
                                                     'optional': False,
                                                     'type': 'BOOLEAN'},
                                                    {'name': 'lock',
                                                     'optional': False,
                                                     'type': 'BOOLEAN'},
                                                    {'name': 'acceptTypes',
                                                     'optional': True,
                                                     'type': 'AcceptTypes'},
                                                    {'name': 'url',
                                                     'optional': False,
                                                     'type': 'OCTET STRING'}],
                                        'tag': {'class': 'APPLICATION',
                                                'kind': 'IMPLICIT',
                                                'number': 0},
                                        'type': 'SEQUENCE'}},
               'values': {}}}

