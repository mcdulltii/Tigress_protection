#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_264 = SymVar_0
ref_279 = ref_264 # MOV operation
ref_6812 = ref_279 # MOV operation
ref_7096 = ref_6812 # MOV operation
ref_7104 = ((ref_7096 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_7111 = ref_7104 # MOV operation
ref_8253 = ref_279 # MOV operation
ref_8492 = ref_8253 # MOV operation
ref_8500 = (ref_8492 >> (0x7 & 0x3F)) # SHR operation
ref_8507 = ref_8500 # MOV operation
ref_8636 = ref_8507 # MOV operation
ref_8648 = ref_7111 # MOV operation
ref_8650 = (ref_8648 | ref_8636) # OR operation
ref_8774 = ref_8650 # MOV operation
ref_11122 = ref_8774 # MOV operation
ref_11401 = ref_11122 # MOV operation
ref_11403 = ((ref_11401 + 0x2D4AF89B) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_11532 = ref_11403 # MOV operation
ref_11534 = (ref_11532 & 0x1D5ABF66) # AND operation
ref_12681 = ref_279 # MOV operation
ref_12965 = ref_12681 # MOV operation
ref_12973 = ((ref_12965 << (0x35 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_12980 = ref_12973 # MOV operation
ref_14122 = ref_279 # MOV operation
ref_14361 = ref_14122 # MOV operation
ref_14369 = (ref_14361 >> (0xB & 0x3F)) # SHR operation
ref_14376 = ref_14369 # MOV operation
ref_14505 = ref_14376 # MOV operation
ref_14517 = ref_12980 # MOV operation
ref_14519 = (ref_14517 | ref_14505) # OR operation
ref_14653 = ref_14519 # MOV operation
ref_14665 = ref_11534 # MOV operation
ref_14667 = ((ref_14653 - ref_14665) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_14675 = ref_14667 # MOV operation
ref_14794 = ref_14675 # MOV operation
ref_17120 = ref_279 # MOV operation
ref_17229 = ref_17120 # MOV operation
ref_17243 = ((ref_17229 - 0xE8D4346) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_17251 = ref_17243 # MOV operation
ref_17370 = ref_17251 # MOV operation
ref_19718 = ref_8774 # MOV operation
ref_19827 = ref_19718 # MOV operation
ref_19841 = ((0x20453EE3 + ref_19827) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_20989 = ref_279 # MOV operation
ref_21098 = ref_20989 # MOV operation
ref_21110 = ref_19841 # MOV operation
ref_21112 = ((ref_21098 - ref_21110) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_21120 = ref_21112 # MOV operation
ref_21239 = ref_21120 # MOV operation
ref_24926 = ref_8774 # MOV operation
ref_26507 = ref_17370 # MOV operation
ref_26616 = ref_26507 # MOV operation
ref_26628 = ref_24926 # MOV operation
ref_26630 = (ref_26628 | ref_26616) # OR operation
ref_26912 = ref_26630 # MOV operation
ref_26918 = (0x3F & ref_26912) # AND operation
ref_27227 = ref_26918 # MOV operation
ref_27235 = ((ref_27227 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_27242 = ref_27235 # MOV operation
ref_28536 = ref_8774 # MOV operation
ref_28645 = ref_28536 # MOV operation
ref_28657 = ref_27242 # MOV operation
ref_28659 = (ref_28657 | ref_28645) # OR operation
ref_28783 = ref_28659 # MOV operation
ref_31410 = ref_14794 # MOV operation
ref_32842 = ref_28783 # MOV operation
ref_33081 = ref_32842 # MOV operation
ref_33089 = (ref_33081 >> (0x1 & 0x3F)) # SHR operation
ref_33096 = ref_33089 # MOV operation
ref_33373 = ref_33096 # MOV operation
ref_33379 = (0xF & ref_33373) # AND operation
ref_33513 = ref_33379 # MOV operation
ref_33527 = (0x1 | ref_33513) # OR operation
ref_33831 = ref_33527 # MOV operation
ref_33833 = ((0x40 - ref_33831) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_33841 = ref_33833 # MOV operation
ref_33987 = ref_31410 # MOV operation
ref_33991 = ref_33841 # MOV operation
ref_33993 = (ref_33991 & 0xFFFFFFFF) # MOV operation
ref_33995 = ((ref_33987 << ((ref_33993 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_34002 = ref_33995 # MOV operation
ref_35166 = ref_14794 # MOV operation
ref_36598 = ref_28783 # MOV operation
ref_36837 = ref_36598 # MOV operation
ref_36845 = (ref_36837 >> (0x1 & 0x3F)) # SHR operation
ref_36852 = ref_36845 # MOV operation
ref_37129 = ref_36852 # MOV operation
ref_37135 = (0xF & ref_37129) # AND operation
ref_37269 = ref_37135 # MOV operation
ref_37283 = (0x1 | ref_37269) # OR operation
ref_37389 = ref_35166 # MOV operation
ref_37393 = ref_37283 # MOV operation
ref_37395 = (ref_37393 & 0xFFFFFFFF) # MOV operation
ref_37397 = (ref_37389 >> ((ref_37395 & 0xFF) & 0x3F)) # SHR operation
ref_37404 = ref_37397 # MOV operation
ref_37533 = ref_37404 # MOV operation
ref_37545 = ref_34002 # MOV operation
ref_37547 = (ref_37545 | ref_37533) # OR operation
ref_37671 = ref_37547 # MOV operation
ref_39861 = ref_21239 # MOV operation
ref_41442 = ref_37671 # MOV operation
ref_41551 = ref_41442 # MOV operation
ref_41563 = ref_39861 # MOV operation
ref_41565 = ((ref_41551 - ref_41563) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_41573 = ref_41565 # MOV operation
ref_41692 = ref_41573 # MOV operation
ref_45662 = ref_28783 # MOV operation
ref_46964 = ref_14794 # MOV operation
ref_47221 = ref_46964 # MOV operation
ref_47227 = (0xF & ref_47221) # AND operation
ref_47361 = ref_47227 # MOV operation
ref_47375 = (0x1 | ref_47361) # OR operation
ref_47679 = ref_47375 # MOV operation
ref_47681 = ((0x40 - ref_47679) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_47689 = ref_47681 # MOV operation
ref_47835 = ref_45662 # MOV operation
ref_47839 = ref_47689 # MOV operation
ref_47841 = (ref_47839 & 0xFFFFFFFF) # MOV operation
ref_47843 = ((ref_47835 << ((ref_47841 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_47850 = ref_47843 # MOV operation
ref_49014 = ref_28783 # MOV operation
ref_50316 = ref_14794 # MOV operation
ref_50573 = ref_50316 # MOV operation
ref_50579 = (0xF & ref_50573) # AND operation
ref_50713 = ref_50579 # MOV operation
ref_50727 = (0x1 | ref_50713) # OR operation
ref_50833 = ref_49014 # MOV operation
ref_50837 = ref_50727 # MOV operation
ref_50839 = (ref_50837 & 0xFFFFFFFF) # MOV operation
ref_50841 = (ref_50833 >> ((ref_50839 & 0xFF) & 0x3F)) # SHR operation
ref_50848 = ref_50841 # MOV operation
ref_50977 = ref_50848 # MOV operation
ref_50989 = ref_47850 # MOV operation
ref_50991 = (ref_50989 | ref_50977) # OR operation
ref_52318 = ref_21239 # MOV operation
ref_53462 = ref_41692 # MOV operation
ref_53571 = ref_53462 # MOV operation
ref_53583 = ref_52318 # MOV operation
ref_53585 = (ref_53583 | ref_53571) # OR operation
ref_53849 = ref_53585 # MOV operation
ref_53857 = (ref_53849 >> (0x1 & 0x3F)) # SHR operation
ref_53864 = ref_53857 # MOV operation
ref_54141 = ref_53864 # MOV operation
ref_54147 = (0x7 & ref_54141) # AND operation
ref_54281 = ref_54147 # MOV operation
ref_54295 = (0x1 | ref_54281) # OR operation
ref_54446 = ref_50991 # MOV operation
ref_54450 = ref_54295 # MOV operation
ref_54452 = (ref_54450 & 0xFFFFFFFF) # MOV operation
ref_54454 = ((ref_54446 << ((ref_54452 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_54461 = ref_54454 # MOV operation
ref_54580 = ref_54461 # MOV operation
ref_54812 = ref_54580 # MOV operation
ref_54814 = ref_54812 # MOV operation

print(ref_54814 & 0xffffffffffffffff)
