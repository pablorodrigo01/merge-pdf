import PyPDF2
import os

merger = PyPDF2.PdfMerger()

list_files = os.listdir('files')
list_files.sort()

for file in list_files:
    if ".pdf" in file:
        merger.append(f"files/{file}")

merger.write("Pdf Merge File.pdf")
