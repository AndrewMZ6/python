import httpx, asyncio


resp: list = []


async def main() -> None:
    urls: list[str] = [
        "https://jsonplaceholder.typicode.com/posts",
        "https://pokeapi.co/api/v2/pokemon/1",
        "https://dog.ceo/api/breeds/image/random",
        "https://catfact.ninja/fact",
        "https://official-joke-api.appspot.com/random_joke",
        "https://bored-api.appbrewery.com/random",
        "https://reqres.in/api/users"
    ]
    async with httpx.AsyncClient() as client:
        for url in urls:
            r = await client.get(url)
            resp.append(r)

    print(resp)


asyncio.run(main())
