#!/usr/bin/env python

import asyncio
import websockets
import json


async def adjustText(websocket, path):
    jsonObject = await websocket.recv()
    text_array = json.loads(jsonObject)
    print(f"< {text_array}")

    modified_text = [text.upper() for text in text_array]

    await websocket.send(json.dumps(modified_text))
    print(f"> {modified_text}")


start_server = websockets.serve(adjustText, "localhost", 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
