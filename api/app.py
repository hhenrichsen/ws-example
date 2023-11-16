import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from multiprocessing import Queue

app = FastAPI()


@app.websocket("/ws")
async def test(websocket: WebSocket):
    await websocket.accept()
    print(f"[WEB]:\t Accepted Socket")
    try:
        while True:
            text = ""
            while not app.queue.empty():
                part = app.queue.get()
                text += " " + part
                print(f"[WEB]:\t Got {part}")
            if text:
                print(f"[WEB]:\t Sending: {text}")
                await websocket.send_text(text.strip())
                await websocket.receive()
    except WebSocketDisconnect:
        print(f"[WEB]:\t Closed Socket")
        await websocket.close()


if __name__ == "__main__":
    uvicorn.run("app:app")
