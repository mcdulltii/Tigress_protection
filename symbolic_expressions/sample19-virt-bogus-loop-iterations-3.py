#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_58534 = ref_278 # MOV operation
ref_61867 = ref_58534 # MOV operation
ref_61881 = ((ref_61867 - 0x35CEDE6D) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_61889 = ref_61881 # MOV operation
ref_65250 = ref_61889 # MOV operation
ref_115760 = ref_278 # MOV operation
ref_122474 = ref_115760 # MOV operation
ref_122482 = ((((0x0) << 64 | ref_122474) / 0x7) & 0xFFFFFFFFFFFFFFFF) # DIV operation
ref_125844 = ref_122482 # MOV operation
ref_183185 = ref_125844 # MOV operation
ref_186518 = ref_183185 # MOV operation
ref_186532 = (ref_186518 >> (0x3 & 0x3F)) # SHR operation
ref_193271 = ref_186532 # MOV operation
ref_193277 = (0xF & ref_193271) # AND operation
ref_200016 = ref_193277 # MOV operation
ref_200022 = (0x1 | ref_200016) # OR operation
ref_206765 = ref_200022 # MOV operation
ref_206767 = ((0x7A11169 << ((ref_206765 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_237119 = ref_125844 # MOV operation
ref_240452 = ref_237119 # MOV operation
ref_240466 = (ref_240452 >> (0x3 & 0x3F)) # SHR operation
ref_247205 = ref_240466 # MOV operation
ref_247211 = (0xF & ref_247205) # AND operation
ref_253950 = ref_247211 # MOV operation
ref_253956 = (0x1 | ref_253950) # OR operation
ref_260699 = ref_253956 # MOV operation
ref_260701 = ((0x40 - ref_260699) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_260709 = ref_260701 # MOV operation
ref_267447 = ref_260709 # MOV operation
ref_267449 = (0x7A11169 >> ((ref_267447 & 0xFF) & 0x3F)) # SHR operation
ref_270815 = ref_206767 # MOV operation
ref_270819 = ref_267449 # MOV operation
ref_270821 = (ref_270819 | ref_270815) # OR operation
ref_274179 = ref_270821 # MOV operation
ref_274193 = (ref_274179 >> (0x4 & 0x3F)) # SHR operation
ref_280932 = ref_274193 # MOV operation
ref_280938 = (0xF & ref_280932) # AND operation
ref_287677 = ref_280938 # MOV operation
ref_287683 = (0x1 | ref_287677) # OR operation
ref_314577 = ref_278 # MOV operation
ref_317910 = ref_314577 # MOV operation
ref_317922 = ref_287683 # MOV operation
ref_317924 = ((ref_317910 << ((ref_317922 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_351649 = ref_125844 # MOV operation
ref_354982 = ref_351649 # MOV operation
ref_354996 = (ref_354982 >> (0x3 & 0x3F)) # SHR operation
ref_361735 = ref_354996 # MOV operation
ref_361741 = (0xF & ref_361735) # AND operation
ref_368480 = ref_361741 # MOV operation
ref_368486 = (0x1 | ref_368480) # OR operation
ref_375229 = ref_368486 # MOV operation
ref_375231 = ((0x7A11169 << ((ref_375229 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_405583 = ref_125844 # MOV operation
ref_408916 = ref_405583 # MOV operation
ref_408930 = (ref_408916 >> (0x3 & 0x3F)) # SHR operation
ref_415669 = ref_408930 # MOV operation
ref_415675 = (0xF & ref_415669) # AND operation
ref_422414 = ref_415675 # MOV operation
ref_422420 = (0x1 | ref_422414) # OR operation
ref_429163 = ref_422420 # MOV operation
ref_429165 = ((0x40 - ref_429163) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_429173 = ref_429165 # MOV operation
ref_435911 = ref_429173 # MOV operation
ref_435913 = (0x7A11169 >> ((ref_435911 & 0xFF) & 0x3F)) # SHR operation
ref_439279 = ref_375231 # MOV operation
ref_439283 = ref_435913 # MOV operation
ref_439285 = (ref_439283 | ref_439279) # OR operation
ref_442643 = ref_439285 # MOV operation
ref_442657 = (ref_442643 >> (0x4 & 0x3F)) # SHR operation
ref_449396 = ref_442657 # MOV operation
ref_449402 = (0xF & ref_449396) # AND operation
ref_456141 = ref_449402 # MOV operation
ref_456147 = (0x1 | ref_456141) # OR operation
ref_462890 = ref_456147 # MOV operation
ref_462892 = ((0x40 - ref_462890) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_462900 = ref_462892 # MOV operation
ref_489789 = ref_278 # MOV operation
ref_493122 = ref_489789 # MOV operation
ref_493134 = ref_462900 # MOV operation
ref_493136 = (ref_493122 >> ((ref_493134 & 0xFF) & 0x3F)) # SHR operation
ref_496502 = ref_317924 # MOV operation
ref_496506 = ref_493136 # MOV operation
ref_496508 = (ref_496506 | ref_496502) # OR operation
ref_499874 = ref_496508 # MOV operation
ref_553757 = ref_278 # MOV operation
ref_557090 = ref_553757 # MOV operation
ref_557104 = ((ref_557090 - 0x297EE8A1) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_557112 = ref_557104 # MOV operation
ref_563846 = ref_557112 # MOV operation
ref_563852 = (((sx(0x40, 0x1471C5DA) * sx(0x40, ref_563846)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_567215 = ref_563852 # MOV operation
ref_567217 = ((ref_567215 >> 56) & 0xFF) # Byte reference - MOV operation
ref_567218 = ((ref_567215 >> 48) & 0xFF) # Byte reference - MOV operation
ref_567219 = ((ref_567215 >> 40) & 0xFF) # Byte reference - MOV operation
ref_567220 = ((ref_567215 >> 32) & 0xFF) # Byte reference - MOV operation
ref_567221 = ((ref_567215 >> 24) & 0xFF) # Byte reference - MOV operation
ref_567222 = ((ref_567215 >> 16) & 0xFF) # Byte reference - MOV operation
ref_567223 = ((ref_567215 >> 8) & 0xFF) # Byte reference - MOV operation
ref_567224 = (ref_567215 & 0xFF) # Byte reference - MOV operation
ref_614337 = ((ref_567219) << 8 | ref_567220) # MOVZX operation
ref_621057 = (ref_614337 & 0xFFFF) # MOVZX operation
ref_668173 = ((ref_567221) << 8 | ref_567222) # MOVZX operation
ref_715277 = (ref_668173 & 0xFFFF) # MOVZX operation
ref_722009 = (ref_621057 & 0xFFFF) # MOVZX operation
ref_769113 = (ref_722009 & 0xFFFF) # MOVZX operation
ref_769115 = (((ref_769113 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_769116 = ((ref_769113 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_1038727 = ref_125844 # MOV operation
ref_1069054 = ref_499874 # MOV operation
ref_1075768 = ref_1069054 # MOV operation
ref_1075774 = (0x1F & ref_1075768) # AND operation
ref_1079132 = ref_1075774 # MOV operation
ref_1079146 = ((ref_1079132 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_1082512 = ref_1038727 # MOV operation
ref_1082516 = ref_1079146 # MOV operation
ref_1082518 = (ref_1082516 | ref_1082512) # OR operation
ref_1085884 = ref_1082518 # MOV operation
ref_1136479 = ref_1085884 # MOV operation
ref_1166806 = ref_1085884 # MOV operation
ref_1173520 = ref_1166806 # MOV operation
ref_1173526 = (0xF & ref_1173520) # AND operation
ref_1176884 = ref_1173526 # MOV operation
ref_1176898 = ((ref_1176884 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_1180264 = ref_1136479 # MOV operation
ref_1180268 = ref_1176898 # MOV operation
ref_1180270 = (ref_1180268 | ref_1180264) # OR operation
ref_1183636 = ref_1180270 # MOV operation
ref_1234099 = ((ref_567217) << 8 | ref_567218) # MOVZX operation
ref_1240819 = (ref_1234099 & 0xFFFF) # MOVZX operation
ref_1287935 = ((ref_567223) << 8 | ref_567224) # MOVZX operation
ref_1335039 = (ref_1287935 & 0xFFFF) # MOVZX operation
ref_1335041 = (((ref_1335039 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_1335042 = ((ref_1335039 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_1341771 = (ref_1240819 & 0xFFFF) # MOVZX operation
ref_1388875 = (ref_1341771 & 0xFFFF) # MOVZX operation
ref_1435991 = (ref_1388875 & 0xFFFF) # MOVZX operation
ref_1442711 = (ref_1435991 & 0xFFFF) # MOVZX operation
ref_1489827 = (ref_715277 & 0xFFFF) # MOVZX operation
ref_1536931 = (ref_1489827 & 0xFFFF) # MOVZX operation
ref_1536933 = (((ref_1536931 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_1536934 = ((ref_1536931 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_1543663 = (ref_1442711 & 0xFFFF) # MOVZX operation
ref_1590767 = (ref_1543663 & 0xFFFF) # MOVZX operation
ref_1590769 = (((ref_1590767 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_1590770 = ((ref_1590767 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_1648026 = ((((((((ref_1335041) << 8 | ref_1335042) << 8 | ref_1590769) << 8 | ref_1590770) << 8 | ref_769115) << 8 | ref_769116) << 8 | ref_1536933) << 8 | ref_1536934) # MOV operation
ref_1651359 = ref_1648026 # MOV operation
ref_1651373 = (ref_1651359 >> (0x2 & 0x3F)) # SHR operation
ref_1658112 = ref_1651373 # MOV operation
ref_1658118 = (0xF & ref_1658112) # AND operation
ref_1664857 = ref_1658118 # MOV operation
ref_1664863 = (0x1 | ref_1664857) # OR operation
ref_1691842 = ref_499874 # MOV operation
ref_1695175 = ref_1691842 # MOV operation
ref_1695187 = ref_1664863 # MOV operation
ref_1695189 = ((ref_1695175 << ((ref_1695187 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_1725541 = ((((((((ref_1335041) << 8 | ref_1335042) << 8 | ref_1590769) << 8 | ref_1590770) << 8 | ref_769115) << 8 | ref_769116) << 8 | ref_1536933) << 8 | ref_1536934) # MOV operation
ref_1728874 = ref_1725541 # MOV operation
ref_1728888 = (ref_1728874 >> (0x2 & 0x3F)) # SHR operation
ref_1735627 = ref_1728888 # MOV operation
ref_1735633 = (0xF & ref_1735627) # AND operation
ref_1742372 = ref_1735633 # MOV operation
ref_1742378 = (0x1 | ref_1742372) # OR operation
ref_1749121 = ref_1742378 # MOV operation
ref_1749123 = ((0x40 - ref_1749121) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_1749131 = ref_1749123 # MOV operation
ref_1776105 = ref_499874 # MOV operation
ref_1779438 = ref_1776105 # MOV operation
ref_1779450 = ref_1749131 # MOV operation
ref_1779452 = (ref_1779438 >> ((ref_1779450 & 0xFF) & 0x3F)) # SHR operation
ref_1782818 = ref_1695189 # MOV operation
ref_1782822 = ref_1779452 # MOV operation
ref_1782824 = (ref_1782822 | ref_1782818) # OR operation
ref_1786182 = ref_1782824 # MOV operation
ref_1786196 = (ref_1786182 >> (0x4 & 0x3F)) # SHR operation
ref_1792935 = ref_1786196 # MOV operation
ref_1792941 = (0xF & ref_1792935) # AND operation
ref_1799680 = ref_1792941 # MOV operation
ref_1799686 = (0x1 | ref_1799680) # OR operation
ref_1826665 = ref_1183636 # MOV operation
ref_1833379 = ref_1826665 # MOV operation
ref_1833385 = (0xF & ref_1833379) # AND operation
ref_1840124 = ref_1833385 # MOV operation
ref_1840130 = (0x1 | ref_1840124) # OR operation
ref_1867109 = ref_65250 # MOV operation
ref_1870442 = ref_1867109 # MOV operation
ref_1870454 = ref_1840130 # MOV operation
ref_1870456 = ((ref_1870442 << ((ref_1870454 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_1897435 = ref_1183636 # MOV operation
ref_1904149 = ref_1897435 # MOV operation
ref_1904155 = (0xF & ref_1904149) # AND operation
ref_1910894 = ref_1904155 # MOV operation
ref_1910900 = (0x1 | ref_1910894) # OR operation
ref_1917643 = ref_1910900 # MOV operation
ref_1917645 = ((0x40 - ref_1917643) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_1917653 = ref_1917645 # MOV operation
ref_1944627 = ref_65250 # MOV operation
ref_1947960 = ref_1944627 # MOV operation
ref_1947972 = ref_1917653 # MOV operation
ref_1947974 = (ref_1947960 >> ((ref_1947972 & 0xFF) & 0x3F)) # SHR operation
ref_1951340 = ref_1870456 # MOV operation
ref_1951344 = ref_1947974 # MOV operation
ref_1951346 = (ref_1951344 | ref_1951340) # OR operation
ref_1954704 = ref_1951346 # MOV operation
ref_1954716 = ref_1799686 # MOV operation
ref_1954718 = (ref_1954704 >> ((ref_1954716 & 0xFF) & 0x3F)) # SHR operation
ref_1988443 = ((((((((ref_1335041) << 8 | ref_1335042) << 8 | ref_1590769) << 8 | ref_1590770) << 8 | ref_769115) << 8 | ref_769116) << 8 | ref_1536933) << 8 | ref_1536934) # MOV operation
ref_1991776 = ref_1988443 # MOV operation
ref_1991790 = (ref_1991776 >> (0x2 & 0x3F)) # SHR operation
ref_1998529 = ref_1991790 # MOV operation
ref_1998535 = (0xF & ref_1998529) # AND operation
ref_2005274 = ref_1998535 # MOV operation
ref_2005280 = (0x1 | ref_2005274) # OR operation
ref_2032259 = ref_499874 # MOV operation
ref_2035592 = ref_2032259 # MOV operation
ref_2035604 = ref_2005280 # MOV operation
ref_2035606 = ((ref_2035592 << ((ref_2035604 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_2065958 = ((((((((ref_1335041) << 8 | ref_1335042) << 8 | ref_1590769) << 8 | ref_1590770) << 8 | ref_769115) << 8 | ref_769116) << 8 | ref_1536933) << 8 | ref_1536934) # MOV operation
ref_2069291 = ref_2065958 # MOV operation
ref_2069305 = (ref_2069291 >> (0x2 & 0x3F)) # SHR operation
ref_2076044 = ref_2069305 # MOV operation
ref_2076050 = (0xF & ref_2076044) # AND operation
ref_2082789 = ref_2076050 # MOV operation
ref_2082795 = (0x1 | ref_2082789) # OR operation
ref_2089538 = ref_2082795 # MOV operation
ref_2089540 = ((0x40 - ref_2089538) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_2089548 = ref_2089540 # MOV operation
ref_2116522 = ref_499874 # MOV operation
ref_2119855 = ref_2116522 # MOV operation
ref_2119867 = ref_2089548 # MOV operation
ref_2119869 = (ref_2119855 >> ((ref_2119867 & 0xFF) & 0x3F)) # SHR operation
ref_2123235 = ref_2035606 # MOV operation
ref_2123239 = ref_2119869 # MOV operation
ref_2123241 = (ref_2123239 | ref_2123235) # OR operation
ref_2126599 = ref_2123241 # MOV operation
ref_2126613 = (ref_2126599 >> (0x4 & 0x3F)) # SHR operation
ref_2133352 = ref_2126613 # MOV operation
ref_2133358 = (0xF & ref_2133352) # AND operation
ref_2140097 = ref_2133358 # MOV operation
ref_2140103 = (0x1 | ref_2140097) # OR operation
ref_2146846 = ref_2140103 # MOV operation
ref_2146848 = ((0x40 - ref_2146846) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_2146856 = ref_2146848 # MOV operation
ref_2173830 = ref_1183636 # MOV operation
ref_2180544 = ref_2173830 # MOV operation
ref_2180550 = (0xF & ref_2180544) # AND operation
ref_2187289 = ref_2180550 # MOV operation
ref_2187295 = (0x1 | ref_2187289) # OR operation
ref_2214274 = ref_65250 # MOV operation
ref_2217607 = ref_2214274 # MOV operation
ref_2217619 = ref_2187295 # MOV operation
ref_2217621 = ((ref_2217607 << ((ref_2217619 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_2244600 = ref_1183636 # MOV operation
ref_2251314 = ref_2244600 # MOV operation
ref_2251320 = (0xF & ref_2251314) # AND operation
ref_2258059 = ref_2251320 # MOV operation
ref_2258065 = (0x1 | ref_2258059) # OR operation
ref_2264808 = ref_2258065 # MOV operation
ref_2264810 = ((0x40 - ref_2264808) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_2264818 = ref_2264810 # MOV operation
ref_2291792 = ref_65250 # MOV operation
ref_2295125 = ref_2291792 # MOV operation
ref_2295137 = ref_2264818 # MOV operation
ref_2295139 = (ref_2295125 >> ((ref_2295137 & 0xFF) & 0x3F)) # SHR operation
ref_2298505 = ref_2217621 # MOV operation
ref_2298509 = ref_2295139 # MOV operation
ref_2298511 = (ref_2298509 | ref_2298505) # OR operation
ref_2301869 = ref_2298511 # MOV operation
ref_2301881 = ref_2146856 # MOV operation
ref_2301883 = ((ref_2301869 << ((ref_2301881 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_2305249 = ref_1954718 # MOV operation
ref_2305253 = ref_2301883 # MOV operation
ref_2305255 = (ref_2305253 | ref_2305249) # OR operation
ref_2308621 = ref_2305255 # MOV operation
ref_2315346 = ref_2308621 # MOV operation
ref_2315348 = ref_2315346 # MOV operation

print(ref_2315348 & 0xffffffffffffffff)
