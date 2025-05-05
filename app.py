import PyPDF2

with open("first.pdf", "rb") as file:

    reader = PyPDF2.PdfReader(file)
    print(len(reader.pages))
    page = reader.pages[0]
    page.rotate(90)
    writer = PyPDF2.PdfWriter()
    writer.add_page(page)
    with open("rotated.pdf", "wb") as output:
        writer.write(output)
