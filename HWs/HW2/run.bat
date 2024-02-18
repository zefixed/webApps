@echo off
echo Wait...
chcp 1251 > nul
python -m venv venv
call venv\Scripts\activate
pip install pytest
@echo on
pytest test.py -vv
@echo off
echo Press any key to exit...
pause > nul
