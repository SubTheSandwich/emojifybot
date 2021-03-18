@echo off
title Emojify
:loop
echo Ran file!
main.py
echo Waiting 5 seconds till next try...
timeout /t 5
goto loop