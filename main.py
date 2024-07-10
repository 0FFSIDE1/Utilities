from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image

def convert_image_to_pdf(image_path, pdf_path):
    # Open the image file
    img = Image.open(image_path)
    
    # Create a new PDF document
    c = canvas.Canvas(pdf_path, pagesize=img.size)
    
    # Draw the image onto the PDF
    c.drawImage(image_path, 0, 0, width=img.width, height=img.height)
    
    # Save the PDF file
    c.save()

# Example usage:
image_path = 'image.jpg'  # Replace with your image path
pdf_path = 'output.pdf'  # Replace with desired output PDF path

convert_image_to_pdf(image_path, pdf_path)
