from collections import namedtuple
import random

Array = namedtuple('Array', ['length', 'minimum', 'maximum', 'item', 'isSequential'])
Number = namedtuple('Number', ['minimum', 'maximum', 'isInteger'])


def create_random_number(item_constraint: Number):
    if type(item_constraint) == Number:
        if item_constraint.isInteger:
            return random.randint(item_constraint.minimum, item_constraint.maximum)
        else:
            generate_positive = random.random() > 0.5
            has_negative = item_constraint.minimum < 0
            return random.randint() * item_constraint.maximum \
                if generate_positive or not has_negative else item_constraint.minimum


def create_array_edge_cases(constraints: Array, extreme=False):
    edge_cases = [
        [],
    ]

    if constraints.isSequential:
        pass
    else:
        pass

    if extreme:
        edge_cases.append(None)

    return edge_cases


def create_number_edge_cases(constraints: Number, extreme=False):
    edge_cases = [
        constraints.minimum,
        constraints.maximum,
    ]

    if constraints.minimum < 0:
        edge_cases.append(0)

    if extreme:
        edge_cases.append(None)

    return edge_cases


def create_edges(var_map: {}, extreme=False):
    factory_map = {
        Array: create_array_edge_cases,
        Number: create_number_edge_cases
    }

    return {key: factory_map[type(var_map[key])](var_map[key], extreme) for key in var_map.keys()}


if __name__ == '__main__':
    number = Number._make([-pow(10, 9), pow(10, 9), True])
    variable_map = {
        'numbs': Array._make([pow(10, 5), -pow(10, 9), pow(10, 9), number, True]),
        'target': number
    }

    generated_edge_cases = create_edges(variable_map)

    print(generated_edge_cases)
