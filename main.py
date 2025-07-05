from fastapi import FastAPI
from routers.route import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://froas.github.io", 
        "https://froas.github.io/react-openapi-sugarfree"
    ],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"]

)

app.include_router(router)