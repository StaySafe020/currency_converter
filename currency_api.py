import asyncio
import websockets

async def consumer_handler(websocket, path):
    while True:
        # Fetch exchange rates from the API
        # ... (code to fetch rates using requests or other libraries)
        await websocket.send(json.dumps(exchange_rates))
        await asyncio.sleep(60)  # Update every 60 seconds

async def main():
    async with websockets.serve(consumer_handler, "localhost", 8765):
        await asyncio.Future()  # Run forever

asyncio.run(main())