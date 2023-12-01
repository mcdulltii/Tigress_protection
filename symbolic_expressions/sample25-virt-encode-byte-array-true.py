#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_72346 = ref_278 # MOV operation
ref_72422 = ref_72346 # MOV operation
ref_72436 = ((ref_72422 << (0xD & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_73390 = ref_278 # MOV operation
ref_73466 = ref_73390 # MOV operation
ref_73480 = (ref_73466 >> (0x33 & 0x3F)) # SHR operation
ref_73589 = ref_72436 # MOV operation
ref_73593 = ref_73480 # MOV operation
ref_73595 = (ref_73593 | ref_73589) # OR operation
ref_73704 = ref_73595 # MOV operation
ref_75475 = ref_278 # MOV operation
ref_75551 = ref_75475 # MOV operation
ref_75567 = ((((0x0) << 64 | ref_75551) / 0x6) & 0xFFFFFFFFFFFFFFFF) # DIV operation
ref_75788 = ref_75567 # MOV operation
ref_75794 = (((sx(0x40, 0xFA0000000002C90C) * sx(0x40, ref_75788)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_75900 = ref_75794 # MOV operation
ref_77640 = ref_73704 # MOV operation
ref_78538 = ref_75900 # MOV operation
ref_78622 = ref_77640 # MOV operation
ref_78626 = ref_78538 # MOV operation
ref_78628 = (ref_78626 | ref_78622) # OR operation
ref_79466 = ref_278 # MOV operation
ref_79542 = ref_79466 # MOV operation
ref_79554 = ref_78628 # MOV operation
ref_79556 = ((ref_79554 + ref_79542) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_79666 = ref_79556 # MOV operation
ref_81638 = ref_73704 # MOV operation
ref_81838 = ref_81638 # MOV operation
ref_81844 = ((ref_81838 - 0x2ED5CD7E) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_81852 = ref_81844 # MOV operation
ref_81960 = ref_81852 # MOV operation
ref_81962 = ((0x28E5FC28 - ref_81960) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_81970 = ref_81962 # MOV operation
ref_82066 = ref_81970 # MOV operation
ref_82080 = (ref_82066 >> (0x2 & 0x3F)) # SHR operation
ref_82305 = ref_82080 # MOV operation
ref_82311 = (0x7 & ref_82305) # AND operation
ref_82536 = ref_82311 # MOV operation
ref_82542 = (0x1 | ref_82536) # OR operation
ref_83465 = ref_75900 # MOV operation
ref_84278 = ref_278 # MOV operation
ref_84354 = ref_84278 # MOV operation
ref_84366 = ref_83465 # MOV operation
ref_84368 = ((ref_84366 + ref_84354) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_84470 = ref_84368 # MOV operation
ref_84482 = ref_82542 # MOV operation
ref_84484 = (ref_84470 >> ((ref_84482 & 0xFF) & 0x3F)) # SHR operation
ref_84593 = ref_84484 # MOV operation
ref_86449 = ref_84593 # MOV operation
ref_86525 = ref_86449 # MOV operation
ref_86539 = (ref_86525 >> (0x1 & 0x3F)) # SHR operation
ref_86764 = ref_86539 # MOV operation
ref_86770 = (0x7 & ref_86764) # AND operation
ref_86995 = ref_86770 # MOV operation
ref_87001 = (0x1 | ref_86995) # OR operation
ref_87924 = ref_84593 # MOV operation
ref_88000 = ref_87924 # MOV operation
ref_88012 = ref_87001 # MOV operation
ref_88014 = (ref_88000 >> ((ref_88012 & 0xFF) & 0x3F)) # SHR operation
ref_88123 = ref_88014 # MOV operation
ref_88125 = ((ref_88123 >> 56) & 0xFF) # Byte reference - MOV operation
ref_88126 = ((ref_88123 >> 48) & 0xFF) # Byte reference - MOV operation
ref_88127 = ((ref_88123 >> 40) & 0xFF) # Byte reference - MOV operation
ref_88128 = ((ref_88123 >> 32) & 0xFF) # Byte reference - MOV operation
ref_88129 = ((ref_88123 >> 24) & 0xFF) # Byte reference - MOV operation
ref_88130 = ((ref_88123 >> 16) & 0xFF) # Byte reference - MOV operation
ref_88131 = ((ref_88123 >> 8) & 0xFF) # Byte reference - MOV operation
ref_88132 = (ref_88123 & 0xFF) # Byte reference - MOV operation
ref_90848 = ref_79666 # MOV operation
ref_91950 = ref_73704 # MOV operation
ref_92150 = ref_91950 # MOV operation
ref_92156 = (0x7 & ref_92150) # AND operation
ref_92257 = ref_92156 # MOV operation
ref_92271 = ((ref_92257 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_92380 = ref_90848 # MOV operation
ref_92384 = ref_92271 # MOV operation
ref_92386 = (ref_92384 | ref_92380) # OR operation
ref_92495 = ref_92386 # MOV operation
ref_94147 = ((((ref_88125) << 8 | ref_88126) << 8 | ref_88127) << 8 | ref_88128) # MOV operation
ref_94227 = (ref_94147 & 0xFFFFFFFF) # MOV operation
ref_97175 = ((((ref_88129) << 8 | ref_88130) << 8 | ref_88131) << 8 | ref_88132) # MOV operation
ref_97255 = (ref_97175 & 0xFFFFFFFF) # MOV operation
ref_98903 = (ref_94227 & 0xFFFFFFFF) # MOV operation
ref_98983 = (ref_98903 & 0xFFFFFFFF) # MOV operation
ref_102024 = ref_92495 # MOV operation
ref_103126 = ref_92495 # MOV operation
ref_103326 = ref_103126 # MOV operation
ref_103332 = (0x7 & ref_103326) # AND operation
ref_103433 = ref_103332 # MOV operation
ref_103447 = ((ref_103433 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_103556 = ref_102024 # MOV operation
ref_103560 = ref_103447 # MOV operation
ref_103562 = (ref_103560 | ref_103556) # OR operation
ref_103671 = ref_103562 # MOV operation
ref_105323 = (ref_97255 & 0xFFFFFFFF) # MOV operation
ref_105403 = (ref_105323 & 0xFFFFFFFF) # MOV operation
ref_108351 = (ref_98983 & 0xFFFFFFFF) # MOV operation
ref_108431 = (ref_108351 & 0xFFFFFFFF) # MOV operation
ref_108433 = (((ref_108431 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_108434 = (((ref_108431 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_108435 = (((ref_108431 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_108436 = ((ref_108431 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_110079 = (ref_105403 & 0xFFFFFFFF) # MOV operation
ref_110159 = (ref_110079 & 0xFFFFFFFF) # MOV operation
ref_110161 = (((ref_110159 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_110162 = (((ref_110159 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_110163 = (((ref_110159 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_110164 = ((ref_110159 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_113285 = ref_103671 # MOV operation
ref_114183 = ((((((((ref_108433) << 8 | ref_108434) << 8 | ref_108435) << 8 | ref_108436) << 8 | ref_110161) << 8 | ref_110162) << 8 | ref_110163) << 8 | ref_110164) # MOV operation
ref_114383 = ref_114183 # MOV operation
ref_114389 = (((sx(0x40, 0x4E1A7F2) * sx(0x40, ref_114383)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_114495 = ref_113285 # MOV operation
ref_114499 = ref_114389 # MOV operation
ref_114501 = (ref_114499 ^ ref_114495) # XOR operation
ref_114726 = ref_114501 # MOV operation
ref_114732 = (0xF & ref_114726) # AND operation
ref_114957 = ref_114732 # MOV operation
ref_114963 = (0x1 | ref_114957) # OR operation
ref_115886 = ref_73704 # MOV operation
ref_116784 = ref_75900 # MOV operation
ref_116868 = ref_115886 # MOV operation
ref_116872 = ref_116784 # MOV operation
ref_116874 = (((sx(0x40, ref_116872) * sx(0x40, ref_116868)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_116972 = ref_116874 # MOV operation
ref_116984 = ref_114963 # MOV operation
ref_116986 = ((ref_116972 << ((ref_116984 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_118025 = ref_103671 # MOV operation
ref_118923 = ((((((((ref_108433) << 8 | ref_108434) << 8 | ref_108435) << 8 | ref_108436) << 8 | ref_110161) << 8 | ref_110162) << 8 | ref_110163) << 8 | ref_110164) # MOV operation
ref_119123 = ref_118923 # MOV operation
ref_119129 = (((sx(0x40, 0x4E1A7F2) * sx(0x40, ref_119123)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_119235 = ref_118025 # MOV operation
ref_119239 = ref_119129 # MOV operation
ref_119241 = (ref_119239 ^ ref_119235) # XOR operation
ref_119466 = ref_119241 # MOV operation
ref_119472 = (0xF & ref_119466) # AND operation
ref_119697 = ref_119472 # MOV operation
ref_119703 = (0x1 | ref_119697) # OR operation
ref_119816 = ref_119703 # MOV operation
ref_119818 = ((0x40 - ref_119816) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_119826 = ref_119818 # MOV operation
ref_120744 = ref_73704 # MOV operation
ref_121642 = ref_75900 # MOV operation
ref_121726 = ref_120744 # MOV operation
ref_121730 = ref_121642 # MOV operation
ref_121732 = (((sx(0x40, ref_121730) * sx(0x40, ref_121726)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_121830 = ref_121732 # MOV operation
ref_121842 = ref_119826 # MOV operation
ref_121844 = (ref_121830 >> ((ref_121842 & 0xFF) & 0x3F)) # SHR operation
ref_121953 = ref_116986 # MOV operation
ref_121957 = ref_121844 # MOV operation
ref_121959 = (ref_121957 | ref_121953) # OR operation
ref_122068 = ref_121959 # MOV operation
ref_122279 = ref_122068 # MOV operation
ref_122281 = ref_122279 # MOV operation

print(ref_122281 & 0xffffffffffffffff)
