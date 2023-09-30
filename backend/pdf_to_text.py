import fitz  # PyMuPDF
import re

"""
THE RECT_LIST VARIABLE IS USED WITH RECT_NAME/RECT_ADDRESS/RECT_WAGES TO VISUALIZE WHERE THE LIBRARY WILL EXTRACT TEXT FROM, RESPECTIVELY.

def visualize_rectangles(pdf_path, rect_list):
    doc = fitz.open(pdf_path)
    for page_number, page in enumerate(doc):
        for rect in rect_list:
            page.draw_rect(rect, color=(1, 0, 0), fill=(0, 1, 0), width=0.3)  # Red rectangle, green fill
        page.get_pixmap().save(f'page_{page_number + 1}.png')

# Define a list of rectangular regions
rect_list = [fitz.Rect(346, 70, 450, 80)]
"""

# Extracts the text given in the rectangular region
def extract_text_pymupdf(pdf_path, rect):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        # Get the text in the specified rectangle for each page
        page_text = page.get_text("text", clip=rect)
        text += page_text
    return text

# Define the rectangular regions for the first and last name, the address, and the wages
rect_names = fitz.Rect(50, 190, 300, 200)
rect_address = fitz.Rect(45, 210, 170, 245)
rect_wages = fitz.Rect(346, 70, 450, 80)

# path for the pdf file
pdf_path = "./backend/w2.pdf"

# Extracts the names, address, and wages as text
names_text = extract_text_pymupdf(pdf_path, rect_names)
address_text = extract_text_pymupdf(pdf_path, rect_address)
wages_text = extract_text_pymupdf(pdf_path, rect_wages)

# Splits the newlines and turns the names, address, and wages into lists
names_lines = names_text.split('\n')
address_lines = address_text.split('\n')
wages_lines = wages_text.split('\n')

# Remove empty strings from the lists
names_lines = [line for line in names_lines if line]
address_lines = [line for line in address_lines if line]
wages_lines = [line for line in wages_lines if line]

if names_lines:
    first_name_initial = names_lines[0].split()
    # Extend names_lines with the split values, and remove the original string
    names_lines = first_name_initial + names_lines[1:]

print(names_lines)
print(address_lines)
print(wages_lines)

# Join the address lines into a single string
address_string = ' '.join(address_lines)

# Since wages and names are on separate lines, you can just get the first item from the list
first_name = names_lines[0] if names_lines else ''
last_name = names_lines[2] if len(names_lines) > 1 else ''
wages_string = wages_lines[0] if wages_lines else ''

# Combine titles and items based on index
structured_data = {
    'First Name': first_name,
    'Last Name': last_name,
    'Address': address_string,
    'Wages': f"${wages_string}"
}

# Output structured data to a text file
with open("./backend/result.txt", "w") as file:
    for field, value in structured_data.items():
        file.write(f"{field}: {value}\n\n")

"""
RELATE TO LINE 5
THIS INITIALIZES THE FUNCTION IN LINE 7

visualize_rectangles(pdf_path, rect_list)
"""