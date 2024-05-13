from pypdf import PdfReader

reader = PdfReader("957")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"
print(text)