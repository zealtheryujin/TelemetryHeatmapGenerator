@echo off
title TelemetryHeatmapGenerator - Made by Zeal
cd /d "%~dp0"

echo.
echo  =============================================
echo   Player Telemetry ^& Heatmap Generator
echo   Made by Zeal
echo  =============================================
echo.

if not exist "venv" (
    echo [*] Creating virtual environment...
    python -m venv venv
)

call venv\Scripts\activate.bat

echo [*] Installing dependencies...
pip install -r requirements.txt -q

echo.
echo [*] Generating Heatmap...
echo     Input : data\mock_data.csv
echo     Output: output\heatmap.png
echo.

if not exist "output" mkdir output

python src/main.py --input data/mock_data.csv --output output/heatmap.png --blur_radius 15

echo.
echo [+] Completed! Output: output\heatmap.png
echo.
pause
