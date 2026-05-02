from PyPDF2 import PdfMerger


def merge_pdfs(output_file, pdf_files):

    merger = PdfMerger()

    for pdf in pdf_files:
        merger.append(pdf)
    
    merger.write(output_file)

    merger.close()

    print(f"Merged PDF saved as {output_file}")

    