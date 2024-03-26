import json
import os
import numpy as np
import torch
from datetime import datetime
from ultralytics import YOLO
import pathlib
import time

# Load a model on CPU
device = torch.device('cpu')
# model = YOLO('C:\\Users\\cybor\\Documents\\Projects\\meter_reading\\meter_reading\\model\\best.pt').to(device)  # pretrained YOLOv8n model
model_path = pathlib.Path('C:\\Users\\cybor\\Documents\\Pracs\\meter_reading\\model\\best.pt')
model = YOLO(model_path).to(device)


# Run inference on an image on CPU
# results = model('C:\\Users\\cybor\\Documents\\Projects\\meter_reading\\meter_reading\\images\\test2.jpg')  # replace with the path to your image
image_path = pathlib.Path('C:\\Users\\cybor\\Documents\\Projects\\meter_reading\\meter_reading\\images\\test14.jpg')
results = model(image_path)


# Process results
boxes = results[0].boxes  # Boxes object for bounding box outputs

# Convert xyxy tensor to numpy array
boxes_np = boxes.xyxy.cpu().numpy()

# Sort based on x-coordinate
sorted_indices = np.argsort(boxes_np[:, 0])

# Concatenate digits into a string
digits = ''
for index in sorted_indices:
    box = boxes[index]
    digit = model.names[int(box.cls)]
    digits += digit

# Get the current date and time
now = datetime.now()
date = now.strftime('%Y-%m-%d')
time = now.strftime('%H:%M:%S')

# Append the result to the JSON file
filename = 'result.json'
if os.path.exists(filename):
    # Load the existing data
    with open(filename, 'r') as f:
        data = json.load(f)
    # If the 'results' key does not exist, create it as an empty list
    if 'results' not in data:
        data['results'] = []
    # Add the new result to the list
    data['results'].append({"date": date, "time": time, "digits": digits})
else:
    # Create a new dictionary with a list of results
    data = {"results": [{"date": date, "time": time, "digits": digits}]}

# Save the updated data to the file
with open(filename, 'w') as f:
    json.dump(data, f)

# Display the image and save it to disk
results[0].show()  # display to screen
results[0].save(filename='result.jpg')  # save to disk

# Convert the JSON file to a CSV file
import csv

# Load the JSON file
with open(filename, 'r') as f:
    data = json.load(f)

# Extract the list of results
results = data['results']

# Define the header for the CSV file
header = ['date', 'time', 'digits']

# Write the results to a CSV file
csv_filename = 'result.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    for result in results:
        writer.writerow([result['date'], result['time'], result['digits']])

print(f"CSV file saved as {csv_filename}")


