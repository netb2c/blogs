#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#Date:2017-01-19
#Autor:netb2c
#Only run on Windows.

import mp3play

filename = r'/home/netb2c/Music/17岁.mp3'

clip = mp3play.load(filename)

clip.play()

import time
time.sleep(min(30, clip.seconds()))
clip.stop()
