#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_6562 = ref_278 # MOV operation
ref_6672 = ref_6562 # MOV operation
ref_6690 = (ref_6672 | 0x1F02C962) # OR operation
ref_6805 = ref_6690 # MOV operation
ref_6823 = (ref_6805 & 0x1F8797B2) # AND operation
ref_6942 = ref_6823 # MOV operation
ref_8676 = ref_6942 # MOV operation
ref_9587 = ref_278 # MOV operation
ref_9697 = ref_9587 # MOV operation
ref_9713 = ref_8676 # MOV operation
ref_9715 = (ref_9697 & ref_9713) # AND operation
ref_9834 = ref_9715 # MOV operation
ref_11568 = ref_9834 # MOV operation
ref_11776 = ref_11568 # MOV operation
ref_11796 = ((ref_11776 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_12725 = ref_9834 # MOV operation
ref_12933 = ref_12725 # MOV operation
ref_12953 = (ref_12933 >> (0x7 & 0x3F)) # SHR operation
ref_13068 = ref_12953 # MOV operation
ref_13084 = ref_11796 # MOV operation
ref_13086 = (ref_13068 | ref_13084) # OR operation
ref_14100 = ref_278 # MOV operation
ref_14210 = ref_14100 # MOV operation
ref_14228 = (((sx(0x40, ref_14210) * sx(0x40, 0x66AF1DF)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_14340 = ref_14228 # MOV operation
ref_14356 = ref_13086 # MOV operation
ref_14358 = ((ref_14340 + ref_14356) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_14478 = ref_14358 # MOV operation
ref_24177 = ref_14478 # MOV operation
ref_25465 = ref_14478 # MOV operation
ref_25575 = ref_25465 # MOV operation
ref_25591 = ref_24177 # MOV operation
ref_25593 = ((ref_25575 + ref_25591) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_25713 = ref_25593 # MOV operation
ref_28041 = ref_9834 # MOV operation
ref_28151 = ref_28041 # MOV operation
ref_28169 = (ref_28151 & 0x7) # AND operation
ref_28382 = ref_28169 # MOV operation
ref_28402 = ((ref_28382 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_29695 = ref_14478 # MOV operation
ref_29805 = ref_29695 # MOV operation
ref_29821 = ref_28402 # MOV operation
ref_29823 = (ref_29805 | ref_29821) # OR operation
ref_29942 = ref_29823 # MOV operation
ref_29944 = ((ref_29942 >> 56) & 0xFF) # Byte reference - MOV operation
ref_29945 = ((ref_29942 >> 48) & 0xFF) # Byte reference - MOV operation
ref_29946 = ((ref_29942 >> 40) & 0xFF) # Byte reference - MOV operation
ref_29947 = ((ref_29942 >> 32) & 0xFF) # Byte reference - MOV operation
ref_29948 = ((ref_29942 >> 24) & 0xFF) # Byte reference - MOV operation
ref_29949 = ((ref_29942 >> 16) & 0xFF) # Byte reference - MOV operation
ref_29950 = ((ref_29942 >> 8) & 0xFF) # Byte reference - MOV operation
ref_29951 = (ref_29942 & 0xFF) # Byte reference - MOV operation
ref_31914 = ref_29944 # MOVZX operation
ref_32138 = (ref_31914 & 0xFF) # MOVZX operation
ref_34102 = ref_29951 # MOVZX operation
ref_36070 = (ref_34102 & 0xFF) # MOVZX operation
ref_36072 = (ref_36070 & 0xFF) # Byte reference - MOV operation
ref_36290 = (ref_32138 & 0xFF) # MOVZX operation
ref_38258 = (ref_36290 & 0xFF) # MOVZX operation
ref_38260 = (ref_38258 & 0xFF) # Byte reference - MOV operation
ref_40214 = ref_9834 # MOV operation
ref_41502 = ((((((((ref_36072) << 8 | ref_29945) << 8 | ref_29946) << 8 | ref_29947) << 8 | ref_29948) << 8 | ref_29949) << 8 | ref_29950) << 8 | ref_38260) # MOV operation
ref_41612 = ref_41502 # MOV operation
ref_41628 = ref_40214 # MOV operation
ref_41630 = (ref_41612 & ref_41628) # AND operation
ref_41745 = ref_41630 # MOV operation
ref_41763 = (ref_41745 & 0x1F) # AND operation
ref_41976 = ref_41763 # MOV operation
ref_41996 = ((ref_41976 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_42925 = ref_6942 # MOV operation
ref_43035 = ref_42925 # MOV operation
ref_43051 = ref_41996 # MOV operation
ref_43053 = (ref_43035 | ref_43051) # OR operation
ref_43172 = ref_43053 # MOV operation
ref_46616 = ref_25713 # MOV operation
ref_47904 = ref_25713 # MOV operation
ref_48014 = ref_47904 # MOV operation
ref_48030 = ref_46616 # MOV operation
ref_48032 = ((ref_48014 + ref_48030) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_48152 = ref_48032 # MOV operation
ref_50480 = ((((((((ref_36072) << 8 | ref_29945) << 8 | ref_29946) << 8 | ref_29947) << 8 | ref_29948) << 8 | ref_29949) << 8 | ref_29950) << 8 | ref_38260) # MOV operation
ref_50590 = ref_50480 # MOV operation
ref_50608 = (ref_50590 & 0x7) # AND operation
ref_50821 = ref_50608 # MOV operation
ref_50841 = ((ref_50821 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_52134 = ref_48152 # MOV operation
ref_52244 = ref_52134 # MOV operation
ref_52260 = ref_50841 # MOV operation
ref_52262 = (ref_52244 | ref_52260) # OR operation
ref_52381 = ref_52262 # MOV operation
ref_52383 = ((ref_52381 >> 56) & 0xFF) # Byte reference - MOV operation
ref_52384 = ((ref_52381 >> 48) & 0xFF) # Byte reference - MOV operation
ref_52385 = ((ref_52381 >> 40) & 0xFF) # Byte reference - MOV operation
ref_52386 = ((ref_52381 >> 32) & 0xFF) # Byte reference - MOV operation
ref_52387 = ((ref_52381 >> 24) & 0xFF) # Byte reference - MOV operation
ref_52388 = ((ref_52381 >> 16) & 0xFF) # Byte reference - MOV operation
ref_52389 = ((ref_52381 >> 8) & 0xFF) # Byte reference - MOV operation
ref_52390 = (ref_52381 & 0xFF) # Byte reference - MOV operation
ref_54353 = ref_52383 # MOVZX operation
ref_54577 = (ref_54353 & 0xFF) # MOVZX operation
ref_56541 = ref_52390 # MOVZX operation
ref_58509 = (ref_56541 & 0xFF) # MOVZX operation
ref_58511 = (ref_58509 & 0xFF) # Byte reference - MOV operation
ref_58729 = (ref_54577 & 0xFF) # MOVZX operation
ref_60697 = (ref_58729 & 0xFF) # MOVZX operation
ref_60699 = (ref_60697 & 0xFF) # Byte reference - MOV operation
ref_62653 = ((((((((ref_36072) << 8 | ref_29945) << 8 | ref_29946) << 8 | ref_29947) << 8 | ref_29948) << 8 | ref_29949) << 8 | ref_29950) << 8 | ref_38260) # MOV operation
ref_63941 = ((((((((ref_58511) << 8 | ref_52384) << 8 | ref_52385) << 8 | ref_52386) << 8 | ref_52387) << 8 | ref_52388) << 8 | ref_52389) << 8 | ref_60699) # MOV operation
ref_64051 = ref_63941 # MOV operation
ref_64067 = ref_62653 # MOV operation
ref_64069 = (ref_64051 & ref_64067) # AND operation
ref_64184 = ref_64069 # MOV operation
ref_64202 = (ref_64184 & 0x1F) # AND operation
ref_64415 = ref_64202 # MOV operation
ref_64435 = ((ref_64415 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_65364 = ref_43172 # MOV operation
ref_65474 = ref_65364 # MOV operation
ref_65490 = ref_64435 # MOV operation
ref_65492 = (ref_65474 | ref_65490) # OR operation
ref_65611 = ref_65492 # MOV operation
ref_68849 = ref_65611 # MOV operation
ref_69969 = ref_9834 # MOV operation
ref_70177 = ref_69969 # MOV operation
ref_70197 = (ref_70177 >> (0x1 & 0x3F)) # SHR operation
ref_70312 = ref_70197 # MOV operation
ref_70330 = (ref_70312 & 0xF) # AND operation
ref_70445 = ref_70330 # MOV operation
ref_70463 = (ref_70445 | 0x1) # OR operation
ref_70692 = ref_70463 # MOV operation
ref_70694 = ((0x40 - ref_70692) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_70810 = ref_68849 # MOV operation
ref_70826 = ref_70694 # MOV operation
ref_70828 = (ref_70826 & 0xFFFFFFFF) # MOV operation
ref_70830 = ((ref_70810 << ((ref_70828 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_71759 = ref_65611 # MOV operation
ref_72879 = ref_9834 # MOV operation
ref_73087 = ref_72879 # MOV operation
ref_73107 = (ref_73087 >> (0x1 & 0x3F)) # SHR operation
ref_73222 = ref_73107 # MOV operation
ref_73240 = (ref_73222 & 0xF) # AND operation
ref_73355 = ref_73240 # MOV operation
ref_73373 = (ref_73355 | 0x1) # OR operation
ref_73488 = ref_71759 # MOV operation
ref_73504 = ref_73373 # MOV operation
ref_73506 = (ref_73504 & 0xFFFFFFFF) # MOV operation
ref_73508 = (ref_73488 >> ((ref_73506 & 0xFF) & 0x3F)) # SHR operation
ref_73623 = ref_73508 # MOV operation
ref_73639 = ref_70830 # MOV operation
ref_73641 = (ref_73623 | ref_73639) # OR operation
ref_74766 = ((((((((ref_58511) << 8 | ref_52384) << 8 | ref_52385) << 8 | ref_52386) << 8 | ref_52387) << 8 | ref_52388) << 8 | ref_52389) << 8 | ref_60699) # MOV operation
ref_75690 = ((((((((ref_36072) << 8 | ref_29945) << 8 | ref_29946) << 8 | ref_29947) << 8 | ref_29948) << 8 | ref_29949) << 8 | ref_29950) << 8 | ref_38260) # MOV operation
ref_75800 = ref_75690 # MOV operation
ref_75816 = ref_74766 # MOV operation
ref_75818 = (ref_75800 | ref_75816) # OR operation
ref_75933 = ref_75818 # MOV operation
ref_75951 = (ref_75933 & 0xF) # AND operation
ref_76066 = ref_75951 # MOV operation
ref_76084 = (ref_76066 | 0x1) # OR operation
ref_76313 = ref_76084 # MOV operation
ref_76315 = ((0x40 - ref_76313) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_76431 = ref_73641 # MOV operation
ref_76447 = ref_76315 # MOV operation
ref_76449 = (ref_76447 & 0xFFFFFFFF) # MOV operation
ref_76451 = (ref_76431 >> ((ref_76449 & 0xFF) & 0x3F)) # SHR operation
ref_77380 = ref_65611 # MOV operation
ref_78500 = ref_9834 # MOV operation
ref_78708 = ref_78500 # MOV operation
ref_78728 = (ref_78708 >> (0x1 & 0x3F)) # SHR operation
ref_78843 = ref_78728 # MOV operation
ref_78861 = (ref_78843 & 0xF) # AND operation
ref_78976 = ref_78861 # MOV operation
ref_78994 = (ref_78976 | 0x1) # OR operation
ref_79223 = ref_78994 # MOV operation
ref_79225 = ((0x40 - ref_79223) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_79341 = ref_77380 # MOV operation
ref_79357 = ref_79225 # MOV operation
ref_79359 = (ref_79357 & 0xFFFFFFFF) # MOV operation
ref_79361 = ((ref_79341 << ((ref_79359 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_80290 = ref_65611 # MOV operation
ref_81410 = ref_9834 # MOV operation
ref_81618 = ref_81410 # MOV operation
ref_81638 = (ref_81618 >> (0x1 & 0x3F)) # SHR operation
ref_81753 = ref_81638 # MOV operation
ref_81771 = (ref_81753 & 0xF) # AND operation
ref_81886 = ref_81771 # MOV operation
ref_81904 = (ref_81886 | 0x1) # OR operation
ref_82019 = ref_80290 # MOV operation
ref_82035 = ref_81904 # MOV operation
ref_82037 = (ref_82035 & 0xFFFFFFFF) # MOV operation
ref_82039 = (ref_82019 >> ((ref_82037 & 0xFF) & 0x3F)) # SHR operation
ref_82154 = ref_82039 # MOV operation
ref_82170 = ref_79361 # MOV operation
ref_82172 = (ref_82154 | ref_82170) # OR operation
ref_83297 = ((((((((ref_58511) << 8 | ref_52384) << 8 | ref_52385) << 8 | ref_52386) << 8 | ref_52387) << 8 | ref_52388) << 8 | ref_52389) << 8 | ref_60699) # MOV operation
ref_84221 = ((((((((ref_36072) << 8 | ref_29945) << 8 | ref_29946) << 8 | ref_29947) << 8 | ref_29948) << 8 | ref_29949) << 8 | ref_29950) << 8 | ref_38260) # MOV operation
ref_84331 = ref_84221 # MOV operation
ref_84347 = ref_83297 # MOV operation
ref_84349 = (ref_84331 | ref_84347) # OR operation
ref_84464 = ref_84349 # MOV operation
ref_84482 = (ref_84464 & 0xF) # AND operation
ref_84597 = ref_84482 # MOV operation
ref_84615 = (ref_84597 | 0x1) # OR operation
ref_84730 = ref_82172 # MOV operation
ref_84746 = ref_84615 # MOV operation
ref_84748 = (ref_84746 & 0xFFFFFFFF) # MOV operation
ref_84750 = ((ref_84730 << ((ref_84748 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_84865 = ref_84750 # MOV operation
ref_84881 = ref_76451 # MOV operation
ref_84883 = (ref_84865 | ref_84881) # OR operation
ref_85002 = ref_84883 # MOV operation
ref_85213 = ref_85002 # MOV operation
ref_85215 = ref_85213 # MOV operation

print(ref_85215 & 0xffffffffffffffff)
