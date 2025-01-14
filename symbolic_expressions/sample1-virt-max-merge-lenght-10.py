#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_264 = SymVar_0
ref_279 = ref_264 # MOV operation
ref_5419 = ref_279 # MOV operation
ref_5461 = ref_5419 # MOV operation
ref_5469 = ((ref_5461 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_5476 = ref_5469 # MOV operation
ref_5831 = ref_279 # MOV operation
ref_5873 = ref_5831 # MOV operation
ref_5881 = (ref_5873 >> (0x7 & 0x3F)) # SHR operation
ref_5888 = ref_5881 # MOV operation
ref_5920 = ref_5888 # MOV operation
ref_5932 = ref_5476 # MOV operation
ref_5934 = (ref_5932 | ref_5920) # OR operation
ref_5973 = ref_5934 # MOV operation
ref_6691 = ref_5973 # MOV operation
ref_6753 = ref_6691 # MOV operation
ref_6755 = ((ref_6753 + 0x2D4AF89B) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_6881 = ref_6755 # MOV operation
ref_6883 = (ref_6881 & 0x1D5ABF66) # AND operation
ref_7243 = ref_279 # MOV operation
ref_7285 = ref_7243 # MOV operation
ref_7293 = ((ref_7285 << (0x35 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_7300 = ref_7293 # MOV operation
ref_7655 = ref_279 # MOV operation
ref_7697 = ref_7655 # MOV operation
ref_7705 = (ref_7697 >> (0xB & 0x3F)) # SHR operation
ref_7712 = ref_7705 # MOV operation
ref_7744 = ref_7712 # MOV operation
ref_7756 = ref_7300 # MOV operation
ref_7758 = (ref_7756 | ref_7744) # OR operation
ref_7795 = ref_7758 # MOV operation
ref_7807 = ref_6883 # MOV operation
ref_7809 = ((ref_7795 - ref_7807) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_7817 = ref_7809 # MOV operation
ref_7851 = ref_7817 # MOV operation
ref_8662 = ref_279 # MOV operation
ref_8694 = ref_8662 # MOV operation
ref_8708 = ((ref_8694 - 0xE8D4346) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_8716 = ref_8708 # MOV operation
ref_8750 = ref_8716 # MOV operation
ref_9448 = ref_5973 # MOV operation
ref_9472 = ref_9448 # MOV operation
ref_9478 = ((0x20453EE3 + ref_9472) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_9931 = ref_279 # MOV operation
ref_9963 = ref_9931 # MOV operation
ref_9975 = ref_9478 # MOV operation
ref_9977 = ((ref_9963 - ref_9975) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_9985 = ref_9977 # MOV operation
ref_10019 = ref_9985 # MOV operation
ref_11225 = ref_5973 # MOV operation
ref_11793 = ref_8750 # MOV operation
ref_11811 = ref_11793 # MOV operation
ref_11823 = ref_11225 # MOV operation
ref_11825 = (ref_11823 | ref_11811) # OR operation
ref_11872 = ref_11825 # MOV operation
ref_11878 = (0x3F & ref_11872) # AND operation
ref_11925 = ref_11878 # MOV operation
ref_11933 = ((ref_11925 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_11940 = ref_11933 # MOV operation
ref_12358 = ref_5973 # MOV operation
ref_12382 = ref_12358 # MOV operation
ref_12386 = ref_11940 # MOV operation
ref_12388 = (ref_12386 | ref_12382) # OR operation
ref_12489 = ref_12388 # MOV operation
ref_13293 = ref_7851 # MOV operation
ref_13729 = ref_12489 # MOV operation
ref_13863 = ref_13729 # MOV operation
ref_13871 = (ref_13863 >> (0x1 & 0x3F)) # SHR operation
ref_13878 = ref_13871 # MOV operation
ref_13920 = ref_13878 # MOV operation
ref_13926 = (0xF & ref_13920) # AND operation
ref_13963 = ref_13926 # MOV operation
ref_13977 = (0x1 | ref_13963) # OR operation
ref_14044 = ref_13977 # MOV operation
ref_14046 = ((0x40 - ref_14044) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_14054 = ref_14046 # MOV operation
ref_14086 = ref_13293 # MOV operation
ref_14098 = ref_14054 # MOV operation
ref_14100 = ((ref_14086 << ((ref_14098 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_14469 = ref_7851 # MOV operation
ref_14905 = ref_12489 # MOV operation
ref_15039 = ref_14905 # MOV operation
ref_15047 = (ref_15039 >> (0x1 & 0x3F)) # SHR operation
ref_15054 = ref_15047 # MOV operation
ref_15096 = ref_15054 # MOV operation
ref_15102 = (0xF & ref_15096) # AND operation
ref_15139 = ref_15102 # MOV operation
ref_15153 = (0x1 | ref_15139) # OR operation
ref_15190 = ref_14469 # MOV operation
ref_15202 = ref_15153 # MOV operation
ref_15204 = (ref_15190 >> ((ref_15202 & 0xFF) & 0x3F)) # SHR operation
ref_15241 = ref_15204 # MOV operation
ref_15253 = ref_14100 # MOV operation
ref_15255 = (ref_15253 | ref_15241) # OR operation
ref_15294 = ref_15255 # MOV operation
ref_15994 = ref_10019 # MOV operation
ref_16562 = ref_15294 # MOV operation
ref_16580 = ref_16562 # MOV operation
ref_16592 = ref_15994 # MOV operation
ref_16594 = ((ref_16580 - ref_16592) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_16602 = ref_16594 # MOV operation
ref_16636 = ref_16602 # MOV operation
ref_18076 = ref_12489 # MOV operation
ref_18458 = ref_7851 # MOV operation
ref_18508 = ref_18458 # MOV operation
ref_18522 = (0xF & ref_18508) # AND operation
ref_18635 = ref_18522 # MOV operation
ref_18649 = (0x1 | ref_18635) # OR operation
ref_18700 = ref_18649 # MOV operation
ref_18702 = ((0x40 - ref_18700) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_18710 = ref_18702 # MOV operation
ref_18742 = ref_18076 # MOV operation
ref_18754 = ref_18710 # MOV operation
ref_18756 = ((ref_18742 << ((ref_18754 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_19125 = ref_12489 # MOV operation
ref_19507 = ref_7851 # MOV operation
ref_19557 = ref_19507 # MOV operation
ref_19571 = (0xF & ref_19557) # AND operation
ref_19684 = ref_19571 # MOV operation
ref_19698 = (0x1 | ref_19684) # OR operation
ref_19735 = ref_19125 # MOV operation
ref_19747 = ref_19698 # MOV operation
ref_19749 = (ref_19735 >> ((ref_19747 & 0xFF) & 0x3F)) # SHR operation
ref_19786 = ref_19749 # MOV operation
ref_19798 = ref_18756 # MOV operation
ref_19800 = (ref_19798 | ref_19786) # OR operation
ref_20187 = ref_10019 # MOV operation
ref_20551 = ref_16636 # MOV operation
ref_20575 = ref_20551 # MOV operation
ref_20579 = ref_20187 # MOV operation
ref_20581 = (ref_20579 | ref_20575) # OR operation
ref_20720 = ref_20581 # MOV operation
ref_20728 = (ref_20720 >> (0x1 & 0x3F)) # SHR operation
ref_20735 = ref_20728 # MOV operation
ref_20777 = ref_20735 # MOV operation
ref_20783 = (0x7 & ref_20777) # AND operation
ref_20820 = ref_20783 # MOV operation
ref_20834 = (0x1 | ref_20820) # OR operation
ref_20871 = ref_19800 # MOV operation
ref_20883 = ref_20834 # MOV operation
ref_20885 = ((ref_20871 << ((ref_20883 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_20924 = ref_20885 # MOV operation
ref_21139 = ref_20924 # MOV operation
ref_21141 = ref_21139 # MOV operation

print(ref_21141 & 0xffffffffffffffff)
