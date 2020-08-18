# HTMLtoPDF
**Aim :** To generate pdfs from HTML templates.

**Problem :**  There were many online solutions specifying ***pdfkit*** which uses * *wkhtmmltopdf* * library.But It requires global installation and manual path configuration.I found it difficult for a beginner to setup and use this.

**Solution :** Finally after scrolling through 10s of websites and posts on stackoverflow,I found this ***WeasyPrint*** package.It was easy to install and run.


WeasyPrint is a smart solution helping web developers to create PDF documents. It turns simple HTML pages into gorgeous statistical reports, invoices, tickets…

From a technical point of view, WeasyPrint is a visual rendering engine for HTML and CSS that can export to PDF and PNG. It aims to support web standards for printing. WeasyPrint is free software made available under a BSD license.

It is based on various libraries but not on a full rendering engine like WebKit or Gecko. The CSS layout engine is written in Python, designed for pagination, and meant to be easy to hack on.

Free software: BSD licensed
Python 3.5+
Website: https://weasyprint.org/
Documentation: https://weasyprint.readthedocs.io/
Source code and issue tracker: https://github.com/Kozea/WeasyPrint
Tests: https://travis-ci.org/Kozea/WeasyPrint
Support: https://www.patreon.com/kozea

# PDFtoPNG

**Aim :** To convert PDF files to Images

**Problem :**  There were many online solutions specifying ***pdf2image*** .But pdf2image is only a wrapper around poppler, to use the module you need to have poppler-utils installed on your machine and in your path.

**Solution :** Finally,I found this ***PyMuPDF*** package.It was easy to install and run.

For all document types you can render pages in raster (PNG) or vector (SVG) formats, extract text and access meta information, links, annotations and bookmarks, as well as decrypt the document. For PDF files, these objects can also be created, modified or deleted. Plus you can rotate, re-arrange, duplicate, create, or delete pages and join or split documents.

Specifically for PDF files, PyMuPDF provides update access to low-level structure information, supports handling of embedded files and modification of page contents (like inserting images, fonts, text, annotations and drawings).

Python 3.5+
Documentation: https://pymupdf.readthedocs.io/en/latest/
