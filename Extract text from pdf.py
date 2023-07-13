import tkinter as tk
import PyPDF2
from tkinter import filedialog
from tkinter import scrolledtext

root = tk.Tk()
root.geometry('800x500')
root.title("PDF Extract Text")
fileName = "No File"
def openFile():
    filename = filedialog.askopenfilename(title="Open pdf file", initialdir=r'G:\Node.js\Office', filetypes=[('PDF files','*.pdf')])
    print(filename)
    if (filename):
        label = tk.Label(root, text=filename, font=("san", 15))
        label.pack(padx=10, pady=10)
    else:
        label = tk.Label(root, text="No File", font=("san", 15))
        label.pack(padx=10, pady=10)
    reader = PyPDF2.PdfReader(filename)

    for i in range(len(reader.pages)):
        current_text = reader.pages[i].extract_text()
        print(current_text)
        body.insert(tk.END, current_text)

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
body = scrolledtext.ScrolledText(root, wrap=tk.WORD, yscrollcommand=scrollbar.set)
body.pack(pady=10)
scrollbar.config(command=body.yview)
button = tk.Button(root, text="Open a pdf", font=("san", 10), command=openFile)
button.pack()

root.mainloop()
