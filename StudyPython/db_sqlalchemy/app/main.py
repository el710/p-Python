"""
    Project people & books

    ORM - object-relatio model: database objects use as python objects

    install fastapi package with all requirments:
    pip install "fastapi[all]"
                + sqlalchemy - sinchronic work with database...
                + alembic

    after making models
    make "migrations" folder in Project root directory for checkup relations betweeen modules
    >alembic init
    and configure it in alembic.ini & env.py ...

    1. make migration(version)
    > alembic revision --autogenerate -m "init migration" - first migration

    2. upgrade
    > alembic upgrade head

"""

from fastapi import FastAPI
from routes.owner import router as user_router
import uvicorn

app = FastAPI()
app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)
