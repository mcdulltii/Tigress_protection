#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_250 = SymVar_0
ref_261 = ref_250 # MOV operation
ref_273 = ref_261 # MOV operation
ref_275 = ref_273 # MOV operation
ref_309 = ((ref_275 >> 56) & 0xFF) # Byte reference - MOV operation
ref_310 = ((ref_275 >> 48) & 0xFF) # Byte reference - MOV operation
ref_311 = ((ref_275 >> 40) & 0xFF) # Byte reference - MOV operation
ref_312 = ((ref_275 >> 32) & 0xFF) # Byte reference - MOV operation
ref_313 = ((ref_275 >> 24) & 0xFF) # Byte reference - MOV operation
ref_314 = ((ref_275 >> 16) & 0xFF) # Byte reference - MOV operation
ref_315 = ((ref_275 >> 8) & 0xFF) # Byte reference - MOV operation
ref_316 = (ref_275 & 0xFF) # Byte reference - MOV operation
ref_8771 = ref_316 # MOVZX operation
ref_8805 = (ref_8771 & 0xFF) # MOVZX operation
ref_8807 = (ref_8805 & 0xFF) # MOVZX operation
ref_8995 = (ref_8807 & 0xFFFFFFFF) # MOV operation
ref_8997 = (((ref_8995 & 0xFFFFFFFF) + 0x1) & 0xFFFFFFFF) # ADD operation
ref_9244 = (ref_8997 & 0xFFFFFFFF) # MOV operation
ref_9253 = ((((0x0) << 32 | (ref_9244 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_9255 = (ref_9253 & 0xFFFFFFFF) # MOV operation
ref_9323 = (ref_9255 & 0xFFFFFFFF) # MOV operation
ref_9575 = (ref_9323 & 0xFFFFFFFF) # MOV operation
ref_9763 = (ref_9575 & 0xFFFFFFFF) # MOV operation
ref_9765 = (((ref_9763 & 0xFFFFFFFF) + 0x0) & 0xFFFFFFFF) # ADD operation
ref_10012 = (ref_9765 & 0xFFFFFFFF) # MOV operation
ref_10021 = ((((0x0) << 32 | (ref_10012 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_10023 = (ref_10021 & 0xFFFFFFFF) # MOV operation
ref_10091 = (ref_10023 & 0xFFFFFFFF) # MOV operation
ref_11808 = ref_315 # MOVZX operation
ref_11842 = (ref_11808 & 0xFF) # MOVZX operation
ref_11844 = (ref_11842 & 0xFF) # MOVZX operation
ref_11980 = (ref_9323 & 0xFFFFFFFF) # MOV operation
ref_12020 = (ref_11980 & 0xFFFFFFFF) # MOV operation
ref_12032 = (ref_11844 & 0xFFFFFFFF) # MOV operation
ref_12034 = (((ref_12032 & 0xFFFFFFFF) + (ref_12020 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_12281 = (ref_12034 & 0xFFFFFFFF) # MOV operation
ref_12290 = ((((0x0) << 32 | (ref_12281 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_12292 = (ref_12290 & 0xFFFFFFFF) # MOV operation
ref_12360 = (ref_12292 & 0xFFFFFFFF) # MOV operation
ref_12612 = (ref_12360 & 0xFFFFFFFF) # MOV operation
ref_12748 = (ref_10091 & 0xFFFFFFFF) # MOV operation
ref_12788 = (ref_12748 & 0xFFFFFFFF) # MOV operation
ref_12800 = (ref_12612 & 0xFFFFFFFF) # MOV operation
ref_12802 = (((ref_12800 & 0xFFFFFFFF) + (ref_12788 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_13049 = (ref_12802 & 0xFFFFFFFF) # MOV operation
ref_13058 = ((((0x0) << 32 | (ref_13049 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_13060 = (ref_13058 & 0xFFFFFFFF) # MOV operation
ref_13128 = (ref_13060 & 0xFFFFFFFF) # MOV operation
ref_14845 = ref_314 # MOVZX operation
ref_14879 = (ref_14845 & 0xFF) # MOVZX operation
ref_14881 = (ref_14879 & 0xFF) # MOVZX operation
ref_15017 = (ref_12360 & 0xFFFFFFFF) # MOV operation
ref_15057 = (ref_15017 & 0xFFFFFFFF) # MOV operation
ref_15069 = (ref_14881 & 0xFFFFFFFF) # MOV operation
ref_15071 = (((ref_15069 & 0xFFFFFFFF) + (ref_15057 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_15318 = (ref_15071 & 0xFFFFFFFF) # MOV operation
ref_15327 = ((((0x0) << 32 | (ref_15318 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_15329 = (ref_15327 & 0xFFFFFFFF) # MOV operation
ref_15397 = (ref_15329 & 0xFFFFFFFF) # MOV operation
ref_15649 = (ref_15397 & 0xFFFFFFFF) # MOV operation
ref_15785 = (ref_13128 & 0xFFFFFFFF) # MOV operation
ref_15825 = (ref_15785 & 0xFFFFFFFF) # MOV operation
ref_15837 = (ref_15649 & 0xFFFFFFFF) # MOV operation
ref_15839 = (((ref_15837 & 0xFFFFFFFF) + (ref_15825 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_16086 = (ref_15839 & 0xFFFFFFFF) # MOV operation
ref_16095 = ((((0x0) << 32 | (ref_16086 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_16097 = (ref_16095 & 0xFFFFFFFF) # MOV operation
ref_16165 = (ref_16097 & 0xFFFFFFFF) # MOV operation
ref_17882 = ref_313 # MOVZX operation
ref_17916 = (ref_17882 & 0xFF) # MOVZX operation
ref_17918 = (ref_17916 & 0xFF) # MOVZX operation
ref_18054 = (ref_15397 & 0xFFFFFFFF) # MOV operation
ref_18094 = (ref_18054 & 0xFFFFFFFF) # MOV operation
ref_18106 = (ref_17918 & 0xFFFFFFFF) # MOV operation
ref_18108 = (((ref_18106 & 0xFFFFFFFF) + (ref_18094 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_18355 = (ref_18108 & 0xFFFFFFFF) # MOV operation
ref_18364 = ((((0x0) << 32 | (ref_18355 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_18366 = (ref_18364 & 0xFFFFFFFF) # MOV operation
ref_18434 = (ref_18366 & 0xFFFFFFFF) # MOV operation
ref_18686 = (ref_18434 & 0xFFFFFFFF) # MOV operation
ref_18822 = (ref_16165 & 0xFFFFFFFF) # MOV operation
ref_18862 = (ref_18822 & 0xFFFFFFFF) # MOV operation
ref_18874 = (ref_18686 & 0xFFFFFFFF) # MOV operation
ref_18876 = (((ref_18874 & 0xFFFFFFFF) + (ref_18862 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_19123 = (ref_18876 & 0xFFFFFFFF) # MOV operation
ref_19132 = ((((0x0) << 32 | (ref_19123 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_19134 = (ref_19132 & 0xFFFFFFFF) # MOV operation
ref_19202 = (ref_19134 & 0xFFFFFFFF) # MOV operation
ref_20919 = ref_312 # MOVZX operation
ref_20953 = (ref_20919 & 0xFF) # MOVZX operation
ref_20955 = (ref_20953 & 0xFF) # MOVZX operation
ref_21091 = (ref_18434 & 0xFFFFFFFF) # MOV operation
ref_21131 = (ref_21091 & 0xFFFFFFFF) # MOV operation
ref_21143 = (ref_20955 & 0xFFFFFFFF) # MOV operation
ref_21145 = (((ref_21143 & 0xFFFFFFFF) + (ref_21131 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_21392 = (ref_21145 & 0xFFFFFFFF) # MOV operation
ref_21401 = ((((0x0) << 32 | (ref_21392 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_21403 = (ref_21401 & 0xFFFFFFFF) # MOV operation
ref_21471 = (ref_21403 & 0xFFFFFFFF) # MOV operation
ref_21723 = (ref_21471 & 0xFFFFFFFF) # MOV operation
ref_21859 = (ref_19202 & 0xFFFFFFFF) # MOV operation
ref_21899 = (ref_21859 & 0xFFFFFFFF) # MOV operation
ref_21911 = (ref_21723 & 0xFFFFFFFF) # MOV operation
ref_21913 = (((ref_21911 & 0xFFFFFFFF) + (ref_21899 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_22160 = (ref_21913 & 0xFFFFFFFF) # MOV operation
ref_22169 = ((((0x0) << 32 | (ref_22160 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_22171 = (ref_22169 & 0xFFFFFFFF) # MOV operation
ref_22239 = (ref_22171 & 0xFFFFFFFF) # MOV operation
ref_23956 = ref_311 # MOVZX operation
ref_23990 = (ref_23956 & 0xFF) # MOVZX operation
ref_23992 = (ref_23990 & 0xFF) # MOVZX operation
ref_24128 = (ref_21471 & 0xFFFFFFFF) # MOV operation
ref_24168 = (ref_24128 & 0xFFFFFFFF) # MOV operation
ref_24180 = (ref_23992 & 0xFFFFFFFF) # MOV operation
ref_24182 = (((ref_24180 & 0xFFFFFFFF) + (ref_24168 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_24429 = (ref_24182 & 0xFFFFFFFF) # MOV operation
ref_24438 = ((((0x0) << 32 | (ref_24429 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_24440 = (ref_24438 & 0xFFFFFFFF) # MOV operation
ref_24508 = (ref_24440 & 0xFFFFFFFF) # MOV operation
ref_24760 = (ref_24508 & 0xFFFFFFFF) # MOV operation
ref_24896 = (ref_22239 & 0xFFFFFFFF) # MOV operation
ref_24936 = (ref_24896 & 0xFFFFFFFF) # MOV operation
ref_24948 = (ref_24760 & 0xFFFFFFFF) # MOV operation
ref_24950 = (((ref_24948 & 0xFFFFFFFF) + (ref_24936 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_25197 = (ref_24950 & 0xFFFFFFFF) # MOV operation
ref_25206 = ((((0x0) << 32 | (ref_25197 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_25208 = (ref_25206 & 0xFFFFFFFF) # MOV operation
ref_25276 = (ref_25208 & 0xFFFFFFFF) # MOV operation
ref_26993 = ref_310 # MOVZX operation
ref_27027 = (ref_26993 & 0xFF) # MOVZX operation
ref_27029 = (ref_27027 & 0xFF) # MOVZX operation
ref_27165 = (ref_24508 & 0xFFFFFFFF) # MOV operation
ref_27205 = (ref_27165 & 0xFFFFFFFF) # MOV operation
ref_27217 = (ref_27029 & 0xFFFFFFFF) # MOV operation
ref_27219 = (((ref_27217 & 0xFFFFFFFF) + (ref_27205 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_27466 = (ref_27219 & 0xFFFFFFFF) # MOV operation
ref_27475 = ((((0x0) << 32 | (ref_27466 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_27477 = (ref_27475 & 0xFFFFFFFF) # MOV operation
ref_27545 = (ref_27477 & 0xFFFFFFFF) # MOV operation
ref_27797 = (ref_27545 & 0xFFFFFFFF) # MOV operation
ref_27933 = (ref_25276 & 0xFFFFFFFF) # MOV operation
ref_27973 = (ref_27933 & 0xFFFFFFFF) # MOV operation
ref_27985 = (ref_27797 & 0xFFFFFFFF) # MOV operation
ref_27987 = (((ref_27985 & 0xFFFFFFFF) + (ref_27973 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_28234 = (ref_27987 & 0xFFFFFFFF) # MOV operation
ref_28243 = ((((0x0) << 32 | (ref_28234 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_28245 = (ref_28243 & 0xFFFFFFFF) # MOV operation
ref_28313 = (ref_28245 & 0xFFFFFFFF) # MOV operation
ref_30030 = ref_309 # MOVZX operation
ref_30064 = (ref_30030 & 0xFF) # MOVZX operation
ref_30066 = (ref_30064 & 0xFF) # MOVZX operation
ref_30202 = (ref_27545 & 0xFFFFFFFF) # MOV operation
ref_30242 = (ref_30202 & 0xFFFFFFFF) # MOV operation
ref_30254 = (ref_30066 & 0xFFFFFFFF) # MOV operation
ref_30256 = (((ref_30254 & 0xFFFFFFFF) + (ref_30242 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_30503 = (ref_30256 & 0xFFFFFFFF) # MOV operation
ref_30512 = ((((0x0) << 32 | (ref_30503 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_30514 = (ref_30512 & 0xFFFFFFFF) # MOV operation
ref_30582 = (ref_30514 & 0xFFFFFFFF) # MOV operation
ref_30834 = (ref_30582 & 0xFFFFFFFF) # MOV operation
ref_30970 = (ref_28313 & 0xFFFFFFFF) # MOV operation
ref_31010 = (ref_30970 & 0xFFFFFFFF) # MOV operation
ref_31022 = (ref_30834 & 0xFFFFFFFF) # MOV operation
ref_31024 = (((ref_31022 & 0xFFFFFFFF) + (ref_31010 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_31271 = (ref_31024 & 0xFFFFFFFF) # MOV operation
ref_31280 = ((((0x0) << 32 | (ref_31271 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_31282 = (ref_31280 & 0xFFFFFFFF) # MOV operation
ref_31350 = (ref_31282 & 0xFFFFFFFF) # MOV operation
ref_32697 = (ref_31350 & 0xFFFFFFFF) # MOV operation
ref_32825 = (ref_32697 & 0xFFFFFFFF) # MOV operation
ref_32833 = (((ref_32825 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_32840 = (ref_32833 & 0xFFFFFFFF) # MOV operation
ref_32996 = (ref_30582 & 0xFFFFFFFF) # MOV operation
ref_33044 = (ref_32840 & 0xFFFFFFFF) # MOV operation
ref_33048 = (ref_32996 & 0xFFFFFFFF) # MOV operation
ref_33050 = ((ref_33048 & 0xFFFFFFFF) | (ref_33044 & 0xFFFFFFFF)) # OR operation
ref_33123 = (ref_33050 & 0xFFFFFFFF) # MOV operation
ref_33338 = (ref_33123 & 0xFFFFFFFF) # MOV operation
ref_33374 = (ref_33338 & 0xFFFFFFFF) # MOV operation
ref_33398 = (ref_33374 & 0xFFFFFFFF) # MOV operation
ref_33406 = (ref_33398 & 0xFFFFFFFF) # MOV operation
ref_33408 = (ref_33406 & 0xFFFFFFFF) # MOV operation

print(ref_33408 & 0xffffffffffffffff)
