#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# Title           : Shadow_Hash.py
# Description     : Generating the hash of password stored in /etc/shadow
# Version         : 1.0
# Python_version  : 2.7

import crypt

print crypt.crypt('doit0002', '$6$kURThR6P')
