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
ref_6492 = ref_6416 # MOV operation
ref_6506 = (0x1F02C962 | ref_6492) # OR operation
ref_6731 = ref_6506 # MOV operation
ref_6737 = (0x1F8797B2 & ref_6731) # AND operation
ref_6846 = ref_6737 # MOV operation
ref_7764 = ref_6846 # MOV operation
ref_8577 = ref_278 # MOV operation
ref_8653 = ref_8577 # MOV operation
ref_8665 = ref_7764 # MOV operation
ref_8667 = (ref_8665 & ref_8653) # AND operation
ref_9598 = ref_8667 # MOV operation
ref_11338 = ref_9598 # MOV operation
ref_11538 = ref_11338 # MOV operation
ref_11546 = ((ref_11538 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_11553 = ref_11546 # MOV operation
ref_12471 = ref_9598 # MOV operation
ref_12671 = ref_12471 # MOV operation
ref_12679 = (ref_12671 >> (0x7 & 0x3F)) # SHR operation
ref_12686 = ref_12679 # MOV operation
ref_12782 = ref_12686 # MOV operation
ref_12794 = ref_11553 # MOV operation
ref_12796 = (ref_12794 | ref_12782) # OR operation
ref_13750 = ref_278 # MOV operation
ref_13826 = ref_13750 # MOV operation
ref_13840 = (((sx(0x40, 0x66AF1DF) * sx(0x40, ref_13826)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_13938 = ref_13840 # MOV operation
ref_13950 = ref_12796 # MOV operation
ref_13952 = ((ref_13950 + ref_13938) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_14062 = ref_13952 # MOV operation
ref_22606 = ref_14062 # MOV operation
ref_23824 = ref_14062 # MOV operation
ref_23900 = ref_23824 # MOV operation
ref_23912 = ref_22606 # MOV operation
ref_23914 = ((ref_23912 + ref_23900) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_24846 = ref_23914 # MOV operation
ref_27110 = ref_9598 # MOV operation
ref_27310 = ref_27110 # MOV operation
ref_27316 = (0x7 & ref_27310) # AND operation
ref_27417 = ref_27316 # MOV operation
ref_27431 = ((ref_27417 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_28674 = ref_14062 # MOV operation
ref_28750 = ref_28674 # MOV operation
ref_28762 = ref_27431 # MOV operation
ref_28764 = (ref_28762 | ref_28750) # OR operation
ref_28873 = ref_28764 # MOV operation
ref_28875 = ((ref_28873 >> 56) & 0xFF) # Byte reference - MOV operation
ref_28876 = ((ref_28873 >> 48) & 0xFF) # Byte reference - MOV operation
ref_28877 = ((ref_28873 >> 40) & 0xFF) # Byte reference - MOV operation
ref_28878 = ((ref_28873 >> 32) & 0xFF) # Byte reference - MOV operation
ref_28879 = ((ref_28873 >> 24) & 0xFF) # Byte reference - MOV operation
ref_28880 = ((ref_28873 >> 16) & 0xFF) # Byte reference - MOV operation
ref_28881 = ((ref_28873 >> 8) & 0xFF) # Byte reference - MOV operation
ref_28882 = (ref_28873 & 0xFF) # Byte reference - MOV operation
ref_30717 = ref_28875 # MOVZX operation
ref_30921 = (ref_30717 & 0xFF) # MOVZX operation
ref_32757 = ref_28882 # MOVZX operation
ref_34581 = (ref_32757 & 0xFF) # MOVZX operation
ref_34583 = (ref_34581 & 0xFF) # Byte reference - MOV operation
ref_34797 = (ref_30921 & 0xFF) # MOVZX operation
ref_36621 = (ref_34797 & 0xFF) # MOVZX operation
ref_36623 = (ref_36621 & 0xFF) # Byte reference - MOV operation
ref_38557 = ref_9598 # MOV operation
ref_39775 = ((((((((ref_34583) << 8 | ref_28876) << 8 | ref_28877) << 8 | ref_28878) << 8 | ref_28879) << 8 | ref_28880) << 8 | ref_28881) << 8 | ref_36623) # MOV operation
ref_39851 = ref_39775 # MOV operation
ref_39863 = ref_38557 # MOV operation
ref_39865 = (ref_39863 & ref_39851) # AND operation
ref_40090 = ref_39865 # MOV operation
ref_40096 = (0x1F & ref_40090) # AND operation
ref_40197 = ref_40096 # MOV operation
ref_40211 = ((ref_40197 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_41134 = ref_6846 # MOV operation
ref_41210 = ref_41134 # MOV operation
ref_41222 = ref_40211 # MOV operation
ref_41224 = (ref_41222 | ref_41210) # OR operation
ref_41333 = ref_41224 # MOV operation
ref_43876 = ref_24846 # MOV operation
ref_45094 = ref_24846 # MOV operation
ref_45170 = ref_45094 # MOV operation
ref_45182 = ref_43876 # MOV operation
ref_45184 = ((ref_45182 + ref_45170) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_46116 = ref_45184 # MOV operation
ref_48380 = ((((((((ref_34583) << 8 | ref_28876) << 8 | ref_28877) << 8 | ref_28878) << 8 | ref_28879) << 8 | ref_28880) << 8 | ref_28881) << 8 | ref_36623) # MOV operation
ref_48580 = ref_48380 # MOV operation
ref_48586 = (0x7 & ref_48580) # AND operation
ref_48687 = ref_48586 # MOV operation
ref_48701 = ((ref_48687 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_49944 = ref_46116 # MOV operation
ref_50020 = ref_49944 # MOV operation
ref_50032 = ref_48701 # MOV operation
ref_50034 = (ref_50032 | ref_50020) # OR operation
ref_50143 = ref_50034 # MOV operation
ref_50145 = ((ref_50143 >> 56) & 0xFF) # Byte reference - MOV operation
ref_50146 = ((ref_50143 >> 48) & 0xFF) # Byte reference - MOV operation
ref_50147 = ((ref_50143 >> 40) & 0xFF) # Byte reference - MOV operation
ref_50148 = ((ref_50143 >> 32) & 0xFF) # Byte reference - MOV operation
ref_50149 = ((ref_50143 >> 24) & 0xFF) # Byte reference - MOV operation
ref_50150 = ((ref_50143 >> 16) & 0xFF) # Byte reference - MOV operation
ref_50151 = ((ref_50143 >> 8) & 0xFF) # Byte reference - MOV operation
ref_50152 = (ref_50143 & 0xFF) # Byte reference - MOV operation
ref_51987 = ref_50145 # MOVZX operation
ref_52191 = (ref_51987 & 0xFF) # MOVZX operation
ref_54027 = ref_50152 # MOVZX operation
ref_55851 = (ref_54027 & 0xFF) # MOVZX operation
ref_55853 = (ref_55851 & 0xFF) # Byte reference - MOV operation
ref_56067 = (ref_52191 & 0xFF) # MOVZX operation
ref_57891 = (ref_56067 & 0xFF) # MOVZX operation
ref_57893 = (ref_57891 & 0xFF) # Byte reference - MOV operation
ref_59827 = ((((((((ref_34583) << 8 | ref_28876) << 8 | ref_28877) << 8 | ref_28878) << 8 | ref_28879) << 8 | ref_28880) << 8 | ref_28881) << 8 | ref_36623) # MOV operation
ref_61045 = ((((((((ref_55853) << 8 | ref_50146) << 8 | ref_50147) << 8 | ref_50148) << 8 | ref_50149) << 8 | ref_50150) << 8 | ref_50151) << 8 | ref_57893) # MOV operation
ref_61121 = ref_61045 # MOV operation
ref_61133 = ref_59827 # MOV operation
ref_61135 = (ref_61133 & ref_61121) # AND operation
ref_61360 = ref_61135 # MOV operation
ref_61366 = (0x1F & ref_61360) # AND operation
ref_61467 = ref_61366 # MOV operation
ref_61481 = ((ref_61467 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_62404 = ref_41333 # MOV operation
ref_62480 = ref_62404 # MOV operation
ref_62492 = ref_61481 # MOV operation
ref_62494 = (ref_62492 | ref_62480) # OR operation
ref_62603 = ref_62494 # MOV operation
ref_65965 = ((((((((ref_55853) << 8 | ref_50146) << 8 | ref_50147) << 8 | ref_50148) << 8 | ref_50149) << 8 | ref_50150) << 8 | ref_50151) << 8 | ref_57893) # MOV operation
ref_66863 = ((((((((ref_34583) << 8 | ref_28876) << 8 | ref_28877) << 8 | ref_28878) << 8 | ref_28879) << 8 | ref_28880) << 8 | ref_28881) << 8 | ref_36623) # MOV operation
ref_66939 = ref_66863 # MOV operation
ref_66951 = ref_65965 # MOV operation
ref_66953 = (ref_66951 | ref_66939) # OR operation
ref_67178 = ref_66953 # MOV operation
ref_67184 = (0xF & ref_67178) # AND operation
ref_67285 = ref_67184 # MOV operation
ref_67299 = (0x1 | ref_67285) # OR operation
ref_67412 = ref_67299 # MOV operation
ref_67414 = ((0x40 - ref_67412) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_67422 = ref_67414 # MOV operation
ref_68340 = ref_62603 # MOV operation
ref_69470 = ref_9598 # MOV operation
ref_69546 = ref_69470 # MOV operation
ref_69560 = (ref_69546 >> (0x1 & 0x3F)) # SHR operation
ref_69785 = ref_69560 # MOV operation
ref_69791 = (0xF & ref_69785) # AND operation
ref_70016 = ref_69791 # MOV operation
ref_70022 = (0x1 | ref_70016) # OR operation
ref_70135 = ref_70022 # MOV operation
ref_70137 = ((0x40 - ref_70135) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_70145 = ref_70137 # MOV operation
ref_70249 = ref_68340 # MOV operation
ref_70253 = ref_70145 # MOV operation
ref_70255 = (ref_70253 & 0xFFFFFFFF) # MOV operation
ref_70257 = ((ref_70249 << ((ref_70255 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_70264 = ref_70257 # MOV operation
ref_71298 = ref_9598 # MOV operation
ref_71374 = ref_71298 # MOV operation
ref_71388 = (ref_71374 >> (0x1 & 0x3F)) # SHR operation
ref_71613 = ref_71388 # MOV operation
ref_71619 = (0xF & ref_71613) # AND operation
ref_71844 = ref_71619 # MOV operation
ref_71850 = (0x1 | ref_71844) # OR operation
ref_72773 = ref_62603 # MOV operation
ref_72849 = ref_72773 # MOV operation
ref_72861 = ref_71850 # MOV operation
ref_72863 = (ref_72849 >> ((ref_72861 & 0xFF) & 0x3F)) # SHR operation
ref_72964 = ref_72863 # MOV operation
ref_72976 = ref_70264 # MOV operation
ref_72978 = (ref_72976 | ref_72964) # OR operation
ref_73079 = ref_72978 # MOV operation
ref_73091 = ref_67422 # MOV operation
ref_73093 = (ref_73079 >> ((ref_73091 & 0xFF) & 0x3F)) # SHR operation
ref_74248 = ref_9598 # MOV operation
ref_74324 = ref_74248 # MOV operation
ref_74338 = (ref_74324 >> (0x1 & 0x3F)) # SHR operation
ref_74563 = ref_74338 # MOV operation
ref_74569 = (0xF & ref_74563) # AND operation
ref_74794 = ref_74569 # MOV operation
ref_74800 = (0x1 | ref_74794) # OR operation
ref_74913 = ref_74800 # MOV operation
ref_74915 = ((0x40 - ref_74913) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_74923 = ref_74915 # MOV operation
ref_75841 = ref_62603 # MOV operation
ref_75917 = ref_75841 # MOV operation
ref_75929 = ref_74923 # MOV operation
ref_75931 = ((ref_75917 << ((ref_75929 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_77086 = ref_9598 # MOV operation
ref_77162 = ref_77086 # MOV operation
ref_77176 = (ref_77162 >> (0x1 & 0x3F)) # SHR operation
ref_77401 = ref_77176 # MOV operation
ref_77407 = (0xF & ref_77401) # AND operation
ref_77508 = ref_77407 # MOV operation
ref_77522 = (0x1 | ref_77508) # OR operation
ref_78445 = ref_62603 # MOV operation
ref_78521 = ref_78445 # MOV operation
ref_78533 = ref_77522 # MOV operation
ref_78535 = (ref_78521 >> ((ref_78533 & 0xFF) & 0x3F)) # SHR operation
ref_78636 = ref_78535 # MOV operation
ref_78648 = ref_75931 # MOV operation
ref_78650 = (ref_78648 | ref_78636) # OR operation
ref_79573 = ((((((((ref_34583) << 8 | ref_28876) << 8 | ref_28877) << 8 | ref_28878) << 8 | ref_28879) << 8 | ref_28880) << 8 | ref_28881) << 8 | ref_36623) # MOV operation
ref_80471 = ((((((((ref_55853) << 8 | ref_50146) << 8 | ref_50147) << 8 | ref_50148) << 8 | ref_50149) << 8 | ref_50150) << 8 | ref_50151) << 8 | ref_57893) # MOV operation
ref_80555 = ref_79573 # MOV operation
ref_80559 = ref_80471 # MOV operation
ref_80561 = (ref_80559 | ref_80555) # OR operation
ref_80786 = ref_80561 # MOV operation
ref_80792 = (0xF & ref_80786) # AND operation
ref_81017 = ref_80792 # MOV operation
ref_81023 = (0x1 | ref_81017) # OR operation
ref_81132 = ref_78650 # MOV operation
ref_81136 = ref_81023 # MOV operation
ref_81138 = (ref_81136 & 0xFFFFFFFF) # MOV operation
ref_81140 = ((ref_81132 << ((ref_81138 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_81147 = ref_81140 # MOV operation
ref_81243 = ref_81147 # MOV operation
ref_81255 = ref_73093 # MOV operation
ref_81257 = (ref_81255 | ref_81243) # OR operation
ref_81366 = ref_81257 # MOV operation
ref_81577 = ref_81366 # MOV operation
ref_81579 = ref_81577 # MOV operation

print(ref_81579 & 0xffffffffffffffff)
