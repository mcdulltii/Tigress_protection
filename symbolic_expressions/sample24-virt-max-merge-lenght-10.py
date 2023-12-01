#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])

ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_5494 = ref_278 # MOV operation
ref_5526 = ref_5494 # MOV operation
ref_5540 = ((ref_5526 << (0xB & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_5950 = ref_278 # MOV operation
ref_5982 = ref_5950 # MOV operation
ref_5996 = (ref_5982 >> (0x35 & 0x3F)) # SHR operation
ref_6033 = ref_5540 # MOV operation
ref_6045 = ref_5996 # MOV operation
ref_6047 = (ref_6045 | ref_6033) # OR operation
ref_6084 = ref_6047 # MOV operation
ref_6098 = (ref_6084 >> (0x1 & 0x3F)) # SHR operation
ref_6137 = ref_6098 # MOV operation
ref_6821 = ref_6137 # MOV operation
ref_6865 = ref_6821 # MOV operation
ref_6879 = (((sx(0x40, 0x6B33F46) * sx(0x40, ref_6865)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_7416 = ref_278 # MOV operation
ref_7458 = ref_7416 # MOV operation
ref_7466 = ((((0x0) << 64 | ref_7458) / 0x3) & 0xFFFFFFFFFFFFFFFF) # DIV operation
ref_7499 = ref_7466 # MOV operation
ref_7511 = ref_6879 # MOV operation
ref_7513 = ((ref_7499 - ref_7511) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_7521 = ref_7513 # MOV operation
ref_7555 = ref_7521 # MOV operation
ref_8313 = ref_7555 # MOV operation
ref_8337 = ref_8313 # MOV operation
ref_8345 = (ref_8337 >> (0x7 & 0x3F)) # SHR operation
ref_8352 = ref_8345 # MOV operation
ref_8370 = ref_8352 # MOV operation
ref_8384 = (ref_8370 >> (0x2 & 0x3F)) # SHR operation
ref_8513 = ref_8384 # MOV operation
ref_8527 = (0x7 & ref_8513) # AND operation
ref_8574 = ref_8527 # MOV operation
ref_8580 = (0x1 | ref_8574) # OR operation
ref_9030 = ref_278 # MOV operation
ref_9062 = ref_9030 # MOV operation
ref_9076 = ((0x9919884 + ref_9062) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_9114 = ref_9076 # MOV operation
ref_9126 = ref_8580 # MOV operation
ref_9128 = (ref_9114 >> ((ref_9126 & 0xFF) & 0x3F)) # SHR operation
ref_9167 = ref_9128 # MOV operation
ref_9998 = ref_278 # MOV operation
ref_10030 = ref_9998 # MOV operation
ref_10044 = ((0x1E5EA08F8 + ref_10030) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_10084 = ref_10044 # MOV operation
ref_11562 = ref_9167 # MOV operation
ref_12184 = ref_9167 # MOV operation
ref_12202 = ref_12184 # MOV operation
ref_12216 = (0x3F & ref_12202) # AND operation
ref_12253 = ref_12216 # MOV operation
ref_12267 = ((ref_12253 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_12304 = ref_11562 # MOV operation
ref_12316 = ref_12267 # MOV operation
ref_12318 = (ref_12316 | ref_12304) # OR operation
ref_12357 = ref_12318 # MOV operation
ref_13863 = ref_12357 # MOV operation
ref_14407 = ref_7555 # MOV operation
ref_14431 = ref_14407 # MOV operation
ref_14439 = (ref_14431 >> (0x2 & 0x3F)) # SHR operation
ref_14446 = ref_14439 # MOV operation
ref_14550 = ref_14446 # MOV operation
ref_14564 = (0xF & ref_14550) # AND operation
ref_14611 = ref_14564 # MOV operation
ref_14617 = (0x1 | ref_14611) # OR operation
ref_14988 = ref_6137 # MOV operation
ref_15012 = ref_14988 # MOV operation
ref_15016 = ref_14617 # MOV operation
ref_15018 = (ref_15016 & 0xFFFFFFFF) # MOV operation
ref_15020 = ((ref_15012 << ((ref_15018 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_15027 = ref_15020 # MOV operation
ref_15515 = ref_7555 # MOV operation
ref_15539 = ref_15515 # MOV operation
ref_15547 = (ref_15539 >> (0x2 & 0x3F)) # SHR operation
ref_15554 = ref_15547 # MOV operation
ref_15658 = ref_15554 # MOV operation
ref_15672 = (0xF & ref_15658) # AND operation
ref_15719 = ref_15672 # MOV operation
ref_15725 = (0x1 | ref_15719) # OR operation
ref_15776 = ref_15725 # MOV operation
ref_15778 = ((0x40 - ref_15776) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_15786 = ref_15778 # MOV operation
ref_16152 = ref_6137 # MOV operation
ref_16176 = ref_16152 # MOV operation
ref_16180 = ref_15786 # MOV operation
ref_16182 = (ref_16180 & 0xFFFFFFFF) # MOV operation
ref_16184 = (ref_16176 >> ((ref_16182 & 0xFF) & 0x3F)) # SHR operation
ref_16191 = ref_16184 # MOV operation
ref_16217 = ref_15027 # MOV operation
ref_16221 = ref_16191 # MOV operation
ref_16223 = (ref_16221 | ref_16217) # OR operation
ref_16352 = ref_16223 # MOV operation
ref_16366 = (0x7 & ref_16352) # AND operation
ref_16403 = ref_16366 # MOV operation
ref_16417 = ((ref_16403 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_16454 = ref_13863 # MOV operation
ref_16466 = ref_16417 # MOV operation
ref_16468 = (ref_16466 | ref_16454) # OR operation
ref_16507 = ref_16468 # MOV operation
ref_17087 = ref_10084 # MOV operation
ref_17111 = ref_17087 # MOV operation
ref_17119 = (ref_17111 >> (0x4 & 0x3F)) # SHR operation
ref_17126 = ref_17119 # MOV operation
ref_17230 = ref_17126 # MOV operation
ref_17244 = (0xF & ref_17230) # AND operation
ref_17291 = ref_17244 # MOV operation
ref_17297 = (0x1 | ref_17291) # OR operation
ref_17668 = ref_16507 # MOV operation
ref_17692 = ref_17668 # MOV operation
ref_17696 = ref_17297 # MOV operation
ref_17698 = (ref_17696 & 0xFFFFFFFF) # MOV operation
ref_17700 = (ref_17692 >> ((ref_17698 & 0xFF) & 0x3F)) # SHR operation
ref_17707 = ref_17700 # MOV operation
ref_18195 = ref_10084 # MOV operation
ref_18219 = ref_18195 # MOV operation
ref_18227 = (ref_18219 >> (0x4 & 0x3F)) # SHR operation
ref_18234 = ref_18227 # MOV operation
ref_18338 = ref_18234 # MOV operation
ref_18352 = (0xF & ref_18338) # AND operation
ref_18399 = ref_18352 # MOV operation
ref_18405 = (0x1 | ref_18399) # OR operation
ref_18456 = ref_18405 # MOV operation
ref_18458 = ((0x40 - ref_18456) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_18466 = ref_18458 # MOV operation
ref_18832 = ref_16507 # MOV operation
ref_18856 = ref_18832 # MOV operation
ref_18860 = ref_18466 # MOV operation
ref_18862 = (ref_18860 & 0xFFFFFFFF) # MOV operation
ref_18864 = ((ref_18856 << ((ref_18862 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_18871 = ref_18864 # MOV operation
ref_18897 = ref_17707 # MOV operation
ref_18901 = ref_18871 # MOV operation
ref_18903 = (ref_18901 | ref_18897) # OR operation
ref_19416 = ref_7555 # MOV operation
ref_19440 = ref_19416 # MOV operation
ref_19448 = (ref_19440 >> (0x3 & 0x3F)) # SHR operation
ref_19455 = ref_19448 # MOV operation
ref_19559 = ref_19455 # MOV operation
ref_19573 = (0xF & ref_19559) # AND operation
ref_19620 = ref_19573 # MOV operation
ref_19626 = (0x1 | ref_19620) # OR operation
ref_19997 = ref_6137 # MOV operation
ref_20021 = ref_19997 # MOV operation
ref_20025 = ref_19626 # MOV operation
ref_20027 = (ref_20025 & 0xFFFFFFFF) # MOV operation
ref_20029 = (ref_20021 >> ((ref_20027 & 0xFF) & 0x3F)) # SHR operation
ref_20036 = ref_20029 # MOV operation
ref_20524 = ref_7555 # MOV operation
ref_20548 = ref_20524 # MOV operation
ref_20556 = (ref_20548 >> (0x3 & 0x3F)) # SHR operation
ref_20563 = ref_20556 # MOV operation
ref_20667 = ref_20563 # MOV operation
ref_20681 = (0xF & ref_20667) # AND operation
ref_20728 = ref_20681 # MOV operation
ref_20734 = (0x1 | ref_20728) # OR operation
ref_20785 = ref_20734 # MOV operation
ref_20787 = ((0x40 - ref_20785) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_20795 = ref_20787 # MOV operation
ref_21161 = ref_6137 # MOV operation
ref_21185 = ref_21161 # MOV operation
ref_21189 = ref_20795 # MOV operation
ref_21191 = (ref_21189 & 0xFFFFFFFF) # MOV operation
ref_21193 = ((ref_21185 << ((ref_21191 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_21200 = ref_21193 # MOV operation
ref_21226 = ref_20036 # MOV operation
ref_21230 = ref_21200 # MOV operation
ref_21232 = (ref_21230 | ref_21226) # OR operation
ref_21361 = ref_21232 # MOV operation
ref_21373 = ref_18903 # MOV operation
ref_21375 = ((ref_21361 - ref_21373) & 0xFFFFFFFFFFFFFFFF) # CMP operation
ref_21377 = ((((ref_21361 ^ (ref_21373 ^ ref_21375)) ^ ((ref_21361 ^ ref_21375) & (ref_21361 ^ ref_21373))) >> 63) & 0x1) # Carry flag
ref_21381 = (0x1 if (ref_21375 == 0x0) else 0x0) # Zero flag
ref_21383 = ((((ref_21373 >> 8) & 0xFFFFFFFFFFFFFF)) << 8 | (0x1 if (((~(ref_21377) & 0x1) & (~(ref_21381) & 0x1)) == 0x1) else 0x0)) # SETA operation
ref_21385 = (ref_21383 & 0xFF) # MOVZX operation
ref_21403 = (ref_21385 & 0xFFFFFFFF) # MOV operation
ref_21405 = ((ref_21403 & 0xFFFFFFFF) & (ref_21403 & 0xFFFFFFFF)) # TEST operation
ref_21410 = (0x1 if (ref_21405 == 0x0) else 0x0) # Zero flag
ref_21412 = (0x2A79 if (ref_21410 == 0x1) else 0x2A5B) # Program Counter


if (ref_21410 == 0x1):
    ref_263 = SymVar_0
    ref_278 = ref_263 # MOV operation
    ref_5494 = ref_278 # MOV operation
    ref_5526 = ref_5494 # MOV operation
    ref_5540 = ((ref_5526 << (0xB & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_5950 = ref_278 # MOV operation
    ref_5982 = ref_5950 # MOV operation
    ref_5996 = (ref_5982 >> (0x35 & 0x3F)) # SHR operation
    ref_6033 = ref_5540 # MOV operation
    ref_6045 = ref_5996 # MOV operation
    ref_6047 = (ref_6045 | ref_6033) # OR operation
    ref_6084 = ref_6047 # MOV operation
    ref_6098 = (ref_6084 >> (0x1 & 0x3F)) # SHR operation
    ref_6137 = ref_6098 # MOV operation
    ref_6821 = ref_6137 # MOV operation
    ref_6865 = ref_6821 # MOV operation
    ref_6879 = (((sx(0x40, 0x6B33F46) * sx(0x40, ref_6865)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_7416 = ref_278 # MOV operation
    ref_7458 = ref_7416 # MOV operation
    ref_7466 = ((((0x0) << 64 | ref_7458) / 0x3) & 0xFFFFFFFFFFFFFFFF) # DIV operation
    ref_7499 = ref_7466 # MOV operation
    ref_7511 = ref_6879 # MOV operation
    ref_7513 = ((ref_7499 - ref_7511) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_7521 = ref_7513 # MOV operation
    ref_7555 = ref_7521 # MOV operation
    ref_8313 = ref_7555 # MOV operation
    ref_8337 = ref_8313 # MOV operation
    ref_8345 = (ref_8337 >> (0x7 & 0x3F)) # SHR operation
    ref_8352 = ref_8345 # MOV operation
    ref_8370 = ref_8352 # MOV operation
    ref_8384 = (ref_8370 >> (0x2 & 0x3F)) # SHR operation
    ref_8513 = ref_8384 # MOV operation
    ref_8527 = (0x7 & ref_8513) # AND operation
    ref_8574 = ref_8527 # MOV operation
    ref_8580 = (0x1 | ref_8574) # OR operation
    ref_9030 = ref_278 # MOV operation
    ref_9062 = ref_9030 # MOV operation
    ref_9076 = ((0x9919884 + ref_9062) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_9114 = ref_9076 # MOV operation
    ref_9126 = ref_8580 # MOV operation
    ref_9128 = (ref_9114 >> ((ref_9126 & 0xFF) & 0x3F)) # SHR operation
    ref_9167 = ref_9128 # MOV operation
    ref_9998 = ref_278 # MOV operation
    ref_10030 = ref_9998 # MOV operation
    ref_10044 = ((0x1E5EA08F8 + ref_10030) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_10084 = ref_10044 # MOV operation
    ref_11562 = ref_9167 # MOV operation
    ref_12184 = ref_9167 # MOV operation
    ref_12202 = ref_12184 # MOV operation
    ref_12216 = (0x3F & ref_12202) # AND operation
    ref_12253 = ref_12216 # MOV operation
    ref_12267 = ((ref_12253 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_12304 = ref_11562 # MOV operation
    ref_12316 = ref_12267 # MOV operation
    ref_12318 = (ref_12316 | ref_12304) # OR operation
    ref_12357 = ref_12318 # MOV operation
    ref_13863 = ref_12357 # MOV operation
    ref_14407 = ref_7555 # MOV operation
    ref_14431 = ref_14407 # MOV operation
    ref_14439 = (ref_14431 >> (0x2 & 0x3F)) # SHR operation
    ref_14446 = ref_14439 # MOV operation
    ref_14550 = ref_14446 # MOV operation
    ref_14564 = (0xF & ref_14550) # AND operation
    ref_14611 = ref_14564 # MOV operation
    ref_14617 = (0x1 | ref_14611) # OR operation
    ref_14988 = ref_6137 # MOV operation
    ref_15012 = ref_14988 # MOV operation
    ref_15016 = ref_14617 # MOV operation
    ref_15018 = (ref_15016 & 0xFFFFFFFF) # MOV operation
    ref_15020 = ((ref_15012 << ((ref_15018 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_15027 = ref_15020 # MOV operation
    ref_15515 = ref_7555 # MOV operation
    ref_15539 = ref_15515 # MOV operation
    ref_15547 = (ref_15539 >> (0x2 & 0x3F)) # SHR operation
    ref_15554 = ref_15547 # MOV operation
    ref_15658 = ref_15554 # MOV operation
    ref_15672 = (0xF & ref_15658) # AND operation
    ref_15719 = ref_15672 # MOV operation
    ref_15725 = (0x1 | ref_15719) # OR operation
    ref_15776 = ref_15725 # MOV operation
    ref_15778 = ((0x40 - ref_15776) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_15786 = ref_15778 # MOV operation
    ref_16152 = ref_6137 # MOV operation
    ref_16176 = ref_16152 # MOV operation
    ref_16180 = ref_15786 # MOV operation
    ref_16182 = (ref_16180 & 0xFFFFFFFF) # MOV operation
    ref_16184 = (ref_16176 >> ((ref_16182 & 0xFF) & 0x3F)) # SHR operation
    ref_16191 = ref_16184 # MOV operation
    ref_16217 = ref_15027 # MOV operation
    ref_16221 = ref_16191 # MOV operation
    ref_16223 = (ref_16221 | ref_16217) # OR operation
    ref_16352 = ref_16223 # MOV operation
    ref_16366 = (0x7 & ref_16352) # AND operation
    ref_16403 = ref_16366 # MOV operation
    ref_16417 = ((ref_16403 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_16454 = ref_13863 # MOV operation
    ref_16466 = ref_16417 # MOV operation
    ref_16468 = (ref_16466 | ref_16454) # OR operation
    ref_16507 = ref_16468 # MOV operation
    ref_22197 = ref_7555 # MOV operation
    ref_22599 = ref_7555 # MOV operation
    ref_22723 = ref_22599 # MOV operation
    ref_22737 = (0xF & ref_22723) # AND operation
    ref_22774 = ref_22737 # MOV operation
    ref_22788 = ((ref_22774 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_22825 = ref_22197 # MOV operation
    ref_22837 = ref_22788 # MOV operation
    ref_22839 = (ref_22837 | ref_22825) # OR operation
    ref_22878 = ref_22839 # MOV operation
    ref_23562 = ref_6137 # MOV operation
    ref_23964 = ref_22878 # MOV operation
    ref_24330 = ref_16507 # MOV operation
    ref_24354 = ref_24330 # MOV operation
    ref_24358 = ref_23964 # MOV operation
    ref_24360 = (ref_24358 & ref_24354) # AND operation
    ref_24469 = ref_24360 # MOV operation
    ref_24483 = (0x1F & ref_24469) # AND operation
    ref_24520 = ref_24483 # MOV operation
    ref_24534 = ((ref_24520 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_24571 = ref_23562 # MOV operation
    ref_24583 = ref_24534 # MOV operation
    ref_24585 = (ref_24583 | ref_24571) # OR operation
    ref_24624 = ref_24585 # MOV operation
    ref_25444 = ref_24624 # MOV operation
    ref_25790 = ref_22878 # MOV operation
    ref_25806 = ref_25444 # MOV operation
    ref_25818 = ref_25790 # MOV operation
    ref_25820 = (ref_25818 | ref_25806) # OR operation
    ref_26171 = ref_16507 # MOV operation
    ref_26537 = ref_10084 # MOV operation
    ref_26553 = ref_26171 # MOV operation
    ref_26565 = ref_26537 # MOV operation
    ref_26567 = (((sx(0x40, ref_26565) * sx(0x40, ref_26553)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_26595 = ref_25820 # MOV operation
    ref_26599 = ref_26567 # MOV operation
    ref_26601 = (((sx(0x40, ref_26599) * sx(0x40, ref_26595)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_26735 = ref_26601 # MOV operation
    ref_26962 = ref_26735 # MOV operation
    ref_26964 = ref_26962 # MOV operation
    endb = ref_26964


else:
    ref_27284 = SymVar_0
    ref_27299 = ref_27284 # MOV operation
    ref_32520 = ref_27299 # MOV operation
    ref_32552 = ref_32520 # MOV operation
    ref_32566 = ((ref_32552 << (0xB & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_32976 = ref_27299 # MOV operation
    ref_33008 = ref_32976 # MOV operation
    ref_33022 = (ref_33008 >> (0x35 & 0x3F)) # SHR operation
    ref_33059 = ref_32566 # MOV operation
    ref_33071 = ref_33022 # MOV operation
    ref_33073 = (ref_33071 | ref_33059) # OR operation
    ref_33110 = ref_33073 # MOV operation
    ref_33124 = (ref_33110 >> (0x1 & 0x3F)) # SHR operation
    ref_33163 = ref_33124 # MOV operation
    ref_33847 = ref_33163 # MOV operation
    ref_33891 = ref_33847 # MOV operation
    ref_33905 = (((sx(0x40, 0x6B33F46) * sx(0x40, ref_33891)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_34442 = ref_27299 # MOV operation
    ref_34484 = ref_34442 # MOV operation
    ref_34492 = ((((0x0) << 64 | ref_34484) / 0x3) & 0xFFFFFFFFFFFFFFFF) # DIV operation
    ref_34525 = ref_34492 # MOV operation
    ref_34537 = ref_33905 # MOV operation
    ref_34539 = ((ref_34525 - ref_34537) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_34547 = ref_34539 # MOV operation
    ref_34581 = ref_34547 # MOV operation
    ref_35339 = ref_34581 # MOV operation
    ref_35363 = ref_35339 # MOV operation
    ref_35371 = (ref_35363 >> (0x7 & 0x3F)) # SHR operation
    ref_35378 = ref_35371 # MOV operation
    ref_35396 = ref_35378 # MOV operation
    ref_35410 = (ref_35396 >> (0x2 & 0x3F)) # SHR operation
    ref_35539 = ref_35410 # MOV operation
    ref_35553 = (0x7 & ref_35539) # AND operation
    ref_35600 = ref_35553 # MOV operation
    ref_35606 = (0x1 | ref_35600) # OR operation
    ref_36056 = ref_27299 # MOV operation
    ref_36088 = ref_36056 # MOV operation
    ref_36102 = ((0x9919884 + ref_36088) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_36140 = ref_36102 # MOV operation
    ref_36152 = ref_35606 # MOV operation
    ref_36154 = (ref_36140 >> ((ref_36152 & 0xFF) & 0x3F)) # SHR operation
    ref_36193 = ref_36154 # MOV operation
    ref_37024 = ref_27299 # MOV operation
    ref_37056 = ref_37024 # MOV operation
    ref_37070 = ((0x1E5EA08F8 + ref_37056) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_37110 = ref_37070 # MOV operation
    ref_38588 = ref_36193 # MOV operation
    ref_39210 = ref_36193 # MOV operation
    ref_39228 = ref_39210 # MOV operation
    ref_39242 = (0x3F & ref_39228) # AND operation
    ref_39279 = ref_39242 # MOV operation
    ref_39293 = ((ref_39279 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_39330 = ref_38588 # MOV operation
    ref_39342 = ref_39293 # MOV operation
    ref_39344 = (ref_39342 | ref_39330) # OR operation
    ref_39383 = ref_39344 # MOV operation
    ref_40889 = ref_39383 # MOV operation
    ref_41433 = ref_34581 # MOV operation
    ref_41457 = ref_41433 # MOV operation
    ref_41465 = (ref_41457 >> (0x2 & 0x3F)) # SHR operation
    ref_41472 = ref_41465 # MOV operation
    ref_41576 = ref_41472 # MOV operation
    ref_41590 = (0xF & ref_41576) # AND operation
    ref_41637 = ref_41590 # MOV operation
    ref_41643 = (0x1 | ref_41637) # OR operation
    ref_42014 = ref_33163 # MOV operation
    ref_42038 = ref_42014 # MOV operation
    ref_42042 = ref_41643 # MOV operation
    ref_42044 = (ref_42042 & 0xFFFFFFFF) # MOV operation
    ref_42046 = ((ref_42038 << ((ref_42044 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_42053 = ref_42046 # MOV operation
    ref_42541 = ref_34581 # MOV operation
    ref_42565 = ref_42541 # MOV operation
    ref_42573 = (ref_42565 >> (0x2 & 0x3F)) # SHR operation
    ref_42580 = ref_42573 # MOV operation
    ref_42684 = ref_42580 # MOV operation
    ref_42698 = (0xF & ref_42684) # AND operation
    ref_42745 = ref_42698 # MOV operation
    ref_42751 = (0x1 | ref_42745) # OR operation
    ref_42802 = ref_42751 # MOV operation
    ref_42804 = ((0x40 - ref_42802) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_42812 = ref_42804 # MOV operation
    ref_43178 = ref_33163 # MOV operation
    ref_43202 = ref_43178 # MOV operation
    ref_43206 = ref_42812 # MOV operation
    ref_43208 = (ref_43206 & 0xFFFFFFFF) # MOV operation
    ref_43210 = (ref_43202 >> ((ref_43208 & 0xFF) & 0x3F)) # SHR operation
    ref_43217 = ref_43210 # MOV operation
    ref_43243 = ref_42053 # MOV operation
    ref_43247 = ref_43217 # MOV operation
    ref_43249 = (ref_43247 | ref_43243) # OR operation
    ref_43378 = ref_43249 # MOV operation
    ref_43392 = (0x7 & ref_43378) # AND operation
    ref_43429 = ref_43392 # MOV operation
    ref_43443 = ((ref_43429 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_43480 = ref_40889 # MOV operation
    ref_43492 = ref_43443 # MOV operation
    ref_43494 = (ref_43492 | ref_43480) # OR operation
    ref_43533 = ref_43494 # MOV operation
    ref_43535 = ((ref_43533 >> 56) & 0xFF) # Byte reference - MOV operation
    ref_43536 = ((ref_43533 >> 48) & 0xFF) # Byte reference - MOV operation
    ref_43537 = ((ref_43533 >> 40) & 0xFF) # Byte reference - MOV operation
    ref_43538 = ((ref_43533 >> 32) & 0xFF) # Byte reference - MOV operation
    ref_43539 = ((ref_43533 >> 24) & 0xFF) # Byte reference - MOV operation
    ref_43540 = ((ref_43533 >> 16) & 0xFF) # Byte reference - MOV operation
    ref_43541 = ((ref_43533 >> 8) & 0xFF) # Byte reference - MOV operation
    ref_43542 = (ref_43533 & 0xFF) # Byte reference - MOV operation
    ref_49174 = ref_37110 # MOV operation
    ref_49198 = ref_49174 # MOV operation
    ref_49206 = (ref_49198 >> (0x3 & 0x3F)) # SHR operation
    ref_49213 = ref_49206 # MOV operation
    ref_49317 = ref_49213 # MOV operation
    ref_49331 = (0xF & ref_49317) # AND operation
    ref_49378 = ref_49331 # MOV operation
    ref_49384 = (0x1 | ref_49378) # OR operation
    ref_49755 = ref_37110 # MOV operation
    ref_49779 = ref_49755 # MOV operation
    ref_49783 = ref_49384 # MOV operation
    ref_49785 = (ref_49783 & 0xFFFFFFFF) # MOV operation
    ref_49787 = ((ref_49779 << ((ref_49785 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_49794 = ref_49787 # MOV operation
    ref_50282 = ref_37110 # MOV operation
    ref_50306 = ref_50282 # MOV operation
    ref_50314 = (ref_50306 >> (0x3 & 0x3F)) # SHR operation
    ref_50321 = ref_50314 # MOV operation
    ref_50425 = ref_50321 # MOV operation
    ref_50439 = (0xF & ref_50425) # AND operation
    ref_50486 = ref_50439 # MOV operation
    ref_50492 = (0x1 | ref_50486) # OR operation
    ref_50543 = ref_50492 # MOV operation
    ref_50545 = ((0x40 - ref_50543) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_50553 = ref_50545 # MOV operation
    ref_50919 = ref_37110 # MOV operation
    ref_50943 = ref_50919 # MOV operation
    ref_50947 = ref_50553 # MOV operation
    ref_50949 = (ref_50947 & 0xFFFFFFFF) # MOV operation
    ref_50951 = (ref_50943 >> ((ref_50949 & 0xFF) & 0x3F)) # SHR operation
    ref_50958 = ref_50951 # MOV operation
    ref_50984 = ref_49794 # MOV operation
    ref_50988 = ref_50958 # MOV operation
    ref_50990 = (ref_50988 | ref_50984) # OR operation
    ref_51127 = ref_50990 # MOV operation
    ref_51575 = ref_43541 # MOVZX operation
    ref_51629 = (ref_51575 & 0xFF) # MOVZX operation
    ref_52239 = ref_43539 # MOVZX operation
    ref_52855 = (ref_52239 & 0xFF) # MOVZX operation
    ref_52857 = (ref_52855 & 0xFF) # Byte reference - MOV operation
    ref_52919 = (ref_51629 & 0xFF) # MOVZX operation
    ref_53535 = (ref_52919 & 0xFF) # MOVZX operation
    ref_53537 = (ref_53535 & 0xFF) # Byte reference - MOV operation
    ref_54367 = ref_51127 # MOV operation
    ref_54713 = ref_34581 # MOV operation
    ref_54729 = ref_54367 # MOV operation
    ref_54741 = ref_54713 # MOV operation
    ref_54743 = (ref_54741 | ref_54729) # OR operation
    ref_55094 = ((((((((ref_43535) << 8 | ref_43536) << 8 | ref_43537) << 8 | ref_43538) << 8 | ref_53537) << 8 | ref_43540) << 8 | ref_52857) << 8 | ref_43542) # MOV operation
    ref_55460 = ref_37110 # MOV operation
    ref_55476 = ref_55094 # MOV operation
    ref_55488 = ref_55460 # MOV operation
    ref_55490 = (((sx(0x40, ref_55488) * sx(0x40, ref_55476)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_55518 = ref_54743 # MOV operation
    ref_55522 = ref_55490 # MOV operation
    ref_55524 = (((sx(0x40, ref_55522) * sx(0x40, ref_55518)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_55658 = ref_55524 # MOV operation
    ref_55885 = ref_55658 # MOV operation
    ref_55887 = ref_55885 # MOV operation
    endb = ref_55887


print(endb & 0xffffffffffffffff)
