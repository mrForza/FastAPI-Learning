from fastapi import FastAPI

from controllers import user_router, order_router


app = FastAPI(title='A query-params and request bodies project', version='1.0')

app.include_router(user_router)
app.include_router(order_router)
