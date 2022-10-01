import PyPDF2
import re

phone_number_regexp = "\\d{3}.\\d{3}.\\d{4}"
text_in_pdf_file = ''

with open("Find_the_Phone_Number.pdf", 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    for page in pdf_reader.pages:
        text_in_pdf_file += page.extractText()

match = re.search(phone_number_regexp, text_in_pdf_file)
print(match.group())
