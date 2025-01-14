#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_214 = SymVar_0
ref_225 = ref_214 # MOV operation
ref_237 = ref_225 # MOV operation
ref_239 = ref_237 # MOV operation
ref_273 = ((ref_239 >> 56) & 0xFF) # Byte reference - MOV operation
ref_274 = ((ref_239 >> 48) & 0xFF) # Byte reference - MOV operation
ref_275 = ((ref_239 >> 40) & 0xFF) # Byte reference - MOV operation
ref_276 = ((ref_239 >> 32) & 0xFF) # Byte reference - MOV operation
ref_277 = ((ref_239 >> 24) & 0xFF) # Byte reference - MOV operation
ref_278 = ((ref_239 >> 16) & 0xFF) # Byte reference - MOV operation
ref_279 = ((ref_239 >> 8) & 0xFF) # Byte reference - MOV operation
ref_280 = (ref_239 & 0xFF) # Byte reference - MOV operation
ref_9210 = ref_280 # MOVZX operation
ref_9312 = (ref_9210 & 0xFF) # MOVZX operation
ref_9314 = (ref_9312 & 0xFF) # MOVZX operation
ref_9662 = (ref_9314 & 0xFFFFFFFF) # MOV operation
ref_9664 = ((0x0 + (ref_9662 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_9898 = (ref_9664 & 0xFFFFFFFF) # MOV operation
ref_10122 = (ref_9898 & 0xFFFFFFFF) # MOV operation
ref_10330 = (ref_10122 & 0xFFFFFFFF) # MOV operation
ref_10342 = (((ref_10330 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_10573 = (ref_9898 & 0xFFFFFFFF) # MOV operation
ref_10679 = (ref_10573 & 0xFFFFFFFF) # MOV operation
ref_10695 = (ref_10342 & 0xFFFFFFFF) # MOV operation
ref_10697 = (((ref_10679 & 0xFFFFFFFF) + (ref_10695 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_10931 = (ref_10697 & 0xFFFFFFFF) # MOV operation
ref_11155 = (ref_10931 & 0xFFFFFFFF) # MOV operation
ref_11363 = (ref_11155 & 0xFFFFFFFF) # MOV operation
ref_11375 = ((ref_11363 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_11606 = (ref_10931 & 0xFFFFFFFF) # MOV operation
ref_11712 = (ref_11606 & 0xFFFFFFFF) # MOV operation
ref_11728 = (ref_11375 & 0xFFFFFFFF) # MOV operation
ref_11730 = ((ref_11712 & 0xFFFFFFFF) ^ (ref_11728 & 0xFFFFFFFF)) # XOR operation
ref_11963 = (ref_11730 & 0xFFFFFFFF) # MOV operation
ref_14955 = ref_279 # MOVZX operation
ref_15057 = (ref_14955 & 0xFF) # MOVZX operation
ref_15059 = (ref_15057 & 0xFF) # MOVZX operation
ref_15285 = (ref_11963 & 0xFFFFFFFF) # MOV operation
ref_15391 = (ref_15285 & 0xFFFFFFFF) # MOV operation
ref_15407 = (ref_15059 & 0xFFFFFFFF) # MOV operation
ref_15409 = (((ref_15391 & 0xFFFFFFFF) + (ref_15407 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_15643 = (ref_15409 & 0xFFFFFFFF) # MOV operation
ref_15867 = (ref_15643 & 0xFFFFFFFF) # MOV operation
ref_16075 = (ref_15867 & 0xFFFFFFFF) # MOV operation
ref_16087 = (((ref_16075 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_16318 = (ref_15643 & 0xFFFFFFFF) # MOV operation
ref_16424 = (ref_16318 & 0xFFFFFFFF) # MOV operation
ref_16440 = (ref_16087 & 0xFFFFFFFF) # MOV operation
ref_16442 = (((ref_16424 & 0xFFFFFFFF) + (ref_16440 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_16676 = (ref_16442 & 0xFFFFFFFF) # MOV operation
ref_16900 = (ref_16676 & 0xFFFFFFFF) # MOV operation
ref_17108 = (ref_16900 & 0xFFFFFFFF) # MOV operation
ref_17120 = ((ref_17108 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_17351 = (ref_16676 & 0xFFFFFFFF) # MOV operation
ref_17457 = (ref_17351 & 0xFFFFFFFF) # MOV operation
ref_17473 = (ref_17120 & 0xFFFFFFFF) # MOV operation
ref_17475 = ((ref_17457 & 0xFFFFFFFF) ^ (ref_17473 & 0xFFFFFFFF)) # XOR operation
ref_17708 = (ref_17475 & 0xFFFFFFFF) # MOV operation
ref_20700 = ref_278 # MOVZX operation
ref_20802 = (ref_20700 & 0xFF) # MOVZX operation
ref_20804 = (ref_20802 & 0xFF) # MOVZX operation
ref_21030 = (ref_17708 & 0xFFFFFFFF) # MOV operation
ref_21136 = (ref_21030 & 0xFFFFFFFF) # MOV operation
ref_21152 = (ref_20804 & 0xFFFFFFFF) # MOV operation
ref_21154 = (((ref_21136 & 0xFFFFFFFF) + (ref_21152 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_21388 = (ref_21154 & 0xFFFFFFFF) # MOV operation
ref_21612 = (ref_21388 & 0xFFFFFFFF) # MOV operation
ref_21820 = (ref_21612 & 0xFFFFFFFF) # MOV operation
ref_21832 = (((ref_21820 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_22063 = (ref_21388 & 0xFFFFFFFF) # MOV operation
ref_22169 = (ref_22063 & 0xFFFFFFFF) # MOV operation
ref_22185 = (ref_21832 & 0xFFFFFFFF) # MOV operation
ref_22187 = (((ref_22169 & 0xFFFFFFFF) + (ref_22185 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_22421 = (ref_22187 & 0xFFFFFFFF) # MOV operation
ref_22645 = (ref_22421 & 0xFFFFFFFF) # MOV operation
ref_22853 = (ref_22645 & 0xFFFFFFFF) # MOV operation
ref_22865 = ((ref_22853 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_23096 = (ref_22421 & 0xFFFFFFFF) # MOV operation
ref_23202 = (ref_23096 & 0xFFFFFFFF) # MOV operation
ref_23218 = (ref_22865 & 0xFFFFFFFF) # MOV operation
ref_23220 = ((ref_23202 & 0xFFFFFFFF) ^ (ref_23218 & 0xFFFFFFFF)) # XOR operation
ref_23453 = (ref_23220 & 0xFFFFFFFF) # MOV operation
ref_26445 = ref_277 # MOVZX operation
ref_26547 = (ref_26445 & 0xFF) # MOVZX operation
ref_26549 = (ref_26547 & 0xFF) # MOVZX operation
ref_26775 = (ref_23453 & 0xFFFFFFFF) # MOV operation
ref_26881 = (ref_26775 & 0xFFFFFFFF) # MOV operation
ref_26897 = (ref_26549 & 0xFFFFFFFF) # MOV operation
ref_26899 = (((ref_26881 & 0xFFFFFFFF) + (ref_26897 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_27133 = (ref_26899 & 0xFFFFFFFF) # MOV operation
ref_27357 = (ref_27133 & 0xFFFFFFFF) # MOV operation
ref_27565 = (ref_27357 & 0xFFFFFFFF) # MOV operation
ref_27577 = (((ref_27565 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_27808 = (ref_27133 & 0xFFFFFFFF) # MOV operation
ref_27914 = (ref_27808 & 0xFFFFFFFF) # MOV operation
ref_27930 = (ref_27577 & 0xFFFFFFFF) # MOV operation
ref_27932 = (((ref_27914 & 0xFFFFFFFF) + (ref_27930 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_28166 = (ref_27932 & 0xFFFFFFFF) # MOV operation
ref_28390 = (ref_28166 & 0xFFFFFFFF) # MOV operation
ref_28598 = (ref_28390 & 0xFFFFFFFF) # MOV operation
ref_28610 = ((ref_28598 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_28841 = (ref_28166 & 0xFFFFFFFF) # MOV operation
ref_28947 = (ref_28841 & 0xFFFFFFFF) # MOV operation
ref_28963 = (ref_28610 & 0xFFFFFFFF) # MOV operation
ref_28965 = ((ref_28947 & 0xFFFFFFFF) ^ (ref_28963 & 0xFFFFFFFF)) # XOR operation
ref_29198 = (ref_28965 & 0xFFFFFFFF) # MOV operation
ref_32190 = ref_276 # MOVZX operation
ref_32292 = (ref_32190 & 0xFF) # MOVZX operation
ref_32294 = (ref_32292 & 0xFF) # MOVZX operation
ref_32520 = (ref_29198 & 0xFFFFFFFF) # MOV operation
ref_32626 = (ref_32520 & 0xFFFFFFFF) # MOV operation
ref_32642 = (ref_32294 & 0xFFFFFFFF) # MOV operation
ref_32644 = (((ref_32626 & 0xFFFFFFFF) + (ref_32642 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_32878 = (ref_32644 & 0xFFFFFFFF) # MOV operation
ref_33102 = (ref_32878 & 0xFFFFFFFF) # MOV operation
ref_33310 = (ref_33102 & 0xFFFFFFFF) # MOV operation
ref_33322 = (((ref_33310 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_33553 = (ref_32878 & 0xFFFFFFFF) # MOV operation
ref_33659 = (ref_33553 & 0xFFFFFFFF) # MOV operation
ref_33675 = (ref_33322 & 0xFFFFFFFF) # MOV operation
ref_33677 = (((ref_33659 & 0xFFFFFFFF) + (ref_33675 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_33911 = (ref_33677 & 0xFFFFFFFF) # MOV operation
ref_34135 = (ref_33911 & 0xFFFFFFFF) # MOV operation
ref_34343 = (ref_34135 & 0xFFFFFFFF) # MOV operation
ref_34355 = ((ref_34343 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_34586 = (ref_33911 & 0xFFFFFFFF) # MOV operation
ref_34692 = (ref_34586 & 0xFFFFFFFF) # MOV operation
ref_34708 = (ref_34355 & 0xFFFFFFFF) # MOV operation
ref_34710 = ((ref_34692 & 0xFFFFFFFF) ^ (ref_34708 & 0xFFFFFFFF)) # XOR operation
ref_34943 = (ref_34710 & 0xFFFFFFFF) # MOV operation
ref_37935 = ref_275 # MOVZX operation
ref_38037 = (ref_37935 & 0xFF) # MOVZX operation
ref_38039 = (ref_38037 & 0xFF) # MOVZX operation
ref_38265 = (ref_34943 & 0xFFFFFFFF) # MOV operation
ref_38371 = (ref_38265 & 0xFFFFFFFF) # MOV operation
ref_38387 = (ref_38039 & 0xFFFFFFFF) # MOV operation
ref_38389 = (((ref_38371 & 0xFFFFFFFF) + (ref_38387 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_38623 = (ref_38389 & 0xFFFFFFFF) # MOV operation
ref_38847 = (ref_38623 & 0xFFFFFFFF) # MOV operation
ref_39055 = (ref_38847 & 0xFFFFFFFF) # MOV operation
ref_39067 = (((ref_39055 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_39298 = (ref_38623 & 0xFFFFFFFF) # MOV operation
ref_39404 = (ref_39298 & 0xFFFFFFFF) # MOV operation
ref_39420 = (ref_39067 & 0xFFFFFFFF) # MOV operation
ref_39422 = (((ref_39404 & 0xFFFFFFFF) + (ref_39420 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_39656 = (ref_39422 & 0xFFFFFFFF) # MOV operation
ref_39880 = (ref_39656 & 0xFFFFFFFF) # MOV operation
ref_40088 = (ref_39880 & 0xFFFFFFFF) # MOV operation
ref_40100 = ((ref_40088 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_40331 = (ref_39656 & 0xFFFFFFFF) # MOV operation
ref_40437 = (ref_40331 & 0xFFFFFFFF) # MOV operation
ref_40453 = (ref_40100 & 0xFFFFFFFF) # MOV operation
ref_40455 = ((ref_40437 & 0xFFFFFFFF) ^ (ref_40453 & 0xFFFFFFFF)) # XOR operation
ref_40688 = (ref_40455 & 0xFFFFFFFF) # MOV operation
ref_43680 = ref_274 # MOVZX operation
ref_43782 = (ref_43680 & 0xFF) # MOVZX operation
ref_43784 = (ref_43782 & 0xFF) # MOVZX operation
ref_44010 = (ref_40688 & 0xFFFFFFFF) # MOV operation
ref_44116 = (ref_44010 & 0xFFFFFFFF) # MOV operation
ref_44132 = (ref_43784 & 0xFFFFFFFF) # MOV operation
ref_44134 = (((ref_44116 & 0xFFFFFFFF) + (ref_44132 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_44368 = (ref_44134 & 0xFFFFFFFF) # MOV operation
ref_44592 = (ref_44368 & 0xFFFFFFFF) # MOV operation
ref_44800 = (ref_44592 & 0xFFFFFFFF) # MOV operation
ref_44812 = (((ref_44800 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_45043 = (ref_44368 & 0xFFFFFFFF) # MOV operation
ref_45149 = (ref_45043 & 0xFFFFFFFF) # MOV operation
ref_45165 = (ref_44812 & 0xFFFFFFFF) # MOV operation
ref_45167 = (((ref_45149 & 0xFFFFFFFF) + (ref_45165 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_45401 = (ref_45167 & 0xFFFFFFFF) # MOV operation
ref_45625 = (ref_45401 & 0xFFFFFFFF) # MOV operation
ref_45833 = (ref_45625 & 0xFFFFFFFF) # MOV operation
ref_45845 = ((ref_45833 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_46076 = (ref_45401 & 0xFFFFFFFF) # MOV operation
ref_46182 = (ref_46076 & 0xFFFFFFFF) # MOV operation
ref_46198 = (ref_45845 & 0xFFFFFFFF) # MOV operation
ref_46200 = ((ref_46182 & 0xFFFFFFFF) ^ (ref_46198 & 0xFFFFFFFF)) # XOR operation
ref_46433 = (ref_46200 & 0xFFFFFFFF) # MOV operation
ref_49425 = ref_273 # MOVZX operation
ref_49527 = (ref_49425 & 0xFF) # MOVZX operation
ref_49529 = (ref_49527 & 0xFF) # MOVZX operation
ref_49755 = (ref_46433 & 0xFFFFFFFF) # MOV operation
ref_49861 = (ref_49755 & 0xFFFFFFFF) # MOV operation
ref_49877 = (ref_49529 & 0xFFFFFFFF) # MOV operation
ref_49879 = (((ref_49861 & 0xFFFFFFFF) + (ref_49877 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_50113 = (ref_49879 & 0xFFFFFFFF) # MOV operation
ref_50337 = (ref_50113 & 0xFFFFFFFF) # MOV operation
ref_50545 = (ref_50337 & 0xFFFFFFFF) # MOV operation
ref_50557 = (((ref_50545 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_50788 = (ref_50113 & 0xFFFFFFFF) # MOV operation
ref_50894 = (ref_50788 & 0xFFFFFFFF) # MOV operation
ref_50910 = (ref_50557 & 0xFFFFFFFF) # MOV operation
ref_50912 = (((ref_50894 & 0xFFFFFFFF) + (ref_50910 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_51146 = (ref_50912 & 0xFFFFFFFF) # MOV operation
ref_51370 = (ref_51146 & 0xFFFFFFFF) # MOV operation
ref_51578 = (ref_51370 & 0xFFFFFFFF) # MOV operation
ref_51590 = ((ref_51578 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_51821 = (ref_51146 & 0xFFFFFFFF) # MOV operation
ref_51927 = (ref_51821 & 0xFFFFFFFF) # MOV operation
ref_51943 = (ref_51590 & 0xFFFFFFFF) # MOV operation
ref_51945 = ((ref_51927 & 0xFFFFFFFF) ^ (ref_51943 & 0xFFFFFFFF)) # XOR operation
ref_52178 = (ref_51945 & 0xFFFFFFFF) # MOV operation
ref_53342 = (ref_52178 & 0xFFFFFFFF) # MOV operation
ref_53550 = (ref_53342 & 0xFFFFFFFF) # MOV operation
ref_53562 = (((ref_53550 & 0xFFFFFFFF) << (0x3 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_53793 = (ref_52178 & 0xFFFFFFFF) # MOV operation
ref_53899 = (ref_53793 & 0xFFFFFFFF) # MOV operation
ref_53915 = (ref_53562 & 0xFFFFFFFF) # MOV operation
ref_53917 = (((ref_53899 & 0xFFFFFFFF) + (ref_53915 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_54151 = (ref_53917 & 0xFFFFFFFF) # MOV operation
ref_54375 = (ref_54151 & 0xFFFFFFFF) # MOV operation
ref_54583 = (ref_54375 & 0xFFFFFFFF) # MOV operation
ref_54595 = ((ref_54583 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_54826 = (ref_54151 & 0xFFFFFFFF) # MOV operation
ref_54932 = (ref_54826 & 0xFFFFFFFF) # MOV operation
ref_54948 = (ref_54595 & 0xFFFFFFFF) # MOV operation
ref_54950 = ((ref_54932 & 0xFFFFFFFF) ^ (ref_54948 & 0xFFFFFFFF)) # XOR operation
ref_55183 = (ref_54950 & 0xFFFFFFFF) # MOV operation
ref_55407 = (ref_55183 & 0xFFFFFFFF) # MOV operation
ref_55615 = (ref_55407 & 0xFFFFFFFF) # MOV operation
ref_55627 = (((ref_55615 & 0xFFFFFFFF) << (0xF & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_55858 = (ref_55183 & 0xFFFFFFFF) # MOV operation
ref_55964 = (ref_55858 & 0xFFFFFFFF) # MOV operation
ref_55980 = (ref_55627 & 0xFFFFFFFF) # MOV operation
ref_55982 = (((ref_55964 & 0xFFFFFFFF) + (ref_55980 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_56216 = (ref_55982 & 0xFFFFFFFF) # MOV operation
ref_56524 = (ref_56216 & 0xFFFFFFFF) # MOV operation
ref_56618 = (ref_56524 & 0xFFFFFFFF) # MOV operation
ref_56642 = (ref_56618 & 0xFFFFFFFF) # MOV operation
ref_56650 = (ref_56642 & 0xFFFFFFFF) # MOV operation
ref_56652 = (ref_56650 & 0xFFFFFFFF) # MOV operation

print(ref_56652 & 0xffffffffffffffff)
