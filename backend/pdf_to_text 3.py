import pdf2image
import pytesseract
import re

# converts pdf pages into images
def uploaded_pdf_to_text(uploaded_pdf_file):
    def convert_pdf_to_image(pdf_file):
        return pdf2image.convert_from_path(pdf_file)
        
    # converts image to text
    def convert_image_to_text(image_to_be_converted):
        text_to_be_parsed = pytesseract.image_to_string(image_to_be_converted)
        return text_to_be_parsed

    # extracts information from text for parsing
    def extract_information(text):
        annual_income = None
        monthly_income = None
        first_name = None
        last_name = None
        
        # Uses regular expression to grab income and names
        income_pattern = r'(Annual|Monthly) Income: \$(\d+,\d+)'
        name_pattern = r"Employee's first name and initial: ([A-Za-z]+)\s+Last Name: ([A-Za-z]+)"

        income_match = re.search(income_pattern, text)
        if income_match:
            income_type, income_value = income_match.groups()
            if income_type == 'Annual':
                annual_income = income_value
            elif income_type == 'Monthly':
                monthly_income = income_value

        name_match = re.search(name_pattern, text)
        if name_match:
            first_name, last_name = name_match.groups()

        return {
            'Annual Income': annual_income,
            'Monthly Income': monthly_income,
            'First Name': first_name,
            'Last Name': last_name
        }
    # Utilizes convert_pdf_to_image() and convert_image_to_text() to convert pdf to text
    def convert_pdf_to_text(attached_file):
        images = convert_pdf_to_image(attached_file)
        extracted_text = ""
        for page, image in enumerate(images):
            page_text = convert_image_to_text(image)
            extracted_text += page_text

    
        final_cache = extract_information(extracted_text)

        # This should be the sections for the inputs
        with open("parsed_pdf.txt", "a") as f:
            f.write(f"Page {page+1}:\n")
            for key, value in final_cache.items():
                f.write(f"{key}: {value}\n")

    convert_pdf_to_text(uploaded_pdf_file)
