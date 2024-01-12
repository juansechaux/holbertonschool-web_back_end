#!/usr/bin/env python3
'''coroutine called async_generator
that takes no arguments'''

import asyncio
import random
from typing import Generator, List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List:
    '''The coroutine will loop 10 times,
    each time asynchronously wait 1 second,
    then yield a random number between 0 and 10'''
    list_r = [num async for num in async_generator()]
    return list_r
