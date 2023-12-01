#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_46545 = ref_278 # MOV operation
ref_52073 = ref_46545 # MOV operation
ref_52079 = ((0x3F22161B + ref_52073) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_54880 = ref_52079 # MOV operation
ref_105190 = ref_54880 # MOV operation
ref_107951 = ref_105190 # MOV operation
ref_107953 = (((sx(0x40, ref_107951) * sx(0x40, 0x378AED0A)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_110736 = ref_107953 # MOV operation
ref_110738 = (((sx(0x40, ref_110736) * sx(0x40, 0xDF2B78B)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_116306 = ref_110738 # MOV operation
ref_116314 = (ref_116306 >> (0x1 & 0x3F)) # SHR operation
ref_116321 = ref_116314 # MOV operation
ref_119117 = ref_116321 # MOV operation
ref_119131 = (0xF & ref_119117) # AND operation
ref_124729 = ref_119131 # MOV operation
ref_124735 = (0x1 | ref_124729) # OR operation
ref_149845 = ref_278 # MOV operation
ref_152621 = ref_149845 # MOV operation
ref_152635 = ((ref_152621 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_174956 = ref_278 # MOV operation
ref_180502 = ref_174956 # MOV operation
ref_180510 = (ref_180502 >> (0x39 & 0x3F)) # SHR operation
ref_180517 = ref_180510 # MOV operation
ref_183321 = ref_152635 # MOV operation
ref_183325 = ref_180517 # MOV operation
ref_183327 = (ref_183325 | ref_183321) # OR operation
ref_186128 = ref_183327 # MOV operation
ref_186140 = ref_124735 # MOV operation
ref_186142 = ((ref_186128 << ((ref_186140 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_211252 = ref_278 # MOV operation
ref_214028 = ref_211252 # MOV operation
ref_214042 = ((ref_214028 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_236363 = ref_278 # MOV operation
ref_241909 = ref_236363 # MOV operation
ref_241917 = (ref_241909 >> (0x39 & 0x3F)) # SHR operation
ref_241924 = ref_241917 # MOV operation
ref_244728 = ref_214042 # MOV operation
ref_244732 = ref_241924 # MOV operation
ref_244734 = (ref_244732 | ref_244728) # OR operation
ref_275471 = ref_54880 # MOV operation
ref_278232 = ref_275471 # MOV operation
ref_278234 = (((sx(0x40, ref_278232) * sx(0x40, 0x378AED0A)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_281017 = ref_278234 # MOV operation
ref_281019 = (((sx(0x40, ref_281017) * sx(0x40, 0xDF2B78B)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_286587 = ref_281019 # MOV operation
ref_286595 = (ref_286587 >> (0x1 & 0x3F)) # SHR operation
ref_286602 = ref_286595 # MOV operation
ref_289398 = ref_286602 # MOV operation
ref_289412 = (0xF & ref_289398) # AND operation
ref_295010 = ref_289412 # MOV operation
ref_295016 = (0x1 | ref_295010) # OR operation
ref_300609 = ref_295016 # MOV operation
ref_300611 = ((0x40 - ref_300609) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_300619 = ref_300611 # MOV operation
ref_303396 = ref_244734 # MOV operation
ref_303400 = ref_300619 # MOV operation
ref_303402 = (ref_303400 & 0xFFFFFFFF) # MOV operation
ref_303404 = (ref_303396 >> ((ref_303402 & 0xFF) & 0x3F)) # SHR operation
ref_303411 = ref_303404 # MOV operation
ref_306215 = ref_186142 # MOV operation
ref_306219 = ref_303411 # MOV operation
ref_306221 = (ref_306219 | ref_306215) # OR operation
ref_309021 = ref_306221 # MOV operation
ref_350915 = ref_278 # MOV operation
ref_373260 = ref_309021 # MOV operation
ref_378788 = ref_373260 # MOV operation
ref_378794 = ((0xAD6EED + ref_378788) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_381559 = ref_350915 # MOV operation
ref_381563 = ref_378794 # MOV operation
ref_381565 = ((ref_381563 + ref_381559) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_384366 = ref_381565 # MOV operation
ref_426260 = ref_278 # MOV operation
ref_448605 = ref_54880 # MOV operation
ref_451389 = ref_426260 # MOV operation
ref_451393 = ref_448605 # MOV operation
ref_451395 = (ref_451393 | ref_451389) # OR operation
ref_473765 = ref_309021 # MOV operation
ref_479293 = ref_473765 # MOV operation
ref_479299 = ((0x2B6B05ED + ref_479293) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_501670 = ref_384366 # MOV operation
ref_504446 = ref_501670 # MOV operation
ref_504458 = ref_479299 # MOV operation
ref_504460 = (ref_504458 & ref_504446) # AND operation
ref_507224 = ref_451395 # MOV operation
ref_507228 = ref_504460 # MOV operation
ref_507230 = ((ref_507228 + ref_507224) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_510031 = ref_507230 # MOV operation
ref_551974 = ref_510031 # MOV operation
ref_579897 = ref_384366 # MOV operation
ref_582673 = ref_579897 # MOV operation
ref_582687 = (0x3F & ref_582673) # AND operation
ref_585488 = ref_582687 # MOV operation
ref_585502 = ((ref_585488 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_588311 = ref_551974 # MOV operation
ref_588315 = ref_585502 # MOV operation
ref_588317 = (ref_588315 | ref_588311) # OR operation
ref_591117 = ref_588317 # MOV operation
ref_635809 = ref_309021 # MOV operation
ref_641355 = ref_635809 # MOV operation
ref_641363 = (ref_641355 >> (0x4 & 0x3F)) # SHR operation
ref_641370 = ref_641363 # MOV operation
ref_644166 = ref_641370 # MOV operation
ref_644180 = (0xF & ref_644166) # AND operation
ref_649778 = ref_644180 # MOV operation
ref_649784 = (0x1 | ref_649778) # OR operation
ref_672154 = ref_54880 # MOV operation
ref_674930 = ref_672154 # MOV operation
ref_674942 = ref_649784 # MOV operation
ref_674944 = ((ref_674930 << ((ref_674942 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_697314 = ref_54880 # MOV operation
ref_722448 = ref_309021 # MOV operation
ref_727994 = ref_722448 # MOV operation
ref_728002 = (ref_727994 >> (0x4 & 0x3F)) # SHR operation
ref_728009 = ref_728002 # MOV operation
ref_730805 = ref_728009 # MOV operation
ref_730819 = (0xF & ref_730805) # AND operation
ref_736417 = ref_730819 # MOV operation
ref_736423 = (0x1 | ref_736417) # OR operation
ref_742016 = ref_736423 # MOV operation
ref_742018 = ((0x40 - ref_742016) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_742026 = ref_742018 # MOV operation
ref_744803 = ref_697314 # MOV operation
ref_744807 = ref_742026 # MOV operation
ref_744809 = (ref_744807 & 0xFFFFFFFF) # MOV operation
ref_744811 = (ref_744803 >> ((ref_744809 & 0xFF) & 0x3F)) # SHR operation
ref_744818 = ref_744811 # MOV operation
ref_747622 = ref_674944 # MOV operation
ref_747626 = ref_744818 # MOV operation
ref_747628 = (ref_747626 | ref_747622) # OR operation
ref_769998 = ref_384366 # MOV operation
ref_792343 = ref_591117 # MOV operation
ref_795082 = ref_769998 # MOV operation
ref_795086 = ref_792343 # MOV operation
ref_795088 = ((ref_795086 + ref_795082) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_797871 = ref_747628 # MOV operation
ref_797875 = ref_795088 # MOV operation
ref_797877 = (((sx(0x40, ref_797875) * sx(0x40, ref_797871)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_800674 = ref_797877 # MOV operation
ref_806195 = ref_800674 # MOV operation
ref_806197 = ref_806195 # MOV operation

print(ref_806197 & 0xffffffffffffffff)
