#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_41076 = ref_278 # MOV operation
ref_45912 = ref_41076 # MOV operation
ref_45918 = (0x1F02C962 | ref_45912) # OR operation
ref_50779 = ref_45918 # MOV operation
ref_50785 = (0x1F8797B2 & ref_50779) # AND operation
ref_53212 = ref_50785 # MOV operation
ref_89637 = ref_278 # MOV operation
ref_109079 = ref_53212 # MOV operation
ref_111481 = ref_89637 # MOV operation
ref_111485 = ref_109079 # MOV operation
ref_111487 = (ref_111485 & ref_111481) # AND operation
ref_113914 = ref_111487 # MOV operation
ref_150339 = ref_278 # MOV operation
ref_155175 = ref_150339 # MOV operation
ref_155181 = (((sx(0x40, 0x66AF1DF) * sx(0x40, ref_155175)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_177079 = ref_113914 # MOV operation
ref_179473 = ref_177079 # MOV operation
ref_179487 = (ref_179473 >> (0x7 & 0x3F)) # SHR operation
ref_201388 = ref_113914 # MOV operation
ref_203782 = ref_201388 # MOV operation
ref_203796 = ((ref_203782 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_206223 = ref_179487 # MOV operation
ref_206227 = ref_203796 # MOV operation
ref_206229 = (ref_206227 | ref_206223) # OR operation
ref_208656 = ref_155181 # MOV operation
ref_208660 = ref_206229 # MOV operation
ref_208662 = ((ref_208660 + ref_208656) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_211090 = ref_208662 # MOV operation
ref_415160 = ref_211090 # MOV operation
ref_441876 = ref_211090 # MOV operation
ref_444278 = ref_415160 # MOV operation
ref_444282 = ref_441876 # MOV operation
ref_444284 = ((ref_444282 + ref_444278) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_446712 = ref_444284 # MOV operation
ref_497770 = ref_211090 # MOV operation
ref_522052 = ref_113914 # MOV operation
ref_526888 = ref_522052 # MOV operation
ref_526894 = (0x7 & ref_526888) # AND operation
ref_529313 = ref_526894 # MOV operation
ref_529327 = ((ref_529313 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_531754 = ref_497770 # MOV operation
ref_531758 = ref_529327 # MOV operation
ref_531760 = (ref_531758 | ref_531754) # OR operation
ref_534187 = ref_531760 # MOV operation
ref_534189 = ((ref_534187 >> 56) & 0xFF) # Byte reference - MOV operation
ref_534190 = ((ref_534187 >> 48) & 0xFF) # Byte reference - MOV operation
ref_534191 = ((ref_534187 >> 40) & 0xFF) # Byte reference - MOV operation
ref_534192 = ((ref_534187 >> 32) & 0xFF) # Byte reference - MOV operation
ref_534193 = ((ref_534187 >> 24) & 0xFF) # Byte reference - MOV operation
ref_534194 = ((ref_534187 >> 16) & 0xFF) # Byte reference - MOV operation
ref_534195 = ((ref_534187 >> 8) & 0xFF) # Byte reference - MOV operation
ref_534196 = (ref_534187 & 0xFF) # Byte reference - MOV operation
ref_577883 = ref_534189 # MOVZX operation
ref_580277 = (ref_577883 & 0xFF) # MOVZX operation
ref_660355 = ref_534196 # MOVZX operation
ref_662749 = (ref_660355 & 0xFF) # MOVZX operation
ref_662751 = (ref_662749 & 0xFF) # Byte reference - MOV operation
ref_706437 = (ref_580277 & 0xFF) # MOVZX operation
ref_708831 = (ref_706437 & 0xFF) # MOVZX operation
ref_708833 = (ref_708831 & 0xFF) # Byte reference - MOV operation
ref_745333 = ref_53212 # MOV operation
ref_774483 = ((((((((ref_662751) << 8 | ref_534190) << 8 | ref_534191) << 8 | ref_534192) << 8 | ref_534193) << 8 | ref_534194) << 8 | ref_534195) << 8 | ref_708833) # MOV operation
ref_796331 = ref_113914 # MOV operation
ref_798733 = ref_774483 # MOV operation
ref_798737 = ref_796331 # MOV operation
ref_798739 = (ref_798737 & ref_798733) # AND operation
ref_803600 = ref_798739 # MOV operation
ref_803606 = (0x1F & ref_803600) # AND operation
ref_806025 = ref_803606 # MOV operation
ref_806039 = ((ref_806025 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_808466 = ref_745333 # MOV operation
ref_808470 = ref_806039 # MOV operation
ref_808472 = (ref_808470 | ref_808466) # OR operation
ref_810899 = ref_808472 # MOV operation
ref_883804 = ref_446712 # MOV operation
ref_910520 = ref_446712 # MOV operation
ref_912922 = ref_883804 # MOV operation
ref_912926 = ref_910520 # MOV operation
ref_912928 = ((ref_912926 + ref_912922) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_915356 = ref_912928 # MOV operation
ref_966414 = ref_915356 # MOV operation
ref_990696 = ((((((((ref_662751) << 8 | ref_534190) << 8 | ref_534191) << 8 | ref_534192) << 8 | ref_534193) << 8 | ref_534194) << 8 | ref_534195) << 8 | ref_708833) # MOV operation
ref_995532 = ref_990696 # MOV operation
ref_995538 = (0x7 & ref_995532) # AND operation
ref_997957 = ref_995538 # MOV operation
ref_997971 = ((ref_997957 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_1000398 = ref_966414 # MOV operation
ref_1000402 = ref_997971 # MOV operation
ref_1000404 = (ref_1000402 | ref_1000398) # OR operation
ref_1002831 = ref_1000404 # MOV operation
ref_1002833 = ((ref_1002831 >> 56) & 0xFF) # Byte reference - MOV operation
ref_1002834 = ((ref_1002831 >> 48) & 0xFF) # Byte reference - MOV operation
ref_1002835 = ((ref_1002831 >> 40) & 0xFF) # Byte reference - MOV operation
ref_1002836 = ((ref_1002831 >> 32) & 0xFF) # Byte reference - MOV operation
ref_1002837 = ((ref_1002831 >> 24) & 0xFF) # Byte reference - MOV operation
ref_1002838 = ((ref_1002831 >> 16) & 0xFF) # Byte reference - MOV operation
ref_1002839 = ((ref_1002831 >> 8) & 0xFF) # Byte reference - MOV operation
ref_1002840 = (ref_1002831 & 0xFF) # Byte reference - MOV operation
ref_1046527 = ref_1002833 # MOVZX operation
ref_1048921 = (ref_1046527 & 0xFF) # MOVZX operation
ref_1128999 = ref_1002840 # MOVZX operation
ref_1131393 = (ref_1128999 & 0xFF) # MOVZX operation
ref_1131395 = (ref_1131393 & 0xFF) # Byte reference - MOV operation
ref_1175081 = (ref_1048921 & 0xFF) # MOVZX operation
ref_1177475 = (ref_1175081 & 0xFF) # MOVZX operation
ref_1177477 = (ref_1177475 & 0xFF) # Byte reference - MOV operation
ref_1213977 = ref_810899 # MOV operation
ref_1243127 = ((((((((ref_1131395) << 8 | ref_1002834) << 8 | ref_1002835) << 8 | ref_1002836) << 8 | ref_1002837) << 8 | ref_1002838) << 8 | ref_1002839) << 8 | ref_1177477) # MOV operation
ref_1264975 = ((((((((ref_662751) << 8 | ref_534190) << 8 | ref_534191) << 8 | ref_534192) << 8 | ref_534193) << 8 | ref_534194) << 8 | ref_534195) << 8 | ref_708833) # MOV operation
ref_1267377 = ref_1243127 # MOV operation
ref_1267381 = ref_1264975 # MOV operation
ref_1267383 = (ref_1267381 & ref_1267377) # AND operation
ref_1272244 = ref_1267383 # MOV operation
ref_1272250 = (0x1F & ref_1272244) # AND operation
ref_1274669 = ref_1272250 # MOV operation
ref_1274683 = ((ref_1274669 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_1277110 = ref_1213977 # MOV operation
ref_1277114 = ref_1274683 # MOV operation
ref_1277116 = (ref_1277114 | ref_1277110) # OR operation
ref_1279543 = ref_1277116 # MOV operation
ref_1349895 = ((((((((ref_662751) << 8 | ref_534190) << 8 | ref_534191) << 8 | ref_534192) << 8 | ref_534193) << 8 | ref_534194) << 8 | ref_534195) << 8 | ref_708833) # MOV operation
ref_1369337 = ((((((((ref_1131395) << 8 | ref_1002834) << 8 | ref_1002835) << 8 | ref_1002836) << 8 | ref_1002837) << 8 | ref_1002838) << 8 | ref_1002839) << 8 | ref_1177477) # MOV operation
ref_1371739 = ref_1349895 # MOV operation
ref_1371743 = ref_1369337 # MOV operation
ref_1371745 = (ref_1371743 | ref_1371739) # OR operation
ref_1376606 = ref_1371745 # MOV operation
ref_1376612 = (0xF & ref_1376606) # AND operation
ref_1381473 = ref_1376612 # MOV operation
ref_1381479 = (0x1 | ref_1381473) # OR operation
ref_1403380 = ref_113914 # MOV operation
ref_1405774 = ref_1403380 # MOV operation
ref_1405788 = (ref_1405774 >> (0x1 & 0x3F)) # SHR operation
ref_1410649 = ref_1405788 # MOV operation
ref_1410655 = (0xF & ref_1410649) # AND operation
ref_1415516 = ref_1410655 # MOV operation
ref_1415522 = (0x1 | ref_1415516) # OR operation
ref_1434989 = ref_1279543 # MOV operation
ref_1437383 = ref_1434989 # MOV operation
ref_1437395 = ref_1415522 # MOV operation
ref_1437397 = (ref_1437383 >> ((ref_1437395 & 0xFF) & 0x3F)) # SHR operation
ref_1459298 = ref_113914 # MOV operation
ref_1461692 = ref_1459298 # MOV operation
ref_1461706 = (ref_1461692 >> (0x1 & 0x3F)) # SHR operation
ref_1466567 = ref_1461706 # MOV operation
ref_1466573 = (0xF & ref_1466567) # AND operation
ref_1471434 = ref_1466573 # MOV operation
ref_1471440 = (0x1 | ref_1471434) # OR operation
ref_1476305 = ref_1471440 # MOV operation
ref_1476307 = ((0x40 - ref_1476305) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_1476315 = ref_1476307 # MOV operation
ref_1495777 = ref_1279543 # MOV operation
ref_1498171 = ref_1495777 # MOV operation
ref_1498183 = ref_1476315 # MOV operation
ref_1498185 = ((ref_1498171 << ((ref_1498183 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_1500612 = ref_1437397 # MOV operation
ref_1500616 = ref_1498185 # MOV operation
ref_1500618 = (ref_1500616 | ref_1500612) # OR operation
ref_1503037 = ref_1500618 # MOV operation
ref_1503049 = ref_1381479 # MOV operation
ref_1503051 = ((ref_1503037 << ((ref_1503049 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_1522518 = ((((((((ref_662751) << 8 | ref_534190) << 8 | ref_534191) << 8 | ref_534192) << 8 | ref_534193) << 8 | ref_534194) << 8 | ref_534195) << 8 | ref_708833) # MOV operation
ref_1541960 = ((((((((ref_1131395) << 8 | ref_1002834) << 8 | ref_1002835) << 8 | ref_1002836) << 8 | ref_1002837) << 8 | ref_1002838) << 8 | ref_1002839) << 8 | ref_1177477) # MOV operation
ref_1544362 = ref_1522518 # MOV operation
ref_1544366 = ref_1541960 # MOV operation
ref_1544368 = (ref_1544366 | ref_1544362) # OR operation
ref_1549229 = ref_1544368 # MOV operation
ref_1549235 = (0xF & ref_1549229) # AND operation
ref_1554096 = ref_1549235 # MOV operation
ref_1554102 = (0x1 | ref_1554096) # OR operation
ref_1558967 = ref_1554102 # MOV operation
ref_1558969 = ((0x40 - ref_1558967) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_1558977 = ref_1558969 # MOV operation
ref_1580873 = ref_113914 # MOV operation
ref_1583267 = ref_1580873 # MOV operation
ref_1583281 = (ref_1583267 >> (0x1 & 0x3F)) # SHR operation
ref_1588142 = ref_1583281 # MOV operation
ref_1588148 = (0xF & ref_1588142) # AND operation
ref_1593009 = ref_1588148 # MOV operation
ref_1593015 = (0x1 | ref_1593009) # OR operation
ref_1612482 = ref_1279543 # MOV operation
ref_1614876 = ref_1612482 # MOV operation
ref_1614888 = ref_1593015 # MOV operation
ref_1614890 = (ref_1614876 >> ((ref_1614888 & 0xFF) & 0x3F)) # SHR operation
ref_1636791 = ref_113914 # MOV operation
ref_1639185 = ref_1636791 # MOV operation
ref_1639199 = (ref_1639185 >> (0x1 & 0x3F)) # SHR operation
ref_1644060 = ref_1639199 # MOV operation
ref_1644066 = (0xF & ref_1644060) # AND operation
ref_1648927 = ref_1644066 # MOV operation
ref_1648933 = (0x1 | ref_1648927) # OR operation
ref_1653798 = ref_1648933 # MOV operation
ref_1653800 = ((0x40 - ref_1653798) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_1653808 = ref_1653800 # MOV operation
ref_1673270 = ref_1279543 # MOV operation
ref_1675664 = ref_1673270 # MOV operation
ref_1675676 = ref_1653808 # MOV operation
ref_1675678 = ((ref_1675664 << ((ref_1675676 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_1678105 = ref_1614890 # MOV operation
ref_1678109 = ref_1675678 # MOV operation
ref_1678111 = (ref_1678109 | ref_1678105) # OR operation
ref_1680530 = ref_1678111 # MOV operation
ref_1680542 = ref_1558977 # MOV operation
ref_1680544 = (ref_1680530 >> ((ref_1680542 & 0xFF) & 0x3F)) # SHR operation
ref_1682971 = ref_1503051 # MOV operation
ref_1682975 = ref_1680544 # MOV operation
ref_1682977 = (ref_1682975 | ref_1682971) # OR operation
ref_1685404 = ref_1682977 # MOV operation
ref_1690251 = ref_1685404 # MOV operation
ref_1690253 = ref_1690251 # MOV operation

print(ref_1690253 & 0xffffffffffffffff)
