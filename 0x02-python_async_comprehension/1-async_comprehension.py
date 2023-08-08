#!/usr/bin/env python3
"""
Async comprehension function
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    async_comprehension 
    """
    valuesList = [_ async for _ in async_generator()]
    return valuesList
