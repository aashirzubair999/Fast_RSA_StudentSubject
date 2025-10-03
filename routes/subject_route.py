# from fastapi import APIRouter, HTTPException
# from db import get_db_connection
# import psycopg2
# from models import SubjectCreate

# subject_router = APIRouter(prefix="/subject", tags=["subjects"])

# @subject_router.post("/addsubject")
# async def add_subject(subject: SubjectCreate):
#     try:
#         conn = get_db_connection()
#         cur = conn.cursor()

#         # Call stored procedure
#         cur.execute("CALL sp_setsubjects(%s, %s);", (subject.subjectname, subject.subjectinfo))

#         conn.commit()
#         cur.close()
#         conn.close()

#         return {"message": "Subject added successfully"}

#     except psycopg2.Error as e:
#         raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Something went wrong: {str(e)}")  


from fastapi import APIRouter, HTTPException
from db import get_db_connection
import psycopg2
from models import Subject

subject_router = APIRouter(prefix="/subject", tags=["subjects"])

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