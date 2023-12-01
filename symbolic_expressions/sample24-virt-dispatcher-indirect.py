#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])

ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_9430 = ref_278 # MOV operation
ref_9480 = ref_9430 # MOV operation
ref_9494 = ((ref_9480 << (0xB & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_10214 = ref_278 # MOV operation
ref_10264 = ref_10214 # MOV operation
ref_10278 = (ref_10264 >> (0x35 & 0x3F)) # SHR operation
ref_10361 = ref_9494 # MOV operation
ref_10365 = ref_10278 # MOV operation
ref_10367 = (ref_10365 | ref_10361) # OR operation
ref_10442 = ref_10367 # MOV operation
ref_10456 = (ref_10442 >> (0x1 & 0x3F)) # SHR operation
ref_10539 = ref_10456 # MOV operation
ref_11889 = ref_10539 # MOV operation
ref_12037 = ref_11889 # MOV operation
ref_12043 = (((sx(0x40, 0x6B33F46) * sx(0x40, ref_12037)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_12670 = ref_278 # MOV operation
ref_12818 = ref_12670 # MOV operation
ref_12826 = ((((0x0) << 64 | ref_12818) / 0x3) & 0xFFFFFFFFFFFFFFFF) # DIV operation
ref_12897 = ref_12826 # MOV operation
ref_12909 = ref_12043 # MOV operation
ref_12911 = ((ref_12897 - ref_12909) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_12919 = ref_12911 # MOV operation
ref_12997 = ref_12919 # MOV operation
ref_14617 = ref_12997 # MOV operation
ref_14667 = ref_14617 # MOV operation
ref_14681 = (ref_14667 >> (0x7 & 0x3F)) # SHR operation
ref_14756 = ref_14681 # MOV operation
ref_14770 = (ref_14756 >> (0x2 & 0x3F)) # SHR operation
ref_14845 = ref_14770 # MOV operation
ref_14859 = (0x7 & ref_14845) # AND operation
ref_15032 = ref_14859 # MOV operation
ref_15038 = (0x1 | ref_15032) # OR operation
ref_15758 = ref_278 # MOV operation
ref_15808 = ref_15758 # MOV operation
ref_15822 = ((0x9919884 + ref_15808) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_15898 = ref_15822 # MOV operation
ref_15910 = ref_15038 # MOV operation
ref_15912 = (ref_15898 >> ((ref_15910 & 0xFF) & 0x3F)) # SHR operation
ref_15995 = ref_15912 # MOV operation
ref_17350 = ref_278 # MOV operation
ref_17400 = ref_17350 # MOV operation
ref_17414 = ((0x1E5EA08F8 + ref_17400) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_17498 = ref_17414 # MOV operation
ref_20083 = ref_15995 # MOV operation
ref_21195 = ref_15995 # MOV operation
ref_21245 = ref_21195 # MOV operation
ref_21259 = (0x3F & ref_21245) # AND operation
ref_21334 = ref_21259 # MOV operation
ref_21348 = ((ref_21334 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_21431 = ref_20083 # MOV operation
ref_21435 = ref_21348 # MOV operation
ref_21437 = (ref_21435 | ref_21431) # OR operation
ref_21520 = ref_21437 # MOV operation
ref_23973 = ref_21520 # MOV operation
ref_25023 = ref_12997 # MOV operation
ref_25073 = ref_25023 # MOV operation
ref_25087 = (ref_25073 >> (0x2 & 0x3F)) # SHR operation
ref_25162 = ref_25087 # MOV operation
ref_25176 = (0xF & ref_25162) # AND operation
ref_25349 = ref_25176 # MOV operation
ref_25355 = (0x1 | ref_25349) # OR operation
ref_26070 = ref_10539 # MOV operation
ref_26120 = ref_26070 # MOV operation
ref_26132 = ref_25355 # MOV operation
ref_26134 = ((ref_26120 << ((ref_26132 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_27029 = ref_12997 # MOV operation
ref_27079 = ref_27029 # MOV operation
ref_27093 = (ref_27079 >> (0x2 & 0x3F)) # SHR operation
ref_27168 = ref_27093 # MOV operation
ref_27182 = (0xF & ref_27168) # AND operation
ref_27355 = ref_27182 # MOV operation
ref_27361 = (0x1 | ref_27355) # OR operation
ref_27538 = ref_27361 # MOV operation
ref_27540 = ((0x40 - ref_27538) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_27548 = ref_27540 # MOV operation
ref_28258 = ref_10539 # MOV operation
ref_28308 = ref_28258 # MOV operation
ref_28320 = ref_27548 # MOV operation
ref_28322 = (ref_28308 >> ((ref_28320 & 0xFF) & 0x3F)) # SHR operation
ref_28405 = ref_26134 # MOV operation
ref_28409 = ref_28322 # MOV operation
ref_28411 = (ref_28409 | ref_28405) # OR operation
ref_28486 = ref_28411 # MOV operation
ref_28500 = (0x7 & ref_28486) # AND operation
ref_28575 = ref_28500 # MOV operation
ref_28589 = ((ref_28575 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_28672 = ref_23973 # MOV operation
ref_28676 = ref_28589 # MOV operation
ref_28678 = (ref_28676 | ref_28672) # OR operation
ref_28761 = ref_28678 # MOV operation
ref_29709 = ref_17498 # MOV operation
ref_29759 = ref_29709 # MOV operation
ref_29773 = (ref_29759 >> (0x4 & 0x3F)) # SHR operation
ref_29848 = ref_29773 # MOV operation
ref_29862 = (0xF & ref_29848) # AND operation
ref_30035 = ref_29862 # MOV operation
ref_30041 = (0x1 | ref_30035) # OR operation
ref_30756 = ref_28761 # MOV operation
ref_30806 = ref_30756 # MOV operation
ref_30818 = ref_30041 # MOV operation
ref_30820 = (ref_30806 >> ((ref_30818 & 0xFF) & 0x3F)) # SHR operation
ref_31715 = ref_17498 # MOV operation
ref_31765 = ref_31715 # MOV operation
ref_31779 = (ref_31765 >> (0x4 & 0x3F)) # SHR operation
ref_31854 = ref_31779 # MOV operation
ref_31868 = (0xF & ref_31854) # AND operation
ref_32041 = ref_31868 # MOV operation
ref_32047 = (0x1 | ref_32041) # OR operation
ref_32224 = ref_32047 # MOV operation
ref_32226 = ((0x40 - ref_32224) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_32234 = ref_32226 # MOV operation
ref_32944 = ref_28761 # MOV operation
ref_32994 = ref_32944 # MOV operation
ref_33006 = ref_32234 # MOV operation
ref_33008 = ((ref_32994 << ((ref_33006 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_33091 = ref_30820 # MOV operation
ref_33095 = ref_33008 # MOV operation
ref_33097 = (ref_33095 | ref_33091) # OR operation
ref_33992 = ref_12997 # MOV operation
ref_34042 = ref_33992 # MOV operation
ref_34056 = (ref_34042 >> (0x3 & 0x3F)) # SHR operation
ref_34131 = ref_34056 # MOV operation
ref_34145 = (0xF & ref_34131) # AND operation
ref_34318 = ref_34145 # MOV operation
ref_34324 = (0x1 | ref_34318) # OR operation
ref_35039 = ref_10539 # MOV operation
ref_35089 = ref_35039 # MOV operation
ref_35101 = ref_34324 # MOV operation
ref_35103 = (ref_35089 >> ((ref_35101 & 0xFF) & 0x3F)) # SHR operation
ref_35998 = ref_12997 # MOV operation
ref_36048 = ref_35998 # MOV operation
ref_36062 = (ref_36048 >> (0x3 & 0x3F)) # SHR operation
ref_36137 = ref_36062 # MOV operation
ref_36151 = (0xF & ref_36137) # AND operation
ref_36324 = ref_36151 # MOV operation
ref_36330 = (0x1 | ref_36324) # OR operation
ref_36507 = ref_36330 # MOV operation
ref_36509 = ((0x40 - ref_36507) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_36517 = ref_36509 # MOV operation
ref_37227 = ref_10539 # MOV operation
ref_37277 = ref_37227 # MOV operation
ref_37289 = ref_36517 # MOV operation
ref_37291 = ((ref_37277 << ((ref_37289 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_37374 = ref_35103 # MOV operation
ref_37378 = ref_37291 # MOV operation
ref_37380 = (ref_37378 | ref_37374) # OR operation
ref_37455 = ref_37380 # MOV operation
ref_37467 = ref_33097 # MOV operation
ref_37469 = ((ref_37455 - ref_37467) & 0xFFFFFFFFFFFFFFFF) # CMP operation
ref_37471 = ((((ref_37455 ^ (ref_37467 ^ ref_37469)) ^ ((ref_37455 ^ ref_37469) & (ref_37455 ^ ref_37467))) >> 63) & 0x1) # Carry flag
ref_37475 = (0x1 if (ref_37469 == 0x0) else 0x0) # Zero flag
ref_37477 = ((((ref_37467 >> 8) & 0xFFFFFFFFFFFFFF)) << 8 | (0x1 if (((~(ref_37471) & 0x1) & (~(ref_37475) & 0x1)) == 0x1) else 0x0)) # SETA operation
ref_37479 = (ref_37477 & 0xFF) # MOVZX operation
ref_37541 = (ref_37479 & 0xFFFFFFFF) # MOV operation
ref_37543 = ((ref_37541 & 0xFFFFFFFF) & (ref_37541 & 0xFFFFFFFF)) # TEST operation
ref_37548 = (0x1 if (ref_37543 == 0x0) else 0x0) # Zero flag
ref_37550 = (0x2D21 if (ref_37548 == 0x0) else 0x2D1D) # Program Counter


if (ref_37548 == 0x0):
    ref_47689 = SymVar_0
    ref_47704 = ref_47689 # MOV operation
    ref_56861 = ref_47704 # MOV operation
    ref_56911 = ref_56861 # MOV operation
    ref_56925 = ((ref_56911 << (0xB & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_57645 = ref_47704 # MOV operation
    ref_57695 = ref_57645 # MOV operation
    ref_57709 = (ref_57695 >> (0x35 & 0x3F)) # SHR operation
    ref_57792 = ref_56925 # MOV operation
    ref_57796 = ref_57709 # MOV operation
    ref_57798 = (ref_57796 | ref_57792) # OR operation
    ref_57873 = ref_57798 # MOV operation
    ref_57887 = (ref_57873 >> (0x1 & 0x3F)) # SHR operation
    ref_57970 = ref_57887 # MOV operation
    ref_59320 = ref_57970 # MOV operation
    ref_59468 = ref_59320 # MOV operation
    ref_59474 = (((sx(0x40, 0x6B33F46) * sx(0x40, ref_59468)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_60101 = ref_47704 # MOV operation
    ref_60249 = ref_60101 # MOV operation
    ref_60257 = ((((0x0) << 64 | ref_60249) / 0x3) & 0xFFFFFFFFFFFFFFFF) # DIV operation
    ref_60328 = ref_60257 # MOV operation
    ref_60340 = ref_59474 # MOV operation
    ref_60342 = ((ref_60328 - ref_60340) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_60350 = ref_60342 # MOV operation
    ref_60428 = ref_60350 # MOV operation
    ref_62048 = ref_60428 # MOV operation
    ref_62098 = ref_62048 # MOV operation
    ref_62112 = (ref_62098 >> (0x7 & 0x3F)) # SHR operation
    ref_62187 = ref_62112 # MOV operation
    ref_62201 = (ref_62187 >> (0x2 & 0x3F)) # SHR operation
    ref_62276 = ref_62201 # MOV operation
    ref_62290 = (0x7 & ref_62276) # AND operation
    ref_62463 = ref_62290 # MOV operation
    ref_62469 = (0x1 | ref_62463) # OR operation
    ref_63189 = ref_47704 # MOV operation
    ref_63239 = ref_63189 # MOV operation
    ref_63253 = ((0x9919884 + ref_63239) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_63329 = ref_63253 # MOV operation
    ref_63341 = ref_62469 # MOV operation
    ref_63343 = (ref_63329 >> ((ref_63341 & 0xFF) & 0x3F)) # SHR operation
    ref_63426 = ref_63343 # MOV operation
    ref_64781 = ref_47704 # MOV operation
    ref_64831 = ref_64781 # MOV operation
    ref_64845 = ((0x1E5EA08F8 + ref_64831) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_64929 = ref_64845 # MOV operation
    ref_67514 = ref_63426 # MOV operation
    ref_68626 = ref_63426 # MOV operation
    ref_68676 = ref_68626 # MOV operation
    ref_68690 = (0x3F & ref_68676) # AND operation
    ref_68765 = ref_68690 # MOV operation
    ref_68779 = ((ref_68765 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_68862 = ref_67514 # MOV operation
    ref_68866 = ref_68779 # MOV operation
    ref_68868 = (ref_68866 | ref_68862) # OR operation
    ref_68951 = ref_68868 # MOV operation
    ref_71404 = ref_68951 # MOV operation
    ref_72454 = ref_60428 # MOV operation
    ref_72504 = ref_72454 # MOV operation
    ref_72518 = (ref_72504 >> (0x2 & 0x3F)) # SHR operation
    ref_72593 = ref_72518 # MOV operation
    ref_72607 = (0xF & ref_72593) # AND operation
    ref_72780 = ref_72607 # MOV operation
    ref_72786 = (0x1 | ref_72780) # OR operation
    ref_73501 = ref_57970 # MOV operation
    ref_73551 = ref_73501 # MOV operation
    ref_73563 = ref_72786 # MOV operation
    ref_73565 = ((ref_73551 << ((ref_73563 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_74460 = ref_60428 # MOV operation
    ref_74510 = ref_74460 # MOV operation
    ref_74524 = (ref_74510 >> (0x2 & 0x3F)) # SHR operation
    ref_74599 = ref_74524 # MOV operation
    ref_74613 = (0xF & ref_74599) # AND operation
    ref_74786 = ref_74613 # MOV operation
    ref_74792 = (0x1 | ref_74786) # OR operation
    ref_74969 = ref_74792 # MOV operation
    ref_74971 = ((0x40 - ref_74969) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_74979 = ref_74971 # MOV operation
    ref_75689 = ref_57970 # MOV operation
    ref_75739 = ref_75689 # MOV operation
    ref_75751 = ref_74979 # MOV operation
    ref_75753 = (ref_75739 >> ((ref_75751 & 0xFF) & 0x3F)) # SHR operation
    ref_75836 = ref_73565 # MOV operation
    ref_75840 = ref_75753 # MOV operation
    ref_75842 = (ref_75840 | ref_75836) # OR operation
    ref_75917 = ref_75842 # MOV operation
    ref_75931 = (0x7 & ref_75917) # AND operation
    ref_76006 = ref_75931 # MOV operation
    ref_76020 = ((ref_76006 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_76103 = ref_71404 # MOV operation
    ref_76107 = ref_76020 # MOV operation
    ref_76109 = (ref_76107 | ref_76103) # OR operation
    ref_76192 = ref_76109 # MOV operation
    ref_76194 = ((ref_76192 >> 56) & 0xFF) # Byte reference - MOV operation
    ref_76195 = ((ref_76192 >> 48) & 0xFF) # Byte reference - MOV operation
    ref_76196 = ((ref_76192 >> 40) & 0xFF) # Byte reference - MOV operation
    ref_76197 = ((ref_76192 >> 32) & 0xFF) # Byte reference - MOV operation
    ref_76198 = ((ref_76192 >> 24) & 0xFF) # Byte reference - MOV operation
    ref_76199 = ((ref_76192 >> 16) & 0xFF) # Byte reference - MOV operation
    ref_76200 = ((ref_76192 >> 8) & 0xFF) # Byte reference - MOV operation
    ref_76201 = (ref_76192 & 0xFF) # Byte reference - MOV operation
    ref_86527 = ref_64929 # MOV operation
    ref_86577 = ref_86527 # MOV operation
    ref_86591 = (ref_86577 >> (0x3 & 0x3F)) # SHR operation
    ref_86666 = ref_86591 # MOV operation
    ref_86680 = (0xF & ref_86666) # AND operation
    ref_86853 = ref_86680 # MOV operation
    ref_86859 = (0x1 | ref_86853) # OR operation
    ref_87574 = ref_64929 # MOV operation
    ref_87624 = ref_87574 # MOV operation
    ref_87636 = ref_86859 # MOV operation
    ref_87638 = ((ref_87624 << ((ref_87636 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_88533 = ref_64929 # MOV operation
    ref_88583 = ref_88533 # MOV operation
    ref_88597 = (ref_88583 >> (0x3 & 0x3F)) # SHR operation
    ref_88672 = ref_88597 # MOV operation
    ref_88686 = (0xF & ref_88672) # AND operation
    ref_88859 = ref_88686 # MOV operation
    ref_88865 = (0x1 | ref_88859) # OR operation
    ref_89042 = ref_88865 # MOV operation
    ref_89044 = ((0x40 - ref_89042) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_89052 = ref_89044 # MOV operation
    ref_89762 = ref_64929 # MOV operation
    ref_89812 = ref_89762 # MOV operation
    ref_89824 = ref_89052 # MOV operation
    ref_89826 = (ref_89812 >> ((ref_89824 & 0xFF) & 0x3F)) # SHR operation
    ref_89909 = ref_87638 # MOV operation
    ref_89913 = ref_89826 # MOV operation
    ref_89915 = (ref_89913 | ref_89909) # OR operation
    ref_89998 = ref_89915 # MOV operation
    ref_91158 = ref_76200 # MOVZX operation
    ref_91310 = (ref_91158 & 0xFF) # MOVZX operation
    ref_92462 = ref_76198 # MOVZX operation
    ref_93602 = (ref_92462 & 0xFF) # MOVZX operation
    ref_93604 = (ref_93602 & 0xFF) # Byte reference - MOV operation
    ref_93766 = (ref_91310 & 0xFF) # MOVZX operation
    ref_94906 = (ref_93766 & 0xFF) # MOVZX operation
    ref_94908 = (ref_94906 & 0xFF) # Byte reference - MOV operation
    ref_96230 = ref_89998 # MOV operation
    ref_96920 = ref_60428 # MOV operation
    ref_96978 = ref_96230 # MOV operation
    ref_96982 = ref_96920 # MOV operation
    ref_96984 = (ref_96982 | ref_96978) # OR operation
    ref_97699 = ((((((((ref_76194) << 8 | ref_76195) << 8 | ref_76196) << 8 | ref_76197) << 8 | ref_94908) << 8 | ref_76199) << 8 | ref_93604) << 8 | ref_76201) # MOV operation
    ref_98389 = ref_64929 # MOV operation
    ref_98447 = ref_97699 # MOV operation
    ref_98451 = ref_98389 # MOV operation
    ref_98453 = (((sx(0x40, ref_98451) * sx(0x40, ref_98447)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_98533 = ref_96984 # MOV operation
    ref_98537 = ref_98453 # MOV operation
    ref_98539 = (((sx(0x40, ref_98537) * sx(0x40, ref_98533)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_98619 = ref_98539 # MOV operation
    ref_98778 = ref_98619 # MOV operation
    ref_98780 = ref_98778 # MOV operation
    endb = ref_98780


else:
    ref_263 = SymVar_0
    ref_278 = ref_263 # MOV operation
    ref_9430 = ref_278 # MOV operation
    ref_9480 = ref_9430 # MOV operation
    ref_9494 = ((ref_9480 << (0xB & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_10214 = ref_278 # MOV operation
    ref_10264 = ref_10214 # MOV operation
    ref_10278 = (ref_10264 >> (0x35 & 0x3F)) # SHR operation
    ref_10361 = ref_9494 # MOV operation
    ref_10365 = ref_10278 # MOV operation
    ref_10367 = (ref_10365 | ref_10361) # OR operation
    ref_10442 = ref_10367 # MOV operation
    ref_10456 = (ref_10442 >> (0x1 & 0x3F)) # SHR operation
    ref_10539 = ref_10456 # MOV operation
    ref_11889 = ref_10539 # MOV operation
    ref_12037 = ref_11889 # MOV operation
    ref_12043 = (((sx(0x40, 0x6B33F46) * sx(0x40, ref_12037)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_12670 = ref_278 # MOV operation
    ref_12818 = ref_12670 # MOV operation
    ref_12826 = ((((0x0) << 64 | ref_12818) / 0x3) & 0xFFFFFFFFFFFFFFFF) # DIV operation
    ref_12897 = ref_12826 # MOV operation
    ref_12909 = ref_12043 # MOV operation
    ref_12911 = ((ref_12897 - ref_12909) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_12919 = ref_12911 # MOV operation
    ref_12997 = ref_12919 # MOV operation
    ref_14617 = ref_12997 # MOV operation
    ref_14667 = ref_14617 # MOV operation
    ref_14681 = (ref_14667 >> (0x7 & 0x3F)) # SHR operation
    ref_14756 = ref_14681 # MOV operation
    ref_14770 = (ref_14756 >> (0x2 & 0x3F)) # SHR operation
    ref_14845 = ref_14770 # MOV operation
    ref_14859 = (0x7 & ref_14845) # AND operation
    ref_15032 = ref_14859 # MOV operation
    ref_15038 = (0x1 | ref_15032) # OR operation
    ref_15758 = ref_278 # MOV operation
    ref_15808 = ref_15758 # MOV operation
    ref_15822 = ((0x9919884 + ref_15808) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_15898 = ref_15822 # MOV operation
    ref_15910 = ref_15038 # MOV operation
    ref_15912 = (ref_15898 >> ((ref_15910 & 0xFF) & 0x3F)) # SHR operation
    ref_15995 = ref_15912 # MOV operation
    ref_17350 = ref_278 # MOV operation
    ref_17400 = ref_17350 # MOV operation
    ref_17414 = ((0x1E5EA08F8 + ref_17400) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_17498 = ref_17414 # MOV operation
    ref_20083 = ref_15995 # MOV operation
    ref_21195 = ref_15995 # MOV operation
    ref_21245 = ref_21195 # MOV operation
    ref_21259 = (0x3F & ref_21245) # AND operation
    ref_21334 = ref_21259 # MOV operation
    ref_21348 = ((ref_21334 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_21431 = ref_20083 # MOV operation
    ref_21435 = ref_21348 # MOV operation
    ref_21437 = (ref_21435 | ref_21431) # OR operation
    ref_21520 = ref_21437 # MOV operation
    ref_23973 = ref_21520 # MOV operation
    ref_25023 = ref_12997 # MOV operation
    ref_25073 = ref_25023 # MOV operation
    ref_25087 = (ref_25073 >> (0x2 & 0x3F)) # SHR operation
    ref_25162 = ref_25087 # MOV operation
    ref_25176 = (0xF & ref_25162) # AND operation
    ref_25349 = ref_25176 # MOV operation
    ref_25355 = (0x1 | ref_25349) # OR operation
    ref_26070 = ref_10539 # MOV operation
    ref_26120 = ref_26070 # MOV operation
    ref_26132 = ref_25355 # MOV operation
    ref_26134 = ((ref_26120 << ((ref_26132 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_27029 = ref_12997 # MOV operation
    ref_27079 = ref_27029 # MOV operation
    ref_27093 = (ref_27079 >> (0x2 & 0x3F)) # SHR operation
    ref_27168 = ref_27093 # MOV operation
    ref_27182 = (0xF & ref_27168) # AND operation
    ref_27355 = ref_27182 # MOV operation
    ref_27361 = (0x1 | ref_27355) # OR operation
    ref_27538 = ref_27361 # MOV operation
    ref_27540 = ((0x40 - ref_27538) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_27548 = ref_27540 # MOV operation
    ref_28258 = ref_10539 # MOV operation
    ref_28308 = ref_28258 # MOV operation
    ref_28320 = ref_27548 # MOV operation
    ref_28322 = (ref_28308 >> ((ref_28320 & 0xFF) & 0x3F)) # SHR operation
    ref_28405 = ref_26134 # MOV operation
    ref_28409 = ref_28322 # MOV operation
    ref_28411 = (ref_28409 | ref_28405) # OR operation
    ref_28486 = ref_28411 # MOV operation
    ref_28500 = (0x7 & ref_28486) # AND operation
    ref_28575 = ref_28500 # MOV operation
    ref_28589 = ((ref_28575 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_28672 = ref_23973 # MOV operation
    ref_28676 = ref_28589 # MOV operation
    ref_28678 = (ref_28676 | ref_28672) # OR operation
    ref_28761 = ref_28678 # MOV operation
    ref_38968 = ref_12997 # MOV operation
    ref_39838 = ref_12997 # MOV operation
    ref_39888 = ref_39838 # MOV operation
    ref_39902 = (0xF & ref_39888) # AND operation
    ref_39977 = ref_39902 # MOV operation
    ref_39991 = ((ref_39977 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_40074 = ref_38968 # MOV operation
    ref_40078 = ref_39991 # MOV operation
    ref_40080 = (ref_40078 | ref_40074) # OR operation
    ref_40163 = ref_40080 # MOV operation
    ref_41513 = ref_10539 # MOV operation
    ref_42383 = ref_40163 # MOV operation
    ref_43073 = ref_28761 # MOV operation
    ref_43123 = ref_43073 # MOV operation
    ref_43135 = ref_42383 # MOV operation
    ref_43137 = (ref_43135 & ref_43123) # AND operation
    ref_43212 = ref_43137 # MOV operation
    ref_43226 = (0x1F & ref_43212) # AND operation
    ref_43301 = ref_43226 # MOV operation
    ref_43315 = ((ref_43301 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_43398 = ref_41513 # MOV operation
    ref_43402 = ref_43315 # MOV operation
    ref_43404 = (ref_43402 | ref_43398) # OR operation
    ref_43487 = ref_43404 # MOV operation
    ref_44819 = ref_43487 # MOV operation
    ref_45509 = ref_40163 # MOV operation
    ref_45567 = ref_44819 # MOV operation
    ref_45571 = ref_45509 # MOV operation
    ref_45573 = (ref_45571 | ref_45567) # OR operation
    ref_46288 = ref_28761 # MOV operation
    ref_46978 = ref_17498 # MOV operation
    ref_47036 = ref_46288 # MOV operation
    ref_47040 = ref_46978 # MOV operation
    ref_47042 = (((sx(0x40, ref_47040) * sx(0x40, ref_47036)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_47122 = ref_45573 # MOV operation
    ref_47126 = ref_47042 # MOV operation
    ref_47128 = (((sx(0x40, ref_47126) * sx(0x40, ref_47122)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_47208 = ref_47128 # MOV operation
    ref_47367 = ref_47208 # MOV operation
    ref_47369 = ref_47367 # MOV operation
    endb = ref_47369


print(endb & 0xffffffffffffffff)
