#!/usr/bin/env python3
'''coroutine called async_generator
that takes no arguments'''

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''The coroutine will loop 10 times,
    each time asynchronously wait 1 second,
    then yield a random number between 0 and 10'''
    for n in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)