import sys
sys.path.append('/usr/local/lib/python3.7/site-packages')

from pymatting import cutout

cutout(
    # input image path
    "1.png",
    # input trimap path
    "2.png",
    # output cutout path
    "3_cutout.png")