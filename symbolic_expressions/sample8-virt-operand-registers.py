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
ref_25531 = ref_239 # MOV operation
ref_25575 = ref_25531 # MOV operation
ref_25610 = (((((((((0x7B) << 8 | 0x6B) << 8 | 0x69) << 8 | 0x6E) << 8 | 0x72) << 8 | 0x7E) << 8 | 0x6C) << 8 | 0x7B) ^ ref_25575) # MOV operation
ref_25651 = (((((((((0x7B) << 8 | 0x6B) << 8 | 0x69) << 8 | 0x6E) << 8 | 0x72) << 8 | 0x7E) << 8 | 0x6C) << 8 | 0x7B) ^ ref_25575) # MOV operation
ref_25653 = rol(0x10, ref_25651) # ROL operation
ref_25657 = (ref_25653 ^ ((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_25610) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_25704 = ref_25657 # MOV operation
ref_25728 = (0x96C62826CF6DE04E ^ ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_25610) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_25745 = ref_25657 # MOV operation
ref_25747 = rol(0x15, ref_25745) # ROL operation
ref_25751 = (ref_25747 ^ ((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_25704) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_25780 = ref_25728 # MOV operation
ref_25798 = ref_25751 # MOV operation
ref_25816 = ref_25728 # MOV operation
ref_25818 = rol(0xD, ref_25816) # ROL operation
ref_25822 = (ref_25818 ^ ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_25704) & 0xFFFFFFFFFFFFFFFF) + ref_25780) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_25839 = ref_25751 # MOV operation
ref_25841 = rol(0x10, ref_25839) # ROL operation
ref_25845 = (ref_25841 ^ ((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_25610) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_25798) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_25874 = ref_25822 # MOV operation
ref_25892 = ref_25845 # MOV operation
ref_25910 = ref_25822 # MOV operation
ref_25912 = rol(0x11, ref_25910) # ROL operation
ref_25916 = (ref_25912 ^ ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_25610) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_25798) & 0xFFFFFFFFFFFFFFFF) + ref_25874) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_25933 = ref_25845 # MOV operation
ref_25935 = rol(0x15, ref_25933) # ROL operation
ref_25939 = (ref_25935 ^ ((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_25704) & 0xFFFFFFFFFFFFFFFF) + ref_25780) & 0xFFFFFFFFFFFFFFFF)) + ref_25892) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_25968 = ref_25531 # MOV operation
ref_26092 = ref_25916 # MOV operation
ref_26110 = (ref_25939 ^ 0x800000000000000) # MOV operation
ref_26128 = ref_25916 # MOV operation
ref_26130 = rol(0xD, ref_26128) # ROL operation
ref_26134 = (ref_26130 ^ (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_25704) & 0xFFFFFFFFFFFFFFFF) + ref_25780) & 0xFFFFFFFFFFFFFFFF)) + ref_25892) & 0xFFFFFFFFFFFFFFFF) ^ ref_25968) + ref_26092) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_26151 = (ref_25939 ^ 0x800000000000000) # MOV operation
ref_26153 = rol(0x10, ref_26151) # ROL operation
ref_26157 = (ref_26153 ^ ((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_25610) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_25798) & 0xFFFFFFFFFFFFFFFF) + ref_25874) & 0xFFFFFFFFFFFFFFFF)) + ref_26110) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_26186 = ref_26134 # MOV operation
ref_26204 = ref_26157 # MOV operation
ref_26222 = ref_26134 # MOV operation
ref_26224 = rol(0x11, ref_26222) # ROL operation
ref_26228 = (ref_26224 ^ ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_25610) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_25798) & 0xFFFFFFFFFFFFFFFF) + ref_25874) & 0xFFFFFFFFFFFFFFFF)) + ref_26110) & 0xFFFFFFFFFFFFFFFF) + ref_26186) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_26245 = ref_26157 # MOV operation
ref_26247 = rol(0x15, ref_26245) # ROL operation
ref_26251 = (ref_26247 ^ ((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_25704) & 0xFFFFFFFFFFFFFFFF) + ref_25780) & 0xFFFFFFFFFFFFFFFF)) + ref_25892) & 0xFFFFFFFFFFFFFFFF) ^ ref_25968) + ref_26092) & 0xFFFFFFFFFFFFFFFF)) + ref_26204) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_26280 = ref_26228 # MOV operation
ref_26298 = ref_26251 # MOV operation
ref_26316 = ref_26228 # MOV operation
ref_26318 = rol(0xD, ref_26316) # ROL operation
ref_26322 = (ref_26318 ^ ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_25704) & 0xFFFFFFFFFFFFFFFF) + ref_25780) & 0xFFFFFFFFFFFFFFFF)) + ref_25892) & 0xFFFFFFFFFFFFFFFF) ^ ref_25968) + ref_26092) & 0xFFFFFFFFFFFFFFFF)) + ref_26204) & 0xFFFFFFFFFFFFFFFF) + ref_26280) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_26339 = ref_26251 # MOV operation
ref_26341 = rol(0x10, ref_26339) # ROL operation
ref_26345 = (ref_26341 ^ ((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_25610) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_25798) & 0xFFFFFFFFFFFFFFFF) + ref_25874) & 0xFFFFFFFFFFFFFFFF)) + ref_26110) & 0xFFFFFFFFFFFFFFFF) + ref_26186) & 0xFFFFFFFFFFFFFFFF)) + ref_26298) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_26374 = ref_26322 # MOV operation
ref_26392 = ref_26345 # MOV operation
ref_26410 = ref_26322 # MOV operation
ref_26412 = rol(0x11, ref_26410) # ROL operation
ref_26416 = (ref_26412 ^ ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_25610) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_25798) & 0xFFFFFFFFFFFFFFFF) + ref_25874) & 0xFFFFFFFFFFFFFFFF)) + ref_26110) & 0xFFFFFFFFFFFFFFFF) + ref_26186) & 0xFFFFFFFFFFFFFFFF)) + ref_26298) & 0xFFFFFFFFFFFFFFFF) + ref_26374) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_26433 = ref_26345 # MOV operation
ref_26435 = rol(0x15, ref_26433) # ROL operation
ref_26439 = (ref_26435 ^ ((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_25704) & 0xFFFFFFFFFFFFFFFF) + ref_25780) & 0xFFFFFFFFFFFFFFFF)) + ref_25892) & 0xFFFFFFFFFFFFFFFF) ^ ref_25968) + ref_26092) & 0xFFFFFFFFFFFFFFFF)) + ref_26204) & 0xFFFFFFFFFFFFFFFF) + ref_26280) & 0xFFFFFFFFFFFFFFFF)) + ref_26392) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_26500 = ref_26416 # MOV operation
ref_26518 = ref_26439 # MOV operation
ref_26536 = ref_26416 # MOV operation
ref_26538 = rol(0xD, ref_26536) # ROL operation
ref_26542 = (ref_26538 ^ (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_25704) & 0xFFFFFFFFFFFFFFFF) + ref_25780) & 0xFFFFFFFFFFFFFFFF)) + ref_25892) & 0xFFFFFFFFFFFFFFFF) ^ ref_25968) + ref_26092) & 0xFFFFFFFFFFFFFFFF)) + ref_26204) & 0xFFFFFFFFFFFFFFFF) + ref_26280) & 0xFFFFFFFFFFFFFFFF)) + ref_26392) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_26500) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_26559 = ref_26439 # MOV operation
ref_26561 = rol(0x10, ref_26559) # ROL operation
ref_26565 = (ref_26561 ^ (((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_25610) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_25798) & 0xFFFFFFFFFFFFFFFF) + ref_25874) & 0xFFFFFFFFFFFFFFFF)) + ref_26110) & 0xFFFFFFFFFFFFFFFF) + ref_26186) & 0xFFFFFFFFFFFFFFFF)) + ref_26298) & 0xFFFFFFFFFFFFFFFF) + ref_26374) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_26518) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_26594 = ref_26542 # MOV operation
ref_26612 = ref_26565 # MOV operation
ref_26630 = ref_26542 # MOV operation
ref_26632 = rol(0x11, ref_26630) # ROL operation
ref_26636 = (ref_26632 ^ (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_25610) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_25798) & 0xFFFFFFFFFFFFFFFF) + ref_25874) & 0xFFFFFFFFFFFFFFFF)) + ref_26110) & 0xFFFFFFFFFFFFFFFF) + ref_26186) & 0xFFFFFFFFFFFFFFFF)) + ref_26298) & 0xFFFFFFFFFFFFFFFF) + ref_26374) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_26518) & 0xFFFFFFFFFFFFFFFF) + ref_26594) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_26653 = ref_26565 # MOV operation
ref_26655 = rol(0x15, ref_26653) # ROL operation
ref_26659 = (ref_26655 ^ ((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_25704) & 0xFFFFFFFFFFFFFFFF) + ref_25780) & 0xFFFFFFFFFFFFFFFF)) + ref_25892) & 0xFFFFFFFFFFFFFFFF) ^ ref_25968) + ref_26092) & 0xFFFFFFFFFFFFFFFF)) + ref_26204) & 0xFFFFFFFFFFFFFFFF) + ref_26280) & 0xFFFFFFFFFFFFFFFF)) + ref_26392) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_26500) & 0xFFFFFFFFFFFFFFFF)) + ref_26612) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_26688 = ref_26636 # MOV operation
ref_26706 = ref_26659 # MOV operation
ref_26724 = ref_26636 # MOV operation
ref_26726 = rol(0xD, ref_26724) # ROL operation
ref_26730 = (ref_26726 ^ ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_25704) & 0xFFFFFFFFFFFFFFFF) + ref_25780) & 0xFFFFFFFFFFFFFFFF)) + ref_25892) & 0xFFFFFFFFFFFFFFFF) ^ ref_25968) + ref_26092) & 0xFFFFFFFFFFFFFFFF)) + ref_26204) & 0xFFFFFFFFFFFFFFFF) + ref_26280) & 0xFFFFFFFFFFFFFFFF)) + ref_26392) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_26500) & 0xFFFFFFFFFFFFFFFF)) + ref_26612) & 0xFFFFFFFFFFFFFFFF) + ref_26688) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_26747 = ref_26659 # MOV operation
ref_26749 = rol(0x10, ref_26747) # ROL operation
ref_26753 = (ref_26749 ^ ((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_25610) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_25798) & 0xFFFFFFFFFFFFFFFF) + ref_25874) & 0xFFFFFFFFFFFFFFFF)) + ref_26110) & 0xFFFFFFFFFFFFFFFF) + ref_26186) & 0xFFFFFFFFFFFFFFFF)) + ref_26298) & 0xFFFFFFFFFFFFFFFF) + ref_26374) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_26518) & 0xFFFFFFFFFFFFFFFF) + ref_26594) & 0xFFFFFFFFFFFFFFFF)) + ref_26706) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_26782 = ref_26730 # MOV operation
ref_26800 = ref_26753 # MOV operation
ref_26818 = ref_26730 # MOV operation
ref_26820 = rol(0x11, ref_26818) # ROL operation
ref_26824 = (ref_26820 ^ ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_25610) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_25798) & 0xFFFFFFFFFFFFFFFF) + ref_25874) & 0xFFFFFFFFFFFFFFFF)) + ref_26110) & 0xFFFFFFFFFFFFFFFF) + ref_26186) & 0xFFFFFFFFFFFFFFFF)) + ref_26298) & 0xFFFFFFFFFFFFFFFF) + ref_26374) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_26518) & 0xFFFFFFFFFFFFFFFF) + ref_26594) & 0xFFFFFFFFFFFFFFFF)) + ref_26706) & 0xFFFFFFFFFFFFFFFF) + ref_26782) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_26841 = ref_26753 # MOV operation
ref_26843 = rol(0x15, ref_26841) # ROL operation
ref_26847 = (ref_26843 ^ ((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_25704) & 0xFFFFFFFFFFFFFFFF) + ref_25780) & 0xFFFFFFFFFFFFFFFF)) + ref_25892) & 0xFFFFFFFFFFFFFFFF) ^ ref_25968) + ref_26092) & 0xFFFFFFFFFFFFFFFF)) + ref_26204) & 0xFFFFFFFFFFFFFFFF) + ref_26280) & 0xFFFFFFFFFFFFFFFF)) + ref_26392) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_26500) & 0xFFFFFFFFFFFFFFFF)) + ref_26612) & 0xFFFFFFFFFFFFFFFF) + ref_26688) & 0xFFFFFFFFFFFFFFFF)) + ref_26800) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_26876 = ref_26824 # MOV operation
ref_26894 = ref_26847 # MOV operation
ref_26912 = ref_26824 # MOV operation
ref_26914 = rol(0xD, ref_26912) # ROL operation
ref_26918 = (ref_26914 ^ ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_25704) & 0xFFFFFFFFFFFFFFFF) + ref_25780) & 0xFFFFFFFFFFFFFFFF)) + ref_25892) & 0xFFFFFFFFFFFFFFFF) ^ ref_25968) + ref_26092) & 0xFFFFFFFFFFFFFFFF)) + ref_26204) & 0xFFFFFFFFFFFFFFFF) + ref_26280) & 0xFFFFFFFFFFFFFFFF)) + ref_26392) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_26500) & 0xFFFFFFFFFFFFFFFF)) + ref_26612) & 0xFFFFFFFFFFFFFFFF) + ref_26688) & 0xFFFFFFFFFFFFFFFF)) + ref_26800) & 0xFFFFFFFFFFFFFFFF) + ref_26876) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_26935 = ref_26847 # MOV operation
ref_26937 = rol(0x10, ref_26935) # ROL operation
ref_26941 = (ref_26937 ^ ((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_25610) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_25798) & 0xFFFFFFFFFFFFFFFF) + ref_25874) & 0xFFFFFFFFFFFFFFFF)) + ref_26110) & 0xFFFFFFFFFFFFFFFF) + ref_26186) & 0xFFFFFFFFFFFFFFFF)) + ref_26298) & 0xFFFFFFFFFFFFFFFF) + ref_26374) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_26518) & 0xFFFFFFFFFFFFFFFF) + ref_26594) & 0xFFFFFFFFFFFFFFFF)) + ref_26706) & 0xFFFFFFFFFFFFFFFF) + ref_26782) & 0xFFFFFFFFFFFFFFFF)) + ref_26894) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_26970 = ref_26918 # MOV operation
ref_26988 = ref_26941 # MOV operation
ref_27006 = ref_26918 # MOV operation
ref_27008 = rol(0x11, ref_27006) # ROL operation
ref_27012 = (ref_27008 ^ ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_25610) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_25798) & 0xFFFFFFFFFFFFFFFF) + ref_25874) & 0xFFFFFFFFFFFFFFFF)) + ref_26110) & 0xFFFFFFFFFFFFFFFF) + ref_26186) & 0xFFFFFFFFFFFFFFFF)) + ref_26298) & 0xFFFFFFFFFFFFFFFF) + ref_26374) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_26518) & 0xFFFFFFFFFFFFFFFF) + ref_26594) & 0xFFFFFFFFFFFFFFFF)) + ref_26706) & 0xFFFFFFFFFFFFFFFF) + ref_26782) & 0xFFFFFFFFFFFFFFFF)) + ref_26894) & 0xFFFFFFFFFFFFFFFF) + ref_26970) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_27029 = ref_26941 # MOV operation
ref_27031 = rol(0x15, ref_27029) # ROL operation
ref_27035 = (ref_27031 ^ ((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_25704) & 0xFFFFFFFFFFFFFFFF) + ref_25780) & 0xFFFFFFFFFFFFFFFF)) + ref_25892) & 0xFFFFFFFFFFFFFFFF) ^ ref_25968) + ref_26092) & 0xFFFFFFFFFFFFFFFF)) + ref_26204) & 0xFFFFFFFFFFFFFFFF) + ref_26280) & 0xFFFFFFFFFFFFFFFF)) + ref_26392) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_26500) & 0xFFFFFFFFFFFFFFFF)) + ref_26612) & 0xFFFFFFFFFFFFFFFF) + ref_26688) & 0xFFFFFFFFFFFFFFFF)) + ref_26800) & 0xFFFFFFFFFFFFFFFF) + ref_26876) & 0xFFFFFFFFFFFFFFFF)) + ref_26988) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_27064 = ref_27012 # MOV operation
ref_27082 = ref_27035 # MOV operation
ref_27100 = ref_27012 # MOV operation
ref_27102 = rol(0xD, ref_27100) # ROL operation
ref_27106 = (ref_27102 ^ ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_25704) & 0xFFFFFFFFFFFFFFFF) + ref_25780) & 0xFFFFFFFFFFFFFFFF)) + ref_25892) & 0xFFFFFFFFFFFFFFFF) ^ ref_25968) + ref_26092) & 0xFFFFFFFFFFFFFFFF)) + ref_26204) & 0xFFFFFFFFFFFFFFFF) + ref_26280) & 0xFFFFFFFFFFFFFFFF)) + ref_26392) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_26500) & 0xFFFFFFFFFFFFFFFF)) + ref_26612) & 0xFFFFFFFFFFFFFFFF) + ref_26688) & 0xFFFFFFFFFFFFFFFF)) + ref_26800) & 0xFFFFFFFFFFFFFFFF) + ref_26876) & 0xFFFFFFFFFFFFFFFF)) + ref_26988) & 0xFFFFFFFFFFFFFFFF) + ref_27064) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_27123 = ref_27035 # MOV operation
ref_27125 = rol(0x10, ref_27123) # ROL operation
ref_27129 = (ref_27125 ^ ((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_25610) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_25798) & 0xFFFFFFFFFFFFFFFF) + ref_25874) & 0xFFFFFFFFFFFFFFFF)) + ref_26110) & 0xFFFFFFFFFFFFFFFF) + ref_26186) & 0xFFFFFFFFFFFFFFFF)) + ref_26298) & 0xFFFFFFFFFFFFFFFF) + ref_26374) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_26518) & 0xFFFFFFFFFFFFFFFF) + ref_26594) & 0xFFFFFFFFFFFFFFFF)) + ref_26706) & 0xFFFFFFFFFFFFFFFF) + ref_26782) & 0xFFFFFFFFFFFFFFFF)) + ref_26894) & 0xFFFFFFFFFFFFFFFF) + ref_26970) & 0xFFFFFFFFFFFFFFFF)) + ref_27082) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_27158 = ref_27106 # MOV operation
ref_27176 = ref_27129 # MOV operation
ref_27194 = ref_27106 # MOV operation
ref_27196 = rol(0x11, ref_27194) # ROL operation
ref_27200 = (ref_27196 ^ ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_25610) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_25798) & 0xFFFFFFFFFFFFFFFF) + ref_25874) & 0xFFFFFFFFFFFFFFFF)) + ref_26110) & 0xFFFFFFFFFFFFFFFF) + ref_26186) & 0xFFFFFFFFFFFFFFFF)) + ref_26298) & 0xFFFFFFFFFFFFFFFF) + ref_26374) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_26518) & 0xFFFFFFFFFFFFFFFF) + ref_26594) & 0xFFFFFFFFFFFFFFFF)) + ref_26706) & 0xFFFFFFFFFFFFFFFF) + ref_26782) & 0xFFFFFFFFFFFFFFFF)) + ref_26894) & 0xFFFFFFFFFFFFFFFF) + ref_26970) & 0xFFFFFFFFFFFFFFFF)) + ref_27082) & 0xFFFFFFFFFFFFFFFF) + ref_27158) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_27217 = ref_27129 # MOV operation
ref_27219 = rol(0x15, ref_27217) # ROL operation
ref_27223 = (ref_27219 ^ ((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_25704) & 0xFFFFFFFFFFFFFFFF) + ref_25780) & 0xFFFFFFFFFFFFFFFF)) + ref_25892) & 0xFFFFFFFFFFFFFFFF) ^ ref_25968) + ref_26092) & 0xFFFFFFFFFFFFFFFF)) + ref_26204) & 0xFFFFFFFFFFFFFFFF) + ref_26280) & 0xFFFFFFFFFFFFFFFF)) + ref_26392) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_26500) & 0xFFFFFFFFFFFFFFFF)) + ref_26612) & 0xFFFFFFFFFFFFFFFF) + ref_26688) & 0xFFFFFFFFFFFFFFFF)) + ref_26800) & 0xFFFFFFFFFFFFFFFF) + ref_26876) & 0xFFFFFFFFFFFFFFFF)) + ref_26988) & 0xFFFFFFFFFFFFFFFF) + ref_27064) & 0xFFFFFFFFFFFFFFFF)) + ref_27176) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_27252 = ((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_25704) & 0xFFFFFFFFFFFFFFFF) + ref_25780) & 0xFFFFFFFFFFFFFFFF)) + ref_25892) & 0xFFFFFFFFFFFFFFFF) ^ ref_25968) + ref_26092) & 0xFFFFFFFFFFFFFFFF)) + ref_26204) & 0xFFFFFFFFFFFFFFFF) + ref_26280) & 0xFFFFFFFFFFFFFFFF)) + ref_26392) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_26500) & 0xFFFFFFFFFFFFFFFF)) + ref_26612) & 0xFFFFFFFFFFFFFFFF) + ref_26688) & 0xFFFFFFFFFFFFFFFF)) + ref_26800) & 0xFFFFFFFFFFFFFFFF) + ref_26876) & 0xFFFFFFFFFFFFFFFF)) + ref_26988) & 0xFFFFFFFFFFFFFFFF) + ref_27064) & 0xFFFFFFFFFFFFFFFF)) + ref_27176) & 0xFFFFFFFFFFFFFFFF) # MOV operation
ref_27254 = (ref_27252 ^ ref_27200) # XOR operation
ref_27261 = ref_27254 # MOV operation
ref_27263 = rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_25610) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_25798) & 0xFFFFFFFFFFFFFFFF) + ref_25874) & 0xFFFFFFFFFFFFFFFF)) + ref_26110) & 0xFFFFFFFFFFFFFFFF) + ref_26186) & 0xFFFFFFFFFFFFFFFF)) + ref_26298) & 0xFFFFFFFFFFFFFFFF) + ref_26374) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_26518) & 0xFFFFFFFFFFFFFFFF) + ref_26594) & 0xFFFFFFFFFFFFFFFF)) + ref_26706) & 0xFFFFFFFFFFFFFFFF) + ref_26782) & 0xFFFFFFFFFFFFFFFF)) + ref_26894) & 0xFFFFFFFFFFFFFFFF) + ref_26970) & 0xFFFFFFFFFFFFFFFF)) + ref_27082) & 0xFFFFFFFFFFFFFFFF) + ref_27158) & 0xFFFFFFFFFFFFFFFF)) # MOV operation
ref_27265 = (ref_27263 ^ ref_27223) # XOR operation
ref_27272 = (ref_27265 ^ ref_27261) # XOR operation
ref_27570 = ref_27272 # MOV operation
ref_27850 = ref_27570 # MOV operation
ref_28234 = ref_27850 # MOV operation
ref_28347 = ref_28234 # MOV operation
ref_28385 = ref_28347 # MOV operation
ref_28397 = ref_28385 # MOV operation
ref_28399 = ref_28397 # MOV operation

print(ref_28399 & 0xffffffffffffffff)
