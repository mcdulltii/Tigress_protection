#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_214 = SymVar_0
ref_225 = ref_214 # MOV operation
ref_237 = ref_225 # MOV operation
ref_239 = ref_237 # MOV operation
ref_273 = ((ref_239 >> 56) & 0xFF) # Byte reference - MOV operation
ref_274 = ((ref_239 >> 48) & 0xFF) # Byte reference - MOV operation
ref_275 = ((ref_239 >> 40) & 0xFF) # Byte reference - MOV operation
ref_276 = ((ref_239 >> 32) & 0xFF) # Byte reference - MOV operation
ref_277 = ((ref_239 >> 24) & 0xFF) # Byte reference - MOV operation
ref_278 = ((ref_239 >> 16) & 0xFF) # Byte reference - MOV operation
ref_279 = ((ref_239 >> 8) & 0xFF) # Byte reference - MOV operation
ref_280 = (ref_239 & 0xFF) # Byte reference - MOV operation
ref_6877 = ref_280 # MOVZX operation
ref_6895 = (ref_6877 & 0xFF) # MOVZX operation
ref_6897 = (ref_6895 & 0xFF) # MOVZX operation
ref_6937 = (ref_6897 & 0xFFFFFFFF) # MOV operation
ref_6939 = (((ref_6937 & 0xFFFFFFFF) + 0x0) & 0xFFFFFFFF) # ADD operation
ref_6975 = (ref_6939 & 0xFFFFFFFF) # MOV operation
ref_7073 = (ref_6975 & 0xFFFFFFFF) # MOV operation
ref_7141 = (ref_6975 & 0xFFFFFFFF) # MOV operation
ref_7298 = (ref_7141 & 0xFFFFFFFF) # MOV operation
ref_7314 = (((ref_7298 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_7321 = (ref_7314 & 0xFFFFFFFF) # MOV operation
ref_7343 = (ref_7073 & 0xFFFFFFFF) # MOV operation
ref_7347 = (ref_7321 & 0xFFFFFFFF) # MOV operation
ref_7349 = (((ref_7347 & 0xFFFFFFFF) + (ref_7343 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_7385 = (ref_7349 & 0xFFFFFFFF) # MOV operation
ref_7497 = (ref_7385 & 0xFFFFFFFF) # MOV operation
ref_7531 = (ref_7497 & 0xFFFFFFFF) # MOV operation
ref_7539 = ((ref_7531 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_7546 = (ref_7539 & 0xFFFFFFFF) # MOV operation
ref_7689 = (ref_7385 & 0xFFFFFFFF) # MOV operation
ref_7703 = (ref_7689 & 0xFFFFFFFF) # MOV operation
ref_7715 = (ref_7546 & 0xFFFFFFFF) # MOV operation
ref_7717 = ((ref_7715 & 0xFFFFFFFF) ^ (ref_7703 & 0xFFFFFFFF)) # XOR operation
ref_7752 = (ref_7717 & 0xFFFFFFFF) # MOV operation
ref_8821 = (ref_7752 & 0xFFFFFFFF) # MOV operation
ref_9235 = ref_279 # MOVZX operation
ref_9253 = (ref_9235 & 0xFF) # MOVZX operation
ref_9255 = (ref_9253 & 0xFF) # MOVZX operation
ref_9283 = (ref_8821 & 0xFFFFFFFF) # MOV operation
ref_9295 = (ref_9255 & 0xFFFFFFFF) # MOV operation
ref_9297 = (((ref_9295 & 0xFFFFFFFF) + (ref_9283 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_9333 = (ref_9297 & 0xFFFFFFFF) # MOV operation
ref_9431 = (ref_9333 & 0xFFFFFFFF) # MOV operation
ref_9499 = (ref_9333 & 0xFFFFFFFF) # MOV operation
ref_9656 = (ref_9499 & 0xFFFFFFFF) # MOV operation
ref_9672 = (((ref_9656 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_9679 = (ref_9672 & 0xFFFFFFFF) # MOV operation
ref_9701 = (ref_9431 & 0xFFFFFFFF) # MOV operation
ref_9705 = (ref_9679 & 0xFFFFFFFF) # MOV operation
ref_9707 = (((ref_9705 & 0xFFFFFFFF) + (ref_9701 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_9743 = (ref_9707 & 0xFFFFFFFF) # MOV operation
ref_9855 = (ref_9743 & 0xFFFFFFFF) # MOV operation
ref_9889 = (ref_9855 & 0xFFFFFFFF) # MOV operation
ref_9897 = ((ref_9889 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_9904 = (ref_9897 & 0xFFFFFFFF) # MOV operation
ref_10047 = (ref_9743 & 0xFFFFFFFF) # MOV operation
ref_10061 = (ref_10047 & 0xFFFFFFFF) # MOV operation
ref_10073 = (ref_9904 & 0xFFFFFFFF) # MOV operation
ref_10075 = ((ref_10073 & 0xFFFFFFFF) ^ (ref_10061 & 0xFFFFFFFF)) # XOR operation
ref_10110 = (ref_10075 & 0xFFFFFFFF) # MOV operation
ref_11179 = (ref_10110 & 0xFFFFFFFF) # MOV operation
ref_11593 = ref_278 # MOVZX operation
ref_11611 = (ref_11593 & 0xFF) # MOVZX operation
ref_11613 = (ref_11611 & 0xFF) # MOVZX operation
ref_11641 = (ref_11179 & 0xFFFFFFFF) # MOV operation
ref_11653 = (ref_11613 & 0xFFFFFFFF) # MOV operation
ref_11655 = (((ref_11653 & 0xFFFFFFFF) + (ref_11641 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_11691 = (ref_11655 & 0xFFFFFFFF) # MOV operation
ref_11789 = (ref_11691 & 0xFFFFFFFF) # MOV operation
ref_11857 = (ref_11691 & 0xFFFFFFFF) # MOV operation
ref_12014 = (ref_11857 & 0xFFFFFFFF) # MOV operation
ref_12030 = (((ref_12014 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_12037 = (ref_12030 & 0xFFFFFFFF) # MOV operation
ref_12059 = (ref_11789 & 0xFFFFFFFF) # MOV operation
ref_12063 = (ref_12037 & 0xFFFFFFFF) # MOV operation
ref_12065 = (((ref_12063 & 0xFFFFFFFF) + (ref_12059 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_12101 = (ref_12065 & 0xFFFFFFFF) # MOV operation
ref_12213 = (ref_12101 & 0xFFFFFFFF) # MOV operation
ref_12247 = (ref_12213 & 0xFFFFFFFF) # MOV operation
ref_12255 = ((ref_12247 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_12262 = (ref_12255 & 0xFFFFFFFF) # MOV operation
ref_12405 = (ref_12101 & 0xFFFFFFFF) # MOV operation
ref_12419 = (ref_12405 & 0xFFFFFFFF) # MOV operation
ref_12431 = (ref_12262 & 0xFFFFFFFF) # MOV operation
ref_12433 = ((ref_12431 & 0xFFFFFFFF) ^ (ref_12419 & 0xFFFFFFFF)) # XOR operation
ref_12468 = (ref_12433 & 0xFFFFFFFF) # MOV operation
ref_13537 = (ref_12468 & 0xFFFFFFFF) # MOV operation
ref_13951 = ref_277 # MOVZX operation
ref_13969 = (ref_13951 & 0xFF) # MOVZX operation
ref_13971 = (ref_13969 & 0xFF) # MOVZX operation
ref_13999 = (ref_13537 & 0xFFFFFFFF) # MOV operation
ref_14011 = (ref_13971 & 0xFFFFFFFF) # MOV operation
ref_14013 = (((ref_14011 & 0xFFFFFFFF) + (ref_13999 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_14049 = (ref_14013 & 0xFFFFFFFF) # MOV operation
ref_14147 = (ref_14049 & 0xFFFFFFFF) # MOV operation
ref_14215 = (ref_14049 & 0xFFFFFFFF) # MOV operation
ref_14372 = (ref_14215 & 0xFFFFFFFF) # MOV operation
ref_14388 = (((ref_14372 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_14395 = (ref_14388 & 0xFFFFFFFF) # MOV operation
ref_14417 = (ref_14147 & 0xFFFFFFFF) # MOV operation
ref_14421 = (ref_14395 & 0xFFFFFFFF) # MOV operation
ref_14423 = (((ref_14421 & 0xFFFFFFFF) + (ref_14417 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_14459 = (ref_14423 & 0xFFFFFFFF) # MOV operation
ref_14571 = (ref_14459 & 0xFFFFFFFF) # MOV operation
ref_14605 = (ref_14571 & 0xFFFFFFFF) # MOV operation
ref_14613 = ((ref_14605 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_14620 = (ref_14613 & 0xFFFFFFFF) # MOV operation
ref_14763 = (ref_14459 & 0xFFFFFFFF) # MOV operation
ref_14777 = (ref_14763 & 0xFFFFFFFF) # MOV operation
ref_14789 = (ref_14620 & 0xFFFFFFFF) # MOV operation
ref_14791 = ((ref_14789 & 0xFFFFFFFF) ^ (ref_14777 & 0xFFFFFFFF)) # XOR operation
ref_14826 = (ref_14791 & 0xFFFFFFFF) # MOV operation
ref_15895 = (ref_14826 & 0xFFFFFFFF) # MOV operation
ref_16309 = ref_276 # MOVZX operation
ref_16327 = (ref_16309 & 0xFF) # MOVZX operation
ref_16329 = (ref_16327 & 0xFF) # MOVZX operation
ref_16357 = (ref_15895 & 0xFFFFFFFF) # MOV operation
ref_16369 = (ref_16329 & 0xFFFFFFFF) # MOV operation
ref_16371 = (((ref_16369 & 0xFFFFFFFF) + (ref_16357 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_16407 = (ref_16371 & 0xFFFFFFFF) # MOV operation
ref_16505 = (ref_16407 & 0xFFFFFFFF) # MOV operation
ref_16573 = (ref_16407 & 0xFFFFFFFF) # MOV operation
ref_16730 = (ref_16573 & 0xFFFFFFFF) # MOV operation
ref_16746 = (((ref_16730 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_16753 = (ref_16746 & 0xFFFFFFFF) # MOV operation
ref_16775 = (ref_16505 & 0xFFFFFFFF) # MOV operation
ref_16779 = (ref_16753 & 0xFFFFFFFF) # MOV operation
ref_16781 = (((ref_16779 & 0xFFFFFFFF) + (ref_16775 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_16817 = (ref_16781 & 0xFFFFFFFF) # MOV operation
ref_16929 = (ref_16817 & 0xFFFFFFFF) # MOV operation
ref_16963 = (ref_16929 & 0xFFFFFFFF) # MOV operation
ref_16971 = ((ref_16963 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_16978 = (ref_16971 & 0xFFFFFFFF) # MOV operation
ref_17121 = (ref_16817 & 0xFFFFFFFF) # MOV operation
ref_17135 = (ref_17121 & 0xFFFFFFFF) # MOV operation
ref_17147 = (ref_16978 & 0xFFFFFFFF) # MOV operation
ref_17149 = ((ref_17147 & 0xFFFFFFFF) ^ (ref_17135 & 0xFFFFFFFF)) # XOR operation
ref_17184 = (ref_17149 & 0xFFFFFFFF) # MOV operation
ref_18253 = (ref_17184 & 0xFFFFFFFF) # MOV operation
ref_18667 = ref_275 # MOVZX operation
ref_18685 = (ref_18667 & 0xFF) # MOVZX operation
ref_18687 = (ref_18685 & 0xFF) # MOVZX operation
ref_18715 = (ref_18253 & 0xFFFFFFFF) # MOV operation
ref_18727 = (ref_18687 & 0xFFFFFFFF) # MOV operation
ref_18729 = (((ref_18727 & 0xFFFFFFFF) + (ref_18715 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_18765 = (ref_18729 & 0xFFFFFFFF) # MOV operation
ref_18863 = (ref_18765 & 0xFFFFFFFF) # MOV operation
ref_18931 = (ref_18765 & 0xFFFFFFFF) # MOV operation
ref_19088 = (ref_18931 & 0xFFFFFFFF) # MOV operation
ref_19104 = (((ref_19088 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_19111 = (ref_19104 & 0xFFFFFFFF) # MOV operation
ref_19133 = (ref_18863 & 0xFFFFFFFF) # MOV operation
ref_19137 = (ref_19111 & 0xFFFFFFFF) # MOV operation
ref_19139 = (((ref_19137 & 0xFFFFFFFF) + (ref_19133 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_19175 = (ref_19139 & 0xFFFFFFFF) # MOV operation
ref_19287 = (ref_19175 & 0xFFFFFFFF) # MOV operation
ref_19321 = (ref_19287 & 0xFFFFFFFF) # MOV operation
ref_19329 = ((ref_19321 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_19336 = (ref_19329 & 0xFFFFFFFF) # MOV operation
ref_19479 = (ref_19175 & 0xFFFFFFFF) # MOV operation
ref_19493 = (ref_19479 & 0xFFFFFFFF) # MOV operation
ref_19505 = (ref_19336 & 0xFFFFFFFF) # MOV operation
ref_19507 = ((ref_19505 & 0xFFFFFFFF) ^ (ref_19493 & 0xFFFFFFFF)) # XOR operation
ref_19542 = (ref_19507 & 0xFFFFFFFF) # MOV operation
ref_20611 = (ref_19542 & 0xFFFFFFFF) # MOV operation
ref_21025 = ref_274 # MOVZX operation
ref_21043 = (ref_21025 & 0xFF) # MOVZX operation
ref_21045 = (ref_21043 & 0xFF) # MOVZX operation
ref_21073 = (ref_20611 & 0xFFFFFFFF) # MOV operation
ref_21085 = (ref_21045 & 0xFFFFFFFF) # MOV operation
ref_21087 = (((ref_21085 & 0xFFFFFFFF) + (ref_21073 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_21123 = (ref_21087 & 0xFFFFFFFF) # MOV operation
ref_21221 = (ref_21123 & 0xFFFFFFFF) # MOV operation
ref_21289 = (ref_21123 & 0xFFFFFFFF) # MOV operation
ref_21446 = (ref_21289 & 0xFFFFFFFF) # MOV operation
ref_21462 = (((ref_21446 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_21469 = (ref_21462 & 0xFFFFFFFF) # MOV operation
ref_21491 = (ref_21221 & 0xFFFFFFFF) # MOV operation
ref_21495 = (ref_21469 & 0xFFFFFFFF) # MOV operation
ref_21497 = (((ref_21495 & 0xFFFFFFFF) + (ref_21491 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_21533 = (ref_21497 & 0xFFFFFFFF) # MOV operation
ref_21645 = (ref_21533 & 0xFFFFFFFF) # MOV operation
ref_21679 = (ref_21645 & 0xFFFFFFFF) # MOV operation
ref_21687 = ((ref_21679 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_21694 = (ref_21687 & 0xFFFFFFFF) # MOV operation
ref_21837 = (ref_21533 & 0xFFFFFFFF) # MOV operation
ref_21851 = (ref_21837 & 0xFFFFFFFF) # MOV operation
ref_21863 = (ref_21694 & 0xFFFFFFFF) # MOV operation
ref_21865 = ((ref_21863 & 0xFFFFFFFF) ^ (ref_21851 & 0xFFFFFFFF)) # XOR operation
ref_21900 = (ref_21865 & 0xFFFFFFFF) # MOV operation
ref_22969 = (ref_21900 & 0xFFFFFFFF) # MOV operation
ref_23383 = ref_273 # MOVZX operation
ref_23401 = (ref_23383 & 0xFF) # MOVZX operation
ref_23403 = (ref_23401 & 0xFF) # MOVZX operation
ref_23431 = (ref_22969 & 0xFFFFFFFF) # MOV operation
ref_23443 = (ref_23403 & 0xFFFFFFFF) # MOV operation
ref_23445 = (((ref_23443 & 0xFFFFFFFF) + (ref_23431 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_23481 = (ref_23445 & 0xFFFFFFFF) # MOV operation
ref_23579 = (ref_23481 & 0xFFFFFFFF) # MOV operation
ref_23647 = (ref_23481 & 0xFFFFFFFF) # MOV operation
ref_23804 = (ref_23647 & 0xFFFFFFFF) # MOV operation
ref_23820 = (((ref_23804 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_23827 = (ref_23820 & 0xFFFFFFFF) # MOV operation
ref_23849 = (ref_23579 & 0xFFFFFFFF) # MOV operation
ref_23853 = (ref_23827 & 0xFFFFFFFF) # MOV operation
ref_23855 = (((ref_23853 & 0xFFFFFFFF) + (ref_23849 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_23891 = (ref_23855 & 0xFFFFFFFF) # MOV operation
ref_24003 = (ref_23891 & 0xFFFFFFFF) # MOV operation
ref_24037 = (ref_24003 & 0xFFFFFFFF) # MOV operation
ref_24045 = ((ref_24037 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_24052 = (ref_24045 & 0xFFFFFFFF) # MOV operation
ref_24195 = (ref_23891 & 0xFFFFFFFF) # MOV operation
ref_24209 = (ref_24195 & 0xFFFFFFFF) # MOV operation
ref_24221 = (ref_24052 & 0xFFFFFFFF) # MOV operation
ref_24223 = ((ref_24221 & 0xFFFFFFFF) ^ (ref_24209 & 0xFFFFFFFF)) # XOR operation
ref_24258 = (ref_24223 & 0xFFFFFFFF) # MOV operation
ref_25089 = (ref_24258 & 0xFFFFFFFF) # MOV operation
ref_25157 = (ref_24258 & 0xFFFFFFFF) # MOV operation
ref_25314 = (ref_25157 & 0xFFFFFFFF) # MOV operation
ref_25330 = (((ref_25314 & 0xFFFFFFFF) << (0x3 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_25337 = (ref_25330 & 0xFFFFFFFF) # MOV operation
ref_25359 = (ref_25089 & 0xFFFFFFFF) # MOV operation
ref_25363 = (ref_25337 & 0xFFFFFFFF) # MOV operation
ref_25365 = (((ref_25363 & 0xFFFFFFFF) + (ref_25359 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_25401 = (ref_25365 & 0xFFFFFFFF) # MOV operation
ref_25513 = (ref_25401 & 0xFFFFFFFF) # MOV operation
ref_25547 = (ref_25513 & 0xFFFFFFFF) # MOV operation
ref_25555 = ((ref_25547 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_25562 = (ref_25555 & 0xFFFFFFFF) # MOV operation
ref_25705 = (ref_25401 & 0xFFFFFFFF) # MOV operation
ref_25719 = (ref_25705 & 0xFFFFFFFF) # MOV operation
ref_25731 = (ref_25562 & 0xFFFFFFFF) # MOV operation
ref_25733 = ((ref_25731 & 0xFFFFFFFF) ^ (ref_25719 & 0xFFFFFFFF)) # XOR operation
ref_25768 = (ref_25733 & 0xFFFFFFFF) # MOV operation
ref_25866 = (ref_25768 & 0xFFFFFFFF) # MOV operation
ref_25916 = (ref_25768 & 0xFFFFFFFF) # MOV operation
ref_26017 = (ref_25916 & 0xFFFFFFFF) # MOV operation
ref_26033 = (((ref_26017 & 0xFFFFFFFF) << (0xF & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_26040 = (ref_26033 & 0xFFFFFFFF) # MOV operation
ref_26062 = (ref_25866 & 0xFFFFFFFF) # MOV operation
ref_26066 = (ref_26040 & 0xFFFFFFFF) # MOV operation
ref_26068 = (((ref_26066 & 0xFFFFFFFF) + (ref_26062 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_26104 = (ref_26068 & 0xFFFFFFFF) # MOV operation
ref_26379 = (ref_26104 & 0xFFFFFFFF) # MOV operation
ref_26520 = (ref_26379 & 0xFFFFFFFF) # MOV operation
ref_26544 = (ref_26520 & 0xFFFFFFFF) # MOV operation
ref_26552 = (ref_26544 & 0xFFFFFFFF) # MOV operation
ref_26554 = (ref_26552 & 0xFFFFFFFF) # MOV operation

print(ref_26554 & 0xffffffffffffffff)
