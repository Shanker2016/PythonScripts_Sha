
# split multiple pages pdf into invidividual pages
# rename each individual pdf page
# convert each individual pdf page to tiff format
# collect tiff files into separate folder and zip it

import os
import PyPDF2
from pdf2image import convert_from_path
from PIL import Image
import shutil
import zipfile

def split_pdf(pdf_path, out_dir, filenames_path):

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(reader.pages)
        #print(num_pages)

        with open(filenames_path) as file:
            filenames = file.read().splitlines()

        if len(filenames) < num_pages // 2:
            raise ValueError("Not enough filenames")

        for i in range(num_pages):
            writer = PyPDF2.PdfWriter()
            writer.add_page(reader.pages[i])

            filename = filenames[i // 2]
            grid_no = filename[0:3]
            point_no = int(filename[4:6]) - 10 + 10000
            
            filename_mod = 'GS '+ grid_no + '(' + str(point_no) + ')' + 'A' if i % 2 == 0 else \
                     'GS '+ grid_no + '(' + str(point_no) + ')' + 'B'
            new_filename_with_suffix = f"{filename_mod}.pdf"
            

            output_path = os.path.join(out_dir, new_filename_with_suffix)
            
            with open(output_path, 'wb') as output_pdf:
                writer.write(output_pdf)

            print(f"Saved page{i+1} as {new_filename_with_suffix}")  

    


def pdf_to_tiff(pdf_folder):
    for filename in os.listdir(pdf_folder):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(pdf_folder, filename)
            tiff_path = os.path.join(pdf_folder, filename.replace('.pdf', '.tiff'))

            images = convert_from_path(pdf_path)

            image = images[0]

            image.save(tiff_path, format = 'TIFF')

            print(f"Converted {pdf_path} to {tiff_path}")

def zip_tiff_files(src_folder, dest_folder, zip_name):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    for filename in os.listdir(src_folder):
        if filename.lower().endswith('.tiff') or filename.lower().endswith('.tiff'):
            full_filename = os.path.join(src_folder, filename)
            if os.path.isfile(full_filename):
                shutil.copy(full_filename, dest_folder)

    shutil.make_archive(zip_name, 'zip', dest_folder)

    print(f"All TIFF files have been collected in '{dest_folder}' and zipped into '{zip_name}.zip'")


if __name__ == '__main__':
    pdf_path = 'Description_Card_36_Stations-Part1.pdf'
    out_dir = 'OUTDIR'
    filenames_path = 'point_name_pt1.txt'
    #src_folder = 'OUTDIR'
    dest_folder = 'DESC_TIFF'
    zip_filename = 'DESC_TIFF_ARCHIVE'

    pdf_path2 = 'Description_Card_36_Stations-Part2.pdf'
    out_dir2 = 'OUTDIR2'
    filenames_path2 = 'point_name_pt2.txt'
    #src_folder = 'OUTDIR'
    dest_folder2 = 'DESC_TIFF2'
    zip_filename2 = 'DESC_TIFF_ARCHIVE2'


    #split_pdf(pdf_path, out_dir, filenames_path)
    #pdf_to_tiff(out_dir)
    #zip_tiff_files(out_dir, dest_folder, zip_filename)

    split_pdf(pdf_path2, out_dir2, filenames_path2)
    pdf_to_tiff(out_dir2)
    zip_tiff_files(out_dir2, dest_folder2, zip_filename2)
