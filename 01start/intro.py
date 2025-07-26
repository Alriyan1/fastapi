from fastapi import FastAPI
import uvicorn

app=FastAPI()

@app.get('/')
def index():
    return {'message':'Hello, world'}

@app.get('/Welcome')
def get_name(name: str):
    return {f'Welcome to {name} learning fastapi '}

if __name__=='__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)
