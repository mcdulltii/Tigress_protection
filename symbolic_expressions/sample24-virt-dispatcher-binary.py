#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])

ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_17550 = ref_278 # MOV operation
ref_18109 = ref_17550 # MOV operation
ref_18123 = ((ref_18109 << (0xB & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_24394 = ref_278 # MOV operation
ref_24883 = ref_24394 # MOV operation
ref_24897 = (ref_24883 >> (0x35 & 0x3F)) # SHR operation
ref_25597 = ref_18123 # MOV operation
ref_25601 = ref_24897 # MOV operation
ref_25603 = (ref_25601 | ref_25597) # OR operation
ref_26117 = ref_25603 # MOV operation
ref_26131 = (ref_26117 >> (0x1 & 0x3F)) # SHR operation
ref_26945 = ref_26131 # MOV operation
ref_37490 = ref_26945 # MOV operation
ref_38808 = ref_37490 # MOV operation
ref_38814 = (((sx(0x40, 0x6B33F46) * sx(0x40, ref_38808)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_44299 = ref_278 # MOV operation
ref_45833 = ref_44299 # MOV operation
ref_45841 = ((((0x0) << 64 | ref_45833) / 0x3) & 0xFFFFFFFFFFFFFFFF) # DIV operation
ref_46459 = ref_45841 # MOV operation
ref_46471 = ref_38814 # MOV operation
ref_46473 = ((ref_46459 - ref_46471) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_46481 = ref_46473 # MOV operation
ref_47290 = ref_46481 # MOV operation
ref_60184 = ref_47290 # MOV operation
ref_60673 = ref_60184 # MOV operation
ref_60687 = (ref_60673 >> (0x7 & 0x3F)) # SHR operation
ref_61201 = ref_60687 # MOV operation
ref_61215 = (ref_61201 >> (0x2 & 0x3F)) # SHR operation
ref_61875 = ref_61215 # MOV operation
ref_61889 = (0x7 & ref_61875) # AND operation
ref_63372 = ref_61889 # MOV operation
ref_63378 = (0x1 | ref_63372) # OR operation
ref_69649 = ref_278 # MOV operation
ref_70354 = ref_69649 # MOV operation
ref_70368 = ((0x9919884 + ref_70354) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_70883 = ref_70368 # MOV operation
ref_70895 = ref_63378 # MOV operation
ref_70897 = (ref_70883 >> ((ref_70895 & 0xFF) & 0x3F)) # SHR operation
ref_71711 = ref_70897 # MOV operation
ref_83068 = ref_278 # MOV operation
ref_83773 = ref_83068 # MOV operation
ref_83787 = ((0x1E5EA08F8 + ref_83773) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_84602 = ref_83787 # MOV operation
ref_104885 = ref_71711 # MOV operation
ref_113768 = ref_71711 # MOV operation
ref_114403 = ref_113768 # MOV operation
ref_114417 = (0x3F & ref_114403) # AND operation
ref_115001 = ref_114417 # MOV operation
ref_115015 = ((ref_115001 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_115715 = ref_104885 # MOV operation
ref_115719 = ref_115015 # MOV operation
ref_115721 = (ref_115719 | ref_115715) # OR operation
ref_116535 = ref_115721 # MOV operation
ref_136138 = ref_116535 # MOV operation
ref_144704 = ref_47290 # MOV operation
ref_145193 = ref_144704 # MOV operation
ref_145207 = (ref_145193 >> (0x2 & 0x3F)) # SHR operation
ref_145867 = ref_145207 # MOV operation
ref_145881 = (0xF & ref_145867) # AND operation
ref_147364 = ref_145881 # MOV operation
ref_147370 = (0x1 | ref_147364) # OR operation
ref_152829 = ref_26945 # MOV operation
ref_153388 = ref_152829 # MOV operation
ref_153400 = ref_147370 # MOV operation
ref_153402 = ((ref_153388 << ((ref_153400 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_160427 = ref_47290 # MOV operation
ref_160916 = ref_160427 # MOV operation
ref_160930 = (ref_160916 >> (0x2 & 0x3F)) # SHR operation
ref_161590 = ref_160930 # MOV operation
ref_161604 = (0xF & ref_161590) # AND operation
ref_163087 = ref_161604 # MOV operation
ref_163093 = (0x1 | ref_163087) # OR operation
ref_164510 = ref_163093 # MOV operation
ref_164512 = ((0x40 - ref_164510) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_164520 = ref_164512 # MOV operation
ref_169974 = ref_26945 # MOV operation
ref_170463 = ref_169974 # MOV operation
ref_170475 = ref_164520 # MOV operation
ref_170477 = (ref_170463 >> ((ref_170475 & 0xFF) & 0x3F)) # SHR operation
ref_171177 = ref_153402 # MOV operation
ref_171181 = ref_170477 # MOV operation
ref_171183 = (ref_171181 | ref_171177) # OR operation
ref_171843 = ref_171183 # MOV operation
ref_171857 = (0x7 & ref_171843) # AND operation
ref_172441 = ref_171857 # MOV operation
ref_172455 = ((ref_172441 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_173155 = ref_136138 # MOV operation
ref_173159 = ref_172455 # MOV operation
ref_173161 = (ref_173159 | ref_173155) # OR operation
ref_173975 = ref_173161 # MOV operation
ref_181600 = ref_84602 # MOV operation
ref_182089 = ref_181600 # MOV operation
ref_182103 = (ref_182089 >> (0x4 & 0x3F)) # SHR operation
ref_182763 = ref_182103 # MOV operation
ref_182777 = (0xF & ref_182763) # AND operation
ref_184260 = ref_182777 # MOV operation
ref_184266 = (0x1 | ref_184260) # OR operation
ref_189725 = ref_173975 # MOV operation
ref_190214 = ref_189725 # MOV operation
ref_190226 = ref_184266 # MOV operation
ref_190228 = (ref_190214 >> ((ref_190226 & 0xFF) & 0x3F)) # SHR operation
ref_197253 = ref_84602 # MOV operation
ref_197742 = ref_197253 # MOV operation
ref_197756 = (ref_197742 >> (0x4 & 0x3F)) # SHR operation
ref_198416 = ref_197756 # MOV operation
ref_198430 = (0xF & ref_198416) # AND operation
ref_199913 = ref_198430 # MOV operation
ref_199919 = (0x1 | ref_199913) # OR operation
ref_201336 = ref_199919 # MOV operation
ref_201338 = ((0x40 - ref_201336) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_201346 = ref_201338 # MOV operation
ref_206800 = ref_173975 # MOV operation
ref_207359 = ref_206800 # MOV operation
ref_207371 = ref_201346 # MOV operation
ref_207373 = ((ref_207359 << ((ref_207371 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_208073 = ref_190228 # MOV operation
ref_208077 = ref_207373 # MOV operation
ref_208079 = (ref_208077 | ref_208073) # OR operation
ref_215104 = ref_47290 # MOV operation
ref_215593 = ref_215104 # MOV operation
ref_215607 = (ref_215593 >> (0x3 & 0x3F)) # SHR operation
ref_216267 = ref_215607 # MOV operation
ref_216281 = (0xF & ref_216267) # AND operation
ref_217764 = ref_216281 # MOV operation
ref_217770 = (0x1 | ref_217764) # OR operation
ref_223229 = ref_26945 # MOV operation
ref_223718 = ref_223229 # MOV operation
ref_223730 = ref_217770 # MOV operation
ref_223732 = (ref_223718 >> ((ref_223730 & 0xFF) & 0x3F)) # SHR operation
ref_230757 = ref_47290 # MOV operation
ref_231246 = ref_230757 # MOV operation
ref_231260 = (ref_231246 >> (0x3 & 0x3F)) # SHR operation
ref_231920 = ref_231260 # MOV operation
ref_231934 = (0xF & ref_231920) # AND operation
ref_233417 = ref_231934 # MOV operation
ref_233423 = (0x1 | ref_233417) # OR operation
ref_234840 = ref_233423 # MOV operation
ref_234842 = ((0x40 - ref_234840) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_234850 = ref_234842 # MOV operation
ref_240304 = ref_26945 # MOV operation
ref_240863 = ref_240304 # MOV operation
ref_240875 = ref_234850 # MOV operation
ref_240877 = ((ref_240863 << ((ref_240875 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_241577 = ref_223732 # MOV operation
ref_241581 = ref_240877 # MOV operation
ref_241583 = (ref_241581 | ref_241577) # OR operation
ref_242243 = ref_241583 # MOV operation
ref_242255 = ref_208079 # MOV operation
ref_242257 = ((ref_242243 - ref_242255) & 0xFFFFFFFFFFFFFFFF) # CMP operation
ref_242259 = ((((ref_242243 ^ (ref_242255 ^ ref_242257)) ^ ((ref_242243 ^ ref_242257) & (ref_242243 ^ ref_242255))) >> 63) & 0x1) # Carry flag
ref_242263 = (0x1 if (ref_242257 == 0x0) else 0x0) # Zero flag
ref_242265 = ((((ref_242255 >> 8) & 0xFFFFFFFFFFFFFF)) << 8 | (0x1 if (((~(ref_242259) & 0x1) & (~(ref_242263) & 0x1)) == 0x1) else 0x0)) # SETA operation
ref_242267 = (ref_242265 & 0xFF) # MOVZX operation
ref_242514 = (ref_242267 & 0xFFFFFFFF) # MOV operation
ref_242516 = ((ref_242514 & 0xFFFFFFFF) & (ref_242514 & 0xFFFFFFFF)) # TEST operation
ref_242521 = (0x1 if (ref_242516 == 0x0) else 0x0) # Zero flag
ref_242523 = (0x1F1C if (ref_242521 == 0x1) else 0x1EFE) # Program Counter


if (ref_242521 == 0x1):
    ref_263 = SymVar_0
    ref_278 = ref_263 # MOV operation
    ref_17550 = ref_278 # MOV operation
    ref_18109 = ref_17550 # MOV operation
    ref_18123 = ((ref_18109 << (0xB & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_24394 = ref_278 # MOV operation
    ref_24883 = ref_24394 # MOV operation
    ref_24897 = (ref_24883 >> (0x35 & 0x3F)) # SHR operation
    ref_25597 = ref_18123 # MOV operation
    ref_25601 = ref_24897 # MOV operation
    ref_25603 = (ref_25601 | ref_25597) # OR operation
    ref_26117 = ref_25603 # MOV operation
    ref_26131 = (ref_26117 >> (0x1 & 0x3F)) # SHR operation
    ref_26945 = ref_26131 # MOV operation
    ref_37490 = ref_26945 # MOV operation
    ref_38808 = ref_37490 # MOV operation
    ref_38814 = (((sx(0x40, 0x6B33F46) * sx(0x40, ref_38808)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_44299 = ref_278 # MOV operation
    ref_45833 = ref_44299 # MOV operation
    ref_45841 = ((((0x0) << 64 | ref_45833) / 0x3) & 0xFFFFFFFFFFFFFFFF) # DIV operation
    ref_46459 = ref_45841 # MOV operation
    ref_46471 = ref_38814 # MOV operation
    ref_46473 = ((ref_46459 - ref_46471) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_46481 = ref_46473 # MOV operation
    ref_47290 = ref_46481 # MOV operation
    ref_60184 = ref_47290 # MOV operation
    ref_60673 = ref_60184 # MOV operation
    ref_60687 = (ref_60673 >> (0x7 & 0x3F)) # SHR operation
    ref_61201 = ref_60687 # MOV operation
    ref_61215 = (ref_61201 >> (0x2 & 0x3F)) # SHR operation
    ref_61875 = ref_61215 # MOV operation
    ref_61889 = (0x7 & ref_61875) # AND operation
    ref_63372 = ref_61889 # MOV operation
    ref_63378 = (0x1 | ref_63372) # OR operation
    ref_69649 = ref_278 # MOV operation
    ref_70354 = ref_69649 # MOV operation
    ref_70368 = ((0x9919884 + ref_70354) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_70883 = ref_70368 # MOV operation
    ref_70895 = ref_63378 # MOV operation
    ref_70897 = (ref_70883 >> ((ref_70895 & 0xFF) & 0x3F)) # SHR operation
    ref_71711 = ref_70897 # MOV operation
    ref_83068 = ref_278 # MOV operation
    ref_83773 = ref_83068 # MOV operation
    ref_83787 = ((0x1E5EA08F8 + ref_83773) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_84602 = ref_83787 # MOV operation
    ref_104885 = ref_71711 # MOV operation
    ref_113768 = ref_71711 # MOV operation
    ref_114403 = ref_113768 # MOV operation
    ref_114417 = (0x3F & ref_114403) # AND operation
    ref_115001 = ref_114417 # MOV operation
    ref_115015 = ((ref_115001 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_115715 = ref_104885 # MOV operation
    ref_115719 = ref_115015 # MOV operation
    ref_115721 = (ref_115719 | ref_115715) # OR operation
    ref_116535 = ref_115721 # MOV operation
    ref_136138 = ref_116535 # MOV operation
    ref_144704 = ref_47290 # MOV operation
    ref_145193 = ref_144704 # MOV operation
    ref_145207 = (ref_145193 >> (0x2 & 0x3F)) # SHR operation
    ref_145867 = ref_145207 # MOV operation
    ref_145881 = (0xF & ref_145867) # AND operation
    ref_147364 = ref_145881 # MOV operation
    ref_147370 = (0x1 | ref_147364) # OR operation
    ref_152829 = ref_26945 # MOV operation
    ref_153388 = ref_152829 # MOV operation
    ref_153400 = ref_147370 # MOV operation
    ref_153402 = ((ref_153388 << ((ref_153400 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_160427 = ref_47290 # MOV operation
    ref_160916 = ref_160427 # MOV operation
    ref_160930 = (ref_160916 >> (0x2 & 0x3F)) # SHR operation
    ref_161590 = ref_160930 # MOV operation
    ref_161604 = (0xF & ref_161590) # AND operation
    ref_163087 = ref_161604 # MOV operation
    ref_163093 = (0x1 | ref_163087) # OR operation
    ref_164510 = ref_163093 # MOV operation
    ref_164512 = ((0x40 - ref_164510) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_164520 = ref_164512 # MOV operation
    ref_169974 = ref_26945 # MOV operation
    ref_170463 = ref_169974 # MOV operation
    ref_170475 = ref_164520 # MOV operation
    ref_170477 = (ref_170463 >> ((ref_170475 & 0xFF) & 0x3F)) # SHR operation
    ref_171177 = ref_153402 # MOV operation
    ref_171181 = ref_170477 # MOV operation
    ref_171183 = (ref_171181 | ref_171177) # OR operation
    ref_171843 = ref_171183 # MOV operation
    ref_171857 = (0x7 & ref_171843) # AND operation
    ref_172441 = ref_171857 # MOV operation
    ref_172455 = ((ref_172441 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_173155 = ref_136138 # MOV operation
    ref_173159 = ref_172455 # MOV operation
    ref_173161 = (ref_173159 | ref_173155) # OR operation
    ref_173975 = ref_173161 # MOV operation
    ref_253682 = ref_47290 # MOV operation
    ref_260682 = ref_47290 # MOV operation
    ref_261317 = ref_260682 # MOV operation
    ref_261331 = (0xF & ref_261317) # AND operation
    ref_261915 = ref_261331 # MOV operation
    ref_261929 = ((ref_261915 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_262629 = ref_253682 # MOV operation
    ref_262633 = ref_261929 # MOV operation
    ref_262635 = (ref_262633 | ref_262629) # OR operation
    ref_263449 = ref_262635 # MOV operation
    ref_273994 = ref_26945 # MOV operation
    ref_280994 = ref_263449 # MOV operation
    ref_286428 = ref_173975 # MOV operation
    ref_287063 = ref_286428 # MOV operation
    ref_287075 = ref_280994 # MOV operation
    ref_287077 = (ref_287075 & ref_287063) # AND operation
    ref_287737 = ref_287077 # MOV operation
    ref_287751 = (0x1F & ref_287737) # AND operation
    ref_288335 = ref_287751 # MOV operation
    ref_288349 = ((ref_288335 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_289049 = ref_273994 # MOV operation
    ref_289053 = ref_288349 # MOV operation
    ref_289055 = (ref_289053 | ref_289049) # OR operation
    ref_289869 = ref_289055 # MOV operation
    ref_301057 = ref_289869 # MOV operation
    ref_306491 = ref_263449 # MOV operation
    ref_307166 = ref_301057 # MOV operation
    ref_307170 = ref_306491 # MOV operation
    ref_307172 = (ref_307170 | ref_307166) # OR operation
    ref_312631 = ref_173975 # MOV operation
    ref_318065 = ref_84602 # MOV operation
    ref_318600 = ref_312631 # MOV operation
    ref_318604 = ref_318065 # MOV operation
    ref_318606 = (((sx(0x40, ref_318604) * sx(0x40, ref_318600)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_319163 = ref_307172 # MOV operation
    ref_319167 = ref_318606 # MOV operation
    ref_319169 = (((sx(0x40, ref_319167) * sx(0x40, ref_319163)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_319980 = ref_319169 # MOV operation
    ref_321087 = ref_319980 # MOV operation
    ref_321089 = ref_321087 # MOV operation
    endb = ref_321089


else:
    ref_321409 = SymVar_0
    ref_321424 = ref_321409 # MOV operation
    ref_338701 = ref_321424 # MOV operation
    ref_339260 = ref_338701 # MOV operation
    ref_339274 = ((ref_339260 << (0xB & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_345545 = ref_321424 # MOV operation
    ref_346034 = ref_345545 # MOV operation
    ref_346048 = (ref_346034 >> (0x35 & 0x3F)) # SHR operation
    ref_346748 = ref_339274 # MOV operation
    ref_346752 = ref_346048 # MOV operation
    ref_346754 = (ref_346752 | ref_346748) # OR operation
    ref_347268 = ref_346754 # MOV operation
    ref_347282 = (ref_347268 >> (0x1 & 0x3F)) # SHR operation
    ref_348096 = ref_347282 # MOV operation
    ref_358641 = ref_348096 # MOV operation
    ref_359959 = ref_358641 # MOV operation
    ref_359965 = (((sx(0x40, 0x6B33F46) * sx(0x40, ref_359959)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_365450 = ref_321424 # MOV operation
    ref_366984 = ref_365450 # MOV operation
    ref_366992 = ((((0x0) << 64 | ref_366984) / 0x3) & 0xFFFFFFFFFFFFFFFF) # DIV operation
    ref_367610 = ref_366992 # MOV operation
    ref_367622 = ref_359965 # MOV operation
    ref_367624 = ((ref_367610 - ref_367622) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_367632 = ref_367624 # MOV operation
    ref_368441 = ref_367632 # MOV operation
    ref_381335 = ref_368441 # MOV operation
    ref_381824 = ref_381335 # MOV operation
    ref_381838 = (ref_381824 >> (0x7 & 0x3F)) # SHR operation
    ref_382352 = ref_381838 # MOV operation
    ref_382366 = (ref_382352 >> (0x2 & 0x3F)) # SHR operation
    ref_383026 = ref_382366 # MOV operation
    ref_383040 = (0x7 & ref_383026) # AND operation
    ref_384523 = ref_383040 # MOV operation
    ref_384529 = (0x1 | ref_384523) # OR operation
    ref_390800 = ref_321424 # MOV operation
    ref_391505 = ref_390800 # MOV operation
    ref_391519 = ((0x9919884 + ref_391505) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_392034 = ref_391519 # MOV operation
    ref_392046 = ref_384529 # MOV operation
    ref_392048 = (ref_392034 >> ((ref_392046 & 0xFF) & 0x3F)) # SHR operation
    ref_392862 = ref_392048 # MOV operation
    ref_404219 = ref_321424 # MOV operation
    ref_404924 = ref_404219 # MOV operation
    ref_404938 = ((0x1E5EA08F8 + ref_404924) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_405753 = ref_404938 # MOV operation
    ref_426036 = ref_392862 # MOV operation
    ref_434919 = ref_392862 # MOV operation
    ref_435554 = ref_434919 # MOV operation
    ref_435568 = (0x3F & ref_435554) # AND operation
    ref_436152 = ref_435568 # MOV operation
    ref_436166 = ((ref_436152 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_436866 = ref_426036 # MOV operation
    ref_436870 = ref_436166 # MOV operation
    ref_436872 = (ref_436870 | ref_436866) # OR operation
    ref_437686 = ref_436872 # MOV operation
    ref_457289 = ref_437686 # MOV operation
    ref_465855 = ref_368441 # MOV operation
    ref_466344 = ref_465855 # MOV operation
    ref_466358 = (ref_466344 >> (0x2 & 0x3F)) # SHR operation
    ref_467018 = ref_466358 # MOV operation
    ref_467032 = (0xF & ref_467018) # AND operation
    ref_468515 = ref_467032 # MOV operation
    ref_468521 = (0x1 | ref_468515) # OR operation
    ref_473980 = ref_348096 # MOV operation
    ref_474539 = ref_473980 # MOV operation
    ref_474551 = ref_468521 # MOV operation
    ref_474553 = ((ref_474539 << ((ref_474551 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_481578 = ref_368441 # MOV operation
    ref_482067 = ref_481578 # MOV operation
    ref_482081 = (ref_482067 >> (0x2 & 0x3F)) # SHR operation
    ref_482741 = ref_482081 # MOV operation
    ref_482755 = (0xF & ref_482741) # AND operation
    ref_484238 = ref_482755 # MOV operation
    ref_484244 = (0x1 | ref_484238) # OR operation
    ref_485661 = ref_484244 # MOV operation
    ref_485663 = ((0x40 - ref_485661) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_485671 = ref_485663 # MOV operation
    ref_491125 = ref_348096 # MOV operation
    ref_491614 = ref_491125 # MOV operation
    ref_491626 = ref_485671 # MOV operation
    ref_491628 = (ref_491614 >> ((ref_491626 & 0xFF) & 0x3F)) # SHR operation
    ref_492328 = ref_474553 # MOV operation
    ref_492332 = ref_491628 # MOV operation
    ref_492334 = (ref_492332 | ref_492328) # OR operation
    ref_492994 = ref_492334 # MOV operation
    ref_493008 = (0x7 & ref_492994) # AND operation
    ref_493592 = ref_493008 # MOV operation
    ref_493606 = ((ref_493592 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_494306 = ref_457289 # MOV operation
    ref_494310 = ref_493606 # MOV operation
    ref_494312 = (ref_494310 | ref_494306) # OR operation
    ref_495126 = ref_494312 # MOV operation
    ref_495128 = ((ref_495126 >> 56) & 0xFF) # Byte reference - MOV operation
    ref_495129 = ((ref_495126 >> 48) & 0xFF) # Byte reference - MOV operation
    ref_495130 = ((ref_495126 >> 40) & 0xFF) # Byte reference - MOV operation
    ref_495131 = ((ref_495126 >> 32) & 0xFF) # Byte reference - MOV operation
    ref_495132 = ((ref_495126 >> 24) & 0xFF) # Byte reference - MOV operation
    ref_495133 = ((ref_495126 >> 16) & 0xFF) # Byte reference - MOV operation
    ref_495134 = ((ref_495126 >> 8) & 0xFF) # Byte reference - MOV operation
    ref_495135 = (ref_495126 & 0xFF) # Byte reference - MOV operation
    ref_575801 = ref_405753 # MOV operation
    ref_576290 = ref_575801 # MOV operation
    ref_576304 = (ref_576290 >> (0x3 & 0x3F)) # SHR operation
    ref_576964 = ref_576304 # MOV operation
    ref_576978 = (0xF & ref_576964) # AND operation
    ref_578461 = ref_576978 # MOV operation
    ref_578467 = (0x1 | ref_578461) # OR operation
    ref_583926 = ref_405753 # MOV operation
    ref_584485 = ref_583926 # MOV operation
    ref_584497 = ref_578467 # MOV operation
    ref_584499 = ((ref_584485 << ((ref_584497 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_591524 = ref_405753 # MOV operation
    ref_592013 = ref_591524 # MOV operation
    ref_592027 = (ref_592013 >> (0x3 & 0x3F)) # SHR operation
    ref_592687 = ref_592027 # MOV operation
    ref_592701 = (0xF & ref_592687) # AND operation
    ref_594184 = ref_592701 # MOV operation
    ref_594190 = (0x1 | ref_594184) # OR operation
    ref_595607 = ref_594190 # MOV operation
    ref_595609 = ((0x40 - ref_595607) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_595617 = ref_595609 # MOV operation
    ref_601071 = ref_405753 # MOV operation
    ref_601560 = ref_601071 # MOV operation
    ref_601572 = ref_595617 # MOV operation
    ref_601574 = (ref_601560 >> ((ref_601572 & 0xFF) & 0x3F)) # SHR operation
    ref_602274 = ref_584499 # MOV operation
    ref_602278 = ref_601574 # MOV operation
    ref_602280 = (ref_602278 | ref_602274) # OR operation
    ref_603094 = ref_602280 # MOV operation
    ref_612578 = ref_495134 # MOVZX operation
    ref_614116 = (ref_612578 & 0xFF) # MOVZX operation
    ref_623592 = ref_495132 # MOVZX operation
    ref_633126 = (ref_623592 & 0xFF) # MOVZX operation
    ref_633128 = (ref_633126 & 0xFF) # Byte reference - MOV operation
    ref_634606 = (ref_614116 & 0xFF) # MOVZX operation
    ref_644140 = (ref_634606 & 0xFF) # MOVZX operation
    ref_644142 = (ref_644140 & 0xFF) # Byte reference - MOV operation
    ref_655320 = ref_603094 # MOV operation
    ref_660754 = ref_368441 # MOV operation
    ref_661429 = ref_655320 # MOV operation
    ref_661433 = ref_660754 # MOV operation
    ref_661435 = (ref_661433 | ref_661429) # OR operation
    ref_666894 = ((((((((ref_495128) << 8 | ref_495129) << 8 | ref_495130) << 8 | ref_495131) << 8 | ref_644142) << 8 | ref_495133) << 8 | ref_633128) << 8 | ref_495135) # MOV operation
    ref_672328 = ref_405753 # MOV operation
    ref_672863 = ref_666894 # MOV operation
    ref_672867 = ref_672328 # MOV operation
    ref_672869 = (((sx(0x40, ref_672867) * sx(0x40, ref_672863)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_673426 = ref_661435 # MOV operation
    ref_673430 = ref_672869 # MOV operation
    ref_673432 = (((sx(0x40, ref_673430) * sx(0x40, ref_673426)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_674243 = ref_673432 # MOV operation
    ref_675350 = ref_674243 # MOV operation
    ref_675352 = ref_675350 # MOV operation
    endb = ref_675352


print(endb & 0xffffffffffffffff)
