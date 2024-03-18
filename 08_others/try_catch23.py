import asyncio

async def handle23(p1,p2):
    print("rcvd param ===> ", p1)
    if(p1 == 'amrica'):
        try:
            for i in range(5):
                print(i, end='__')
            if (p2 == 'throw23'):
                raise Exception("sorry, phattuuu")
        except Exception as e23:
            print("\nthis is the exception ==> ", e23)
    elif (p1 == 'espana'):
        print("inside elif block ===> ")

asyncio.run(handle23('amrica', 'throw23'))