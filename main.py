from fastapi import FastAPI
from web import borrowings as borrow_router

app = FastAPI()
app.include_router(borrow_router.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host='0.0.0.0', reload=True)
