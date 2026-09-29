@echo off

call comiccraft-env\Scripts\activate

python -m uvicorn app.main:app --reload

pause