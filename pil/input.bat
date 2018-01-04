@echo off
::显示并返回文件名
if "%~nxp1" == "" goto :eof
set "getname=%~nxp1"
python pil.py %getname% 
echo 处理完毕,任意键退出
pause