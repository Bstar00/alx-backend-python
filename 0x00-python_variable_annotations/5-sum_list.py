#!/usr/bin/env python3
"""
Complex types - list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of the elements in a list of floats.
    
    Args:
        input_list (List[float]): A list of floating-point numbers.
        
    Returns:
        float: The sum of the elements in the input list.
    """
    return sum(input_list)
