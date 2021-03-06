import asyncio

import websockets


# create handler for each connection

async def handler(websocket, path):
    data = await websocket.recv()

    reply = f"Data received as:  {data} and returned by server"

    await websocket.send(reply)


start_server = websockets.serve(handler, "0.0.0.0", 8080)

asyncio.get_event_loop().run_until_complete(start_server)

asyncio.get_event_loop().run_forever()
