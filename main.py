from fastapi import FastAPI
from app.api.v1.api import router as api_router





app = FastAPI(
    title='Now Image | Text -> Image Search',
    description='Text | Image -> Image Search',
    version='1.0.0',
    contact={
        "name": "bandersnatchx64",
        "url": "https://twitter.com/bandersnatchx64",
        "email": "lordareello@gmail.com",
    },
)


TITLE = 'Jina Image | Text -> Image Search'
DESCRIPTION = 'Jina Image | Text -> Image Search Api'
AUTHOR = 'Bandersnatchx64'
EMAIL = 'lordareello@gmail.com'
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

