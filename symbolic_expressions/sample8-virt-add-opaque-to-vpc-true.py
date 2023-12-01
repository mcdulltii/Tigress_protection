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
ref_28410 = ref_239 # MOV operation
ref_28454 = ref_28410 # MOV operation
ref_28489 = (((((((((0x7B) << 8 | 0x6B) << 8 | 0x69) << 8 | 0x6E) << 8 | 0x72) << 8 | 0x7E) << 8 | 0x6C) << 8 | 0x7B) ^ ref_28454) # MOV operation
ref_28530 = (((((((((0x7B) << 8 | 0x6B) << 8 | 0x69) << 8 | 0x6E) << 8 | 0x72) << 8 | 0x7E) << 8 | 0x6C) << 8 | 0x7B) ^ ref_28454) # MOV operation
ref_28532 = rol(0x10, ref_28530) # ROL operation
ref_28536 = (ref_28532 ^ ((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_28489) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_28583 = ref_28536 # MOV operation
ref_28607 = (0x96C62826CF6DE04E ^ ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_28489) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_28624 = ref_28536 # MOV operation
ref_28626 = rol(0x15, ref_28624) # ROL operation
ref_28630 = (ref_28626 ^ ((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_28583) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_28659 = ref_28607 # MOV operation
ref_28677 = ref_28630 # MOV operation
ref_28695 = ref_28607 # MOV operation
ref_28697 = rol(0xD, ref_28695) # ROL operation
ref_28701 = (ref_28697 ^ ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_28583) & 0xFFFFFFFFFFFFFFFF) + ref_28659) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_28718 = ref_28630 # MOV operation
ref_28720 = rol(0x10, ref_28718) # ROL operation
ref_28724 = (ref_28720 ^ ((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_28489) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_28677) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_28753 = ref_28701 # MOV operation
ref_28771 = ref_28724 # MOV operation
ref_28789 = ref_28701 # MOV operation
ref_28791 = rol(0x11, ref_28789) # ROL operation
ref_28795 = (ref_28791 ^ ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_28489) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_28677) & 0xFFFFFFFFFFFFFFFF) + ref_28753) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_28812 = ref_28724 # MOV operation
ref_28814 = rol(0x15, ref_28812) # ROL operation
ref_28818 = (ref_28814 ^ ((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_28583) & 0xFFFFFFFFFFFFFFFF) + ref_28659) & 0xFFFFFFFFFFFFFFFF)) + ref_28771) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_28847 = ref_28410 # MOV operation
ref_28971 = ref_28795 # MOV operation
ref_28989 = (ref_28818 ^ 0x800000000000000) # MOV operation
ref_29007 = ref_28795 # MOV operation
ref_29009 = rol(0xD, ref_29007) # ROL operation
ref_29013 = (ref_29009 ^ (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_28583) & 0xFFFFFFFFFFFFFFFF) + ref_28659) & 0xFFFFFFFFFFFFFFFF)) + ref_28771) & 0xFFFFFFFFFFFFFFFF) ^ ref_28847) + ref_28971) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_29030 = (ref_28818 ^ 0x800000000000000) # MOV operation
ref_29032 = rol(0x10, ref_29030) # ROL operation
ref_29036 = (ref_29032 ^ ((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_28489) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_28677) & 0xFFFFFFFFFFFFFFFF) + ref_28753) & 0xFFFFFFFFFFFFFFFF)) + ref_28989) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_29065 = ref_29013 # MOV operation
ref_29083 = ref_29036 # MOV operation
ref_29101 = ref_29013 # MOV operation
ref_29103 = rol(0x11, ref_29101) # ROL operation
ref_29107 = (ref_29103 ^ ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_28489) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_28677) & 0xFFFFFFFFFFFFFFFF) + ref_28753) & 0xFFFFFFFFFFFFFFFF)) + ref_28989) & 0xFFFFFFFFFFFFFFFF) + ref_29065) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_29124 = ref_29036 # MOV operation
ref_29126 = rol(0x15, ref_29124) # ROL operation
ref_29130 = (ref_29126 ^ ((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_28583) & 0xFFFFFFFFFFFFFFFF) + ref_28659) & 0xFFFFFFFFFFFFFFFF)) + ref_28771) & 0xFFFFFFFFFFFFFFFF) ^ ref_28847) + ref_28971) & 0xFFFFFFFFFFFFFFFF)) + ref_29083) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_29159 = ref_29107 # MOV operation
ref_29177 = ref_29130 # MOV operation
ref_29195 = ref_29107 # MOV operation
ref_29197 = rol(0xD, ref_29195) # ROL operation
ref_29201 = (ref_29197 ^ ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_28583) & 0xFFFFFFFFFFFFFFFF) + ref_28659) & 0xFFFFFFFFFFFFFFFF)) + ref_28771) & 0xFFFFFFFFFFFFFFFF) ^ ref_28847) + ref_28971) & 0xFFFFFFFFFFFFFFFF)) + ref_29083) & 0xFFFFFFFFFFFFFFFF) + ref_29159) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_29218 = ref_29130 # MOV operation
ref_29220 = rol(0x10, ref_29218) # ROL operation
ref_29224 = (ref_29220 ^ ((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_28489) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_28677) & 0xFFFFFFFFFFFFFFFF) + ref_28753) & 0xFFFFFFFFFFFFFFFF)) + ref_28989) & 0xFFFFFFFFFFFFFFFF) + ref_29065) & 0xFFFFFFFFFFFFFFFF)) + ref_29177) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_29253 = ref_29201 # MOV operation
ref_29271 = ref_29224 # MOV operation
ref_29289 = ref_29201 # MOV operation
ref_29291 = rol(0x11, ref_29289) # ROL operation
ref_29295 = (ref_29291 ^ ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_28489) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_28677) & 0xFFFFFFFFFFFFFFFF) + ref_28753) & 0xFFFFFFFFFFFFFFFF)) + ref_28989) & 0xFFFFFFFFFFFFFFFF) + ref_29065) & 0xFFFFFFFFFFFFFFFF)) + ref_29177) & 0xFFFFFFFFFFFFFFFF) + ref_29253) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_29312 = ref_29224 # MOV operation
ref_29314 = rol(0x15, ref_29312) # ROL operation
ref_29318 = (ref_29314 ^ ((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_28583) & 0xFFFFFFFFFFFFFFFF) + ref_28659) & 0xFFFFFFFFFFFFFFFF)) + ref_28771) & 0xFFFFFFFFFFFFFFFF) ^ ref_28847) + ref_28971) & 0xFFFFFFFFFFFFFFFF)) + ref_29083) & 0xFFFFFFFFFFFFFFFF) + ref_29159) & 0xFFFFFFFFFFFFFFFF)) + ref_29271) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_29379 = ref_29295 # MOV operation
ref_29397 = ref_29318 # MOV operation
ref_29415 = ref_29295 # MOV operation
ref_29417 = rol(0xD, ref_29415) # ROL operation
ref_29421 = (ref_29417 ^ (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_28583) & 0xFFFFFFFFFFFFFFFF) + ref_28659) & 0xFFFFFFFFFFFFFFFF)) + ref_28771) & 0xFFFFFFFFFFFFFFFF) ^ ref_28847) + ref_28971) & 0xFFFFFFFFFFFFFFFF)) + ref_29083) & 0xFFFFFFFFFFFFFFFF) + ref_29159) & 0xFFFFFFFFFFFFFFFF)) + ref_29271) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_29379) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_29438 = ref_29318 # MOV operation
ref_29440 = rol(0x10, ref_29438) # ROL operation
ref_29444 = (ref_29440 ^ (((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_28489) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_28677) & 0xFFFFFFFFFFFFFFFF) + ref_28753) & 0xFFFFFFFFFFFFFFFF)) + ref_28989) & 0xFFFFFFFFFFFFFFFF) + ref_29065) & 0xFFFFFFFFFFFFFFFF)) + ref_29177) & 0xFFFFFFFFFFFFFFFF) + ref_29253) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_29397) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_29473 = ref_29421 # MOV operation
ref_29491 = ref_29444 # MOV operation
ref_29509 = ref_29421 # MOV operation
ref_29511 = rol(0x11, ref_29509) # ROL operation
ref_29515 = (ref_29511 ^ (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_28489) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_28677) & 0xFFFFFFFFFFFFFFFF) + ref_28753) & 0xFFFFFFFFFFFFFFFF)) + ref_28989) & 0xFFFFFFFFFFFFFFFF) + ref_29065) & 0xFFFFFFFFFFFFFFFF)) + ref_29177) & 0xFFFFFFFFFFFFFFFF) + ref_29253) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_29397) & 0xFFFFFFFFFFFFFFFF) + ref_29473) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_29532 = ref_29444 # MOV operation
ref_29534 = rol(0x15, ref_29532) # ROL operation
ref_29538 = (ref_29534 ^ ((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_28583) & 0xFFFFFFFFFFFFFFFF) + ref_28659) & 0xFFFFFFFFFFFFFFFF)) + ref_28771) & 0xFFFFFFFFFFFFFFFF) ^ ref_28847) + ref_28971) & 0xFFFFFFFFFFFFFFFF)) + ref_29083) & 0xFFFFFFFFFFFFFFFF) + ref_29159) & 0xFFFFFFFFFFFFFFFF)) + ref_29271) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_29379) & 0xFFFFFFFFFFFFFFFF)) + ref_29491) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_29567 = ref_29515 # MOV operation
ref_29585 = ref_29538 # MOV operation
ref_29603 = ref_29515 # MOV operation
ref_29605 = rol(0xD, ref_29603) # ROL operation
ref_29609 = (ref_29605 ^ ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_28583) & 0xFFFFFFFFFFFFFFFF) + ref_28659) & 0xFFFFFFFFFFFFFFFF)) + ref_28771) & 0xFFFFFFFFFFFFFFFF) ^ ref_28847) + ref_28971) & 0xFFFFFFFFFFFFFFFF)) + ref_29083) & 0xFFFFFFFFFFFFFFFF) + ref_29159) & 0xFFFFFFFFFFFFFFFF)) + ref_29271) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_29379) & 0xFFFFFFFFFFFFFFFF)) + ref_29491) & 0xFFFFFFFFFFFFFFFF) + ref_29567) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_29626 = ref_29538 # MOV operation
ref_29628 = rol(0x10, ref_29626) # ROL operation
ref_29632 = (ref_29628 ^ ((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_28489) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_28677) & 0xFFFFFFFFFFFFFFFF) + ref_28753) & 0xFFFFFFFFFFFFFFFF)) + ref_28989) & 0xFFFFFFFFFFFFFFFF) + ref_29065) & 0xFFFFFFFFFFFFFFFF)) + ref_29177) & 0xFFFFFFFFFFFFFFFF) + ref_29253) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_29397) & 0xFFFFFFFFFFFFFFFF) + ref_29473) & 0xFFFFFFFFFFFFFFFF)) + ref_29585) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_29661 = ref_29609 # MOV operation
ref_29679 = ref_29632 # MOV operation
ref_29697 = ref_29609 # MOV operation
ref_29699 = rol(0x11, ref_29697) # ROL operation
ref_29703 = (ref_29699 ^ ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_28489) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_28677) & 0xFFFFFFFFFFFFFFFF) + ref_28753) & 0xFFFFFFFFFFFFFFFF)) + ref_28989) & 0xFFFFFFFFFFFFFFFF) + ref_29065) & 0xFFFFFFFFFFFFFFFF)) + ref_29177) & 0xFFFFFFFFFFFFFFFF) + ref_29253) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_29397) & 0xFFFFFFFFFFFFFFFF) + ref_29473) & 0xFFFFFFFFFFFFFFFF)) + ref_29585) & 0xFFFFFFFFFFFFFFFF) + ref_29661) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_29720 = ref_29632 # MOV operation
ref_29722 = rol(0x15, ref_29720) # ROL operation
ref_29726 = (ref_29722 ^ ((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_28583) & 0xFFFFFFFFFFFFFFFF) + ref_28659) & 0xFFFFFFFFFFFFFFFF)) + ref_28771) & 0xFFFFFFFFFFFFFFFF) ^ ref_28847) + ref_28971) & 0xFFFFFFFFFFFFFFFF)) + ref_29083) & 0xFFFFFFFFFFFFFFFF) + ref_29159) & 0xFFFFFFFFFFFFFFFF)) + ref_29271) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_29379) & 0xFFFFFFFFFFFFFFFF)) + ref_29491) & 0xFFFFFFFFFFFFFFFF) + ref_29567) & 0xFFFFFFFFFFFFFFFF)) + ref_29679) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_29755 = ref_29703 # MOV operation
ref_29773 = ref_29726 # MOV operation
ref_29791 = ref_29703 # MOV operation
ref_29793 = rol(0xD, ref_29791) # ROL operation
ref_29797 = (ref_29793 ^ ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_28583) & 0xFFFFFFFFFFFFFFFF) + ref_28659) & 0xFFFFFFFFFFFFFFFF)) + ref_28771) & 0xFFFFFFFFFFFFFFFF) ^ ref_28847) + ref_28971) & 0xFFFFFFFFFFFFFFFF)) + ref_29083) & 0xFFFFFFFFFFFFFFFF) + ref_29159) & 0xFFFFFFFFFFFFFFFF)) + ref_29271) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_29379) & 0xFFFFFFFFFFFFFFFF)) + ref_29491) & 0xFFFFFFFFFFFFFFFF) + ref_29567) & 0xFFFFFFFFFFFFFFFF)) + ref_29679) & 0xFFFFFFFFFFFFFFFF) + ref_29755) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_29814 = ref_29726 # MOV operation
ref_29816 = rol(0x10, ref_29814) # ROL operation
ref_29820 = (ref_29816 ^ ((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_28489) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_28677) & 0xFFFFFFFFFFFFFFFF) + ref_28753) & 0xFFFFFFFFFFFFFFFF)) + ref_28989) & 0xFFFFFFFFFFFFFFFF) + ref_29065) & 0xFFFFFFFFFFFFFFFF)) + ref_29177) & 0xFFFFFFFFFFFFFFFF) + ref_29253) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_29397) & 0xFFFFFFFFFFFFFFFF) + ref_29473) & 0xFFFFFFFFFFFFFFFF)) + ref_29585) & 0xFFFFFFFFFFFFFFFF) + ref_29661) & 0xFFFFFFFFFFFFFFFF)) + ref_29773) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_29849 = ref_29797 # MOV operation
ref_29867 = ref_29820 # MOV operation
ref_29885 = ref_29797 # MOV operation
ref_29887 = rol(0x11, ref_29885) # ROL operation
ref_29891 = (ref_29887 ^ ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_28489) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_28677) & 0xFFFFFFFFFFFFFFFF) + ref_28753) & 0xFFFFFFFFFFFFFFFF)) + ref_28989) & 0xFFFFFFFFFFFFFFFF) + ref_29065) & 0xFFFFFFFFFFFFFFFF)) + ref_29177) & 0xFFFFFFFFFFFFFFFF) + ref_29253) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_29397) & 0xFFFFFFFFFFFFFFFF) + ref_29473) & 0xFFFFFFFFFFFFFFFF)) + ref_29585) & 0xFFFFFFFFFFFFFFFF) + ref_29661) & 0xFFFFFFFFFFFFFFFF)) + ref_29773) & 0xFFFFFFFFFFFFFFFF) + ref_29849) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_29908 = ref_29820 # MOV operation
ref_29910 = rol(0x15, ref_29908) # ROL operation
ref_29914 = (ref_29910 ^ ((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_28583) & 0xFFFFFFFFFFFFFFFF) + ref_28659) & 0xFFFFFFFFFFFFFFFF)) + ref_28771) & 0xFFFFFFFFFFFFFFFF) ^ ref_28847) + ref_28971) & 0xFFFFFFFFFFFFFFFF)) + ref_29083) & 0xFFFFFFFFFFFFFFFF) + ref_29159) & 0xFFFFFFFFFFFFFFFF)) + ref_29271) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_29379) & 0xFFFFFFFFFFFFFFFF)) + ref_29491) & 0xFFFFFFFFFFFFFFFF) + ref_29567) & 0xFFFFFFFFFFFFFFFF)) + ref_29679) & 0xFFFFFFFFFFFFFFFF) + ref_29755) & 0xFFFFFFFFFFFFFFFF)) + ref_29867) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_29943 = ref_29891 # MOV operation
ref_29961 = ref_29914 # MOV operation
ref_29979 = ref_29891 # MOV operation
ref_29981 = rol(0xD, ref_29979) # ROL operation
ref_29985 = (ref_29981 ^ ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_28583) & 0xFFFFFFFFFFFFFFFF) + ref_28659) & 0xFFFFFFFFFFFFFFFF)) + ref_28771) & 0xFFFFFFFFFFFFFFFF) ^ ref_28847) + ref_28971) & 0xFFFFFFFFFFFFFFFF)) + ref_29083) & 0xFFFFFFFFFFFFFFFF) + ref_29159) & 0xFFFFFFFFFFFFFFFF)) + ref_29271) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_29379) & 0xFFFFFFFFFFFFFFFF)) + ref_29491) & 0xFFFFFFFFFFFFFFFF) + ref_29567) & 0xFFFFFFFFFFFFFFFF)) + ref_29679) & 0xFFFFFFFFFFFFFFFF) + ref_29755) & 0xFFFFFFFFFFFFFFFF)) + ref_29867) & 0xFFFFFFFFFFFFFFFF) + ref_29943) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_30002 = ref_29914 # MOV operation
ref_30004 = rol(0x10, ref_30002) # ROL operation
ref_30008 = (ref_30004 ^ ((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_28489) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_28677) & 0xFFFFFFFFFFFFFFFF) + ref_28753) & 0xFFFFFFFFFFFFFFFF)) + ref_28989) & 0xFFFFFFFFFFFFFFFF) + ref_29065) & 0xFFFFFFFFFFFFFFFF)) + ref_29177) & 0xFFFFFFFFFFFFFFFF) + ref_29253) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_29397) & 0xFFFFFFFFFFFFFFFF) + ref_29473) & 0xFFFFFFFFFFFFFFFF)) + ref_29585) & 0xFFFFFFFFFFFFFFFF) + ref_29661) & 0xFFFFFFFFFFFFFFFF)) + ref_29773) & 0xFFFFFFFFFFFFFFFF) + ref_29849) & 0xFFFFFFFFFFFFFFFF)) + ref_29961) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_30037 = ref_29985 # MOV operation
ref_30055 = ref_30008 # MOV operation
ref_30073 = ref_29985 # MOV operation
ref_30075 = rol(0x11, ref_30073) # ROL operation
ref_30079 = (ref_30075 ^ ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_28489) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_28677) & 0xFFFFFFFFFFFFFFFF) + ref_28753) & 0xFFFFFFFFFFFFFFFF)) + ref_28989) & 0xFFFFFFFFFFFFFFFF) + ref_29065) & 0xFFFFFFFFFFFFFFFF)) + ref_29177) & 0xFFFFFFFFFFFFFFFF) + ref_29253) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_29397) & 0xFFFFFFFFFFFFFFFF) + ref_29473) & 0xFFFFFFFFFFFFFFFF)) + ref_29585) & 0xFFFFFFFFFFFFFFFF) + ref_29661) & 0xFFFFFFFFFFFFFFFF)) + ref_29773) & 0xFFFFFFFFFFFFFFFF) + ref_29849) & 0xFFFFFFFFFFFFFFFF)) + ref_29961) & 0xFFFFFFFFFFFFFFFF) + ref_30037) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_30096 = ref_30008 # MOV operation
ref_30098 = rol(0x15, ref_30096) # ROL operation
ref_30102 = (ref_30098 ^ ((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_28583) & 0xFFFFFFFFFFFFFFFF) + ref_28659) & 0xFFFFFFFFFFFFFFFF)) + ref_28771) & 0xFFFFFFFFFFFFFFFF) ^ ref_28847) + ref_28971) & 0xFFFFFFFFFFFFFFFF)) + ref_29083) & 0xFFFFFFFFFFFFFFFF) + ref_29159) & 0xFFFFFFFFFFFFFFFF)) + ref_29271) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_29379) & 0xFFFFFFFFFFFFFFFF)) + ref_29491) & 0xFFFFFFFFFFFFFFFF) + ref_29567) & 0xFFFFFFFFFFFFFFFF)) + ref_29679) & 0xFFFFFFFFFFFFFFFF) + ref_29755) & 0xFFFFFFFFFFFFFFFF)) + ref_29867) & 0xFFFFFFFFFFFFFFFF) + ref_29943) & 0xFFFFFFFFFFFFFFFF)) + ref_30055) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_30131 = ((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_28583) & 0xFFFFFFFFFFFFFFFF) + ref_28659) & 0xFFFFFFFFFFFFFFFF)) + ref_28771) & 0xFFFFFFFFFFFFFFFF) ^ ref_28847) + ref_28971) & 0xFFFFFFFFFFFFFFFF)) + ref_29083) & 0xFFFFFFFFFFFFFFFF) + ref_29159) & 0xFFFFFFFFFFFFFFFF)) + ref_29271) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_29379) & 0xFFFFFFFFFFFFFFFF)) + ref_29491) & 0xFFFFFFFFFFFFFFFF) + ref_29567) & 0xFFFFFFFFFFFFFFFF)) + ref_29679) & 0xFFFFFFFFFFFFFFFF) + ref_29755) & 0xFFFFFFFFFFFFFFFF)) + ref_29867) & 0xFFFFFFFFFFFFFFFF) + ref_29943) & 0xFFFFFFFFFFFFFFFF)) + ref_30055) & 0xFFFFFFFFFFFFFFFF) # MOV operation
ref_30133 = (ref_30131 ^ ref_30079) # XOR operation
ref_30140 = ref_30133 # MOV operation
ref_30142 = rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_28489) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_28677) & 0xFFFFFFFFFFFFFFFF) + ref_28753) & 0xFFFFFFFFFFFFFFFF)) + ref_28989) & 0xFFFFFFFFFFFFFFFF) + ref_29065) & 0xFFFFFFFFFFFFFFFF)) + ref_29177) & 0xFFFFFFFFFFFFFFFF) + ref_29253) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_29397) & 0xFFFFFFFFFFFFFFFF) + ref_29473) & 0xFFFFFFFFFFFFFFFF)) + ref_29585) & 0xFFFFFFFFFFFFFFFF) + ref_29661) & 0xFFFFFFFFFFFFFFFF)) + ref_29773) & 0xFFFFFFFFFFFFFFFF) + ref_29849) & 0xFFFFFFFFFFFFFFFF)) + ref_29961) & 0xFFFFFFFFFFFFFFFF) + ref_30037) & 0xFFFFFFFFFFFFFFFF)) # MOV operation
ref_30144 = (ref_30142 ^ ref_30102) # XOR operation
ref_30151 = (ref_30144 ^ ref_30140) # XOR operation
ref_30630 = ref_30151 # MOV operation
ref_30788 = ref_30630 # MOV operation
ref_31210 = ref_30788 # MOV operation
ref_31313 = ref_31210 # MOV operation
ref_31351 = ref_31313 # MOV operation
ref_31363 = ref_31351 # MOV operation
ref_31365 = ref_31363 # MOV operation

print(ref_31365 & 0xffffffffffffffff)
