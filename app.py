import os
import psycopg2
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

def get_conn():
    # Open a connection using the URL from the environment.
    return psycopg2.connect(os.environ["DATABASE_URL"])

@app.on_event("startup")
def startup():
    # When uvicorn starts: create the table if it is missing.
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL
        )
        """
    )
    conn.commit()
    cur.close()
    conn.close()

@app.get("/health")
def health():
    return {"status": "ok"}

class TaskIn(BaseModel):
    title: str

@app.post("/tasks")
def create_task(item: TaskIn):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO tasks (title) VALUES (%s) RETURNING id, title",
        (item.title,),
    )
    row = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return {"id": row[0], "title": row[1]}

@app.get("/tasks")
def list_tasks():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, title FROM tasks ORDER BY id")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"id": r[0], "title": r[1]} for r in rows]
