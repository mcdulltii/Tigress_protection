#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_342 = SymVar_0
ref_353 = ref_342 # MOV operation
ref_365 = ref_353 # MOV operation
ref_367 = ref_365 # MOV operation
ref_5369 = ref_367 # MOV operation
ref_5381 = ref_5369 # MOV operation
ref_5427 = ref_5369 # MOV operation
ref_5471 = ref_5369 # MOV operation
ref_5558 = (((rol(0xE, (rol(0xE, ((((((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) + ref_5381) & 0xFFFFFFFFFFFFFFFF) + 0x1F3D5B79) & 0xFFFFFFFFFFFFFFFF)) ^ ref_5427)) ^ 0x1F3D5B79) + ref_5471) & 0xFFFFFFFFFFFFFFFF) # MOV operation
ref_5898 = ref_5558 # MOV operation
ref_5997 = ref_5898 # MOV operation
ref_6332 = ref_5997 # MOV operation
ref_6428 = ref_6332 # MOV operation
ref_6466 = ref_6428 # MOV operation
ref_6478 = ref_6466 # MOV operation
ref_6480 = ref_6478 # MOV operation

print(ref_6480 & 0xffffffffffffffff)
