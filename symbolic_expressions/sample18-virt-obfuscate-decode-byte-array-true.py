#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])

ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_84246 = ref_278 # MOV operation
ref_84322 = ref_84246 # MOV operation
ref_84336 = (ref_84322 >> (0xD & 0x3F)) # SHR operation
ref_85174 = ref_278 # MOV operation
ref_85374 = ref_85174 # MOV operation
ref_85382 = ((ref_85374 << (0x33 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_85389 = ref_85382 # MOV operation
ref_85493 = ref_84336 # MOV operation
ref_85497 = ref_85389 # MOV operation
ref_85499 = (ref_85497 | ref_85493) # OR operation
ref_85600 = ref_85499 # MOV operation
ref_85614 = ((0x2EA4A1C39AF5800 + ref_85600) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_86546 = ref_85614 # MOV operation
ref_87464 = ref_86546 # MOV operation
ref_88277 = ref_278 # MOV operation
ref_88353 = ref_88277 # MOV operation
ref_88365 = ref_87464 # MOV operation
ref_88367 = ((ref_88353 - ref_88365) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_88375 = ref_88367 # MOV operation
ref_89301 = ref_88375 # MOV operation
ref_90134 = ref_278 # MOV operation
ref_90334 = ref_90134 # MOV operation
ref_90342 = ((ref_90334 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_90349 = ref_90342 # MOV operation
ref_91298 = ref_278 # MOV operation
ref_91374 = ref_91298 # MOV operation
ref_91388 = (ref_91374 >> (0x37 & 0x3F)) # SHR operation
ref_91497 = ref_90349 # MOV operation
ref_91501 = ref_91388 # MOV operation
ref_91503 = (ref_91501 | ref_91497) # OR operation
ref_92434 = ref_91503 # MOV operation
ref_93267 = ref_278 # MOV operation
ref_93467 = ref_93267 # MOV operation
ref_93473 = (0x3E908497 | ref_93467) # OR operation
ref_94404 = ref_93473 # MOV operation
ref_95638 = ref_89301 # MOV operation
ref_95714 = ref_95638 # MOV operation
ref_95728 = (ref_95714 >> (0x2 & 0x3F)) # SHR operation
ref_95829 = ref_95728 # MOV operation
ref_95843 = (0xF & ref_95829) # AND operation
ref_96068 = ref_95843 # MOV operation
ref_96074 = (0x1 | ref_96068) # OR operation
ref_96997 = ref_86546 # MOV operation
ref_97073 = ref_96997 # MOV operation
ref_97085 = ref_96074 # MOV operation
ref_97087 = (ref_97073 >> ((ref_97085 & 0xFF) & 0x3F)) # SHR operation
ref_98010 = ref_86546 # MOV operation
ref_99140 = ref_89301 # MOV operation
ref_99216 = ref_99140 # MOV operation
ref_99230 = (ref_99216 >> (0x2 & 0x3F)) # SHR operation
ref_99331 = ref_99230 # MOV operation
ref_99345 = (0xF & ref_99331) # AND operation
ref_99570 = ref_99345 # MOV operation
ref_99576 = (0x1 | ref_99570) # OR operation
ref_99805 = ref_99576 # MOV operation
ref_99807 = ((0x40 - ref_99805) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_99815 = ref_99807 # MOV operation
ref_99919 = ref_98010 # MOV operation
ref_99923 = ref_99815 # MOV operation
ref_99925 = (ref_99923 & 0xFFFFFFFF) # MOV operation
ref_99927 = ((ref_99919 << ((ref_99925 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_99934 = ref_99927 # MOV operation
ref_100038 = ref_97087 # MOV operation
ref_100042 = ref_99934 # MOV operation
ref_100044 = (ref_100042 | ref_100038) # OR operation
ref_100967 = ref_94404 # MOV operation
ref_101865 = ref_92434 # MOV operation
ref_101941 = ref_101865 # MOV operation
ref_101953 = ref_100967 # MOV operation
ref_101955 = ((ref_101941 - ref_101953) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_101963 = ref_101955 # MOV operation
ref_102067 = ref_100044 # MOV operation
ref_102071 = ref_101963 # MOV operation
ref_102073 = ((ref_102067 - ref_102071) & 0xFFFFFFFFFFFFFFFF) # CMP operation
ref_102075 = ((((ref_102067 ^ (ref_102071 ^ ref_102073)) ^ ((ref_102067 ^ ref_102073) & (ref_102067 ^ ref_102071))) >> 63) & 0x1) # Carry flag
ref_102081 = ((((ref_102071 >> 8) & 0xFFFFFFFFFFFFFF)) << 8 | (0x1 if (ref_102075 == 0x1) else 0x0)) # SETB operation
ref_102083 = (ref_102081 & 0xFF) # MOVZX operation
ref_102171 = (ref_102083 & 0xFFFFFFFF) # MOV operation
ref_102173 = ((ref_102171 & 0xFFFFFFFF) & (ref_102171 & 0xFFFFFFFF)) # TEST operation
ref_102178 = (0x1 if (ref_102173 == 0x0) else 0x0) # Zero flag
ref_102180 = (0x15FA if (ref_102178 == 0x1) else 0x15DC) # Program Counter


if (ref_102178 == 0x1):
    ref_129350 = SymVar_0
    ref_129365 = ref_129350 # MOV operation
    ref_213338 = ref_129365 # MOV operation
    ref_213414 = ref_213338 # MOV operation
    ref_213428 = (ref_213414 >> (0xD & 0x3F)) # SHR operation
    ref_214266 = ref_129365 # MOV operation
    ref_214466 = ref_214266 # MOV operation
    ref_214474 = ((ref_214466 << (0x33 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_214481 = ref_214474 # MOV operation
    ref_214585 = ref_213428 # MOV operation
    ref_214589 = ref_214481 # MOV operation
    ref_214591 = (ref_214589 | ref_214585) # OR operation
    ref_214692 = ref_214591 # MOV operation
    ref_214706 = ((0x2EA4A1C39AF5800 + ref_214692) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_215638 = ref_214706 # MOV operation
    ref_216556 = ref_215638 # MOV operation
    ref_217369 = ref_129365 # MOV operation
    ref_217445 = ref_217369 # MOV operation
    ref_217457 = ref_216556 # MOV operation
    ref_217459 = ((ref_217445 - ref_217457) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_217467 = ref_217459 # MOV operation
    ref_218393 = ref_217467 # MOV operation
    ref_219226 = ref_129365 # MOV operation
    ref_219426 = ref_219226 # MOV operation
    ref_219434 = ((ref_219426 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_219441 = ref_219434 # MOV operation
    ref_220390 = ref_129365 # MOV operation
    ref_220466 = ref_220390 # MOV operation
    ref_220480 = (ref_220466 >> (0x37 & 0x3F)) # SHR operation
    ref_220589 = ref_219441 # MOV operation
    ref_220593 = ref_220480 # MOV operation
    ref_220595 = (ref_220593 | ref_220589) # OR operation
    ref_221526 = ref_220595 # MOV operation
    ref_222359 = ref_129365 # MOV operation
    ref_222559 = ref_222359 # MOV operation
    ref_222565 = (0x3E908497 | ref_222559) # OR operation
    ref_223496 = ref_222565 # MOV operation
    ref_232515 = ref_221526 # MOV operation
    ref_233413 = ref_223496 # MOV operation
    ref_233497 = ref_232515 # MOV operation
    ref_233501 = ref_233413 # MOV operation
    ref_233503 = (ref_233501 | ref_233497) # OR operation
    ref_233604 = ref_233503 # MOV operation
    ref_233618 = (ref_233604 >> (0x4 & 0x3F)) # SHR operation
    ref_233719 = ref_233618 # MOV operation
    ref_233733 = (0x7 & ref_233719) # AND operation
    ref_233958 = ref_233733 # MOV operation
    ref_233964 = (0x1 | ref_233958) # OR operation
    ref_234887 = ref_215638 # MOV operation
    ref_236017 = ref_218393 # MOV operation
    ref_236093 = ref_236017 # MOV operation
    ref_236107 = (ref_236093 >> (0x4 & 0x3F)) # SHR operation
    ref_236208 = ref_236107 # MOV operation
    ref_236222 = (0xF & ref_236208) # AND operation
    ref_236447 = ref_236222 # MOV operation
    ref_236453 = (0x1 | ref_236447) # OR operation
    ref_236562 = ref_234887 # MOV operation
    ref_236566 = ref_236453 # MOV operation
    ref_236568 = (ref_236566 & 0xFFFFFFFF) # MOV operation
    ref_236570 = ((ref_236562 << ((ref_236568 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_236577 = ref_236570 # MOV operation
    ref_237727 = ref_218393 # MOV operation
    ref_237803 = ref_237727 # MOV operation
    ref_237817 = (ref_237803 >> (0x4 & 0x3F)) # SHR operation
    ref_237918 = ref_237817 # MOV operation
    ref_237932 = (0xF & ref_237918) # AND operation
    ref_238157 = ref_237932 # MOV operation
    ref_238163 = (0x1 | ref_238157) # OR operation
    ref_238392 = ref_238163 # MOV operation
    ref_238394 = ((0x40 - ref_238392) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_238402 = ref_238394 # MOV operation
    ref_239320 = ref_215638 # MOV operation
    ref_239396 = ref_239320 # MOV operation
    ref_239408 = ref_238402 # MOV operation
    ref_239410 = (ref_239396 >> ((ref_239408 & 0xFF) & 0x3F)) # SHR operation
    ref_239519 = ref_236577 # MOV operation
    ref_239523 = ref_239410 # MOV operation
    ref_239525 = (ref_239523 | ref_239519) # OR operation
    ref_239626 = ref_239525 # MOV operation
    ref_239638 = ref_233964 # MOV operation
    ref_239640 = (ref_239626 >> ((ref_239638 & 0xFF) & 0x3F)) # SHR operation
    ref_240495 = ref_239640 # MOV operation
    ref_240706 = ref_240495 # MOV operation
    ref_240708 = ref_240706 # MOV operation
    endb = ref_240708


else:
    ref_263 = SymVar_0
    ref_278 = ref_263 # MOV operation
    ref_84246 = ref_278 # MOV operation
    ref_84322 = ref_84246 # MOV operation
    ref_84336 = (ref_84322 >> (0xD & 0x3F)) # SHR operation
    ref_85174 = ref_278 # MOV operation
    ref_85374 = ref_85174 # MOV operation
    ref_85382 = ((ref_85374 << (0x33 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_85389 = ref_85382 # MOV operation
    ref_85493 = ref_84336 # MOV operation
    ref_85497 = ref_85389 # MOV operation
    ref_85499 = (ref_85497 | ref_85493) # OR operation
    ref_85600 = ref_85499 # MOV operation
    ref_85614 = ((0x2EA4A1C39AF5800 + ref_85600) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_86546 = ref_85614 # MOV operation
    ref_87464 = ref_86546 # MOV operation
    ref_88277 = ref_278 # MOV operation
    ref_88353 = ref_88277 # MOV operation
    ref_88365 = ref_87464 # MOV operation
    ref_88367 = ((ref_88353 - ref_88365) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_88375 = ref_88367 # MOV operation
    ref_89301 = ref_88375 # MOV operation
    ref_89303 = ((ref_89301 >> 56) & 0xFF) # Byte reference - MOV operation
    ref_89304 = ((ref_89301 >> 48) & 0xFF) # Byte reference - MOV operation
    ref_89305 = ((ref_89301 >> 40) & 0xFF) # Byte reference - MOV operation
    ref_89306 = ((ref_89301 >> 32) & 0xFF) # Byte reference - MOV operation
    ref_89307 = ((ref_89301 >> 24) & 0xFF) # Byte reference - MOV operation
    ref_89308 = ((ref_89301 >> 16) & 0xFF) # Byte reference - MOV operation
    ref_89309 = ((ref_89301 >> 8) & 0xFF) # Byte reference - MOV operation
    ref_89310 = (ref_89301 & 0xFF) # Byte reference - MOV operation
    ref_90134 = ref_278 # MOV operation
    ref_90334 = ref_90134 # MOV operation
    ref_90342 = ((ref_90334 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_90349 = ref_90342 # MOV operation
    ref_91298 = ref_278 # MOV operation
    ref_91374 = ref_91298 # MOV operation
    ref_91388 = (ref_91374 >> (0x37 & 0x3F)) # SHR operation
    ref_91497 = ref_90349 # MOV operation
    ref_91501 = ref_91388 # MOV operation
    ref_91503 = (ref_91501 | ref_91497) # OR operation
    ref_92434 = ref_91503 # MOV operation
    ref_93267 = ref_278 # MOV operation
    ref_93467 = ref_93267 # MOV operation
    ref_93473 = (0x3E908497 | ref_93467) # OR operation
    ref_94404 = ref_93473 # MOV operation
    ref_103848 = ((((ref_89303) << 8 | ref_89304) << 8 | ref_89305) << 8 | ref_89306) # MOV operation
    ref_103928 = (ref_103848 & 0xFFFFFFFF) # MOV operation
    ref_106876 = ((((ref_89307) << 8 | ref_89308) << 8 | ref_89309) << 8 | ref_89310) # MOV operation
    ref_106956 = (ref_106876 & 0xFFFFFFFF) # MOV operation
    ref_106958 = (((ref_106956 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
    ref_106959 = (((ref_106956 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
    ref_106960 = (((ref_106956 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
    ref_106961 = ((ref_106956 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
    ref_108604 = (ref_103928 & 0xFFFFFFFF) # MOV operation
    ref_108684 = (ref_108604 & 0xFFFFFFFF) # MOV operation
    ref_108686 = (((ref_108684 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
    ref_108687 = (((ref_108684 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
    ref_108688 = (((ref_108684 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
    ref_108689 = ((ref_108684 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
    ref_109598 = ref_86546 # MOV operation
    ref_110612 = ref_86546 # MOV operation
    ref_110688 = ref_110612 # MOV operation
    ref_110702 = (0x3F & ref_110688) # AND operation
    ref_110927 = ref_110702 # MOV operation
    ref_110935 = ((ref_110927 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_110942 = ref_110935 # MOV operation
    ref_111046 = ref_109598 # MOV operation
    ref_111050 = ref_110942 # MOV operation
    ref_111052 = (ref_111050 | ref_111046) # OR operation
    ref_111983 = ref_111052 # MOV operation
    ref_112901 = ref_94404 # MOV operation
    ref_113915 = ref_111983 # MOV operation
    ref_113991 = ref_113915 # MOV operation
    ref_114005 = (0x1F & ref_113991) # AND operation
    ref_114230 = ref_114005 # MOV operation
    ref_114238 = ((ref_114230 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_114245 = ref_114238 # MOV operation
    ref_114349 = ref_112901 # MOV operation
    ref_114353 = ref_114245 # MOV operation
    ref_114355 = (ref_114353 | ref_114349) # OR operation
    ref_115286 = ref_114355 # MOV operation
    ref_116204 = ref_111983 # MOV operation
    ref_117218 = ref_92434 # MOV operation
    ref_118116 = ref_111983 # MOV operation
    ref_118192 = ref_118116 # MOV operation
    ref_118204 = ref_117218 # MOV operation
    ref_118206 = ((ref_118204 + ref_118192) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_118308 = ref_118206 # MOV operation
    ref_118322 = (0x1F & ref_118308) # AND operation
    ref_118547 = ref_118322 # MOV operation
    ref_118555 = ((ref_118547 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_118562 = ref_118555 # MOV operation
    ref_118666 = ref_116204 # MOV operation
    ref_118670 = ref_118562 # MOV operation
    ref_118672 = (ref_118670 | ref_118666) # OR operation
    ref_119603 = ref_118672 # MOV operation
    ref_120837 = ref_92434 # MOV operation
    ref_121735 = ref_115286 # MOV operation
    ref_121819 = ref_120837 # MOV operation
    ref_121823 = ref_121735 # MOV operation
    ref_121825 = (ref_121823 | ref_121819) # OR operation
    ref_121926 = ref_121825 # MOV operation
    ref_121940 = (ref_121926 >> (0x4 & 0x3F)) # SHR operation
    ref_122041 = ref_121940 # MOV operation
    ref_122055 = (0x7 & ref_122041) # AND operation
    ref_122280 = ref_122055 # MOV operation
    ref_122286 = (0x1 | ref_122280) # OR operation
    ref_123209 = ref_119603 # MOV operation
    ref_124339 = ((((((((ref_106958) << 8 | ref_106959) << 8 | ref_106960) << 8 | ref_106961) << 8 | ref_108686) << 8 | ref_108687) << 8 | ref_108688) << 8 | ref_108689) # MOV operation
    ref_124415 = ref_124339 # MOV operation
    ref_124429 = (ref_124415 >> (0x4 & 0x3F)) # SHR operation
    ref_124530 = ref_124429 # MOV operation
    ref_124544 = (0xF & ref_124530) # AND operation
    ref_124769 = ref_124544 # MOV operation
    ref_124775 = (0x1 | ref_124769) # OR operation
    ref_124884 = ref_123209 # MOV operation
    ref_124888 = ref_124775 # MOV operation
    ref_124890 = (ref_124888 & 0xFFFFFFFF) # MOV operation
    ref_124892 = ((ref_124884 << ((ref_124890 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_124899 = ref_124892 # MOV operation
    ref_126049 = ((((((((ref_106958) << 8 | ref_106959) << 8 | ref_106960) << 8 | ref_106961) << 8 | ref_108686) << 8 | ref_108687) << 8 | ref_108688) << 8 | ref_108689) # MOV operation
    ref_126125 = ref_126049 # MOV operation
    ref_126139 = (ref_126125 >> (0x4 & 0x3F)) # SHR operation
    ref_126240 = ref_126139 # MOV operation
    ref_126254 = (0xF & ref_126240) # AND operation
    ref_126479 = ref_126254 # MOV operation
    ref_126485 = (0x1 | ref_126479) # OR operation
    ref_126714 = ref_126485 # MOV operation
    ref_126716 = ((0x40 - ref_126714) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_126724 = ref_126716 # MOV operation
    ref_127642 = ref_119603 # MOV operation
    ref_127718 = ref_127642 # MOV operation
    ref_127730 = ref_126724 # MOV operation
    ref_127732 = (ref_127718 >> ((ref_127730 & 0xFF) & 0x3F)) # SHR operation
    ref_127841 = ref_124899 # MOV operation
    ref_127845 = ref_127732 # MOV operation
    ref_127847 = (ref_127845 | ref_127841) # OR operation
    ref_127948 = ref_127847 # MOV operation
    ref_127960 = ref_122286 # MOV operation
    ref_127962 = (ref_127948 >> ((ref_127960 & 0xFF) & 0x3F)) # SHR operation
    ref_128817 = ref_127962 # MOV operation
    ref_129028 = ref_128817 # MOV operation
    ref_129030 = ref_129028 # MOV operation
    endb = ref_129030


print(endb & 0xffffffffffffffff)
