from fastapi import APIRouter, HTTPException
from db import get_db_connection
import psycopg2
from models import Subject

# Define the router for subjects
subject_router = APIRouter(prefix="/subject", tags=["subjects"])

# Add subject endpoint
@subject_router.post("/addsubject")
async def add_subject(subject: Subject):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("CALL sp_setsubjects(%s, %s);", (subject.subjectname, subject.subjectinfo))
        conn.commit()
        cur.close()
        conn.close()
        return {"message": "Subject added successfully"}
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Something went wrong: {str(e)}")