#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_668919 = ref_278 # MOV operation
ref_757483 = ref_668919 # MOV operation
ref_757491 = ((ref_757483 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_757498 = ref_757491 # MOV operation
ref_1111760 = ref_278 # MOV operation
ref_1200279 = ref_1111760 # MOV operation
ref_1200287 = (ref_1200279 >> (0x7 & 0x3F)) # SHR operation
ref_1200294 = ref_1200287 # MOV operation
ref_1244563 = ref_1200294 # MOV operation
ref_1244575 = ref_757498 # MOV operation
ref_1244577 = (ref_1244575 | ref_1244563) # OR operation
ref_1288841 = ref_1244577 # MOV operation
ref_1997429 = ref_1288841 # MOV operation
ref_2085988 = ref_1997429 # MOV operation
ref_2085990 = ((ref_2085988 + 0x2D4AF89B) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_2130259 = ref_2085990 # MOV operation
ref_2130261 = (ref_2130259 & 0x1D5ABF66) # AND operation
ref_2484528 = ref_278 # MOV operation
ref_2573092 = ref_2484528 # MOV operation
ref_2573100 = ((ref_2573092 << (0x35 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_2573107 = ref_2573100 # MOV operation
ref_2927369 = ref_278 # MOV operation
ref_3015888 = ref_2927369 # MOV operation
ref_3015896 = (ref_3015888 >> (0xB & 0x3F)) # SHR operation
ref_3015903 = ref_3015896 # MOV operation
ref_3060172 = ref_3015903 # MOV operation
ref_3060184 = ref_2573107 # MOV operation
ref_3060186 = (ref_3060184 | ref_3060172) # OR operation
ref_3104460 = ref_3060186 # MOV operation
ref_3104472 = ref_2130261 # MOV operation
ref_3104474 = ((ref_3104460 - ref_3104472) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_3104482 = ref_3104474 # MOV operation
ref_3148741 = ref_3104482 # MOV operation
ref_3857307 = ref_278 # MOV operation
ref_3901556 = ref_3857307 # MOV operation
ref_3901570 = ((ref_3901556 - 0xE8D4346) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_3901578 = ref_3901570 # MOV operation
ref_3945837 = ref_3901578 # MOV operation
ref_4654425 = ref_1288841 # MOV operation
ref_4698674 = ref_4654425 # MOV operation
ref_4698688 = ((0x20453EE3 + ref_4698674) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_5052956 = ref_278 # MOV operation
ref_5097205 = ref_5052956 # MOV operation
ref_5097217 = ref_4698688 # MOV operation
ref_5097219 = ((ref_5097205 - ref_5097217) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_5097227 = ref_5097219 # MOV operation
ref_5141486 = ref_5097227 # MOV operation
ref_6292813 = ref_1288841 # MOV operation
ref_6779934 = ref_3945837 # MOV operation
ref_6824183 = ref_6779934 # MOV operation
ref_6824195 = ref_6292813 # MOV operation
ref_6824197 = (ref_6824195 | ref_6824183) # OR operation
ref_6912759 = ref_6824197 # MOV operation
ref_6912765 = (0x3F & ref_6912759) # AND operation
ref_7001354 = ref_6912765 # MOV operation
ref_7001362 = ((ref_7001354 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_7001369 = ref_7001362 # MOV operation
ref_7399923 = ref_1288841 # MOV operation
ref_7444172 = ref_7399923 # MOV operation
ref_7444184 = ref_7001369 # MOV operation
ref_7444186 = (ref_7444184 | ref_7444172) # OR operation
ref_7488450 = ref_7444186 # MOV operation
ref_8285597 = ref_3148741 # MOV operation
ref_8728429 = ref_7488450 # MOV operation
ref_8816948 = ref_8728429 # MOV operation
ref_8816956 = (ref_8816948 >> (0x1 & 0x3F)) # SHR operation
ref_8816963 = ref_8816956 # MOV operation
ref_8905520 = ref_8816963 # MOV operation
ref_8905526 = (0xF & ref_8905520) # AND operation
ref_8949800 = ref_8905526 # MOV operation
ref_8949814 = (0x1 | ref_8949800) # OR operation
ref_9038398 = ref_8949814 # MOV operation
ref_9038400 = ((0x40 - ref_9038398) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_9038408 = ref_9038400 # MOV operation
ref_9082694 = ref_8285597 # MOV operation
ref_9082698 = ref_9038408 # MOV operation
ref_9082700 = (ref_9082698 & 0xFFFFFFFF) # MOV operation
ref_9082702 = ((ref_9082694 << ((ref_9082700 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_9082709 = ref_9082702 # MOV operation
ref_9436993 = ref_3148741 # MOV operation
ref_9879825 = ref_7488450 # MOV operation
ref_9968344 = ref_9879825 # MOV operation
ref_9968352 = (ref_9968344 >> (0x1 & 0x3F)) # SHR operation
ref_9968359 = ref_9968352 # MOV operation
ref_10056916 = ref_9968359 # MOV operation
ref_10056922 = (0xF & ref_10056916) # AND operation
ref_10101196 = ref_10056922 # MOV operation
ref_10101210 = (0x1 | ref_10101196) # OR operation
ref_10145456 = ref_9436993 # MOV operation
ref_10145460 = ref_10101210 # MOV operation
ref_10145462 = (ref_10145460 & 0xFFFFFFFF) # MOV operation
ref_10145464 = (ref_10145456 >> ((ref_10145462 & 0xFF) & 0x3F)) # SHR operation
ref_10145471 = ref_10145464 # MOV operation
ref_10189740 = ref_10145471 # MOV operation
ref_10189752 = ref_9082709 # MOV operation
ref_10189754 = (ref_10189752 | ref_10189740) # OR operation
ref_10234018 = ref_10189754 # MOV operation
ref_10898308 = ref_5141486 # MOV operation
ref_11385429 = ref_10234018 # MOV operation
ref_11429678 = ref_11385429 # MOV operation
ref_11429690 = ref_10898308 # MOV operation
ref_11429692 = ((ref_11429678 - ref_11429690) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_11429700 = ref_11429692 # MOV operation
ref_11473959 = ref_11429700 # MOV operation
ref_12757989 = ref_7488450 # MOV operation
ref_13156551 = ref_3148741 # MOV operation
ref_13245088 = ref_13156551 # MOV operation
ref_13245094 = (0xF & ref_13245088) # AND operation
ref_13289368 = ref_13245094 # MOV operation
ref_13289382 = (0x1 | ref_13289368) # OR operation
ref_13377966 = ref_13289382 # MOV operation
ref_13377968 = ((0x40 - ref_13377966) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_13377976 = ref_13377968 # MOV operation
ref_13422262 = ref_12757989 # MOV operation
ref_13422266 = ref_13377976 # MOV operation
ref_13422268 = (ref_13422266 & 0xFFFFFFFF) # MOV operation
ref_13422270 = ((ref_13422262 << ((ref_13422268 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_13422277 = ref_13422270 # MOV operation
ref_13776561 = ref_7488450 # MOV operation
ref_14175123 = ref_3148741 # MOV operation
ref_14263660 = ref_14175123 # MOV operation
ref_14263666 = (0xF & ref_14263660) # AND operation
ref_14307940 = ref_14263666 # MOV operation
ref_14307954 = (0x1 | ref_14307940) # OR operation
ref_14352200 = ref_13776561 # MOV operation
ref_14352204 = ref_14307954 # MOV operation
ref_14352206 = (ref_14352204 & 0xFFFFFFFF) # MOV operation
ref_14352208 = (ref_14352200 >> ((ref_14352206 & 0xFF) & 0x3F)) # SHR operation
ref_14352215 = ref_14352208 # MOV operation
ref_14396484 = ref_14352215 # MOV operation
ref_14396496 = ref_13422277 # MOV operation
ref_14396498 = (ref_14396496 | ref_14396484) # OR operation
ref_14795085 = ref_5141486 # MOV operation
ref_15149349 = ref_11473959 # MOV operation
ref_15193598 = ref_15149349 # MOV operation
ref_15193610 = ref_14795085 # MOV operation
ref_15193612 = (ref_15193610 | ref_15193598) # OR operation
ref_15282156 = ref_15193612 # MOV operation
ref_15282164 = (ref_15282156 >> (0x1 & 0x3F)) # SHR operation
ref_15282171 = ref_15282164 # MOV operation
ref_15370728 = ref_15282171 # MOV operation
ref_15370734 = (0x7 & ref_15370728) # AND operation
ref_15415008 = ref_15370734 # MOV operation
ref_15415022 = (0x1 | ref_15415008) # OR operation
ref_15459313 = ref_14396498 # MOV operation
ref_15459317 = ref_15415022 # MOV operation
ref_15459319 = (ref_15459317 & 0xFFFFFFFF) # MOV operation
ref_15459321 = ((ref_15459313 << ((ref_15459319 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_15459328 = ref_15459321 # MOV operation
ref_15503587 = ref_15459328 # MOV operation
ref_15592099 = ref_15503587 # MOV operation
ref_15592101 = ref_15592099 # MOV operation

print(ref_15592101 & 0xffffffffffffffff)
