import asyncio
import websockets


async def main():
    async with websockets.connect("ws://localhost:9001") as websocket:
        message = "hello,server!"
        await websocket.send(message)
        print(f"Sent:{message}")

        response = await websocket.recv()
        print(f"Received: {response}")

asyncio.run(main())
