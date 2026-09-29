import os

from dotenv import load_dotenv


# Load variables from .env
load_dotenv()


# Gemini API key
GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY",
    ""
).strip()


# Gemini text model
TEXT_MODEL = os.getenv(
    "GEMINI_TEXT_MODEL",
    "gemini-2.5-flash"
)


# Gemini image model
IMAGE_MODEL = os.getenv(
    "GEMINI_IMAGE_MODEL",
    "gemini-2.5-flash-image"
)