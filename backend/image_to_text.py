# Import required packages
import cv2
import pytesseract
import re

# Mention the installed location of Tesseract-OCR in your system
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

# Read image from which text needs to be extracted
img = cv2.imread("./uploads/image.jpg")

# Convert the image to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    

# Get the dimensions of the image
h, w = gray.shape

# Define the coordinates for the ROI
x, y, w, h = 20, h//4 + 20, w//2, h//2

# Crop the ROI from the grayscale image
roi = gray[y:y+h, x:x+w]

# Apply OCR on the ROI with custom configuration
custom_config = r'--oem 3 --psm 11'
text = pytesseract.image_to_string(roi, config=custom_config)
"""print(text)"""

# Look for first name and last name based on titles
first_name_match = re.search(r'prsrnane ra\s+(\w+)', text, re.IGNORECASE)
last_name_match = re.search(r'UASTNAME\s+(\w+)', text, re.IGNORECASE)
dob_match = re.search(r'(\d{1,2}/\d{1,2}/\d{4})', text, re.IGNORECASE)

# Open the file in writing mode
with open("recognized.txt", "w") as file:
    if first_name_match:
        first_name = first_name_match.group(1)
        file.write(f'First Name: {first_name}\n')
    if last_name_match:
        last_name = last_name_match.group(1)
        file.write(f'Last Name: {last_name}\n')
    if dob_match:
        dob = dob_match.group(1)
        file.write(f'Date of Birth: {dob}\n')
        
    # Appending the text into file
    """file.write(text)"""
    file.write("\n")