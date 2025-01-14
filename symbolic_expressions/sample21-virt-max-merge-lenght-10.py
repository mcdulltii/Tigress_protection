#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_5500 = ref_278 # MOV operation
ref_5542 = ref_5500 # MOV operation
ref_5550 = (ref_5542 >> (0x3 & 0x3F)) # SHR operation
ref_5557 = ref_5550 # MOV operation
ref_6002 = ref_278 # MOV operation
ref_6034 = ref_6002 # MOV operation
ref_6048 = ((ref_6034 << (0x3D & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_6085 = ref_5557 # MOV operation
ref_6097 = ref_6048 # MOV operation
ref_6099 = (ref_6097 | ref_6085) # OR operation
ref_6136 = ref_6099 # MOV operation
ref_6150 = ((ref_6136 - 0x3FEFFF7F) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_6158 = ref_6150 # MOV operation
ref_6192 = ref_6158 # MOV operation
ref_6194 = ((ref_6192 >> 56) & 0xFF) # Byte reference - MOV operation
ref_6195 = ((ref_6192 >> 48) & 0xFF) # Byte reference - MOV operation
ref_6196 = ((ref_6192 >> 40) & 0xFF) # Byte reference - MOV operation
ref_6197 = ((ref_6192 >> 32) & 0xFF) # Byte reference - MOV operation
ref_6198 = ((ref_6192 >> 24) & 0xFF) # Byte reference - MOV operation
ref_6199 = ((ref_6192 >> 16) & 0xFF) # Byte reference - MOV operation
ref_6200 = ((ref_6192 >> 8) & 0xFF) # Byte reference - MOV operation
ref_6201 = (ref_6192 & 0xFF) # Byte reference - MOV operation
ref_7047 = ref_278 # MOV operation
ref_7363 = ref_6192 # MOV operation
ref_7389 = ref_7047 # MOV operation
ref_7393 = ref_7363 # MOV operation
ref_7395 = (ref_7393 | ref_7389) # OR operation
ref_7432 = ref_7395 # MOV operation
ref_7446 = ((ref_7432 - 0x11E59B96) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_7454 = ref_7446 # MOV operation
ref_7488 = ref_7454 # MOV operation
ref_7490 = ((ref_7488 >> 56) & 0xFF) # Byte reference - MOV operation
ref_7491 = ((ref_7488 >> 48) & 0xFF) # Byte reference - MOV operation
ref_7492 = ((ref_7488 >> 40) & 0xFF) # Byte reference - MOV operation
ref_7493 = ((ref_7488 >> 32) & 0xFF) # Byte reference - MOV operation
ref_7494 = ((ref_7488 >> 24) & 0xFF) # Byte reference - MOV operation
ref_7495 = ((ref_7488 >> 16) & 0xFF) # Byte reference - MOV operation
ref_7496 = ((ref_7488 >> 8) & 0xFF) # Byte reference - MOV operation
ref_7497 = (ref_7488 & 0xFF) # Byte reference - MOV operation
ref_8325 = ref_278 # MOV operation
ref_8641 = ref_6192 # MOV operation
ref_8667 = ref_8325 # MOV operation
ref_8671 = ref_8641 # MOV operation
ref_8673 = (((sx(0x40, ref_8671) * sx(0x40, ref_8667)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_9061 = ref_7488 # MOV operation
ref_9079 = ref_9061 # MOV operation
ref_9093 = ((ref_9079 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_9124 = ref_8673 # MOV operation
ref_9136 = ref_9093 # MOV operation
ref_9138 = (((sx(0x40, ref_9136) * sx(0x40, ref_9124)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_9174 = ref_9138 # MOV operation
ref_10029 = ref_278 # MOV operation
ref_10061 = ref_10029 # MOV operation
ref_10075 = ((ref_10061 - 0x2000000007A4C37E) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_10083 = ref_10075 # MOV operation
ref_10117 = ref_10083 # MOV operation
ref_11213 = ((((ref_6194) << 8 | ref_6195) << 8 | ref_6196) << 8 | ref_6197) # MOV operation
ref_11271 = (ref_11213 & 0xFFFFFFFF) # MOV operation
ref_11933 = ((((ref_6198) << 8 | ref_6199) << 8 | ref_6200) << 8 | ref_6201) # MOV operation
ref_12601 = (ref_11933 & 0xFFFFFFFF) # MOV operation
ref_12603 = (((ref_12601 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_12604 = (((ref_12601 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_12605 = (((ref_12601 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_12606 = ((ref_12601 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_12669 = (ref_11271 & 0xFFFFFFFF) # MOV operation
ref_13337 = (ref_12669 & 0xFFFFFFFF) # MOV operation
ref_13339 = (((ref_13337 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_13340 = (((ref_13337 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_13341 = (((ref_13337 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_13342 = ((ref_13337 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_14073 = ((((((((ref_12603) << 8 | ref_12604) << 8 | ref_12605) << 8 | ref_12606) << 8 | ref_13339) << 8 | ref_13340) << 8 | ref_13341) << 8 | ref_13342) # MOV operation
ref_14547 = ref_9174 # MOV operation
ref_14927 = ref_9174 # MOV operation
ref_14943 = ref_14547 # MOV operation
ref_14955 = ref_14927 # MOV operation
ref_14957 = ((ref_14955 + ref_14943) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_15113 = ref_14957 # MOV operation
ref_15119 = (0x3F & ref_15113) # AND operation
ref_15156 = ref_15119 # MOV operation
ref_15170 = ((ref_15156 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_15207 = ref_14073 # MOV operation
ref_15219 = ref_15170 # MOV operation
ref_15221 = (ref_15219 | ref_15207) # OR operation
ref_15260 = ref_15221 # MOV operation
ref_16480 = ((((ref_7490) << 8 | ref_7491) << 8 | ref_7492) << 8 | ref_7493) # MOV operation
ref_16538 = (ref_16480 & 0xFFFFFFFF) # MOV operation
ref_17200 = ((((ref_7494) << 8 | ref_7495) << 8 | ref_7496) << 8 | ref_7497) # MOV operation
ref_17868 = (ref_17200 & 0xFFFFFFFF) # MOV operation
ref_17870 = (((ref_17868 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_17871 = (((ref_17868 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_17872 = (((ref_17868 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_17873 = ((ref_17868 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_17936 = (ref_16538 & 0xFFFFFFFF) # MOV operation
ref_18604 = (ref_17936 & 0xFFFFFFFF) # MOV operation
ref_18606 = (((ref_18604 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_18607 = (((ref_18604 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_18608 = (((ref_18604 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_18609 = ((ref_18604 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_19340 = ((((((((ref_17870) << 8 | ref_17871) << 8 | ref_17872) << 8 | ref_17873) << 8 | ref_18606) << 8 | ref_18607) << 8 | ref_18608) << 8 | ref_18609) # MOV operation
ref_19814 = ref_10117 # MOV operation
ref_20194 = ref_9174 # MOV operation
ref_20210 = ref_19814 # MOV operation
ref_20222 = ref_20194 # MOV operation
ref_20224 = ((ref_20222 + ref_20210) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_20380 = ref_20224 # MOV operation
ref_20386 = (0x3F & ref_20380) # AND operation
ref_20423 = ref_20386 # MOV operation
ref_20437 = ((ref_20423 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_20474 = ref_19340 # MOV operation
ref_20486 = ref_20437 # MOV operation
ref_20488 = (ref_20486 | ref_20474) # OR operation
ref_20527 = ref_20488 # MOV operation
ref_20529 = ((ref_20527 >> 56) & 0xFF) # Byte reference - MOV operation
ref_20530 = ((ref_20527 >> 48) & 0xFF) # Byte reference - MOV operation
ref_20531 = ((ref_20527 >> 40) & 0xFF) # Byte reference - MOV operation
ref_20532 = ((ref_20527 >> 32) & 0xFF) # Byte reference - MOV operation
ref_20533 = ((ref_20527 >> 24) & 0xFF) # Byte reference - MOV operation
ref_20534 = ((ref_20527 >> 16) & 0xFF) # Byte reference - MOV operation
ref_20535 = ((ref_20527 >> 8) & 0xFF) # Byte reference - MOV operation
ref_20536 = (ref_20527 & 0xFF) # Byte reference - MOV operation
ref_21891 = ref_20531 # MOVZX operation
ref_22025 = (ref_21891 & 0xFF) # MOVZX operation
ref_22509 = ref_20535 # MOVZX operation
ref_23129 = (ref_22509 & 0xFF) # MOVZX operation
ref_23131 = (ref_23129 & 0xFF) # Byte reference - MOV operation
ref_23285 = (ref_22025 & 0xFF) # MOVZX operation
ref_23819 = (ref_23285 & 0xFF) # MOVZX operation
ref_23821 = (ref_23819 & 0xFF) # Byte reference - MOV operation
ref_24557 = ref_9174 # MOV operation
ref_24917 = ref_10117 # MOV operation
ref_24933 = ref_24557 # MOV operation
ref_24945 = ref_24917 # MOV operation
ref_24947 = (ref_24945 & ref_24933) # AND operation
ref_25102 = ref_24947 # MOV operation
ref_25108 = (0xF & ref_25102) # AND operation
ref_25155 = ref_25108 # MOV operation
ref_25161 = (0x1 | ref_25155) # OR operation
ref_25546 = ref_15260 # MOV operation
ref_25926 = ((((((((ref_20529) << 8 | ref_20530) << 8 | ref_23131) << 8 | ref_20532) << 8 | ref_20533) << 8 | ref_20534) << 8 | ref_23821) << 8 | ref_20536) # MOV operation
ref_25942 = ref_25546 # MOV operation
ref_25954 = ref_25926 # MOV operation
ref_25956 = ((ref_25954 + ref_25942) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_25980 = ref_25956 # MOV operation
ref_25992 = ref_25161 # MOV operation
ref_25994 = ((ref_25980 << ((ref_25992 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_26379 = ref_15260 # MOV operation
ref_26759 = ((((((((ref_20529) << 8 | ref_20530) << 8 | ref_23131) << 8 | ref_20532) << 8 | ref_20533) << 8 | ref_20534) << 8 | ref_23821) << 8 | ref_20536) # MOV operation
ref_26775 = ref_26379 # MOV operation
ref_26787 = ref_26759 # MOV operation
ref_26789 = ((ref_26787 + ref_26775) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_27155 = ref_9174 # MOV operation
ref_27535 = ref_10117 # MOV operation
ref_27551 = ref_27155 # MOV operation
ref_27563 = ref_27535 # MOV operation
ref_27565 = (ref_27563 & ref_27551) # AND operation
ref_27720 = ref_27565 # MOV operation
ref_27726 = (0xF & ref_27720) # AND operation
ref_27773 = ref_27726 # MOV operation
ref_27779 = (0x1 | ref_27773) # OR operation
ref_27830 = ref_27779 # MOV operation
ref_27832 = ((0x40 - ref_27830) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_27840 = ref_27832 # MOV operation
ref_27872 = ref_26789 # MOV operation
ref_27884 = ref_27840 # MOV operation
ref_27886 = (ref_27872 >> ((ref_27884 & 0xFF) & 0x3F)) # SHR operation
ref_27923 = ref_25994 # MOV operation
ref_27935 = ref_27886 # MOV operation
ref_27937 = (ref_27935 | ref_27923) # OR operation
ref_27976 = ref_27937 # MOV operation
ref_28223 = ref_27976 # MOV operation
ref_28225 = ref_28223 # MOV operation

print(ref_28225 & 0xffffffffffffffff)
