import uvicorn
from fastapi import FastAPI, WebSocket
from multiprocessing import Queue

app = FastAPI()


@app.websocket("/ws")
async def test(websocket: WebSocket):
    await websocket.accept()
    while True:
        text = app.queue.get()
        print(f"[WEB]:\t Got {text}")
        if text:
            print(f"[WEB]:\t Sending: {text}")
            await websocket.send_text(text)


if __name__ == "__main__":
    uvicorn.run("app:app")
