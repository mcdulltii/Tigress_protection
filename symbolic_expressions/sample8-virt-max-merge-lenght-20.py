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
ref_10657 = ref_239 # MOV operation
ref_10701 = ref_10657 # MOV operation
ref_10736 = (((((((((0x7B) << 8 | 0x6B) << 8 | 0x69) << 8 | 0x6E) << 8 | 0x72) << 8 | 0x7E) << 8 | 0x6C) << 8 | 0x7B) ^ ref_10701) # MOV operation
ref_10777 = (((((((((0x7B) << 8 | 0x6B) << 8 | 0x69) << 8 | 0x6E) << 8 | 0x72) << 8 | 0x7E) << 8 | 0x6C) << 8 | 0x7B) ^ ref_10701) # MOV operation
ref_10779 = rol(0x10, ref_10777) # ROL operation
ref_10783 = (ref_10779 ^ ((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_10736) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_10830 = ref_10783 # MOV operation
ref_10854 = (0x96C62826CF6DE04E ^ ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_10736) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_10871 = ref_10783 # MOV operation
ref_10873 = rol(0x15, ref_10871) # ROL operation
ref_10877 = (ref_10873 ^ ((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_10830) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_10906 = ref_10854 # MOV operation
ref_10924 = ref_10877 # MOV operation
ref_10942 = ref_10854 # MOV operation
ref_10944 = rol(0xD, ref_10942) # ROL operation
ref_10948 = (ref_10944 ^ ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_10830) & 0xFFFFFFFFFFFFFFFF) + ref_10906) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_10965 = ref_10877 # MOV operation
ref_10967 = rol(0x10, ref_10965) # ROL operation
ref_10971 = (ref_10967 ^ ((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_10736) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_10924) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_11000 = ref_10948 # MOV operation
ref_11018 = ref_10971 # MOV operation
ref_11036 = ref_10948 # MOV operation
ref_11038 = rol(0x11, ref_11036) # ROL operation
ref_11042 = (ref_11038 ^ ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_10736) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_10924) & 0xFFFFFFFFFFFFFFFF) + ref_11000) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_11059 = ref_10971 # MOV operation
ref_11061 = rol(0x15, ref_11059) # ROL operation
ref_11065 = (ref_11061 ^ ((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_10830) & 0xFFFFFFFFFFFFFFFF) + ref_10906) & 0xFFFFFFFFFFFFFFFF)) + ref_11018) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_11094 = ref_10657 # MOV operation
ref_11218 = ref_11042 # MOV operation
ref_11236 = (ref_11065 ^ 0x800000000000000) # MOV operation
ref_11254 = ref_11042 # MOV operation
ref_11256 = rol(0xD, ref_11254) # ROL operation
ref_11260 = (ref_11256 ^ (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_10830) & 0xFFFFFFFFFFFFFFFF) + ref_10906) & 0xFFFFFFFFFFFFFFFF)) + ref_11018) & 0xFFFFFFFFFFFFFFFF) ^ ref_11094) + ref_11218) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_11277 = (ref_11065 ^ 0x800000000000000) # MOV operation
ref_11279 = rol(0x10, ref_11277) # ROL operation
ref_11283 = (ref_11279 ^ ((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_10736) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_10924) & 0xFFFFFFFFFFFFFFFF) + ref_11000) & 0xFFFFFFFFFFFFFFFF)) + ref_11236) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_11312 = ref_11260 # MOV operation
ref_11330 = ref_11283 # MOV operation
ref_11348 = ref_11260 # MOV operation
ref_11350 = rol(0x11, ref_11348) # ROL operation
ref_11354 = (ref_11350 ^ ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_10736) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_10924) & 0xFFFFFFFFFFFFFFFF) + ref_11000) & 0xFFFFFFFFFFFFFFFF)) + ref_11236) & 0xFFFFFFFFFFFFFFFF) + ref_11312) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_11371 = ref_11283 # MOV operation
ref_11373 = rol(0x15, ref_11371) # ROL operation
ref_11377 = (ref_11373 ^ ((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_10830) & 0xFFFFFFFFFFFFFFFF) + ref_10906) & 0xFFFFFFFFFFFFFFFF)) + ref_11018) & 0xFFFFFFFFFFFFFFFF) ^ ref_11094) + ref_11218) & 0xFFFFFFFFFFFFFFFF)) + ref_11330) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_11406 = ref_11354 # MOV operation
ref_11424 = ref_11377 # MOV operation
ref_11442 = ref_11354 # MOV operation
ref_11444 = rol(0xD, ref_11442) # ROL operation
ref_11448 = (ref_11444 ^ ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_10830) & 0xFFFFFFFFFFFFFFFF) + ref_10906) & 0xFFFFFFFFFFFFFFFF)) + ref_11018) & 0xFFFFFFFFFFFFFFFF) ^ ref_11094) + ref_11218) & 0xFFFFFFFFFFFFFFFF)) + ref_11330) & 0xFFFFFFFFFFFFFFFF) + ref_11406) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_11465 = ref_11377 # MOV operation
ref_11467 = rol(0x10, ref_11465) # ROL operation
ref_11471 = (ref_11467 ^ ((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_10736) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_10924) & 0xFFFFFFFFFFFFFFFF) + ref_11000) & 0xFFFFFFFFFFFFFFFF)) + ref_11236) & 0xFFFFFFFFFFFFFFFF) + ref_11312) & 0xFFFFFFFFFFFFFFFF)) + ref_11424) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_11500 = ref_11448 # MOV operation
ref_11518 = ref_11471 # MOV operation
ref_11536 = ref_11448 # MOV operation
ref_11538 = rol(0x11, ref_11536) # ROL operation
ref_11542 = (ref_11538 ^ ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_10736) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_10924) & 0xFFFFFFFFFFFFFFFF) + ref_11000) & 0xFFFFFFFFFFFFFFFF)) + ref_11236) & 0xFFFFFFFFFFFFFFFF) + ref_11312) & 0xFFFFFFFFFFFFFFFF)) + ref_11424) & 0xFFFFFFFFFFFFFFFF) + ref_11500) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_11559 = ref_11471 # MOV operation
ref_11561 = rol(0x15, ref_11559) # ROL operation
ref_11565 = (ref_11561 ^ ((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_10830) & 0xFFFFFFFFFFFFFFFF) + ref_10906) & 0xFFFFFFFFFFFFFFFF)) + ref_11018) & 0xFFFFFFFFFFFFFFFF) ^ ref_11094) + ref_11218) & 0xFFFFFFFFFFFFFFFF)) + ref_11330) & 0xFFFFFFFFFFFFFFFF) + ref_11406) & 0xFFFFFFFFFFFFFFFF)) + ref_11518) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_11626 = ref_11542 # MOV operation
ref_11644 = ref_11565 # MOV operation
ref_11662 = ref_11542 # MOV operation
ref_11664 = rol(0xD, ref_11662) # ROL operation
ref_11668 = (ref_11664 ^ (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_10830) & 0xFFFFFFFFFFFFFFFF) + ref_10906) & 0xFFFFFFFFFFFFFFFF)) + ref_11018) & 0xFFFFFFFFFFFFFFFF) ^ ref_11094) + ref_11218) & 0xFFFFFFFFFFFFFFFF)) + ref_11330) & 0xFFFFFFFFFFFFFFFF) + ref_11406) & 0xFFFFFFFFFFFFFFFF)) + ref_11518) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_11626) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_11685 = ref_11565 # MOV operation
ref_11687 = rol(0x10, ref_11685) # ROL operation
ref_11691 = (ref_11687 ^ (((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_10736) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_10924) & 0xFFFFFFFFFFFFFFFF) + ref_11000) & 0xFFFFFFFFFFFFFFFF)) + ref_11236) & 0xFFFFFFFFFFFFFFFF) + ref_11312) & 0xFFFFFFFFFFFFFFFF)) + ref_11424) & 0xFFFFFFFFFFFFFFFF) + ref_11500) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_11644) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_11720 = ref_11668 # MOV operation
ref_11738 = ref_11691 # MOV operation
ref_11756 = ref_11668 # MOV operation
ref_11758 = rol(0x11, ref_11756) # ROL operation
ref_11762 = (ref_11758 ^ (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_10736) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_10924) & 0xFFFFFFFFFFFFFFFF) + ref_11000) & 0xFFFFFFFFFFFFFFFF)) + ref_11236) & 0xFFFFFFFFFFFFFFFF) + ref_11312) & 0xFFFFFFFFFFFFFFFF)) + ref_11424) & 0xFFFFFFFFFFFFFFFF) + ref_11500) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_11644) & 0xFFFFFFFFFFFFFFFF) + ref_11720) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_11779 = ref_11691 # MOV operation
ref_11781 = rol(0x15, ref_11779) # ROL operation
ref_11785 = (ref_11781 ^ ((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_10830) & 0xFFFFFFFFFFFFFFFF) + ref_10906) & 0xFFFFFFFFFFFFFFFF)) + ref_11018) & 0xFFFFFFFFFFFFFFFF) ^ ref_11094) + ref_11218) & 0xFFFFFFFFFFFFFFFF)) + ref_11330) & 0xFFFFFFFFFFFFFFFF) + ref_11406) & 0xFFFFFFFFFFFFFFFF)) + ref_11518) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_11626) & 0xFFFFFFFFFFFFFFFF)) + ref_11738) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_11814 = ref_11762 # MOV operation
ref_11832 = ref_11785 # MOV operation
ref_11850 = ref_11762 # MOV operation
ref_11852 = rol(0xD, ref_11850) # ROL operation
ref_11856 = (ref_11852 ^ ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_10830) & 0xFFFFFFFFFFFFFFFF) + ref_10906) & 0xFFFFFFFFFFFFFFFF)) + ref_11018) & 0xFFFFFFFFFFFFFFFF) ^ ref_11094) + ref_11218) & 0xFFFFFFFFFFFFFFFF)) + ref_11330) & 0xFFFFFFFFFFFFFFFF) + ref_11406) & 0xFFFFFFFFFFFFFFFF)) + ref_11518) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_11626) & 0xFFFFFFFFFFFFFFFF)) + ref_11738) & 0xFFFFFFFFFFFFFFFF) + ref_11814) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_11873 = ref_11785 # MOV operation
ref_11875 = rol(0x10, ref_11873) # ROL operation
ref_11879 = (ref_11875 ^ ((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_10736) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_10924) & 0xFFFFFFFFFFFFFFFF) + ref_11000) & 0xFFFFFFFFFFFFFFFF)) + ref_11236) & 0xFFFFFFFFFFFFFFFF) + ref_11312) & 0xFFFFFFFFFFFFFFFF)) + ref_11424) & 0xFFFFFFFFFFFFFFFF) + ref_11500) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_11644) & 0xFFFFFFFFFFFFFFFF) + ref_11720) & 0xFFFFFFFFFFFFFFFF)) + ref_11832) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_11908 = ref_11856 # MOV operation
ref_11926 = ref_11879 # MOV operation
ref_11944 = ref_11856 # MOV operation
ref_11946 = rol(0x11, ref_11944) # ROL operation
ref_11950 = (ref_11946 ^ ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_10736) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_10924) & 0xFFFFFFFFFFFFFFFF) + ref_11000) & 0xFFFFFFFFFFFFFFFF)) + ref_11236) & 0xFFFFFFFFFFFFFFFF) + ref_11312) & 0xFFFFFFFFFFFFFFFF)) + ref_11424) & 0xFFFFFFFFFFFFFFFF) + ref_11500) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_11644) & 0xFFFFFFFFFFFFFFFF) + ref_11720) & 0xFFFFFFFFFFFFFFFF)) + ref_11832) & 0xFFFFFFFFFFFFFFFF) + ref_11908) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_11967 = ref_11879 # MOV operation
ref_11969 = rol(0x15, ref_11967) # ROL operation
ref_11973 = (ref_11969 ^ ((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_10830) & 0xFFFFFFFFFFFFFFFF) + ref_10906) & 0xFFFFFFFFFFFFFFFF)) + ref_11018) & 0xFFFFFFFFFFFFFFFF) ^ ref_11094) + ref_11218) & 0xFFFFFFFFFFFFFFFF)) + ref_11330) & 0xFFFFFFFFFFFFFFFF) + ref_11406) & 0xFFFFFFFFFFFFFFFF)) + ref_11518) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_11626) & 0xFFFFFFFFFFFFFFFF)) + ref_11738) & 0xFFFFFFFFFFFFFFFF) + ref_11814) & 0xFFFFFFFFFFFFFFFF)) + ref_11926) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_12002 = ref_11950 # MOV operation
ref_12020 = ref_11973 # MOV operation
ref_12038 = ref_11950 # MOV operation
ref_12040 = rol(0xD, ref_12038) # ROL operation
ref_12044 = (ref_12040 ^ ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_10830) & 0xFFFFFFFFFFFFFFFF) + ref_10906) & 0xFFFFFFFFFFFFFFFF)) + ref_11018) & 0xFFFFFFFFFFFFFFFF) ^ ref_11094) + ref_11218) & 0xFFFFFFFFFFFFFFFF)) + ref_11330) & 0xFFFFFFFFFFFFFFFF) + ref_11406) & 0xFFFFFFFFFFFFFFFF)) + ref_11518) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_11626) & 0xFFFFFFFFFFFFFFFF)) + ref_11738) & 0xFFFFFFFFFFFFFFFF) + ref_11814) & 0xFFFFFFFFFFFFFFFF)) + ref_11926) & 0xFFFFFFFFFFFFFFFF) + ref_12002) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_12061 = ref_11973 # MOV operation
ref_12063 = rol(0x10, ref_12061) # ROL operation
ref_12067 = (ref_12063 ^ ((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_10736) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_10924) & 0xFFFFFFFFFFFFFFFF) + ref_11000) & 0xFFFFFFFFFFFFFFFF)) + ref_11236) & 0xFFFFFFFFFFFFFFFF) + ref_11312) & 0xFFFFFFFFFFFFFFFF)) + ref_11424) & 0xFFFFFFFFFFFFFFFF) + ref_11500) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_11644) & 0xFFFFFFFFFFFFFFFF) + ref_11720) & 0xFFFFFFFFFFFFFFFF)) + ref_11832) & 0xFFFFFFFFFFFFFFFF) + ref_11908) & 0xFFFFFFFFFFFFFFFF)) + ref_12020) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_12096 = ref_12044 # MOV operation
ref_12114 = ref_12067 # MOV operation
ref_12132 = ref_12044 # MOV operation
ref_12134 = rol(0x11, ref_12132) # ROL operation
ref_12138 = (ref_12134 ^ ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_10736) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_10924) & 0xFFFFFFFFFFFFFFFF) + ref_11000) & 0xFFFFFFFFFFFFFFFF)) + ref_11236) & 0xFFFFFFFFFFFFFFFF) + ref_11312) & 0xFFFFFFFFFFFFFFFF)) + ref_11424) & 0xFFFFFFFFFFFFFFFF) + ref_11500) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_11644) & 0xFFFFFFFFFFFFFFFF) + ref_11720) & 0xFFFFFFFFFFFFFFFF)) + ref_11832) & 0xFFFFFFFFFFFFFFFF) + ref_11908) & 0xFFFFFFFFFFFFFFFF)) + ref_12020) & 0xFFFFFFFFFFFFFFFF) + ref_12096) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_12155 = ref_12067 # MOV operation
ref_12157 = rol(0x15, ref_12155) # ROL operation
ref_12161 = (ref_12157 ^ ((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_10830) & 0xFFFFFFFFFFFFFFFF) + ref_10906) & 0xFFFFFFFFFFFFFFFF)) + ref_11018) & 0xFFFFFFFFFFFFFFFF) ^ ref_11094) + ref_11218) & 0xFFFFFFFFFFFFFFFF)) + ref_11330) & 0xFFFFFFFFFFFFFFFF) + ref_11406) & 0xFFFFFFFFFFFFFFFF)) + ref_11518) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_11626) & 0xFFFFFFFFFFFFFFFF)) + ref_11738) & 0xFFFFFFFFFFFFFFFF) + ref_11814) & 0xFFFFFFFFFFFFFFFF)) + ref_11926) & 0xFFFFFFFFFFFFFFFF) + ref_12002) & 0xFFFFFFFFFFFFFFFF)) + ref_12114) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_12190 = ref_12138 # MOV operation
ref_12208 = ref_12161 # MOV operation
ref_12226 = ref_12138 # MOV operation
ref_12228 = rol(0xD, ref_12226) # ROL operation
ref_12232 = (ref_12228 ^ ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_10830) & 0xFFFFFFFFFFFFFFFF) + ref_10906) & 0xFFFFFFFFFFFFFFFF)) + ref_11018) & 0xFFFFFFFFFFFFFFFF) ^ ref_11094) + ref_11218) & 0xFFFFFFFFFFFFFFFF)) + ref_11330) & 0xFFFFFFFFFFFFFFFF) + ref_11406) & 0xFFFFFFFFFFFFFFFF)) + ref_11518) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_11626) & 0xFFFFFFFFFFFFFFFF)) + ref_11738) & 0xFFFFFFFFFFFFFFFF) + ref_11814) & 0xFFFFFFFFFFFFFFFF)) + ref_11926) & 0xFFFFFFFFFFFFFFFF) + ref_12002) & 0xFFFFFFFFFFFFFFFF)) + ref_12114) & 0xFFFFFFFFFFFFFFFF) + ref_12190) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_12249 = ref_12161 # MOV operation
ref_12251 = rol(0x10, ref_12249) # ROL operation
ref_12255 = (ref_12251 ^ ((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_10736) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_10924) & 0xFFFFFFFFFFFFFFFF) + ref_11000) & 0xFFFFFFFFFFFFFFFF)) + ref_11236) & 0xFFFFFFFFFFFFFFFF) + ref_11312) & 0xFFFFFFFFFFFFFFFF)) + ref_11424) & 0xFFFFFFFFFFFFFFFF) + ref_11500) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_11644) & 0xFFFFFFFFFFFFFFFF) + ref_11720) & 0xFFFFFFFFFFFFFFFF)) + ref_11832) & 0xFFFFFFFFFFFFFFFF) + ref_11908) & 0xFFFFFFFFFFFFFFFF)) + ref_12020) & 0xFFFFFFFFFFFFFFFF) + ref_12096) & 0xFFFFFFFFFFFFFFFF)) + ref_12208) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_12284 = ref_12232 # MOV operation
ref_12302 = ref_12255 # MOV operation
ref_12320 = ref_12232 # MOV operation
ref_12322 = rol(0x11, ref_12320) # ROL operation
ref_12326 = (ref_12322 ^ ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_10736) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_10924) & 0xFFFFFFFFFFFFFFFF) + ref_11000) & 0xFFFFFFFFFFFFFFFF)) + ref_11236) & 0xFFFFFFFFFFFFFFFF) + ref_11312) & 0xFFFFFFFFFFFFFFFF)) + ref_11424) & 0xFFFFFFFFFFFFFFFF) + ref_11500) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_11644) & 0xFFFFFFFFFFFFFFFF) + ref_11720) & 0xFFFFFFFFFFFFFFFF)) + ref_11832) & 0xFFFFFFFFFFFFFFFF) + ref_11908) & 0xFFFFFFFFFFFFFFFF)) + ref_12020) & 0xFFFFFFFFFFFFFFFF) + ref_12096) & 0xFFFFFFFFFFFFFFFF)) + ref_12208) & 0xFFFFFFFFFFFFFFFF) + ref_12284) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_12343 = ref_12255 # MOV operation
ref_12345 = rol(0x15, ref_12343) # ROL operation
ref_12349 = (ref_12345 ^ ((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_10830) & 0xFFFFFFFFFFFFFFFF) + ref_10906) & 0xFFFFFFFFFFFFFFFF)) + ref_11018) & 0xFFFFFFFFFFFFFFFF) ^ ref_11094) + ref_11218) & 0xFFFFFFFFFFFFFFFF)) + ref_11330) & 0xFFFFFFFFFFFFFFFF) + ref_11406) & 0xFFFFFFFFFFFFFFFF)) + ref_11518) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_11626) & 0xFFFFFFFFFFFFFFFF)) + ref_11738) & 0xFFFFFFFFFFFFFFFF) + ref_11814) & 0xFFFFFFFFFFFFFFFF)) + ref_11926) & 0xFFFFFFFFFFFFFFFF) + ref_12002) & 0xFFFFFFFFFFFFFFFF)) + ref_12114) & 0xFFFFFFFFFFFFFFFF) + ref_12190) & 0xFFFFFFFFFFFFFFFF)) + ref_12302) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_12378 = ((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_10830) & 0xFFFFFFFFFFFFFFFF) + ref_10906) & 0xFFFFFFFFFFFFFFFF)) + ref_11018) & 0xFFFFFFFFFFFFFFFF) ^ ref_11094) + ref_11218) & 0xFFFFFFFFFFFFFFFF)) + ref_11330) & 0xFFFFFFFFFFFFFFFF) + ref_11406) & 0xFFFFFFFFFFFFFFFF)) + ref_11518) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_11626) & 0xFFFFFFFFFFFFFFFF)) + ref_11738) & 0xFFFFFFFFFFFFFFFF) + ref_11814) & 0xFFFFFFFFFFFFFFFF)) + ref_11926) & 0xFFFFFFFFFFFFFFFF) + ref_12002) & 0xFFFFFFFFFFFFFFFF)) + ref_12114) & 0xFFFFFFFFFFFFFFFF) + ref_12190) & 0xFFFFFFFFFFFFFFFF)) + ref_12302) & 0xFFFFFFFFFFFFFFFF) # MOV operation
ref_12380 = (ref_12378 ^ ref_12326) # XOR operation
ref_12387 = ref_12380 # MOV operation
ref_12389 = rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_10736) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_10924) & 0xFFFFFFFFFFFFFFFF) + ref_11000) & 0xFFFFFFFFFFFFFFFF)) + ref_11236) & 0xFFFFFFFFFFFFFFFF) + ref_11312) & 0xFFFFFFFFFFFFFFFF)) + ref_11424) & 0xFFFFFFFFFFFFFFFF) + ref_11500) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_11644) & 0xFFFFFFFFFFFFFFFF) + ref_11720) & 0xFFFFFFFFFFFFFFFF)) + ref_11832) & 0xFFFFFFFFFFFFFFFF) + ref_11908) & 0xFFFFFFFFFFFFFFFF)) + ref_12020) & 0xFFFFFFFFFFFFFFFF) + ref_12096) & 0xFFFFFFFFFFFFFFFF)) + ref_12208) & 0xFFFFFFFFFFFFFFFF) + ref_12284) & 0xFFFFFFFFFFFFFFFF)) # MOV operation
ref_12391 = (ref_12389 ^ ref_12349) # XOR operation
ref_12398 = (ref_12391 ^ ref_12387) # XOR operation
ref_12624 = ref_12398 # MOV operation
ref_12658 = ref_12624 # MOV operation
ref_12917 = ref_12658 # MOV operation
ref_13044 = ref_12917 # MOV operation
ref_13082 = ref_13044 # MOV operation
ref_13094 = ref_13082 # MOV operation
ref_13096 = ref_13094 # MOV operation

print(ref_13096 & 0xffffffffffffffff)
