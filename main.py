from fastapi import FastAPI

from routers import items
from routers import users

app = FastAPI()

app.include_router(users.router)
app.include_router(items.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
