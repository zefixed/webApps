@echo off
git pull
echo:
echo [36mДобавляем?[0m
pause > nul
git add *
git status
set /p commit="[36mПушим? (Введи имя коммита, Diff - по умолчанию):[0m"
IF "%commit%" == "" set commit=Diff
git commit -m "%commit%"
git push
pause > nul