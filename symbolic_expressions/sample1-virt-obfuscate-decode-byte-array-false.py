#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_264 = SymVar_0
ref_279 = ref_264 # MOV operation
ref_76088 = ref_279 # MOV operation
ref_76363 = ref_76088 # MOV operation
ref_76371 = (ref_76363 >> (0x7 & 0x3F)) # SHR operation
ref_76378 = ref_76371 # MOV operation
ref_77660 = ref_279 # MOV operation
ref_77769 = ref_77660 # MOV operation
ref_77783 = ((ref_77769 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_77889 = ref_76378 # MOV operation
ref_77893 = ref_77783 # MOV operation
ref_77895 = (ref_77893 | ref_77889) # OR operation
ref_79108 = ref_77895 # MOV operation
ref_80484 = ref_79108 # MOV operation
ref_80551 = ref_80484 # MOV operation
ref_80553 = ((ref_80551 + 0x2D4AF89B) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_80858 = ref_80553 # MOV operation
ref_80860 = (ref_80858 & 0x1D5ABF66) # AND operation
ref_81989 = ref_279 # MOV operation
ref_82264 = ref_81989 # MOV operation
ref_82272 = (ref_82264 >> (0xB & 0x3F)) # SHR operation
ref_82279 = ref_82272 # MOV operation
ref_83561 = ref_279 # MOV operation
ref_83670 = ref_83561 # MOV operation
ref_83684 = ((ref_83670 << (0x35 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_83790 = ref_82279 # MOV operation
ref_83794 = ref_83684 # MOV operation
ref_83796 = (ref_83794 | ref_83790) # OR operation
ref_83894 = ref_83796 # MOV operation
ref_83906 = ref_80860 # MOV operation
ref_83908 = ((ref_83894 - ref_83906) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_83916 = ref_83908 # MOV operation
ref_85124 = ref_83916 # MOV operation
ref_86406 = ref_279 # MOV operation
ref_86479 = ref_86406 # MOV operation
ref_86493 = ((ref_86479 - 0xE8D4346) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_86501 = ref_86493 # MOV operation
ref_87709 = ref_86501 # MOV operation
ref_88927 = ref_79108 # MOV operation
ref_89148 = ref_88927 # MOV operation
ref_89154 = ((0x20453EE3 + ref_89148) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_90284 = ref_279 # MOV operation
ref_90357 = ref_90284 # MOV operation
ref_90369 = ref_89154 # MOV operation
ref_90371 = ((ref_90357 - ref_90369) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_90379 = ref_90371 # MOV operation
ref_91587 = ref_90379 # MOV operation
ref_94172 = ref_79108 # MOV operation
ref_96051 = ref_87709 # MOV operation
ref_97361 = ref_79108 # MOV operation
ref_97442 = ref_96051 # MOV operation
ref_97446 = ref_97361 # MOV operation
ref_97448 = (ref_97446 | ref_97442) # OR operation
ref_97582 = ref_97448 # MOV operation
ref_97596 = (0x3F & ref_97582) # AND operation
ref_97730 = ref_97596 # MOV operation
ref_97744 = ((ref_97730 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_97850 = ref_94172 # MOV operation
ref_97854 = ref_97744 # MOV operation
ref_97856 = (ref_97854 | ref_97850) # OR operation
ref_99181 = ref_97856 # MOV operation
ref_100399 = ref_85124 # MOV operation
ref_101867 = ref_99181 # MOV operation
ref_102142 = ref_101867 # MOV operation
ref_102150 = (ref_102142 >> (0x1 & 0x3F)) # SHR operation
ref_102157 = ref_102150 # MOV operation
ref_102286 = ref_102157 # MOV operation
ref_102300 = (0xF & ref_102286) # AND operation
ref_102564 = ref_102300 # MOV operation
ref_102570 = (0x1 | ref_102564) # OR operation
ref_102712 = ref_100399 # MOV operation
ref_102716 = ref_102570 # MOV operation
ref_102718 = (ref_102716 & 0xFFFFFFFF) # MOV operation
ref_102720 = (ref_102712 >> ((ref_102718 & 0xFF) & 0x3F)) # SHR operation
ref_102727 = ref_102720 # MOV operation
ref_104215 = ref_99181 # MOV operation
ref_104490 = ref_104215 # MOV operation
ref_104498 = (ref_104490 >> (0x1 & 0x3F)) # SHR operation
ref_104505 = ref_104498 # MOV operation
ref_104634 = ref_104505 # MOV operation
ref_104648 = (0xF & ref_104634) # AND operation
ref_104912 = ref_104648 # MOV operation
ref_104918 = (0x1 | ref_104912) # OR operation
ref_105186 = ref_104918 # MOV operation
ref_105188 = ((0x40 - ref_105186) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_105196 = ref_105188 # MOV operation
ref_106414 = ref_85124 # MOV operation
ref_106523 = ref_106414 # MOV operation
ref_106535 = ref_105196 # MOV operation
ref_106537 = ((ref_106523 << ((ref_106535 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_106643 = ref_102727 # MOV operation
ref_106647 = ref_106537 # MOV operation
ref_106649 = (ref_106647 | ref_106643) # OR operation
ref_108227 = ref_106649 # MOV operation
ref_109445 = ref_91587 # MOV operation
ref_111008 = ref_108227 # MOV operation
ref_111081 = ref_111008 # MOV operation
ref_111093 = ref_109445 # MOV operation
ref_111095 = ((ref_111081 - ref_111093) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_111103 = ref_111095 # MOV operation
ref_112311 = ref_111103 # MOV operation
ref_115498 = ref_112311 # MOV operation
ref_116696 = ref_91587 # MOV operation
ref_116777 = ref_115498 # MOV operation
ref_116781 = ref_116696 # MOV operation
ref_116783 = (ref_116781 | ref_116777) # OR operation
ref_117083 = ref_116783 # MOV operation
ref_117091 = (ref_117083 >> (0x1 & 0x3F)) # SHR operation
ref_117098 = ref_117091 # MOV operation
ref_117227 = ref_117098 # MOV operation
ref_117241 = (0x7 & ref_117227) # AND operation
ref_117505 = ref_117241 # MOV operation
ref_117511 = (0x1 | ref_117505) # OR operation
ref_118734 = ref_99181 # MOV operation
ref_120090 = ref_85124 # MOV operation
ref_120199 = ref_120090 # MOV operation
ref_120213 = (0xF & ref_120199) # AND operation
ref_120477 = ref_120213 # MOV operation
ref_120483 = (0x1 | ref_120477) # OR operation
ref_120625 = ref_118734 # MOV operation
ref_120629 = ref_120483 # MOV operation
ref_120631 = (ref_120629 & 0xFFFFFFFF) # MOV operation
ref_120633 = (ref_120625 >> ((ref_120631 & 0xFF) & 0x3F)) # SHR operation
ref_120640 = ref_120633 # MOV operation
ref_122016 = ref_85124 # MOV operation
ref_122125 = ref_122016 # MOV operation
ref_122139 = (0xF & ref_122125) # AND operation
ref_122403 = ref_122139 # MOV operation
ref_122409 = (0x1 | ref_122403) # OR operation
ref_122677 = ref_122409 # MOV operation
ref_122679 = ((0x40 - ref_122677) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_122687 = ref_122679 # MOV operation
ref_123905 = ref_99181 # MOV operation
ref_124014 = ref_123905 # MOV operation
ref_124026 = ref_122687 # MOV operation
ref_124028 = ((ref_124014 << ((ref_124026 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_124134 = ref_120640 # MOV operation
ref_124138 = ref_124028 # MOV operation
ref_124140 = (ref_124138 | ref_124134) # OR operation
ref_124274 = ref_124140 # MOV operation
ref_124286 = ref_117511 # MOV operation
ref_124288 = ((ref_124274 << ((ref_124286 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_125416 = ref_124288 # MOV operation
ref_125684 = ref_125416 # MOV operation
ref_125686 = ref_125684 # MOV operation

print(ref_125686 & 0xffffffffffffffff)
