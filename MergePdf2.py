from PyPDF2 import PdfMerger
import easygui

p = int(input("Enter the number of PDF files: "))
arr = []

for _ in range(p):
    file = easygui.fileopenbox(filetypes=["*.pdf"])
    arr.append(file)

output_directory = easygui.diropenbox(title="Select Directory to Save Merged PDF")

if not output_directory:
    print("No directory selected. Exiting.")
    exit()

output_filename = easygui.enterbox(msg="Enter the name of the merged PDF file (including '.pdf'): ", title="Merged PDF Filename")
# Check if the specified filename has a '.pdf' extension
if output_filename.split('.')[-1].lower() != 'pdf':
    output_path = f"{output_directory}/{output_filename}.pdf"
else:
    output_path = f"{output_directory}/{output_filename}"

merger = PdfMerger()
for pdf in arr:
    merger.append(pdf)

merger.write(output_path)
merger.close()

print(f"Merged PDF saved to: {output_path}")
