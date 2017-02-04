#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#Date:2017-01-23
#Autor:netb2c
#
import os,sys
from mutagen.mp3 import MP3

def get_bitrate(musicfile):
    f = MP3(musicfile)
    bitrate = f.info.bitrate / 1000
    return bitrate

def get_length(musicfile):
    f = MP3(musicfile)
    length = f.info.length
    return length

def get_all_file (full_path):
    try:
        all_file = os.listdir(full_path)
    except Exception, e:
        return '[]'
    file = []
    for L in all_file:
        path = full_path + os.sep  + L
        f = open(path,"r")
        filestr = f.read()
        f.close()
        head3Str = filestr[:3]
        if head3Str == "ID3" :
            file.append(path)
    return file

musicfile =  get_all_file('/home/netb2c/Music')
for i in range(0,len(musicfile)):
    print musicfile[i]+'  Bitrate is :',get_bitrate(musicfile[i]),'kbps', ' File length is :',get_length(musicfile[i]),'s'
