#!/usr/bin/env python3
import os
import zipfile
import shutil

for file in os.listdir('.'):
    print(file,"==>",zipfile.is_zipfile(file))

shutil.unregister_archive_format("")
