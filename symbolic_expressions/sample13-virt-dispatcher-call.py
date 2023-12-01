#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_524 = SymVar_0
ref_535 = ref_524 # MOV operation
ref_547 = ref_535 # MOV operation
ref_549 = ref_547 # MOV operation
ref_6669 = ref_549 # MOV operation
ref_6673 = ((0xDEADBEEFDEADBEEF + ref_6669) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_6780 = ref_6673 # MOV operation
ref_6782 = (0xE6ADBEEFDEADBEEF ^ ref_6780) # XOR operation
ref_6803 = ref_6673 # MOV operation
ref_6807 = ref_6803 # MOV operation
ref_6851 = ref_6807 # MOV operation
ref_6855 = rol(0xF, ref_6851) # ROL operation
ref_6859 = ref_6855 # MOV operation
ref_6866 = ref_6859 # MOV operation
ref_6882 = ref_6782 # MOV operation
ref_6886 = ref_6866 # MOV operation
ref_6888 = ((ref_6882 + ref_6886) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_6914 = ref_6888 # MOV operation
ref_6916 = (0x1234 ^ ref_6914) # XOR operation
ref_6937 = ref_6888 # MOV operation
ref_6941 = ref_6937 # MOV operation
ref_6985 = ref_6941 # MOV operation
ref_6989 = rol(0x34, ref_6985) # ROL operation
ref_6993 = ref_6989 # MOV operation
ref_7000 = ref_6993 # MOV operation
ref_7016 = ref_6916 # MOV operation
ref_7020 = ref_7000 # MOV operation
ref_7022 = ((ref_7016 + ref_7020) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_7048 = ref_7022 # MOV operation
ref_7050 = (0x1234 ^ ref_7048) # XOR operation
ref_7071 = ref_7022 # MOV operation
ref_7075 = ref_7071 # MOV operation
ref_7119 = ref_7075 # MOV operation
ref_7123 = rol(0x1A, ref_7119) # ROL operation
ref_7127 = ref_7123 # MOV operation
ref_7134 = ref_7127 # MOV operation
ref_7150 = ref_7050 # MOV operation
ref_7154 = ref_7134 # MOV operation
ref_7156 = ((ref_7150 + ref_7154) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_7178 = ref_6866 # MOV operation
ref_7182 = ref_7156 # MOV operation
ref_7184 = (ref_7178 ^ ref_7182) # XOR operation
ref_7205 = ref_7156 # MOV operation
ref_7209 = ref_7205 # MOV operation
ref_7253 = ref_7209 # MOV operation
ref_7257 = rol(0x33, ref_7253) # ROL operation
ref_7261 = ref_7257 # MOV operation
ref_7268 = ref_7261 # MOV operation
ref_7284 = ref_7184 # MOV operation
ref_7288 = ref_7268 # MOV operation
ref_7290 = ((ref_7284 + ref_7288) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_7312 = ref_7000 # MOV operation
ref_7316 = ref_7290 # MOV operation
ref_7318 = (ref_7312 ^ ref_7316) # XOR operation
ref_7339 = ref_7290 # MOV operation
ref_7343 = ref_7339 # MOV operation
ref_7387 = ref_7343 # MOV operation
ref_7391 = rol(0x1C, ref_7387) # ROL operation
ref_7395 = ref_7391 # MOV operation
ref_7402 = ref_7395 # MOV operation
ref_7418 = ref_7318 # MOV operation
ref_7422 = ref_7402 # MOV operation
ref_7424 = ((ref_7418 + ref_7422) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_7446 = ref_7134 # MOV operation
ref_7450 = ref_7424 # MOV operation
ref_7452 = (ref_7446 ^ ref_7450) # XOR operation
ref_7473 = ref_7424 # MOV operation
ref_7477 = ref_7473 # MOV operation
ref_7521 = ref_7477 # MOV operation
ref_7525 = rol(0x9, ref_7521) # ROL operation
ref_7529 = ref_7525 # MOV operation
ref_7536 = ref_7529 # MOV operation
ref_7552 = ref_7452 # MOV operation
ref_7556 = ref_7536 # MOV operation
ref_7558 = ((ref_7552 + ref_7556) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_7580 = ref_7268 # MOV operation
ref_7584 = ref_7558 # MOV operation
ref_7586 = (ref_7580 ^ ref_7584) # XOR operation
ref_7607 = ref_7558 # MOV operation
ref_7611 = ref_7607 # MOV operation
ref_7655 = ref_7611 # MOV operation
ref_7659 = rol(0x2F, ref_7655) # ROL operation
ref_7663 = ref_7659 # MOV operation
ref_7670 = ref_7663 # MOV operation
ref_7686 = ref_7586 # MOV operation
ref_7690 = ref_7670 # MOV operation
ref_7692 = ((ref_7686 + ref_7690) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_7714 = ref_7402 # MOV operation
ref_7718 = ref_7692 # MOV operation
ref_7720 = (ref_7714 ^ ref_7718) # XOR operation
ref_7741 = ref_7692 # MOV operation
ref_7745 = ref_7741 # MOV operation
ref_7789 = ref_7745 # MOV operation
ref_7793 = rol(0x36, ref_7789) # ROL operation
ref_7797 = ref_7793 # MOV operation
ref_7804 = ref_7797 # MOV operation
ref_7820 = ref_7720 # MOV operation
ref_7824 = ref_7804 # MOV operation
ref_7826 = ((ref_7820 + ref_7824) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_7848 = ref_7536 # MOV operation
ref_7852 = ref_7826 # MOV operation
ref_7854 = (ref_7848 ^ ref_7852) # XOR operation
ref_7875 = ref_7826 # MOV operation
ref_7879 = ref_7875 # MOV operation
ref_7923 = ref_7879 # MOV operation
ref_7927 = rol(0x20, ref_7923) # ROL operation
ref_7931 = ref_7927 # MOV operation
ref_7938 = ref_7931 # MOV operation
ref_7954 = ref_7854 # MOV operation
ref_7958 = ref_7938 # MOV operation
ref_7960 = ((ref_7954 + ref_7958) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_7982 = ref_7670 # MOV operation
ref_7986 = ref_7960 # MOV operation
ref_7988 = (ref_7982 ^ ref_7986) # XOR operation
ref_8009 = ref_7960 # MOV operation
ref_8013 = ref_8009 # MOV operation
ref_8057 = ref_8013 # MOV operation
ref_8061 = rol(0x19, ref_8057) # ROL operation
ref_8065 = ref_8061 # MOV operation
ref_8072 = ref_8065 # MOV operation
ref_8088 = ref_7988 # MOV operation
ref_8092 = ref_8072 # MOV operation
ref_8094 = ((ref_8088 + ref_8092) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_8143 = ref_8094 # MOV operation
ref_8147 = ref_8143 # MOV operation
ref_8191 = ref_8147 # MOV operation
ref_8195 = rol(0x3F, ref_8191) # ROL operation
ref_8199 = ref_8195 # MOV operation
ref_8206 = ref_8199 # MOV operation
ref_8255 = ref_8206 # MOV operation
ref_8317 = ref_8255 # MOV operation
ref_9053 = ref_8317 # MOV operation
ref_9259 = ref_9053 # MOV operation
ref_9936 = ref_9259 # MOV operation
ref_10128 = ref_9936 # MOV operation
ref_10172 = ref_10128 # MOV operation
ref_10200 = ref_10172 # MOV operation
ref_10212 = ref_10200 # MOV operation
ref_10214 = ref_10212 # MOV operation

print(ref_10214 & 0xffffffffffffffff)
