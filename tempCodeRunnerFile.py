if output_filename.split('.')[1] == 'pdf':
    output_path = f"{output_directory}.pdf/{output_filename}"
else:
    output_path = f"{output_directory}/{output_filename}"