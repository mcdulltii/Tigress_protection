#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_250 = SymVar_0
ref_261 = ref_250 # MOV operation
ref_273 = ref_261 # MOV operation
ref_275 = ref_273 # MOV operation
ref_309 = ((ref_275 >> 56) & 0xFF) # Byte reference - MOV operation
ref_310 = ((ref_275 >> 48) & 0xFF) # Byte reference - MOV operation
ref_311 = ((ref_275 >> 40) & 0xFF) # Byte reference - MOV operation
ref_312 = ((ref_275 >> 32) & 0xFF) # Byte reference - MOV operation
ref_313 = ((ref_275 >> 24) & 0xFF) # Byte reference - MOV operation
ref_314 = ((ref_275 >> 16) & 0xFF) # Byte reference - MOV operation
ref_315 = ((ref_275 >> 8) & 0xFF) # Byte reference - MOV operation
ref_316 = (ref_275 & 0xFF) # Byte reference - MOV operation
ref_2309623 = ref_316 # MOVZX operation
ref_2373612 = (ref_2309623 & 0xFF) # MOVZX operation
ref_2373614 = (ref_2373612 & 0xFF) # MOVZX operation
ref_2565667 = (ref_2373614 & 0xFFFFFFFF) # MOV operation
ref_2565669 = (((ref_2565667 & 0xFFFFFFFF) + 0x1) & 0xFFFFFFFF) # ADD operation
ref_2821736 = (ref_2565669 & 0xFFFFFFFF) # MOV operation
ref_2821745 = ((((0x0) << 32 | (ref_2821736 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_2821747 = (ref_2821745 & 0xFFFFFFFF) # MOV operation
ref_2885770 = (ref_2821747 & 0xFFFFFFFF) # MOV operation
ref_3077887 = (ref_2885770 & 0xFFFFFFFF) # MOV operation
ref_3269940 = (ref_3077887 & 0xFFFFFFFF) # MOV operation
ref_3269942 = (((ref_3269940 & 0xFFFFFFFF) + 0x0) & 0xFFFFFFFF) # ADD operation
ref_3526009 = (ref_3269942 & 0xFFFFFFFF) # MOV operation
ref_3526018 = ((((0x0) << 32 | (ref_3526009 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_3526020 = (ref_3526018 & 0xFFFFFFFF) # MOV operation
ref_3590043 = (ref_3526020 & 0xFFFFFFFF) # MOV operation
ref_5062711 = ref_315 # MOVZX operation
ref_5126700 = (ref_5062711 & 0xFF) # MOVZX operation
ref_5126702 = (ref_5126700 & 0xFF) # MOVZX operation
ref_5254748 = (ref_2885770 & 0xFFFFFFFF) # MOV operation
ref_5318743 = (ref_5254748 & 0xFFFFFFFF) # MOV operation
ref_5318755 = (ref_5126702 & 0xFFFFFFFF) # MOV operation
ref_5318757 = (((ref_5318755 & 0xFFFFFFFF) + (ref_5318743 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_5574824 = (ref_5318757 & 0xFFFFFFFF) # MOV operation
ref_5574833 = ((((0x0) << 32 | (ref_5574824 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_5574835 = (ref_5574833 & 0xFFFFFFFF) # MOV operation
ref_5638858 = (ref_5574835 & 0xFFFFFFFF) # MOV operation
ref_5830975 = (ref_5638858 & 0xFFFFFFFF) # MOV operation
ref_5959021 = (ref_3590043 & 0xFFFFFFFF) # MOV operation
ref_6023016 = (ref_5959021 & 0xFFFFFFFF) # MOV operation
ref_6023028 = (ref_5830975 & 0xFFFFFFFF) # MOV operation
ref_6023030 = (((ref_6023028 & 0xFFFFFFFF) + (ref_6023016 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_6279097 = (ref_6023030 & 0xFFFFFFFF) # MOV operation
ref_6279106 = ((((0x0) << 32 | (ref_6279097 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_6279108 = (ref_6279106 & 0xFFFFFFFF) # MOV operation
ref_6343131 = (ref_6279108 & 0xFFFFFFFF) # MOV operation
ref_7815799 = ref_314 # MOVZX operation
ref_7879788 = (ref_7815799 & 0xFF) # MOVZX operation
ref_7879790 = (ref_7879788 & 0xFF) # MOVZX operation
ref_8007836 = (ref_5638858 & 0xFFFFFFFF) # MOV operation
ref_8071831 = (ref_8007836 & 0xFFFFFFFF) # MOV operation
ref_8071843 = (ref_7879790 & 0xFFFFFFFF) # MOV operation
ref_8071845 = (((ref_8071843 & 0xFFFFFFFF) + (ref_8071831 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_8327912 = (ref_8071845 & 0xFFFFFFFF) # MOV operation
ref_8327921 = ((((0x0) << 32 | (ref_8327912 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_8327923 = (ref_8327921 & 0xFFFFFFFF) # MOV operation
ref_8391946 = (ref_8327923 & 0xFFFFFFFF) # MOV operation
ref_8584063 = (ref_8391946 & 0xFFFFFFFF) # MOV operation
ref_8712109 = (ref_6343131 & 0xFFFFFFFF) # MOV operation
ref_8776104 = (ref_8712109 & 0xFFFFFFFF) # MOV operation
ref_8776116 = (ref_8584063 & 0xFFFFFFFF) # MOV operation
ref_8776118 = (((ref_8776116 & 0xFFFFFFFF) + (ref_8776104 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_9032185 = (ref_8776118 & 0xFFFFFFFF) # MOV operation
ref_9032194 = ((((0x0) << 32 | (ref_9032185 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_9032196 = (ref_9032194 & 0xFFFFFFFF) # MOV operation
ref_9096219 = (ref_9032196 & 0xFFFFFFFF) # MOV operation
ref_10568887 = ref_313 # MOVZX operation
ref_10632876 = (ref_10568887 & 0xFF) # MOVZX operation
ref_10632878 = (ref_10632876 & 0xFF) # MOVZX operation
ref_10760924 = (ref_8391946 & 0xFFFFFFFF) # MOV operation
ref_10824919 = (ref_10760924 & 0xFFFFFFFF) # MOV operation
ref_10824931 = (ref_10632878 & 0xFFFFFFFF) # MOV operation
ref_10824933 = (((ref_10824931 & 0xFFFFFFFF) + (ref_10824919 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_11081000 = (ref_10824933 & 0xFFFFFFFF) # MOV operation
ref_11081009 = ((((0x0) << 32 | (ref_11081000 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_11081011 = (ref_11081009 & 0xFFFFFFFF) # MOV operation
ref_11145034 = (ref_11081011 & 0xFFFFFFFF) # MOV operation
ref_11337151 = (ref_11145034 & 0xFFFFFFFF) # MOV operation
ref_11465197 = (ref_9096219 & 0xFFFFFFFF) # MOV operation
ref_11529192 = (ref_11465197 & 0xFFFFFFFF) # MOV operation
ref_11529204 = (ref_11337151 & 0xFFFFFFFF) # MOV operation
ref_11529206 = (((ref_11529204 & 0xFFFFFFFF) + (ref_11529192 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_11785273 = (ref_11529206 & 0xFFFFFFFF) # MOV operation
ref_11785282 = ((((0x0) << 32 | (ref_11785273 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_11785284 = (ref_11785282 & 0xFFFFFFFF) # MOV operation
ref_11849307 = (ref_11785284 & 0xFFFFFFFF) # MOV operation
ref_13321975 = ref_312 # MOVZX operation
ref_13385964 = (ref_13321975 & 0xFF) # MOVZX operation
ref_13385966 = (ref_13385964 & 0xFF) # MOVZX operation
ref_13514012 = (ref_11145034 & 0xFFFFFFFF) # MOV operation
ref_13578007 = (ref_13514012 & 0xFFFFFFFF) # MOV operation
ref_13578019 = (ref_13385966 & 0xFFFFFFFF) # MOV operation
ref_13578021 = (((ref_13578019 & 0xFFFFFFFF) + (ref_13578007 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_13834088 = (ref_13578021 & 0xFFFFFFFF) # MOV operation
ref_13834097 = ((((0x0) << 32 | (ref_13834088 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_13834099 = (ref_13834097 & 0xFFFFFFFF) # MOV operation
ref_13898122 = (ref_13834099 & 0xFFFFFFFF) # MOV operation
ref_14090239 = (ref_13898122 & 0xFFFFFFFF) # MOV operation
ref_14218285 = (ref_11849307 & 0xFFFFFFFF) # MOV operation
ref_14282280 = (ref_14218285 & 0xFFFFFFFF) # MOV operation
ref_14282292 = (ref_14090239 & 0xFFFFFFFF) # MOV operation
ref_14282294 = (((ref_14282292 & 0xFFFFFFFF) + (ref_14282280 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_14538361 = (ref_14282294 & 0xFFFFFFFF) # MOV operation
ref_14538370 = ((((0x0) << 32 | (ref_14538361 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_14538372 = (ref_14538370 & 0xFFFFFFFF) # MOV operation
ref_14602395 = (ref_14538372 & 0xFFFFFFFF) # MOV operation
ref_16075063 = ref_311 # MOVZX operation
ref_16139052 = (ref_16075063 & 0xFF) # MOVZX operation
ref_16139054 = (ref_16139052 & 0xFF) # MOVZX operation
ref_16267100 = (ref_13898122 & 0xFFFFFFFF) # MOV operation
ref_16331095 = (ref_16267100 & 0xFFFFFFFF) # MOV operation
ref_16331107 = (ref_16139054 & 0xFFFFFFFF) # MOV operation
ref_16331109 = (((ref_16331107 & 0xFFFFFFFF) + (ref_16331095 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_16587176 = (ref_16331109 & 0xFFFFFFFF) # MOV operation
ref_16587185 = ((((0x0) << 32 | (ref_16587176 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_16587187 = (ref_16587185 & 0xFFFFFFFF) # MOV operation
ref_16651210 = (ref_16587187 & 0xFFFFFFFF) # MOV operation
ref_16843327 = (ref_16651210 & 0xFFFFFFFF) # MOV operation
ref_16971373 = (ref_14602395 & 0xFFFFFFFF) # MOV operation
ref_17035368 = (ref_16971373 & 0xFFFFFFFF) # MOV operation
ref_17035380 = (ref_16843327 & 0xFFFFFFFF) # MOV operation
ref_17035382 = (((ref_17035380 & 0xFFFFFFFF) + (ref_17035368 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_17291449 = (ref_17035382 & 0xFFFFFFFF) # MOV operation
ref_17291458 = ((((0x0) << 32 | (ref_17291449 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_17291460 = (ref_17291458 & 0xFFFFFFFF) # MOV operation
ref_17355483 = (ref_17291460 & 0xFFFFFFFF) # MOV operation
ref_18828151 = ref_310 # MOVZX operation
ref_18892140 = (ref_18828151 & 0xFF) # MOVZX operation
ref_18892142 = (ref_18892140 & 0xFF) # MOVZX operation
ref_19020188 = (ref_16651210 & 0xFFFFFFFF) # MOV operation
ref_19084183 = (ref_19020188 & 0xFFFFFFFF) # MOV operation
ref_19084195 = (ref_18892142 & 0xFFFFFFFF) # MOV operation
ref_19084197 = (((ref_19084195 & 0xFFFFFFFF) + (ref_19084183 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_19340264 = (ref_19084197 & 0xFFFFFFFF) # MOV operation
ref_19340273 = ((((0x0) << 32 | (ref_19340264 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_19340275 = (ref_19340273 & 0xFFFFFFFF) # MOV operation
ref_19404298 = (ref_19340275 & 0xFFFFFFFF) # MOV operation
ref_19596415 = (ref_19404298 & 0xFFFFFFFF) # MOV operation
ref_19724461 = (ref_17355483 & 0xFFFFFFFF) # MOV operation
ref_19788456 = (ref_19724461 & 0xFFFFFFFF) # MOV operation
ref_19788468 = (ref_19596415 & 0xFFFFFFFF) # MOV operation
ref_19788470 = (((ref_19788468 & 0xFFFFFFFF) + (ref_19788456 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_20044537 = (ref_19788470 & 0xFFFFFFFF) # MOV operation
ref_20044546 = ((((0x0) << 32 | (ref_20044537 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_20044548 = (ref_20044546 & 0xFFFFFFFF) # MOV operation
ref_20108571 = (ref_20044548 & 0xFFFFFFFF) # MOV operation
ref_21581239 = ref_309 # MOVZX operation
ref_21645228 = (ref_21581239 & 0xFF) # MOVZX operation
ref_21645230 = (ref_21645228 & 0xFF) # MOVZX operation
ref_21773276 = (ref_19404298 & 0xFFFFFFFF) # MOV operation
ref_21837271 = (ref_21773276 & 0xFFFFFFFF) # MOV operation
ref_21837283 = (ref_21645230 & 0xFFFFFFFF) # MOV operation
ref_21837285 = (((ref_21837283 & 0xFFFFFFFF) + (ref_21837271 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_22093352 = (ref_21837285 & 0xFFFFFFFF) # MOV operation
ref_22093361 = ((((0x0) << 32 | (ref_22093352 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_22093363 = (ref_22093361 & 0xFFFFFFFF) # MOV operation
ref_22157386 = (ref_22093363 & 0xFFFFFFFF) # MOV operation
ref_22349503 = (ref_22157386 & 0xFFFFFFFF) # MOV operation
ref_22477549 = (ref_20108571 & 0xFFFFFFFF) # MOV operation
ref_22541544 = (ref_22477549 & 0xFFFFFFFF) # MOV operation
ref_22541556 = (ref_22349503 & 0xFFFFFFFF) # MOV operation
ref_22541558 = (((ref_22541556 & 0xFFFFFFFF) + (ref_22541544 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_22797625 = (ref_22541558 & 0xFFFFFFFF) # MOV operation
ref_22797634 = ((((0x0) << 32 | (ref_22797625 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_22797636 = (ref_22797634 & 0xFFFFFFFF) # MOV operation
ref_22861659 = (ref_22797636 & 0xFFFFFFFF) # MOV operation
ref_24014175 = (ref_22861659 & 0xFFFFFFFF) # MOV operation
ref_24142213 = (ref_24014175 & 0xFFFFFFFF) # MOV operation
ref_24142221 = (((ref_24142213 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_24142228 = (ref_24142221 & 0xFFFFFFFF) # MOV operation
ref_24270294 = (ref_22157386 & 0xFFFFFFFF) # MOV operation
ref_24334297 = (ref_24142228 & 0xFFFFFFFF) # MOV operation
ref_24334301 = (ref_24270294 & 0xFFFFFFFF) # MOV operation
ref_24334303 = ((ref_24334301 & 0xFFFFFFFF) | (ref_24334297 & 0xFFFFFFFF)) # OR operation
ref_24398331 = (ref_24334303 & 0xFFFFFFFF) # MOV operation
ref_24590404 = (ref_24398331 & 0xFFFFFFFF) # MOV operation
ref_24654395 = (ref_24590404 & 0xFFFFFFFF) # MOV operation
ref_24654419 = (ref_24654395 & 0xFFFFFFFF) # MOV operation
ref_24654427 = (ref_24654419 & 0xFFFFFFFF) # MOV operation
ref_24654429 = (ref_24654427 & 0xFFFFFFFF) # MOV operation

print(ref_24654429 & 0xffffffffffffffff)
