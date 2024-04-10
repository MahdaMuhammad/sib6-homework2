from fastapi import FastAPI
from fastapi.responses import JSONResponse
from decouple import config
import psycopg2

app = FastAPI()


@app.get("/")
def main():
    # get connection
    try:
        conn_pg = psycopg2.connect(
            host=config('MB_DB_HOST'),
            database=config('MB_DB_DBNAME'),
            user=config('MB_DB_USER'),
            password=config('MB_DB_PASS'),
            port=int(config('MB_DB_PORT'))
        )
        conn_pg.close()
        return {"status": 500, "db": "connected"}
    except psycopg2.Error as e:
        return JSONResponse(status_code=500, content={"error": str(e)})


@app.get("/health")
def health():
    return {"status": "Sukses"}
