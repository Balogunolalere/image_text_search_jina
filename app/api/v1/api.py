from fastapi import APIRouter

from app.api.v1.routers import img2image, text2image


router = APIRouter()


router.include_router(img2image.router, prefix='/img2image', tags=['Image -> Image'])
router.include_router(text2image.router, prefix='/text2image', tags=['Text -> Image'])