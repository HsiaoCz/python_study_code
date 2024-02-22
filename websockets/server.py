import websockets
import asyncio


async def echo(websocket, path):
    async for message in websockets:
        print(f"Received message:{message}")
        await websockets.send(f"Echo:{message}")


start_server = websockets.serve(echo, "localhost", 9001)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
