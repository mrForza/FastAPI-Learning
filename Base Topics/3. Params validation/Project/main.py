from fastapi import FastAPI

from controllers import user_router

app = FastAPI(title='Path-Query params validation', version='1.0')

app.include_router(user_router)
