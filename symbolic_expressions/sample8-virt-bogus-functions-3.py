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
ref_88340 = ref_239 # MOV operation
ref_88384 = ref_88340 # MOV operation
ref_88419 = (((((((((0x7B) << 8 | 0x6B) << 8 | 0x69) << 8 | 0x6E) << 8 | 0x72) << 8 | 0x7E) << 8 | 0x6C) << 8 | 0x7B) ^ ref_88384) # MOV operation
ref_88460 = (((((((((0x7B) << 8 | 0x6B) << 8 | 0x69) << 8 | 0x6E) << 8 | 0x72) << 8 | 0x7E) << 8 | 0x6C) << 8 | 0x7B) ^ ref_88384) # MOV operation
ref_88462 = rol(0x10, ref_88460) # ROL operation
ref_88466 = (ref_88462 ^ ((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_88419) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_88513 = ref_88466 # MOV operation
ref_88537 = (0x96C62826CF6DE04E ^ ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_88419) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_88554 = ref_88466 # MOV operation
ref_88556 = rol(0x15, ref_88554) # ROL operation
ref_88560 = (ref_88556 ^ ((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_88513) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_88589 = ref_88537 # MOV operation
ref_88607 = ref_88560 # MOV operation
ref_88625 = ref_88537 # MOV operation
ref_88627 = rol(0xD, ref_88625) # ROL operation
ref_88631 = (ref_88627 ^ ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_88513) & 0xFFFFFFFFFFFFFFFF) + ref_88589) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_88648 = ref_88560 # MOV operation
ref_88650 = rol(0x10, ref_88648) # ROL operation
ref_88654 = (ref_88650 ^ ((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_88419) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_88607) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_88683 = ref_88631 # MOV operation
ref_88701 = ref_88654 # MOV operation
ref_88719 = ref_88631 # MOV operation
ref_88721 = rol(0x11, ref_88719) # ROL operation
ref_88725 = (ref_88721 ^ ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_88419) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_88607) & 0xFFFFFFFFFFFFFFFF) + ref_88683) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_88742 = ref_88654 # MOV operation
ref_88744 = rol(0x15, ref_88742) # ROL operation
ref_88748 = (ref_88744 ^ ((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_88513) & 0xFFFFFFFFFFFFFFFF) + ref_88589) & 0xFFFFFFFFFFFFFFFF)) + ref_88701) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_88777 = ref_88340 # MOV operation
ref_88901 = ref_88725 # MOV operation
ref_88919 = (ref_88748 ^ 0x800000000000000) # MOV operation
ref_88937 = ref_88725 # MOV operation
ref_88939 = rol(0xD, ref_88937) # ROL operation
ref_88943 = (ref_88939 ^ (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_88513) & 0xFFFFFFFFFFFFFFFF) + ref_88589) & 0xFFFFFFFFFFFFFFFF)) + ref_88701) & 0xFFFFFFFFFFFFFFFF) ^ ref_88777) + ref_88901) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_88960 = (ref_88748 ^ 0x800000000000000) # MOV operation
ref_88962 = rol(0x10, ref_88960) # ROL operation
ref_88966 = (ref_88962 ^ ((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_88419) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_88607) & 0xFFFFFFFFFFFFFFFF) + ref_88683) & 0xFFFFFFFFFFFFFFFF)) + ref_88919) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_88995 = ref_88943 # MOV operation
ref_89013 = ref_88966 # MOV operation
ref_89031 = ref_88943 # MOV operation
ref_89033 = rol(0x11, ref_89031) # ROL operation
ref_89037 = (ref_89033 ^ ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_88419) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_88607) & 0xFFFFFFFFFFFFFFFF) + ref_88683) & 0xFFFFFFFFFFFFFFFF)) + ref_88919) & 0xFFFFFFFFFFFFFFFF) + ref_88995) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_89054 = ref_88966 # MOV operation
ref_89056 = rol(0x15, ref_89054) # ROL operation
ref_89060 = (ref_89056 ^ ((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_88513) & 0xFFFFFFFFFFFFFFFF) + ref_88589) & 0xFFFFFFFFFFFFFFFF)) + ref_88701) & 0xFFFFFFFFFFFFFFFF) ^ ref_88777) + ref_88901) & 0xFFFFFFFFFFFFFFFF)) + ref_89013) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_89089 = ref_89037 # MOV operation
ref_89107 = ref_89060 # MOV operation
ref_89125 = ref_89037 # MOV operation
ref_89127 = rol(0xD, ref_89125) # ROL operation
ref_89131 = (ref_89127 ^ ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_88513) & 0xFFFFFFFFFFFFFFFF) + ref_88589) & 0xFFFFFFFFFFFFFFFF)) + ref_88701) & 0xFFFFFFFFFFFFFFFF) ^ ref_88777) + ref_88901) & 0xFFFFFFFFFFFFFFFF)) + ref_89013) & 0xFFFFFFFFFFFFFFFF) + ref_89089) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_89148 = ref_89060 # MOV operation
ref_89150 = rol(0x10, ref_89148) # ROL operation
ref_89154 = (ref_89150 ^ ((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_88419) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_88607) & 0xFFFFFFFFFFFFFFFF) + ref_88683) & 0xFFFFFFFFFFFFFFFF)) + ref_88919) & 0xFFFFFFFFFFFFFFFF) + ref_88995) & 0xFFFFFFFFFFFFFFFF)) + ref_89107) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_89183 = ref_89131 # MOV operation
ref_89201 = ref_89154 # MOV operation
ref_89219 = ref_89131 # MOV operation
ref_89221 = rol(0x11, ref_89219) # ROL operation
ref_89225 = (ref_89221 ^ ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_88419) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_88607) & 0xFFFFFFFFFFFFFFFF) + ref_88683) & 0xFFFFFFFFFFFFFFFF)) + ref_88919) & 0xFFFFFFFFFFFFFFFF) + ref_88995) & 0xFFFFFFFFFFFFFFFF)) + ref_89107) & 0xFFFFFFFFFFFFFFFF) + ref_89183) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_89242 = ref_89154 # MOV operation
ref_89244 = rol(0x15, ref_89242) # ROL operation
ref_89248 = (ref_89244 ^ ((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_88513) & 0xFFFFFFFFFFFFFFFF) + ref_88589) & 0xFFFFFFFFFFFFFFFF)) + ref_88701) & 0xFFFFFFFFFFFFFFFF) ^ ref_88777) + ref_88901) & 0xFFFFFFFFFFFFFFFF)) + ref_89013) & 0xFFFFFFFFFFFFFFFF) + ref_89089) & 0xFFFFFFFFFFFFFFFF)) + ref_89201) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_89309 = ref_89225 # MOV operation
ref_89327 = ref_89248 # MOV operation
ref_89345 = ref_89225 # MOV operation
ref_89347 = rol(0xD, ref_89345) # ROL operation
ref_89351 = (ref_89347 ^ (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_88513) & 0xFFFFFFFFFFFFFFFF) + ref_88589) & 0xFFFFFFFFFFFFFFFF)) + ref_88701) & 0xFFFFFFFFFFFFFFFF) ^ ref_88777) + ref_88901) & 0xFFFFFFFFFFFFFFFF)) + ref_89013) & 0xFFFFFFFFFFFFFFFF) + ref_89089) & 0xFFFFFFFFFFFFFFFF)) + ref_89201) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_89309) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_89368 = ref_89248 # MOV operation
ref_89370 = rol(0x10, ref_89368) # ROL operation
ref_89374 = (ref_89370 ^ (((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_88419) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_88607) & 0xFFFFFFFFFFFFFFFF) + ref_88683) & 0xFFFFFFFFFFFFFFFF)) + ref_88919) & 0xFFFFFFFFFFFFFFFF) + ref_88995) & 0xFFFFFFFFFFFFFFFF)) + ref_89107) & 0xFFFFFFFFFFFFFFFF) + ref_89183) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_89327) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_89403 = ref_89351 # MOV operation
ref_89421 = ref_89374 # MOV operation
ref_89439 = ref_89351 # MOV operation
ref_89441 = rol(0x11, ref_89439) # ROL operation
ref_89445 = (ref_89441 ^ (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_88419) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_88607) & 0xFFFFFFFFFFFFFFFF) + ref_88683) & 0xFFFFFFFFFFFFFFFF)) + ref_88919) & 0xFFFFFFFFFFFFFFFF) + ref_88995) & 0xFFFFFFFFFFFFFFFF)) + ref_89107) & 0xFFFFFFFFFFFFFFFF) + ref_89183) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_89327) & 0xFFFFFFFFFFFFFFFF) + ref_89403) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_89462 = ref_89374 # MOV operation
ref_89464 = rol(0x15, ref_89462) # ROL operation
ref_89468 = (ref_89464 ^ ((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_88513) & 0xFFFFFFFFFFFFFFFF) + ref_88589) & 0xFFFFFFFFFFFFFFFF)) + ref_88701) & 0xFFFFFFFFFFFFFFFF) ^ ref_88777) + ref_88901) & 0xFFFFFFFFFFFFFFFF)) + ref_89013) & 0xFFFFFFFFFFFFFFFF) + ref_89089) & 0xFFFFFFFFFFFFFFFF)) + ref_89201) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_89309) & 0xFFFFFFFFFFFFFFFF)) + ref_89421) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_89497 = ref_89445 # MOV operation
ref_89515 = ref_89468 # MOV operation
ref_89533 = ref_89445 # MOV operation
ref_89535 = rol(0xD, ref_89533) # ROL operation
ref_89539 = (ref_89535 ^ ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_88513) & 0xFFFFFFFFFFFFFFFF) + ref_88589) & 0xFFFFFFFFFFFFFFFF)) + ref_88701) & 0xFFFFFFFFFFFFFFFF) ^ ref_88777) + ref_88901) & 0xFFFFFFFFFFFFFFFF)) + ref_89013) & 0xFFFFFFFFFFFFFFFF) + ref_89089) & 0xFFFFFFFFFFFFFFFF)) + ref_89201) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_89309) & 0xFFFFFFFFFFFFFFFF)) + ref_89421) & 0xFFFFFFFFFFFFFFFF) + ref_89497) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_89556 = ref_89468 # MOV operation
ref_89558 = rol(0x10, ref_89556) # ROL operation
ref_89562 = (ref_89558 ^ ((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_88419) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_88607) & 0xFFFFFFFFFFFFFFFF) + ref_88683) & 0xFFFFFFFFFFFFFFFF)) + ref_88919) & 0xFFFFFFFFFFFFFFFF) + ref_88995) & 0xFFFFFFFFFFFFFFFF)) + ref_89107) & 0xFFFFFFFFFFFFFFFF) + ref_89183) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_89327) & 0xFFFFFFFFFFFFFFFF) + ref_89403) & 0xFFFFFFFFFFFFFFFF)) + ref_89515) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_89591 = ref_89539 # MOV operation
ref_89609 = ref_89562 # MOV operation
ref_89627 = ref_89539 # MOV operation
ref_89629 = rol(0x11, ref_89627) # ROL operation
ref_89633 = (ref_89629 ^ ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_88419) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_88607) & 0xFFFFFFFFFFFFFFFF) + ref_88683) & 0xFFFFFFFFFFFFFFFF)) + ref_88919) & 0xFFFFFFFFFFFFFFFF) + ref_88995) & 0xFFFFFFFFFFFFFFFF)) + ref_89107) & 0xFFFFFFFFFFFFFFFF) + ref_89183) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_89327) & 0xFFFFFFFFFFFFFFFF) + ref_89403) & 0xFFFFFFFFFFFFFFFF)) + ref_89515) & 0xFFFFFFFFFFFFFFFF) + ref_89591) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_89650 = ref_89562 # MOV operation
ref_89652 = rol(0x15, ref_89650) # ROL operation
ref_89656 = (ref_89652 ^ ((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_88513) & 0xFFFFFFFFFFFFFFFF) + ref_88589) & 0xFFFFFFFFFFFFFFFF)) + ref_88701) & 0xFFFFFFFFFFFFFFFF) ^ ref_88777) + ref_88901) & 0xFFFFFFFFFFFFFFFF)) + ref_89013) & 0xFFFFFFFFFFFFFFFF) + ref_89089) & 0xFFFFFFFFFFFFFFFF)) + ref_89201) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_89309) & 0xFFFFFFFFFFFFFFFF)) + ref_89421) & 0xFFFFFFFFFFFFFFFF) + ref_89497) & 0xFFFFFFFFFFFFFFFF)) + ref_89609) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_89685 = ref_89633 # MOV operation
ref_89703 = ref_89656 # MOV operation
ref_89721 = ref_89633 # MOV operation
ref_89723 = rol(0xD, ref_89721) # ROL operation
ref_89727 = (ref_89723 ^ ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_88513) & 0xFFFFFFFFFFFFFFFF) + ref_88589) & 0xFFFFFFFFFFFFFFFF)) + ref_88701) & 0xFFFFFFFFFFFFFFFF) ^ ref_88777) + ref_88901) & 0xFFFFFFFFFFFFFFFF)) + ref_89013) & 0xFFFFFFFFFFFFFFFF) + ref_89089) & 0xFFFFFFFFFFFFFFFF)) + ref_89201) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_89309) & 0xFFFFFFFFFFFFFFFF)) + ref_89421) & 0xFFFFFFFFFFFFFFFF) + ref_89497) & 0xFFFFFFFFFFFFFFFF)) + ref_89609) & 0xFFFFFFFFFFFFFFFF) + ref_89685) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_89744 = ref_89656 # MOV operation
ref_89746 = rol(0x10, ref_89744) # ROL operation
ref_89750 = (ref_89746 ^ ((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_88419) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_88607) & 0xFFFFFFFFFFFFFFFF) + ref_88683) & 0xFFFFFFFFFFFFFFFF)) + ref_88919) & 0xFFFFFFFFFFFFFFFF) + ref_88995) & 0xFFFFFFFFFFFFFFFF)) + ref_89107) & 0xFFFFFFFFFFFFFFFF) + ref_89183) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_89327) & 0xFFFFFFFFFFFFFFFF) + ref_89403) & 0xFFFFFFFFFFFFFFFF)) + ref_89515) & 0xFFFFFFFFFFFFFFFF) + ref_89591) & 0xFFFFFFFFFFFFFFFF)) + ref_89703) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_89779 = ref_89727 # MOV operation
ref_89797 = ref_89750 # MOV operation
ref_89815 = ref_89727 # MOV operation
ref_89817 = rol(0x11, ref_89815) # ROL operation
ref_89821 = (ref_89817 ^ ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_88419) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_88607) & 0xFFFFFFFFFFFFFFFF) + ref_88683) & 0xFFFFFFFFFFFFFFFF)) + ref_88919) & 0xFFFFFFFFFFFFFFFF) + ref_88995) & 0xFFFFFFFFFFFFFFFF)) + ref_89107) & 0xFFFFFFFFFFFFFFFF) + ref_89183) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_89327) & 0xFFFFFFFFFFFFFFFF) + ref_89403) & 0xFFFFFFFFFFFFFFFF)) + ref_89515) & 0xFFFFFFFFFFFFFFFF) + ref_89591) & 0xFFFFFFFFFFFFFFFF)) + ref_89703) & 0xFFFFFFFFFFFFFFFF) + ref_89779) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_89838 = ref_89750 # MOV operation
ref_89840 = rol(0x15, ref_89838) # ROL operation
ref_89844 = (ref_89840 ^ ((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_88513) & 0xFFFFFFFFFFFFFFFF) + ref_88589) & 0xFFFFFFFFFFFFFFFF)) + ref_88701) & 0xFFFFFFFFFFFFFFFF) ^ ref_88777) + ref_88901) & 0xFFFFFFFFFFFFFFFF)) + ref_89013) & 0xFFFFFFFFFFFFFFFF) + ref_89089) & 0xFFFFFFFFFFFFFFFF)) + ref_89201) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_89309) & 0xFFFFFFFFFFFFFFFF)) + ref_89421) & 0xFFFFFFFFFFFFFFFF) + ref_89497) & 0xFFFFFFFFFFFFFFFF)) + ref_89609) & 0xFFFFFFFFFFFFFFFF) + ref_89685) & 0xFFFFFFFFFFFFFFFF)) + ref_89797) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_89873 = ref_89821 # MOV operation
ref_89891 = ref_89844 # MOV operation
ref_89909 = ref_89821 # MOV operation
ref_89911 = rol(0xD, ref_89909) # ROL operation
ref_89915 = (ref_89911 ^ ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_88513) & 0xFFFFFFFFFFFFFFFF) + ref_88589) & 0xFFFFFFFFFFFFFFFF)) + ref_88701) & 0xFFFFFFFFFFFFFFFF) ^ ref_88777) + ref_88901) & 0xFFFFFFFFFFFFFFFF)) + ref_89013) & 0xFFFFFFFFFFFFFFFF) + ref_89089) & 0xFFFFFFFFFFFFFFFF)) + ref_89201) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_89309) & 0xFFFFFFFFFFFFFFFF)) + ref_89421) & 0xFFFFFFFFFFFFFFFF) + ref_89497) & 0xFFFFFFFFFFFFFFFF)) + ref_89609) & 0xFFFFFFFFFFFFFFFF) + ref_89685) & 0xFFFFFFFFFFFFFFFF)) + ref_89797) & 0xFFFFFFFFFFFFFFFF) + ref_89873) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_89932 = ref_89844 # MOV operation
ref_89934 = rol(0x10, ref_89932) # ROL operation
ref_89938 = (ref_89934 ^ ((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_88419) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_88607) & 0xFFFFFFFFFFFFFFFF) + ref_88683) & 0xFFFFFFFFFFFFFFFF)) + ref_88919) & 0xFFFFFFFFFFFFFFFF) + ref_88995) & 0xFFFFFFFFFFFFFFFF)) + ref_89107) & 0xFFFFFFFFFFFFFFFF) + ref_89183) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_89327) & 0xFFFFFFFFFFFFFFFF) + ref_89403) & 0xFFFFFFFFFFFFFFFF)) + ref_89515) & 0xFFFFFFFFFFFFFFFF) + ref_89591) & 0xFFFFFFFFFFFFFFFF)) + ref_89703) & 0xFFFFFFFFFFFFFFFF) + ref_89779) & 0xFFFFFFFFFFFFFFFF)) + ref_89891) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_89967 = ref_89915 # MOV operation
ref_89985 = ref_89938 # MOV operation
ref_90003 = ref_89915 # MOV operation
ref_90005 = rol(0x11, ref_90003) # ROL operation
ref_90009 = (ref_90005 ^ ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_88419) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_88607) & 0xFFFFFFFFFFFFFFFF) + ref_88683) & 0xFFFFFFFFFFFFFFFF)) + ref_88919) & 0xFFFFFFFFFFFFFFFF) + ref_88995) & 0xFFFFFFFFFFFFFFFF)) + ref_89107) & 0xFFFFFFFFFFFFFFFF) + ref_89183) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_89327) & 0xFFFFFFFFFFFFFFFF) + ref_89403) & 0xFFFFFFFFFFFFFFFF)) + ref_89515) & 0xFFFFFFFFFFFFFFFF) + ref_89591) & 0xFFFFFFFFFFFFFFFF)) + ref_89703) & 0xFFFFFFFFFFFFFFFF) + ref_89779) & 0xFFFFFFFFFFFFFFFF)) + ref_89891) & 0xFFFFFFFFFFFFFFFF) + ref_89967) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_90026 = ref_89938 # MOV operation
ref_90028 = rol(0x15, ref_90026) # ROL operation
ref_90032 = (ref_90028 ^ ((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_88513) & 0xFFFFFFFFFFFFFFFF) + ref_88589) & 0xFFFFFFFFFFFFFFFF)) + ref_88701) & 0xFFFFFFFFFFFFFFFF) ^ ref_88777) + ref_88901) & 0xFFFFFFFFFFFFFFFF)) + ref_89013) & 0xFFFFFFFFFFFFFFFF) + ref_89089) & 0xFFFFFFFFFFFFFFFF)) + ref_89201) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_89309) & 0xFFFFFFFFFFFFFFFF)) + ref_89421) & 0xFFFFFFFFFFFFFFFF) + ref_89497) & 0xFFFFFFFFFFFFFFFF)) + ref_89609) & 0xFFFFFFFFFFFFFFFF) + ref_89685) & 0xFFFFFFFFFFFFFFFF)) + ref_89797) & 0xFFFFFFFFFFFFFFFF) + ref_89873) & 0xFFFFFFFFFFFFFFFF)) + ref_89985) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_90061 = ((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_88513) & 0xFFFFFFFFFFFFFFFF) + ref_88589) & 0xFFFFFFFFFFFFFFFF)) + ref_88701) & 0xFFFFFFFFFFFFFFFF) ^ ref_88777) + ref_88901) & 0xFFFFFFFFFFFFFFFF)) + ref_89013) & 0xFFFFFFFFFFFFFFFF) + ref_89089) & 0xFFFFFFFFFFFFFFFF)) + ref_89201) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_89309) & 0xFFFFFFFFFFFFFFFF)) + ref_89421) & 0xFFFFFFFFFFFFFFFF) + ref_89497) & 0xFFFFFFFFFFFFFFFF)) + ref_89609) & 0xFFFFFFFFFFFFFFFF) + ref_89685) & 0xFFFFFFFFFFFFFFFF)) + ref_89797) & 0xFFFFFFFFFFFFFFFF) + ref_89873) & 0xFFFFFFFFFFFFFFFF)) + ref_89985) & 0xFFFFFFFFFFFFFFFF) # MOV operation
ref_90063 = (ref_90061 ^ ref_90009) # XOR operation
ref_90070 = ref_90063 # MOV operation
ref_90072 = rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_88419) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_88607) & 0xFFFFFFFFFFFFFFFF) + ref_88683) & 0xFFFFFFFFFFFFFFFF)) + ref_88919) & 0xFFFFFFFFFFFFFFFF) + ref_88995) & 0xFFFFFFFFFFFFFFFF)) + ref_89107) & 0xFFFFFFFFFFFFFFFF) + ref_89183) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_89327) & 0xFFFFFFFFFFFFFFFF) + ref_89403) & 0xFFFFFFFFFFFFFFFF)) + ref_89515) & 0xFFFFFFFFFFFFFFFF) + ref_89591) & 0xFFFFFFFFFFFFFFFF)) + ref_89703) & 0xFFFFFFFFFFFFFFFF) + ref_89779) & 0xFFFFFFFFFFFFFFFF)) + ref_89891) & 0xFFFFFFFFFFFFFFFF) + ref_89967) & 0xFFFFFFFFFFFFFFFF)) # MOV operation
ref_90074 = (ref_90072 ^ ref_90032) # XOR operation
ref_90081 = (ref_90074 ^ ref_90070) # XOR operation
ref_91202 = ref_90081 # MOV operation
ref_92250 = ref_91202 # MOV operation
ref_93708 = ref_92250 # MOV operation
ref_94293 = ref_93708 # MOV operation
ref_94334 = ref_94293 # MOV operation
ref_94346 = ref_94334 # MOV operation
ref_94348 = ref_94346 # MOV operation

print(ref_94348 & 0xffffffffffffffff)
