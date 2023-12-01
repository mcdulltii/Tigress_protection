#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_10006 = ref_278 # MOV operation
ref_10584 = ref_10006 # MOV operation
ref_10602 = (ref_10584 >> (0x33 & 0x3F)) # SHR operation
ref_10609 = ref_10602 # MOV operation
ref_15828 = ref_278 # MOV operation
ref_17030 = ref_15828 # MOV operation
ref_17040 = ((ref_17030 << (0xD & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_17047 = ref_17040 # MOV operation
ref_17661 = ref_17047 # MOV operation
ref_17675 = ref_10609 # MOV operation
ref_17677 = (ref_17675 | ref_17661) # OR operation
ref_22642 = ref_17677 # MOV operation
ref_28398 = ref_278 # MOV operation
ref_29519 = ref_28398 # MOV operation
ref_29529 = ((((0x0) << 64 | ref_29519) / 0x6) & 0xFFFFFFFFFFFFFFFF) # DIV operation
ref_30264 = ref_29529 # MOV operation
ref_30280 = (((sx(0x40, 0xFA0000000002C90C) * sx(0x40, ref_30264)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_35282 = ref_30280 # MOV operation
ref_40272 = ref_278 # MOV operation
ref_45288 = ref_35282 # MOV operation
ref_50414 = ref_22642 # MOV operation
ref_50997 = ref_50414 # MOV operation
ref_51011 = ref_45288 # MOV operation
ref_51013 = (ref_51011 | ref_50997) # OR operation
ref_51606 = ref_40272 # MOV operation
ref_51612 = ref_51013 # MOV operation
ref_51614 = ((ref_51612 + ref_51606) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_56733 = ref_51614 # MOV operation
ref_63722 = ref_22642 # MOV operation
ref_64350 = ref_63722 # MOV operation
ref_64366 = ((ref_64350 - 0x2ED5CD7E) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_64374 = ref_64366 # MOV operation
ref_65625 = ref_64374 # MOV operation
ref_65627 = ((0x28E5FC28 - ref_65625) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_65635 = ref_65627 # MOV operation
ref_66217 = ref_65635 # MOV operation
ref_66235 = (ref_66217 >> (0x2 & 0x3F)) # SHR operation
ref_66242 = ref_66235 # MOV operation
ref_67491 = ref_66242 # MOV operation
ref_67499 = (0x7 & ref_67491) # AND operation
ref_68074 = ref_67499 # MOV operation
ref_68090 = (0x1 | ref_68074) # OR operation
ref_73128 = ref_278 # MOV operation
ref_78196 = ref_35282 # MOV operation
ref_78788 = ref_73128 # MOV operation
ref_78794 = ref_78196 # MOV operation
ref_78796 = ((ref_78794 + ref_78788) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_79530 = ref_78796 # MOV operation
ref_79544 = ref_68090 # MOV operation
ref_79546 = (ref_79544 & 0xFFFFFFFF) # MOV operation
ref_79548 = (ref_79530 >> ((ref_79546 & 0xFF) & 0x3F)) # SHR operation
ref_79555 = ref_79548 # MOV operation
ref_84534 = ref_79555 # MOV operation
ref_90850 = ref_84534 # MOV operation
ref_91446 = ref_90850 # MOV operation
ref_91464 = (ref_91446 >> (0x1 & 0x3F)) # SHR operation
ref_91471 = ref_91464 # MOV operation
ref_92754 = ref_91471 # MOV operation
ref_92762 = (0x7 & ref_92754) # AND operation
ref_93437 = ref_92762 # MOV operation
ref_93453 = (0x1 | ref_93437) # OR operation
ref_98510 = ref_84534 # MOV operation
ref_99115 = ref_98510 # MOV operation
ref_99129 = ref_93453 # MOV operation
ref_99131 = (ref_99129 & 0xFFFFFFFF) # MOV operation
ref_99133 = (ref_99115 >> ((ref_99131 & 0xFF) & 0x3F)) # SHR operation
ref_99140 = ref_99133 # MOV operation
ref_104157 = ref_99140 # MOV operation
ref_104159 = ((ref_104157 >> 56) & 0xFF) # Byte reference - MOV operation
ref_104160 = ((ref_104157 >> 48) & 0xFF) # Byte reference - MOV operation
ref_104161 = ((ref_104157 >> 40) & 0xFF) # Byte reference - MOV operation
ref_104162 = ((ref_104157 >> 32) & 0xFF) # Byte reference - MOV operation
ref_104163 = ((ref_104157 >> 24) & 0xFF) # Byte reference - MOV operation
ref_104164 = ((ref_104157 >> 16) & 0xFF) # Byte reference - MOV operation
ref_104165 = ((ref_104157 >> 8) & 0xFF) # Byte reference - MOV operation
ref_104166 = (ref_104157 & 0xFF) # Byte reference - MOV operation
ref_115556 = ref_22642 # MOV operation
ref_116797 = ref_115556 # MOV operation
ref_116805 = (0x7 & ref_116797) # AND operation
ref_118034 = ref_116805 # MOV operation
ref_118044 = ((ref_118034 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_118051 = ref_118044 # MOV operation
ref_123102 = ref_56733 # MOV operation
ref_123654 = ref_123102 # MOV operation
ref_123668 = ref_118051 # MOV operation
ref_123670 = (ref_123668 | ref_123654) # OR operation
ref_128904 = ref_123670 # MOV operation
ref_137562 = ((((ref_104159) << 8 | ref_104160) << 8 | ref_104161) << 8 | ref_104162) # MOV operation
ref_138885 = (ref_137562 & 0xFFFFFFFF) # MOV operation
ref_147779 = ((((ref_104163) << 8 | ref_104164) << 8 | ref_104165) << 8 | ref_104166) # MOV operation
ref_156346 = (ref_147779 & 0xFFFFFFFF) # MOV operation
ref_157640 = (ref_138885 & 0xFFFFFFFF) # MOV operation
ref_166330 = (ref_157640 & 0xFFFFFFFF) # MOV operation
ref_179652 = ref_128904 # MOV operation
ref_180830 = ref_179652 # MOV operation
ref_180838 = (0x7 & ref_180830) # AND operation
ref_182077 = ref_180838 # MOV operation
ref_182087 = ((ref_182077 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_182094 = ref_182087 # MOV operation
ref_187114 = ref_128904 # MOV operation
ref_187740 = ref_187114 # MOV operation
ref_187754 = ref_182094 # MOV operation
ref_187756 = (ref_187754 | ref_187740) # OR operation
ref_192825 = ref_187756 # MOV operation
ref_201609 = (ref_156346 & 0xFFFFFFFF) # MOV operation
ref_202850 = (ref_201609 & 0xFFFFFFFF) # MOV operation
ref_211753 = (ref_166330 & 0xFFFFFFFF) # MOV operation
ref_220519 = (ref_211753 & 0xFFFFFFFF) # MOV operation
ref_220521 = (((ref_220519 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_220522 = (((ref_220519 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_220523 = (((ref_220519 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_220524 = ((ref_220519 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_221712 = (ref_202850 & 0xFFFFFFFF) # MOV operation
ref_230599 = (ref_221712 & 0xFFFFFFFF) # MOV operation
ref_230601 = (((ref_230599 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_230602 = (((ref_230599 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_230603 = (((ref_230599 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_230604 = ((ref_230599 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_245662 = ((((((((ref_220521) << 8 | ref_220522) << 8 | ref_220523) << 8 | ref_220524) << 8 | ref_230601) << 8 | ref_230602) << 8 | ref_230603) << 8 | ref_230604) # MOV operation
ref_246282 = ref_245662 # MOV operation
ref_246298 = (((sx(0x40, 0x4E1A7F2) * sx(0x40, ref_246282)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_251281 = ref_192825 # MOV operation
ref_251840 = ref_251281 # MOV operation
ref_251854 = ref_246298 # MOV operation
ref_251856 = (ref_251854 ^ ref_251840) # XOR operation
ref_253177 = ref_251856 # MOV operation
ref_253185 = (0xF & ref_253177) # AND operation
ref_253747 = ref_253185 # MOV operation
ref_253763 = (0x1 | ref_253747) # OR operation
ref_255040 = ref_253763 # MOV operation
ref_255042 = ((0x40 - ref_255040) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_255050 = ref_255042 # MOV operation
ref_260228 = ref_35282 # MOV operation
ref_265231 = ref_22642 # MOV operation
ref_265883 = ref_265231 # MOV operation
ref_265897 = ref_260228 # MOV operation
ref_265899 = (((sx(0x40, ref_265897) * sx(0x40, ref_265883)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_266411 = ref_265899 # MOV operation
ref_266425 = ref_255050 # MOV operation
ref_266427 = (ref_266425 & 0xFFFFFFFF) # MOV operation
ref_266429 = (ref_266411 >> ((ref_266427 & 0xFF) & 0x3F)) # SHR operation
ref_266436 = ref_266429 # MOV operation
ref_271535 = ref_35282 # MOV operation
ref_276648 = ref_22642 # MOV operation
ref_277300 = ref_276648 # MOV operation
ref_277314 = ref_271535 # MOV operation
ref_277316 = (((sx(0x40, ref_277314) * sx(0x40, ref_277300)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_283560 = ((((((((ref_220521) << 8 | ref_220522) << 8 | ref_220523) << 8 | ref_220524) << 8 | ref_230601) << 8 | ref_230602) << 8 | ref_230603) << 8 | ref_230604) # MOV operation
ref_284186 = ref_283560 # MOV operation
ref_284202 = (((sx(0x40, 0x4E1A7F2) * sx(0x40, ref_284186)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_289316 = ref_192825 # MOV operation
ref_289952 = ref_289316 # MOV operation
ref_289966 = ref_284202 # MOV operation
ref_289968 = (ref_289966 ^ ref_289952) # XOR operation
ref_291197 = ref_289968 # MOV operation
ref_291205 = (0xF & ref_291197) # AND operation
ref_291782 = ref_291205 # MOV operation
ref_291798 = (0x1 | ref_291782) # OR operation
ref_292551 = ref_277316 # MOV operation
ref_292557 = ref_291798 # MOV operation
ref_292559 = (ref_292557 & 0xFFFFFFFF) # MOV operation
ref_292561 = ((ref_292551 << ((ref_292559 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_292568 = ref_292561 # MOV operation
ref_293106 = ref_292568 # MOV operation
ref_293120 = ref_266436 # MOV operation
ref_293122 = (ref_293120 | ref_293106) # OR operation
ref_298041 = ref_293122 # MOV operation
ref_299242 = ref_298041 # MOV operation
ref_299244 = ref_299242 # MOV operation

print(ref_299244 & 0xffffffffffffffff)
