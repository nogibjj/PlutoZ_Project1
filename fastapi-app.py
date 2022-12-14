from fastapi import FastAPI
import uvicorn
from dblib.querydb import querydb

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Databricks"}


@app.get("/query")
async def query():
    """Excute a SQL query"""

    result = querydb()
    return {"The unemployment rate is": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")