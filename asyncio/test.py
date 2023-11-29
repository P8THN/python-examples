import asyncio
import aiohttp


# zum Zerlegen der Liste und initieren von koroutinen
async def prepare(numbers):
    async with aiohttp.ClientSession() as session:
        koroutinen = [get(session, number) for number in numbers]
        return await asyncio.gather(*koroutinen)
    

async def get(session, no):
    print(f"startet: {no}")
    url = f"https://hub.dummyapis.com/delay?seconds={no}"
    async with session.get(url) as response:
        feedback = await response.text()
        print(f"done: {no}")
        return feedback
    

numbers = [2.2,2.1,2.2,2.3,2.4,2.5,5,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,3,3,3,6]

feedbacks = asyncio.run(prepare(numbers))