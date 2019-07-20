import unittest
from service import get_configs, get_all_configs, add_config, remove_config, update_config_by_name, search_by_query
unittest.TestLoader.sortTestMethodsUsing=None

class TestStringMethods(unittest.TestCase):

    def test1_get_all_configs(self):
        c1 = get_all_configs()
        self.assertEqual(len(c1), 2)

    def test2_get_config_by_name(self):
        c2 = get_configs("datacenter-2")
        c2_result= [{'name': 'datacenter-2', 'metadata': {'monitoring': {'enabled': True}, 'limits': {'cpu': {'enabled': True}}}}]
        self.assertEqual(c2, c2_result)

    def test3_add_config_by_name(self):
        add_config("datacenter-3", True, False)
        c3_result= get_configs("datacenter-3")
        self.assertEqual(len(c3_result), 1)
        c1_new = get_all_configs()
        self.assertEqual(len(c1_new), 3)

    def test4_remove_config(self):
        add_config("datacenter-4", True, False)
        c4 = get_configs("datacenter-4")
        self.assertEqual(len(c4), 1)
        remove_config("datacenter-4")
        c5 = get_configs("datacenter-4")
        self.assertEqual(len(c5), 0)

    def test5_update_config_by_name(self):
        add_config("datacenter-5", True, False)
        c5 = get_configs("datacenter-5")
        c5_result = [{'name': 'datacenter-5','metadata': {'monitoring': {'enabled': True}, 'limits': {'cpu': {'enabled': False}}}}]
        self.assertEqual(c5, c5_result)
        c6_tobe = {'name': 'datacenter-5','metadata': {'monitoring': {'enabled': False}, 'limits': {'cpu': {'enabled': True}}}}
        update_config_by_name("datacenter-5", c6_tobe)
        c6=get_configs("datacenter-5")
        self.assertEqual(c6[0], c6_tobe)

    def test6_search_by_query(self):
        add_config("datacenter-6", False, False)
        c7_tobe = get_configs("datacenter-6")
        c7=search_by_query("metadata.monitoring.enabled", "false")
        self.assertIn(c7_tobe[0], c7)


if __name__ == '__main__':
    unittest.main()
