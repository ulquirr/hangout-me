from fastapi import FastAPI
from hangout import  models
from hangout.database import engine
from hangout.routers import hangout
from hangout.routers import user
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


models.Base.metadata.create_all(engine)

app.include_router(hangout.router)
app.include_router(user.router)