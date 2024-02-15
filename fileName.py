# Import the tkinter module
import tkinter as tk
# Import the file dialog functions from tkinter.filedialog
from tkinter.filedialog import askopenfilename, askopenfile

# Create a root window
root = tk.Tk()
# Hide the root window
root.withdraw()
# Show an "Open" dialog and get the path of the selected file
filename = askopenfilename()
# Alternatively, you can get a file object of the selected file
#file = askopenfile()
# Print the filename or file object
print(filename.split('/'))
print(len(filename.split('/')))
a = filename.split('/')
l = len(filename.split('/'))
endPoint = a[l -1].split('.')
if endPoint != 'pdf':
    filename = askopenfilename()
    a = filename.split('/')
    l = len(filename.split('/'))
    endPoint = a[l -1].split('.')
print(a[l-1].split('.'))

#print(file)
