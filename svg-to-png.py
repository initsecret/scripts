import glob
import os
import re

# https://stackoverflow.com/a/1176023
pattern = re.compile(r'(?<!^)(?=[A-Z])')

for file in glob.glob("*.svg"):
    new = pattern.sub('-', file).lower()
    new = new.replace('.svg', '.png')
    run = f"rsvg-convert -h 512 {file} > {new}"
    os.system(run)
