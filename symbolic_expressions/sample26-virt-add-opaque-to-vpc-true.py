#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_7367 = ref_278 # MOV operation
ref_7690 = ref_7367 # MOV operation
ref_7698 = (ref_7690 >> (0x5 & 0x3F)) # SHR operation
ref_7705 = ref_7698 # MOV operation
ref_7860 = ref_7705 # MOV operation
ref_7874 = (0x1376783EF7559EA & ref_7860) # AND operation
ref_8047 = ref_7874 # MOV operation
ref_8049 = ((ref_8047 >> 56) & 0xFF) # Byte reference - MOV operation
ref_8050 = ((ref_8047 >> 48) & 0xFF) # Byte reference - MOV operation
ref_8051 = ((ref_8047 >> 40) & 0xFF) # Byte reference - MOV operation
ref_8052 = ((ref_8047 >> 32) & 0xFF) # Byte reference - MOV operation
ref_8053 = ((ref_8047 >> 24) & 0xFF) # Byte reference - MOV operation
ref_8054 = ((ref_8047 >> 16) & 0xFF) # Byte reference - MOV operation
ref_8055 = ((ref_8047 >> 8) & 0xFF) # Byte reference - MOV operation
ref_8056 = (ref_8047 & 0xFF) # Byte reference - MOV operation
ref_10589 = ref_278 # MOV operation
ref_10889 = ref_10589 # MOV operation
ref_10895 = (0x1A5612E2 | ref_10889) # OR operation
ref_12475 = ref_8047 # MOV operation
ref_12610 = ref_12475 # MOV operation
ref_12624 = (0x7063FB7 & ref_12610) # AND operation
ref_12769 = ref_10895 # MOV operation
ref_12773 = ref_12624 # MOV operation
ref_12775 = ((ref_12773 + ref_12769) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_12949 = ref_12775 # MOV operation
ref_12951 = ((ref_12949 >> 56) & 0xFF) # Byte reference - MOV operation
ref_12952 = ((ref_12949 >> 48) & 0xFF) # Byte reference - MOV operation
ref_12953 = ((ref_12949 >> 40) & 0xFF) # Byte reference - MOV operation
ref_12954 = ((ref_12949 >> 32) & 0xFF) # Byte reference - MOV operation
ref_12955 = ((ref_12949 >> 24) & 0xFF) # Byte reference - MOV operation
ref_12956 = ((ref_12949 >> 16) & 0xFF) # Byte reference - MOV operation
ref_12957 = ((ref_12949 >> 8) & 0xFF) # Byte reference - MOV operation
ref_12958 = (ref_12949 & 0xFF) # Byte reference - MOV operation
ref_15939 = ref_12949 # MOV operation
ref_16262 = ref_15939 # MOV operation
ref_16270 = (ref_16262 >> (0x3 & 0x3F)) # SHR operation
ref_16277 = ref_16270 # MOV operation
ref_16432 = ref_16277 # MOV operation
ref_16446 = (0xF & ref_16432) # AND operation
ref_16771 = ref_16446 # MOV operation
ref_16777 = (0x1 | ref_16771) # OR operation
ref_17129 = ref_16777 # MOV operation
ref_17131 = ((0x3162E74F << ((ref_17129 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_18891 = ref_12949 # MOV operation
ref_19214 = ref_18891 # MOV operation
ref_19222 = (ref_19214 >> (0x3 & 0x3F)) # SHR operation
ref_19229 = ref_19222 # MOV operation
ref_19384 = ref_19229 # MOV operation
ref_19398 = (0xF & ref_19384) # AND operation
ref_19723 = ref_19398 # MOV operation
ref_19729 = (0x1 | ref_19723) # OR operation
ref_20061 = ref_19729 # MOV operation
ref_20063 = ((0x40 - ref_20061) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_20071 = ref_20063 # MOV operation
ref_20238 = ref_20071 # MOV operation
ref_20240 = (ref_20238 & 0xFFFFFFFF) # MOV operation
ref_20242 = (0x3162E74F >> ((ref_20240 & 0xFF) & 0x3F)) # SHR operation
ref_20249 = ref_20242 # MOV operation
ref_20389 = ref_17131 # MOV operation
ref_20393 = ref_20249 # MOV operation
ref_20395 = (ref_20393 | ref_20389) # OR operation
ref_20743 = ref_20395 # MOV operation
ref_20751 = (ref_20743 >> (0x4 & 0x3F)) # SHR operation
ref_20758 = ref_20751 # MOV operation
ref_20913 = ref_20758 # MOV operation
ref_20927 = (0x7 & ref_20913) # AND operation
ref_21252 = ref_20927 # MOV operation
ref_21258 = (0x1 | ref_21252) # OR operation
ref_22750 = ref_278 # MOV operation
ref_22865 = ref_22750 # MOV operation
ref_22879 = ((ref_22865 - 0x2907943) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_22887 = ref_22879 # MOV operation
ref_23042 = ref_22887 # MOV operation
ref_23054 = ref_21258 # MOV operation
ref_23056 = ((ref_23042 << ((ref_23054 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_23229 = ref_23056 # MOV operation
ref_25951 = ref_278 # MOV operation
ref_26066 = ref_25951 # MOV operation
ref_26080 = ((ref_26066 - 0x3C563FC) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_26088 = ref_26080 # MOV operation
ref_26256 = ref_26088 # MOV operation
ref_30368 = ref_26256 # MOV operation
ref_32562 = ref_12949 # MOV operation
ref_32697 = ref_32562 # MOV operation
ref_32711 = (0xF & ref_32697) # AND operation
ref_32871 = ref_32711 # MOV operation
ref_32885 = ((ref_32871 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_33030 = ref_30368 # MOV operation
ref_33034 = ref_32885 # MOV operation
ref_33036 = (ref_33034 | ref_33030) # OR operation
ref_33209 = ref_33036 # MOV operation
ref_35839 = ref_23229 # MOV operation
ref_37574 = ref_33209 # MOV operation
ref_37709 = ref_37574 # MOV operation
ref_37723 = (0x1F & ref_37709) # AND operation
ref_37883 = ref_37723 # MOV operation
ref_37897 = ((ref_37883 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_38042 = ref_35839 # MOV operation
ref_38046 = ref_37897 # MOV operation
ref_38048 = (ref_38046 | ref_38042) # OR operation
ref_38221 = ref_38048 # MOV operation
ref_40851 = ref_33209 # MOV operation
ref_43045 = ref_12949 # MOV operation
ref_43180 = ref_43045 # MOV operation
ref_43194 = (0xF & ref_43180) # AND operation
ref_43354 = ref_43194 # MOV operation
ref_43368 = ((ref_43354 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_43513 = ref_40851 # MOV operation
ref_43517 = ref_43368 # MOV operation
ref_43519 = (ref_43517 | ref_43513) # OR operation
ref_43692 = ref_43519 # MOV operation
ref_48263 = ref_43692 # MOV operation
ref_50457 = ref_43692 # MOV operation
ref_50592 = ref_50457 # MOV operation
ref_50606 = (0xF & ref_50592) # AND operation
ref_50766 = ref_50606 # MOV operation
ref_50780 = ((ref_50766 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_50925 = ref_48263 # MOV operation
ref_50929 = ref_50780 # MOV operation
ref_50931 = (ref_50929 | ref_50925) # OR operation
ref_51104 = ref_50931 # MOV operation
ref_53734 = ref_38221 # MOV operation
ref_55469 = ref_51104 # MOV operation
ref_55604 = ref_55469 # MOV operation
ref_55618 = (0x1F & ref_55604) # AND operation
ref_55778 = ref_55618 # MOV operation
ref_55792 = ((ref_55778 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_55937 = ref_53734 # MOV operation
ref_55941 = ref_55792 # MOV operation
ref_55943 = (ref_55941 | ref_55937) # OR operation
ref_56116 = ref_55943 # MOV operation
ref_56118 = ((ref_56116 >> 56) & 0xFF) # Byte reference - MOV operation
ref_56119 = ((ref_56116 >> 48) & 0xFF) # Byte reference - MOV operation
ref_56120 = ((ref_56116 >> 40) & 0xFF) # Byte reference - MOV operation
ref_56121 = ((ref_56116 >> 32) & 0xFF) # Byte reference - MOV operation
ref_56122 = ((ref_56116 >> 24) & 0xFF) # Byte reference - MOV operation
ref_56123 = ((ref_56116 >> 16) & 0xFF) # Byte reference - MOV operation
ref_56124 = ((ref_56116 >> 8) & 0xFF) # Byte reference - MOV operation
ref_56125 = (ref_56116 & 0xFF) # Byte reference - MOV operation
ref_58746 = ref_51104 # MOV operation
ref_60940 = ref_51104 # MOV operation
ref_61075 = ref_60940 # MOV operation
ref_61089 = (0xF & ref_61075) # AND operation
ref_61249 = ref_61089 # MOV operation
ref_61263 = ((ref_61249 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_61408 = ref_58746 # MOV operation
ref_61412 = ref_61263 # MOV operation
ref_61414 = (ref_61412 | ref_61408) # OR operation
ref_61587 = ref_61414 # MOV operation
ref_73620 = ref_61587 # MOV operation
ref_75355 = ref_56116 # MOV operation
ref_76730 = ref_56116 # MOV operation
ref_76850 = ref_75355 # MOV operation
ref_76854 = ref_76730 # MOV operation
ref_76856 = ((ref_76854 + ref_76850) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_77017 = ref_76856 # MOV operation
ref_77031 = (0x7 & ref_77017) # AND operation
ref_77191 = ref_77031 # MOV operation
ref_77205 = ((ref_77191 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_77350 = ref_73620 # MOV operation
ref_77354 = ref_77205 # MOV operation
ref_77356 = (ref_77354 | ref_77350) # OR operation
ref_77529 = ref_77356 # MOV operation
ref_79831 = ((((ref_56118) << 8 | ref_56119) << 8 | ref_56120) << 8 | ref_56121) # MOV operation
ref_80137 = (ref_79831 & 0xFFFFFFFF) # MOV operation
ref_82435 = ((((ref_56122) << 8 | ref_56123) << 8 | ref_56124) << 8 | ref_56125) # MOV operation
ref_84718 = (ref_82435 & 0xFFFFFFFF) # MOV operation
ref_84720 = (((ref_84718 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_84721 = (((ref_84718 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_84722 = (((ref_84718 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_84723 = ((ref_84718 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_85039 = (ref_80137 & 0xFFFFFFFF) # MOV operation
ref_87322 = (ref_85039 & 0xFFFFFFFF) # MOV operation
ref_87324 = (((ref_87322 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_87325 = (((ref_87322 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_87326 = (((ref_87322 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_87327 = ((ref_87322 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_89764 = ref_8051 # MOVZX operation
ref_89899 = (ref_89764 & 0xFF) # MOVZX operation
ref_94314 = ref_8052 # MOVZX operation
ref_94449 = (ref_94314 & 0xFF) # MOVZX operation
ref_94451 = (ref_94449 & 0xFF) # Byte reference - MOV operation
ref_96887 = (ref_89899 & 0xFF) # MOVZX operation
ref_97022 = (ref_96887 & 0xFF) # MOVZX operation
ref_97024 = (ref_97022 & 0xFF) # Byte reference - MOV operation
ref_99460 = ref_8050 # MOVZX operation
ref_99595 = (ref_99460 & 0xFF) # MOVZX operation
ref_104010 = ref_8056 # MOVZX operation
ref_104145 = (ref_104010 & 0xFF) # MOVZX operation
ref_104147 = (ref_104145 & 0xFF) # Byte reference - MOV operation
ref_106583 = (ref_99595 & 0xFF) # MOVZX operation
ref_106718 = (ref_106583 & 0xFF) # MOVZX operation
ref_106720 = (ref_106718 & 0xFF) # Byte reference - MOV operation
ref_109012 = ((((ref_12955) << 8 | ref_12956) << 8 | ref_12957) << 8 | ref_12958) # MOV operation
ref_109318 = (ref_109012 & 0xFFFFFFFF) # MOV operation
ref_111616 = ((((ref_12951) << 8 | ref_12952) << 8 | ref_12953) << 8 | ref_12954) # MOV operation
ref_113899 = (ref_111616 & 0xFFFFFFFF) # MOV operation
ref_113901 = (((ref_113899 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_113902 = (((ref_113899 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_113903 = (((ref_113899 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_113904 = ((ref_113899 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_114220 = (ref_109318 & 0xFFFFFFFF) # MOV operation
ref_116503 = (ref_114220 & 0xFFFFFFFF) # MOV operation
ref_116505 = (((ref_116503 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_116506 = (((ref_116503 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_116507 = (((ref_116503 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_116508 = ((ref_116503 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_121011 = ((((((((ref_116505) << 8 | ref_116506) << 8 | ref_116507) << 8 | ref_116508) << 8 | ref_113901) << 8 | ref_113902) << 8 | ref_113903) << 8 | ref_113904) # MOV operation
ref_123205 = ((((((((ref_8049) << 8 | ref_104147) << 8 | ref_94451) << 8 | ref_97024) << 8 | ref_8053) << 8 | ref_8054) << 8 | ref_8055) << 8 | ref_106720) # MOV operation
ref_123340 = ref_123205 # MOV operation
ref_123354 = (0x3F & ref_123340) # AND operation
ref_123514 = ref_123354 # MOV operation
ref_123528 = ((ref_123514 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_123673 = ref_121011 # MOV operation
ref_123677 = ref_123528 # MOV operation
ref_123679 = (ref_123677 | ref_123673) # OR operation
ref_123852 = ref_123679 # MOV operation
ref_128708 = ((((((((ref_84720) << 8 | ref_84721) << 8 | ref_84722) << 8 | ref_84723) << 8 | ref_87324) << 8 | ref_87325) << 8 | ref_87326) << 8 | ref_87327) # MOV operation
ref_130443 = ref_77529 # MOV operation
ref_131998 = ref_123852 # MOV operation
ref_132321 = ref_131998 # MOV operation
ref_132329 = (ref_132321 >> (0x3 & 0x3F)) # SHR operation
ref_132336 = ref_132329 # MOV operation
ref_132491 = ref_132336 # MOV operation
ref_132505 = (0xF & ref_132491) # AND operation
ref_132830 = ref_132505 # MOV operation
ref_132836 = (0x1 | ref_132830) # OR operation
ref_133004 = ref_130443 # MOV operation
ref_133008 = ref_132836 # MOV operation
ref_133010 = (ref_133008 & 0xFFFFFFFF) # MOV operation
ref_133012 = (ref_133004 >> ((ref_133010 & 0xFF) & 0x3F)) # SHR operation
ref_133019 = ref_133012 # MOV operation
ref_134594 = ref_123852 # MOV operation
ref_134917 = ref_134594 # MOV operation
ref_134925 = (ref_134917 >> (0x3 & 0x3F)) # SHR operation
ref_134932 = ref_134925 # MOV operation
ref_135087 = ref_134932 # MOV operation
ref_135101 = (0xF & ref_135087) # AND operation
ref_135426 = ref_135101 # MOV operation
ref_135432 = (0x1 | ref_135426) # OR operation
ref_135764 = ref_135432 # MOV operation
ref_135766 = ((0x40 - ref_135764) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_135774 = ref_135766 # MOV operation
ref_137169 = ref_77529 # MOV operation
ref_137304 = ref_137169 # MOV operation
ref_137316 = ref_135774 # MOV operation
ref_137318 = ((ref_137304 << ((ref_137316 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_137463 = ref_133019 # MOV operation
ref_137467 = ref_137318 # MOV operation
ref_137469 = (ref_137467 | ref_137463) # OR operation
ref_137629 = ref_137469 # MOV operation
ref_137643 = (0xF & ref_137629) # AND operation
ref_137803 = ref_137643 # MOV operation
ref_137817 = ((ref_137803 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_137962 = ref_128708 # MOV operation
ref_137966 = ref_137817 # MOV operation
ref_137968 = (ref_137966 | ref_137962) # OR operation
ref_138141 = ref_137968 # MOV operation
ref_140872 = ref_123852 # MOV operation
ref_141195 = ref_140872 # MOV operation
ref_141203 = (ref_141195 >> (0x3 & 0x3F)) # SHR operation
ref_141210 = ref_141203 # MOV operation
ref_141365 = ref_141210 # MOV operation
ref_141379 = (0x7 & ref_141365) # AND operation
ref_141704 = ref_141379 # MOV operation
ref_141710 = (0x1 | ref_141704) # OR operation
ref_143110 = ((((((((ref_8049) << 8 | ref_104147) << 8 | ref_94451) << 8 | ref_97024) << 8 | ref_8053) << 8 | ref_8054) << 8 | ref_8055) << 8 | ref_106720) # MOV operation
ref_143245 = ref_143110 # MOV operation
ref_143257 = ref_141710 # MOV operation
ref_143259 = ((ref_143245 << ((ref_143257 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_144659 = ref_138141 # MOV operation
ref_146034 = ref_77529 # MOV operation
ref_146154 = ref_144659 # MOV operation
ref_146158 = ref_146034 # MOV operation
ref_146160 = (ref_146158 | ref_146154) # OR operation
ref_146305 = ref_143259 # MOV operation
ref_146309 = ref_146160 # MOV operation
ref_146311 = (ref_146309 | ref_146305) # OR operation
ref_146484 = ref_146311 # MOV operation
ref_146793 = ref_146484 # MOV operation
ref_146795 = ref_146793 # MOV operation

print(ref_146795 & 0xffffffffffffffff)
