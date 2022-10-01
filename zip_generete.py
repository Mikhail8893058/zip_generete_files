import zipfile, os
import getting_text as gt
from seminar_05.DZ.RLE.getting_text import get_txt

file_zip = get_txt.ZipFile('r')

def compress_zip():
    for folder, subfolders, files in os.walk('/Users/mac/python/seminar_05/DZ/RLE'):
        for file in files:
            if file.endswith('.txt'):
                file_zip.write(os.path.join(folder, file), 
                os.path.realpath(os.path.join(folder, file), '/Users/mac/python/seminar_05/DZ/RLE'),
                compress_type = zipfile.ZIP_DEFLATED)

file_zip.close()

