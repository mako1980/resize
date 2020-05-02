import os
import sys
import glob
from PIL import Image

# JPGファイルを縮小
#   →*_aft.JPG
# 引数'd'で元ファイル削除

delete_f = '0'
if len(sys.argv) == 2:
    args = sys.argv
    if args[1] == 'd':
        delete_f = '1'

types = ['*.JPG', '*.jpg', '*.JPEG', '*jpeg']
files = []
for t in types:
    files.extend(glob.glob(t))
for f in files:
    im = Image.open(f)
    im_resize = im.resize((int(im.width / 2), int(im.height / 2)))
    title, ext = os.path.splitext(f)
    a = title + '_aft' + ext
    im_resize.save(a)
    print(f + ' -> ' + a)
    if delete_f == '1':
        os.remove(f)

if delete_f == '1':
    print('--\nDelete original file.\ndone.')
else:
    print('--\ndone.')
