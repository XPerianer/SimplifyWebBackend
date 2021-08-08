#!/usr/bin/env python

import asyncio
import websockets
import json

from extractive_summarization import summarize


async def adjustText(websocket, path):
    json_object = await websocket.recv()
    req = json.loads(json_object)
    #print(f"Req: {req}")
    text_array = req["text"]
    print(req["options"])

    print(f"\n\nsummarizing {len(text_array)} paragraphs")
    modified_text = []
    for text in text_array:
        score = req["options"]["shortness"] / 100
        summary_text = summarize(text,  score)
        modified_text.append(summary_text)
        print(f">> ratio {len(summary_text) / len(text)}\t score {score}")


    await websocket.send(json.dumps(modified_text))
    # print(f"> {modified_text}")


start_server = websockets.serve(adjustText, "localhost", 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
