#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_5424 = ref_278 # MOV operation
ref_5456 = ref_5424 # MOV operation
ref_5470 = ((ref_5456 - 0x35CEDE6D) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_5478 = ref_5470 # MOV operation
ref_5512 = ref_5478 # MOV operation
ref_6187 = ref_278 # MOV operation
ref_6229 = ref_6187 # MOV operation
ref_6237 = ((((0x0) << 64 | ref_6229) / 0x7) & 0xFFFFFFFFFFFFFFFF) # DIV operation
ref_6272 = ref_6237 # MOV operation
ref_6816 = ref_6272 # MOV operation
ref_6840 = ref_6816 # MOV operation
ref_6848 = (ref_6840 >> (0x3 & 0x3F)) # SHR operation
ref_6855 = ref_6848 # MOV operation
ref_6889 = ref_6855 # MOV operation
ref_6903 = (0xF & ref_6889) # AND operation
ref_6942 = ref_6903 # MOV operation
ref_6956 = (0x1 | ref_6942) # OR operation
ref_7007 = ref_6956 # MOV operation
ref_7009 = (ref_7007 & 0xFFFFFFFF) # MOV operation
ref_7011 = ((0x7A11169 << ((ref_7009 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_7018 = ref_7011 # MOV operation
ref_7396 = ref_6272 # MOV operation
ref_7428 = ref_7396 # MOV operation
ref_7442 = (ref_7428 >> (0x3 & 0x3F)) # SHR operation
ref_7497 = ref_7442 # MOV operation
ref_7511 = (0xF & ref_7497) # AND operation
ref_7566 = ref_7511 # MOV operation
ref_7580 = (0x1 | ref_7566) # OR operation
ref_7647 = ref_7580 # MOV operation
ref_7649 = ((0x40 - ref_7647) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_7657 = ref_7649 # MOV operation
ref_7719 = ref_7657 # MOV operation
ref_7721 = (0x7A11169 >> ((ref_7719 & 0xFF) & 0x3F)) # SHR operation
ref_7742 = ref_7018 # MOV operation
ref_7754 = ref_7721 # MOV operation
ref_7756 = (ref_7754 | ref_7742) # OR operation
ref_7779 = ref_7756 # MOV operation
ref_7793 = (ref_7779 >> (0x4 & 0x3F)) # SHR operation
ref_7840 = ref_7793 # MOV operation
ref_7846 = (0xF & ref_7840) # AND operation
ref_7893 = ref_7846 # MOV operation
ref_7899 = (0x1 | ref_7893) # OR operation
ref_8291 = ref_278 # MOV operation
ref_8323 = ref_8291 # MOV operation
ref_8335 = ref_7899 # MOV operation
ref_8337 = ((ref_8323 << ((ref_8335 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_8650 = ref_6272 # MOV operation
ref_8674 = ref_8650 # MOV operation
ref_8682 = (ref_8674 >> (0x3 & 0x3F)) # SHR operation
ref_8689 = ref_8682 # MOV operation
ref_8723 = ref_8689 # MOV operation
ref_8737 = (0xF & ref_8723) # AND operation
ref_8776 = ref_8737 # MOV operation
ref_8790 = (0x1 | ref_8776) # OR operation
ref_8841 = ref_8790 # MOV operation
ref_8843 = (ref_8841 & 0xFFFFFFFF) # MOV operation
ref_8845 = ((0x7A11169 << ((ref_8843 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_8852 = ref_8845 # MOV operation
ref_9230 = ref_6272 # MOV operation
ref_9262 = ref_9230 # MOV operation
ref_9276 = (ref_9262 >> (0x3 & 0x3F)) # SHR operation
ref_9331 = ref_9276 # MOV operation
ref_9345 = (0xF & ref_9331) # AND operation
ref_9400 = ref_9345 # MOV operation
ref_9414 = (0x1 | ref_9400) # OR operation
ref_9481 = ref_9414 # MOV operation
ref_9483 = ((0x40 - ref_9481) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_9491 = ref_9483 # MOV operation
ref_9553 = ref_9491 # MOV operation
ref_9555 = (0x7A11169 >> ((ref_9553 & 0xFF) & 0x3F)) # SHR operation
ref_9576 = ref_8852 # MOV operation
ref_9588 = ref_9555 # MOV operation
ref_9590 = (ref_9588 | ref_9576) # OR operation
ref_9613 = ref_9590 # MOV operation
ref_9627 = (ref_9613 >> (0x4 & 0x3F)) # SHR operation
ref_9674 = ref_9627 # MOV operation
ref_9680 = (0xF & ref_9674) # AND operation
ref_9727 = ref_9680 # MOV operation
ref_9733 = (0x1 | ref_9727) # OR operation
ref_9784 = ref_9733 # MOV operation
ref_9786 = ((0x40 - ref_9784) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_9794 = ref_9786 # MOV operation
ref_10181 = ref_278 # MOV operation
ref_10213 = ref_10181 # MOV operation
ref_10225 = ref_9794 # MOV operation
ref_10227 = (ref_10213 >> ((ref_10225 & 0xFF) & 0x3F)) # SHR operation
ref_10264 = ref_8337 # MOV operation
ref_10276 = ref_10227 # MOV operation
ref_10278 = (ref_10276 | ref_10264) # OR operation
ref_10317 = ref_10278 # MOV operation
ref_11010 = ref_278 # MOV operation
ref_11042 = ref_11010 # MOV operation
ref_11056 = ((ref_11042 - 0x297EE8A1) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_11064 = ref_11056 # MOV operation
ref_11108 = ref_11064 # MOV operation
ref_11122 = (((sx(0x40, 0x1471C5DA) * sx(0x40, ref_11108)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_11158 = ref_11122 # MOV operation
ref_11160 = ((ref_11158 >> 56) & 0xFF) # Byte reference - MOV operation
ref_11161 = ((ref_11158 >> 48) & 0xFF) # Byte reference - MOV operation
ref_11162 = ((ref_11158 >> 40) & 0xFF) # Byte reference - MOV operation
ref_11163 = ((ref_11158 >> 32) & 0xFF) # Byte reference - MOV operation
ref_11164 = ((ref_11158 >> 24) & 0xFF) # Byte reference - MOV operation
ref_11165 = ((ref_11158 >> 16) & 0xFF) # Byte reference - MOV operation
ref_11166 = ((ref_11158 >> 8) & 0xFF) # Byte reference - MOV operation
ref_11167 = (ref_11158 & 0xFF) # Byte reference - MOV operation
ref_11602 = ((ref_11162) << 8 | ref_11163) # MOVZX operation
ref_11674 = (ref_11602 & 0xFFFF) # MOVZX operation
ref_12202 = ((ref_11164) << 8 | ref_11165) # MOVZX operation
ref_12648 = (ref_12202 & 0xFFFF) # MOVZX operation
ref_12696 = (ref_11674 & 0xFFFF) # MOVZX operation
ref_13232 = (ref_12696 & 0xFFFF) # MOVZX operation
ref_13234 = (((ref_13232 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_13235 = ((ref_13232 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_16492 = ref_6272 # MOV operation
ref_16784 = ref_10317 # MOV operation
ref_16834 = ref_16784 # MOV operation
ref_16848 = (0x1F & ref_16834) # AND operation
ref_16885 = ref_16848 # MOV operation
ref_16899 = ((ref_16885 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_16936 = ref_16492 # MOV operation
ref_16948 = ref_16899 # MOV operation
ref_16950 = (ref_16948 | ref_16936) # OR operation
ref_16989 = ref_16950 # MOV operation
ref_17595 = ref_16989 # MOV operation
ref_17887 = ref_16989 # MOV operation
ref_17937 = ref_17887 # MOV operation
ref_17951 = (0xF & ref_17937) # AND operation
ref_17988 = ref_17951 # MOV operation
ref_18002 = ((ref_17988 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_18039 = ref_17595 # MOV operation
ref_18051 = ref_18002 # MOV operation
ref_18053 = (ref_18051 | ref_18039) # OR operation
ref_18092 = ref_18053 # MOV operation
ref_18724 = ((ref_11160) << 8 | ref_11161) # MOVZX operation
ref_18796 = (ref_18724 & 0xFFFF) # MOVZX operation
ref_19324 = ((ref_11166) << 8 | ref_11167) # MOVZX operation
ref_19770 = (ref_19324 & 0xFFFF) # MOVZX operation
ref_19772 = (((ref_19770 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_19773 = ((ref_19770 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_19818 = (ref_18796 & 0xFFFF) # MOVZX operation
ref_20354 = (ref_19818 & 0xFFFF) # MOVZX operation
ref_20734 = (ref_20354 & 0xFFFF) # MOVZX operation
ref_20790 = (ref_20734 & 0xFFFF) # MOVZX operation
ref_21308 = (ref_12648 & 0xFFFF) # MOVZX operation
ref_21754 = (ref_21308 & 0xFFFF) # MOVZX operation
ref_21756 = (((ref_21754 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_21757 = ((ref_21754 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_21802 = (ref_20790 & 0xFFFF) # MOVZX operation
ref_22338 = (ref_21802 & 0xFFFF) # MOVZX operation
ref_22340 = (((ref_22338 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_22341 = ((ref_22338 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_23040 = ((((((((ref_19772) << 8 | ref_19773) << 8 | ref_22340) << 8 | ref_22341) << 8 | ref_13234) << 8 | ref_13235) << 8 | ref_21756) << 8 | ref_21757) # MOV operation
ref_23072 = ref_23040 # MOV operation
ref_23086 = (ref_23072 >> (0x2 & 0x3F)) # SHR operation
ref_23141 = ref_23086 # MOV operation
ref_23155 = (0xF & ref_23141) # AND operation
ref_23210 = ref_23155 # MOV operation
ref_23224 = (0x1 | ref_23210) # OR operation
ref_23503 = ref_10317 # MOV operation
ref_23535 = ref_23503 # MOV operation
ref_23547 = ref_23224 # MOV operation
ref_23549 = ((ref_23535 << ((ref_23547 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_23952 = ((((((((ref_19772) << 8 | ref_19773) << 8 | ref_22340) << 8 | ref_22341) << 8 | ref_13234) << 8 | ref_13235) << 8 | ref_21756) << 8 | ref_21757) # MOV operation
ref_23984 = ref_23952 # MOV operation
ref_23998 = (ref_23984 >> (0x2 & 0x3F)) # SHR operation
ref_24053 = ref_23998 # MOV operation
ref_24067 = (0xF & ref_24053) # AND operation
ref_24122 = ref_24067 # MOV operation
ref_24136 = (0x1 | ref_24122) # OR operation
ref_24203 = ref_24136 # MOV operation
ref_24205 = ((0x40 - ref_24203) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_24213 = ref_24205 # MOV operation
ref_24487 = ref_10317 # MOV operation
ref_24519 = ref_24487 # MOV operation
ref_24531 = ref_24213 # MOV operation
ref_24533 = (ref_24519 >> ((ref_24531 & 0xFF) & 0x3F)) # SHR operation
ref_24554 = ref_23549 # MOV operation
ref_24566 = ref_24533 # MOV operation
ref_24568 = (ref_24566 | ref_24554) # OR operation
ref_24591 = ref_24568 # MOV operation
ref_24605 = (ref_24591 >> (0x4 & 0x3F)) # SHR operation
ref_24652 = ref_24605 # MOV operation
ref_24658 = (0xF & ref_24652) # AND operation
ref_24791 = ref_24658 # MOV operation
ref_24797 = (0x1 | ref_24791) # OR operation
ref_25032 = ref_18092 # MOV operation
ref_25066 = ref_25032 # MOV operation
ref_25080 = (0xF & ref_25066) # AND operation
ref_25119 = ref_25080 # MOV operation
ref_25133 = (0x1 | ref_25119) # OR operation
ref_25412 = ref_5512 # MOV operation
ref_25436 = ref_25412 # MOV operation
ref_25440 = ref_25133 # MOV operation
ref_25442 = (ref_25440 & 0xFFFFFFFF) # MOV operation
ref_25444 = ((ref_25436 << ((ref_25442 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_25451 = ref_25444 # MOV operation
ref_25725 = ref_18092 # MOV operation
ref_25865 = ref_25725 # MOV operation
ref_25879 = (0xF & ref_25865) # AND operation
ref_25918 = ref_25879 # MOV operation
ref_25932 = (0x1 | ref_25918) # OR operation
ref_25983 = ref_25932 # MOV operation
ref_25985 = ((0x40 - ref_25983) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_25993 = ref_25985 # MOV operation
ref_26267 = ref_5512 # MOV operation
ref_26291 = ref_26267 # MOV operation
ref_26295 = ref_25993 # MOV operation
ref_26297 = (ref_26295 & 0xFFFFFFFF) # MOV operation
ref_26299 = (ref_26291 >> ((ref_26297 & 0xFF) & 0x3F)) # SHR operation
ref_26306 = ref_26299 # MOV operation
ref_26332 = ref_25451 # MOV operation
ref_26336 = ref_26306 # MOV operation
ref_26338 = (ref_26336 | ref_26332) # OR operation
ref_26375 = ref_26338 # MOV operation
ref_26387 = ref_24797 # MOV operation
ref_26389 = (ref_26375 >> ((ref_26387 & 0xFF) & 0x3F)) # SHR operation
ref_26810 = ((((((((ref_19772) << 8 | ref_19773) << 8 | ref_22340) << 8 | ref_22341) << 8 | ref_13234) << 8 | ref_13235) << 8 | ref_21756) << 8 | ref_21757) # MOV operation
ref_26842 = ref_26810 # MOV operation
ref_26856 = (ref_26842 >> (0x2 & 0x3F)) # SHR operation
ref_26911 = ref_26856 # MOV operation
ref_26925 = (0xF & ref_26911) # AND operation
ref_26980 = ref_26925 # MOV operation
ref_26994 = (0x1 | ref_26980) # OR operation
ref_27273 = ref_10317 # MOV operation
ref_27305 = ref_27273 # MOV operation
ref_27317 = ref_26994 # MOV operation
ref_27319 = ((ref_27305 << ((ref_27317 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_27722 = ((((((((ref_19772) << 8 | ref_19773) << 8 | ref_22340) << 8 | ref_22341) << 8 | ref_13234) << 8 | ref_13235) << 8 | ref_21756) << 8 | ref_21757) # MOV operation
ref_27754 = ref_27722 # MOV operation
ref_27768 = (ref_27754 >> (0x2 & 0x3F)) # SHR operation
ref_27823 = ref_27768 # MOV operation
ref_27837 = (0xF & ref_27823) # AND operation
ref_27892 = ref_27837 # MOV operation
ref_27906 = (0x1 | ref_27892) # OR operation
ref_27973 = ref_27906 # MOV operation
ref_27975 = ((0x40 - ref_27973) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_27983 = ref_27975 # MOV operation
ref_28257 = ref_10317 # MOV operation
ref_28289 = ref_28257 # MOV operation
ref_28301 = ref_27983 # MOV operation
ref_28303 = (ref_28289 >> ((ref_28301 & 0xFF) & 0x3F)) # SHR operation
ref_28324 = ref_27319 # MOV operation
ref_28336 = ref_28303 # MOV operation
ref_28338 = (ref_28336 | ref_28324) # OR operation
ref_28361 = ref_28338 # MOV operation
ref_28375 = (ref_28361 >> (0x4 & 0x3F)) # SHR operation
ref_28422 = ref_28375 # MOV operation
ref_28428 = (0xF & ref_28422) # AND operation
ref_28561 = ref_28428 # MOV operation
ref_28567 = (0x1 | ref_28561) # OR operation
ref_28618 = ref_28567 # MOV operation
ref_28620 = ((0x40 - ref_28618) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_28628 = ref_28620 # MOV operation
ref_28858 = ref_18092 # MOV operation
ref_28892 = ref_28858 # MOV operation
ref_28906 = (0xF & ref_28892) # AND operation
ref_28945 = ref_28906 # MOV operation
ref_28959 = (0x1 | ref_28945) # OR operation
ref_29238 = ref_5512 # MOV operation
ref_29262 = ref_29238 # MOV operation
ref_29266 = ref_28959 # MOV operation
ref_29268 = (ref_29266 & 0xFFFFFFFF) # MOV operation
ref_29270 = ((ref_29262 << ((ref_29268 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_29277 = ref_29270 # MOV operation
ref_29637 = ref_18092 # MOV operation
ref_29687 = ref_29637 # MOV operation
ref_29701 = (0xF & ref_29687) # AND operation
ref_29756 = ref_29701 # MOV operation
ref_29770 = (0x1 | ref_29756) # OR operation
ref_29837 = ref_29770 # MOV operation
ref_29839 = ((0x40 - ref_29837) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_29847 = ref_29839 # MOV operation
ref_30121 = ref_5512 # MOV operation
ref_30153 = ref_30121 # MOV operation
ref_30165 = ref_29847 # MOV operation
ref_30167 = (ref_30153 >> ((ref_30165 & 0xFF) & 0x3F)) # SHR operation
ref_30188 = ref_29277 # MOV operation
ref_30200 = ref_30167 # MOV operation
ref_30202 = (ref_30200 | ref_30188) # OR operation
ref_30225 = ref_30202 # MOV operation
ref_30237 = ref_28628 # MOV operation
ref_30239 = ((ref_30225 << ((ref_30237 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_30276 = ref_26389 # MOV operation
ref_30288 = ref_30239 # MOV operation
ref_30290 = (ref_30288 | ref_30276) # OR operation
ref_30329 = ref_30290 # MOV operation
ref_30576 = ref_30329 # MOV operation
ref_30578 = ref_30576 # MOV operation

print(ref_30578 & 0xffffffffffffffff)
