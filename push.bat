@echo off
git pull
echo:
echo [36m������塞?[0m
pause > nul
git add *
git status
set /p commit="[36m��訬? (����� ��� ������, Diff - �� 㬮�砭��):[0m"
IF "%commit%" == "" set commit=Diff
git commit -m "%commit%"
git push
pause > nul