#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure the tuples have at least two elements,
    # filling with zeros if necessary
    tuple_a = tuple_a + (0,) * (2 - len(tuple_a))
    tuple_b = tuple_b + (0,) * (2 - len(tuple_b))

    # Add the corresponding elements of the tuples
    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return new_tuple
