import PyPDF2
import pathlib

ROOT_FOLDER = pathlib.Path(__file__).parent
GET_PDF = ROOT_FOLDER / "origin_pdf"
NEW_PDFS = ROOT_FOLDER / "new_pdfs"


NEW_PDFS.mkdir(exist_ok=True)

BCRELATORIO = GET_PDF / "R20250627.pdf"

# PDF pages length 
reader = PyPDF2.PdfReader(BCRELATORIO)
print(len(reader.pages))

# Accessing pages
for page in reader.pages:
    print()
    print(page)

print()

# Extracting text from  page
# Note: The text extraction may not be perfect depending on the PDF structure
page0 = reader.pages[0].extract_text()
print(page0)

print()

# Extracting images from PDF 
page0 = reader.pages[0]
imagem0 = page.images[0]

print(imagem0)

with open(NEW_PDFS / imagem0.name, "wb") as fp:
    fp.write(imagem0.data)