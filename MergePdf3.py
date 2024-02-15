from PyPDF2 import PdfMerger
import tkinter as tk
from tkinter.filedialog import askopenfilename, askdirectory

root = tk.Tk()
root.withdraw()

arr = []

while True:
    file = askopenfilename(filetypes=[("PDF files", "*.pdf")])
    
    # If the user cancels or closes the file dialog, exit the loop
    if not file:
        break
    
    arr.append(file)

# Ask user for the directory to save the merged PDF
output_directory = askdirectory(title="Select Directory to Save Merged PDF")

if not output_directory:
    print("No directory selected. Exiting.")
    exit()

# Ask user for the filename of the merged PDF
output_filename = input("Enter the name of the merged PDF file (including '.pdf'): ")
if output_filename.split('.')[-1] != 'pdf':
    output_path = f"{output_directory}/{output_filename}.pdf"
else:
    output_path = f"{output_directory}/{output_filename}"

merger = PdfMerger()
for pdf in arr:
    merger.append(pdf)

merger.write(output_path)
merger.close()

print(f"Merged PDF saved to: {output_path}")
