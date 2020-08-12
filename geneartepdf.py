import os
from weasyprint import HTML

for f in os.listdir('path_to_HTML_directory'):
    pdf_name = f.replace('.html','')
    pdf_file_path = 'path_to_PDF_directory/{}.pdf'.format(pdf_name)
    html_file_path = 'path_to_HTML_directory'+f
    HTML(html_file_path).write_pdf(pdf_file_path)
