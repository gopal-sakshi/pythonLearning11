import asyncio

def main(a, b):
    res = asyncio.run(async_main(a, b))
    print(f"in main, result is {res}")

async def funcA(a, b):
    print('funcA - start')
    await asyncio.sleep(3)
    result = (a+b) # some processing done here
    print('funcA - end')

    return result

async def funcB(a, b):
    print('funcB - start')
    await asyncio.sleep(3)
    result = (a+b)*2 # some processing done here
    print('funcB - end')
    return result

async def funcC(a, b):
    print('funcC - start')
    await asyncio.sleep(3)
    result = (a+b)*3 # some processing done here
    print('funcC - end')

    return result

async def async_main(a, b):
    print("in async_main")
    res = await asyncio.gather(funcA(a, b), funcB(a, b), funcC(a, b))
    print(f"in async_main, result is {res}")
    return res

if __name__ == "__main__":
    main(1, 2)