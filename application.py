from fastapi import FastAPI
from routes.home_route import home_router
# from routers.subject_router import subject_router
# from routers.student_router import student_router

app = FastAPI(
    title="Student-Subject API",
    description="FastAPI implementation of Student-Subject management system",
    version="1.0.0"
)

# Include routers
app.include_router(home_router)
# app.include_router(subject_router)
# app.include_router(student_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("application:app", host="0.0.0.0", port=8000, reload=True)