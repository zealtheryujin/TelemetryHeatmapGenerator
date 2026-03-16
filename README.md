# Player Telemetry & Heatmap Generator

A Python tool for game designers and level architects to visually analyze player deaths, kills, and damage points.

## Features
- Parses `.csv` session data containing X, Y coordinates, Event Type (Death, Kill, Damage) and Timestamp.
- Generates a vibrant, Gaussian Blurred "Heatmap" of the most active/dangerous zones.
- Intended to be overlaid on top of a top-down level map image.

## How to Run
Run the batch file to automatically create a virtual environment, install dependencies (`Pillow`, `pandas`, `matplotlib`), and generate an example heatmap:
```bash
run.bat
```

## Inputs and Outputs
- **Input:** Takes session data (e.g., `data/mock_data.csv`).
- **Output:** Saves a PNG heatmap to `output/heatmap.png`.


Also I added a mock data as an example
