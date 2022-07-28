import unittest
from knapsack import find_max_value_items, find_all_combinations, find_combinations_satisfy_weight_limit


class MyTestCase(unittest.TestCase):
    def test_knapsack(self):
        knapsack = [{"weight": 5, "value": 10}, {"weight": 4, "value": 40}, {"weight": 6, "value": 30},
                    {"weight": 4, "value": 50}]
        weight_limit = 10
        items = find_max_value_items(knapsack, weight_limit)
        self.assertEqual(items, [1, 3])

    def test_combinations(self):
        number_of_items = 3
        combinations = list(find_all_combinations(number_of_items))
        self.assertEqual(combinations, [[], [0], [1], [2], [0, 1], [0, 2], [1, 2]])

    def test_combinations_satisfy_weight_limit(self):
        knapsack = [{"weight": 5, "value": 50}, {"weight": 4, "value": 40}, {"weight": 6, "value": 30}]
        weight_limit = 10
        combinations = find_combinations_satisfy_weight_limit(knapsack, weight_limit)
        self.assertEqual([[], [0], [1], [2], [0, 1], [1, 2]], combinations)


if __name__ == '__main__':
    unittest.main()
