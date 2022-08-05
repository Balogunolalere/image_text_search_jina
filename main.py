from fastapi import FastAPI
from app.api.v1.api import router as api_router





app = FastAPI()


TITLE = 'Jina NOW'
DESCRIPTION = 'The Jina NOW service API'
AUTHOR = 'Jina AI'
EMAIL = 'hello@jina.ai'
__version__ = 'latest'



@app.get('/')
async def root():
    #return {"message": "Hello World"}
    return {
        "title": TITLE,
        "description": DESCRIPTION,
        "author": AUTHOR,
        "email": EMAIL,
        "version": __version__,
    }

app.include_router(api_router, prefix='/api/v1')

