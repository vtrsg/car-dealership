from fastapi import FastAPI

from backend.routes import auth, brands, types, users

app = FastAPI()

app.include_router(auth.router)
app.include_router(brands.router)
app.include_router(types.router)
app.include_router(users.router)
