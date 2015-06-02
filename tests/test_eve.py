import mock

from tests.compat import unittest
from tests.utils import APITestCase

import evelink.eve as evelink_eve

class EVETestCase(APITestCase):

    def setUp(self):
        super(EVETestCase, self).setUp()
        self.eve = evelink_eve.EVE(api=self.api)

    def test_type_names_from_ids(self):
        self.api.get.return_value = self.make_api_result("eve/typename.xml")

        result, current, expires = self.eve.type_names_from_ids(set([12345,23456]))

        self.assertEqual(result, {12345:"200mm Railgun I Blueprint",
                                  23456:"Gara Kort's Raven"})
        self.assertEqual(self.api.mock_calls, [
                mock.call.get('eve/TypeName', params={'IDs': set([12345,23456])}),
            ])
        self.assertEqual(current, 12345)
        self.assertEqual(expires, 67890)

    def test_type_name_from_id(self):
        self.api.get.return_value = self.make_api_result("eve/typename_single.xml")

        result, current, expires = self.eve.type_name_from_id(12345)

        self.assertEqual(result, "200mm Railgun I Blueprint")
        self.assertEqual(self.api.mock_calls, [
                mock.call.get('eve/TypeName', params={'IDs': [12345]}),
            ])
        self.assertEqual(current, 12345)
        self.assertEqual(expires, 67890)

    def test_type_name_from_string_id(self):
        self.api.get.return_value = self.make_api_result("eve/typename_single.xml")

        result, current, expires = self.eve.type_name_from_id("12345")

        self.assertEqual(result, "200mm Railgun I Blueprint")
        self.assertEqual(self.api.mock_calls, [
                mock.call.get('eve/TypeName', params={'IDs': ["12345"]}),
            ])
        self.assertEqual(current, 12345)
        self.assertEqual(expires, 67890)

    def test_character_names_from_ids(self):
        self.api.get.return_value = self.make_api_result("eve/character_name.xml")

        result, current, expires = self.eve.character_names_from_ids(set([1,2]))

        self.assertEqual(result, {1:"EVE System", 2:"EVE Central Bank"})
        self.assertEqual(self.api.mock_calls, [
                mock.call.get('eve/CharacterName', params={'IDs': set([1,2])}),
            ])
        self.assertEqual(current, 12345)
        self.assertEqual(expires, 67890)

    def test_character_name_from_id(self):
        self.api.get.return_value = self.make_api_result("eve/character_name_single.xml")

        result, current, expires = self.eve.character_name_from_id(1)

        self.assertEqual(result, "EVE System")
        self.assertEqual(self.api.mock_calls, [
                mock.call.get('eve/CharacterName', params={'IDs': [1]}),
            ])
        self.assertEqual(current, 12345)
        self.assertEqual(expires, 67890)

    def test_character_name_from_string_id(self):
        self.api.get.return_value = self.make_api_result("eve/character_name_single.xml")

        result, current, expires = self.eve.character_name_from_id("1")

        self.assertEqual(result, "EVE System")
        self.assertEqual(self.api.mock_calls, [
                mock.call.get('eve/CharacterName', params={'IDs': ["1"]}),
            ])
        self.assertEqual(current, 12345)
        self.assertEqual(expires, 67890)

    def test_character_ids_from_names(self):
        self.api.get.return_value = self.make_api_result("eve/character_id.xml")

        result, current, expires = self.eve.character_ids_from_names(set(["EVE System", "EVE Central Bank"]))
        self.assertEqual(result, {"EVE System":1, "EVE Central Bank":2})
        self.assertEqual(self.api.mock_calls, [
                mock.call.get('eve/CharacterID', params={'names': set(["EVE System","EVE Central Bank"])}),
            ])
        self.assertEqual(current, 12345)
        self.assertEqual(expires, 67890)

    def test_character_id_from_name(self):
        self.api.get.return_value = self.make_api_result("eve/character_id_single.xml")

        result, current, expires = self.eve.character_id_from_name("EVE System")
        self.assertEqual(result, 1)
        self.assertEqual(self.api.mock_calls, [
                mock.call.get('eve/CharacterID', params={'names': ["EVE System"]}),
            ])
        self.assertEqual(current, 12345)
        self.assertEqual(expires, 67890)

    def test_affiliations_for_characters(self):
        self.api.get.return_value = self.make_api_result("eve/character_affiliation.xml")

        result, current, expires = self.eve.affiliations_for_characters(set([92168909, 401111892, 1979087900]))
        self.assertEqual(result, {
            1979087900: {
                'id': 1979087900,
                'name': 'Marcel Devereux',
                'faction': {
                    'id': 500004,
                    'name': 'Gallente Federation'
                },
                'corp': {
                    'id': 1894214152,
                    'name': 'Aideron Robotics'
                }
            },
            401111892: {
                'id': 401111892,
                'name': 'ShadowMaster',
                'alliance': {
                    'id': 99000652,
                    'name': 'RvB - BLUE Republic'
                },
                'corp': {
                    'id': 1741770561,
                    'name': 'Blue Republic'
                }
            },
            92168909: {
                'id': 92168909,
                'name': 'CCP FoxFour',
                'alliance': {
                    'id': 434243723,
                    'name': 'C C P Alliance'
                },
                'corp': {
                    'id': 109299958,
                    'name': 'C C P'
                }
            }
        })

        self.assertEqual(self.api.mock_calls, [
            mock.call.get('eve/CharacterAffiliation', params={'ids': set([92168909, 401111892, 1979087900])})
        ])
        self.assertEqual(current, 12345)
        self.assertEqual(expires, 67890)

    def test_affiliations_for_character(self):
        self.api.get.return_value = self.make_api_result("eve/character_affiliation_single.xml")

        result, current, expires = self.eve.affiliations_for_character(92168909)
        self.assertEqual(result, {
            'id': 92168909,
            'name': 'CCP FoxFour',
            'alliance': {
                'id': 434243723,
                'name': 'C C P Alliance'
            },
            'corp': {
                'id': 109299958,
                'name': 'C C P'
            }
        })

        self.assertEqual(self.api.mock_calls, [
            mock.call.get('eve/CharacterAffiliation', params={'ids': [92168909]})
        ])
        self.assertEqual(current, 12345)
        self.assertEqual(expires, 67890)

    def test_character_info_from_id(self):
        self.api.get.return_value = self.make_api_result("eve/character_info.xml")

        result, current, expires = self.eve.character_info_from_id(1234)
        self.assertEqual(result, {
            'alliance': {'id': None, 'name': None, 'timestamp': None},
            'bloodline': 'Civire',
            'corp': {'id': 2345, 'name': 'Test Corporation', 'timestamp': 1338689400},
            'history': [
                {'corp_id': 1, 'corp_name': 'test_one', 'start_ts': 1338603000},
                {'corp_id': 2, 'corp_name': 'test_two', 'start_ts': 1318422896}
            ],
            'id': 1234,
            'isk': None,
            'location': None,
            'name': 'Test Character',
            'race': 'Caldari',
            'sec_status': 2.5,
            'ship': {'name': None, 'type_id': None, 'type_name': None},
            'skillpoints': None,
        })
        self.assertEqual(self.api.mock_calls, [
                mock.call.get('eve/CharacterInfo', params={'characterID': 1234}),
            ])
        self.assertEqual(current, 12345)
        self.assertEqual(expires, 67890)

    def test_alliances(self):
        self.api.get.return_value = self.make_api_result("eve/alliances.xml")

        result, current, expires = self.eve.alliances()
        self.assertEqual(result, {
                1: {
                    'executor_id': 2,
                    'id': 1,
                    'member_corps': {
                        2: {'id': 2, 'timestamp': 1289250660},
                        3: {'id': 3, 'timestamp': 1327728960},
                        4: {'id': 4, 'timestamp': 1292440500},
                    },
                    'member_count': 123,
                    'name': 'Test Alliance',
                    'ticker': 'TEST',
                    'timestamp': 1272717240,
                }
            })
        self.assertEqual(self.api.mock_calls, [
                mock.call.get('eve/AllianceList', params={}),
            ])
        self.assertEqual(current, 12345)
        self.assertEqual(expires, 67890)

    def test_errors(self):
        self.api.get.return_value = self.make_api_result("eve/errors.xml")

        result, current, expires = self.eve.errors()
        self.assertEqual(result, {1:"Foo", 2:"Bar"})
        self.assertEqual(self.api.mock_calls, [
                mock.call.get('eve/ErrorList', params={}),
            ])
        self.assertEqual(current, 12345)
        self.assertEqual(expires, 67890)

    def test_faction_warfare_stats(self):
        self.api.get.return_value = self.make_api_result("eve/faction_warfare_stats.xml")

        result, current, expires = self.eve.faction_warfare_stats()
        self.assertEqual(result, {
            'kills': {'total': 232772, 'week': 3246, 'yesterday': 677},
            'points': {'total': 44045189, 'week': 414049, 'yesterday': 55087},
            'factions': {
                500001: {
                    'id': 500001,
                    'kills': {'total': 59239, 'week': 627, 'yesterday': 115},
                    'name': 'Caldari State',
                    'pilots': 5324,
                    'points': {'total': 4506493, 'week': 64548, 'yesterday': 9934},
                    'systems': 61,
                },
                500002: {
                    'id': 500002,
                    'kills': {'total': 56736, 'week': 952, 'yesterday': 213},
                    'name': 'Minmatar Republic',
                    'pilots': 4068,
                    'points': {'total': 3627522, 'week': 51211, 'yesterday': 2925},
                    'systems': 0,
                },
                500003: {
                    'id': 500003,
                    'kills': {'total': 55717, 'week': 1000, 'yesterday': 225},
                    'name': 'Amarr Empire',
                    'pilots': 3960,
                    'points': {'total': 3670190, 'week': 50518, 'yesterday': 3330},
                    'systems': 11,
                },
                500004: {
                    'id': 500004,
                    'kills': {'total': 61080, 'week': 667, 'yesterday': 124},
                    'name': 'Gallente Federation',
                    'pilots': 3663,
                    'points': {'total': 4098366, 'week': 62118, 'yesterday': 10343},
                    'systems': 0,
                },
            },
            'wars': [
                    {
                        'against': {'id': 500002, 'name': 'Minmatar Republic'},
                        'faction': {'id': 500001, 'name': 'Caldari State'},
                    },
                    {
                        'against': {'id': 500004, 'name': 'Gallente Federation'},
                        'faction': {'id': 500001, 'name': 'Caldari State'},
                    },
                    {
                        'against': {'id': 500001, 'name': 'Caldari State'},
                        'faction': {'id': 500002, 'name': 'Minmatar Republic'},
                    },
                    {
                        'against': {'id': 500003, 'name': 'Amarr Empire'},
                        'faction': {'id': 500002, 'name': 'Minmatar Republic'},
                    },
                    {
                        'against': {'id': 500002, 'name': 'Minmatar Republic'},
                        'faction': {'id': 500003, 'name': 'Amarr Empire'},
                    },
                    {
                        'against': {'id': 500004, 'name': 'Gallente Federation'},
                        'faction': {'id': 500003, 'name': 'Amarr Empire'},
                    },
                    {
                        'against': {'id': 500001, 'name': 'Caldari State'},
                        'faction': {'id': 500004, 'name': 'Gallente Federation'},
                    },
                    {
                        'against': {'id': 500003, 'name': 'Amarr Empire'},
                        'faction': {'id': 500004, 'name': 'Gallente Federation'},
                    }
                ],
            })
        self.assertEqual(self.api.mock_calls, [
                mock.call.get('eve/FacWarStats', params={}),
            ])
        self.assertEqual(current, 12345)
        self.assertEqual(expires, 67890)

    def test_faction_warfare_leaderboard(self):
        self.api.get.return_value = self.make_api_result("eve/faction_warfare_leaderboard.xml")

        result, current, expires = self.eve.faction_warfare_leaderboard()
        self.assertEqual(result, {
                'char': {
                    'kills': {
                        'total': [{'id': 673662188, 'kills': 451, 'name': 'Val Erian'}],
                        'week': [{'id': 187452523,  'kills': 52, 'name': 'Tigrana Blanque'}],
                        'yesterday': [
                            {'id': 1007512845, 'kills': 14, 'name': 'StonedBoy'},
                            {'id': 646053002, 'kills': 11, 'name': 'Erick Voliffe'},
                        ],
                    },
                    'points': {
                        'total': [{'id': 395923478, 'name': 'sasawong', 'points': 197046}],
                         'week': [{'id': 161929388, 'name': 'Ankhesentapemkah', 'points': 20851}],
                         'yesterday': [{'id': 774720050, 'name': 'v3nd3tt4', 'points': 3151}],
                    },
                },
                'corp': {
                    'kills': {
                        'total': [{'id': 673662188, 'kills': 451, 'name': 'Val Erian'}],
                        'week': [{'id': 187452523,  'kills': 52, 'name': 'Tigrana Blanque'}],
                        'yesterday': [
                            {'id': 1007512845, 'kills': 14, 'name': 'StonedBoy'},
                            {'id': 646053002, 'kills': 11, 'name': 'Erick Voliffe'},
                        ],
                    },
                    'points': {
                        'total': [{'id': 395923478, 'name': 'sasawong', 'points': 197046}],
                         'week': [{'id': 161929388, 'name': 'Ankhesentapemkah', 'points': 20851}],
                         'yesterday': [{'id': 774720050, 'name': 'v3nd3tt4', 'points': 3151}],
                    },
                },
                'faction': {
                    'kills': {
                        'total': [{'id': 500004, 'kills': 104, 'name': 'Gallente Federation'}],
                        'week': [{'id': 500004, 'kills': 105, 'name': 'Gallente Federation'}],
                        'yesterday': [{'id': 500004, 'kills': 106, 'name': 'Gallente Federation'}],
                    },
                    'points': {
                        'total': [{'id': 500004, 'points': 101, 'name': 'Gallente Federation'}],
                        'week': [{'id': 500004, 'points': 102, 'name': 'Gallente Federation'}],
                        'yesterday': [{'id': 500004, 'points': 103, 'name': 'Gallente Federation'}],
                    },
                },
            })
        self.assertEqual(self.api.mock_calls, [
                mock.call.get('eve/FacWarTopStats', params={}),
            ])
        self.assertEqual(current, 12345)
        self.assertEqual(expires, 67890)

    def test_conquerable_stations(self):
        self.api.get.return_value = self.make_api_result("eve/conquerable_stations.xml")

        result, current, expires = self.eve.conquerable_stations()
        self.assertEqual(result, {
            1:{ 'id':1,
                'name':"Station station station",
                'type_id':123,
                'system_id':512,
                'corp':{
                        'id':444,
                        'name':"Valkyries of Night" }
                },
            2:{ 'id':2,
                'name':"Station the station",
                'type_id':42,
                'system_id':503,
                'corp':{
                        'id':400,
                        'name':"Deus Fides Empire"}
                }
           })
        self.assertEqual(self.api.mock_calls, [
                mock.call.get('eve/ConquerableStationlist', params={}),
            ])
        self.assertEqual(current, 12345)
        self.assertEqual(expires, 67890)

    def test_skill_tree(self):
        self.api.get.return_value = self.make_api_result("eve/skill_tree.xml")

        result, current, expires = self.eve.skill_tree()

        self.assertEqual(result, {
                255: {
                    'id': 255,
                    'name': 'Gunnery',
                    'skills': {
                        3300: {
                            'attributes': {
                                'primary': 'perception',
                                 'secondary': 'willpower',
                            },
                            'bonuses': {
                                'turretSpeeBonus': {
                                    'type': 'turretSpeeBonus',
                                    'value': -2.0,
                                },
                            },
                            'description': "Basic turret operation skill. 2% Bonus to weapon turrets' rate of fire per skill level.",
                            'group_id': 255,
                            'id': 3300,
                            'name': 'Gunnery',
                            'published': True,
                            'rank': 1,
                            'required_skills': {},
                        },
                        3301: {
                            'attributes': {
                                'primary': 'perception',
                                'secondary': 'willpower',
                            },
                            'bonuses': {
                                'damageMultiplierBonus': {
                                    'type': 'damageMultiplierBonus',
                                    'value': 5.0,
                                },
                            },
                            'description': 'Operation of small hybrid turrets. 5% Bonus to small hybrid turret damage per level.',
                            'group_id': 255,
                            'id': 3301,
                            'name': 'Small Hybrid Turret',
                            'published': True,
                            'rank': 1,
                            'required_skills': {
                                3300: {
                                    'id': 3300,
                                    'level': 1,
                                    'name': 'Gunnery',
                                },
                            },
                        },
                    },
                },
                266: {
                    'id': 266,
                    'name': 'Corporation Management',
                    'skills': {
                        11584 : {
                            'id': 11584,
                            'group_id': 266,
                            'name': 'Anchoring',
                            'description': 'Skill at Anchoring Deployables. Can not be trained on Trial Accounts.',
                            'published': True,
                            'rank': 3,
                            'attributes': {
                                'primary': 'memory',
                                'secondary': 'charisma',
                                },
                            'required_skills': {},
                            'bonuses': {
                                'canNotBeTrainedOnTrial': {
                                    'type': 'canNotBeTrainedOnTrial',
                                    'value': 1.0,
                                    }
                                }
                            },
                        3369 : {
                            'id': 3369,
                            'group_id': 266,
                            'name': 'CFO Training',
                            'description': 'Skill at managing corp finances. 5% discount on all fees at non-hostile NPC station if acting as CFO of a corp. ',
                            'published': False,
                            'rank': 3,
                            'attributes': {
                                'primary': 'memory',
                                'secondary': 'charisma',
                                },
                            'required_skills': {
                                3363 : { 'id' : 3363, 'level' : 2, 'name' : None },
                                3444 : { 'id' : 3444, 'level' : 3, 'name' : None },
                                },
                            'bonuses': {}
                            }
                        }
                    }
                })
        self.assertEqual(current, 12345)
        self.assertEqual(expires, 67890)

        self.assertEqual(self.api.mock_calls, [
                mock.call.get('eve/SkillTree', params={})
                ])


    def test_reference_types(self):
        self.api.get.return_value = self.make_api_result("eve/reference_types.xml")

        result, current, expires = self.eve.reference_types()

        self.assertEqual(result, {
                0: 'Undefined',
                1: 'Player Trading',
                2: 'Market Transaction',
                3: 'GM Cash Transfer',
                4: 'ATM Withdraw',
                5: 'ATM Deposit'
                })
        self.assertEqual(current, 12345)
        self.assertEqual(expires, 67890)

        self.assertEqual(self.api.mock_calls, [
                mock.call.get('eve/RefTypes', params={})
                ])


if __name__ == "__main__":
    unittest.main()
