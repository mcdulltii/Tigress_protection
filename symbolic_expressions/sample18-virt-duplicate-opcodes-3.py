#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])

ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_6532 = ref_278 # MOV operation
ref_6608 = ref_6532 # MOV operation
ref_6622 = (ref_6608 >> (0xD & 0x3F)) # SHR operation
ref_7460 = ref_278 # MOV operation
ref_7660 = ref_7460 # MOV operation
ref_7668 = ((ref_7660 << (0x33 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_7675 = ref_7668 # MOV operation
ref_7779 = ref_6622 # MOV operation
ref_7783 = ref_7675 # MOV operation
ref_7785 = (ref_7783 | ref_7779) # OR operation
ref_7886 = ref_7785 # MOV operation
ref_7900 = ((0x2EA4A1C39AF5800 + ref_7886) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_8010 = ref_7900 # MOV operation
ref_9750 = ref_8010 # MOV operation
ref_10563 = ref_278 # MOV operation
ref_10639 = ref_10563 # MOV operation
ref_10651 = ref_9750 # MOV operation
ref_10653 = ((ref_10639 - ref_10651) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_10661 = ref_10653 # MOV operation
ref_10765 = ref_10661 # MOV operation
ref_11714 = ref_278 # MOV operation
ref_11790 = ref_11714 # MOV operation
ref_11804 = ((ref_11790 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_12758 = ref_278 # MOV operation
ref_12834 = ref_12758 # MOV operation
ref_12848 = (ref_12834 >> (0x37 & 0x3F)) # SHR operation
ref_12957 = ref_11804 # MOV operation
ref_12961 = ref_12848 # MOV operation
ref_12963 = (ref_12961 | ref_12957) # OR operation
ref_13894 = ref_12963 # MOV operation
ref_14843 = ref_278 # MOV operation
ref_14919 = ref_14843 # MOV operation
ref_14933 = (0x3E908497 | ref_14919) # OR operation
ref_15864 = ref_14933 # MOV operation
ref_16982 = ref_10765 # MOV operation
ref_17182 = ref_16982 # MOV operation
ref_17190 = (ref_17182 >> (0x2 & 0x3F)) # SHR operation
ref_17197 = ref_17190 # MOV operation
ref_17417 = ref_17197 # MOV operation
ref_17423 = (0xF & ref_17417) # AND operation
ref_17524 = ref_17423 # MOV operation
ref_17538 = (0x1 | ref_17524) # OR operation
ref_18461 = ref_8010 # MOV operation
ref_18537 = ref_18461 # MOV operation
ref_18549 = ref_17538 # MOV operation
ref_18551 = (ref_18537 >> ((ref_18549 & 0xFF) & 0x3F)) # SHR operation
ref_19474 = ref_8010 # MOV operation
ref_20488 = ref_10765 # MOV operation
ref_20564 = ref_20488 # MOV operation
ref_20578 = (ref_20564 >> (0x2 & 0x3F)) # SHR operation
ref_20803 = ref_20578 # MOV operation
ref_20809 = (0xF & ref_20803) # AND operation
ref_21034 = ref_20809 # MOV operation
ref_21040 = (0x1 | ref_21034) # OR operation
ref_21269 = ref_21040 # MOV operation
ref_21271 = ((0x40 - ref_21269) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_21279 = ref_21271 # MOV operation
ref_21383 = ref_19474 # MOV operation
ref_21387 = ref_21279 # MOV operation
ref_21389 = (ref_21387 & 0xFFFFFFFF) # MOV operation
ref_21391 = ((ref_21383 << ((ref_21389 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_21398 = ref_21391 # MOV operation
ref_21502 = ref_18551 # MOV operation
ref_21506 = ref_21398 # MOV operation
ref_21508 = (ref_21506 | ref_21502) # OR operation
ref_22431 = ref_15864 # MOV operation
ref_23329 = ref_13894 # MOV operation
ref_23405 = ref_23329 # MOV operation
ref_23417 = ref_22431 # MOV operation
ref_23419 = ((ref_23405 - ref_23417) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_23427 = ref_23419 # MOV operation
ref_23531 = ref_21508 # MOV operation
ref_23535 = ref_23427 # MOV operation
ref_23537 = ((ref_23531 - ref_23535) & 0xFFFFFFFFFFFFFFFF) # CMP operation
ref_23539 = ((((ref_23531 ^ (ref_23535 ^ ref_23537)) ^ ((ref_23531 ^ ref_23537) & (ref_23531 ^ ref_23535))) >> 63) & 0x1) # Carry flag
ref_23545 = ((((ref_23535 >> 8) & 0xFFFFFFFFFFFFFF)) << 8 | (0x1 if (ref_23539 == 0x1) else 0x0)) # SETB operation
ref_23547 = (ref_23545 & 0xFF) # MOVZX operation
ref_23635 = (ref_23547 & 0xFFFFFFFF) # MOV operation
ref_23637 = ((ref_23635 & 0xFFFFFFFF) & (ref_23635 & 0xFFFFFFFF)) # TEST operation
ref_23642 = (0x1 if (ref_23637 == 0x0) else 0x0) # Zero flag
ref_23644 = (0x1B71 if (ref_23642 == 0x1) else 0x1B53) # Program Counter


if (ref_23642 == 0x1):
    ref_50822 = SymVar_0
    ref_50837 = ref_50822 # MOV operation
    ref_57096 = ref_50837 # MOV operation
    ref_57172 = ref_57096 # MOV operation
    ref_57186 = (ref_57172 >> (0xD & 0x3F)) # SHR operation
    ref_58024 = ref_50837 # MOV operation
    ref_58224 = ref_58024 # MOV operation
    ref_58232 = ((ref_58224 << (0x33 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_58239 = ref_58232 # MOV operation
    ref_58343 = ref_57186 # MOV operation
    ref_58347 = ref_58239 # MOV operation
    ref_58349 = (ref_58347 | ref_58343) # OR operation
    ref_58450 = ref_58349 # MOV operation
    ref_58464 = ((0x2EA4A1C39AF5800 + ref_58450) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_58574 = ref_58464 # MOV operation
    ref_60314 = ref_58574 # MOV operation
    ref_61127 = ref_50837 # MOV operation
    ref_61203 = ref_61127 # MOV operation
    ref_61215 = ref_60314 # MOV operation
    ref_61217 = ((ref_61203 - ref_61215) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_61225 = ref_61217 # MOV operation
    ref_61329 = ref_61225 # MOV operation
    ref_62278 = ref_50837 # MOV operation
    ref_62354 = ref_62278 # MOV operation
    ref_62368 = ((ref_62354 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_63322 = ref_50837 # MOV operation
    ref_63398 = ref_63322 # MOV operation
    ref_63412 = (ref_63398 >> (0x37 & 0x3F)) # SHR operation
    ref_63521 = ref_62368 # MOV operation
    ref_63525 = ref_63412 # MOV operation
    ref_63527 = (ref_63525 | ref_63521) # OR operation
    ref_64458 = ref_63527 # MOV operation
    ref_65407 = ref_50837 # MOV operation
    ref_65483 = ref_65407 # MOV operation
    ref_65497 = (0x3E908497 | ref_65483) # OR operation
    ref_66428 = ref_65497 # MOV operation
    ref_76197 = ref_64458 # MOV operation
    ref_77095 = ref_66428 # MOV operation
    ref_77179 = ref_76197 # MOV operation
    ref_77183 = ref_77095 # MOV operation
    ref_77185 = (ref_77183 | ref_77179) # OR operation
    ref_77410 = ref_77185 # MOV operation
    ref_77418 = (ref_77410 >> (0x4 & 0x3F)) # SHR operation
    ref_77425 = ref_77418 # MOV operation
    ref_77521 = ref_77425 # MOV operation
    ref_77535 = (0x7 & ref_77521) # AND operation
    ref_77636 = ref_77535 # MOV operation
    ref_77650 = (0x1 | ref_77636) # OR operation
    ref_78573 = ref_61329 # MOV operation
    ref_78773 = ref_78573 # MOV operation
    ref_78781 = (ref_78773 >> (0x4 & 0x3F)) # SHR operation
    ref_78788 = ref_78781 # MOV operation
    ref_79008 = ref_78788 # MOV operation
    ref_79014 = (0xF & ref_79008) # AND operation
    ref_79239 = ref_79014 # MOV operation
    ref_79245 = (0x1 | ref_79239) # OR operation
    ref_80168 = ref_58574 # MOV operation
    ref_80244 = ref_80168 # MOV operation
    ref_80256 = ref_79245 # MOV operation
    ref_80258 = ((ref_80244 << ((ref_80256 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_81181 = ref_58574 # MOV operation
    ref_82195 = ref_61329 # MOV operation
    ref_82395 = ref_82195 # MOV operation
    ref_82403 = (ref_82395 >> (0x4 & 0x3F)) # SHR operation
    ref_82410 = ref_82403 # MOV operation
    ref_82630 = ref_82410 # MOV operation
    ref_82636 = (0xF & ref_82630) # AND operation
    ref_82737 = ref_82636 # MOV operation
    ref_82751 = (0x1 | ref_82737) # OR operation
    ref_82980 = ref_82751 # MOV operation
    ref_82982 = ((0x40 - ref_82980) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_82990 = ref_82982 # MOV operation
    ref_83094 = ref_81181 # MOV operation
    ref_83098 = ref_82990 # MOV operation
    ref_83100 = (ref_83098 & 0xFFFFFFFF) # MOV operation
    ref_83102 = (ref_83094 >> ((ref_83100 & 0xFF) & 0x3F)) # SHR operation
    ref_83109 = ref_83102 # MOV operation
    ref_83213 = ref_80258 # MOV operation
    ref_83217 = ref_83109 # MOV operation
    ref_83219 = (ref_83217 | ref_83213) # OR operation
    ref_83320 = ref_83219 # MOV operation
    ref_83332 = ref_77650 # MOV operation
    ref_83334 = (ref_83320 >> ((ref_83332 & 0xFF) & 0x3F)) # SHR operation
    ref_83443 = ref_83334 # MOV operation
    ref_83654 = ref_83443 # MOV operation
    ref_83656 = ref_83654 # MOV operation
    endb = ref_83656


else:
    ref_263 = SymVar_0
    ref_278 = ref_263 # MOV operation
    ref_6532 = ref_278 # MOV operation
    ref_6608 = ref_6532 # MOV operation
    ref_6622 = (ref_6608 >> (0xD & 0x3F)) # SHR operation
    ref_7460 = ref_278 # MOV operation
    ref_7660 = ref_7460 # MOV operation
    ref_7668 = ((ref_7660 << (0x33 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_7675 = ref_7668 # MOV operation
    ref_7779 = ref_6622 # MOV operation
    ref_7783 = ref_7675 # MOV operation
    ref_7785 = (ref_7783 | ref_7779) # OR operation
    ref_7886 = ref_7785 # MOV operation
    ref_7900 = ((0x2EA4A1C39AF5800 + ref_7886) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_8010 = ref_7900 # MOV operation
    ref_9750 = ref_8010 # MOV operation
    ref_10563 = ref_278 # MOV operation
    ref_10639 = ref_10563 # MOV operation
    ref_10651 = ref_9750 # MOV operation
    ref_10653 = ((ref_10639 - ref_10651) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_10661 = ref_10653 # MOV operation
    ref_10765 = ref_10661 # MOV operation
    ref_10767 = ((ref_10765 >> 56) & 0xFF) # Byte reference - MOV operation
    ref_10768 = ((ref_10765 >> 48) & 0xFF) # Byte reference - MOV operation
    ref_10769 = ((ref_10765 >> 40) & 0xFF) # Byte reference - MOV operation
    ref_10770 = ((ref_10765 >> 32) & 0xFF) # Byte reference - MOV operation
    ref_10771 = ((ref_10765 >> 24) & 0xFF) # Byte reference - MOV operation
    ref_10772 = ((ref_10765 >> 16) & 0xFF) # Byte reference - MOV operation
    ref_10773 = ((ref_10765 >> 8) & 0xFF) # Byte reference - MOV operation
    ref_10774 = (ref_10765 & 0xFF) # Byte reference - MOV operation
    ref_11714 = ref_278 # MOV operation
    ref_11790 = ref_11714 # MOV operation
    ref_11804 = ((ref_11790 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_12758 = ref_278 # MOV operation
    ref_12834 = ref_12758 # MOV operation
    ref_12848 = (ref_12834 >> (0x37 & 0x3F)) # SHR operation
    ref_12957 = ref_11804 # MOV operation
    ref_12961 = ref_12848 # MOV operation
    ref_12963 = (ref_12961 | ref_12957) # OR operation
    ref_13894 = ref_12963 # MOV operation
    ref_14843 = ref_278 # MOV operation
    ref_14919 = ref_14843 # MOV operation
    ref_14933 = (0x3E908497 | ref_14919) # OR operation
    ref_15864 = ref_14933 # MOV operation
    ref_25312 = ((((ref_10767) << 8 | ref_10768) << 8 | ref_10769) << 8 | ref_10770) # MOV operation
    ref_25392 = (ref_25312 & 0xFFFFFFFF) # MOV operation
    ref_28340 = ((((ref_10771) << 8 | ref_10772) << 8 | ref_10773) << 8 | ref_10774) # MOV operation
    ref_28420 = (ref_28340 & 0xFFFFFFFF) # MOV operation
    ref_28422 = (((ref_28420 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
    ref_28423 = (((ref_28420 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
    ref_28424 = (((ref_28420 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
    ref_28425 = ((ref_28420 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
    ref_30068 = (ref_25392 & 0xFFFFFFFF) # MOV operation
    ref_30148 = (ref_30068 & 0xFFFFFFFF) # MOV operation
    ref_30150 = (((ref_30148 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
    ref_30151 = (((ref_30148 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
    ref_30152 = (((ref_30148 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
    ref_30153 = ((ref_30148 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
    ref_31062 = ref_8010 # MOV operation
    ref_31960 = ref_8010 # MOV operation
    ref_32160 = ref_31960 # MOV operation
    ref_32166 = (0x3F & ref_32160) # AND operation
    ref_32391 = ref_32166 # MOV operation
    ref_32399 = ((ref_32391 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_32406 = ref_32399 # MOV operation
    ref_32510 = ref_31062 # MOV operation
    ref_32514 = ref_32406 # MOV operation
    ref_32516 = (ref_32514 | ref_32510) # OR operation
    ref_33447 = ref_32516 # MOV operation
    ref_35187 = ref_15864 # MOV operation
    ref_36317 = ref_33447 # MOV operation
    ref_36393 = ref_36317 # MOV operation
    ref_36407 = (0x1F & ref_36393) # AND operation
    ref_36508 = ref_36407 # MOV operation
    ref_36522 = ((ref_36508 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_36631 = ref_35187 # MOV operation
    ref_36635 = ref_36522 # MOV operation
    ref_36637 = (ref_36635 | ref_36631) # OR operation
    ref_36746 = ref_36637 # MOV operation
    ref_38602 = ref_13894 # MOV operation
    ref_39500 = ref_33447 # MOV operation
    ref_39576 = ref_39500 # MOV operation
    ref_39588 = ref_38602 # MOV operation
    ref_39590 = ((ref_39588 + ref_39576) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_39692 = ref_39590 # MOV operation
    ref_39706 = (0x1F & ref_39692) # AND operation
    ref_39931 = ref_39706 # MOV operation
    ref_39939 = ((ref_39931 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_39946 = ref_39939 # MOV operation
    ref_40864 = ref_33447 # MOV operation
    ref_40940 = ref_40864 # MOV operation
    ref_40952 = ref_39946 # MOV operation
    ref_40954 = (ref_40952 | ref_40940) # OR operation
    ref_41063 = ref_40954 # MOV operation
    ref_43043 = ref_13894 # MOV operation
    ref_43941 = ref_36746 # MOV operation
    ref_44025 = ref_43043 # MOV operation
    ref_44029 = ref_43941 # MOV operation
    ref_44031 = (ref_44029 | ref_44025) # OR operation
    ref_44256 = ref_44031 # MOV operation
    ref_44264 = (ref_44256 >> (0x4 & 0x3F)) # SHR operation
    ref_44271 = ref_44264 # MOV operation
    ref_44367 = ref_44271 # MOV operation
    ref_44381 = (0x7 & ref_44367) # AND operation
    ref_44482 = ref_44381 # MOV operation
    ref_44496 = (0x1 | ref_44482) # OR operation
    ref_45419 = ((((((((ref_28422) << 8 | ref_28423) << 8 | ref_28424) << 8 | ref_28425) << 8 | ref_30150) << 8 | ref_30151) << 8 | ref_30152) << 8 | ref_30153) # MOV operation
    ref_45619 = ref_45419 # MOV operation
    ref_45627 = (ref_45619 >> (0x4 & 0x3F)) # SHR operation
    ref_45634 = ref_45627 # MOV operation
    ref_45854 = ref_45634 # MOV operation
    ref_45860 = (0xF & ref_45854) # AND operation
    ref_46085 = ref_45860 # MOV operation
    ref_46091 = (0x1 | ref_46085) # OR operation
    ref_47014 = ref_41063 # MOV operation
    ref_47090 = ref_47014 # MOV operation
    ref_47102 = ref_46091 # MOV operation
    ref_47104 = ((ref_47090 << ((ref_47102 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_48027 = ref_41063 # MOV operation
    ref_49041 = ((((((((ref_28422) << 8 | ref_28423) << 8 | ref_28424) << 8 | ref_28425) << 8 | ref_30150) << 8 | ref_30151) << 8 | ref_30152) << 8 | ref_30153) # MOV operation
    ref_49241 = ref_49041 # MOV operation
    ref_49249 = (ref_49241 >> (0x4 & 0x3F)) # SHR operation
    ref_49256 = ref_49249 # MOV operation
    ref_49476 = ref_49256 # MOV operation
    ref_49482 = (0xF & ref_49476) # AND operation
    ref_49583 = ref_49482 # MOV operation
    ref_49597 = (0x1 | ref_49583) # OR operation
    ref_49826 = ref_49597 # MOV operation
    ref_49828 = ((0x40 - ref_49826) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_49836 = ref_49828 # MOV operation
    ref_49940 = ref_48027 # MOV operation
    ref_49944 = ref_49836 # MOV operation
    ref_49946 = (ref_49944 & 0xFFFFFFFF) # MOV operation
    ref_49948 = (ref_49940 >> ((ref_49946 & 0xFF) & 0x3F)) # SHR operation
    ref_49955 = ref_49948 # MOV operation
    ref_50059 = ref_47104 # MOV operation
    ref_50063 = ref_49955 # MOV operation
    ref_50065 = (ref_50063 | ref_50059) # OR operation
    ref_50166 = ref_50065 # MOV operation
    ref_50178 = ref_44496 # MOV operation
    ref_50180 = (ref_50166 >> ((ref_50178 & 0xFF) & 0x3F)) # SHR operation
    ref_50289 = ref_50180 # MOV operation
    ref_50500 = ref_50289 # MOV operation
    ref_50502 = ref_50500 # MOV operation
    endb = ref_50502


print(endb & 0xffffffffffffffff)
