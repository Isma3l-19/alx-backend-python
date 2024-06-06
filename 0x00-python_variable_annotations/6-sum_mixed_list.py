#!/usr/bin/env python3
"""
a function that takes a list of floats and intergers
"""

def sum_mixed_list(mxd_lst: int | float) -> float:
    """
    a type-annotated function sum_mixed_list which takes a list mxd_lst of integers and floats
    and returns their sum as a float.
    """
    return sum(float(mxd_lst))