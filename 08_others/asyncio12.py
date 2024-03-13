import asyncio

async def fetch_text() -> str:
    return "text 2323"

async def show_something():
    something = await fetch_text()
    print(something)

### throws ERROR "await" allowed only within async function
# await show_something()

### RuntimeWarning: 'show_something' was never awaited
# show_something()
    
######## WORKSSSSSSSSSSSSSSSSSSSS
asyncio.run(show_something())