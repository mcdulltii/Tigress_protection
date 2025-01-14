#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_5594 = ref_278 # MOV operation
ref_5670 = ref_5594 # MOV operation
ref_5684 = (ref_5670 >> (0x33 & 0x3F)) # SHR operation
ref_6638 = ref_278 # MOV operation
ref_6714 = ref_6638 # MOV operation
ref_6728 = ((ref_6714 << (0xD & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_6829 = ref_6728 # MOV operation
ref_6841 = ref_5684 # MOV operation
ref_6843 = (ref_6841 | ref_6829) # OR operation
ref_7774 = ref_6843 # MOV operation
ref_8723 = ref_278 # MOV operation
ref_8799 = ref_8723 # MOV operation
ref_8815 = ((((0x0) << 64 | ref_8799) / 0x6) & 0xFFFFFFFFFFFFFFFF) # DIV operation
ref_9036 = ref_8815 # MOV operation
ref_9042 = (((sx(0x40, 0xFA0000000002C90C) * sx(0x40, ref_9036)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_9970 = ref_9042 # MOV operation
ref_10888 = ref_9970 # MOV operation
ref_11786 = ref_7774 # MOV operation
ref_11862 = ref_11786 # MOV operation
ref_11874 = ref_10888 # MOV operation
ref_11876 = (ref_11874 | ref_11862) # OR operation
ref_12714 = ref_278 # MOV operation
ref_12790 = ref_12714 # MOV operation
ref_12802 = ref_11876 # MOV operation
ref_12804 = ((ref_12802 + ref_12790) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_13736 = ref_12804 # MOV operation
ref_15118 = ref_7774 # MOV operation
ref_15318 = ref_15118 # MOV operation
ref_15324 = ((ref_15318 - 0x2ED5CD7E) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_15332 = ref_15324 # MOV operation
ref_15440 = ref_15332 # MOV operation
ref_15442 = ((0x28E5FC28 - ref_15440) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_15450 = ref_15442 # MOV operation
ref_15546 = ref_15450 # MOV operation
ref_15560 = (ref_15546 >> (0x2 & 0x3F)) # SHR operation
ref_15661 = ref_15560 # MOV operation
ref_15675 = (0x7 & ref_15661) # AND operation
ref_15776 = ref_15675 # MOV operation
ref_15790 = (0x1 | ref_15776) # OR operation
ref_16713 = ref_9970 # MOV operation
ref_17526 = ref_278 # MOV operation
ref_17602 = ref_17526 # MOV operation
ref_17614 = ref_16713 # MOV operation
ref_17616 = ((ref_17614 + ref_17602) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_17718 = ref_17616 # MOV operation
ref_17730 = ref_15790 # MOV operation
ref_17732 = (ref_17718 >> ((ref_17730 & 0xFF) & 0x3F)) # SHR operation
ref_18663 = ref_17732 # MOV operation
ref_19929 = ref_18663 # MOV operation
ref_20005 = ref_19929 # MOV operation
ref_20019 = (ref_20005 >> (0x1 & 0x3F)) # SHR operation
ref_20120 = ref_20019 # MOV operation
ref_20134 = (0x7 & ref_20120) # AND operation
ref_20235 = ref_20134 # MOV operation
ref_20249 = (0x1 | ref_20235) # OR operation
ref_21172 = ref_18663 # MOV operation
ref_21248 = ref_21172 # MOV operation
ref_21260 = ref_20249 # MOV operation
ref_21262 = (ref_21248 >> ((ref_21260 & 0xFF) & 0x3F)) # SHR operation
ref_22193 = ref_21262 # MOV operation
ref_22195 = ((ref_22193 >> 56) & 0xFF) # Byte reference - MOV operation
ref_22196 = ((ref_22193 >> 48) & 0xFF) # Byte reference - MOV operation
ref_22197 = ((ref_22193 >> 40) & 0xFF) # Byte reference - MOV operation
ref_22198 = ((ref_22193 >> 32) & 0xFF) # Byte reference - MOV operation
ref_22199 = ((ref_22193 >> 24) & 0xFF) # Byte reference - MOV operation
ref_22200 = ((ref_22193 >> 16) & 0xFF) # Byte reference - MOV operation
ref_22201 = ((ref_22193 >> 8) & 0xFF) # Byte reference - MOV operation
ref_22202 = (ref_22193 & 0xFF) # Byte reference - MOV operation
ref_24416 = ref_7774 # MOV operation
ref_24492 = ref_24416 # MOV operation
ref_24506 = (0x7 & ref_24492) # AND operation
ref_24607 = ref_24506 # MOV operation
ref_24621 = ((ref_24607 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_25544 = ref_13736 # MOV operation
ref_25620 = ref_25544 # MOV operation
ref_25632 = ref_24621 # MOV operation
ref_25634 = (ref_25632 | ref_25620) # OR operation
ref_26565 = ref_25634 # MOV operation
ref_28089 = ((((ref_22195) << 8 | ref_22196) << 8 | ref_22197) << 8 | ref_22198) # MOV operation
ref_28297 = (ref_28089 & 0xFFFFFFFF) # MOV operation
ref_29817 = ((((ref_22199) << 8 | ref_22200) << 8 | ref_22201) << 8 | ref_22202) # MOV operation
ref_31325 = (ref_29817 & 0xFFFFFFFF) # MOV operation
ref_31545 = (ref_28297 & 0xFFFFFFFF) # MOV operation
ref_33053 = (ref_31545 & 0xFFFFFFFF) # MOV operation
ref_35592 = ref_26565 # MOV operation
ref_35668 = ref_35592 # MOV operation
ref_35682 = (0x7 & ref_35668) # AND operation
ref_35783 = ref_35682 # MOV operation
ref_35797 = ((ref_35783 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_36720 = ref_26565 # MOV operation
ref_36796 = ref_36720 # MOV operation
ref_36808 = ref_35797 # MOV operation
ref_36810 = (ref_36808 | ref_36796) # OR operation
ref_37741 = ref_36810 # MOV operation
ref_39265 = (ref_31325 & 0xFFFFFFFF) # MOV operation
ref_39473 = (ref_39265 & 0xFFFFFFFF) # MOV operation
ref_40993 = (ref_33053 & 0xFFFFFFFF) # MOV operation
ref_42501 = (ref_40993 & 0xFFFFFFFF) # MOV operation
ref_42503 = (((ref_42501 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_42504 = (((ref_42501 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_42505 = (((ref_42501 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_42506 = ((ref_42501 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_42721 = (ref_39473 & 0xFFFFFFFF) # MOV operation
ref_44229 = (ref_42721 & 0xFFFFFFFF) # MOV operation
ref_44231 = (((ref_44229 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_44232 = (((ref_44229 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_44233 = (((ref_44229 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_44234 = ((ref_44229 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_46957 = ref_37741 # MOV operation
ref_47855 = ((((((((ref_42503) << 8 | ref_42504) << 8 | ref_42505) << 8 | ref_42506) << 8 | ref_44231) << 8 | ref_44232) << 8 | ref_44233) << 8 | ref_44234) # MOV operation
ref_48055 = ref_47855 # MOV operation
ref_48061 = (((sx(0x40, 0x4E1A7F2) * sx(0x40, ref_48055)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_48167 = ref_46957 # MOV operation
ref_48171 = ref_48061 # MOV operation
ref_48173 = (ref_48171 ^ ref_48167) # XOR operation
ref_48274 = ref_48173 # MOV operation
ref_48288 = (0xF & ref_48274) # AND operation
ref_48389 = ref_48288 # MOV operation
ref_48403 = (0x1 | ref_48389) # OR operation
ref_48516 = ref_48403 # MOV operation
ref_48518 = ((0x40 - ref_48516) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_48526 = ref_48518 # MOV operation
ref_49444 = ref_7774 # MOV operation
ref_50342 = ref_9970 # MOV operation
ref_50426 = ref_49444 # MOV operation
ref_50430 = ref_50342 # MOV operation
ref_50432 = (((sx(0x40, ref_50430) * sx(0x40, ref_50426)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_50530 = ref_50432 # MOV operation
ref_50542 = ref_48526 # MOV operation
ref_50544 = (ref_50530 >> ((ref_50542 & 0xFF) & 0x3F)) # SHR operation
ref_51699 = ref_37741 # MOV operation
ref_52597 = ((((((((ref_42503) << 8 | ref_42504) << 8 | ref_42505) << 8 | ref_42506) << 8 | ref_44231) << 8 | ref_44232) << 8 | ref_44233) << 8 | ref_44234) # MOV operation
ref_52797 = ref_52597 # MOV operation
ref_52803 = (((sx(0x40, 0x4E1A7F2) * sx(0x40, ref_52797)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_52909 = ref_51699 # MOV operation
ref_52913 = ref_52803 # MOV operation
ref_52915 = (ref_52913 ^ ref_52909) # XOR operation
ref_53016 = ref_52915 # MOV operation
ref_53030 = (0xF & ref_53016) # AND operation
ref_53131 = ref_53030 # MOV operation
ref_53145 = (0x1 | ref_53131) # OR operation
ref_54068 = ref_7774 # MOV operation
ref_54966 = ref_9970 # MOV operation
ref_55050 = ref_54068 # MOV operation
ref_55054 = ref_54966 # MOV operation
ref_55056 = (((sx(0x40, ref_55054) * sx(0x40, ref_55050)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_55154 = ref_55056 # MOV operation
ref_55166 = ref_53145 # MOV operation
ref_55168 = ((ref_55154 << ((ref_55166 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_55269 = ref_55168 # MOV operation
ref_55281 = ref_50544 # MOV operation
ref_55283 = (ref_55281 | ref_55269) # OR operation
ref_56138 = ref_55283 # MOV operation
ref_56349 = ref_56138 # MOV operation
ref_56351 = ref_56349 # MOV operation

print(ref_56351 & 0xffffffffffffffff)
