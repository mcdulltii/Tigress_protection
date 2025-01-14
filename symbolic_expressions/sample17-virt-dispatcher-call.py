#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_6105 = SymVar_0
ref_6120 = ref_6105 # MOV operation
ref_13930 = ref_6120 # MOV operation
ref_14372 = ref_13930 # MOV operation
ref_14382 = ((ref_14372 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_14389 = ref_14382 # MOV operation
ref_16192 = ref_6120 # MOV operation
ref_16634 = ref_16192 # MOV operation
ref_16644 = (ref_16634 >> (0x7 & 0x3F)) # SHR operation
ref_16651 = ref_16644 # MOV operation
ref_16868 = ref_16651 # MOV operation
ref_16882 = ref_14389 # MOV operation
ref_16884 = (ref_16882 | ref_16868) # OR operation
ref_17114 = ref_16884 # MOV operation
ref_20900 = ref_17114 # MOV operation
ref_21348 = ref_20900 # MOV operation
ref_21350 = ((ref_21348 + 0x2D4AF89B) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_21587 = ref_21350 # MOV operation
ref_21589 = (ref_21587 & 0x1D5ABF66) # AND operation
ref_23397 = ref_6120 # MOV operation
ref_23839 = ref_23397 # MOV operation
ref_23849 = ((ref_23839 << (0x35 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_23856 = ref_23849 # MOV operation
ref_25659 = ref_6120 # MOV operation
ref_26101 = ref_25659 # MOV operation
ref_26111 = (ref_26101 >> (0xB & 0x3F)) # SHR operation
ref_26118 = ref_26111 # MOV operation
ref_26335 = ref_26118 # MOV operation
ref_26349 = ref_23856 # MOV operation
ref_26351 = (ref_26349 | ref_26335) # OR operation
ref_26573 = ref_26351 # MOV operation
ref_26587 = ref_21589 # MOV operation
ref_26589 = ((ref_26573 - ref_26587) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_26597 = ref_26589 # MOV operation
ref_26822 = ref_26597 # MOV operation
ref_30527 = ref_6120 # MOV operation
ref_30726 = ref_30527 # MOV operation
ref_30742 = ((ref_30726 - 0xE8D4346) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_30750 = ref_30742 # MOV operation
ref_30975 = ref_30750 # MOV operation
ref_34761 = ref_17114 # MOV operation
ref_34960 = ref_34761 # MOV operation
ref_34976 = ((0x20453EE3 + ref_34960) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_36785 = ref_6120 # MOV operation
ref_36984 = ref_36785 # MOV operation
ref_36998 = ref_34976 # MOV operation
ref_37000 = ((ref_36984 - ref_36998) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_37008 = ref_37000 # MOV operation
ref_37233 = ref_37008 # MOV operation
ref_43298 = ref_17114 # MOV operation
ref_45849 = ref_30975 # MOV operation
ref_46048 = ref_45849 # MOV operation
ref_46062 = ref_43298 # MOV operation
ref_46064 = (ref_46062 | ref_46048) # OR operation
ref_46529 = ref_46064 # MOV operation
ref_46537 = (0x3F & ref_46529) # AND operation
ref_47002 = ref_46537 # MOV operation
ref_47012 = ((ref_47002 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_47019 = ref_47012 # MOV operation
ref_49114 = ref_17114 # MOV operation
ref_49313 = ref_49114 # MOV operation
ref_49327 = ref_47019 # MOV operation
ref_49329 = (ref_49327 | ref_49313) # OR operation
ref_49559 = ref_49329 # MOV operation
ref_53795 = ref_26822 # MOV operation
ref_56107 = ref_49559 # MOV operation
ref_56549 = ref_56107 # MOV operation
ref_56559 = (ref_56549 >> (0x1 & 0x3F)) # SHR operation
ref_56566 = ref_56559 # MOV operation
ref_57026 = ref_56566 # MOV operation
ref_57034 = (0xF & ref_57026) # AND operation
ref_57256 = ref_57034 # MOV operation
ref_57272 = (0x1 | ref_57256) # OR operation
ref_57743 = ref_57272 # MOV operation
ref_57745 = ((0x40 - ref_57743) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_57753 = ref_57745 # MOV operation
ref_57978 = ref_53795 # MOV operation
ref_57984 = ref_57753 # MOV operation
ref_57986 = (ref_57984 & 0xFFFFFFFF) # MOV operation
ref_57988 = ((ref_57978 << ((ref_57986 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_57995 = ref_57988 # MOV operation
ref_59879 = ref_26822 # MOV operation
ref_62191 = ref_49559 # MOV operation
ref_62633 = ref_62191 # MOV operation
ref_62643 = (ref_62633 >> (0x1 & 0x3F)) # SHR operation
ref_62650 = ref_62643 # MOV operation
ref_63110 = ref_62650 # MOV operation
ref_63118 = (0xF & ref_63110) # AND operation
ref_63340 = ref_63118 # MOV operation
ref_63356 = (0x1 | ref_63340) # OR operation
ref_63586 = ref_59879 # MOV operation
ref_63592 = ref_63356 # MOV operation
ref_63594 = (ref_63592 & 0xFFFFFFFF) # MOV operation
ref_63596 = (ref_63586 >> ((ref_63594 & 0xFF) & 0x3F)) # SHR operation
ref_63603 = ref_63596 # MOV operation
ref_63820 = ref_63603 # MOV operation
ref_63834 = ref_57995 # MOV operation
ref_63836 = (ref_63834 | ref_63820) # OR operation
ref_64066 = ref_63836 # MOV operation
ref_67617 = ref_37233 # MOV operation
ref_70168 = ref_64066 # MOV operation
ref_70367 = ref_70168 # MOV operation
ref_70381 = ref_67617 # MOV operation
ref_70383 = ((ref_70367 - ref_70381) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_70391 = ref_70383 # MOV operation
ref_70616 = ref_70391 # MOV operation
ref_77282 = ref_49559 # MOV operation
ref_79383 = ref_26822 # MOV operation
ref_79825 = ref_79383 # MOV operation
ref_79833 = (0xF & ref_79825) # AND operation
ref_80055 = ref_79833 # MOV operation
ref_80071 = (0x1 | ref_80055) # OR operation
ref_80542 = ref_80071 # MOV operation
ref_80544 = ((0x40 - ref_80542) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_80552 = ref_80544 # MOV operation
ref_80777 = ref_77282 # MOV operation
ref_80783 = ref_80552 # MOV operation
ref_80785 = (ref_80783 & 0xFFFFFFFF) # MOV operation
ref_80787 = ((ref_80777 << ((ref_80785 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_80794 = ref_80787 # MOV operation
ref_82678 = ref_49559 # MOV operation
ref_84779 = ref_26822 # MOV operation
ref_85221 = ref_84779 # MOV operation
ref_85229 = (0xF & ref_85221) # AND operation
ref_85451 = ref_85229 # MOV operation
ref_85467 = (0x1 | ref_85451) # OR operation
ref_85697 = ref_82678 # MOV operation
ref_85703 = ref_85467 # MOV operation
ref_85705 = (ref_85703 & 0xFFFFFFFF) # MOV operation
ref_85707 = (ref_85697 >> ((ref_85705 & 0xFF) & 0x3F)) # SHR operation
ref_85714 = ref_85707 # MOV operation
ref_85931 = ref_85714 # MOV operation
ref_85945 = ref_80794 # MOV operation
ref_85947 = (ref_85945 | ref_85931) # OR operation
ref_88071 = ref_37233 # MOV operation
ref_89937 = ref_70616 # MOV operation
ref_90136 = ref_89937 # MOV operation
ref_90150 = ref_88071 # MOV operation
ref_90152 = (ref_90150 | ref_90136) # OR operation
ref_90617 = ref_90152 # MOV operation
ref_90627 = (ref_90617 >> (0x1 & 0x3F)) # SHR operation
ref_90634 = ref_90627 # MOV operation
ref_91094 = ref_90634 # MOV operation
ref_91102 = (0x7 & ref_91094) # AND operation
ref_91324 = ref_91102 # MOV operation
ref_91340 = (0x1 | ref_91324) # OR operation
ref_91570 = ref_85947 # MOV operation
ref_91576 = ref_91340 # MOV operation
ref_91578 = (ref_91576 & 0xFFFFFFFF) # MOV operation
ref_91580 = ((ref_91570 << ((ref_91578 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_91587 = ref_91580 # MOV operation
ref_91812 = ref_91587 # MOV operation
ref_92302 = ref_91812 # MOV operation
ref_92304 = ref_92302 # MOV operation

print(ref_92304 & 0xffffffffffffffff)
