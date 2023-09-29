import pytesseract
import pdf2image
import PyPDF2

def uploaded_pdf_to_text(uploaded_pdf_file):
  def convert_pdf_to_image(pdf_file):
      # a basic function that converts pdf to image
      return pdf2image.convert_from_path(pdf_file)
  
  def convert_image_to_text(image_to_be_converted):
      # convert image to text
      text_to_be_parsed = pytesseract.image_to_string(image_to_be_converted)
      return text_to_be_parsed
  
  def convert_pdf_to_text(attached_file):
      # converts uploaded pdf to text
      images = convert_pdf_to_image(uploaded_pdf_file)
      resulting_text = ''
      for page,image in images:
          resulting_text += convert_image_to_text(images)
      return resulting_text
    
  conver_pdf_to_text(uploaded_pdf_file)
# Optimized uploaded_pdf_to_text
def to_text(attached_pdf):
  final_text = PyPDF2.PdfReader(attached_file)
  return final_text.extrct_text()
  


