@echo off
::��ʾ�������ļ���
if "%~nxp1" == "" goto :eof
set "getname=%~nxp1"
python pil.py %getname% 
echo �������,������˳�
pause