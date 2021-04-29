from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette import status
from app.api import router as main_router
from sqlalchemy.exc import IntegrityError

app = FastAPI()

app.include_router(main_router, prefix="/api")

@app.exception_handler(IntegrityError)
def db_exc_handler(req: Request, exc: IntegrityError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content = {
            "info": "Database Operation Error",
            "detail": str(exc).split(' ')[0]
        }
    )