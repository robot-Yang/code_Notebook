import sys
sys.path.append('/usr/local/lib/python3.7/site-packages')

from pymatting import cutout

cutout(
    # input image path
    "lemur.png",
    # input trimap path
    "lemur_trimap.png",
    # output cutout path
    "lemur_cutout.png")