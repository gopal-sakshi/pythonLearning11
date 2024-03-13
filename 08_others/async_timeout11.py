
import asyncio

######## it seems there is no hoisting in python
async def inner23():
    print('some inner func')
    
### two ways to use import
# ###### APPROACH I
# import async_timeout
# async def usingTimeout11():
#     async with async_timeout.timeout(5000):
#         print('I got executed after 5 seconds timeout ')
# asyncio.run(usingTimeout11())

###### APPROACH II
from async_timeout import timeout
async def usingTimeout12():
    async with timeout(5000):           ### "with timeout" (deprecated); use "async with timeout"
        await inner23()             
        print('if inner23 is executed within 5 seconds - nothing happens')
        print('if inner23 is takes more than 5 seconds - its cancelled')
asyncio.run(usingTimeout12())


# ######## it seems there is no hoisting in python
# async def inner23():
#     print('some inner func')