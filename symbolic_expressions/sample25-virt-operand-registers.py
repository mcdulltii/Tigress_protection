#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_6366 = ref_278 # MOV operation
ref_6582 = ref_6366 # MOV operation
ref_6594 = (ref_6582 >> (0x33 & 0x3F)) # SHR operation
ref_7510 = ref_278 # MOV operation
ref_7718 = ref_7510 # MOV operation
ref_7738 = ((ref_7718 << (0xD & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_7853 = ref_7738 # MOV operation
ref_7869 = ref_6594 # MOV operation
ref_7871 = (ref_7853 | ref_7869) # OR operation
ref_7990 = ref_7871 # MOV operation
ref_9809 = ref_278 # MOV operation
ref_10025 = ref_9809 # MOV operation
ref_10037 = ((((0x0) << 64 | ref_10025) / 0x6) & 0xFFFFFFFFFFFFFFFF) # DIV operation
ref_10040 = ref_10037 # MOV operation
ref_10150 = ref_10040 # MOV operation
ref_10168 = (((sx(0x40, ref_10150) * sx(0x40, 0xFA0000000002C90C)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_10284 = ref_10168 # MOV operation
ref_12005 = ref_278 # MOV operation
ref_12929 = ref_10284 # MOV operation
ref_13853 = ref_7990 # MOV operation
ref_13963 = ref_13853 # MOV operation
ref_13979 = ref_12929 # MOV operation
ref_13981 = (ref_13963 | ref_13979) # OR operation
ref_14104 = ref_12005 # MOV operation
ref_14112 = ref_13981 # MOV operation
ref_14114 = ((ref_14104 + ref_14112) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_14234 = ref_14114 # MOV operation
ref_15955 = ref_278 # MOV operation
ref_16879 = ref_10284 # MOV operation
ref_16997 = ref_15955 # MOV operation
ref_17005 = ref_16879 # MOV operation
ref_17007 = ((ref_16997 + ref_17005) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_18231 = ref_7990 # MOV operation
ref_18439 = ref_18231 # MOV operation
ref_18457 = ((ref_18439 - 0x2ED5CD7E) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_18589 = ref_18457 # MOV operation
ref_18591 = ((0x28E5FC28 - ref_18589) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_18813 = ref_18591 # MOV operation
ref_18825 = (ref_18813 >> (0x2 & 0x3F)) # SHR operation
ref_18940 = ref_18825 # MOV operation
ref_18958 = (ref_18940 & 0x7) # AND operation
ref_19073 = ref_18958 # MOV operation
ref_19091 = (ref_19073 | 0x1) # OR operation
ref_19214 = ref_17007 # MOV operation
ref_19222 = ref_19091 # MOV operation
ref_19224 = (ref_19222 & 0xFFFFFFFF) # MOV operation
ref_19226 = (ref_19214 >> ((ref_19224 & 0xFF) & 0x3F)) # SHR operation
ref_19345 = ref_19226 # MOV operation
ref_21079 = ref_19345 # MOV operation
ref_22199 = ref_19345 # MOV operation
ref_22415 = ref_22199 # MOV operation
ref_22427 = (ref_22415 >> (0x1 & 0x3F)) # SHR operation
ref_22542 = ref_22427 # MOV operation
ref_22560 = (ref_22542 & 0x7) # AND operation
ref_22675 = ref_22560 # MOV operation
ref_22693 = (ref_22675 | 0x1) # OR operation
ref_22816 = ref_21079 # MOV operation
ref_22824 = ref_22693 # MOV operation
ref_22826 = (ref_22824 & 0xFFFFFFFF) # MOV operation
ref_22828 = (ref_22816 >> ((ref_22826 & 0xFF) & 0x3F)) # SHR operation
ref_22947 = ref_22828 # MOV operation
ref_22949 = ((ref_22947 >> 56) & 0xFF) # Byte reference - MOV operation
ref_22950 = ((ref_22947 >> 48) & 0xFF) # Byte reference - MOV operation
ref_22951 = ((ref_22947 >> 40) & 0xFF) # Byte reference - MOV operation
ref_22952 = ((ref_22947 >> 32) & 0xFF) # Byte reference - MOV operation
ref_22953 = ((ref_22947 >> 24) & 0xFF) # Byte reference - MOV operation
ref_22954 = ((ref_22947 >> 16) & 0xFF) # Byte reference - MOV operation
ref_22955 = ((ref_22947 >> 8) & 0xFF) # Byte reference - MOV operation
ref_22956 = (ref_22947 & 0xFF) # Byte reference - MOV operation
ref_25893 = ref_7990 # MOV operation
ref_26003 = ref_25893 # MOV operation
ref_26021 = (ref_26003 & 0x7) # AND operation
ref_26234 = ref_26021 # MOV operation
ref_26254 = ((ref_26234 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_27183 = ref_14234 # MOV operation
ref_27293 = ref_27183 # MOV operation
ref_27309 = ref_26254 # MOV operation
ref_27311 = (ref_27293 | ref_27309) # OR operation
ref_27430 = ref_27311 # MOV operation
ref_29030 = ((((ref_22949) << 8 | ref_22950) << 8 | ref_22951) << 8 | ref_22952) # MOV operation
ref_29258 = (ref_29030 & 0xFFFFFFFF) # MOV operation
ref_30854 = ((((ref_22953) << 8 | ref_22954) << 8 | ref_22955) << 8 | ref_22956) # MOV operation
ref_32454 = (ref_30854 & 0xFFFFFFFF) # MOV operation
ref_32678 = (ref_29258 & 0xFFFFFFFF) # MOV operation
ref_34278 = (ref_32678 & 0xFFFFFFFF) # MOV operation
ref_37584 = ref_27430 # MOV operation
ref_37694 = ref_37584 # MOV operation
ref_37712 = (ref_37694 & 0x7) # AND operation
ref_37925 = ref_37712 # MOV operation
ref_37945 = ((ref_37925 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_38874 = ref_27430 # MOV operation
ref_38984 = ref_38874 # MOV operation
ref_39000 = ref_37945 # MOV operation
ref_39002 = (ref_38984 | ref_39000) # OR operation
ref_39121 = ref_39002 # MOV operation
ref_40721 = (ref_32454 & 0xFFFFFFFF) # MOV operation
ref_40949 = (ref_40721 & 0xFFFFFFFF) # MOV operation
ref_42545 = (ref_34278 & 0xFFFFFFFF) # MOV operation
ref_44145 = (ref_42545 & 0xFFFFFFFF) # MOV operation
ref_44147 = (((ref_44145 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_44148 = (((ref_44145 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_44149 = (((ref_44145 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_44150 = ((ref_44145 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_44369 = (ref_40949 & 0xFFFFFFFF) # MOV operation
ref_45969 = (ref_44369 & 0xFFFFFFFF) # MOV operation
ref_45971 = (((ref_45969 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_45972 = (((ref_45969 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_45973 = (((ref_45969 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_45974 = ((ref_45969 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_49203 = ref_10284 # MOV operation
ref_50127 = ref_7990 # MOV operation
ref_50237 = ref_50127 # MOV operation
ref_50253 = ref_49203 # MOV operation
ref_50255 = (((sx(0x40, ref_50237) * sx(0x40, ref_50253)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_51573 = ((((((((ref_44147) << 8 | ref_44148) << 8 | ref_44149) << 8 | ref_44150) << 8 | ref_45971) << 8 | ref_45972) << 8 | ref_45973) << 8 | ref_45974) # MOV operation
ref_51683 = ref_51573 # MOV operation
ref_51701 = (((sx(0x40, ref_51683) * sx(0x40, 0x4E1A7F2)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_52627 = ref_39121 # MOV operation
ref_52737 = ref_52627 # MOV operation
ref_52753 = ref_51701 # MOV operation
ref_52755 = (ref_52737 ^ ref_52753) # XOR operation
ref_52870 = ref_52755 # MOV operation
ref_52888 = (ref_52870 & 0xF) # AND operation
ref_53003 = ref_52888 # MOV operation
ref_53021 = (ref_53003 | 0x1) # OR operation
ref_53152 = ref_53021 # MOV operation
ref_53154 = ((0x40 - ref_53152) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_53278 = ref_50255 # MOV operation
ref_53286 = ref_53154 # MOV operation
ref_53288 = (ref_53286 & 0xFFFFFFFF) # MOV operation
ref_53290 = (ref_53278 >> ((ref_53288 & 0xFF) & 0x3F)) # SHR operation
ref_54219 = ref_10284 # MOV operation
ref_55143 = ref_7990 # MOV operation
ref_55253 = ref_55143 # MOV operation
ref_55269 = ref_54219 # MOV operation
ref_55271 = (((sx(0x40, ref_55253) * sx(0x40, ref_55269)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_56491 = ((((((((ref_44147) << 8 | ref_44148) << 8 | ref_44149) << 8 | ref_44150) << 8 | ref_45971) << 8 | ref_45972) << 8 | ref_45973) << 8 | ref_45974) # MOV operation
ref_56601 = ref_56491 # MOV operation
ref_56619 = (((sx(0x40, ref_56601) * sx(0x40, 0x4E1A7F2)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_57545 = ref_39121 # MOV operation
ref_57655 = ref_57545 # MOV operation
ref_57671 = ref_56619 # MOV operation
ref_57673 = (ref_57655 ^ ref_57671) # XOR operation
ref_57788 = ref_57673 # MOV operation
ref_57806 = (ref_57788 & 0xF) # AND operation
ref_57921 = ref_57806 # MOV operation
ref_57939 = (ref_57921 | 0x1) # OR operation
ref_58054 = ref_55271 # MOV operation
ref_58070 = ref_57939 # MOV operation
ref_58072 = (ref_58070 & 0xFFFFFFFF) # MOV operation
ref_58074 = ((ref_58054 << ((ref_58072 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_58189 = ref_58074 # MOV operation
ref_58205 = ref_53290 # MOV operation
ref_58207 = (ref_58189 | ref_58205) # OR operation
ref_58326 = ref_58207 # MOV operation
ref_58537 = ref_58326 # MOV operation
ref_58539 = ref_58537 # MOV operation

print(ref_58539 & 0xffffffffffffffff)
