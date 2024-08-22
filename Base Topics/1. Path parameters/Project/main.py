from fastapi import FastAPI

from controllers import vehicle_router, engine_router


app = FastAPI(title='Project for path operations learning', version='1.0')

app.include_router(vehicle_router)
app.include_router(engine_router)
