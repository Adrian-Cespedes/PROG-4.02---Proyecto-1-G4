@echo off

python src\__main__.py

rd /S /Q src\__pycache__
rd /S /Q src\functions\__pycache__
rd /S /Q src\functions\importsl\__pycache__
