import sqlite3

from dotenv import load_dotenv
load_dotenv()

from retrieval import Retrieval
from models import csModel

from fastapi import FastAPI
app = FastAPI()

@app.get("/health")
def works_check():
    return {"status": "ok"}

@app.post("/chat")
def chat(payload: csModel):
    try:
        res = Retrieval().ask(payload.question)
        return {"answer": res}
    except Exception as e:
        return {"error": str(e)}

@app.get("/history")
def history():
    records = []
    try:
        conn = sqlite3.connect("database/data.db")

        with conn:
            query = """
            SELECT user_prompt, system_answer FROM conversation ORDER BY created_at DESC LIMIT 5;"""
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()

            header = [desc[0] for desc in cursor.description]

            records = [dict(zip(header, row)) for row in rows]

        return {"records": records}
    except Exception as e:
        return {"error": str(e)}
