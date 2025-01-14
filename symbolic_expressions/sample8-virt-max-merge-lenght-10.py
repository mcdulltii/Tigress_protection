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
ref_11304 = ref_239 # MOV operation
ref_11348 = ref_11304 # MOV operation
ref_11383 = (((((((((0x7B) << 8 | 0x6B) << 8 | 0x69) << 8 | 0x6E) << 8 | 0x72) << 8 | 0x7E) << 8 | 0x6C) << 8 | 0x7B) ^ ref_11348) # MOV operation
ref_11424 = (((((((((0x7B) << 8 | 0x6B) << 8 | 0x69) << 8 | 0x6E) << 8 | 0x72) << 8 | 0x7E) << 8 | 0x6C) << 8 | 0x7B) ^ ref_11348) # MOV operation
ref_11426 = rol(0x10, ref_11424) # ROL operation
ref_11430 = (ref_11426 ^ ((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_11383) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_11477 = ref_11430 # MOV operation
ref_11501 = (0x96C62826CF6DE04E ^ ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_11383) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_11518 = ref_11430 # MOV operation
ref_11520 = rol(0x15, ref_11518) # ROL operation
ref_11524 = (ref_11520 ^ ((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_11477) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_11553 = ref_11501 # MOV operation
ref_11571 = ref_11524 # MOV operation
ref_11589 = ref_11501 # MOV operation
ref_11591 = rol(0xD, ref_11589) # ROL operation
ref_11595 = (ref_11591 ^ ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_11477) & 0xFFFFFFFFFFFFFFFF) + ref_11553) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_11612 = ref_11524 # MOV operation
ref_11614 = rol(0x10, ref_11612) # ROL operation
ref_11618 = (ref_11614 ^ ((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_11383) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_11571) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_11647 = ref_11595 # MOV operation
ref_11665 = ref_11618 # MOV operation
ref_11683 = ref_11595 # MOV operation
ref_11685 = rol(0x11, ref_11683) # ROL operation
ref_11689 = (ref_11685 ^ ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_11383) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_11571) & 0xFFFFFFFFFFFFFFFF) + ref_11647) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_11706 = ref_11618 # MOV operation
ref_11708 = rol(0x15, ref_11706) # ROL operation
ref_11712 = (ref_11708 ^ ((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_11477) & 0xFFFFFFFFFFFFFFFF) + ref_11553) & 0xFFFFFFFFFFFFFFFF)) + ref_11665) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_11741 = ref_11304 # MOV operation
ref_11865 = ref_11689 # MOV operation
ref_11883 = (ref_11712 ^ 0x800000000000000) # MOV operation
ref_11901 = ref_11689 # MOV operation
ref_11903 = rol(0xD, ref_11901) # ROL operation
ref_11907 = (ref_11903 ^ (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_11477) & 0xFFFFFFFFFFFFFFFF) + ref_11553) & 0xFFFFFFFFFFFFFFFF)) + ref_11665) & 0xFFFFFFFFFFFFFFFF) ^ ref_11741) + ref_11865) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_11924 = (ref_11712 ^ 0x800000000000000) # MOV operation
ref_11926 = rol(0x10, ref_11924) # ROL operation
ref_11930 = (ref_11926 ^ ((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_11383) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_11571) & 0xFFFFFFFFFFFFFFFF) + ref_11647) & 0xFFFFFFFFFFFFFFFF)) + ref_11883) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_11959 = ref_11907 # MOV operation
ref_11977 = ref_11930 # MOV operation
ref_11995 = ref_11907 # MOV operation
ref_11997 = rol(0x11, ref_11995) # ROL operation
ref_12001 = (ref_11997 ^ ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_11383) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_11571) & 0xFFFFFFFFFFFFFFFF) + ref_11647) & 0xFFFFFFFFFFFFFFFF)) + ref_11883) & 0xFFFFFFFFFFFFFFFF) + ref_11959) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_12018 = ref_11930 # MOV operation
ref_12020 = rol(0x15, ref_12018) # ROL operation
ref_12024 = (ref_12020 ^ ((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_11477) & 0xFFFFFFFFFFFFFFFF) + ref_11553) & 0xFFFFFFFFFFFFFFFF)) + ref_11665) & 0xFFFFFFFFFFFFFFFF) ^ ref_11741) + ref_11865) & 0xFFFFFFFFFFFFFFFF)) + ref_11977) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_12053 = ref_12001 # MOV operation
ref_12071 = ref_12024 # MOV operation
ref_12089 = ref_12001 # MOV operation
ref_12091 = rol(0xD, ref_12089) # ROL operation
ref_12095 = (ref_12091 ^ ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_11477) & 0xFFFFFFFFFFFFFFFF) + ref_11553) & 0xFFFFFFFFFFFFFFFF)) + ref_11665) & 0xFFFFFFFFFFFFFFFF) ^ ref_11741) + ref_11865) & 0xFFFFFFFFFFFFFFFF)) + ref_11977) & 0xFFFFFFFFFFFFFFFF) + ref_12053) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_12112 = ref_12024 # MOV operation
ref_12114 = rol(0x10, ref_12112) # ROL operation
ref_12118 = (ref_12114 ^ ((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_11383) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_11571) & 0xFFFFFFFFFFFFFFFF) + ref_11647) & 0xFFFFFFFFFFFFFFFF)) + ref_11883) & 0xFFFFFFFFFFFFFFFF) + ref_11959) & 0xFFFFFFFFFFFFFFFF)) + ref_12071) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_12147 = ref_12095 # MOV operation
ref_12165 = ref_12118 # MOV operation
ref_12183 = ref_12095 # MOV operation
ref_12185 = rol(0x11, ref_12183) # ROL operation
ref_12189 = (ref_12185 ^ ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_11383) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_11571) & 0xFFFFFFFFFFFFFFFF) + ref_11647) & 0xFFFFFFFFFFFFFFFF)) + ref_11883) & 0xFFFFFFFFFFFFFFFF) + ref_11959) & 0xFFFFFFFFFFFFFFFF)) + ref_12071) & 0xFFFFFFFFFFFFFFFF) + ref_12147) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_12206 = ref_12118 # MOV operation
ref_12208 = rol(0x15, ref_12206) # ROL operation
ref_12212 = (ref_12208 ^ ((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_11477) & 0xFFFFFFFFFFFFFFFF) + ref_11553) & 0xFFFFFFFFFFFFFFFF)) + ref_11665) & 0xFFFFFFFFFFFFFFFF) ^ ref_11741) + ref_11865) & 0xFFFFFFFFFFFFFFFF)) + ref_11977) & 0xFFFFFFFFFFFFFFFF) + ref_12053) & 0xFFFFFFFFFFFFFFFF)) + ref_12165) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_12273 = ref_12189 # MOV operation
ref_12291 = ref_12212 # MOV operation
ref_12309 = ref_12189 # MOV operation
ref_12311 = rol(0xD, ref_12309) # ROL operation
ref_12315 = (ref_12311 ^ (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_11477) & 0xFFFFFFFFFFFFFFFF) + ref_11553) & 0xFFFFFFFFFFFFFFFF)) + ref_11665) & 0xFFFFFFFFFFFFFFFF) ^ ref_11741) + ref_11865) & 0xFFFFFFFFFFFFFFFF)) + ref_11977) & 0xFFFFFFFFFFFFFFFF) + ref_12053) & 0xFFFFFFFFFFFFFFFF)) + ref_12165) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_12273) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_12332 = ref_12212 # MOV operation
ref_12334 = rol(0x10, ref_12332) # ROL operation
ref_12338 = (ref_12334 ^ (((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_11383) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_11571) & 0xFFFFFFFFFFFFFFFF) + ref_11647) & 0xFFFFFFFFFFFFFFFF)) + ref_11883) & 0xFFFFFFFFFFFFFFFF) + ref_11959) & 0xFFFFFFFFFFFFFFFF)) + ref_12071) & 0xFFFFFFFFFFFFFFFF) + ref_12147) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_12291) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_12367 = ref_12315 # MOV operation
ref_12385 = ref_12338 # MOV operation
ref_12403 = ref_12315 # MOV operation
ref_12405 = rol(0x11, ref_12403) # ROL operation
ref_12409 = (ref_12405 ^ (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_11383) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_11571) & 0xFFFFFFFFFFFFFFFF) + ref_11647) & 0xFFFFFFFFFFFFFFFF)) + ref_11883) & 0xFFFFFFFFFFFFFFFF) + ref_11959) & 0xFFFFFFFFFFFFFFFF)) + ref_12071) & 0xFFFFFFFFFFFFFFFF) + ref_12147) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_12291) & 0xFFFFFFFFFFFFFFFF) + ref_12367) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_12426 = ref_12338 # MOV operation
ref_12428 = rol(0x15, ref_12426) # ROL operation
ref_12432 = (ref_12428 ^ ((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_11477) & 0xFFFFFFFFFFFFFFFF) + ref_11553) & 0xFFFFFFFFFFFFFFFF)) + ref_11665) & 0xFFFFFFFFFFFFFFFF) ^ ref_11741) + ref_11865) & 0xFFFFFFFFFFFFFFFF)) + ref_11977) & 0xFFFFFFFFFFFFFFFF) + ref_12053) & 0xFFFFFFFFFFFFFFFF)) + ref_12165) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_12273) & 0xFFFFFFFFFFFFFFFF)) + ref_12385) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_12461 = ref_12409 # MOV operation
ref_12479 = ref_12432 # MOV operation
ref_12497 = ref_12409 # MOV operation
ref_12499 = rol(0xD, ref_12497) # ROL operation
ref_12503 = (ref_12499 ^ ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_11477) & 0xFFFFFFFFFFFFFFFF) + ref_11553) & 0xFFFFFFFFFFFFFFFF)) + ref_11665) & 0xFFFFFFFFFFFFFFFF) ^ ref_11741) + ref_11865) & 0xFFFFFFFFFFFFFFFF)) + ref_11977) & 0xFFFFFFFFFFFFFFFF) + ref_12053) & 0xFFFFFFFFFFFFFFFF)) + ref_12165) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_12273) & 0xFFFFFFFFFFFFFFFF)) + ref_12385) & 0xFFFFFFFFFFFFFFFF) + ref_12461) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_12520 = ref_12432 # MOV operation
ref_12522 = rol(0x10, ref_12520) # ROL operation
ref_12526 = (ref_12522 ^ ((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_11383) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_11571) & 0xFFFFFFFFFFFFFFFF) + ref_11647) & 0xFFFFFFFFFFFFFFFF)) + ref_11883) & 0xFFFFFFFFFFFFFFFF) + ref_11959) & 0xFFFFFFFFFFFFFFFF)) + ref_12071) & 0xFFFFFFFFFFFFFFFF) + ref_12147) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_12291) & 0xFFFFFFFFFFFFFFFF) + ref_12367) & 0xFFFFFFFFFFFFFFFF)) + ref_12479) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_12555 = ref_12503 # MOV operation
ref_12573 = ref_12526 # MOV operation
ref_12591 = ref_12503 # MOV operation
ref_12593 = rol(0x11, ref_12591) # ROL operation
ref_12597 = (ref_12593 ^ ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_11383) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_11571) & 0xFFFFFFFFFFFFFFFF) + ref_11647) & 0xFFFFFFFFFFFFFFFF)) + ref_11883) & 0xFFFFFFFFFFFFFFFF) + ref_11959) & 0xFFFFFFFFFFFFFFFF)) + ref_12071) & 0xFFFFFFFFFFFFFFFF) + ref_12147) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_12291) & 0xFFFFFFFFFFFFFFFF) + ref_12367) & 0xFFFFFFFFFFFFFFFF)) + ref_12479) & 0xFFFFFFFFFFFFFFFF) + ref_12555) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_12614 = ref_12526 # MOV operation
ref_12616 = rol(0x15, ref_12614) # ROL operation
ref_12620 = (ref_12616 ^ ((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_11477) & 0xFFFFFFFFFFFFFFFF) + ref_11553) & 0xFFFFFFFFFFFFFFFF)) + ref_11665) & 0xFFFFFFFFFFFFFFFF) ^ ref_11741) + ref_11865) & 0xFFFFFFFFFFFFFFFF)) + ref_11977) & 0xFFFFFFFFFFFFFFFF) + ref_12053) & 0xFFFFFFFFFFFFFFFF)) + ref_12165) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_12273) & 0xFFFFFFFFFFFFFFFF)) + ref_12385) & 0xFFFFFFFFFFFFFFFF) + ref_12461) & 0xFFFFFFFFFFFFFFFF)) + ref_12573) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_12649 = ref_12597 # MOV operation
ref_12667 = ref_12620 # MOV operation
ref_12685 = ref_12597 # MOV operation
ref_12687 = rol(0xD, ref_12685) # ROL operation
ref_12691 = (ref_12687 ^ ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_11477) & 0xFFFFFFFFFFFFFFFF) + ref_11553) & 0xFFFFFFFFFFFFFFFF)) + ref_11665) & 0xFFFFFFFFFFFFFFFF) ^ ref_11741) + ref_11865) & 0xFFFFFFFFFFFFFFFF)) + ref_11977) & 0xFFFFFFFFFFFFFFFF) + ref_12053) & 0xFFFFFFFFFFFFFFFF)) + ref_12165) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_12273) & 0xFFFFFFFFFFFFFFFF)) + ref_12385) & 0xFFFFFFFFFFFFFFFF) + ref_12461) & 0xFFFFFFFFFFFFFFFF)) + ref_12573) & 0xFFFFFFFFFFFFFFFF) + ref_12649) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_12708 = ref_12620 # MOV operation
ref_12710 = rol(0x10, ref_12708) # ROL operation
ref_12714 = (ref_12710 ^ ((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_11383) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_11571) & 0xFFFFFFFFFFFFFFFF) + ref_11647) & 0xFFFFFFFFFFFFFFFF)) + ref_11883) & 0xFFFFFFFFFFFFFFFF) + ref_11959) & 0xFFFFFFFFFFFFFFFF)) + ref_12071) & 0xFFFFFFFFFFFFFFFF) + ref_12147) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_12291) & 0xFFFFFFFFFFFFFFFF) + ref_12367) & 0xFFFFFFFFFFFFFFFF)) + ref_12479) & 0xFFFFFFFFFFFFFFFF) + ref_12555) & 0xFFFFFFFFFFFFFFFF)) + ref_12667) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_12743 = ref_12691 # MOV operation
ref_12761 = ref_12714 # MOV operation
ref_12779 = ref_12691 # MOV operation
ref_12781 = rol(0x11, ref_12779) # ROL operation
ref_12785 = (ref_12781 ^ ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_11383) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_11571) & 0xFFFFFFFFFFFFFFFF) + ref_11647) & 0xFFFFFFFFFFFFFFFF)) + ref_11883) & 0xFFFFFFFFFFFFFFFF) + ref_11959) & 0xFFFFFFFFFFFFFFFF)) + ref_12071) & 0xFFFFFFFFFFFFFFFF) + ref_12147) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_12291) & 0xFFFFFFFFFFFFFFFF) + ref_12367) & 0xFFFFFFFFFFFFFFFF)) + ref_12479) & 0xFFFFFFFFFFFFFFFF) + ref_12555) & 0xFFFFFFFFFFFFFFFF)) + ref_12667) & 0xFFFFFFFFFFFFFFFF) + ref_12743) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_12802 = ref_12714 # MOV operation
ref_12804 = rol(0x15, ref_12802) # ROL operation
ref_12808 = (ref_12804 ^ ((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_11477) & 0xFFFFFFFFFFFFFFFF) + ref_11553) & 0xFFFFFFFFFFFFFFFF)) + ref_11665) & 0xFFFFFFFFFFFFFFFF) ^ ref_11741) + ref_11865) & 0xFFFFFFFFFFFFFFFF)) + ref_11977) & 0xFFFFFFFFFFFFFFFF) + ref_12053) & 0xFFFFFFFFFFFFFFFF)) + ref_12165) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_12273) & 0xFFFFFFFFFFFFFFFF)) + ref_12385) & 0xFFFFFFFFFFFFFFFF) + ref_12461) & 0xFFFFFFFFFFFFFFFF)) + ref_12573) & 0xFFFFFFFFFFFFFFFF) + ref_12649) & 0xFFFFFFFFFFFFFFFF)) + ref_12761) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_12837 = ref_12785 # MOV operation
ref_12855 = ref_12808 # MOV operation
ref_12873 = ref_12785 # MOV operation
ref_12875 = rol(0xD, ref_12873) # ROL operation
ref_12879 = (ref_12875 ^ ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_11477) & 0xFFFFFFFFFFFFFFFF) + ref_11553) & 0xFFFFFFFFFFFFFFFF)) + ref_11665) & 0xFFFFFFFFFFFFFFFF) ^ ref_11741) + ref_11865) & 0xFFFFFFFFFFFFFFFF)) + ref_11977) & 0xFFFFFFFFFFFFFFFF) + ref_12053) & 0xFFFFFFFFFFFFFFFF)) + ref_12165) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_12273) & 0xFFFFFFFFFFFFFFFF)) + ref_12385) & 0xFFFFFFFFFFFFFFFF) + ref_12461) & 0xFFFFFFFFFFFFFFFF)) + ref_12573) & 0xFFFFFFFFFFFFFFFF) + ref_12649) & 0xFFFFFFFFFFFFFFFF)) + ref_12761) & 0xFFFFFFFFFFFFFFFF) + ref_12837) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_12896 = ref_12808 # MOV operation
ref_12898 = rol(0x10, ref_12896) # ROL operation
ref_12902 = (ref_12898 ^ ((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_11383) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_11571) & 0xFFFFFFFFFFFFFFFF) + ref_11647) & 0xFFFFFFFFFFFFFFFF)) + ref_11883) & 0xFFFFFFFFFFFFFFFF) + ref_11959) & 0xFFFFFFFFFFFFFFFF)) + ref_12071) & 0xFFFFFFFFFFFFFFFF) + ref_12147) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_12291) & 0xFFFFFFFFFFFFFFFF) + ref_12367) & 0xFFFFFFFFFFFFFFFF)) + ref_12479) & 0xFFFFFFFFFFFFFFFF) + ref_12555) & 0xFFFFFFFFFFFFFFFF)) + ref_12667) & 0xFFFFFFFFFFFFFFFF) + ref_12743) & 0xFFFFFFFFFFFFFFFF)) + ref_12855) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_12931 = ref_12879 # MOV operation
ref_12949 = ref_12902 # MOV operation
ref_12967 = ref_12879 # MOV operation
ref_12969 = rol(0x11, ref_12967) # ROL operation
ref_12973 = (ref_12969 ^ ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_11383) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_11571) & 0xFFFFFFFFFFFFFFFF) + ref_11647) & 0xFFFFFFFFFFFFFFFF)) + ref_11883) & 0xFFFFFFFFFFFFFFFF) + ref_11959) & 0xFFFFFFFFFFFFFFFF)) + ref_12071) & 0xFFFFFFFFFFFFFFFF) + ref_12147) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_12291) & 0xFFFFFFFFFFFFFFFF) + ref_12367) & 0xFFFFFFFFFFFFFFFF)) + ref_12479) & 0xFFFFFFFFFFFFFFFF) + ref_12555) & 0xFFFFFFFFFFFFFFFF)) + ref_12667) & 0xFFFFFFFFFFFFFFFF) + ref_12743) & 0xFFFFFFFFFFFFFFFF)) + ref_12855) & 0xFFFFFFFFFFFFFFFF) + ref_12931) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_12990 = ref_12902 # MOV operation
ref_12992 = rol(0x15, ref_12990) # ROL operation
ref_12996 = (ref_12992 ^ ((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_11477) & 0xFFFFFFFFFFFFFFFF) + ref_11553) & 0xFFFFFFFFFFFFFFFF)) + ref_11665) & 0xFFFFFFFFFFFFFFFF) ^ ref_11741) + ref_11865) & 0xFFFFFFFFFFFFFFFF)) + ref_11977) & 0xFFFFFFFFFFFFFFFF) + ref_12053) & 0xFFFFFFFFFFFFFFFF)) + ref_12165) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_12273) & 0xFFFFFFFFFFFFFFFF)) + ref_12385) & 0xFFFFFFFFFFFFFFFF) + ref_12461) & 0xFFFFFFFFFFFFFFFF)) + ref_12573) & 0xFFFFFFFFFFFFFFFF) + ref_12649) & 0xFFFFFFFFFFFFFFFF)) + ref_12761) & 0xFFFFFFFFFFFFFFFF) + ref_12837) & 0xFFFFFFFFFFFFFFFF)) + ref_12949) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_13025 = ((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_11477) & 0xFFFFFFFFFFFFFFFF) + ref_11553) & 0xFFFFFFFFFFFFFFFF)) + ref_11665) & 0xFFFFFFFFFFFFFFFF) ^ ref_11741) + ref_11865) & 0xFFFFFFFFFFFFFFFF)) + ref_11977) & 0xFFFFFFFFFFFFFFFF) + ref_12053) & 0xFFFFFFFFFFFFFFFF)) + ref_12165) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_12273) & 0xFFFFFFFFFFFFFFFF)) + ref_12385) & 0xFFFFFFFFFFFFFFFF) + ref_12461) & 0xFFFFFFFFFFFFFFFF)) + ref_12573) & 0xFFFFFFFFFFFFFFFF) + ref_12649) & 0xFFFFFFFFFFFFFFFF)) + ref_12761) & 0xFFFFFFFFFFFFFFFF) + ref_12837) & 0xFFFFFFFFFFFFFFFF)) + ref_12949) & 0xFFFFFFFFFFFFFFFF) # MOV operation
ref_13027 = (ref_13025 ^ ref_12973) # XOR operation
ref_13034 = ref_13027 # MOV operation
ref_13036 = rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_11383) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_11571) & 0xFFFFFFFFFFFFFFFF) + ref_11647) & 0xFFFFFFFFFFFFFFFF)) + ref_11883) & 0xFFFFFFFFFFFFFFFF) + ref_11959) & 0xFFFFFFFFFFFFFFFF)) + ref_12071) & 0xFFFFFFFFFFFFFFFF) + ref_12147) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_12291) & 0xFFFFFFFFFFFFFFFF) + ref_12367) & 0xFFFFFFFFFFFFFFFF)) + ref_12479) & 0xFFFFFFFFFFFFFFFF) + ref_12555) & 0xFFFFFFFFFFFFFFFF)) + ref_12667) & 0xFFFFFFFFFFFFFFFF) + ref_12743) & 0xFFFFFFFFFFFFFFFF)) + ref_12855) & 0xFFFFFFFFFFFFFFFF) + ref_12931) & 0xFFFFFFFFFFFFFFFF)) # MOV operation
ref_13038 = (ref_13036 ^ ref_12996) # XOR operation
ref_13045 = (ref_13038 ^ ref_13034) # XOR operation
ref_13271 = ref_13045 # MOV operation
ref_13305 = ref_13271 # MOV operation
ref_13501 = ref_13305 # MOV operation
ref_13628 = ref_13501 # MOV operation
ref_13666 = ref_13628 # MOV operation
ref_13678 = ref_13666 # MOV operation
ref_13680 = ref_13678 # MOV operation

print(ref_13680 & 0xffffffffffffffff)
