#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_264 = SymVar_0
ref_279 = ref_264 # MOV operation
ref_10138 = ref_279 # MOV operation
ref_10808 = ref_10138 # MOV operation
ref_10818 = ((ref_10808 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_10825 = ref_10818 # MOV operation
ref_13604 = ref_279 # MOV operation
ref_14276 = ref_13604 # MOV operation
ref_14286 = (ref_14276 >> (0x7 & 0x3F)) # SHR operation
ref_14293 = ref_14286 # MOV operation
ref_14657 = ref_14293 # MOV operation
ref_14671 = ref_10825 # MOV operation
ref_14673 = (ref_14671 | ref_14657) # OR operation
ref_15008 = ref_14673 # MOV operation
ref_20480 = ref_279 # MOV operation
ref_21151 = ref_20480 # MOV operation
ref_21161 = ((ref_21151 << (0x35 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_21168 = ref_21161 # MOV operation
ref_24009 = ref_279 # MOV operation
ref_24719 = ref_24009 # MOV operation
ref_24729 = (ref_24719 >> (0xB & 0x3F)) # SHR operation
ref_24736 = ref_24729 # MOV operation
ref_25052 = ref_24736 # MOV operation
ref_25066 = ref_21168 # MOV operation
ref_25068 = (ref_25066 | ref_25052) # OR operation
ref_28377 = ref_15008 # MOV operation
ref_28788 = ref_28377 # MOV operation
ref_28790 = ((ref_28788 + 0x2D4AF89B) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_29509 = ref_28790 # MOV operation
ref_29511 = (ref_29509 & 0x1D5ABF66) # AND operation
ref_29912 = ref_25068 # MOV operation
ref_29918 = ref_29511 # MOV operation
ref_29920 = ((ref_29912 - ref_29918) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_29928 = ref_29920 # MOV operation
ref_30212 = ref_29928 # MOV operation
ref_35632 = ref_279 # MOV operation
ref_36313 = ref_35632 # MOV operation
ref_36321 = ((ref_36313 - 0xE8D4346) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_36329 = ref_36321 # MOV operation
ref_36697 = ref_36329 # MOV operation
ref_42110 = ref_279 # MOV operation
ref_45039 = ref_15008 # MOV operation
ref_45754 = ref_45039 # MOV operation
ref_45762 = ((0x20453EE3 + ref_45754) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_46136 = ref_42110 # MOV operation
ref_46142 = ref_45762 # MOV operation
ref_46144 = ((ref_46136 - ref_46142) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_46152 = ref_46144 # MOV operation
ref_46496 = ref_46152 # MOV operation
ref_56313 = ref_15008 # MOV operation
ref_60281 = ref_36697 # MOV operation
ref_60581 = ref_60281 # MOV operation
ref_60595 = ref_56313 # MOV operation
ref_60597 = (ref_60595 | ref_60581) # OR operation
ref_60950 = ref_60597 # MOV operation
ref_60966 = (0x3F & ref_60950) # AND operation
ref_61721 = ref_60966 # MOV operation
ref_61731 = ((ref_61721 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_61738 = ref_61731 # MOV operation
ref_65008 = ref_15008 # MOV operation
ref_65307 = ref_65008 # MOV operation
ref_65321 = ref_61738 # MOV operation
ref_65323 = (ref_65321 | ref_65307) # OR operation
ref_65706 = ref_65323 # MOV operation
ref_72239 = ref_30212 # MOV operation
ref_76641 = ref_65706 # MOV operation
ref_77331 = ref_76641 # MOV operation
ref_77341 = (ref_77331 >> (0x1 & 0x3F)) # SHR operation
ref_77348 = ref_77341 # MOV operation
ref_77703 = ref_77348 # MOV operation
ref_77719 = (0xF & ref_77703) # AND operation
ref_78094 = ref_77719 # MOV operation
ref_78110 = (0x1 | ref_78094) # OR operation
ref_78467 = ref_78110 # MOV operation
ref_78469 = ((0x40 - ref_78467) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_78477 = ref_78469 # MOV operation
ref_78817 = ref_72239 # MOV operation
ref_78823 = ref_78477 # MOV operation
ref_78825 = (ref_78823 & 0xFFFFFFFF) # MOV operation
ref_78827 = ((ref_78817 << ((ref_78825 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_78834 = ref_78827 # MOV operation
ref_81771 = ref_30212 # MOV operation
ref_85794 = ref_65706 # MOV operation
ref_86515 = ref_85794 # MOV operation
ref_86525 = (ref_86515 >> (0x1 & 0x3F)) # SHR operation
ref_86532 = ref_86525 # MOV operation
ref_86848 = ref_86532 # MOV operation
ref_86864 = (0xF & ref_86848) # AND operation
ref_87211 = ref_86864 # MOV operation
ref_87227 = (0x1 | ref_87211) # OR operation
ref_87578 = ref_81771 # MOV operation
ref_87584 = ref_87227 # MOV operation
ref_87586 = (ref_87584 & 0xFFFFFFFF) # MOV operation
ref_87588 = (ref_87578 >> ((ref_87586 & 0xFF) & 0x3F)) # SHR operation
ref_87595 = ref_87588 # MOV operation
ref_87933 = ref_87595 # MOV operation
ref_87947 = ref_78834 # MOV operation
ref_87949 = (ref_87947 | ref_87933) # OR operation
ref_88284 = ref_87949 # MOV operation
ref_94744 = ref_88284 # MOV operation
ref_97613 = ref_46496 # MOV operation
ref_97931 = ref_94744 # MOV operation
ref_97937 = ref_97613 # MOV operation
ref_97939 = ((ref_97931 - ref_97937) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_97947 = ref_97939 # MOV operation
ref_98272 = ref_97947 # MOV operation
ref_108713 = ref_65706 # MOV operation
ref_112713 = ref_30212 # MOV operation
ref_113038 = ref_112713 # MOV operation
ref_113054 = (0xF & ref_113038) # AND operation
ref_113464 = ref_113054 # MOV operation
ref_113480 = (0x1 | ref_113464) # OR operation
ref_113849 = ref_113480 # MOV operation
ref_113851 = ((0x40 - ref_113849) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_113859 = ref_113851 # MOV operation
ref_114179 = ref_108713 # MOV operation
ref_114185 = ref_113859 # MOV operation
ref_114187 = (ref_114185 & 0xFFFFFFFF) # MOV operation
ref_114189 = ((ref_114179 << ((ref_114187 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_114196 = ref_114189 # MOV operation
ref_117071 = ref_65706 # MOV operation
ref_120723 = ref_30212 # MOV operation
ref_121051 = ref_120723 # MOV operation
ref_121067 = (0xF & ref_121051) # AND operation
ref_121442 = ref_121067 # MOV operation
ref_121458 = (0x1 | ref_121442) # OR operation
ref_121783 = ref_117071 # MOV operation
ref_121789 = ref_121458 # MOV operation
ref_121791 = (ref_121789 & 0xFFFFFFFF) # MOV operation
ref_121793 = (ref_121783 >> ((ref_121791 & 0xFF) & 0x3F)) # SHR operation
ref_121800 = ref_121793 # MOV operation
ref_122170 = ref_121800 # MOV operation
ref_122184 = ref_114196 # MOV operation
ref_122186 = (ref_122184 | ref_122170) # OR operation
ref_125881 = ref_46496 # MOV operation
ref_128771 = ref_98272 # MOV operation
ref_129081 = ref_128771 # MOV operation
ref_129095 = ref_125881 # MOV operation
ref_129097 = (ref_129095 | ref_129081) # OR operation
ref_129845 = ref_129097 # MOV operation
ref_129855 = (ref_129845 >> (0x1 & 0x3F)) # SHR operation
ref_129862 = ref_129855 # MOV operation
ref_130230 = ref_129862 # MOV operation
ref_130246 = (0x7 & ref_130230) # AND operation
ref_130597 = ref_130246 # MOV operation
ref_130613 = (0x1 | ref_130597) # OR operation
ref_130996 = ref_122186 # MOV operation
ref_131002 = ref_130613 # MOV operation
ref_131004 = (ref_131002 & 0xFFFFFFFF) # MOV operation
ref_131006 = ((ref_130996 << ((ref_131004 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_131013 = ref_131006 # MOV operation
ref_131338 = ref_131013 # MOV operation
ref_132068 = ref_131338 # MOV operation
ref_132070 = ref_132068 # MOV operation

print(ref_132070 & 0xffffffffffffffff)
