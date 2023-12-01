#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])

ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_9340 = ref_278 # MOV operation
ref_9488 = ref_9340 # MOV operation
ref_9494 = (0x1D2C27F0 | ref_9488) # OR operation
ref_9569 = ref_9494 # MOV operation
ref_9583 = ((ref_9569 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_10213 = ref_278 # MOV operation
ref_10361 = ref_10213 # MOV operation
ref_10367 = (0x1D2C27F0 | ref_10361) # OR operation
ref_10540 = ref_10367 # MOV operation
ref_10548 = (ref_10540 >> (0x37 & 0x3F)) # SHR operation
ref_10555 = ref_10548 # MOV operation
ref_10633 = ref_9583 # MOV operation
ref_10637 = ref_10555 # MOV operation
ref_10639 = (ref_10637 | ref_10633) # OR operation
ref_10722 = ref_10639 # MOV operation
ref_11987 = ref_278 # MOV operation
ref_12767 = ref_10722 # MOV operation
ref_12817 = ref_12767 # MOV operation
ref_12831 = ((ref_12817 << (0xD & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_13546 = ref_10722 # MOV operation
ref_13694 = ref_13546 # MOV operation
ref_13702 = (ref_13694 >> (0x33 & 0x3F)) # SHR operation
ref_13709 = ref_13702 # MOV operation
ref_13787 = ref_12831 # MOV operation
ref_13791 = ref_13709 # MOV operation
ref_13793 = (ref_13791 | ref_13787) # OR operation
ref_13876 = ref_11987 # MOV operation
ref_13880 = ref_13793 # MOV operation
ref_13882 = (ref_13880 | ref_13876) # OR operation
ref_13965 = ref_13882 # MOV operation
ref_15320 = ref_278 # MOV operation
ref_15370 = ref_15320 # MOV operation
ref_15384 = ((0x6402BE2 + ref_15370) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_15468 = ref_15384 # MOV operation
ref_16733 = ref_278 # MOV operation
ref_16881 = ref_16733 # MOV operation
ref_16887 = (0x3544223F | ref_16881) # OR operation
ref_17692 = ref_15468 # MOV operation
ref_18382 = ref_13965 # MOV operation
ref_18440 = ref_17692 # MOV operation
ref_18444 = ref_18382 # MOV operation
ref_18446 = (((sx(0x40, ref_18444) * sx(0x40, ref_18440)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_18530 = ref_18446 # MOV operation
ref_18532 = (((sx(0x40, ref_18530) * sx(0x40, 0x3BE31211)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_18612 = ref_16887 # MOV operation
ref_18616 = ref_18532 # MOV operation
ref_18618 = (((sx(0x40, ref_18616) * sx(0x40, ref_18612)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_18698 = ref_18618 # MOV operation
ref_20048 = ref_15468 # MOV operation
ref_20918 = ref_18698 # MOV operation
ref_20968 = ref_20918 # MOV operation
ref_20982 = (0x1F & ref_20968) # AND operation
ref_21057 = ref_20982 # MOV operation
ref_21071 = ((ref_21057 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_21154 = ref_20048 # MOV operation
ref_21158 = ref_21071 # MOV operation
ref_21160 = (ref_21158 | ref_21154) # OR operation
ref_21243 = ref_21160 # MOV operation
ref_22101 = ref_13965 # MOV operation
ref_22249 = ref_22101 # MOV operation
ref_22257 = (ref_22249 >> (0x1 & 0x3F)) # SHR operation
ref_22264 = ref_22257 # MOV operation
ref_22334 = ref_22264 # MOV operation
ref_22348 = (0xF & ref_22334) # AND operation
ref_22521 = ref_22348 # MOV operation
ref_22527 = (0x1 | ref_22521) # OR operation
ref_23242 = ref_10722 # MOV operation
ref_23292 = ref_23242 # MOV operation
ref_23304 = ref_22527 # MOV operation
ref_23306 = ((ref_23292 << ((ref_23304 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_24021 = ref_10722 # MOV operation
ref_24801 = ref_13965 # MOV operation
ref_24949 = ref_24801 # MOV operation
ref_24957 = (ref_24949 >> (0x1 & 0x3F)) # SHR operation
ref_24964 = ref_24957 # MOV operation
ref_25034 = ref_24964 # MOV operation
ref_25048 = (0xF & ref_25034) # AND operation
ref_25221 = ref_25048 # MOV operation
ref_25227 = (0x1 | ref_25221) # OR operation
ref_25404 = ref_25227 # MOV operation
ref_25406 = ((0x40 - ref_25404) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_25414 = ref_25406 # MOV operation
ref_25492 = ref_24021 # MOV operation
ref_25496 = ref_25414 # MOV operation
ref_25498 = (ref_25496 & 0xFFFFFFFF) # MOV operation
ref_25500 = (ref_25492 >> ((ref_25498 & 0xFF) & 0x3F)) # SHR operation
ref_25507 = ref_25500 # MOV operation
ref_25585 = ref_23306 # MOV operation
ref_25589 = ref_25507 # MOV operation
ref_25591 = (ref_25589 | ref_25585) # OR operation
ref_26306 = ref_21243 # MOV operation
ref_27086 = ref_18698 # MOV operation
ref_27234 = ref_27086 # MOV operation
ref_27242 = (ref_27234 >> (0x3 & 0x3F)) # SHR operation
ref_27249 = ref_27242 # MOV operation
ref_27319 = ref_27249 # MOV operation
ref_27333 = (0x7 & ref_27319) # AND operation
ref_27506 = ref_27333 # MOV operation
ref_27512 = (0x1 | ref_27506) # OR operation
ref_27595 = ref_26306 # MOV operation
ref_27599 = ref_27512 # MOV operation
ref_27601 = (ref_27599 & 0xFFFFFFFF) # MOV operation
ref_27603 = (ref_27595 >> ((ref_27601 & 0xFF) & 0x3F)) # SHR operation
ref_27610 = ref_27603 # MOV operation
ref_27688 = ref_25591 # MOV operation
ref_27692 = ref_27610 # MOV operation
ref_27694 = ((ref_27688 - ref_27692) & 0xFFFFFFFFFFFFFFFF) # CMP operation
ref_27696 = ((((ref_27688 ^ (ref_27692 ^ ref_27694)) ^ ((ref_27688 ^ ref_27694) & (ref_27688 ^ ref_27692))) >> 63) & 0x1) # Carry flag
ref_27700 = (0x1 if (ref_27694 == 0x0) else 0x0) # Zero flag
ref_27702 = ((((ref_27692 >> 8) & 0xFFFFFFFFFFFFFF)) << 8 | (0x1 if ((ref_27696 | ref_27700) == 0x1) else 0x0)) # SETBE operation
ref_27704 = (ref_27702 & 0xFF) # MOVZX operation
ref_27766 = (ref_27704 & 0xFFFFFFFF) # MOV operation
ref_27768 = ((ref_27766 & 0xFFFFFFFF) & (ref_27766 & 0xFFFFFFFF)) # TEST operation
ref_27773 = (0x1 if (ref_27768 == 0x0) else 0x0) # Zero flag
ref_27775 = (0x36C2 if (ref_27773 == 0x1) else 0x36A4) # Program Counter


if (ref_27773 == 0x1):
    ref_263 = SymVar_0
    ref_278 = ref_263 # MOV operation
    ref_9340 = ref_278 # MOV operation
    ref_9488 = ref_9340 # MOV operation
    ref_9494 = (0x1D2C27F0 | ref_9488) # OR operation
    ref_9569 = ref_9494 # MOV operation
    ref_9583 = ((ref_9569 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_10213 = ref_278 # MOV operation
    ref_10361 = ref_10213 # MOV operation
    ref_10367 = (0x1D2C27F0 | ref_10361) # OR operation
    ref_10540 = ref_10367 # MOV operation
    ref_10548 = (ref_10540 >> (0x37 & 0x3F)) # SHR operation
    ref_10555 = ref_10548 # MOV operation
    ref_10633 = ref_9583 # MOV operation
    ref_10637 = ref_10555 # MOV operation
    ref_10639 = (ref_10637 | ref_10633) # OR operation
    ref_10722 = ref_10639 # MOV operation
    ref_11987 = ref_278 # MOV operation
    ref_12767 = ref_10722 # MOV operation
    ref_12817 = ref_12767 # MOV operation
    ref_12831 = ((ref_12817 << (0xD & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_13546 = ref_10722 # MOV operation
    ref_13694 = ref_13546 # MOV operation
    ref_13702 = (ref_13694 >> (0x33 & 0x3F)) # SHR operation
    ref_13709 = ref_13702 # MOV operation
    ref_13787 = ref_12831 # MOV operation
    ref_13791 = ref_13709 # MOV operation
    ref_13793 = (ref_13791 | ref_13787) # OR operation
    ref_13876 = ref_11987 # MOV operation
    ref_13880 = ref_13793 # MOV operation
    ref_13882 = (ref_13880 | ref_13876) # OR operation
    ref_13965 = ref_13882 # MOV operation
    ref_15320 = ref_278 # MOV operation
    ref_15370 = ref_15320 # MOV operation
    ref_15384 = ((0x6402BE2 + ref_15370) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_15468 = ref_15384 # MOV operation
    ref_16733 = ref_278 # MOV operation
    ref_16881 = ref_16733 # MOV operation
    ref_16887 = (0x3544223F | ref_16881) # OR operation
    ref_17692 = ref_15468 # MOV operation
    ref_18382 = ref_13965 # MOV operation
    ref_18440 = ref_17692 # MOV operation
    ref_18444 = ref_18382 # MOV operation
    ref_18446 = (((sx(0x40, ref_18444) * sx(0x40, ref_18440)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_18530 = ref_18446 # MOV operation
    ref_18532 = (((sx(0x40, ref_18530) * sx(0x40, 0x3BE31211)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_18612 = ref_16887 # MOV operation
    ref_18616 = ref_18532 # MOV operation
    ref_18618 = (((sx(0x40, ref_18616) * sx(0x40, ref_18612)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_18698 = ref_18618 # MOV operation
    ref_20048 = ref_15468 # MOV operation
    ref_20918 = ref_18698 # MOV operation
    ref_20968 = ref_20918 # MOV operation
    ref_20982 = (0x1F & ref_20968) # AND operation
    ref_21057 = ref_20982 # MOV operation
    ref_21071 = ((ref_21057 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_21154 = ref_20048 # MOV operation
    ref_21158 = ref_21071 # MOV operation
    ref_21160 = (ref_21158 | ref_21154) # OR operation
    ref_21243 = ref_21160 # MOV operation
    ref_29192 = ref_13965 # MOV operation
    ref_30062 = ref_13965 # MOV operation
    ref_30112 = ref_30062 # MOV operation
    ref_30126 = (0xF & ref_30112) # AND operation
    ref_30201 = ref_30126 # MOV operation
    ref_30215 = ((ref_30201 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_30298 = ref_29192 # MOV operation
    ref_30302 = ref_30215 # MOV operation
    ref_30304 = (ref_30302 | ref_30298) # OR operation
    ref_30387 = ref_30304 # MOV operation
    ref_31809 = ref_30387 # MOV operation
    ref_31957 = ref_31809 # MOV operation
    ref_31965 = (ref_31957 >> (0x3 & 0x3F)) # SHR operation
    ref_31972 = ref_31965 # MOV operation
    ref_32042 = ref_31972 # MOV operation
    ref_32056 = (0xF & ref_32042) # AND operation
    ref_32229 = ref_32056 # MOV operation
    ref_32235 = (0x1 | ref_32229) # OR operation
    ref_32950 = ref_10722 # MOV operation
    ref_33000 = ref_32950 # MOV operation
    ref_33012 = ref_32235 # MOV operation
    ref_33014 = ((ref_33000 << ((ref_33012 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_33729 = ref_10722 # MOV operation
    ref_34509 = ref_30387 # MOV operation
    ref_34657 = ref_34509 # MOV operation
    ref_34665 = (ref_34657 >> (0x3 & 0x3F)) # SHR operation
    ref_34672 = ref_34665 # MOV operation
    ref_34742 = ref_34672 # MOV operation
    ref_34756 = (0xF & ref_34742) # AND operation
    ref_34929 = ref_34756 # MOV operation
    ref_34935 = (0x1 | ref_34929) # OR operation
    ref_35112 = ref_34935 # MOV operation
    ref_35114 = ((0x40 - ref_35112) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_35122 = ref_35114 # MOV operation
    ref_35200 = ref_33729 # MOV operation
    ref_35204 = ref_35122 # MOV operation
    ref_35206 = (ref_35204 & 0xFFFFFFFF) # MOV operation
    ref_35208 = (ref_35200 >> ((ref_35206 & 0xFF) & 0x3F)) # SHR operation
    ref_35215 = ref_35208 # MOV operation
    ref_35293 = ref_33014 # MOV operation
    ref_35297 = ref_35215 # MOV operation
    ref_35299 = (ref_35297 | ref_35293) # OR operation
    ref_36014 = ref_21243 # MOV operation
    ref_36794 = ref_18698 # MOV operation
    ref_36844 = ref_36794 # MOV operation
    ref_36858 = ((0x369A4780 + ref_36844) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_36942 = ref_36014 # MOV operation
    ref_36946 = ref_36858 # MOV operation
    ref_36948 = (((sx(0x40, ref_36946) * sx(0x40, ref_36942)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_37028 = ref_35299 # MOV operation
    ref_37032 = ref_36948 # MOV operation
    ref_37034 = (((sx(0x40, ref_37032) * sx(0x40, ref_37028)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_37114 = ref_37034 # MOV operation
    ref_37273 = ref_37114 # MOV operation
    ref_37275 = ref_37273 # MOV operation
    endb = ref_37275


else:
    ref_37595 = SymVar_0
    ref_37610 = ref_37595 # MOV operation
    ref_46677 = ref_37610 # MOV operation
    ref_46825 = ref_46677 # MOV operation
    ref_46831 = (0x1D2C27F0 | ref_46825) # OR operation
    ref_46906 = ref_46831 # MOV operation
    ref_46920 = ((ref_46906 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_47550 = ref_37610 # MOV operation
    ref_47698 = ref_47550 # MOV operation
    ref_47704 = (0x1D2C27F0 | ref_47698) # OR operation
    ref_47877 = ref_47704 # MOV operation
    ref_47885 = (ref_47877 >> (0x37 & 0x3F)) # SHR operation
    ref_47892 = ref_47885 # MOV operation
    ref_47970 = ref_46920 # MOV operation
    ref_47974 = ref_47892 # MOV operation
    ref_47976 = (ref_47974 | ref_47970) # OR operation
    ref_48059 = ref_47976 # MOV operation
    ref_49324 = ref_37610 # MOV operation
    ref_50104 = ref_48059 # MOV operation
    ref_50154 = ref_50104 # MOV operation
    ref_50168 = ((ref_50154 << (0xD & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_50883 = ref_48059 # MOV operation
    ref_51031 = ref_50883 # MOV operation
    ref_51039 = (ref_51031 >> (0x33 & 0x3F)) # SHR operation
    ref_51046 = ref_51039 # MOV operation
    ref_51124 = ref_50168 # MOV operation
    ref_51128 = ref_51046 # MOV operation
    ref_51130 = (ref_51128 | ref_51124) # OR operation
    ref_51213 = ref_49324 # MOV operation
    ref_51217 = ref_51130 # MOV operation
    ref_51219 = (ref_51217 | ref_51213) # OR operation
    ref_51302 = ref_51219 # MOV operation
    ref_51304 = ((ref_51302 >> 56) & 0xFF) # Byte reference - MOV operation
    ref_51305 = ((ref_51302 >> 48) & 0xFF) # Byte reference - MOV operation
    ref_51306 = ((ref_51302 >> 40) & 0xFF) # Byte reference - MOV operation
    ref_51307 = ((ref_51302 >> 32) & 0xFF) # Byte reference - MOV operation
    ref_51308 = ((ref_51302 >> 24) & 0xFF) # Byte reference - MOV operation
    ref_51309 = ((ref_51302 >> 16) & 0xFF) # Byte reference - MOV operation
    ref_51310 = ((ref_51302 >> 8) & 0xFF) # Byte reference - MOV operation
    ref_51311 = (ref_51302 & 0xFF) # Byte reference - MOV operation
    ref_52657 = ref_37610 # MOV operation
    ref_52707 = ref_52657 # MOV operation
    ref_52721 = ((0x6402BE2 + ref_52707) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_52805 = ref_52721 # MOV operation
    ref_54070 = ref_37610 # MOV operation
    ref_54218 = ref_54070 # MOV operation
    ref_54224 = (0x3544223F | ref_54218) # OR operation
    ref_55029 = ref_52805 # MOV operation
    ref_55719 = ref_51302 # MOV operation
    ref_55777 = ref_55029 # MOV operation
    ref_55781 = ref_55719 # MOV operation
    ref_55783 = (((sx(0x40, ref_55781) * sx(0x40, ref_55777)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_55867 = ref_55783 # MOV operation
    ref_55869 = (((sx(0x40, ref_55867) * sx(0x40, 0x3BE31211)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_55949 = ref_54224 # MOV operation
    ref_55953 = ref_55869 # MOV operation
    ref_55955 = (((sx(0x40, ref_55953) * sx(0x40, ref_55949)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_56035 = ref_55955 # MOV operation
    ref_57385 = ref_52805 # MOV operation
    ref_58255 = ref_56035 # MOV operation
    ref_58305 = ref_58255 # MOV operation
    ref_58319 = (0x1F & ref_58305) # AND operation
    ref_58394 = ref_58319 # MOV operation
    ref_58408 = ((ref_58394 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_58491 = ref_57385 # MOV operation
    ref_58495 = ref_58408 # MOV operation
    ref_58497 = (ref_58495 | ref_58491) # OR operation
    ref_58580 = ref_58497 # MOV operation
    ref_66568 = ref_56035 # MOV operation
    ref_66618 = ref_66568 # MOV operation
    ref_66634 = ((((0x0) << 64 | ref_66618) / 0x8) & 0xFFFFFFFFFFFFFFFF) # DIV operation
    ref_66713 = ref_66634 # MOV operation
    ref_66715 = ((ref_66713 >> 56) & 0xFF) # Byte reference - MOV operation
    ref_66716 = ((ref_66713 >> 48) & 0xFF) # Byte reference - MOV operation
    ref_66717 = ((ref_66713 >> 40) & 0xFF) # Byte reference - MOV operation
    ref_66718 = ((ref_66713 >> 32) & 0xFF) # Byte reference - MOV operation
    ref_66719 = ((ref_66713 >> 24) & 0xFF) # Byte reference - MOV operation
    ref_66720 = ((ref_66713 >> 16) & 0xFF) # Byte reference - MOV operation
    ref_66721 = ((ref_66713 >> 8) & 0xFF) # Byte reference - MOV operation
    ref_66722 = (ref_66713 & 0xFF) # Byte reference - MOV operation
    ref_67873 = ref_51309 # MOVZX operation
    ref_68025 = (ref_67873 & 0xFF) # MOVZX operation
    ref_69177 = ref_51306 # MOVZX operation
    ref_70317 = (ref_69177 & 0xFF) # MOVZX operation
    ref_70319 = (ref_70317 & 0xFF) # Byte reference - MOV operation
    ref_70481 = (ref_68025 & 0xFF) # MOVZX operation
    ref_71621 = (ref_70481 & 0xFF) # MOVZX operation
    ref_71623 = (ref_71621 & 0xFF) # Byte reference - MOV operation
    ref_72773 = ref_51304 # MOVZX operation
    ref_72925 = (ref_72773 & 0xFF) # MOVZX operation
    ref_74077 = ref_51311 # MOVZX operation
    ref_75217 = (ref_74077 & 0xFF) # MOVZX operation
    ref_75219 = (ref_75217 & 0xFF) # Byte reference - MOV operation
    ref_75381 = (ref_72925 & 0xFF) # MOVZX operation
    ref_76521 = (ref_75381 & 0xFF) # MOVZX operation
    ref_76523 = (ref_76521 & 0xFF) # Byte reference - MOV operation
    ref_77673 = ref_66718 # MOVZX operation
    ref_77825 = (ref_77673 & 0xFF) # MOVZX operation
    ref_78977 = ref_66722 # MOVZX operation
    ref_80117 = (ref_78977 & 0xFF) # MOVZX operation
    ref_80119 = (ref_80117 & 0xFF) # Byte reference - MOV operation
    ref_80281 = (ref_77825 & 0xFF) # MOVZX operation
    ref_81421 = (ref_80281 & 0xFF) # MOVZX operation
    ref_81423 = (ref_81421 & 0xFF) # Byte reference - MOV operation
    ref_82835 = ((((((((ref_75219) << 8 | ref_51305) << 8 | ref_71623) << 8 | ref_51307) << 8 | ref_51308) << 8 | ref_70319) << 8 | ref_51310) << 8 | ref_76523) # MOV operation
    ref_82983 = ref_82835 # MOV operation
    ref_82991 = (ref_82983 >> (0x3 & 0x3F)) # SHR operation
    ref_82998 = ref_82991 # MOV operation
    ref_83068 = ref_82998 # MOV operation
    ref_83082 = (0xF & ref_83068) # AND operation
    ref_83255 = ref_83082 # MOV operation
    ref_83261 = (0x1 | ref_83255) # OR operation
    ref_83976 = ((((((((ref_66715) << 8 | ref_66716) << 8 | ref_66717) << 8 | ref_80119) << 8 | ref_66719) << 8 | ref_66720) << 8 | ref_66721) << 8 | ref_81423) # MOV operation
    ref_84026 = ref_83976 # MOV operation
    ref_84038 = ref_83261 # MOV operation
    ref_84040 = ((ref_84026 << ((ref_84038 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_84755 = ((((((((ref_66715) << 8 | ref_66716) << 8 | ref_66717) << 8 | ref_80119) << 8 | ref_66719) << 8 | ref_66720) << 8 | ref_66721) << 8 | ref_81423) # MOV operation
    ref_85535 = ((((((((ref_75219) << 8 | ref_51305) << 8 | ref_71623) << 8 | ref_51307) << 8 | ref_51308) << 8 | ref_70319) << 8 | ref_51310) << 8 | ref_76523) # MOV operation
    ref_85683 = ref_85535 # MOV operation
    ref_85691 = (ref_85683 >> (0x3 & 0x3F)) # SHR operation
    ref_85698 = ref_85691 # MOV operation
    ref_85768 = ref_85698 # MOV operation
    ref_85782 = (0xF & ref_85768) # AND operation
    ref_85955 = ref_85782 # MOV operation
    ref_85961 = (0x1 | ref_85955) # OR operation
    ref_86138 = ref_85961 # MOV operation
    ref_86140 = ((0x40 - ref_86138) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_86148 = ref_86140 # MOV operation
    ref_86226 = ref_84755 # MOV operation
    ref_86230 = ref_86148 # MOV operation
    ref_86232 = (ref_86230 & 0xFFFFFFFF) # MOV operation
    ref_86234 = (ref_86226 >> ((ref_86232 & 0xFF) & 0x3F)) # SHR operation
    ref_86241 = ref_86234 # MOV operation
    ref_86319 = ref_84040 # MOV operation
    ref_86323 = ref_86241 # MOV operation
    ref_86325 = (ref_86323 | ref_86319) # OR operation
    ref_87040 = ref_58580 # MOV operation
    ref_87820 = ref_56035 # MOV operation
    ref_87870 = ref_87820 # MOV operation
    ref_87884 = ((0x369A4780 + ref_87870) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_87968 = ref_87040 # MOV operation
    ref_87972 = ref_87884 # MOV operation
    ref_87974 = (((sx(0x40, ref_87972) * sx(0x40, ref_87968)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_88054 = ref_86325 # MOV operation
    ref_88058 = ref_87974 # MOV operation
    ref_88060 = (((sx(0x40, ref_88058) * sx(0x40, ref_88054)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_88140 = ref_88060 # MOV operation
    ref_88299 = ref_88140 # MOV operation
    ref_88301 = ref_88299 # MOV operation
    endb = ref_88301


print(endb & 0xffffffffffffffff)
