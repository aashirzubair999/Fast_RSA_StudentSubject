from fastapi import APIRouter, HTTPException
from db import get_db_connection
from rsa_utils import encrypt_name, decrypt_name
from models import Student
import logging

student_router = APIRouter(prefix="/student", tags=["students"])

@student_router.post("/addstudent")
async def add_student(student: Student):
    try:
        encrypted_name = encrypt_name(student.studentname)  # Use studentname
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("CALL sp_setstudentbysubjectid(%s, %s);", (student.subjectid, encrypted_name))
        conn.commit()
        cur.close()
        conn.close()
        return {"message": "Student added successfully"}
    except Exception as e:
        logging.error(f"Error adding student: {e}")
        raise HTTPException(status_code=500, detail="Failed to add student")

@student_router.get("/all/{subjectid}")
async def get_students(subjectid: int):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("BEGIN")
        cur.execute("CALL sp_getstudentbysubjectid(%s, %s);", (subjectid, "refcursor1"))
        cur.execute("FETCH ALL FROM refcursor1;")
        rows = cur.fetchall()
        cur.execute("CLOSE refcursor1")
        conn.commit()
        cur.close()
        conn.close()

        students = []
        for r in rows:
            try:
                encrypted_name = r[1]
                students.append({
                    "studentid": r[0],
                    "studentname": decrypt_name(encrypted_name),  # Use studentname
                    "subjectid": r[2]
                })
            except Exception as e:
                logging.error(f"Error decrypting student {r[0]}: {e}")
                students.append({
                    "studentid": r[0],
                    "studentname": "[Decryption Error]",  # Use studentname
                    "subjectid": r[2]
                })
        return students
    except Exception as e:
        logging.error(f"Error fetching students: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch students")

@student_router.get("/getstudent/{studentid}")
async def get_student(studentid: int):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("BEGIN")
        cur.execute("CALL sp_getstudentbystudentid(%s, %s);", (studentid, "refcursor1"))
        cur.execute("FETCH ALL FROM refcursor1;")
        rows = cur.fetchall()
        cur.execute("CLOSE refcursor1")
        conn.commit()
        cur.close()
        conn.close()

        if rows and len(rows) > 0:
            row = rows[0]
            return {
                "studentid": row[0],
                "studentname": decrypt_name(row[1]),  # Use studentname
                "subjectid": row[2]
            }
        raise HTTPException(status_code=404, detail="Student not found")
    except HTTPException:
        raise
    except Exception as e:
        logging.error(f"Error fetching student {studentid}: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch student")

@student_router.put("/update/{studentid}")
async def update_student(studentid: int, student: Student):
    try:
        encrypted_name = encrypt_name(student.studentname)  # Use studentname
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("CALL sp_updatestudentbystudentid(%s, %s, %s);", 
                   (studentid, student.subjectid, encrypted_name))
        conn.commit()
        cur.close()
        conn.close()
        return {"message": "Student updated successfully"}
    except Exception as e:
        logging.error(f"Error updating student {studentid}: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to update student: {str(e)}")