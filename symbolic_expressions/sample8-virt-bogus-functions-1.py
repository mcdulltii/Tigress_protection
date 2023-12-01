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
ref_56765 = ref_239 # MOV operation
ref_56809 = ref_56765 # MOV operation
ref_56844 = (((((((((0x7B) << 8 | 0x6B) << 8 | 0x69) << 8 | 0x6E) << 8 | 0x72) << 8 | 0x7E) << 8 | 0x6C) << 8 | 0x7B) ^ ref_56809) # MOV operation
ref_56885 = (((((((((0x7B) << 8 | 0x6B) << 8 | 0x69) << 8 | 0x6E) << 8 | 0x72) << 8 | 0x7E) << 8 | 0x6C) << 8 | 0x7B) ^ ref_56809) # MOV operation
ref_56887 = rol(0x10, ref_56885) # ROL operation
ref_56891 = (ref_56887 ^ ((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_56844) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_56938 = ref_56891 # MOV operation
ref_56962 = (0x96C62826CF6DE04E ^ ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_56844) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_56979 = ref_56891 # MOV operation
ref_56981 = rol(0x15, ref_56979) # ROL operation
ref_56985 = (ref_56981 ^ ((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_56938) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_57014 = ref_56962 # MOV operation
ref_57032 = ref_56985 # MOV operation
ref_57050 = ref_56962 # MOV operation
ref_57052 = rol(0xD, ref_57050) # ROL operation
ref_57056 = (ref_57052 ^ ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_56938) & 0xFFFFFFFFFFFFFFFF) + ref_57014) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_57073 = ref_56985 # MOV operation
ref_57075 = rol(0x10, ref_57073) # ROL operation
ref_57079 = (ref_57075 ^ ((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_56844) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_57032) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_57108 = ref_57056 # MOV operation
ref_57126 = ref_57079 # MOV operation
ref_57144 = ref_57056 # MOV operation
ref_57146 = rol(0x11, ref_57144) # ROL operation
ref_57150 = (ref_57146 ^ ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_56844) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_57032) & 0xFFFFFFFFFFFFFFFF) + ref_57108) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_57167 = ref_57079 # MOV operation
ref_57169 = rol(0x15, ref_57167) # ROL operation
ref_57173 = (ref_57169 ^ ((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_56938) & 0xFFFFFFFFFFFFFFFF) + ref_57014) & 0xFFFFFFFFFFFFFFFF)) + ref_57126) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_57202 = ref_56765 # MOV operation
ref_57326 = ref_57150 # MOV operation
ref_57344 = (ref_57173 ^ 0x800000000000000) # MOV operation
ref_57362 = ref_57150 # MOV operation
ref_57364 = rol(0xD, ref_57362) # ROL operation
ref_57368 = (ref_57364 ^ (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_56938) & 0xFFFFFFFFFFFFFFFF) + ref_57014) & 0xFFFFFFFFFFFFFFFF)) + ref_57126) & 0xFFFFFFFFFFFFFFFF) ^ ref_57202) + ref_57326) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_57385 = (ref_57173 ^ 0x800000000000000) # MOV operation
ref_57387 = rol(0x10, ref_57385) # ROL operation
ref_57391 = (ref_57387 ^ ((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_56844) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_57032) & 0xFFFFFFFFFFFFFFFF) + ref_57108) & 0xFFFFFFFFFFFFFFFF)) + ref_57344) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_57420 = ref_57368 # MOV operation
ref_57438 = ref_57391 # MOV operation
ref_57456 = ref_57368 # MOV operation
ref_57458 = rol(0x11, ref_57456) # ROL operation
ref_57462 = (ref_57458 ^ ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_56844) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_57032) & 0xFFFFFFFFFFFFFFFF) + ref_57108) & 0xFFFFFFFFFFFFFFFF)) + ref_57344) & 0xFFFFFFFFFFFFFFFF) + ref_57420) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_57479 = ref_57391 # MOV operation
ref_57481 = rol(0x15, ref_57479) # ROL operation
ref_57485 = (ref_57481 ^ ((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_56938) & 0xFFFFFFFFFFFFFFFF) + ref_57014) & 0xFFFFFFFFFFFFFFFF)) + ref_57126) & 0xFFFFFFFFFFFFFFFF) ^ ref_57202) + ref_57326) & 0xFFFFFFFFFFFFFFFF)) + ref_57438) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_57514 = ref_57462 # MOV operation
ref_57532 = ref_57485 # MOV operation
ref_57550 = ref_57462 # MOV operation
ref_57552 = rol(0xD, ref_57550) # ROL operation
ref_57556 = (ref_57552 ^ ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_56938) & 0xFFFFFFFFFFFFFFFF) + ref_57014) & 0xFFFFFFFFFFFFFFFF)) + ref_57126) & 0xFFFFFFFFFFFFFFFF) ^ ref_57202) + ref_57326) & 0xFFFFFFFFFFFFFFFF)) + ref_57438) & 0xFFFFFFFFFFFFFFFF) + ref_57514) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_57573 = ref_57485 # MOV operation
ref_57575 = rol(0x10, ref_57573) # ROL operation
ref_57579 = (ref_57575 ^ ((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_56844) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_57032) & 0xFFFFFFFFFFFFFFFF) + ref_57108) & 0xFFFFFFFFFFFFFFFF)) + ref_57344) & 0xFFFFFFFFFFFFFFFF) + ref_57420) & 0xFFFFFFFFFFFFFFFF)) + ref_57532) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_57608 = ref_57556 # MOV operation
ref_57626 = ref_57579 # MOV operation
ref_57644 = ref_57556 # MOV operation
ref_57646 = rol(0x11, ref_57644) # ROL operation
ref_57650 = (ref_57646 ^ ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_56844) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_57032) & 0xFFFFFFFFFFFFFFFF) + ref_57108) & 0xFFFFFFFFFFFFFFFF)) + ref_57344) & 0xFFFFFFFFFFFFFFFF) + ref_57420) & 0xFFFFFFFFFFFFFFFF)) + ref_57532) & 0xFFFFFFFFFFFFFFFF) + ref_57608) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_57667 = ref_57579 # MOV operation
ref_57669 = rol(0x15, ref_57667) # ROL operation
ref_57673 = (ref_57669 ^ ((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_56938) & 0xFFFFFFFFFFFFFFFF) + ref_57014) & 0xFFFFFFFFFFFFFFFF)) + ref_57126) & 0xFFFFFFFFFFFFFFFF) ^ ref_57202) + ref_57326) & 0xFFFFFFFFFFFFFFFF)) + ref_57438) & 0xFFFFFFFFFFFFFFFF) + ref_57514) & 0xFFFFFFFFFFFFFFFF)) + ref_57626) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_57734 = ref_57650 # MOV operation
ref_57752 = ref_57673 # MOV operation
ref_57770 = ref_57650 # MOV operation
ref_57772 = rol(0xD, ref_57770) # ROL operation
ref_57776 = (ref_57772 ^ (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_56938) & 0xFFFFFFFFFFFFFFFF) + ref_57014) & 0xFFFFFFFFFFFFFFFF)) + ref_57126) & 0xFFFFFFFFFFFFFFFF) ^ ref_57202) + ref_57326) & 0xFFFFFFFFFFFFFFFF)) + ref_57438) & 0xFFFFFFFFFFFFFFFF) + ref_57514) & 0xFFFFFFFFFFFFFFFF)) + ref_57626) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_57734) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_57793 = ref_57673 # MOV operation
ref_57795 = rol(0x10, ref_57793) # ROL operation
ref_57799 = (ref_57795 ^ (((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_56844) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_57032) & 0xFFFFFFFFFFFFFFFF) + ref_57108) & 0xFFFFFFFFFFFFFFFF)) + ref_57344) & 0xFFFFFFFFFFFFFFFF) + ref_57420) & 0xFFFFFFFFFFFFFFFF)) + ref_57532) & 0xFFFFFFFFFFFFFFFF) + ref_57608) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_57752) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_57828 = ref_57776 # MOV operation
ref_57846 = ref_57799 # MOV operation
ref_57864 = ref_57776 # MOV operation
ref_57866 = rol(0x11, ref_57864) # ROL operation
ref_57870 = (ref_57866 ^ (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_56844) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_57032) & 0xFFFFFFFFFFFFFFFF) + ref_57108) & 0xFFFFFFFFFFFFFFFF)) + ref_57344) & 0xFFFFFFFFFFFFFFFF) + ref_57420) & 0xFFFFFFFFFFFFFFFF)) + ref_57532) & 0xFFFFFFFFFFFFFFFF) + ref_57608) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_57752) & 0xFFFFFFFFFFFFFFFF) + ref_57828) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_57887 = ref_57799 # MOV operation
ref_57889 = rol(0x15, ref_57887) # ROL operation
ref_57893 = (ref_57889 ^ ((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_56938) & 0xFFFFFFFFFFFFFFFF) + ref_57014) & 0xFFFFFFFFFFFFFFFF)) + ref_57126) & 0xFFFFFFFFFFFFFFFF) ^ ref_57202) + ref_57326) & 0xFFFFFFFFFFFFFFFF)) + ref_57438) & 0xFFFFFFFFFFFFFFFF) + ref_57514) & 0xFFFFFFFFFFFFFFFF)) + ref_57626) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_57734) & 0xFFFFFFFFFFFFFFFF)) + ref_57846) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_57922 = ref_57870 # MOV operation
ref_57940 = ref_57893 # MOV operation
ref_57958 = ref_57870 # MOV operation
ref_57960 = rol(0xD, ref_57958) # ROL operation
ref_57964 = (ref_57960 ^ ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_56938) & 0xFFFFFFFFFFFFFFFF) + ref_57014) & 0xFFFFFFFFFFFFFFFF)) + ref_57126) & 0xFFFFFFFFFFFFFFFF) ^ ref_57202) + ref_57326) & 0xFFFFFFFFFFFFFFFF)) + ref_57438) & 0xFFFFFFFFFFFFFFFF) + ref_57514) & 0xFFFFFFFFFFFFFFFF)) + ref_57626) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_57734) & 0xFFFFFFFFFFFFFFFF)) + ref_57846) & 0xFFFFFFFFFFFFFFFF) + ref_57922) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_57981 = ref_57893 # MOV operation
ref_57983 = rol(0x10, ref_57981) # ROL operation
ref_57987 = (ref_57983 ^ ((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_56844) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_57032) & 0xFFFFFFFFFFFFFFFF) + ref_57108) & 0xFFFFFFFFFFFFFFFF)) + ref_57344) & 0xFFFFFFFFFFFFFFFF) + ref_57420) & 0xFFFFFFFFFFFFFFFF)) + ref_57532) & 0xFFFFFFFFFFFFFFFF) + ref_57608) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_57752) & 0xFFFFFFFFFFFFFFFF) + ref_57828) & 0xFFFFFFFFFFFFFFFF)) + ref_57940) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_58016 = ref_57964 # MOV operation
ref_58034 = ref_57987 # MOV operation
ref_58052 = ref_57964 # MOV operation
ref_58054 = rol(0x11, ref_58052) # ROL operation
ref_58058 = (ref_58054 ^ ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_56844) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_57032) & 0xFFFFFFFFFFFFFFFF) + ref_57108) & 0xFFFFFFFFFFFFFFFF)) + ref_57344) & 0xFFFFFFFFFFFFFFFF) + ref_57420) & 0xFFFFFFFFFFFFFFFF)) + ref_57532) & 0xFFFFFFFFFFFFFFFF) + ref_57608) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_57752) & 0xFFFFFFFFFFFFFFFF) + ref_57828) & 0xFFFFFFFFFFFFFFFF)) + ref_57940) & 0xFFFFFFFFFFFFFFFF) + ref_58016) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_58075 = ref_57987 # MOV operation
ref_58077 = rol(0x15, ref_58075) # ROL operation
ref_58081 = (ref_58077 ^ ((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_56938) & 0xFFFFFFFFFFFFFFFF) + ref_57014) & 0xFFFFFFFFFFFFFFFF)) + ref_57126) & 0xFFFFFFFFFFFFFFFF) ^ ref_57202) + ref_57326) & 0xFFFFFFFFFFFFFFFF)) + ref_57438) & 0xFFFFFFFFFFFFFFFF) + ref_57514) & 0xFFFFFFFFFFFFFFFF)) + ref_57626) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_57734) & 0xFFFFFFFFFFFFFFFF)) + ref_57846) & 0xFFFFFFFFFFFFFFFF) + ref_57922) & 0xFFFFFFFFFFFFFFFF)) + ref_58034) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_58110 = ref_58058 # MOV operation
ref_58128 = ref_58081 # MOV operation
ref_58146 = ref_58058 # MOV operation
ref_58148 = rol(0xD, ref_58146) # ROL operation
ref_58152 = (ref_58148 ^ ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_56938) & 0xFFFFFFFFFFFFFFFF) + ref_57014) & 0xFFFFFFFFFFFFFFFF)) + ref_57126) & 0xFFFFFFFFFFFFFFFF) ^ ref_57202) + ref_57326) & 0xFFFFFFFFFFFFFFFF)) + ref_57438) & 0xFFFFFFFFFFFFFFFF) + ref_57514) & 0xFFFFFFFFFFFFFFFF)) + ref_57626) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_57734) & 0xFFFFFFFFFFFFFFFF)) + ref_57846) & 0xFFFFFFFFFFFFFFFF) + ref_57922) & 0xFFFFFFFFFFFFFFFF)) + ref_58034) & 0xFFFFFFFFFFFFFFFF) + ref_58110) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_58169 = ref_58081 # MOV operation
ref_58171 = rol(0x10, ref_58169) # ROL operation
ref_58175 = (ref_58171 ^ ((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_56844) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_57032) & 0xFFFFFFFFFFFFFFFF) + ref_57108) & 0xFFFFFFFFFFFFFFFF)) + ref_57344) & 0xFFFFFFFFFFFFFFFF) + ref_57420) & 0xFFFFFFFFFFFFFFFF)) + ref_57532) & 0xFFFFFFFFFFFFFFFF) + ref_57608) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_57752) & 0xFFFFFFFFFFFFFFFF) + ref_57828) & 0xFFFFFFFFFFFFFFFF)) + ref_57940) & 0xFFFFFFFFFFFFFFFF) + ref_58016) & 0xFFFFFFFFFFFFFFFF)) + ref_58128) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_58204 = ref_58152 # MOV operation
ref_58222 = ref_58175 # MOV operation
ref_58240 = ref_58152 # MOV operation
ref_58242 = rol(0x11, ref_58240) # ROL operation
ref_58246 = (ref_58242 ^ ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_56844) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_57032) & 0xFFFFFFFFFFFFFFFF) + ref_57108) & 0xFFFFFFFFFFFFFFFF)) + ref_57344) & 0xFFFFFFFFFFFFFFFF) + ref_57420) & 0xFFFFFFFFFFFFFFFF)) + ref_57532) & 0xFFFFFFFFFFFFFFFF) + ref_57608) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_57752) & 0xFFFFFFFFFFFFFFFF) + ref_57828) & 0xFFFFFFFFFFFFFFFF)) + ref_57940) & 0xFFFFFFFFFFFFFFFF) + ref_58016) & 0xFFFFFFFFFFFFFFFF)) + ref_58128) & 0xFFFFFFFFFFFFFFFF) + ref_58204) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_58263 = ref_58175 # MOV operation
ref_58265 = rol(0x15, ref_58263) # ROL operation
ref_58269 = (ref_58265 ^ ((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_56938) & 0xFFFFFFFFFFFFFFFF) + ref_57014) & 0xFFFFFFFFFFFFFFFF)) + ref_57126) & 0xFFFFFFFFFFFFFFFF) ^ ref_57202) + ref_57326) & 0xFFFFFFFFFFFFFFFF)) + ref_57438) & 0xFFFFFFFFFFFFFFFF) + ref_57514) & 0xFFFFFFFFFFFFFFFF)) + ref_57626) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_57734) & 0xFFFFFFFFFFFFFFFF)) + ref_57846) & 0xFFFFFFFFFFFFFFFF) + ref_57922) & 0xFFFFFFFFFFFFFFFF)) + ref_58034) & 0xFFFFFFFFFFFFFFFF) + ref_58110) & 0xFFFFFFFFFFFFFFFF)) + ref_58222) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_58298 = ref_58246 # MOV operation
ref_58316 = ref_58269 # MOV operation
ref_58334 = ref_58246 # MOV operation
ref_58336 = rol(0xD, ref_58334) # ROL operation
ref_58340 = (ref_58336 ^ ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_56938) & 0xFFFFFFFFFFFFFFFF) + ref_57014) & 0xFFFFFFFFFFFFFFFF)) + ref_57126) & 0xFFFFFFFFFFFFFFFF) ^ ref_57202) + ref_57326) & 0xFFFFFFFFFFFFFFFF)) + ref_57438) & 0xFFFFFFFFFFFFFFFF) + ref_57514) & 0xFFFFFFFFFFFFFFFF)) + ref_57626) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_57734) & 0xFFFFFFFFFFFFFFFF)) + ref_57846) & 0xFFFFFFFFFFFFFFFF) + ref_57922) & 0xFFFFFFFFFFFFFFFF)) + ref_58034) & 0xFFFFFFFFFFFFFFFF) + ref_58110) & 0xFFFFFFFFFFFFFFFF)) + ref_58222) & 0xFFFFFFFFFFFFFFFF) + ref_58298) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_58357 = ref_58269 # MOV operation
ref_58359 = rol(0x10, ref_58357) # ROL operation
ref_58363 = (ref_58359 ^ ((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_56844) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_57032) & 0xFFFFFFFFFFFFFFFF) + ref_57108) & 0xFFFFFFFFFFFFFFFF)) + ref_57344) & 0xFFFFFFFFFFFFFFFF) + ref_57420) & 0xFFFFFFFFFFFFFFFF)) + ref_57532) & 0xFFFFFFFFFFFFFFFF) + ref_57608) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_57752) & 0xFFFFFFFFFFFFFFFF) + ref_57828) & 0xFFFFFFFFFFFFFFFF)) + ref_57940) & 0xFFFFFFFFFFFFFFFF) + ref_58016) & 0xFFFFFFFFFFFFFFFF)) + ref_58128) & 0xFFFFFFFFFFFFFFFF) + ref_58204) & 0xFFFFFFFFFFFFFFFF)) + ref_58316) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_58392 = ref_58340 # MOV operation
ref_58410 = ref_58363 # MOV operation
ref_58428 = ref_58340 # MOV operation
ref_58430 = rol(0x11, ref_58428) # ROL operation
ref_58434 = (ref_58430 ^ ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_56844) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_57032) & 0xFFFFFFFFFFFFFFFF) + ref_57108) & 0xFFFFFFFFFFFFFFFF)) + ref_57344) & 0xFFFFFFFFFFFFFFFF) + ref_57420) & 0xFFFFFFFFFFFFFFFF)) + ref_57532) & 0xFFFFFFFFFFFFFFFF) + ref_57608) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_57752) & 0xFFFFFFFFFFFFFFFF) + ref_57828) & 0xFFFFFFFFFFFFFFFF)) + ref_57940) & 0xFFFFFFFFFFFFFFFF) + ref_58016) & 0xFFFFFFFFFFFFFFFF)) + ref_58128) & 0xFFFFFFFFFFFFFFFF) + ref_58204) & 0xFFFFFFFFFFFFFFFF)) + ref_58316) & 0xFFFFFFFFFFFFFFFF) + ref_58392) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_58451 = ref_58363 # MOV operation
ref_58453 = rol(0x15, ref_58451) # ROL operation
ref_58457 = (ref_58453 ^ ((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_56938) & 0xFFFFFFFFFFFFFFFF) + ref_57014) & 0xFFFFFFFFFFFFFFFF)) + ref_57126) & 0xFFFFFFFFFFFFFFFF) ^ ref_57202) + ref_57326) & 0xFFFFFFFFFFFFFFFF)) + ref_57438) & 0xFFFFFFFFFFFFFFFF) + ref_57514) & 0xFFFFFFFFFFFFFFFF)) + ref_57626) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_57734) & 0xFFFFFFFFFFFFFFFF)) + ref_57846) & 0xFFFFFFFFFFFFFFFF) + ref_57922) & 0xFFFFFFFFFFFFFFFF)) + ref_58034) & 0xFFFFFFFFFFFFFFFF) + ref_58110) & 0xFFFFFFFFFFFFFFFF)) + ref_58222) & 0xFFFFFFFFFFFFFFFF) + ref_58298) & 0xFFFFFFFFFFFFFFFF)) + ref_58410) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_58486 = ((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_56938) & 0xFFFFFFFFFFFFFFFF) + ref_57014) & 0xFFFFFFFFFFFFFFFF)) + ref_57126) & 0xFFFFFFFFFFFFFFFF) ^ ref_57202) + ref_57326) & 0xFFFFFFFFFFFFFFFF)) + ref_57438) & 0xFFFFFFFFFFFFFFFF) + ref_57514) & 0xFFFFFFFFFFFFFFFF)) + ref_57626) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_57734) & 0xFFFFFFFFFFFFFFFF)) + ref_57846) & 0xFFFFFFFFFFFFFFFF) + ref_57922) & 0xFFFFFFFFFFFFFFFF)) + ref_58034) & 0xFFFFFFFFFFFFFFFF) + ref_58110) & 0xFFFFFFFFFFFFFFFF)) + ref_58222) & 0xFFFFFFFFFFFFFFFF) + ref_58298) & 0xFFFFFFFFFFFFFFFF)) + ref_58410) & 0xFFFFFFFFFFFFFFFF) # MOV operation
ref_58488 = (ref_58486 ^ ref_58434) # XOR operation
ref_58495 = ref_58488 # MOV operation
ref_58497 = rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_56844) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_57032) & 0xFFFFFFFFFFFFFFFF) + ref_57108) & 0xFFFFFFFFFFFFFFFF)) + ref_57344) & 0xFFFFFFFFFFFFFFFF) + ref_57420) & 0xFFFFFFFFFFFFFFFF)) + ref_57532) & 0xFFFFFFFFFFFFFFFF) + ref_57608) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_57752) & 0xFFFFFFFFFFFFFFFF) + ref_57828) & 0xFFFFFFFFFFFFFFFF)) + ref_57940) & 0xFFFFFFFFFFFFFFFF) + ref_58016) & 0xFFFFFFFFFFFFFFFF)) + ref_58128) & 0xFFFFFFFFFFFFFFFF) + ref_58204) & 0xFFFFFFFFFFFFFFFF)) + ref_58316) & 0xFFFFFFFFFFFFFFFF) + ref_58392) & 0xFFFFFFFFFFFFFFFF)) # MOV operation
ref_58499 = (ref_58497 ^ ref_58457) # XOR operation
ref_58506 = (ref_58499 ^ ref_58495) # XOR operation
ref_59520 = ref_58506 # MOV operation
ref_59778 = ref_59520 # MOV operation
ref_60701 = ref_59778 # MOV operation
ref_60977 = ref_60701 # MOV operation
ref_61018 = ref_60977 # MOV operation
ref_61030 = ref_61018 # MOV operation
ref_61032 = ref_61030 # MOV operation

print(ref_61032 & 0xffffffffffffffff)
