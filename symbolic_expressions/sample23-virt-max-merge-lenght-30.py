#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_5463 = ref_278 # MOV operation
ref_5505 = ref_5463 # MOV operation
ref_5511 = ((0x3F22161B + ref_5505) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_5551 = ref_5511 # MOV operation
ref_6113 = ref_5551 # MOV operation
ref_6151 = ref_6113 # MOV operation
ref_6153 = (((sx(0x40, ref_6151) * sx(0x40, 0x378AED0A)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6183 = ref_6153 # MOV operation
ref_6185 = (((sx(0x40, ref_6183) * sx(0x40, 0xDF2B78B)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_6221 = ref_6185 # MOV operation
ref_6235 = (ref_6221 >> (0x1 & 0x3F)) # SHR operation
ref_6258 = ref_6235 # MOV operation
ref_6272 = (0xF & ref_6258) # AND operation
ref_6430 = ref_6272 # MOV operation
ref_6436 = (0x1 | ref_6430) # OR operation
ref_6945 = ref_278 # MOV operation
ref_6977 = ref_6945 # MOV operation
ref_6991 = ((ref_6977 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_7411 = ref_278 # MOV operation
ref_7453 = ref_7411 # MOV operation
ref_7461 = (ref_7453 >> (0x39 & 0x3F)) # SHR operation
ref_7468 = ref_7461 # MOV operation
ref_7500 = ref_6991 # MOV operation
ref_7512 = ref_7468 # MOV operation
ref_7514 = (ref_7512 | ref_7500) # OR operation
ref_7551 = ref_7514 # MOV operation
ref_7563 = ref_6436 # MOV operation
ref_7565 = ((ref_7551 << ((ref_7563 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_8066 = ref_278 # MOV operation
ref_8098 = ref_8066 # MOV operation
ref_8112 = ((ref_8098 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_8577 = ref_278 # MOV operation
ref_8619 = ref_8577 # MOV operation
ref_8627 = (ref_8619 >> (0x39 & 0x3F)) # SHR operation
ref_8634 = ref_8627 # MOV operation
ref_8666 = ref_8112 # MOV operation
ref_8678 = ref_8634 # MOV operation
ref_8680 = (ref_8678 | ref_8666) # OR operation
ref_9011 = ref_5551 # MOV operation
ref_9049 = ref_9011 # MOV operation
ref_9051 = (((sx(0x40, ref_9049) * sx(0x40, 0x378AED0A)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_9081 = ref_9051 # MOV operation
ref_9083 = (((sx(0x40, ref_9081) * sx(0x40, 0xDF2B78B)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_9119 = ref_9083 # MOV operation
ref_9133 = (ref_9119 >> (0x1 & 0x3F)) # SHR operation
ref_9156 = ref_9133 # MOV operation
ref_9170 = (0xF & ref_9156) # AND operation
ref_9217 = ref_9170 # MOV operation
ref_9223 = (0x1 | ref_9217) # OR operation
ref_9274 = ref_9223 # MOV operation
ref_9276 = ((0x40 - ref_9274) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_9284 = ref_9276 # MOV operation
ref_9316 = ref_8680 # MOV operation
ref_9328 = ref_9284 # MOV operation
ref_9330 = (ref_9316 >> ((ref_9328 & 0xFF) & 0x3F)) # SHR operation
ref_9367 = ref_7565 # MOV operation
ref_9379 = ref_9330 # MOV operation
ref_9381 = (ref_9379 | ref_9367) # OR operation
ref_9420 = ref_9381 # MOV operation
ref_10249 = ref_278 # MOV operation
ref_10479 = ref_9420 # MOV operation
ref_10513 = ref_10479 # MOV operation
ref_10527 = ((0xAD6EED + ref_10513) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_10559 = ref_10249 # MOV operation
ref_10563 = ref_10527 # MOV operation
ref_10565 = ((ref_10563 + ref_10559) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_10605 = ref_10565 # MOV operation
ref_11292 = ref_278 # MOV operation
ref_11522 = ref_5551 # MOV operation
ref_11548 = ref_11292 # MOV operation
ref_11552 = ref_11522 # MOV operation
ref_11554 = (ref_11552 | ref_11548) # OR operation
ref_11789 = ref_9420 # MOV operation
ref_11823 = ref_11789 # MOV operation
ref_11837 = ((0x2B6B05ED + ref_11823) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_12117 = ref_10605 # MOV operation
ref_12266 = ref_12117 # MOV operation
ref_12278 = ref_11837 # MOV operation
ref_12280 = (ref_12278 & ref_12266) # AND operation
ref_12317 = ref_11554 # MOV operation
ref_12329 = ref_12280 # MOV operation
ref_12331 = ((ref_12329 + ref_12317) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_12371 = ref_12331 # MOV operation
ref_12881 = ref_12371 # MOV operation
ref_13189 = ref_10605 # MOV operation
ref_13213 = ref_13189 # MOV operation
ref_13219 = (0x3F & ref_13213) # AND operation
ref_13242 = ref_13219 # MOV operation
ref_13256 = ((ref_13242 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_13409 = ref_12881 # MOV operation
ref_13413 = ref_13256 # MOV operation
ref_13415 = (ref_13413 | ref_13409) # OR operation
ref_13454 = ref_13415 # MOV operation
ref_14186 = ref_9420 # MOV operation
ref_14236 = ref_14186 # MOV operation
ref_14250 = (ref_14236 >> (0x4 & 0x3F)) # SHR operation
ref_14279 = ref_14250 # MOV operation
ref_14285 = (0xF & ref_14279) # AND operation
ref_14324 = ref_14285 # MOV operation
ref_14338 = (0x1 | ref_14324) # OR operation
ref_14617 = ref_5551 # MOV operation
ref_14641 = ref_14617 # MOV operation
ref_14645 = ref_14338 # MOV operation
ref_14647 = (ref_14645 & 0xFFFFFFFF) # MOV operation
ref_14649 = ((ref_14641 << ((ref_14647 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_14656 = ref_14649 # MOV operation
ref_15005 = ref_5551 # MOV operation
ref_15297 = ref_9420 # MOV operation
ref_15347 = ref_15297 # MOV operation
ref_15361 = (ref_15347 >> (0x4 & 0x3F)) # SHR operation
ref_15398 = ref_15361 # MOV operation
ref_15412 = (0xF & ref_15398) # AND operation
ref_15467 = ref_15412 # MOV operation
ref_15481 = (0x1 | ref_15467) # OR operation
ref_15548 = ref_15481 # MOV operation
ref_15550 = ((0x40 - ref_15548) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_15558 = ref_15550 # MOV operation
ref_15590 = ref_15005 # MOV operation
ref_15602 = ref_15558 # MOV operation
ref_15604 = (ref_15590 >> ((ref_15602 & 0xFF) & 0x3F)) # SHR operation
ref_15625 = ref_14656 # MOV operation
ref_15637 = ref_15604 # MOV operation
ref_15639 = (ref_15637 | ref_15625) # OR operation
ref_15993 = ref_10605 # MOV operation
ref_16267 = ref_13454 # MOV operation
ref_16299 = ref_15993 # MOV operation
ref_16311 = ref_16267 # MOV operation
ref_16313 = ((ref_16311 + ref_16299) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_16335 = ref_15639 # MOV operation
ref_16347 = ref_16313 # MOV operation
ref_16349 = (((sx(0x40, ref_16347) * sx(0x40, ref_16335)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_16377 = ref_16349 # MOV operation
ref_16656 = ref_16377 # MOV operation
ref_16658 = ref_16656 # MOV operation

print(ref_16658 & 0xffffffffffffffff)
