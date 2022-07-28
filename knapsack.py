# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from itertools import combinations


def sum_field(indexes, knapsack, field_name) -> int:
    result = 0
    for idx in indexes:
        result += knapsack[idx][field_name]
    return result


def find_max_value_items(knapsack, weight_limit):
    all_combination_knapsacks = find_combinations_satisfy_weight_limit(knapsack, weight_limit)
    max_total_value = 0
    max_total_items = None
    for combination in all_combination_knapsacks:
        total_value = sum_field(combination, knapsack, 'value')
        if total_value > max_total_value:
            max_total_value = total_value
            max_total_items = combination
    return max_total_items


def find_all_combinations(length):
    iterable = range(length)
    for i in iterable:
        for c in combinations(iterable, i):
            yield list(c)


def find_combinations_satisfy_weight_limit(knapsack, weight_limit):
    all_combinations = find_all_combinations(len(knapsack))
    result = list(filter(lambda c: sum_field(c, knapsack, "weight") <= weight_limit, all_combinations))
    return result


