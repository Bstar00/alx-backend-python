#!/usr/bin/env python3
"""
Complex types - functions of multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float
    """
    def multiplies(n: float):
        """
        multiplies two numbers
        """
        return n * multiplier
    return multiplies
