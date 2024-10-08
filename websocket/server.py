# -*- coding: utf8 -*-

import asyncio
import websockets
async def handler(websocket, path):
    try:
        while True:
            message = await asyncio.wait_for(websocket.recv(),timeout=120)
            print(f"Received message: {message}")
            await websocket.send(f"Echoing back: {message}")
    except asyncio.TimeoutError:
        print("WebSocket connection timed out")
    except websockets.exceptions.ConnectionClosed:
        print("WebSocket connection closed")
async def main():
    async with websockets.serve(handler, "0.0.0.0", 9000):
        print("WebSocket server started")
        await asyncio.Future()  # run forever
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())








