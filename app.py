from quart import Quart, render_template, websocket

app = Quart(__name__)

@app.route("/")
async def hello():
    return 'Done'

@app.route("/api")
async def json():
    return {"hello": "world"}

@app.websocket("/ws")
async def ws():
    await websocket.send_json('Hello')
    while True:
        res= await websocket.receive()
        await websocket.send(res)
        
if __name__ == "__main__":
    app.run(debug=True, port=4000)