#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])

ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_16134 = ref_278 # MOV operation
ref_16270 = ref_16134 # MOV operation
ref_16276 = (0x1D2C27F0 | ref_16270) # OR operation
ref_16345 = ref_16276 # MOV operation
ref_16359 = ((ref_16345 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_16941 = ref_278 # MOV operation
ref_17077 = ref_16941 # MOV operation
ref_17083 = (0x1D2C27F0 | ref_17077) # OR operation
ref_17244 = ref_17083 # MOV operation
ref_17252 = (ref_17244 >> (0x37 & 0x3F)) # SHR operation
ref_17259 = ref_17252 # MOV operation
ref_17331 = ref_16359 # MOV operation
ref_17335 = ref_17259 # MOV operation
ref_17337 = (ref_17335 | ref_17331) # OR operation
ref_17414 = ref_17337 # MOV operation
ref_18589 = ref_278 # MOV operation
ref_19315 = ref_17414 # MOV operation
ref_19359 = ref_19315 # MOV operation
ref_19373 = ((ref_19359 << (0xD & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_20040 = ref_17414 # MOV operation
ref_20176 = ref_20040 # MOV operation
ref_20184 = (ref_20176 >> (0x33 & 0x3F)) # SHR operation
ref_20191 = ref_20184 # MOV operation
ref_20263 = ref_19373 # MOV operation
ref_20267 = ref_20191 # MOV operation
ref_20269 = (ref_20267 | ref_20263) # OR operation
ref_20346 = ref_18589 # MOV operation
ref_20350 = ref_20269 # MOV operation
ref_20352 = (ref_20350 | ref_20346) # OR operation
ref_20429 = ref_20352 # MOV operation
ref_21688 = ref_278 # MOV operation
ref_21732 = ref_21688 # MOV operation
ref_21746 = ((0x6402BE2 + ref_21732) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_21824 = ref_21746 # MOV operation
ref_22999 = ref_278 # MOV operation
ref_23135 = ref_22999 # MOV operation
ref_23141 = (0x3544223F | ref_23135) # OR operation
ref_23892 = ref_21824 # MOV operation
ref_24534 = ref_20429 # MOV operation
ref_24586 = ref_23892 # MOV operation
ref_24590 = ref_24534 # MOV operation
ref_24592 = (((sx(0x40, ref_24590) * sx(0x40, ref_24586)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_24670 = ref_24592 # MOV operation
ref_24672 = (((sx(0x40, ref_24670) * sx(0x40, 0x3BE31211)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_24746 = ref_23141 # MOV operation
ref_24750 = ref_24672 # MOV operation
ref_24752 = (((sx(0x40, ref_24750) * sx(0x40, ref_24746)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_24826 = ref_24752 # MOV operation
ref_26086 = ref_21824 # MOV operation
ref_26896 = ref_24826 # MOV operation
ref_26940 = ref_26896 # MOV operation
ref_26954 = (0x1F & ref_26940) # AND operation
ref_27023 = ref_26954 # MOV operation
ref_27037 = ((ref_27023 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_27114 = ref_26086 # MOV operation
ref_27118 = ref_27037 # MOV operation
ref_27120 = (ref_27118 | ref_27114) # OR operation
ref_27197 = ref_27120 # MOV operation
ref_28002 = ref_20429 # MOV operation
ref_28138 = ref_28002 # MOV operation
ref_28146 = (ref_28138 >> (0x1 & 0x3F)) # SHR operation
ref_28153 = ref_28146 # MOV operation
ref_28217 = ref_28153 # MOV operation
ref_28231 = (0xF & ref_28217) # AND operation
ref_28392 = ref_28231 # MOV operation
ref_28398 = (0x1 | ref_28392) # OR operation
ref_29065 = ref_17414 # MOV operation
ref_29109 = ref_29065 # MOV operation
ref_29121 = ref_28398 # MOV operation
ref_29123 = ((ref_29109 << ((ref_29121 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_29790 = ref_17414 # MOV operation
ref_30516 = ref_20429 # MOV operation
ref_30652 = ref_30516 # MOV operation
ref_30660 = (ref_30652 >> (0x1 & 0x3F)) # SHR operation
ref_30667 = ref_30660 # MOV operation
ref_30731 = ref_30667 # MOV operation
ref_30745 = (0xF & ref_30731) # AND operation
ref_30906 = ref_30745 # MOV operation
ref_30912 = (0x1 | ref_30906) # OR operation
ref_31077 = ref_30912 # MOV operation
ref_31079 = ((0x40 - ref_31077) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_31087 = ref_31079 # MOV operation
ref_31159 = ref_29790 # MOV operation
ref_31163 = ref_31087 # MOV operation
ref_31165 = (ref_31163 & 0xFFFFFFFF) # MOV operation
ref_31167 = (ref_31159 >> ((ref_31165 & 0xFF) & 0x3F)) # SHR operation
ref_31174 = ref_31167 # MOV operation
ref_31246 = ref_29123 # MOV operation
ref_31250 = ref_31174 # MOV operation
ref_31252 = (ref_31250 | ref_31246) # OR operation
ref_31919 = ref_27197 # MOV operation
ref_32645 = ref_24826 # MOV operation
ref_32781 = ref_32645 # MOV operation
ref_32789 = (ref_32781 >> (0x3 & 0x3F)) # SHR operation
ref_32796 = ref_32789 # MOV operation
ref_32860 = ref_32796 # MOV operation
ref_32874 = (0x7 & ref_32860) # AND operation
ref_33035 = ref_32874 # MOV operation
ref_33041 = (0x1 | ref_33035) # OR operation
ref_33118 = ref_31919 # MOV operation
ref_33122 = ref_33041 # MOV operation
ref_33124 = (ref_33122 & 0xFFFFFFFF) # MOV operation
ref_33126 = (ref_33118 >> ((ref_33124 & 0xFF) & 0x3F)) # SHR operation
ref_33133 = ref_33126 # MOV operation
ref_33205 = ref_31252 # MOV operation
ref_33209 = ref_33133 # MOV operation
ref_33211 = ((ref_33205 - ref_33209) & 0xFFFFFFFFFFFFFFFF) # CMP operation
ref_33213 = ((((ref_33205 ^ (ref_33209 ^ ref_33211)) ^ ((ref_33205 ^ ref_33211) & (ref_33205 ^ ref_33209))) >> 63) & 0x1) # Carry flag
ref_33217 = (0x1 if (ref_33211 == 0x0) else 0x0) # Zero flag
ref_33219 = ((((ref_33209 >> 8) & 0xFFFFFFFFFFFFFF)) << 8 | (0x1 if ((ref_33213 | ref_33217) == 0x1) else 0x0)) # SETBE operation
ref_33221 = (ref_33219 & 0xFF) # MOVZX operation
ref_33277 = (ref_33221 & 0xFFFFFFFF) # MOV operation
ref_33279 = ((ref_33277 & 0xFFFFFFFF) & (ref_33277 & 0xFFFFFFFF)) # TEST operation
ref_33284 = (0x1 if (ref_33279 == 0x0) else 0x0) # Zero flag
ref_33286 = (0x48A1 if (ref_33284 == 0x0) else 0x489D) # Program Counter


if (ref_33284 == 0x0):
    ref_42468 = SymVar_0
    ref_42483 = ref_42468 # MOV operation
    ref_58344 = ref_42483 # MOV operation
    ref_58480 = ref_58344 # MOV operation
    ref_58486 = (0x1D2C27F0 | ref_58480) # OR operation
    ref_58555 = ref_58486 # MOV operation
    ref_58569 = ((ref_58555 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_59151 = ref_42483 # MOV operation
    ref_59287 = ref_59151 # MOV operation
    ref_59293 = (0x1D2C27F0 | ref_59287) # OR operation
    ref_59454 = ref_59293 # MOV operation
    ref_59462 = (ref_59454 >> (0x37 & 0x3F)) # SHR operation
    ref_59469 = ref_59462 # MOV operation
    ref_59541 = ref_58569 # MOV operation
    ref_59545 = ref_59469 # MOV operation
    ref_59547 = (ref_59545 | ref_59541) # OR operation
    ref_59624 = ref_59547 # MOV operation
    ref_60799 = ref_42483 # MOV operation
    ref_61525 = ref_59624 # MOV operation
    ref_61569 = ref_61525 # MOV operation
    ref_61583 = ((ref_61569 << (0xD & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_62250 = ref_59624 # MOV operation
    ref_62386 = ref_62250 # MOV operation
    ref_62394 = (ref_62386 >> (0x33 & 0x3F)) # SHR operation
    ref_62401 = ref_62394 # MOV operation
    ref_62473 = ref_61583 # MOV operation
    ref_62477 = ref_62401 # MOV operation
    ref_62479 = (ref_62477 | ref_62473) # OR operation
    ref_62556 = ref_60799 # MOV operation
    ref_62560 = ref_62479 # MOV operation
    ref_62562 = (ref_62560 | ref_62556) # OR operation
    ref_62639 = ref_62562 # MOV operation
    ref_62641 = ((ref_62639 >> 56) & 0xFF) # Byte reference - MOV operation
    ref_62642 = ((ref_62639 >> 48) & 0xFF) # Byte reference - MOV operation
    ref_62643 = ((ref_62639 >> 40) & 0xFF) # Byte reference - MOV operation
    ref_62644 = ((ref_62639 >> 32) & 0xFF) # Byte reference - MOV operation
    ref_62645 = ((ref_62639 >> 24) & 0xFF) # Byte reference - MOV operation
    ref_62646 = ((ref_62639 >> 16) & 0xFF) # Byte reference - MOV operation
    ref_62647 = ((ref_62639 >> 8) & 0xFF) # Byte reference - MOV operation
    ref_62648 = (ref_62639 & 0xFF) # Byte reference - MOV operation
    ref_63898 = ref_42483 # MOV operation
    ref_63942 = ref_63898 # MOV operation
    ref_63956 = ((0x6402BE2 + ref_63942) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_64034 = ref_63956 # MOV operation
    ref_65209 = ref_42483 # MOV operation
    ref_65345 = ref_65209 # MOV operation
    ref_65351 = (0x3544223F | ref_65345) # OR operation
    ref_66102 = ref_64034 # MOV operation
    ref_66744 = ref_62639 # MOV operation
    ref_66796 = ref_66102 # MOV operation
    ref_66800 = ref_66744 # MOV operation
    ref_66802 = (((sx(0x40, ref_66800) * sx(0x40, ref_66796)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_66880 = ref_66802 # MOV operation
    ref_66882 = (((sx(0x40, ref_66880) * sx(0x40, 0x3BE31211)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_66956 = ref_65351 # MOV operation
    ref_66960 = ref_66882 # MOV operation
    ref_66962 = (((sx(0x40, ref_66960) * sx(0x40, ref_66956)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_67036 = ref_66962 # MOV operation
    ref_68296 = ref_64034 # MOV operation
    ref_69106 = ref_67036 # MOV operation
    ref_69150 = ref_69106 # MOV operation
    ref_69164 = (0x1F & ref_69150) # AND operation
    ref_69233 = ref_69164 # MOV operation
    ref_69247 = ((ref_69233 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_69324 = ref_68296 # MOV operation
    ref_69328 = ref_69247 # MOV operation
    ref_69330 = (ref_69328 | ref_69324) # OR operation
    ref_69407 = ref_69330 # MOV operation
    ref_76863 = ref_67036 # MOV operation
    ref_76907 = ref_76863 # MOV operation
    ref_76923 = ((((0x0) << 64 | ref_76907) / 0x8) & 0xFFFFFFFFFFFFFFFF) # DIV operation
    ref_76996 = ref_76923 # MOV operation
    ref_76998 = ((ref_76996 >> 56) & 0xFF) # Byte reference - MOV operation
    ref_76999 = ((ref_76996 >> 48) & 0xFF) # Byte reference - MOV operation
    ref_77000 = ((ref_76996 >> 40) & 0xFF) # Byte reference - MOV operation
    ref_77001 = ((ref_76996 >> 32) & 0xFF) # Byte reference - MOV operation
    ref_77002 = ((ref_76996 >> 24) & 0xFF) # Byte reference - MOV operation
    ref_77003 = ((ref_76996 >> 16) & 0xFF) # Byte reference - MOV operation
    ref_77004 = ((ref_76996 >> 8) & 0xFF) # Byte reference - MOV operation
    ref_77005 = (ref_76996 & 0xFF) # Byte reference - MOV operation
    ref_78072 = ref_62646 # MOVZX operation
    ref_78212 = (ref_78072 & 0xFF) # MOVZX operation
    ref_79280 = ref_62643 # MOVZX operation
    ref_80336 = (ref_79280 & 0xFF) # MOVZX operation
    ref_80338 = (ref_80336 & 0xFF) # Byte reference - MOV operation
    ref_80488 = (ref_78212 & 0xFF) # MOVZX operation
    ref_81544 = (ref_80488 & 0xFF) # MOVZX operation
    ref_81546 = (ref_81544 & 0xFF) # Byte reference - MOV operation
    ref_82612 = ref_62641 # MOVZX operation
    ref_82752 = (ref_82612 & 0xFF) # MOVZX operation
    ref_83820 = ref_62648 # MOVZX operation
    ref_84876 = (ref_83820 & 0xFF) # MOVZX operation
    ref_84878 = (ref_84876 & 0xFF) # Byte reference - MOV operation
    ref_85028 = (ref_82752 & 0xFF) # MOVZX operation
    ref_86084 = (ref_85028 & 0xFF) # MOVZX operation
    ref_86086 = (ref_86084 & 0xFF) # Byte reference - MOV operation
    ref_87152 = ref_77001 # MOVZX operation
    ref_87292 = (ref_87152 & 0xFF) # MOVZX operation
    ref_88360 = ref_77005 # MOVZX operation
    ref_89416 = (ref_88360 & 0xFF) # MOVZX operation
    ref_89418 = (ref_89416 & 0xFF) # Byte reference - MOV operation
    ref_89568 = (ref_87292 & 0xFF) # MOVZX operation
    ref_90624 = (ref_89568 & 0xFF) # MOVZX operation
    ref_90626 = (ref_90624 & 0xFF) # Byte reference - MOV operation
    ref_91943 = ((((((((ref_84878) << 8 | ref_62642) << 8 | ref_81546) << 8 | ref_62644) << 8 | ref_62645) << 8 | ref_80338) << 8 | ref_62647) << 8 | ref_86086) # MOV operation
    ref_92079 = ref_91943 # MOV operation
    ref_92087 = (ref_92079 >> (0x3 & 0x3F)) # SHR operation
    ref_92094 = ref_92087 # MOV operation
    ref_92158 = ref_92094 # MOV operation
    ref_92172 = (0xF & ref_92158) # AND operation
    ref_92333 = ref_92172 # MOV operation
    ref_92339 = (0x1 | ref_92333) # OR operation
    ref_93006 = ((((((((ref_76998) << 8 | ref_76999) << 8 | ref_77000) << 8 | ref_89418) << 8 | ref_77002) << 8 | ref_77003) << 8 | ref_77004) << 8 | ref_90626) # MOV operation
    ref_93050 = ref_93006 # MOV operation
    ref_93062 = ref_92339 # MOV operation
    ref_93064 = ((ref_93050 << ((ref_93062 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_93731 = ((((((((ref_76998) << 8 | ref_76999) << 8 | ref_77000) << 8 | ref_89418) << 8 | ref_77002) << 8 | ref_77003) << 8 | ref_77004) << 8 | ref_90626) # MOV operation
    ref_94457 = ((((((((ref_84878) << 8 | ref_62642) << 8 | ref_81546) << 8 | ref_62644) << 8 | ref_62645) << 8 | ref_80338) << 8 | ref_62647) << 8 | ref_86086) # MOV operation
    ref_94593 = ref_94457 # MOV operation
    ref_94601 = (ref_94593 >> (0x3 & 0x3F)) # SHR operation
    ref_94608 = ref_94601 # MOV operation
    ref_94672 = ref_94608 # MOV operation
    ref_94686 = (0xF & ref_94672) # AND operation
    ref_94847 = ref_94686 # MOV operation
    ref_94853 = (0x1 | ref_94847) # OR operation
    ref_95018 = ref_94853 # MOV operation
    ref_95020 = ((0x40 - ref_95018) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_95028 = ref_95020 # MOV operation
    ref_95100 = ref_93731 # MOV operation
    ref_95104 = ref_95028 # MOV operation
    ref_95106 = (ref_95104 & 0xFFFFFFFF) # MOV operation
    ref_95108 = (ref_95100 >> ((ref_95106 & 0xFF) & 0x3F)) # SHR operation
    ref_95115 = ref_95108 # MOV operation
    ref_95187 = ref_93064 # MOV operation
    ref_95191 = ref_95115 # MOV operation
    ref_95193 = (ref_95191 | ref_95187) # OR operation
    ref_95860 = ref_69407 # MOV operation
    ref_96586 = ref_67036 # MOV operation
    ref_96630 = ref_96586 # MOV operation
    ref_96644 = ((0x369A4780 + ref_96630) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_96722 = ref_95860 # MOV operation
    ref_96726 = ref_96644 # MOV operation
    ref_96728 = (((sx(0x40, ref_96726) * sx(0x40, ref_96722)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_96802 = ref_95193 # MOV operation
    ref_96806 = ref_96728 # MOV operation
    ref_96808 = (((sx(0x40, ref_96806) * sx(0x40, ref_96802)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_96882 = ref_96808 # MOV operation
    ref_97036 = ref_96882 # MOV operation
    ref_97038 = ref_97036 # MOV operation
    endb = ref_97038


else:
    ref_263 = SymVar_0
    ref_278 = ref_263 # MOV operation
    ref_16134 = ref_278 # MOV operation
    ref_16270 = ref_16134 # MOV operation
    ref_16276 = (0x1D2C27F0 | ref_16270) # OR operation
    ref_16345 = ref_16276 # MOV operation
    ref_16359 = ((ref_16345 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_16941 = ref_278 # MOV operation
    ref_17077 = ref_16941 # MOV operation
    ref_17083 = (0x1D2C27F0 | ref_17077) # OR operation
    ref_17244 = ref_17083 # MOV operation
    ref_17252 = (ref_17244 >> (0x37 & 0x3F)) # SHR operation
    ref_17259 = ref_17252 # MOV operation
    ref_17331 = ref_16359 # MOV operation
    ref_17335 = ref_17259 # MOV operation
    ref_17337 = (ref_17335 | ref_17331) # OR operation
    ref_17414 = ref_17337 # MOV operation
    ref_18589 = ref_278 # MOV operation
    ref_19315 = ref_17414 # MOV operation
    ref_19359 = ref_19315 # MOV operation
    ref_19373 = ((ref_19359 << (0xD & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_20040 = ref_17414 # MOV operation
    ref_20176 = ref_20040 # MOV operation
    ref_20184 = (ref_20176 >> (0x33 & 0x3F)) # SHR operation
    ref_20191 = ref_20184 # MOV operation
    ref_20263 = ref_19373 # MOV operation
    ref_20267 = ref_20191 # MOV operation
    ref_20269 = (ref_20267 | ref_20263) # OR operation
    ref_20346 = ref_18589 # MOV operation
    ref_20350 = ref_20269 # MOV operation
    ref_20352 = (ref_20350 | ref_20346) # OR operation
    ref_20429 = ref_20352 # MOV operation
    ref_21688 = ref_278 # MOV operation
    ref_21732 = ref_21688 # MOV operation
    ref_21746 = ((0x6402BE2 + ref_21732) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_21824 = ref_21746 # MOV operation
    ref_22999 = ref_278 # MOV operation
    ref_23135 = ref_22999 # MOV operation
    ref_23141 = (0x3544223F | ref_23135) # OR operation
    ref_23892 = ref_21824 # MOV operation
    ref_24534 = ref_20429 # MOV operation
    ref_24586 = ref_23892 # MOV operation
    ref_24590 = ref_24534 # MOV operation
    ref_24592 = (((sx(0x40, ref_24590) * sx(0x40, ref_24586)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_24670 = ref_24592 # MOV operation
    ref_24672 = (((sx(0x40, ref_24670) * sx(0x40, 0x3BE31211)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_24746 = ref_23141 # MOV operation
    ref_24750 = ref_24672 # MOV operation
    ref_24752 = (((sx(0x40, ref_24750) * sx(0x40, ref_24746)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_24826 = ref_24752 # MOV operation
    ref_26086 = ref_21824 # MOV operation
    ref_26896 = ref_24826 # MOV operation
    ref_26940 = ref_26896 # MOV operation
    ref_26954 = (0x1F & ref_26940) # AND operation
    ref_27023 = ref_26954 # MOV operation
    ref_27037 = ((ref_27023 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_27114 = ref_26086 # MOV operation
    ref_27118 = ref_27037 # MOV operation
    ref_27120 = (ref_27118 | ref_27114) # OR operation
    ref_27197 = ref_27120 # MOV operation
    ref_34615 = ref_20429 # MOV operation
    ref_35425 = ref_20429 # MOV operation
    ref_35469 = ref_35425 # MOV operation
    ref_35483 = (0xF & ref_35469) # AND operation
    ref_35552 = ref_35483 # MOV operation
    ref_35566 = ((ref_35552 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_35643 = ref_34615 # MOV operation
    ref_35647 = ref_35566 # MOV operation
    ref_35649 = (ref_35647 | ref_35643) # OR operation
    ref_35726 = ref_35649 # MOV operation
    ref_37053 = ref_35726 # MOV operation
    ref_37189 = ref_37053 # MOV operation
    ref_37197 = (ref_37189 >> (0x3 & 0x3F)) # SHR operation
    ref_37204 = ref_37197 # MOV operation
    ref_37268 = ref_37204 # MOV operation
    ref_37282 = (0xF & ref_37268) # AND operation
    ref_37443 = ref_37282 # MOV operation
    ref_37449 = (0x1 | ref_37443) # OR operation
    ref_38116 = ref_17414 # MOV operation
    ref_38160 = ref_38116 # MOV operation
    ref_38172 = ref_37449 # MOV operation
    ref_38174 = ((ref_38160 << ((ref_38172 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_38841 = ref_17414 # MOV operation
    ref_39567 = ref_35726 # MOV operation
    ref_39703 = ref_39567 # MOV operation
    ref_39711 = (ref_39703 >> (0x3 & 0x3F)) # SHR operation
    ref_39718 = ref_39711 # MOV operation
    ref_39782 = ref_39718 # MOV operation
    ref_39796 = (0xF & ref_39782) # AND operation
    ref_39957 = ref_39796 # MOV operation
    ref_39963 = (0x1 | ref_39957) # OR operation
    ref_40128 = ref_39963 # MOV operation
    ref_40130 = ((0x40 - ref_40128) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_40138 = ref_40130 # MOV operation
    ref_40210 = ref_38841 # MOV operation
    ref_40214 = ref_40138 # MOV operation
    ref_40216 = (ref_40214 & 0xFFFFFFFF) # MOV operation
    ref_40218 = (ref_40210 >> ((ref_40216 & 0xFF) & 0x3F)) # SHR operation
    ref_40225 = ref_40218 # MOV operation
    ref_40297 = ref_38174 # MOV operation
    ref_40301 = ref_40225 # MOV operation
    ref_40303 = (ref_40301 | ref_40297) # OR operation
    ref_40970 = ref_27197 # MOV operation
    ref_41696 = ref_24826 # MOV operation
    ref_41740 = ref_41696 # MOV operation
    ref_41754 = ((0x369A4780 + ref_41740) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_41832 = ref_40970 # MOV operation
    ref_41836 = ref_41754 # MOV operation
    ref_41838 = (((sx(0x40, ref_41836) * sx(0x40, ref_41832)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_41912 = ref_40303 # MOV operation
    ref_41916 = ref_41838 # MOV operation
    ref_41918 = (((sx(0x40, ref_41916) * sx(0x40, ref_41912)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_41992 = ref_41918 # MOV operation
    ref_42146 = ref_41992 # MOV operation
    ref_42148 = ref_42146 # MOV operation
    endb = ref_42148


print(endb & 0xffffffffffffffff)
