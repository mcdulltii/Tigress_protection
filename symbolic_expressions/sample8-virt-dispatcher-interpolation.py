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
ref_107128 = ref_239 # MOV operation
ref_107172 = ref_107128 # MOV operation
ref_107207 = (((((((((0x7B) << 8 | 0x6B) << 8 | 0x69) << 8 | 0x6E) << 8 | 0x72) << 8 | 0x7E) << 8 | 0x6C) << 8 | 0x7B) ^ ref_107172) # MOV operation
ref_107248 = (((((((((0x7B) << 8 | 0x6B) << 8 | 0x69) << 8 | 0x6E) << 8 | 0x72) << 8 | 0x7E) << 8 | 0x6C) << 8 | 0x7B) ^ ref_107172) # MOV operation
ref_107250 = rol(0x10, ref_107248) # ROL operation
ref_107254 = (ref_107250 ^ ((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_107207) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_107301 = ref_107254 # MOV operation
ref_107325 = (0x96C62826CF6DE04E ^ ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_107207) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_107342 = ref_107254 # MOV operation
ref_107344 = rol(0x15, ref_107342) # ROL operation
ref_107348 = (ref_107344 ^ ((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_107301) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_107377 = ref_107325 # MOV operation
ref_107395 = ref_107348 # MOV operation
ref_107413 = ref_107325 # MOV operation
ref_107415 = rol(0xD, ref_107413) # ROL operation
ref_107419 = (ref_107415 ^ ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_107301) & 0xFFFFFFFFFFFFFFFF) + ref_107377) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_107436 = ref_107348 # MOV operation
ref_107438 = rol(0x10, ref_107436) # ROL operation
ref_107442 = (ref_107438 ^ ((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_107207) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_107395) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_107471 = ref_107419 # MOV operation
ref_107489 = ref_107442 # MOV operation
ref_107507 = ref_107419 # MOV operation
ref_107509 = rol(0x11, ref_107507) # ROL operation
ref_107513 = (ref_107509 ^ ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_107207) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_107395) & 0xFFFFFFFFFFFFFFFF) + ref_107471) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_107530 = ref_107442 # MOV operation
ref_107532 = rol(0x15, ref_107530) # ROL operation
ref_107536 = (ref_107532 ^ ((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_107301) & 0xFFFFFFFFFFFFFFFF) + ref_107377) & 0xFFFFFFFFFFFFFFFF)) + ref_107489) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_107565 = ref_107128 # MOV operation
ref_107689 = ref_107513 # MOV operation
ref_107707 = (ref_107536 ^ 0x800000000000000) # MOV operation
ref_107725 = ref_107513 # MOV operation
ref_107727 = rol(0xD, ref_107725) # ROL operation
ref_107731 = (ref_107727 ^ (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_107301) & 0xFFFFFFFFFFFFFFFF) + ref_107377) & 0xFFFFFFFFFFFFFFFF)) + ref_107489) & 0xFFFFFFFFFFFFFFFF) ^ ref_107565) + ref_107689) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_107748 = (ref_107536 ^ 0x800000000000000) # MOV operation
ref_107750 = rol(0x10, ref_107748) # ROL operation
ref_107754 = (ref_107750 ^ ((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_107207) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_107395) & 0xFFFFFFFFFFFFFFFF) + ref_107471) & 0xFFFFFFFFFFFFFFFF)) + ref_107707) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_107783 = ref_107731 # MOV operation
ref_107801 = ref_107754 # MOV operation
ref_107819 = ref_107731 # MOV operation
ref_107821 = rol(0x11, ref_107819) # ROL operation
ref_107825 = (ref_107821 ^ ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_107207) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_107395) & 0xFFFFFFFFFFFFFFFF) + ref_107471) & 0xFFFFFFFFFFFFFFFF)) + ref_107707) & 0xFFFFFFFFFFFFFFFF) + ref_107783) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_107842 = ref_107754 # MOV operation
ref_107844 = rol(0x15, ref_107842) # ROL operation
ref_107848 = (ref_107844 ^ ((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_107301) & 0xFFFFFFFFFFFFFFFF) + ref_107377) & 0xFFFFFFFFFFFFFFFF)) + ref_107489) & 0xFFFFFFFFFFFFFFFF) ^ ref_107565) + ref_107689) & 0xFFFFFFFFFFFFFFFF)) + ref_107801) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_107877 = ref_107825 # MOV operation
ref_107895 = ref_107848 # MOV operation
ref_107913 = ref_107825 # MOV operation
ref_107915 = rol(0xD, ref_107913) # ROL operation
ref_107919 = (ref_107915 ^ ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_107301) & 0xFFFFFFFFFFFFFFFF) + ref_107377) & 0xFFFFFFFFFFFFFFFF)) + ref_107489) & 0xFFFFFFFFFFFFFFFF) ^ ref_107565) + ref_107689) & 0xFFFFFFFFFFFFFFFF)) + ref_107801) & 0xFFFFFFFFFFFFFFFF) + ref_107877) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_107936 = ref_107848 # MOV operation
ref_107938 = rol(0x10, ref_107936) # ROL operation
ref_107942 = (ref_107938 ^ ((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_107207) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_107395) & 0xFFFFFFFFFFFFFFFF) + ref_107471) & 0xFFFFFFFFFFFFFFFF)) + ref_107707) & 0xFFFFFFFFFFFFFFFF) + ref_107783) & 0xFFFFFFFFFFFFFFFF)) + ref_107895) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_107971 = ref_107919 # MOV operation
ref_107989 = ref_107942 # MOV operation
ref_108007 = ref_107919 # MOV operation
ref_108009 = rol(0x11, ref_108007) # ROL operation
ref_108013 = (ref_108009 ^ ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_107207) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_107395) & 0xFFFFFFFFFFFFFFFF) + ref_107471) & 0xFFFFFFFFFFFFFFFF)) + ref_107707) & 0xFFFFFFFFFFFFFFFF) + ref_107783) & 0xFFFFFFFFFFFFFFFF)) + ref_107895) & 0xFFFFFFFFFFFFFFFF) + ref_107971) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_108030 = ref_107942 # MOV operation
ref_108032 = rol(0x15, ref_108030) # ROL operation
ref_108036 = (ref_108032 ^ ((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_107301) & 0xFFFFFFFFFFFFFFFF) + ref_107377) & 0xFFFFFFFFFFFFFFFF)) + ref_107489) & 0xFFFFFFFFFFFFFFFF) ^ ref_107565) + ref_107689) & 0xFFFFFFFFFFFFFFFF)) + ref_107801) & 0xFFFFFFFFFFFFFFFF) + ref_107877) & 0xFFFFFFFFFFFFFFFF)) + ref_107989) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_108097 = ref_108013 # MOV operation
ref_108115 = ref_108036 # MOV operation
ref_108133 = ref_108013 # MOV operation
ref_108135 = rol(0xD, ref_108133) # ROL operation
ref_108139 = (ref_108135 ^ (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_107301) & 0xFFFFFFFFFFFFFFFF) + ref_107377) & 0xFFFFFFFFFFFFFFFF)) + ref_107489) & 0xFFFFFFFFFFFFFFFF) ^ ref_107565) + ref_107689) & 0xFFFFFFFFFFFFFFFF)) + ref_107801) & 0xFFFFFFFFFFFFFFFF) + ref_107877) & 0xFFFFFFFFFFFFFFFF)) + ref_107989) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_108097) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_108156 = ref_108036 # MOV operation
ref_108158 = rol(0x10, ref_108156) # ROL operation
ref_108162 = (ref_108158 ^ (((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_107207) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_107395) & 0xFFFFFFFFFFFFFFFF) + ref_107471) & 0xFFFFFFFFFFFFFFFF)) + ref_107707) & 0xFFFFFFFFFFFFFFFF) + ref_107783) & 0xFFFFFFFFFFFFFFFF)) + ref_107895) & 0xFFFFFFFFFFFFFFFF) + ref_107971) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_108115) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_108191 = ref_108139 # MOV operation
ref_108209 = ref_108162 # MOV operation
ref_108227 = ref_108139 # MOV operation
ref_108229 = rol(0x11, ref_108227) # ROL operation
ref_108233 = (ref_108229 ^ (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_107207) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_107395) & 0xFFFFFFFFFFFFFFFF) + ref_107471) & 0xFFFFFFFFFFFFFFFF)) + ref_107707) & 0xFFFFFFFFFFFFFFFF) + ref_107783) & 0xFFFFFFFFFFFFFFFF)) + ref_107895) & 0xFFFFFFFFFFFFFFFF) + ref_107971) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_108115) & 0xFFFFFFFFFFFFFFFF) + ref_108191) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_108250 = ref_108162 # MOV operation
ref_108252 = rol(0x15, ref_108250) # ROL operation
ref_108256 = (ref_108252 ^ ((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_107301) & 0xFFFFFFFFFFFFFFFF) + ref_107377) & 0xFFFFFFFFFFFFFFFF)) + ref_107489) & 0xFFFFFFFFFFFFFFFF) ^ ref_107565) + ref_107689) & 0xFFFFFFFFFFFFFFFF)) + ref_107801) & 0xFFFFFFFFFFFFFFFF) + ref_107877) & 0xFFFFFFFFFFFFFFFF)) + ref_107989) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_108097) & 0xFFFFFFFFFFFFFFFF)) + ref_108209) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_108285 = ref_108233 # MOV operation
ref_108303 = ref_108256 # MOV operation
ref_108321 = ref_108233 # MOV operation
ref_108323 = rol(0xD, ref_108321) # ROL operation
ref_108327 = (ref_108323 ^ ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_107301) & 0xFFFFFFFFFFFFFFFF) + ref_107377) & 0xFFFFFFFFFFFFFFFF)) + ref_107489) & 0xFFFFFFFFFFFFFFFF) ^ ref_107565) + ref_107689) & 0xFFFFFFFFFFFFFFFF)) + ref_107801) & 0xFFFFFFFFFFFFFFFF) + ref_107877) & 0xFFFFFFFFFFFFFFFF)) + ref_107989) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_108097) & 0xFFFFFFFFFFFFFFFF)) + ref_108209) & 0xFFFFFFFFFFFFFFFF) + ref_108285) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_108344 = ref_108256 # MOV operation
ref_108346 = rol(0x10, ref_108344) # ROL operation
ref_108350 = (ref_108346 ^ ((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_107207) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_107395) & 0xFFFFFFFFFFFFFFFF) + ref_107471) & 0xFFFFFFFFFFFFFFFF)) + ref_107707) & 0xFFFFFFFFFFFFFFFF) + ref_107783) & 0xFFFFFFFFFFFFFFFF)) + ref_107895) & 0xFFFFFFFFFFFFFFFF) + ref_107971) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_108115) & 0xFFFFFFFFFFFFFFFF) + ref_108191) & 0xFFFFFFFFFFFFFFFF)) + ref_108303) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_108379 = ref_108327 # MOV operation
ref_108397 = ref_108350 # MOV operation
ref_108415 = ref_108327 # MOV operation
ref_108417 = rol(0x11, ref_108415) # ROL operation
ref_108421 = (ref_108417 ^ ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_107207) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_107395) & 0xFFFFFFFFFFFFFFFF) + ref_107471) & 0xFFFFFFFFFFFFFFFF)) + ref_107707) & 0xFFFFFFFFFFFFFFFF) + ref_107783) & 0xFFFFFFFFFFFFFFFF)) + ref_107895) & 0xFFFFFFFFFFFFFFFF) + ref_107971) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_108115) & 0xFFFFFFFFFFFFFFFF) + ref_108191) & 0xFFFFFFFFFFFFFFFF)) + ref_108303) & 0xFFFFFFFFFFFFFFFF) + ref_108379) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_108438 = ref_108350 # MOV operation
ref_108440 = rol(0x15, ref_108438) # ROL operation
ref_108444 = (ref_108440 ^ ((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_107301) & 0xFFFFFFFFFFFFFFFF) + ref_107377) & 0xFFFFFFFFFFFFFFFF)) + ref_107489) & 0xFFFFFFFFFFFFFFFF) ^ ref_107565) + ref_107689) & 0xFFFFFFFFFFFFFFFF)) + ref_107801) & 0xFFFFFFFFFFFFFFFF) + ref_107877) & 0xFFFFFFFFFFFFFFFF)) + ref_107989) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_108097) & 0xFFFFFFFFFFFFFFFF)) + ref_108209) & 0xFFFFFFFFFFFFFFFF) + ref_108285) & 0xFFFFFFFFFFFFFFFF)) + ref_108397) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_108473 = ref_108421 # MOV operation
ref_108491 = ref_108444 # MOV operation
ref_108509 = ref_108421 # MOV operation
ref_108511 = rol(0xD, ref_108509) # ROL operation
ref_108515 = (ref_108511 ^ ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_107301) & 0xFFFFFFFFFFFFFFFF) + ref_107377) & 0xFFFFFFFFFFFFFFFF)) + ref_107489) & 0xFFFFFFFFFFFFFFFF) ^ ref_107565) + ref_107689) & 0xFFFFFFFFFFFFFFFF)) + ref_107801) & 0xFFFFFFFFFFFFFFFF) + ref_107877) & 0xFFFFFFFFFFFFFFFF)) + ref_107989) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_108097) & 0xFFFFFFFFFFFFFFFF)) + ref_108209) & 0xFFFFFFFFFFFFFFFF) + ref_108285) & 0xFFFFFFFFFFFFFFFF)) + ref_108397) & 0xFFFFFFFFFFFFFFFF) + ref_108473) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_108532 = ref_108444 # MOV operation
ref_108534 = rol(0x10, ref_108532) # ROL operation
ref_108538 = (ref_108534 ^ ((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_107207) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_107395) & 0xFFFFFFFFFFFFFFFF) + ref_107471) & 0xFFFFFFFFFFFFFFFF)) + ref_107707) & 0xFFFFFFFFFFFFFFFF) + ref_107783) & 0xFFFFFFFFFFFFFFFF)) + ref_107895) & 0xFFFFFFFFFFFFFFFF) + ref_107971) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_108115) & 0xFFFFFFFFFFFFFFFF) + ref_108191) & 0xFFFFFFFFFFFFFFFF)) + ref_108303) & 0xFFFFFFFFFFFFFFFF) + ref_108379) & 0xFFFFFFFFFFFFFFFF)) + ref_108491) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_108567 = ref_108515 # MOV operation
ref_108585 = ref_108538 # MOV operation
ref_108603 = ref_108515 # MOV operation
ref_108605 = rol(0x11, ref_108603) # ROL operation
ref_108609 = (ref_108605 ^ ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_107207) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_107395) & 0xFFFFFFFFFFFFFFFF) + ref_107471) & 0xFFFFFFFFFFFFFFFF)) + ref_107707) & 0xFFFFFFFFFFFFFFFF) + ref_107783) & 0xFFFFFFFFFFFFFFFF)) + ref_107895) & 0xFFFFFFFFFFFFFFFF) + ref_107971) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_108115) & 0xFFFFFFFFFFFFFFFF) + ref_108191) & 0xFFFFFFFFFFFFFFFF)) + ref_108303) & 0xFFFFFFFFFFFFFFFF) + ref_108379) & 0xFFFFFFFFFFFFFFFF)) + ref_108491) & 0xFFFFFFFFFFFFFFFF) + ref_108567) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_108626 = ref_108538 # MOV operation
ref_108628 = rol(0x15, ref_108626) # ROL operation
ref_108632 = (ref_108628 ^ ((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_107301) & 0xFFFFFFFFFFFFFFFF) + ref_107377) & 0xFFFFFFFFFFFFFFFF)) + ref_107489) & 0xFFFFFFFFFFFFFFFF) ^ ref_107565) + ref_107689) & 0xFFFFFFFFFFFFFFFF)) + ref_107801) & 0xFFFFFFFFFFFFFFFF) + ref_107877) & 0xFFFFFFFFFFFFFFFF)) + ref_107989) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_108097) & 0xFFFFFFFFFFFFFFFF)) + ref_108209) & 0xFFFFFFFFFFFFFFFF) + ref_108285) & 0xFFFFFFFFFFFFFFFF)) + ref_108397) & 0xFFFFFFFFFFFFFFFF) + ref_108473) & 0xFFFFFFFFFFFFFFFF)) + ref_108585) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_108661 = ref_108609 # MOV operation
ref_108679 = ref_108632 # MOV operation
ref_108697 = ref_108609 # MOV operation
ref_108699 = rol(0xD, ref_108697) # ROL operation
ref_108703 = (ref_108699 ^ ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_107301) & 0xFFFFFFFFFFFFFFFF) + ref_107377) & 0xFFFFFFFFFFFFFFFF)) + ref_107489) & 0xFFFFFFFFFFFFFFFF) ^ ref_107565) + ref_107689) & 0xFFFFFFFFFFFFFFFF)) + ref_107801) & 0xFFFFFFFFFFFFFFFF) + ref_107877) & 0xFFFFFFFFFFFFFFFF)) + ref_107989) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_108097) & 0xFFFFFFFFFFFFFFFF)) + ref_108209) & 0xFFFFFFFFFFFFFFFF) + ref_108285) & 0xFFFFFFFFFFFFFFFF)) + ref_108397) & 0xFFFFFFFFFFFFFFFF) + ref_108473) & 0xFFFFFFFFFFFFFFFF)) + ref_108585) & 0xFFFFFFFFFFFFFFFF) + ref_108661) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_108720 = ref_108632 # MOV operation
ref_108722 = rol(0x10, ref_108720) # ROL operation
ref_108726 = (ref_108722 ^ ((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_107207) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_107395) & 0xFFFFFFFFFFFFFFFF) + ref_107471) & 0xFFFFFFFFFFFFFFFF)) + ref_107707) & 0xFFFFFFFFFFFFFFFF) + ref_107783) & 0xFFFFFFFFFFFFFFFF)) + ref_107895) & 0xFFFFFFFFFFFFFFFF) + ref_107971) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_108115) & 0xFFFFFFFFFFFFFFFF) + ref_108191) & 0xFFFFFFFFFFFFFFFF)) + ref_108303) & 0xFFFFFFFFFFFFFFFF) + ref_108379) & 0xFFFFFFFFFFFFFFFF)) + ref_108491) & 0xFFFFFFFFFFFFFFFF) + ref_108567) & 0xFFFFFFFFFFFFFFFF)) + ref_108679) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_108755 = ref_108703 # MOV operation
ref_108773 = ref_108726 # MOV operation
ref_108791 = ref_108703 # MOV operation
ref_108793 = rol(0x11, ref_108791) # ROL operation
ref_108797 = (ref_108793 ^ ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_107207) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_107395) & 0xFFFFFFFFFFFFFFFF) + ref_107471) & 0xFFFFFFFFFFFFFFFF)) + ref_107707) & 0xFFFFFFFFFFFFFFFF) + ref_107783) & 0xFFFFFFFFFFFFFFFF)) + ref_107895) & 0xFFFFFFFFFFFFFFFF) + ref_107971) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_108115) & 0xFFFFFFFFFFFFFFFF) + ref_108191) & 0xFFFFFFFFFFFFFFFF)) + ref_108303) & 0xFFFFFFFFFFFFFFFF) + ref_108379) & 0xFFFFFFFFFFFFFFFF)) + ref_108491) & 0xFFFFFFFFFFFFFFFF) + ref_108567) & 0xFFFFFFFFFFFFFFFF)) + ref_108679) & 0xFFFFFFFFFFFFFFFF) + ref_108755) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_108814 = ref_108726 # MOV operation
ref_108816 = rol(0x15, ref_108814) # ROL operation
ref_108820 = (ref_108816 ^ ((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_107301) & 0xFFFFFFFFFFFFFFFF) + ref_107377) & 0xFFFFFFFFFFFFFFFF)) + ref_107489) & 0xFFFFFFFFFFFFFFFF) ^ ref_107565) + ref_107689) & 0xFFFFFFFFFFFFFFFF)) + ref_107801) & 0xFFFFFFFFFFFFFFFF) + ref_107877) & 0xFFFFFFFFFFFFFFFF)) + ref_107989) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_108097) & 0xFFFFFFFFFFFFFFFF)) + ref_108209) & 0xFFFFFFFFFFFFFFFF) + ref_108285) & 0xFFFFFFFFFFFFFFFF)) + ref_108397) & 0xFFFFFFFFFFFFFFFF) + ref_108473) & 0xFFFFFFFFFFFFFFFF)) + ref_108585) & 0xFFFFFFFFFFFFFFFF) + ref_108661) & 0xFFFFFFFFFFFFFFFF)) + ref_108773) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_108849 = ((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_107301) & 0xFFFFFFFFFFFFFFFF) + ref_107377) & 0xFFFFFFFFFFFFFFFF)) + ref_107489) & 0xFFFFFFFFFFFFFFFF) ^ ref_107565) + ref_107689) & 0xFFFFFFFFFFFFFFFF)) + ref_107801) & 0xFFFFFFFFFFFFFFFF) + ref_107877) & 0xFFFFFFFFFFFFFFFF)) + ref_107989) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_108097) & 0xFFFFFFFFFFFFFFFF)) + ref_108209) & 0xFFFFFFFFFFFFFFFF) + ref_108285) & 0xFFFFFFFFFFFFFFFF)) + ref_108397) & 0xFFFFFFFFFFFFFFFF) + ref_108473) & 0xFFFFFFFFFFFFFFFF)) + ref_108585) & 0xFFFFFFFFFFFFFFFF) + ref_108661) & 0xFFFFFFFFFFFFFFFF)) + ref_108773) & 0xFFFFFFFFFFFFFFFF) # MOV operation
ref_108851 = (ref_108849 ^ ref_108797) # XOR operation
ref_108858 = ref_108851 # MOV operation
ref_108860 = rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_107207) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_107395) & 0xFFFFFFFFFFFFFFFF) + ref_107471) & 0xFFFFFFFFFFFFFFFF)) + ref_107707) & 0xFFFFFFFFFFFFFFFF) + ref_107783) & 0xFFFFFFFFFFFFFFFF)) + ref_107895) & 0xFFFFFFFFFFFFFFFF) + ref_107971) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_108115) & 0xFFFFFFFFFFFFFFFF) + ref_108191) & 0xFFFFFFFFFFFFFFFF)) + ref_108303) & 0xFFFFFFFFFFFFFFFF) + ref_108379) & 0xFFFFFFFFFFFFFFFF)) + ref_108491) & 0xFFFFFFFFFFFFFFFF) + ref_108567) & 0xFFFFFFFFFFFFFFFF)) + ref_108679) & 0xFFFFFFFFFFFFFFFF) + ref_108755) & 0xFFFFFFFFFFFFFFFF)) # MOV operation
ref_108862 = (ref_108860 ^ ref_108820) # XOR operation
ref_108869 = (ref_108862 ^ ref_108858) # XOR operation
ref_110878 = ref_108869 # MOV operation
ref_111242 = ref_110878 # MOV operation
ref_113185 = ref_111242 # MOV operation
ref_113537 = ref_113185 # MOV operation
ref_113575 = ref_113537 # MOV operation
ref_113587 = ref_113575 # MOV operation
ref_113589 = ref_113587 # MOV operation

print(ref_113589 & 0xffffffffffffffff)
