import os
import os
import PyPDF2

def webscrape(pdf_directory):
    """
    This function performs web scraping on PDF files in the given directory.

    Parameters:
        pdf_directory (str): The directory path where the PDF files are located.

    Returns:
        None
    """
    # Check if the directory exists
    if not os.path.isdir(pdf_directory):
        print("Invalid directory path.")
        return

    # Iterate over the PDF files in the directory
    for filename in os.listdir(pdf_directory):
        if filename.endswith(".pdf"):
            # Perform web scraping on the PDF file
            pdf_path = os.path.join(pdf_directory, filename)
            with open(pdf_path, "rb") as file:

                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text()

                # Do whatever you want with the extracted text
                # For example, you can print it or save it to a file
                print(f"Scraping {filename}...")
                print(text)


webscrape("./test_data")