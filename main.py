from fastapi import FastAPI

import app_statistic

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
