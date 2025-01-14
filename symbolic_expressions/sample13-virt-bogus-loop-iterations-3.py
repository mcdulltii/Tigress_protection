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
ref_495553 = ref_239 # MOV operation
ref_495557 = ((0xDEADBEEFDEADBEEF + ref_495553) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_495664 = ref_495557 # MOV operation
ref_495666 = (0xE6ADBEEFDEADBEEF ^ ref_495664) # XOR operation
ref_495687 = ref_495557 # MOV operation
ref_495691 = ref_495687 # MOV operation
ref_495735 = ref_495691 # MOV operation
ref_495739 = rol(0xF, ref_495735) # ROL operation
ref_495743 = ref_495739 # MOV operation
ref_495750 = ref_495743 # MOV operation
ref_495766 = ref_495666 # MOV operation
ref_495770 = ref_495750 # MOV operation
ref_495772 = ((ref_495766 + ref_495770) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_495798 = ref_495772 # MOV operation
ref_495800 = (0x1234 ^ ref_495798) # XOR operation
ref_495821 = ref_495772 # MOV operation
ref_495825 = ref_495821 # MOV operation
ref_495869 = ref_495825 # MOV operation
ref_495873 = rol(0x34, ref_495869) # ROL operation
ref_495877 = ref_495873 # MOV operation
ref_495884 = ref_495877 # MOV operation
ref_495900 = ref_495800 # MOV operation
ref_495904 = ref_495884 # MOV operation
ref_495906 = ((ref_495900 + ref_495904) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_495932 = ref_495906 # MOV operation
ref_495934 = (0x1234 ^ ref_495932) # XOR operation
ref_495955 = ref_495906 # MOV operation
ref_495959 = ref_495955 # MOV operation
ref_496003 = ref_495959 # MOV operation
ref_496007 = rol(0x1A, ref_496003) # ROL operation
ref_496011 = ref_496007 # MOV operation
ref_496018 = ref_496011 # MOV operation
ref_496034 = ref_495934 # MOV operation
ref_496038 = ref_496018 # MOV operation
ref_496040 = ((ref_496034 + ref_496038) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_496062 = ref_495750 # MOV operation
ref_496066 = ref_496040 # MOV operation
ref_496068 = (ref_496062 ^ ref_496066) # XOR operation
ref_496089 = ref_496040 # MOV operation
ref_496093 = ref_496089 # MOV operation
ref_496137 = ref_496093 # MOV operation
ref_496141 = rol(0x33, ref_496137) # ROL operation
ref_496145 = ref_496141 # MOV operation
ref_496152 = ref_496145 # MOV operation
ref_496168 = ref_496068 # MOV operation
ref_496172 = ref_496152 # MOV operation
ref_496174 = ((ref_496168 + ref_496172) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_496196 = ref_495884 # MOV operation
ref_496200 = ref_496174 # MOV operation
ref_496202 = (ref_496196 ^ ref_496200) # XOR operation
ref_496223 = ref_496174 # MOV operation
ref_496227 = ref_496223 # MOV operation
ref_496271 = ref_496227 # MOV operation
ref_496275 = rol(0x1C, ref_496271) # ROL operation
ref_496279 = ref_496275 # MOV operation
ref_496286 = ref_496279 # MOV operation
ref_496302 = ref_496202 # MOV operation
ref_496306 = ref_496286 # MOV operation
ref_496308 = ((ref_496302 + ref_496306) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_496330 = ref_496018 # MOV operation
ref_496334 = ref_496308 # MOV operation
ref_496336 = (ref_496330 ^ ref_496334) # XOR operation
ref_496357 = ref_496308 # MOV operation
ref_496361 = ref_496357 # MOV operation
ref_496405 = ref_496361 # MOV operation
ref_496409 = rol(0x9, ref_496405) # ROL operation
ref_496413 = ref_496409 # MOV operation
ref_496420 = ref_496413 # MOV operation
ref_496436 = ref_496336 # MOV operation
ref_496440 = ref_496420 # MOV operation
ref_496442 = ((ref_496436 + ref_496440) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_496464 = ref_496152 # MOV operation
ref_496468 = ref_496442 # MOV operation
ref_496470 = (ref_496464 ^ ref_496468) # XOR operation
ref_496491 = ref_496442 # MOV operation
ref_496495 = ref_496491 # MOV operation
ref_496539 = ref_496495 # MOV operation
ref_496543 = rol(0x2F, ref_496539) # ROL operation
ref_496547 = ref_496543 # MOV operation
ref_496554 = ref_496547 # MOV operation
ref_496570 = ref_496470 # MOV operation
ref_496574 = ref_496554 # MOV operation
ref_496576 = ((ref_496570 + ref_496574) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_496598 = ref_496286 # MOV operation
ref_496602 = ref_496576 # MOV operation
ref_496604 = (ref_496598 ^ ref_496602) # XOR operation
ref_496625 = ref_496576 # MOV operation
ref_496629 = ref_496625 # MOV operation
ref_496673 = ref_496629 # MOV operation
ref_496677 = rol(0x36, ref_496673) # ROL operation
ref_496681 = ref_496677 # MOV operation
ref_496688 = ref_496681 # MOV operation
ref_496704 = ref_496604 # MOV operation
ref_496708 = ref_496688 # MOV operation
ref_496710 = ((ref_496704 + ref_496708) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_496732 = ref_496420 # MOV operation
ref_496736 = ref_496710 # MOV operation
ref_496738 = (ref_496732 ^ ref_496736) # XOR operation
ref_496759 = ref_496710 # MOV operation
ref_496763 = ref_496759 # MOV operation
ref_496807 = ref_496763 # MOV operation
ref_496811 = rol(0x20, ref_496807) # ROL operation
ref_496815 = ref_496811 # MOV operation
ref_496822 = ref_496815 # MOV operation
ref_496838 = ref_496738 # MOV operation
ref_496842 = ref_496822 # MOV operation
ref_496844 = ((ref_496838 + ref_496842) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_496866 = ref_496554 # MOV operation
ref_496870 = ref_496844 # MOV operation
ref_496872 = (ref_496866 ^ ref_496870) # XOR operation
ref_496893 = ref_496844 # MOV operation
ref_496897 = ref_496893 # MOV operation
ref_496941 = ref_496897 # MOV operation
ref_496945 = rol(0x19, ref_496941) # ROL operation
ref_496949 = ref_496945 # MOV operation
ref_496956 = ref_496949 # MOV operation
ref_496972 = ref_496872 # MOV operation
ref_496976 = ref_496956 # MOV operation
ref_496978 = ((ref_496972 + ref_496976) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_497027 = ref_496978 # MOV operation
ref_497031 = ref_497027 # MOV operation
ref_497075 = ref_497031 # MOV operation
ref_497079 = rol(0x3F, ref_497075) # ROL operation
ref_497083 = ref_497079 # MOV operation
ref_497090 = ref_497083 # MOV operation
ref_497139 = ref_497090 # MOV operation
ref_497201 = ref_497139 # MOV operation
ref_742484 = ref_497201 # MOV operation
ref_824227 = ref_742484 # MOV operation
ref_1069485 = ref_824227 # MOV operation
ref_1151225 = ref_1069485 # MOV operation
ref_1151263 = ref_1151225 # MOV operation
ref_1151275 = ref_1151263 # MOV operation
ref_1151277 = ref_1151275 # MOV operation

print(ref_1151277 & 0xffffffffffffffff)
