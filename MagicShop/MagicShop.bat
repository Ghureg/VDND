@ echo off
title MagicSpellsScripts
color 0d
cls
python ./lib/MagicGetter.py
cls
start "" %~dp0/lib/Spells.txt"
cls
exit
