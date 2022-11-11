import asyncio
import random

import requests


async def gather_worker():
    result = await asyncio.gather(
        get_residents(),
        get_char_img(fut),
        stop_event_loop(event_loop)
    )


async def get_random_char(future):
    print("Getting random character...")
    char_id = random.randint(1, 826)
    data = requests.get(
        f"https://rickandmortyapi.com/api/character/{char_id}").json()
    future.set_result(data)
    print(f"Got character: '{data['name']}'.")
    return data


async def get_char_img(future):
    print("Getting character image...")
    data = await future
    img = requests.get(data["image"])
    if img.status_code == 200:
        img_name = data["name"].replace(" ", "_").lower() + ".jpg"
        with open(img_name, 'wb') as f:
            f.write(img.content)
        print(f"Saved image: '{img_name}'.")


async def get_residents():
    print("Getting residents...")
    data = await get_random_char(fut)
    resident_origin = data["origin"]["name"]
    print(f'Got resident origin: {resident_origin}')
    response = requests.get(
        f"https://rickandmortyapi.com/api/location?name={resident_origin}").json()
    residents_links = response["results"][0]["residents"]
    print("Got residents with the same origin:")
    for resident in residents_links:
        await get_resident_name(resident)


async def get_resident_name(link):
    response = requests.get(link).json()
    print(response['name'])
    return response["name"]


async def stop_event_loop(loop):
    loop.stop()
    print('Stopped')


event_loop = asyncio.new_event_loop()
fut = event_loop.create_future()

event_loop.create_task(gather_worker())

event_loop.run_forever()
event_loop.close()
