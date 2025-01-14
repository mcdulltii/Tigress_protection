#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_6416 = ref_278 # MOV operation
ref_6616 = ref_6416 # MOV operation
ref_6624 = (ref_6616 >> (0x3 & 0x3F)) # SHR operation
ref_6631 = ref_6624 # MOV operation
ref_7580 = ref_278 # MOV operation
ref_7656 = ref_7580 # MOV operation
ref_7670 = ((ref_7656 << (0x3D & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_7779 = ref_6631 # MOV operation
ref_7783 = ref_7670 # MOV operation
ref_7785 = (ref_7783 | ref_7779) # OR operation
ref_7886 = ref_7785 # MOV operation
ref_7900 = ((ref_7886 - 0x3FEFFF7F) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_7908 = ref_7900 # MOV operation
ref_8012 = ref_7908 # MOV operation
ref_8014 = ((ref_8012 >> 56) & 0xFF) # Byte reference - MOV operation
ref_8015 = ((ref_8012 >> 48) & 0xFF) # Byte reference - MOV operation
ref_8016 = ((ref_8012 >> 40) & 0xFF) # Byte reference - MOV operation
ref_8017 = ((ref_8012 >> 32) & 0xFF) # Byte reference - MOV operation
ref_8018 = ((ref_8012 >> 24) & 0xFF) # Byte reference - MOV operation
ref_8019 = ((ref_8012 >> 16) & 0xFF) # Byte reference - MOV operation
ref_8020 = ((ref_8012 >> 8) & 0xFF) # Byte reference - MOV operation
ref_8021 = (ref_8012 & 0xFF) # Byte reference - MOV operation
ref_9783 = ref_278 # MOV operation
ref_10681 = ref_8012 # MOV operation
ref_10765 = ref_9783 # MOV operation
ref_10769 = ref_10681 # MOV operation
ref_10771 = (ref_10769 | ref_10765) # OR operation
ref_10872 = ref_10771 # MOV operation
ref_10886 = ((ref_10872 - 0x11E59B96) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_10894 = ref_10886 # MOV operation
ref_10998 = ref_10894 # MOV operation
ref_11000 = ((ref_10998 >> 56) & 0xFF) # Byte reference - MOV operation
ref_11001 = ((ref_10998 >> 48) & 0xFF) # Byte reference - MOV operation
ref_11002 = ((ref_10998 >> 40) & 0xFF) # Byte reference - MOV operation
ref_11003 = ((ref_10998 >> 32) & 0xFF) # Byte reference - MOV operation
ref_11004 = ((ref_10998 >> 24) & 0xFF) # Byte reference - MOV operation
ref_11005 = ((ref_10998 >> 16) & 0xFF) # Byte reference - MOV operation
ref_11006 = ((ref_10998 >> 8) & 0xFF) # Byte reference - MOV operation
ref_11007 = (ref_10998 & 0xFF) # Byte reference - MOV operation
ref_12653 = ref_278 # MOV operation
ref_13551 = ref_8012 # MOV operation
ref_13635 = ref_12653 # MOV operation
ref_13639 = ref_13551 # MOV operation
ref_13641 = (((sx(0x40, ref_13639) * sx(0x40, ref_13635)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_14677 = ref_10998 # MOV operation
ref_14753 = ref_14677 # MOV operation
ref_14767 = ((ref_14753 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_14876 = ref_13641 # MOV operation
ref_14880 = ref_14767 # MOV operation
ref_14882 = (((sx(0x40, ref_14880) * sx(0x40, ref_14876)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_14988 = ref_14882 # MOV operation
ref_16759 = ref_278 # MOV operation
ref_16835 = ref_16759 # MOV operation
ref_16849 = ((ref_16835 - 0x2000000007A4C37E) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_16857 = ref_16849 # MOV operation
ref_16961 = ref_16857 # MOV operation
ref_19558 = ((((ref_8014) << 8 | ref_8015) << 8 | ref_8016) << 8 | ref_8017) # MOV operation
ref_19766 = (ref_19558 & 0xFFFFFFFF) # MOV operation
ref_21374 = ((((ref_8018) << 8 | ref_8019) << 8 | ref_8020) << 8 | ref_8021) # MOV operation
ref_22970 = (ref_21374 & 0xFFFFFFFF) # MOV operation
ref_22972 = (((ref_22970 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_22973 = (((ref_22970 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_22974 = (((ref_22970 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_22975 = ((ref_22970 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_23190 = (ref_19766 & 0xFFFFFFFF) # MOV operation
ref_24786 = (ref_23190 & 0xFFFFFFFF) # MOV operation
ref_24788 = (((ref_24786 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_24789 = (((ref_24786 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_24790 = (((ref_24786 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_24791 = ((ref_24786 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_26698 = ((((((((ref_22972) << 8 | ref_22973) << 8 | ref_22974) << 8 | ref_22975) << 8 | ref_24788) << 8 | ref_24789) << 8 | ref_24790) << 8 | ref_24791) # MOV operation
ref_28032 = ref_14988 # MOV operation
ref_28930 = ref_14988 # MOV operation
ref_29014 = ref_28032 # MOV operation
ref_29018 = ref_28930 # MOV operation
ref_29020 = ((ref_29018 + ref_29014) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_29246 = ref_29020 # MOV operation
ref_29252 = (0x3F & ref_29246) # AND operation
ref_29353 = ref_29252 # MOV operation
ref_29367 = ((ref_29353 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_29476 = ref_26698 # MOV operation
ref_29480 = ref_29367 # MOV operation
ref_29482 = (ref_29480 | ref_29476) # OR operation
ref_29591 = ref_29482 # MOV operation
ref_32508 = ((((ref_11000) << 8 | ref_11001) << 8 | ref_11002) << 8 | ref_11003) # MOV operation
ref_32716 = (ref_32508 & 0xFFFFFFFF) # MOV operation
ref_34324 = ((((ref_11004) << 8 | ref_11005) << 8 | ref_11006) << 8 | ref_11007) # MOV operation
ref_35920 = (ref_34324 & 0xFFFFFFFF) # MOV operation
ref_35922 = (((ref_35920 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_35923 = (((ref_35920 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_35924 = (((ref_35920 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_35925 = ((ref_35920 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_36140 = (ref_32716 & 0xFFFFFFFF) # MOV operation
ref_37736 = (ref_36140 & 0xFFFFFFFF) # MOV operation
ref_37738 = (((ref_37736 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_37739 = (((ref_37736 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_37740 = (((ref_37736 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_37741 = ((ref_37736 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_39648 = ((((((((ref_35922) << 8 | ref_35923) << 8 | ref_35924) << 8 | ref_35925) << 8 | ref_37738) << 8 | ref_37739) << 8 | ref_37740) << 8 | ref_37741) # MOV operation
ref_40982 = ref_16961 # MOV operation
ref_41880 = ref_14988 # MOV operation
ref_41964 = ref_40982 # MOV operation
ref_41968 = ref_41880 # MOV operation
ref_41970 = ((ref_41968 + ref_41964) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_42196 = ref_41970 # MOV operation
ref_42202 = (0x3F & ref_42196) # AND operation
ref_42303 = ref_42202 # MOV operation
ref_42317 = ((ref_42303 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_42426 = ref_39648 # MOV operation
ref_42430 = ref_42317 # MOV operation
ref_42432 = (ref_42430 | ref_42426) # OR operation
ref_42541 = ref_42432 # MOV operation
ref_42543 = ((ref_42541 >> 56) & 0xFF) # Byte reference - MOV operation
ref_42544 = ((ref_42541 >> 48) & 0xFF) # Byte reference - MOV operation
ref_42545 = ((ref_42541 >> 40) & 0xFF) # Byte reference - MOV operation
ref_42546 = ((ref_42541 >> 32) & 0xFF) # Byte reference - MOV operation
ref_42547 = ((ref_42541 >> 24) & 0xFF) # Byte reference - MOV operation
ref_42548 = ((ref_42541 >> 16) & 0xFF) # Byte reference - MOV operation
ref_42549 = ((ref_42541 >> 8) & 0xFF) # Byte reference - MOV operation
ref_42550 = (ref_42541 & 0xFF) # Byte reference - MOV operation
ref_45531 = ref_42545 # MOVZX operation
ref_45735 = (ref_45531 & 0xFF) # MOVZX operation
ref_47251 = ref_42549 # MOVZX operation
ref_48755 = (ref_47251 & 0xFF) # MOVZX operation
ref_48757 = (ref_48755 & 0xFF) # Byte reference - MOV operation
ref_48971 = (ref_45735 & 0xFF) # MOVZX operation
ref_50475 = (ref_48971 & 0xFF) # MOVZX operation
ref_50477 = (ref_50475 & 0xFF) # Byte reference - MOV operation
ref_52131 = ref_14988 # MOV operation
ref_53029 = ref_16961 # MOV operation
ref_53113 = ref_52131 # MOV operation
ref_53117 = ref_53029 # MOV operation
ref_53119 = (ref_53117 & ref_53113) # AND operation
ref_53344 = ref_53119 # MOV operation
ref_53350 = (0xF & ref_53344) # AND operation
ref_53575 = ref_53350 # MOV operation
ref_53581 = (0x1 | ref_53575) # OR operation
ref_54504 = ref_29591 # MOV operation
ref_55402 = ((((((((ref_42543) << 8 | ref_42544) << 8 | ref_48757) << 8 | ref_42546) << 8 | ref_42547) << 8 | ref_42548) << 8 | ref_50477) << 8 | ref_42550) # MOV operation
ref_55486 = ref_54504 # MOV operation
ref_55490 = ref_55402 # MOV operation
ref_55492 = ((ref_55490 + ref_55486) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_55594 = ref_55492 # MOV operation
ref_55606 = ref_53581 # MOV operation
ref_55608 = ((ref_55594 << ((ref_55606 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_56531 = ref_29591 # MOV operation
ref_57429 = ((((((((ref_42543) << 8 | ref_42544) << 8 | ref_48757) << 8 | ref_42546) << 8 | ref_42547) << 8 | ref_42548) << 8 | ref_50477) << 8 | ref_42550) # MOV operation
ref_57513 = ref_56531 # MOV operation
ref_57517 = ref_57429 # MOV operation
ref_57519 = ((ref_57517 + ref_57513) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_58443 = ref_14988 # MOV operation
ref_59341 = ref_16961 # MOV operation
ref_59425 = ref_58443 # MOV operation
ref_59429 = ref_59341 # MOV operation
ref_59431 = (ref_59429 & ref_59425) # AND operation
ref_59656 = ref_59431 # MOV operation
ref_59662 = (0xF & ref_59656) # AND operation
ref_59887 = ref_59662 # MOV operation
ref_59893 = (0x1 | ref_59887) # OR operation
ref_60122 = ref_59893 # MOV operation
ref_60124 = ((0x40 - ref_60122) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_60132 = ref_60124 # MOV operation
ref_60236 = ref_57519 # MOV operation
ref_60240 = ref_60132 # MOV operation
ref_60242 = (ref_60240 & 0xFFFFFFFF) # MOV operation
ref_60244 = (ref_60236 >> ((ref_60242 & 0xFF) & 0x3F)) # SHR operation
ref_60251 = ref_60244 # MOV operation
ref_60355 = ref_55608 # MOV operation
ref_60359 = ref_60251 # MOV operation
ref_60361 = (ref_60359 | ref_60355) # OR operation
ref_60470 = ref_60361 # MOV operation
ref_60681 = ref_60470 # MOV operation
ref_60683 = ref_60681 # MOV operation

print(ref_60683 & 0xffffffffffffffff)
