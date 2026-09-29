from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from app.services.image_generator import generate_comic_image


router = APIRouter()

templates = Jinja2Templates(
    directory="app/templates"
)


class ComicRequest(BaseModel):

    story: str

    characters: str = ""

    style: str = "Modern Comic"

    panels: int = 4


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@router.post("/generate")
async def generate_comic(data: ComicRequest):

    try:

        image_url = generate_comic_image(
            story=data.story,
            characters=data.characters,
            style=data.style,
            panels=data.panels
        )

        return {
            "success": True,
            "image_url": image_url
        }

    except Exception as error:

        # IMPORTANT:
        # Show technical error in terminal,
        # not on the website.

        print("\n==============================")
        print("COMIC GENERATION ERROR")
        print("==============================")
        print(error)
        print("==============================\n")

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": "Comic generation is temporarily unavailable."
            }
        )