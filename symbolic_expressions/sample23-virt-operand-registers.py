#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_6735 = ref_278 # MOV operation
ref_6955 = ref_6735 # MOV operation
ref_6973 = ((ref_6955 + 0x3F22161B) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_7126 = ref_6973 # MOV operation
ref_9419 = ref_7126 # MOV operation
ref_9673 = ref_9419 # MOV operation
ref_9675 = (((sx(0x40, 0x378AED0A) * sx(0x40, ref_9673)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_9931 = ref_9675 # MOV operation
ref_9933 = (((sx(0x40, 0xDF2B78B) * sx(0x40, ref_9931)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_10060 = ref_9933 # MOV operation
ref_10080 = (ref_10060 >> (0x1 & 0x3F)) # SHR operation
ref_10237 = ref_10080 # MOV operation
ref_10255 = (ref_10237 & 0xF) # AND operation
ref_10525 = ref_10255 # MOV operation
ref_10543 = (ref_10525 | 0x1) # OR operation
ref_11791 = ref_278 # MOV operation
ref_11943 = ref_11791 # MOV operation
ref_11963 = ((ref_11943 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_13211 = ref_278 # MOV operation
ref_13336 = ref_13211 # MOV operation
ref_13356 = (ref_13336 >> (0x39 & 0x3F)) # SHR operation
ref_13513 = ref_11963 # MOV operation
ref_13529 = ref_13356 # MOV operation
ref_13531 = (ref_13513 | ref_13529) # OR operation
ref_13688 = ref_13531 # MOV operation
ref_13704 = ref_10543 # MOV operation
ref_13706 = (ref_13704 & 0xFFFFFFFF) # MOV operation
ref_13708 = ((ref_13688 << ((ref_13706 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_15159 = ref_7126 # MOV operation
ref_15413 = ref_15159 # MOV operation
ref_15415 = (((sx(0x40, 0x378AED0A) * sx(0x40, ref_15413)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_15671 = ref_15415 # MOV operation
ref_15673 = (((sx(0x40, 0xDF2B78B) * sx(0x40, ref_15671)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_15800 = ref_15673 # MOV operation
ref_15820 = (ref_15800 >> (0x1 & 0x3F)) # SHR operation
ref_15977 = ref_15820 # MOV operation
ref_15995 = (ref_15977 & 0xF) # AND operation
ref_16265 = ref_15995 # MOV operation
ref_16283 = (ref_16265 | 0x1) # OR operation
ref_16447 = ref_16283 # MOV operation
ref_16449 = ((0x40 - ref_16447) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_17698 = ref_278 # MOV operation
ref_17850 = ref_17698 # MOV operation
ref_17870 = ((ref_17850 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_19118 = ref_278 # MOV operation
ref_19243 = ref_19118 # MOV operation
ref_19263 = (ref_19243 >> (0x39 & 0x3F)) # SHR operation
ref_19420 = ref_17870 # MOV operation
ref_19436 = ref_19263 # MOV operation
ref_19438 = (ref_19420 | ref_19436) # OR operation
ref_19568 = ref_19438 # MOV operation
ref_19584 = ref_16449 # MOV operation
ref_19586 = (ref_19584 & 0xFFFFFFFF) # MOV operation
ref_19588 = (ref_19568 >> ((ref_19586 & 0xFF) & 0x3F)) # SHR operation
ref_19745 = ref_13708 # MOV operation
ref_19761 = ref_19588 # MOV operation
ref_19763 = (ref_19745 | ref_19761) # OR operation
ref_19915 = ref_19763 # MOV operation
ref_22005 = ref_278 # MOV operation
ref_23112 = ref_19915 # MOV operation
ref_23332 = ref_23112 # MOV operation
ref_23350 = ((ref_23332 + 0xAD6EED) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_23463 = ref_22005 # MOV operation
ref_23479 = ref_23350 # MOV operation
ref_23481 = ((ref_23463 + ref_23479) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_23634 = ref_23481 # MOV operation
ref_25724 = ref_278 # MOV operation
ref_26831 = ref_7126 # MOV operation
ref_26983 = ref_25724 # MOV operation
ref_26999 = ref_26831 # MOV operation
ref_27001 = (ref_26983 | ref_26999) # OR operation
ref_28113 = ref_19915 # MOV operation
ref_28333 = ref_28113 # MOV operation
ref_28351 = ((ref_28333 + 0x2B6B05ED) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_29464 = ref_23634 # MOV operation
ref_29616 = ref_29464 # MOV operation
ref_29632 = ref_28351 # MOV operation
ref_29634 = (ref_29616 & ref_29632) # AND operation
ref_29746 = ref_27001 # MOV operation
ref_29762 = ref_29634 # MOV operation
ref_29764 = ((ref_29746 + ref_29762) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_29917 = ref_29764 # MOV operation
ref_31984 = ref_29917 # MOV operation
ref_33317 = ref_23634 # MOV operation
ref_33469 = ref_33317 # MOV operation
ref_33487 = (ref_33469 & 0x3F) # AND operation
ref_33644 = ref_33487 # MOV operation
ref_33664 = ((ref_33644 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_33821 = ref_31984 # MOV operation
ref_33837 = ref_33664 # MOV operation
ref_33839 = (ref_33821 | ref_33837) # OR operation
ref_33991 = ref_33839 # MOV operation
ref_36090 = ref_23634 # MOV operation
ref_37197 = ref_33991 # MOV operation
ref_37304 = ref_36090 # MOV operation
ref_37320 = ref_37197 # MOV operation
ref_37322 = ((ref_37304 + ref_37320) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_38661 = ref_19915 # MOV operation
ref_38786 = ref_38661 # MOV operation
ref_38806 = (ref_38786 >> (0x4 & 0x3F)) # SHR operation
ref_38963 = ref_38806 # MOV operation
ref_38981 = (ref_38963 & 0xF) # AND operation
ref_39251 = ref_38981 # MOV operation
ref_39269 = (ref_39251 | 0x1) # OR operation
ref_40381 = ref_7126 # MOV operation
ref_40533 = ref_40381 # MOV operation
ref_40549 = ref_39269 # MOV operation
ref_40551 = (ref_40549 & 0xFFFFFFFF) # MOV operation
ref_40553 = ((ref_40533 << ((ref_40551 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_42004 = ref_19915 # MOV operation
ref_42129 = ref_42004 # MOV operation
ref_42149 = (ref_42129 >> (0x4 & 0x3F)) # SHR operation
ref_42306 = ref_42149 # MOV operation
ref_42324 = (ref_42306 & 0xF) # AND operation
ref_42594 = ref_42324 # MOV operation
ref_42612 = (ref_42594 | 0x1) # OR operation
ref_42776 = ref_42612 # MOV operation
ref_42778 = ((0x40 - ref_42776) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_43891 = ref_7126 # MOV operation
ref_44016 = ref_43891 # MOV operation
ref_44032 = ref_42778 # MOV operation
ref_44034 = (ref_44032 & 0xFFFFFFFF) # MOV operation
ref_44036 = (ref_44016 >> ((ref_44034 & 0xFF) & 0x3F)) # SHR operation
ref_44193 = ref_40553 # MOV operation
ref_44209 = ref_44036 # MOV operation
ref_44211 = (ref_44193 | ref_44209) # OR operation
ref_44341 = ref_44211 # MOV operation
ref_44357 = ref_37322 # MOV operation
ref_44359 = (((sx(0x40, ref_44341) * sx(0x40, ref_44357)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_44508 = ref_44359 # MOV operation
ref_44713 = ref_44508 # MOV operation
ref_44715 = ref_44713 # MOV operation

print(ref_44715 & 0xffffffffffffffff)
