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
ref_6777 = ref_239 # MOV operation
ref_6781 = ((0xDEADBEEFDEADBEEF + ref_6777) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_6888 = ref_6781 # MOV operation
ref_6890 = (0xE6ADBEEFDEADBEEF ^ ref_6888) # XOR operation
ref_6911 = ref_6781 # MOV operation
ref_6915 = ref_6911 # MOV operation
ref_6959 = ref_6915 # MOV operation
ref_6963 = rol(0xF, ref_6959) # ROL operation
ref_6967 = ref_6963 # MOV operation
ref_6974 = ref_6967 # MOV operation
ref_6990 = ref_6890 # MOV operation
ref_6994 = ref_6974 # MOV operation
ref_6996 = ((ref_6990 + ref_6994) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_7022 = ref_6996 # MOV operation
ref_7024 = (0x1234 ^ ref_7022) # XOR operation
ref_7045 = ref_6996 # MOV operation
ref_7049 = ref_7045 # MOV operation
ref_7093 = ref_7049 # MOV operation
ref_7097 = rol(0x34, ref_7093) # ROL operation
ref_7101 = ref_7097 # MOV operation
ref_7108 = ref_7101 # MOV operation
ref_7124 = ref_7024 # MOV operation
ref_7128 = ref_7108 # MOV operation
ref_7130 = ((ref_7124 + ref_7128) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_7156 = ref_7130 # MOV operation
ref_7158 = (0x1234 ^ ref_7156) # XOR operation
ref_7179 = ref_7130 # MOV operation
ref_7183 = ref_7179 # MOV operation
ref_7227 = ref_7183 # MOV operation
ref_7231 = rol(0x1A, ref_7227) # ROL operation
ref_7235 = ref_7231 # MOV operation
ref_7242 = ref_7235 # MOV operation
ref_7258 = ref_7158 # MOV operation
ref_7262 = ref_7242 # MOV operation
ref_7264 = ((ref_7258 + ref_7262) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_7286 = ref_6974 # MOV operation
ref_7290 = ref_7264 # MOV operation
ref_7292 = (ref_7286 ^ ref_7290) # XOR operation
ref_7313 = ref_7264 # MOV operation
ref_7317 = ref_7313 # MOV operation
ref_7361 = ref_7317 # MOV operation
ref_7365 = rol(0x33, ref_7361) # ROL operation
ref_7369 = ref_7365 # MOV operation
ref_7376 = ref_7369 # MOV operation
ref_7392 = ref_7292 # MOV operation
ref_7396 = ref_7376 # MOV operation
ref_7398 = ((ref_7392 + ref_7396) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_7420 = ref_7108 # MOV operation
ref_7424 = ref_7398 # MOV operation
ref_7426 = (ref_7420 ^ ref_7424) # XOR operation
ref_7447 = ref_7398 # MOV operation
ref_7451 = ref_7447 # MOV operation
ref_7495 = ref_7451 # MOV operation
ref_7499 = rol(0x1C, ref_7495) # ROL operation
ref_7503 = ref_7499 # MOV operation
ref_7510 = ref_7503 # MOV operation
ref_7526 = ref_7426 # MOV operation
ref_7530 = ref_7510 # MOV operation
ref_7532 = ((ref_7526 + ref_7530) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_7554 = ref_7242 # MOV operation
ref_7558 = ref_7532 # MOV operation
ref_7560 = (ref_7554 ^ ref_7558) # XOR operation
ref_7581 = ref_7532 # MOV operation
ref_7585 = ref_7581 # MOV operation
ref_7629 = ref_7585 # MOV operation
ref_7633 = rol(0x9, ref_7629) # ROL operation
ref_7637 = ref_7633 # MOV operation
ref_7644 = ref_7637 # MOV operation
ref_7660 = ref_7560 # MOV operation
ref_7664 = ref_7644 # MOV operation
ref_7666 = ((ref_7660 + ref_7664) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_7688 = ref_7376 # MOV operation
ref_7692 = ref_7666 # MOV operation
ref_7694 = (ref_7688 ^ ref_7692) # XOR operation
ref_7715 = ref_7666 # MOV operation
ref_7719 = ref_7715 # MOV operation
ref_7763 = ref_7719 # MOV operation
ref_7767 = rol(0x2F, ref_7763) # ROL operation
ref_7771 = ref_7767 # MOV operation
ref_7778 = ref_7771 # MOV operation
ref_7794 = ref_7694 # MOV operation
ref_7798 = ref_7778 # MOV operation
ref_7800 = ((ref_7794 + ref_7798) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_7822 = ref_7510 # MOV operation
ref_7826 = ref_7800 # MOV operation
ref_7828 = (ref_7822 ^ ref_7826) # XOR operation
ref_7849 = ref_7800 # MOV operation
ref_7853 = ref_7849 # MOV operation
ref_7897 = ref_7853 # MOV operation
ref_7901 = rol(0x36, ref_7897) # ROL operation
ref_7905 = ref_7901 # MOV operation
ref_7912 = ref_7905 # MOV operation
ref_7928 = ref_7828 # MOV operation
ref_7932 = ref_7912 # MOV operation
ref_7934 = ((ref_7928 + ref_7932) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_7956 = ref_7644 # MOV operation
ref_7960 = ref_7934 # MOV operation
ref_7962 = (ref_7956 ^ ref_7960) # XOR operation
ref_7983 = ref_7934 # MOV operation
ref_7987 = ref_7983 # MOV operation
ref_8031 = ref_7987 # MOV operation
ref_8035 = rol(0x20, ref_8031) # ROL operation
ref_8039 = ref_8035 # MOV operation
ref_8046 = ref_8039 # MOV operation
ref_8062 = ref_7962 # MOV operation
ref_8066 = ref_8046 # MOV operation
ref_8068 = ((ref_8062 + ref_8066) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_8090 = ref_7778 # MOV operation
ref_8094 = ref_8068 # MOV operation
ref_8096 = (ref_8090 ^ ref_8094) # XOR operation
ref_8117 = ref_8068 # MOV operation
ref_8121 = ref_8117 # MOV operation
ref_8165 = ref_8121 # MOV operation
ref_8169 = rol(0x19, ref_8165) # ROL operation
ref_8173 = ref_8169 # MOV operation
ref_8180 = ref_8173 # MOV operation
ref_8196 = ref_8096 # MOV operation
ref_8200 = ref_8180 # MOV operation
ref_8202 = ((ref_8196 + ref_8200) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_8251 = ref_8202 # MOV operation
ref_8255 = ref_8251 # MOV operation
ref_8299 = ref_8255 # MOV operation
ref_8303 = rol(0x3F, ref_8299) # ROL operation
ref_8307 = ref_8303 # MOV operation
ref_8314 = ref_8307 # MOV operation
ref_8363 = ref_8314 # MOV operation
ref_8425 = ref_8363 # MOV operation
ref_9394 = ref_8425 # MOV operation
ref_9658 = ref_9394 # MOV operation
ref_10555 = ref_9658 # MOV operation
ref_10877 = ref_10555 # MOV operation
ref_10918 = ref_10877 # MOV operation
ref_10930 = ref_10918 # MOV operation
ref_10932 = ref_10930 # MOV operation

print(ref_10932 & 0xffffffffffffffff)
