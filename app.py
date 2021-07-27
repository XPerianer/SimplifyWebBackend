#!/usr/bin/env python

import asyncio
import websockets
import json

from extractive_summarization import summarize


async def adjustText(websocket, path):
    json_object = await websocket.recv()
    req = json.loads(json_object)
    print(f"Req: {req}")
    text_array = req["text"]

    modified_text = [summarize(text, req["options"]["shortness"] / 100) for text in text_array]

    await websocket.send(json.dumps(modified_text))
    print(f"> {modified_text}")


start_server = websockets.serve(adjustText, "localhost", 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
