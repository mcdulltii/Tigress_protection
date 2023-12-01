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
ref_6506 = ((ref_6492 << (0xD & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_7460 = ref_278 # MOV operation
ref_7536 = ref_7460 # MOV operation
ref_7550 = (ref_7536 >> (0x33 & 0x3F)) # SHR operation
ref_7659 = ref_6506 # MOV operation
ref_7663 = ref_7550 # MOV operation
ref_7665 = (ref_7663 | ref_7659) # OR operation
ref_7774 = ref_7665 # MOV operation
ref_9545 = ref_278 # MOV operation
ref_9621 = ref_9545 # MOV operation
ref_9637 = ((((0x0) << 64 | ref_9621) / 0x6) & 0xFFFFFFFFFFFFFFFF) # DIV operation
ref_9858 = ref_9637 # MOV operation
ref_9864 = (((sx(0x40, 0xFA0000000002C90C) * sx(0x40, ref_9858)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_9970 = ref_9864 # MOV operation
ref_11710 = ref_7774 # MOV operation
ref_12608 = ref_9970 # MOV operation
ref_12692 = ref_11710 # MOV operation
ref_12696 = ref_12608 # MOV operation
ref_12698 = (ref_12696 | ref_12692) # OR operation
ref_13536 = ref_278 # MOV operation
ref_13612 = ref_13536 # MOV operation
ref_13624 = ref_12698 # MOV operation
ref_13626 = ((ref_13624 + ref_13612) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_13736 = ref_13626 # MOV operation
ref_15708 = ref_7774 # MOV operation
ref_15908 = ref_15708 # MOV operation
ref_15914 = ((ref_15908 - 0x2ED5CD7E) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_15922 = ref_15914 # MOV operation
ref_16030 = ref_15922 # MOV operation
ref_16032 = ((0x28E5FC28 - ref_16030) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_16040 = ref_16032 # MOV operation
ref_16136 = ref_16040 # MOV operation
ref_16150 = (ref_16136 >> (0x2 & 0x3F)) # SHR operation
ref_16375 = ref_16150 # MOV operation
ref_16381 = (0x7 & ref_16375) # AND operation
ref_16606 = ref_16381 # MOV operation
ref_16612 = (0x1 | ref_16606) # OR operation
ref_17535 = ref_9970 # MOV operation
ref_18348 = ref_278 # MOV operation
ref_18424 = ref_18348 # MOV operation
ref_18436 = ref_17535 # MOV operation
ref_18438 = ((ref_18436 + ref_18424) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_18540 = ref_18438 # MOV operation
ref_18552 = ref_16612 # MOV operation
ref_18554 = (ref_18540 >> ((ref_18552 & 0xFF) & 0x3F)) # SHR operation
ref_18663 = ref_18554 # MOV operation
ref_20519 = ref_18663 # MOV operation
ref_20595 = ref_20519 # MOV operation
ref_20609 = (ref_20595 >> (0x1 & 0x3F)) # SHR operation
ref_20834 = ref_20609 # MOV operation
ref_20840 = (0x7 & ref_20834) # AND operation
ref_21065 = ref_20840 # MOV operation
ref_21071 = (0x1 | ref_21065) # OR operation
ref_21994 = ref_18663 # MOV operation
ref_22070 = ref_21994 # MOV operation
ref_22082 = ref_21071 # MOV operation
ref_22084 = (ref_22070 >> ((ref_22082 & 0xFF) & 0x3F)) # SHR operation
ref_22193 = ref_22084 # MOV operation
ref_22195 = ((ref_22193 >> 56) & 0xFF) # Byte reference - MOV operation
ref_22196 = ((ref_22193 >> 48) & 0xFF) # Byte reference - MOV operation
ref_22197 = ((ref_22193 >> 40) & 0xFF) # Byte reference - MOV operation
ref_22198 = ((ref_22193 >> 32) & 0xFF) # Byte reference - MOV operation
ref_22199 = ((ref_22193 >> 24) & 0xFF) # Byte reference - MOV operation
ref_22200 = ((ref_22193 >> 16) & 0xFF) # Byte reference - MOV operation
ref_22201 = ((ref_22193 >> 8) & 0xFF) # Byte reference - MOV operation
ref_22202 = (ref_22193 & 0xFF) # Byte reference - MOV operation
ref_24918 = ref_13736 # MOV operation
ref_26020 = ref_7774 # MOV operation
ref_26220 = ref_26020 # MOV operation
ref_26226 = (0x7 & ref_26220) # AND operation
ref_26327 = ref_26226 # MOV operation
ref_26341 = ((ref_26327 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_26450 = ref_24918 # MOV operation
ref_26454 = ref_26341 # MOV operation
ref_26456 = (ref_26454 | ref_26450) # OR operation
ref_26565 = ref_26456 # MOV operation
ref_28217 = ((((ref_22195) << 8 | ref_22196) << 8 | ref_22197) << 8 | ref_22198) # MOV operation
ref_28297 = (ref_28217 & 0xFFFFFFFF) # MOV operation
ref_31245 = ((((ref_22199) << 8 | ref_22200) << 8 | ref_22201) << 8 | ref_22202) # MOV operation
ref_31325 = (ref_31245 & 0xFFFFFFFF) # MOV operation
ref_32973 = (ref_28297 & 0xFFFFFFFF) # MOV operation
ref_33053 = (ref_32973 & 0xFFFFFFFF) # MOV operation
ref_36094 = ref_26565 # MOV operation
ref_37196 = ref_26565 # MOV operation
ref_37396 = ref_37196 # MOV operation
ref_37402 = (0x7 & ref_37396) # AND operation
ref_37503 = ref_37402 # MOV operation
ref_37517 = ((ref_37503 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_37626 = ref_36094 # MOV operation
ref_37630 = ref_37517 # MOV operation
ref_37632 = (ref_37630 | ref_37626) # OR operation
ref_37741 = ref_37632 # MOV operation
ref_39393 = (ref_31325 & 0xFFFFFFFF) # MOV operation
ref_39473 = (ref_39393 & 0xFFFFFFFF) # MOV operation
ref_42421 = (ref_33053 & 0xFFFFFFFF) # MOV operation
ref_42501 = (ref_42421 & 0xFFFFFFFF) # MOV operation
ref_42503 = (((ref_42501 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_42504 = (((ref_42501 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_42505 = (((ref_42501 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_42506 = ((ref_42501 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_44149 = (ref_39473 & 0xFFFFFFFF) # MOV operation
ref_44229 = (ref_44149 & 0xFFFFFFFF) # MOV operation
ref_44231 = (((ref_44229 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_44232 = (((ref_44229 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_44233 = (((ref_44229 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_44234 = ((ref_44229 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_47355 = ref_37741 # MOV operation
ref_48253 = ((((((((ref_42503) << 8 | ref_42504) << 8 | ref_42505) << 8 | ref_42506) << 8 | ref_44231) << 8 | ref_44232) << 8 | ref_44233) << 8 | ref_44234) # MOV operation
ref_48453 = ref_48253 # MOV operation
ref_48459 = (((sx(0x40, 0x4E1A7F2) * sx(0x40, ref_48453)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_48565 = ref_47355 # MOV operation
ref_48569 = ref_48459 # MOV operation
ref_48571 = (ref_48569 ^ ref_48565) # XOR operation
ref_48796 = ref_48571 # MOV operation
ref_48802 = (0xF & ref_48796) # AND operation
ref_49027 = ref_48802 # MOV operation
ref_49033 = (0x1 | ref_49027) # OR operation
ref_49956 = ref_7774 # MOV operation
ref_50854 = ref_9970 # MOV operation
ref_50938 = ref_49956 # MOV operation
ref_50942 = ref_50854 # MOV operation
ref_50944 = (((sx(0x40, ref_50942) * sx(0x40, ref_50938)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_51042 = ref_50944 # MOV operation
ref_51054 = ref_49033 # MOV operation
ref_51056 = ((ref_51042 << ((ref_51054 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_52095 = ref_37741 # MOV operation
ref_52993 = ((((((((ref_42503) << 8 | ref_42504) << 8 | ref_42505) << 8 | ref_42506) << 8 | ref_44231) << 8 | ref_44232) << 8 | ref_44233) << 8 | ref_44234) # MOV operation
ref_53193 = ref_52993 # MOV operation
ref_53199 = (((sx(0x40, 0x4E1A7F2) * sx(0x40, ref_53193)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_53305 = ref_52095 # MOV operation
ref_53309 = ref_53199 # MOV operation
ref_53311 = (ref_53309 ^ ref_53305) # XOR operation
ref_53536 = ref_53311 # MOV operation
ref_53542 = (0xF & ref_53536) # AND operation
ref_53767 = ref_53542 # MOV operation
ref_53773 = (0x1 | ref_53767) # OR operation
ref_53886 = ref_53773 # MOV operation
ref_53888 = ((0x40 - ref_53886) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_53896 = ref_53888 # MOV operation
ref_54814 = ref_7774 # MOV operation
ref_55712 = ref_9970 # MOV operation
ref_55796 = ref_54814 # MOV operation
ref_55800 = ref_55712 # MOV operation
ref_55802 = (((sx(0x40, ref_55800) * sx(0x40, ref_55796)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_55900 = ref_55802 # MOV operation
ref_55912 = ref_53896 # MOV operation
ref_55914 = (ref_55900 >> ((ref_55912 & 0xFF) & 0x3F)) # SHR operation
ref_56023 = ref_51056 # MOV operation
ref_56027 = ref_55914 # MOV operation
ref_56029 = (ref_56027 | ref_56023) # OR operation
ref_56138 = ref_56029 # MOV operation
ref_56349 = ref_56138 # MOV operation
ref_56351 = ref_56349 # MOV operation

print(ref_56351 & 0xffffffffffffffff)
