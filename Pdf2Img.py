import fitz
import os

pdfs_path = 'path_to_pdfs'
imgs_path = 'path_to_imgs'

for f in os.listdir(pdfs_path):
  doc = fitz.open(pdfs_path+f)
  page = doc.loadPage(0)  
  pix = page.getPixmap()
  output = imgs_path+"{}.png".format(f)
  pix.writePNG(output)
