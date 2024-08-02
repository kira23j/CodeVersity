from fastapi import FastAPI

app=FastAPI()

@app.get('/root')
def index():
    return {"hello there pal "}