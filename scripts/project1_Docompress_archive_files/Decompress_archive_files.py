#!/usr/bin/env python3
import os
import  patoolib

patool_Supported_archive_formats = ['.7z','.ace','.adf','.alz','.ape','.a','.arc','.arj','.bz2','.cab',
				    '.Z','.cpio','.deb', '.dms', '.flac','.gz', '.iso','.lrz','.lha', '.lzh',
				    '.lz', '.lzma','.lzo','.rpm','.rar','.rz','.shn','.tar','.xz','.zip', '.jar','.zoo' ,'.zpaq']

for file in os.listdir('.'):
    if '.' in file:                    #check if the file is an archive or dirictory
    	for archive_format in patool_Supported_archive_formats:
    		if archive_format in file:
	            print(file)
	            index = file.index('.')
	            file_name = file[:index]
	            file_dir = os.getcwd()+'/'+file_name
	            print("======>",file_name)
	            try:               #create the folder and extract the files
	                    if file_name not in os.listdir('.'):
	                            os.mkdir(file_name)
	                    print("*****>",file_name)
	                    try:
	                            patoolib.extract_archive(file,outdir=file_dir)
	                    except:
	                            print("Unsupported archive format")
	                            pass
	            except:             #the folder exist, extract the files
	                    print("="*40,'The folder exists',"="*40)

	                    print("*****>",file_name)
	                    patoolib.extract_archive(file,outdir=file_dir)
	            else:               #the folder and the files exist,exit
	                    print("="*40,'The Unpack files exist'"="*40,)
	            print(file," Umpacked Succcessfully")


