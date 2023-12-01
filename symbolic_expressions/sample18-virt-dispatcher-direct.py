#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])

ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_13742 = ref_278 # MOV operation
ref_13878 = ref_13742 # MOV operation
ref_13886 = ((ref_13878 << (0x33 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_13893 = ref_13886 # MOV operation
ref_14470 = ref_278 # MOV operation
ref_14606 = ref_14470 # MOV operation
ref_14614 = (ref_14606 >> (0xD & 0x3F)) # SHR operation
ref_14621 = ref_14614 # MOV operation
ref_14685 = ref_14621 # MOV operation
ref_14697 = ref_13893 # MOV operation
ref_14699 = (ref_14697 | ref_14685) # OR operation
ref_14768 = ref_14699 # MOV operation
ref_14782 = ((0x2EA4A1C39AF5800 + ref_14768) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_14860 = ref_14782 # MOV operation
ref_16120 = ref_14860 # MOV operation
ref_16677 = ref_278 # MOV operation
ref_16721 = ref_16677 # MOV operation
ref_16733 = ref_16120 # MOV operation
ref_16735 = ((ref_16721 - ref_16733) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_16743 = ref_16735 # MOV operation
ref_16815 = ref_16743 # MOV operation
ref_17990 = ref_278 # MOV operation
ref_18126 = ref_17990 # MOV operation
ref_18134 = (ref_18126 >> (0x37 & 0x3F)) # SHR operation
ref_18141 = ref_18134 # MOV operation
ref_18718 = ref_278 # MOV operation
ref_18854 = ref_18718 # MOV operation
ref_18862 = ((ref_18854 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_18869 = ref_18862 # MOV operation
ref_18933 = ref_18869 # MOV operation
ref_18945 = ref_18141 # MOV operation
ref_18947 = (ref_18945 | ref_18933) # OR operation
ref_19024 = ref_18947 # MOV operation
ref_20283 = ref_278 # MOV operation
ref_20327 = ref_20283 # MOV operation
ref_20341 = (0x3E908497 | ref_20327) # OR operation
ref_20418 = ref_20341 # MOV operation
ref_21139 = ref_20418 # MOV operation
ref_21781 = ref_19024 # MOV operation
ref_21825 = ref_21781 # MOV operation
ref_21837 = ref_21139 # MOV operation
ref_21839 = ((ref_21825 - ref_21837) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_21847 = ref_21839 # MOV operation
ref_22509 = ref_14860 # MOV operation
ref_23235 = ref_16815 # MOV operation
ref_23371 = ref_23235 # MOV operation
ref_23379 = (ref_23371 >> (0x2 & 0x3F)) # SHR operation
ref_23386 = ref_23379 # MOV operation
ref_23542 = ref_23386 # MOV operation
ref_23548 = (0xF & ref_23542) # AND operation
ref_23617 = ref_23548 # MOV operation
ref_23631 = (0x1 | ref_23617) # OR operation
ref_23796 = ref_23631 # MOV operation
ref_23798 = ((0x40 - ref_23796) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_23806 = ref_23798 # MOV operation
ref_23878 = ref_22509 # MOV operation
ref_23882 = ref_23806 # MOV operation
ref_23884 = (ref_23882 & 0xFFFFFFFF) # MOV operation
ref_23886 = ((ref_23878 << ((ref_23884 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_23893 = ref_23886 # MOV operation
ref_24555 = ref_14860 # MOV operation
ref_25281 = ref_16815 # MOV operation
ref_25417 = ref_25281 # MOV operation
ref_25425 = (ref_25417 >> (0x2 & 0x3F)) # SHR operation
ref_25432 = ref_25425 # MOV operation
ref_25588 = ref_25432 # MOV operation
ref_25594 = (0xF & ref_25588) # AND operation
ref_25663 = ref_25594 # MOV operation
ref_25677 = (0x1 | ref_25663) # OR operation
ref_25754 = ref_24555 # MOV operation
ref_25758 = ref_25677 # MOV operation
ref_25760 = (ref_25758 & 0xFFFFFFFF) # MOV operation
ref_25762 = (ref_25754 >> ((ref_25760 & 0xFF) & 0x3F)) # SHR operation
ref_25769 = ref_25762 # MOV operation
ref_25833 = ref_25769 # MOV operation
ref_25845 = ref_23893 # MOV operation
ref_25847 = (ref_25845 | ref_25833) # OR operation
ref_25916 = ref_25847 # MOV operation
ref_25928 = ref_21847 # MOV operation
ref_25930 = ((ref_25916 - ref_25928) & 0xFFFFFFFFFFFFFFFF) # CMP operation
ref_25932 = ((((ref_25916 ^ (ref_25928 ^ ref_25930)) ^ ((ref_25916 ^ ref_25930) & (ref_25916 ^ ref_25928))) >> 63) & 0x1) # Carry flag
ref_25938 = ((((ref_25928 >> 8) & 0xFFFFFFFFFFFFFF)) << 8 | (0x1 if (ref_25932 == 0x1) else 0x0)) # SETB operation
ref_25940 = (ref_25938 & 0xFF) # MOVZX operation
ref_25996 = (ref_25940 & 0xFFFFFFFF) # MOV operation
ref_25998 = ((ref_25996 & 0xFFFFFFFF) & (ref_25996 & 0xFFFFFFFF)) # TEST operation
ref_26003 = (0x1 if (ref_25998 == 0x0) else 0x0) # Zero flag
ref_26005 = (0x3E32 if (ref_26003 == 0x1) else 0x3E10) # Program Counter


if (ref_26003 == 0x1):
    ref_45536 = SymVar_0
    ref_45551 = ref_45536 # MOV operation
    ref_59020 = ref_45551 # MOV operation
    ref_59156 = ref_59020 # MOV operation
    ref_59164 = ((ref_59156 << (0x33 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_59171 = ref_59164 # MOV operation
    ref_59748 = ref_45551 # MOV operation
    ref_59884 = ref_59748 # MOV operation
    ref_59892 = (ref_59884 >> (0xD & 0x3F)) # SHR operation
    ref_59899 = ref_59892 # MOV operation
    ref_59963 = ref_59899 # MOV operation
    ref_59975 = ref_59171 # MOV operation
    ref_59977 = (ref_59975 | ref_59963) # OR operation
    ref_60046 = ref_59977 # MOV operation
    ref_60060 = ((0x2EA4A1C39AF5800 + ref_60046) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_60138 = ref_60060 # MOV operation
    ref_61398 = ref_60138 # MOV operation
    ref_61955 = ref_45551 # MOV operation
    ref_61999 = ref_61955 # MOV operation
    ref_62011 = ref_61398 # MOV operation
    ref_62013 = ((ref_61999 - ref_62011) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_62021 = ref_62013 # MOV operation
    ref_62093 = ref_62021 # MOV operation
    ref_63268 = ref_45551 # MOV operation
    ref_63404 = ref_63268 # MOV operation
    ref_63412 = (ref_63404 >> (0x37 & 0x3F)) # SHR operation
    ref_63419 = ref_63412 # MOV operation
    ref_63996 = ref_45551 # MOV operation
    ref_64132 = ref_63996 # MOV operation
    ref_64140 = ((ref_64132 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_64147 = ref_64140 # MOV operation
    ref_64211 = ref_64147 # MOV operation
    ref_64223 = ref_63419 # MOV operation
    ref_64225 = (ref_64223 | ref_64211) # OR operation
    ref_64302 = ref_64225 # MOV operation
    ref_65561 = ref_45551 # MOV operation
    ref_65605 = ref_65561 # MOV operation
    ref_65619 = (0x3E908497 | ref_65605) # OR operation
    ref_65696 = ref_65619 # MOV operation
    ref_72535 = ref_60138 # MOV operation
    ref_73261 = ref_62093 # MOV operation
    ref_73397 = ref_73261 # MOV operation
    ref_73405 = (ref_73397 >> (0x4 & 0x3F)) # SHR operation
    ref_73412 = ref_73405 # MOV operation
    ref_73568 = ref_73412 # MOV operation
    ref_73574 = (0xF & ref_73568) # AND operation
    ref_73643 = ref_73574 # MOV operation
    ref_73657 = (0x1 | ref_73643) # OR operation
    ref_73822 = ref_73657 # MOV operation
    ref_73824 = ((0x40 - ref_73822) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_73832 = ref_73824 # MOV operation
    ref_73904 = ref_72535 # MOV operation
    ref_73908 = ref_73832 # MOV operation
    ref_73910 = (ref_73908 & 0xFFFFFFFF) # MOV operation
    ref_73912 = (ref_73904 >> ((ref_73910 & 0xFF) & 0x3F)) # SHR operation
    ref_73919 = ref_73912 # MOV operation
    ref_74581 = ref_60138 # MOV operation
    ref_75307 = ref_62093 # MOV operation
    ref_75443 = ref_75307 # MOV operation
    ref_75451 = (ref_75443 >> (0x4 & 0x3F)) # SHR operation
    ref_75458 = ref_75451 # MOV operation
    ref_75614 = ref_75458 # MOV operation
    ref_75620 = (0xF & ref_75614) # AND operation
    ref_75689 = ref_75620 # MOV operation
    ref_75703 = (0x1 | ref_75689) # OR operation
    ref_75780 = ref_74581 # MOV operation
    ref_75784 = ref_75703 # MOV operation
    ref_75786 = (ref_75784 & 0xFFFFFFFF) # MOV operation
    ref_75788 = ((ref_75780 << ((ref_75786 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_75795 = ref_75788 # MOV operation
    ref_75859 = ref_75795 # MOV operation
    ref_75871 = ref_73919 # MOV operation
    ref_75873 = (ref_75871 | ref_75859) # OR operation
    ref_76624 = ref_65696 # MOV operation
    ref_77266 = ref_64302 # MOV operation
    ref_77310 = ref_77266 # MOV operation
    ref_77322 = ref_76624 # MOV operation
    ref_77324 = (ref_77322 | ref_77310) # OR operation
    ref_77485 = ref_77324 # MOV operation
    ref_77493 = (ref_77485 >> (0x4 & 0x3F)) # SHR operation
    ref_77500 = ref_77493 # MOV operation
    ref_77656 = ref_77500 # MOV operation
    ref_77662 = (0x7 & ref_77656) # AND operation
    ref_77731 = ref_77662 # MOV operation
    ref_77745 = (0x1 | ref_77731) # OR operation
    ref_77822 = ref_75873 # MOV operation
    ref_77826 = ref_77745 # MOV operation
    ref_77828 = (ref_77826 & 0xFFFFFFFF) # MOV operation
    ref_77830 = (ref_77822 >> ((ref_77828 & 0xFF) & 0x3F)) # SHR operation
    ref_77837 = ref_77830 # MOV operation
    ref_77909 = ref_77837 # MOV operation
    ref_78063 = ref_77909 # MOV operation
    ref_78065 = ref_78063 # MOV operation
    endb = ref_78065


else:
    ref_263 = SymVar_0
    ref_278 = ref_263 # MOV operation
    ref_13742 = ref_278 # MOV operation
    ref_13878 = ref_13742 # MOV operation
    ref_13886 = ((ref_13878 << (0x33 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_13893 = ref_13886 # MOV operation
    ref_14470 = ref_278 # MOV operation
    ref_14606 = ref_14470 # MOV operation
    ref_14614 = (ref_14606 >> (0xD & 0x3F)) # SHR operation
    ref_14621 = ref_14614 # MOV operation
    ref_14685 = ref_14621 # MOV operation
    ref_14697 = ref_13893 # MOV operation
    ref_14699 = (ref_14697 | ref_14685) # OR operation
    ref_14768 = ref_14699 # MOV operation
    ref_14782 = ((0x2EA4A1C39AF5800 + ref_14768) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_14860 = ref_14782 # MOV operation
    ref_16120 = ref_14860 # MOV operation
    ref_16677 = ref_278 # MOV operation
    ref_16721 = ref_16677 # MOV operation
    ref_16733 = ref_16120 # MOV operation
    ref_16735 = ((ref_16721 - ref_16733) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_16743 = ref_16735 # MOV operation
    ref_16815 = ref_16743 # MOV operation
    ref_16817 = ((ref_16815 >> 56) & 0xFF) # Byte reference - MOV operation
    ref_16818 = ((ref_16815 >> 48) & 0xFF) # Byte reference - MOV operation
    ref_16819 = ((ref_16815 >> 40) & 0xFF) # Byte reference - MOV operation
    ref_16820 = ((ref_16815 >> 32) & 0xFF) # Byte reference - MOV operation
    ref_16821 = ((ref_16815 >> 24) & 0xFF) # Byte reference - MOV operation
    ref_16822 = ((ref_16815 >> 16) & 0xFF) # Byte reference - MOV operation
    ref_16823 = ((ref_16815 >> 8) & 0xFF) # Byte reference - MOV operation
    ref_16824 = (ref_16815 & 0xFF) # Byte reference - MOV operation
    ref_17990 = ref_278 # MOV operation
    ref_18126 = ref_17990 # MOV operation
    ref_18134 = (ref_18126 >> (0x37 & 0x3F)) # SHR operation
    ref_18141 = ref_18134 # MOV operation
    ref_18718 = ref_278 # MOV operation
    ref_18854 = ref_18718 # MOV operation
    ref_18862 = ((ref_18854 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_18869 = ref_18862 # MOV operation
    ref_18933 = ref_18869 # MOV operation
    ref_18945 = ref_18141 # MOV operation
    ref_18947 = (ref_18945 | ref_18933) # OR operation
    ref_19024 = ref_18947 # MOV operation
    ref_20283 = ref_278 # MOV operation
    ref_20327 = ref_20283 # MOV operation
    ref_20341 = (0x3E908497 | ref_20327) # OR operation
    ref_20418 = ref_20341 # MOV operation
    ref_27104 = ((((ref_16817) << 8 | ref_16818) << 8 | ref_16819) << 8 | ref_16820) # MOV operation
    ref_27248 = (ref_27104 & 0xFFFFFFFF) # MOV operation
    ref_28320 = ((((ref_16821) << 8 | ref_16822) << 8 | ref_16823) << 8 | ref_16824) # MOV operation
    ref_29380 = (ref_28320 & 0xFFFFFFFF) # MOV operation
    ref_29382 = (((ref_29380 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
    ref_29383 = (((ref_29380 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
    ref_29384 = (((ref_29380 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
    ref_29385 = ((ref_29380 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
    ref_29536 = (ref_27248 & 0xFFFFFFFF) # MOV operation
    ref_30596 = (ref_29536 & 0xFFFFFFFF) # MOV operation
    ref_30598 = (((ref_30596 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
    ref_30599 = (((ref_30596 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
    ref_30600 = (((ref_30596 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
    ref_30601 = ((ref_30596 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
    ref_31852 = ref_14860 # MOV operation
    ref_31988 = ref_31852 # MOV operation
    ref_31994 = (0x3F & ref_31988) # AND operation
    ref_32155 = ref_31994 # MOV operation
    ref_32163 = ((ref_32155 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_32170 = ref_32163 # MOV operation
    ref_32832 = ref_14860 # MOV operation
    ref_32876 = ref_32832 # MOV operation
    ref_32888 = ref_32170 # MOV operation
    ref_32890 = (ref_32888 | ref_32876) # OR operation
    ref_32967 = ref_32890 # MOV operation
    ref_34227 = ref_32967 # MOV operation
    ref_34363 = ref_34227 # MOV operation
    ref_34369 = (0x1F & ref_34363) # AND operation
    ref_34530 = ref_34369 # MOV operation
    ref_34538 = ((ref_34530 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_34545 = ref_34538 # MOV operation
    ref_35207 = ref_20418 # MOV operation
    ref_35251 = ref_35207 # MOV operation
    ref_35263 = ref_34545 # MOV operation
    ref_35265 = (ref_35263 | ref_35251) # OR operation
    ref_35342 = ref_35265 # MOV operation
    ref_36602 = ref_19024 # MOV operation
    ref_37244 = ref_32967 # MOV operation
    ref_37288 = ref_37244 # MOV operation
    ref_37300 = ref_36602 # MOV operation
    ref_37302 = ((ref_37300 + ref_37288) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_37464 = ref_37302 # MOV operation
    ref_37470 = (0x1F & ref_37464) # AND operation
    ref_37631 = ref_37470 # MOV operation
    ref_37639 = ((ref_37631 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_37646 = ref_37639 # MOV operation
    ref_38308 = ref_32967 # MOV operation
    ref_38352 = ref_38308 # MOV operation
    ref_38364 = ref_37646 # MOV operation
    ref_38366 = (ref_38364 | ref_38352) # OR operation
    ref_38443 = ref_38366 # MOV operation
    ref_39686 = ref_38443 # MOV operation
    ref_40412 = ((((((((ref_29382) << 8 | ref_29383) << 8 | ref_29384) << 8 | ref_29385) << 8 | ref_30598) << 8 | ref_30599) << 8 | ref_30600) << 8 | ref_30601) # MOV operation
    ref_40548 = ref_40412 # MOV operation
    ref_40556 = (ref_40548 >> (0x4 & 0x3F)) # SHR operation
    ref_40563 = ref_40556 # MOV operation
    ref_40719 = ref_40563 # MOV operation
    ref_40725 = (0xF & ref_40719) # AND operation
    ref_40794 = ref_40725 # MOV operation
    ref_40808 = (0x1 | ref_40794) # OR operation
    ref_40973 = ref_40808 # MOV operation
    ref_40975 = ((0x40 - ref_40973) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_40983 = ref_40975 # MOV operation
    ref_41055 = ref_39686 # MOV operation
    ref_41059 = ref_40983 # MOV operation
    ref_41061 = (ref_41059 & 0xFFFFFFFF) # MOV operation
    ref_41063 = (ref_41055 >> ((ref_41061 & 0xFF) & 0x3F)) # SHR operation
    ref_41070 = ref_41063 # MOV operation
    ref_41732 = ref_38443 # MOV operation
    ref_42458 = ((((((((ref_29382) << 8 | ref_29383) << 8 | ref_29384) << 8 | ref_29385) << 8 | ref_30598) << 8 | ref_30599) << 8 | ref_30600) << 8 | ref_30601) # MOV operation
    ref_42594 = ref_42458 # MOV operation
    ref_42602 = (ref_42594 >> (0x4 & 0x3F)) # SHR operation
    ref_42609 = ref_42602 # MOV operation
    ref_42765 = ref_42609 # MOV operation
    ref_42771 = (0xF & ref_42765) # AND operation
    ref_42840 = ref_42771 # MOV operation
    ref_42854 = (0x1 | ref_42840) # OR operation
    ref_42931 = ref_41732 # MOV operation
    ref_42935 = ref_42854 # MOV operation
    ref_42937 = (ref_42935 & 0xFFFFFFFF) # MOV operation
    ref_42939 = ((ref_42931 << ((ref_42937 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_42946 = ref_42939 # MOV operation
    ref_43010 = ref_42946 # MOV operation
    ref_43022 = ref_41070 # MOV operation
    ref_43024 = (ref_43022 | ref_43010) # OR operation
    ref_43775 = ref_35342 # MOV operation
    ref_44417 = ref_19024 # MOV operation
    ref_44461 = ref_44417 # MOV operation
    ref_44473 = ref_43775 # MOV operation
    ref_44475 = (ref_44473 | ref_44461) # OR operation
    ref_44636 = ref_44475 # MOV operation
    ref_44644 = (ref_44636 >> (0x4 & 0x3F)) # SHR operation
    ref_44651 = ref_44644 # MOV operation
    ref_44807 = ref_44651 # MOV operation
    ref_44813 = (0x7 & ref_44807) # AND operation
    ref_44882 = ref_44813 # MOV operation
    ref_44896 = (0x1 | ref_44882) # OR operation
    ref_44973 = ref_43024 # MOV operation
    ref_44977 = ref_44896 # MOV operation
    ref_44979 = (ref_44977 & 0xFFFFFFFF) # MOV operation
    ref_44981 = (ref_44973 >> ((ref_44979 & 0xFF) & 0x3F)) # SHR operation
    ref_44988 = ref_44981 # MOV operation
    ref_45060 = ref_44988 # MOV operation
    ref_45214 = ref_45060 # MOV operation
    ref_45216 = ref_45214 # MOV operation
    endb = ref_45216


print(endb & 0xffffffffffffffff)
