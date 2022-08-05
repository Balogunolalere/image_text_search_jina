from fastapi import FastAPI
from app.api.v1.api import router as api_router
import uvicorn





app = FastAPI()





@app.get('/')
async def root():
    return {"message": "Hello World"}


app.include_router(api_router, prefix='/api/v1')

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000, reload=True)

