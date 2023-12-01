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
ref_9390 = ref_9340 # MOV operation
ref_9404 = ((ref_9390 - 0x35CEDE6D) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_9412 = ref_9404 # MOV operation
ref_9490 = ref_9412 # MOV operation
ref_10755 = ref_278 # MOV operation
ref_10903 = ref_10755 # MOV operation
ref_10911 = ((((0x0) << 64 | ref_10903) / 0x7) & 0xFFFFFFFFFFFFFFFF) # DIV operation
ref_10990 = ref_10911 # MOV operation
ref_12520 = ref_10990 # MOV operation
ref_12570 = ref_12520 # MOV operation
ref_12584 = (ref_12570 >> (0x3 & 0x3F)) # SHR operation
ref_12757 = ref_12584 # MOV operation
ref_12763 = (0xF & ref_12757) # AND operation
ref_12936 = ref_12763 # MOV operation
ref_12942 = (0x1 | ref_12936) # OR operation
ref_13119 = ref_12942 # MOV operation
ref_13121 = ((0x7A11169 << ((ref_13119 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_13926 = ref_10990 # MOV operation
ref_13976 = ref_13926 # MOV operation
ref_13990 = (ref_13976 >> (0x3 & 0x3F)) # SHR operation
ref_14163 = ref_13990 # MOV operation
ref_14169 = (0xF & ref_14163) # AND operation
ref_14342 = ref_14169 # MOV operation
ref_14348 = (0x1 | ref_14342) # OR operation
ref_14525 = ref_14348 # MOV operation
ref_14527 = ((0x40 - ref_14525) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_14535 = ref_14527 # MOV operation
ref_14707 = ref_14535 # MOV operation
ref_14709 = (0x7A11169 >> ((ref_14707 & 0xFF) & 0x3F)) # SHR operation
ref_14792 = ref_13121 # MOV operation
ref_14796 = ref_14709 # MOV operation
ref_14798 = (ref_14796 | ref_14792) # OR operation
ref_14873 = ref_14798 # MOV operation
ref_14887 = (ref_14873 >> (0x4 & 0x3F)) # SHR operation
ref_15060 = ref_14887 # MOV operation
ref_15066 = (0xF & ref_15060) # AND operation
ref_15239 = ref_15066 # MOV operation
ref_15245 = (0x1 | ref_15239) # OR operation
ref_15875 = ref_278 # MOV operation
ref_15925 = ref_15875 # MOV operation
ref_15937 = ref_15245 # MOV operation
ref_15939 = ((ref_15925 << ((ref_15937 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_16834 = ref_10990 # MOV operation
ref_16884 = ref_16834 # MOV operation
ref_16898 = (ref_16884 >> (0x3 & 0x3F)) # SHR operation
ref_17071 = ref_16898 # MOV operation
ref_17077 = (0xF & ref_17071) # AND operation
ref_17250 = ref_17077 # MOV operation
ref_17256 = (0x1 | ref_17250) # OR operation
ref_17433 = ref_17256 # MOV operation
ref_17435 = ((0x7A11169 << ((ref_17433 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_18240 = ref_10990 # MOV operation
ref_18290 = ref_18240 # MOV operation
ref_18304 = (ref_18290 >> (0x3 & 0x3F)) # SHR operation
ref_18477 = ref_18304 # MOV operation
ref_18483 = (0xF & ref_18477) # AND operation
ref_18656 = ref_18483 # MOV operation
ref_18662 = (0x1 | ref_18656) # OR operation
ref_18839 = ref_18662 # MOV operation
ref_18841 = ((0x40 - ref_18839) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_18849 = ref_18841 # MOV operation
ref_19021 = ref_18849 # MOV operation
ref_19023 = (0x7A11169 >> ((ref_19021 & 0xFF) & 0x3F)) # SHR operation
ref_19106 = ref_17435 # MOV operation
ref_19110 = ref_19023 # MOV operation
ref_19112 = (ref_19110 | ref_19106) # OR operation
ref_19187 = ref_19112 # MOV operation
ref_19201 = (ref_19187 >> (0x4 & 0x3F)) # SHR operation
ref_19374 = ref_19201 # MOV operation
ref_19380 = (0xF & ref_19374) # AND operation
ref_19553 = ref_19380 # MOV operation
ref_19559 = (0x1 | ref_19553) # OR operation
ref_19736 = ref_19559 # MOV operation
ref_19738 = ((0x40 - ref_19736) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_19746 = ref_19738 # MOV operation
ref_20371 = ref_278 # MOV operation
ref_20421 = ref_20371 # MOV operation
ref_20433 = ref_19746 # MOV operation
ref_20435 = (ref_20421 >> ((ref_20433 & 0xFF) & 0x3F)) # SHR operation
ref_20518 = ref_15939 # MOV operation
ref_20522 = ref_20435 # MOV operation
ref_20524 = (ref_20522 | ref_20518) # OR operation
ref_20607 = ref_20524 # MOV operation
ref_21962 = ref_278 # MOV operation
ref_22012 = ref_21962 # MOV operation
ref_22026 = ((ref_22012 - 0x297EE8A1) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_22034 = ref_22026 # MOV operation
ref_22202 = ref_22034 # MOV operation
ref_22208 = (((sx(0x40, 0x1471C5DA) * sx(0x40, ref_22202)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_22288 = ref_22208 # MOV operation
ref_22290 = ((ref_22288 >> 56) & 0xFF) # Byte reference - MOV operation
ref_22291 = ((ref_22288 >> 48) & 0xFF) # Byte reference - MOV operation
ref_22292 = ((ref_22288 >> 40) & 0xFF) # Byte reference - MOV operation
ref_22293 = ((ref_22288 >> 32) & 0xFF) # Byte reference - MOV operation
ref_22294 = ((ref_22288 >> 24) & 0xFF) # Byte reference - MOV operation
ref_22295 = ((ref_22288 >> 16) & 0xFF) # Byte reference - MOV operation
ref_22296 = ((ref_22288 >> 8) & 0xFF) # Byte reference - MOV operation
ref_22297 = (ref_22288 & 0xFF) # Byte reference - MOV operation
ref_23448 = ((ref_22292) << 8 | ref_22293) # MOVZX operation
ref_23602 = (ref_23448 & 0xFFFF) # MOVZX operation
ref_24756 = ((ref_22294) << 8 | ref_22295) # MOVZX operation
ref_25898 = (ref_24756 & 0xFFFF) # MOVZX operation
ref_26064 = (ref_23602 & 0xFFFF) # MOVZX operation
ref_27206 = (ref_26064 & 0xFFFF) # MOVZX operation
ref_27208 = (((ref_27206 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_27209 = ((ref_27206 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_34180 = ref_10990 # MOV operation
ref_34960 = ref_20607 # MOV operation
ref_35108 = ref_34960 # MOV operation
ref_35114 = (0x1F & ref_35108) # AND operation
ref_35189 = ref_35114 # MOV operation
ref_35203 = ((ref_35189 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_35286 = ref_34180 # MOV operation
ref_35290 = ref_35203 # MOV operation
ref_35292 = (ref_35290 | ref_35286) # OR operation
ref_35375 = ref_35292 # MOV operation
ref_36725 = ref_35375 # MOV operation
ref_37505 = ref_35375 # MOV operation
ref_37653 = ref_37505 # MOV operation
ref_37659 = (0xF & ref_37653) # AND operation
ref_37734 = ref_37659 # MOV operation
ref_37748 = ((ref_37734 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_37831 = ref_36725 # MOV operation
ref_37835 = ref_37748 # MOV operation
ref_37837 = (ref_37835 | ref_37831) # OR operation
ref_37920 = ref_37837 # MOV operation
ref_39138 = ((ref_22290) << 8 | ref_22291) # MOVZX operation
ref_39292 = (ref_39138 & 0xFFFF) # MOVZX operation
ref_40446 = ((ref_22296) << 8 | ref_22297) # MOVZX operation
ref_41588 = (ref_40446 & 0xFFFF) # MOVZX operation
ref_41590 = (((ref_41588 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_41591 = ((ref_41588 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_41754 = (ref_39292 & 0xFFFF) # MOVZX operation
ref_42896 = (ref_41754 & 0xFFFF) # MOVZX operation
ref_44050 = (ref_42896 & 0xFFFF) # MOVZX operation
ref_44204 = (ref_44050 & 0xFFFF) # MOVZX operation
ref_45358 = (ref_25898 & 0xFFFF) # MOVZX operation
ref_46500 = (ref_45358 & 0xFFFF) # MOVZX operation
ref_46502 = (((ref_46500 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_46503 = ((ref_46500 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_46666 = (ref_44204 & 0xFFFF) # MOVZX operation
ref_47808 = (ref_46666 & 0xFFFF) # MOVZX operation
ref_47810 = (((ref_47808 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_47811 = ((ref_47808 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_49256 = ((((((((ref_41590) << 8 | ref_41591) << 8 | ref_47810) << 8 | ref_47811) << 8 | ref_27208) << 8 | ref_27209) << 8 | ref_46502) << 8 | ref_46503) # MOV operation
ref_49306 = ref_49256 # MOV operation
ref_49320 = (ref_49306 >> (0x2 & 0x3F)) # SHR operation
ref_49493 = ref_49320 # MOV operation
ref_49499 = (0xF & ref_49493) # AND operation
ref_49672 = ref_49499 # MOV operation
ref_49678 = (0x1 | ref_49672) # OR operation
ref_50393 = ref_20607 # MOV operation
ref_50443 = ref_50393 # MOV operation
ref_50455 = ref_49678 # MOV operation
ref_50457 = ((ref_50443 << ((ref_50455 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_51262 = ((((((((ref_41590) << 8 | ref_41591) << 8 | ref_47810) << 8 | ref_47811) << 8 | ref_27208) << 8 | ref_27209) << 8 | ref_46502) << 8 | ref_46503) # MOV operation
ref_51312 = ref_51262 # MOV operation
ref_51326 = (ref_51312 >> (0x2 & 0x3F)) # SHR operation
ref_51499 = ref_51326 # MOV operation
ref_51505 = (0xF & ref_51499) # AND operation
ref_51678 = ref_51505 # MOV operation
ref_51684 = (0x1 | ref_51678) # OR operation
ref_51861 = ref_51684 # MOV operation
ref_51863 = ((0x40 - ref_51861) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_51871 = ref_51863 # MOV operation
ref_52581 = ref_20607 # MOV operation
ref_52631 = ref_52581 # MOV operation
ref_52643 = ref_51871 # MOV operation
ref_52645 = (ref_52631 >> ((ref_52643 & 0xFF) & 0x3F)) # SHR operation
ref_52728 = ref_50457 # MOV operation
ref_52732 = ref_52645 # MOV operation
ref_52734 = (ref_52732 | ref_52728) # OR operation
ref_52809 = ref_52734 # MOV operation
ref_52823 = (ref_52809 >> (0x4 & 0x3F)) # SHR operation
ref_52996 = ref_52823 # MOV operation
ref_53002 = (0xF & ref_52996) # AND operation
ref_53175 = ref_53002 # MOV operation
ref_53181 = (0x1 | ref_53175) # OR operation
ref_53896 = ref_37920 # MOV operation
ref_54044 = ref_53896 # MOV operation
ref_54050 = (0xF & ref_54044) # AND operation
ref_54223 = ref_54050 # MOV operation
ref_54229 = (0x1 | ref_54223) # OR operation
ref_54944 = ref_9490 # MOV operation
ref_54994 = ref_54944 # MOV operation
ref_55006 = ref_54229 # MOV operation
ref_55008 = ((ref_54994 << ((ref_55006 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_55723 = ref_37920 # MOV operation
ref_55871 = ref_55723 # MOV operation
ref_55877 = (0xF & ref_55871) # AND operation
ref_56050 = ref_55877 # MOV operation
ref_56056 = (0x1 | ref_56050) # OR operation
ref_56233 = ref_56056 # MOV operation
ref_56235 = ((0x40 - ref_56233) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_56243 = ref_56235 # MOV operation
ref_56953 = ref_9490 # MOV operation
ref_57003 = ref_56953 # MOV operation
ref_57015 = ref_56243 # MOV operation
ref_57017 = (ref_57003 >> ((ref_57015 & 0xFF) & 0x3F)) # SHR operation
ref_57100 = ref_55008 # MOV operation
ref_57104 = ref_57017 # MOV operation
ref_57106 = (ref_57104 | ref_57100) # OR operation
ref_57181 = ref_57106 # MOV operation
ref_57193 = ref_53181 # MOV operation
ref_57195 = (ref_57181 >> ((ref_57193 & 0xFF) & 0x3F)) # SHR operation
ref_58090 = ((((((((ref_41590) << 8 | ref_41591) << 8 | ref_47810) << 8 | ref_47811) << 8 | ref_27208) << 8 | ref_27209) << 8 | ref_46502) << 8 | ref_46503) # MOV operation
ref_58140 = ref_58090 # MOV operation
ref_58154 = (ref_58140 >> (0x2 & 0x3F)) # SHR operation
ref_58327 = ref_58154 # MOV operation
ref_58333 = (0xF & ref_58327) # AND operation
ref_58506 = ref_58333 # MOV operation
ref_58512 = (0x1 | ref_58506) # OR operation
ref_59227 = ref_20607 # MOV operation
ref_59277 = ref_59227 # MOV operation
ref_59289 = ref_58512 # MOV operation
ref_59291 = ((ref_59277 << ((ref_59289 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_60096 = ((((((((ref_41590) << 8 | ref_41591) << 8 | ref_47810) << 8 | ref_47811) << 8 | ref_27208) << 8 | ref_27209) << 8 | ref_46502) << 8 | ref_46503) # MOV operation
ref_60146 = ref_60096 # MOV operation
ref_60160 = (ref_60146 >> (0x2 & 0x3F)) # SHR operation
ref_60333 = ref_60160 # MOV operation
ref_60339 = (0xF & ref_60333) # AND operation
ref_60512 = ref_60339 # MOV operation
ref_60518 = (0x1 | ref_60512) # OR operation
ref_60695 = ref_60518 # MOV operation
ref_60697 = ((0x40 - ref_60695) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_60705 = ref_60697 # MOV operation
ref_61415 = ref_20607 # MOV operation
ref_61465 = ref_61415 # MOV operation
ref_61477 = ref_60705 # MOV operation
ref_61479 = (ref_61465 >> ((ref_61477 & 0xFF) & 0x3F)) # SHR operation
ref_61562 = ref_59291 # MOV operation
ref_61566 = ref_61479 # MOV operation
ref_61568 = (ref_61566 | ref_61562) # OR operation
ref_61643 = ref_61568 # MOV operation
ref_61657 = (ref_61643 >> (0x4 & 0x3F)) # SHR operation
ref_61830 = ref_61657 # MOV operation
ref_61836 = (0xF & ref_61830) # AND operation
ref_62009 = ref_61836 # MOV operation
ref_62015 = (0x1 | ref_62009) # OR operation
ref_62192 = ref_62015 # MOV operation
ref_62194 = ((0x40 - ref_62192) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_62202 = ref_62194 # MOV operation
ref_62912 = ref_37920 # MOV operation
ref_63060 = ref_62912 # MOV operation
ref_63066 = (0xF & ref_63060) # AND operation
ref_63239 = ref_63066 # MOV operation
ref_63245 = (0x1 | ref_63239) # OR operation
ref_63960 = ref_9490 # MOV operation
ref_64010 = ref_63960 # MOV operation
ref_64022 = ref_63245 # MOV operation
ref_64024 = ((ref_64010 << ((ref_64022 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_64739 = ref_37920 # MOV operation
ref_64887 = ref_64739 # MOV operation
ref_64893 = (0xF & ref_64887) # AND operation
ref_65066 = ref_64893 # MOV operation
ref_65072 = (0x1 | ref_65066) # OR operation
ref_65249 = ref_65072 # MOV operation
ref_65251 = ((0x40 - ref_65249) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_65259 = ref_65251 # MOV operation
ref_65969 = ref_9490 # MOV operation
ref_66019 = ref_65969 # MOV operation
ref_66031 = ref_65259 # MOV operation
ref_66033 = (ref_66019 >> ((ref_66031 & 0xFF) & 0x3F)) # SHR operation
ref_66116 = ref_64024 # MOV operation
ref_66120 = ref_66033 # MOV operation
ref_66122 = (ref_66120 | ref_66116) # OR operation
ref_66197 = ref_66122 # MOV operation
ref_66209 = ref_62202 # MOV operation
ref_66211 = ((ref_66197 << ((ref_66209 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_66294 = ref_57195 # MOV operation
ref_66298 = ref_66211 # MOV operation
ref_66300 = (ref_66298 | ref_66294) # OR operation
ref_66383 = ref_66300 # MOV operation
ref_66542 = ref_66383 # MOV operation
ref_66544 = ref_66542 # MOV operation

print(ref_66544 & 0xffffffffffffffff)
