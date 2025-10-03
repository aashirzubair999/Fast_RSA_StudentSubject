from fastapi import FastAPI
from routes.home_route import home_router
from routes.subject_route import subject_router
from routes.student_route import student_router

application = FastAPI(
    title="Student-Subject API",
    description="FastAPI implementation of Student-Subject management system",
    version="1.0.0"
)

# Include routers
application.include_router(home_router)
application.include_router(subject_router)
application.include_router(student_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("application:application", port=8000, reload=True)