import os
import glob
from PIL import Image

# JPGファイルを縮小
#   →*_aft.JPG

files = glob.glob('*.[Jj][Pp][Gg]')
for f in files:
    print(f)
    im = Image.open(f)
    im_resize = im.resize((int(im.width / 2), int(im.height / 2)))
    title, ext = os.path.splitext(f)
    im_resize.save(title + '_aft' + ext)
print("done")
