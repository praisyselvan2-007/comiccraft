# ComicCraft
# AI Comic Story Creator using Gemini Models

ComicCraft is an AI-powered web application
that converts a user's story idea into a
multi-panel comic.

The application uses:

- FastAPI
- Jinja2
- Gemini
- Pillow
- FPDF2
- HTML
- CSS
- JavaScript


## FEATURES

1. Story prompt input
2. Character name
3. Setting selection
4. Story tone selection
5. Art style selection
6. AI story outline generation
7. AI narration generation
8. AI dialogue generation
9. AI image generation
10. Comic preview
11. PDF export
12. Export success page


## PROJECT FLOW

User

↓

Create Your Comic

↓

Gemini Story Outline

↓

Gemini Narration / Dialogue

↓

Comic Image Generation

↓

Comic Preview

↓

PDF Export

↓

Success Page


## INSTALLATION

Open PowerShell:

cd C:\ComicCraft


Create virtual environment:

python -m venv comiccraft-env


Activate:

.\comiccraft-env\Scripts\Activate.ps1


Install:

pip install -r requirements.txt


## CONFIGURATION

Create .env:

GEMINI_API_KEY=YOUR_KEY

GEMINI_TEXT_MODEL=gemini-2.5-flash

GEMINI_IMAGE_MODEL=gemini-2.5-flash-image


## RUN

python -m uvicorn app.main:app --reload


Open:

http://127.0.0.1:8000


## API DOCUMENTATION

http://127.0.0.1:8000/docs


## PAGES

/

Create Your Comic page


/generate

Comic generation POST endpoint


/generate-comic/json

JSON generation API


/test-image

Image generation test


/export-pdf

PDF generation


/export-success

Export success page


## GENERATED FILES

Comic images:

app/static/panels/


PDF files:

app/static/exports/