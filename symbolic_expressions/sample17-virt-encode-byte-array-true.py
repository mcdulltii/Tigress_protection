#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_69311 = ref_278 # MOV operation
ref_69595 = ref_69311 # MOV operation
ref_69603 = ((ref_69595 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_69610 = ref_69603 # MOV operation
ref_70752 = ref_278 # MOV operation
ref_70991 = ref_70752 # MOV operation
ref_70999 = (ref_70991 >> (0x7 & 0x3F)) # SHR operation
ref_71006 = ref_70999 # MOV operation
ref_71135 = ref_71006 # MOV operation
ref_71147 = ref_69610 # MOV operation
ref_71149 = (ref_71147 | ref_71135) # OR operation
ref_71273 = ref_71149 # MOV operation
ref_73621 = ref_71273 # MOV operation
ref_73900 = ref_73621 # MOV operation
ref_73902 = ((ref_73900 + 0x2D4AF89B) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_74031 = ref_73902 # MOV operation
ref_74033 = (ref_74031 & 0x1D5ABF66) # AND operation
ref_75180 = ref_278 # MOV operation
ref_75464 = ref_75180 # MOV operation
ref_75472 = ((ref_75464 << (0x35 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_75479 = ref_75472 # MOV operation
ref_76621 = ref_278 # MOV operation
ref_76860 = ref_76621 # MOV operation
ref_76868 = (ref_76860 >> (0xB & 0x3F)) # SHR operation
ref_76875 = ref_76868 # MOV operation
ref_77004 = ref_76875 # MOV operation
ref_77016 = ref_75479 # MOV operation
ref_77018 = (ref_77016 | ref_77004) # OR operation
ref_77152 = ref_77018 # MOV operation
ref_77164 = ref_74033 # MOV operation
ref_77166 = ((ref_77152 - ref_77164) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_77174 = ref_77166 # MOV operation
ref_77293 = ref_77174 # MOV operation
ref_79619 = ref_278 # MOV operation
ref_79728 = ref_79619 # MOV operation
ref_79742 = ((ref_79728 - 0xE8D4346) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_79750 = ref_79742 # MOV operation
ref_79869 = ref_79750 # MOV operation
ref_82217 = ref_71273 # MOV operation
ref_82326 = ref_82217 # MOV operation
ref_82340 = ((0x20453EE3 + ref_82326) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_83488 = ref_278 # MOV operation
ref_83597 = ref_83488 # MOV operation
ref_83609 = ref_82340 # MOV operation
ref_83611 = ((ref_83597 - ref_83609) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_83619 = ref_83611 # MOV operation
ref_83738 = ref_83619 # MOV operation
ref_87425 = ref_71273 # MOV operation
ref_89006 = ref_79869 # MOV operation
ref_89115 = ref_89006 # MOV operation
ref_89127 = ref_87425 # MOV operation
ref_89129 = (ref_89127 | ref_89115) # OR operation
ref_89411 = ref_89129 # MOV operation
ref_89417 = (0x3F & ref_89411) # AND operation
ref_89726 = ref_89417 # MOV operation
ref_89734 = ((ref_89726 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_89741 = ref_89734 # MOV operation
ref_91035 = ref_71273 # MOV operation
ref_91144 = ref_91035 # MOV operation
ref_91156 = ref_89741 # MOV operation
ref_91158 = (ref_91156 | ref_91144) # OR operation
ref_91282 = ref_91158 # MOV operation
ref_93909 = ref_77293 # MOV operation
ref_95341 = ref_91282 # MOV operation
ref_95580 = ref_95341 # MOV operation
ref_95588 = (ref_95580 >> (0x1 & 0x3F)) # SHR operation
ref_95595 = ref_95588 # MOV operation
ref_95872 = ref_95595 # MOV operation
ref_95878 = (0xF & ref_95872) # AND operation
ref_96012 = ref_95878 # MOV operation
ref_96026 = (0x1 | ref_96012) # OR operation
ref_96330 = ref_96026 # MOV operation
ref_96332 = ((0x40 - ref_96330) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_96340 = ref_96332 # MOV operation
ref_96486 = ref_93909 # MOV operation
ref_96490 = ref_96340 # MOV operation
ref_96492 = (ref_96490 & 0xFFFFFFFF) # MOV operation
ref_96494 = ((ref_96486 << ((ref_96492 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_96501 = ref_96494 # MOV operation
ref_97665 = ref_77293 # MOV operation
ref_99097 = ref_91282 # MOV operation
ref_99336 = ref_99097 # MOV operation
ref_99344 = (ref_99336 >> (0x1 & 0x3F)) # SHR operation
ref_99351 = ref_99344 # MOV operation
ref_99628 = ref_99351 # MOV operation
ref_99634 = (0xF & ref_99628) # AND operation
ref_99768 = ref_99634 # MOV operation
ref_99782 = (0x1 | ref_99768) # OR operation
ref_99888 = ref_97665 # MOV operation
ref_99892 = ref_99782 # MOV operation
ref_99894 = (ref_99892 & 0xFFFFFFFF) # MOV operation
ref_99896 = (ref_99888 >> ((ref_99894 & 0xFF) & 0x3F)) # SHR operation
ref_99903 = ref_99896 # MOV operation
ref_100032 = ref_99903 # MOV operation
ref_100044 = ref_96501 # MOV operation
ref_100046 = (ref_100044 | ref_100032) # OR operation
ref_100170 = ref_100046 # MOV operation
ref_102360 = ref_83738 # MOV operation
ref_103941 = ref_100170 # MOV operation
ref_104050 = ref_103941 # MOV operation
ref_104062 = ref_102360 # MOV operation
ref_104064 = ((ref_104050 - ref_104062) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_104072 = ref_104064 # MOV operation
ref_104191 = ref_104072 # MOV operation
ref_108161 = ref_91282 # MOV operation
ref_109463 = ref_77293 # MOV operation
ref_109720 = ref_109463 # MOV operation
ref_109726 = (0xF & ref_109720) # AND operation
ref_109860 = ref_109726 # MOV operation
ref_109874 = (0x1 | ref_109860) # OR operation
ref_110178 = ref_109874 # MOV operation
ref_110180 = ((0x40 - ref_110178) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_110188 = ref_110180 # MOV operation
ref_110334 = ref_108161 # MOV operation
ref_110338 = ref_110188 # MOV operation
ref_110340 = (ref_110338 & 0xFFFFFFFF) # MOV operation
ref_110342 = ((ref_110334 << ((ref_110340 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_110349 = ref_110342 # MOV operation
ref_111513 = ref_91282 # MOV operation
ref_112815 = ref_77293 # MOV operation
ref_113072 = ref_112815 # MOV operation
ref_113078 = (0xF & ref_113072) # AND operation
ref_113212 = ref_113078 # MOV operation
ref_113226 = (0x1 | ref_113212) # OR operation
ref_113332 = ref_111513 # MOV operation
ref_113336 = ref_113226 # MOV operation
ref_113338 = (ref_113336 & 0xFFFFFFFF) # MOV operation
ref_113340 = (ref_113332 >> ((ref_113338 & 0xFF) & 0x3F)) # SHR operation
ref_113347 = ref_113340 # MOV operation
ref_113476 = ref_113347 # MOV operation
ref_113488 = ref_110349 # MOV operation
ref_113490 = (ref_113488 | ref_113476) # OR operation
ref_114817 = ref_83738 # MOV operation
ref_115961 = ref_104191 # MOV operation
ref_116070 = ref_115961 # MOV operation
ref_116082 = ref_114817 # MOV operation
ref_116084 = (ref_116082 | ref_116070) # OR operation
ref_116348 = ref_116084 # MOV operation
ref_116356 = (ref_116348 >> (0x1 & 0x3F)) # SHR operation
ref_116363 = ref_116356 # MOV operation
ref_116640 = ref_116363 # MOV operation
ref_116646 = (0x7 & ref_116640) # AND operation
ref_116780 = ref_116646 # MOV operation
ref_116794 = (0x1 | ref_116780) # OR operation
ref_116945 = ref_113490 # MOV operation
ref_116949 = ref_116794 # MOV operation
ref_116951 = (ref_116949 & 0xFFFFFFFF) # MOV operation
ref_116953 = ((ref_116945 << ((ref_116951 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_116960 = ref_116953 # MOV operation
ref_117079 = ref_116960 # MOV operation
ref_117311 = ref_117079 # MOV operation
ref_117313 = ref_117311 # MOV operation

print(ref_117313 & 0xffffffffffffffff)
