#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_5594 = ref_278 # MOV operation
ref_5670 = ref_5594 # MOV operation
ref_5684 = ((ref_5670 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_6522 = ref_278 # MOV operation
ref_6722 = ref_6522 # MOV operation
ref_6730 = (ref_6722 >> (0x7 & 0x3F)) # SHR operation
ref_6737 = ref_6730 # MOV operation
ref_6833 = ref_6737 # MOV operation
ref_6845 = ref_5684 # MOV operation
ref_6847 = (ref_6845 | ref_6833) # OR operation
ref_7778 = ref_6847 # MOV operation
ref_8727 = ref_278 # MOV operation
ref_8803 = ref_8727 # MOV operation
ref_8817 = ((ref_8803 << (0x35 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_9655 = ref_278 # MOV operation
ref_9855 = ref_9655 # MOV operation
ref_9863 = (ref_9855 >> (0xB & 0x3F)) # SHR operation
ref_9870 = ref_9863 # MOV operation
ref_9966 = ref_9870 # MOV operation
ref_9978 = ref_8817 # MOV operation
ref_9980 = (ref_9978 | ref_9966) # OR operation
ref_11019 = ref_7778 # MOV operation
ref_11107 = ref_11019 # MOV operation
ref_11109 = ((ref_11107 + 0x2D4AF89B) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_11339 = ref_11109 # MOV operation
ref_11341 = (ref_11339 & 0x1D5ABF66) # AND operation
ref_11450 = ref_9980 # MOV operation
ref_11454 = ref_11341 # MOV operation
ref_11456 = ((ref_11450 - ref_11454) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_11464 = ref_11456 # MOV operation
ref_12390 = ref_11464 # MOV operation
ref_13223 = ref_278 # MOV operation
ref_13423 = ref_13223 # MOV operation
ref_13429 = ((ref_13423 - 0xE8D4346) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_13437 = ref_13429 # MOV operation
ref_14363 = ref_13437 # MOV operation
ref_15196 = ref_278 # MOV operation
ref_16094 = ref_7778 # MOV operation
ref_16294 = ref_16094 # MOV operation
ref_16300 = ((0x20453EE3 + ref_16294) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_16410 = ref_15196 # MOV operation
ref_16414 = ref_16300 # MOV operation
ref_16416 = ((ref_16410 - ref_16414) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_16424 = ref_16416 # MOV operation
ref_17350 = ref_16424 # MOV operation
ref_19573 = ref_7778 # MOV operation
ref_20791 = ref_14363 # MOV operation
ref_20867 = ref_20791 # MOV operation
ref_20879 = ref_19573 # MOV operation
ref_20881 = (ref_20879 | ref_20867) # OR operation
ref_20982 = ref_20881 # MOV operation
ref_20996 = (0x3F & ref_20982) # AND operation
ref_21097 = ref_20996 # MOV operation
ref_21111 = ((ref_21097 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_22122 = ref_7778 # MOV operation
ref_22198 = ref_22122 # MOV operation
ref_22210 = ref_21111 # MOV operation
ref_22212 = (ref_22210 | ref_22198) # OR operation
ref_23231 = ref_22212 # MOV operation
ref_24585 = ref_23231 # MOV operation
ref_24785 = ref_24585 # MOV operation
ref_24793 = (ref_24785 >> (0x1 & 0x3F)) # SHR operation
ref_24800 = ref_24793 # MOV operation
ref_24896 = ref_24800 # MOV operation
ref_24910 = (0xF & ref_24896) # AND operation
ref_25011 = ref_24910 # MOV operation
ref_25025 = (0x1 | ref_25011) # OR operation
ref_25138 = ref_25025 # MOV operation
ref_25140 = ((0x40 - ref_25138) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_25148 = ref_25140 # MOV operation
ref_26066 = ref_12390 # MOV operation
ref_26142 = ref_26066 # MOV operation
ref_26154 = ref_25148 # MOV operation
ref_26156 = ((ref_26142 << ((ref_26154 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_27079 = ref_12390 # MOV operation
ref_28297 = ref_23231 # MOV operation
ref_28497 = ref_28297 # MOV operation
ref_28505 = (ref_28497 >> (0x1 & 0x3F)) # SHR operation
ref_28512 = ref_28505 # MOV operation
ref_28608 = ref_28512 # MOV operation
ref_28622 = (0xF & ref_28608) # AND operation
ref_28723 = ref_28622 # MOV operation
ref_28737 = (0x1 | ref_28723) # OR operation
ref_28846 = ref_27079 # MOV operation
ref_28850 = ref_28737 # MOV operation
ref_28852 = (ref_28850 & 0xFFFFFFFF) # MOV operation
ref_28854 = (ref_28846 >> ((ref_28852 & 0xFF) & 0x3F)) # SHR operation
ref_28861 = ref_28854 # MOV operation
ref_28957 = ref_28861 # MOV operation
ref_28969 = ref_26156 # MOV operation
ref_28971 = (ref_28969 | ref_28957) # OR operation
ref_30222 = ref_28971 # MOV operation
ref_31460 = ref_30222 # MOV operation
ref_32358 = ref_17350 # MOV operation
ref_32442 = ref_31460 # MOV operation
ref_32446 = ref_32358 # MOV operation
ref_32448 = ((ref_32442 - ref_32446) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_32456 = ref_32448 # MOV operation
ref_33382 = ref_32456 # MOV operation
ref_35998 = ref_17350 # MOV operation
ref_36896 = ref_33382 # MOV operation
ref_36972 = ref_36896 # MOV operation
ref_36984 = ref_35998 # MOV operation
ref_36986 = (ref_36984 | ref_36972) # OR operation
ref_37211 = ref_36986 # MOV operation
ref_37219 = (ref_37211 >> (0x1 & 0x3F)) # SHR operation
ref_37226 = ref_37219 # MOV operation
ref_37322 = ref_37226 # MOV operation
ref_37336 = (0x7 & ref_37322) # AND operation
ref_37437 = ref_37336 # MOV operation
ref_37451 = (0x1 | ref_37437) # OR operation
ref_38722 = ref_12390 # MOV operation
ref_38798 = ref_38722 # MOV operation
ref_38812 = (0xF & ref_38798) # AND operation
ref_38913 = ref_38812 # MOV operation
ref_38927 = (0x1 | ref_38913) # OR operation
ref_39040 = ref_38927 # MOV operation
ref_39042 = ((0x40 - ref_39040) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_39050 = ref_39042 # MOV operation
ref_39968 = ref_23231 # MOV operation
ref_40044 = ref_39968 # MOV operation
ref_40056 = ref_39050 # MOV operation
ref_40058 = ((ref_40044 << ((ref_40056 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_40981 = ref_23231 # MOV operation
ref_42111 = ref_12390 # MOV operation
ref_42187 = ref_42111 # MOV operation
ref_42201 = (0xF & ref_42187) # AND operation
ref_42302 = ref_42201 # MOV operation
ref_42316 = (0x1 | ref_42302) # OR operation
ref_42425 = ref_40981 # MOV operation
ref_42429 = ref_42316 # MOV operation
ref_42431 = (ref_42429 & 0xFFFFFFFF) # MOV operation
ref_42433 = (ref_42425 >> ((ref_42431 & 0xFF) & 0x3F)) # SHR operation
ref_42440 = ref_42433 # MOV operation
ref_42536 = ref_42440 # MOV operation
ref_42548 = ref_40058 # MOV operation
ref_42550 = (ref_42548 | ref_42536) # OR operation
ref_42651 = ref_42550 # MOV operation
ref_42663 = ref_37451 # MOV operation
ref_42665 = ((ref_42651 << ((ref_42663 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_43520 = ref_42665 # MOV operation
ref_43731 = ref_43520 # MOV operation
ref_43733 = ref_43731 # MOV operation

print(ref_43733 & 0xffffffffffffffff)
