REM add the Registry value
REM REG ADD KeyName [/v ValueName | /ve] [/t Type] [/s Separator] [/d Data] [/f]
REM Name lowbattery
REM Data path of the vbs
REM /f  Force overwriting the existing registry entry without prompt.
REG ADD "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run" /v "lowbattery" /t REG_SZ /d "D:\lowbattery\lowbattery.vbs" /f
pause