# Water Meter Reading System

This project involves the creation of a water meter reading system using YOLOv8 for training, a Raspberry Pi for image capture, and a data processing pipeline that saves readings in a JSON file, which are then converted to a CSV file.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Hardware Requirements](#hardware-requirements)
3. [Software Requirements](#software-requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Data Processing](#data-processing)
7. [Results](#results)
8. [License](#license)

## Project Overview
The water meter reading system is designed to automate the process of collecting and storing water meter readings. The system utilizes a Raspberry Pi to capture images of the water meter, which are then processed using a YOLOv8 model to detect and read the meter values. The readings are saved in a JSON file and later converted to a CSV file for further analysis.

![System Overview](images/system_overview.png)

## Hardware Requirements
- Raspberry Pi (any version with a camera module)
- Water meter with a visible dial or digital display
- Power supply for Raspberry Pi
- MicroSD card for Raspberry Pi (minimum 16GB)

## Software Requirements
- Raspberry Pi OS (Raspbian)
- Python 3.x
- TensorFlow 2.x
- OpenCV
- YOLOv8

## Installation
1. Install Raspberry Pi OS on your Raspberry Pi.
2. Install Python 3.x and the required packages:
```bash
pip install ultralytics pathlib json csv
```
3. Clone this repository and navigate to the project directory:
```bash
https://github.com/gauravdesale8/water_meter_reading.git
cd water_meter_reading
```
4. Follow the instructions in the YOLOv8 repository to download the pre-trained weights and configure the model for water meter detection.

## Usage
1. Connect the Raspberry Pi camera module to your Raspberry Pi.
2. Position the camera to capture clear images of the water meter.
3. Run the `main.py` script to begin the detections:
```bash
python main.py
```
4. The script will automatically detect and preprocess the images using the YOLOv8 model.
5. The detected readings will be saved in a JSON file.

## Data Processing
1. After capturing and processing the images, the `main.py` to convert the JSON file to a CSV file:

2. The CSV file can be opened and analyzed using any spreadsheet software, such as Microsoft Excel or Google Sheets.

## Results
The water meter reading system provides accurate and reliable readings, making it an ideal solution for automating the process of collecting and storing water meter data. The system can be further customized and optimized to suit specific requirements and use cases.

## License
This project is licensed under the [MIT License](LICENSE).