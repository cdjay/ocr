import sys
from ocrapi import readimg

imgpath=str(sys.argv[1])

img=readimg(imgpath)

print(img['words_result'])