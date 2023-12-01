#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])

ref_228 = SymVar_0
ref_243 = ref_228 # MOV operation
ref_7000 = ref_243 # MOV operation
ref_7570 = ref_7000 # MOV operation
ref_7584 = (0x222C2AFC & ref_7570) # AND operation
ref_8179 = ref_7584 # MOV operation
ref_8193 = ref_8179 # MOV operation
ref_8195 = ((ref_8193 - 0x14582014) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_8203 = ref_8195 # MOV operation
ref_13491 = ref_8203 # MOV operation
ref_18716 = ref_243 # MOV operation
ref_20004 = ref_18716 # MOV operation
ref_20010 = ((0x22722B13 + ref_20004) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_26036 = ref_13491 # MOV operation
ref_27394 = ref_26036 # MOV operation
ref_27400 = (((sx(0x40, 0x1DF2339F) * sx(0x40, ref_27394)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_28004 = ref_27400 # MOV operation
ref_28006 = ((ref_28004 + 0x608C69) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_28610 = ref_20010 # MOV operation
ref_28614 = ref_28006 # MOV operation
ref_28616 = ((ref_28614 + ref_28610) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_33910 = ref_28616 # MOV operation
ref_40555 = ref_243 # MOV operation
ref_41125 = ref_40555 # MOV operation
ref_41139 = (0x140538E4 & ref_41125) # AND operation
ref_41734 = ref_41139 # MOV operation
ref_41748 = ref_41734 # MOV operation
ref_41750 = ((ref_41748 - 0x5F1E4CE7) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_41758 = ref_41750 # MOV operation
ref_47046 = ref_41758 # MOV operation
ref_52271 = ref_243 # MOV operation
ref_57561 = ref_33910 # MOV operation
ref_64271 = ref_47046 # MOV operation
ref_65399 = ref_64271 # MOV operation
ref_65405 = ref_65399 # MOV operation
ref_65409 = (ref_65405 >> (0x3 & 0x3F)) # SHR operation
ref_65416 = ref_65409 # MOV operation
ref_66006 = ref_65416 # MOV operation
ref_66020 = (0x7 & ref_66006) # AND operation
ref_66655 = ref_66020 # MOV operation
ref_66669 = (0x1 | ref_66655) # OR operation
ref_67112 = ref_57561 # MOV operation
ref_67116 = ref_66669 # MOV operation
ref_67118 = ref_67112 # MOV operation
ref_67120 = (ref_67116 & 0xFFFFFFFF) # MOV operation
ref_67122 = (ref_67118 >> ((ref_67120 & 0xFF) & 0x3F)) # SHR operation
ref_67129 = ref_67122 # MOV operation
ref_67727 = ref_52271 # MOV operation
ref_67731 = ref_67129 # MOV operation
ref_67733 = ((ref_67731 + ref_67727) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_73027 = ref_67733 # MOV operation
ref_78945 = ref_47046 # MOV operation
ref_84235 = ref_73027 # MOV operation
ref_84883 = ref_78945 # MOV operation
ref_84887 = ref_84235 # MOV operation
ref_84889 = (((sx(0x40, ref_84887) * sx(0x40, ref_84883)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_90201 = ref_33910 # MOV operation
ref_95491 = ref_13491 # MOV operation
ref_96161 = ref_95491 # MOV operation
ref_96173 = ref_90201 # MOV operation
ref_96175 = (ref_96173 ^ ref_96161) # XOR operation
ref_96870 = ref_96175 # MOV operation
ref_96882 = ref_84889 # MOV operation
ref_96884 = ((ref_96870 - ref_96882) & 0xFFFFFFFFFFFFFFFF) # CMP operation
ref_96890 = (0x1 if (ref_96884 == 0x0) else 0x0) # Zero flag
ref_96892 = ((((ref_96882 >> 8) & 0xFFFFFFFFFFFFFF)) << 8 | (0x1 if (ref_96890 == 0x1) else 0x0)) # SETE operation
ref_96894 = (ref_96892 & 0xFF) # MOVZX operation
ref_97346 = (ref_96894 & 0xFFFFFFFF) # MOV operation
ref_97348 = ((ref_97346 & 0xFFFFFFFF) & (ref_97346 & 0xFFFFFFFF)) # TEST operation
ref_97353 = (0x1 if (ref_97348 == 0x0) else 0x0) # Zero flag
ref_97355 = (0x400A95 if (ref_97353 == 0x1) else 0x400A80) # Program Counter


if (ref_97353 == 0x1):
    ref_228 = SymVar_0
    ref_243 = ref_228 # MOV operation
    ref_7000 = ref_243 # MOV operation
    ref_7570 = ref_7000 # MOV operation
    ref_7584 = (0x222C2AFC & ref_7570) # AND operation
    ref_8179 = ref_7584 # MOV operation
    ref_8193 = ref_8179 # MOV operation
    ref_8195 = ((ref_8193 - 0x14582014) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_8203 = ref_8195 # MOV operation
    ref_13491 = ref_8203 # MOV operation
    ref_13493 = ((ref_13491 >> 56) & 0xFF) # Byte reference - MOV operation
    ref_13494 = ((ref_13491 >> 48) & 0xFF) # Byte reference - MOV operation
    ref_13495 = ((ref_13491 >> 40) & 0xFF) # Byte reference - MOV operation
    ref_13496 = ((ref_13491 >> 32) & 0xFF) # Byte reference - MOV operation
    ref_13497 = ((ref_13491 >> 24) & 0xFF) # Byte reference - MOV operation
    ref_13498 = ((ref_13491 >> 16) & 0xFF) # Byte reference - MOV operation
    ref_13499 = ((ref_13491 >> 8) & 0xFF) # Byte reference - MOV operation
    ref_13500 = (ref_13491 & 0xFF) # Byte reference - MOV operation
    ref_18716 = ref_243 # MOV operation
    ref_20004 = ref_18716 # MOV operation
    ref_20010 = ((0x22722B13 + ref_20004) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_26036 = ref_13491 # MOV operation
    ref_27394 = ref_26036 # MOV operation
    ref_27400 = (((sx(0x40, 0x1DF2339F) * sx(0x40, ref_27394)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_28004 = ref_27400 # MOV operation
    ref_28006 = ((ref_28004 + 0x608C69) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_28610 = ref_20010 # MOV operation
    ref_28614 = ref_28006 # MOV operation
    ref_28616 = ((ref_28614 + ref_28610) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_33910 = ref_28616 # MOV operation
    ref_40555 = ref_243 # MOV operation
    ref_41125 = ref_40555 # MOV operation
    ref_41139 = (0x140538E4 & ref_41125) # AND operation
    ref_41734 = ref_41139 # MOV operation
    ref_41748 = ref_41734 # MOV operation
    ref_41750 = ((ref_41748 - 0x5F1E4CE7) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_41758 = ref_41750 # MOV operation
    ref_47046 = ref_41758 # MOV operation
    ref_52271 = ref_243 # MOV operation
    ref_57561 = ref_33910 # MOV operation
    ref_64271 = ref_47046 # MOV operation
    ref_65399 = ref_64271 # MOV operation
    ref_65405 = ref_65399 # MOV operation
    ref_65409 = (ref_65405 >> (0x3 & 0x3F)) # SHR operation
    ref_65416 = ref_65409 # MOV operation
    ref_66006 = ref_65416 # MOV operation
    ref_66020 = (0x7 & ref_66006) # AND operation
    ref_66655 = ref_66020 # MOV operation
    ref_66669 = (0x1 | ref_66655) # OR operation
    ref_67112 = ref_57561 # MOV operation
    ref_67116 = ref_66669 # MOV operation
    ref_67118 = ref_67112 # MOV operation
    ref_67120 = (ref_67116 & 0xFFFFFFFF) # MOV operation
    ref_67122 = (ref_67118 >> ((ref_67120 & 0xFF) & 0x3F)) # SHR operation
    ref_67129 = ref_67122 # MOV operation
    ref_67727 = ref_52271 # MOV operation
    ref_67731 = ref_67129 # MOV operation
    ref_67733 = ((ref_67731 + ref_67727) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_73027 = ref_67733 # MOV operation
    ref_73029 = ((ref_73027 >> 56) & 0xFF) # Byte reference - MOV operation
    ref_73030 = ((ref_73027 >> 48) & 0xFF) # Byte reference - MOV operation
    ref_73031 = ((ref_73027 >> 40) & 0xFF) # Byte reference - MOV operation
    ref_73032 = ((ref_73027 >> 32) & 0xFF) # Byte reference - MOV operation
    ref_73033 = ((ref_73027 >> 24) & 0xFF) # Byte reference - MOV operation
    ref_73034 = ((ref_73027 >> 16) & 0xFF) # Byte reference - MOV operation
    ref_73035 = ((ref_73027 >> 8) & 0xFF) # Byte reference - MOV operation
    ref_73036 = (ref_73027 & 0xFF) # Byte reference - MOV operation
    ref_106532 = ((ref_73033) << 8 | ref_73034) # MOVZX operation
    ref_107796 = (ref_106532 & 0xFFFF) # MOVZX operation
    ref_116350 = ((ref_73035) << 8 | ref_73036) # MOVZX operation
    ref_124732 = (ref_116350 & 0xFFFF) # MOVZX operation
    ref_124734 = (((ref_124732 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
    ref_124735 = ((ref_124732 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
    ref_126168 = (ref_107796 & 0xFFFF) # MOVZX operation
    ref_134550 = (ref_126168 & 0xFFFF) # MOVZX operation
    ref_134552 = (((ref_134550 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
    ref_134553 = ((ref_134550 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
    ref_139854 = ref_47046 # MOV operation
    ref_146564 = ref_13491 # MOV operation
    ref_147134 = ref_146564 # MOV operation
    ref_147148 = (0xF & ref_147134) # AND operation
    ref_147783 = ref_147148 # MOV operation
    ref_147797 = (0x1 | ref_147783) # OR operation
    ref_149114 = ref_147797 # MOV operation
    ref_149118 = ((0x40 - ref_149114) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_149126 = ref_149118 # MOV operation
    ref_149564 = ref_139854 # MOV operation
    ref_149568 = ref_149126 # MOV operation
    ref_149570 = ref_149564 # MOV operation
    ref_149572 = (ref_149568 & 0xFFFFFFFF) # MOV operation
    ref_149574 = (ref_149570 >> ((ref_149572 & 0xFF) & 0x3F)) # SHR operation
    ref_149581 = ref_149574 # MOV operation
    ref_154891 = ref_47046 # MOV operation
    ref_161601 = ref_13491 # MOV operation
    ref_162171 = ref_161601 # MOV operation
    ref_162185 = (0xF & ref_162171) # AND operation
    ref_162820 = ref_162185 # MOV operation
    ref_162834 = (0x1 | ref_162820) # OR operation
    ref_163407 = ref_154891 # MOV operation
    ref_163411 = ref_162834 # MOV operation
    ref_163413 = ref_163407 # MOV operation
    ref_163415 = (ref_163411 & 0xFFFFFFFF) # MOV operation
    ref_163417 = ((ref_163413 << ((ref_163415 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_163424 = ref_163417 # MOV operation
    ref_164054 = ref_163424 # MOV operation
    ref_164066 = ref_149581 # MOV operation
    ref_164068 = (ref_164066 | ref_164054) # OR operation
    ref_169361 = ref_164068 # MOV operation
    ref_175381 = ref_169361 # MOV operation
    ref_175951 = ref_175381 # MOV operation
    ref_175965 = (0xF & ref_175951) # AND operation
    ref_177248 = ref_175965 # MOV operation
    ref_177254 = ref_177248 # MOV operation
    ref_177258 = ((ref_177254 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_177265 = ref_177258 # MOV operation
    ref_182575 = ((((((((ref_73029) << 8 | ref_73030) << 8 | ref_73031) << 8 | ref_73032) << 8 | ref_124734) << 8 | ref_124735) << 8 | ref_134552) << 8 | ref_134553) # MOV operation
    ref_183185 = ref_182575 # MOV operation
    ref_183197 = ref_177265 # MOV operation
    ref_183199 = (ref_183197 | ref_183185) # OR operation
    ref_188492 = ref_183199 # MOV operation
    ref_197052 = ((ref_13499) << 8 | ref_13500) # MOVZX operation
    ref_198316 = (ref_197052 & 0xFFFF) # MOVZX operation
    ref_206870 = ((ref_13493) << 8 | ref_13494) # MOVZX operation
    ref_215252 = (ref_206870 & 0xFFFF) # MOVZX operation
    ref_215254 = (((ref_215252 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
    ref_215255 = ((ref_215252 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
    ref_216688 = (ref_198316 & 0xFFFF) # MOVZX operation
    ref_225070 = (ref_216688 & 0xFFFF) # MOVZX operation
    ref_225072 = (((ref_225070 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
    ref_225073 = ((ref_225070 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
    ref_233624 = ((ref_13495) << 8 | ref_13496) # MOVZX operation
    ref_234888 = (ref_233624 & 0xFFFF) # MOVZX operation
    ref_243442 = ((ref_13497) << 8 | ref_13498) # MOVZX operation
    ref_251824 = (ref_243442 & 0xFFFF) # MOVZX operation
    ref_251826 = (((ref_251824 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
    ref_251827 = ((ref_251824 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
    ref_253260 = (ref_234888 & 0xFFFF) # MOVZX operation
    ref_261642 = (ref_253260 & 0xFFFF) # MOVZX operation
    ref_261644 = (((ref_261642 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
    ref_261645 = ((ref_261642 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
    ref_268264 = ref_33910 # MOV operation
    ref_268834 = ref_268264 # MOV operation
    ref_268848 = (0x7 & ref_268834) # AND operation
    ref_270131 = ref_268848 # MOV operation
    ref_270137 = ref_270131 # MOV operation
    ref_270141 = ((ref_270137 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_270148 = ref_270141 # MOV operation
    ref_275458 = ((((((((ref_225072) << 8 | ref_225073) << 8 | ref_251826) << 8 | ref_251827) << 8 | ref_261644) << 8 | ref_261645) << 8 | ref_215254) << 8 | ref_215255) # MOV operation
    ref_276068 = ref_275458 # MOV operation
    ref_276080 = ref_270148 # MOV operation
    ref_276082 = (ref_276080 | ref_276068) # OR operation
    ref_281375 = ref_276082 # MOV operation
    ref_286685 = ref_281375 # MOV operation
    ref_293395 = ref_33910 # MOV operation
    ref_294523 = ref_293395 # MOV operation
    ref_294529 = ref_294523 # MOV operation
    ref_294533 = (ref_294529 >> (0x1 & 0x3F)) # SHR operation
    ref_294540 = ref_294533 # MOV operation
    ref_295130 = ref_294540 # MOV operation
    ref_295144 = (0xF & ref_295130) # AND operation
    ref_295779 = ref_295144 # MOV operation
    ref_295793 = (0x1 | ref_295779) # OR operation
    ref_297110 = ref_295793 # MOV operation
    ref_297114 = ((0x40 - ref_297110) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_297122 = ref_297114 # MOV operation
    ref_297690 = ref_286685 # MOV operation
    ref_297694 = ref_297122 # MOV operation
    ref_297696 = ref_297690 # MOV operation
    ref_297698 = (ref_297694 & 0xFFFFFFFF) # MOV operation
    ref_297700 = ((ref_297696 << ((ref_297698 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_297707 = ref_297700 # MOV operation
    ref_303017 = ref_281375 # MOV operation
    ref_309727 = ref_33910 # MOV operation
    ref_310855 = ref_309727 # MOV operation
    ref_310861 = ref_310855 # MOV operation
    ref_310865 = (ref_310861 >> (0x1 & 0x3F)) # SHR operation
    ref_310872 = ref_310865 # MOV operation
    ref_311462 = ref_310872 # MOV operation
    ref_311476 = (0xF & ref_311462) # AND operation
    ref_312111 = ref_311476 # MOV operation
    ref_312125 = (0x1 | ref_312111) # OR operation
    ref_312568 = ref_303017 # MOV operation
    ref_312572 = ref_312125 # MOV operation
    ref_312574 = ref_312568 # MOV operation
    ref_312576 = (ref_312572 & 0xFFFFFFFF) # MOV operation
    ref_312578 = (ref_312574 >> ((ref_312576 & 0xFF) & 0x3F)) # SHR operation
    ref_312585 = ref_312578 # MOV operation
    ref_313215 = ref_312585 # MOV operation
    ref_313227 = ref_297707 # MOV operation
    ref_313229 = (ref_313227 | ref_313215) # OR operation
    ref_319964 = ref_188492 # MOV operation
    ref_325254 = ref_169361 # MOV operation
    ref_325924 = ref_325254 # MOV operation
    ref_325936 = ref_319964 # MOV operation
    ref_325938 = (ref_325936 ^ ref_325924) # XOR operation
    ref_327091 = ref_325938 # MOV operation
    ref_327097 = ref_327091 # MOV operation
    ref_327101 = (ref_327097 >> (0x3 & 0x3F)) # SHR operation
    ref_327108 = ref_327101 # MOV operation
    ref_327698 = ref_327108 # MOV operation
    ref_327712 = (0xF & ref_327698) # AND operation
    ref_328347 = ref_327712 # MOV operation
    ref_328361 = (0x1 | ref_328347) # OR operation
    ref_329678 = ref_328361 # MOV operation
    ref_329682 = ((0x40 - ref_329678) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_329690 = ref_329682 # MOV operation
    ref_330128 = ref_313229 # MOV operation
    ref_330132 = ref_329690 # MOV operation
    ref_330134 = ref_330128 # MOV operation
    ref_330136 = (ref_330132 & 0xFFFFFFFF) # MOV operation
    ref_330138 = (ref_330134 >> ((ref_330136 & 0xFF) & 0x3F)) # SHR operation
    ref_330145 = ref_330138 # MOV operation
    ref_335455 = ref_281375 # MOV operation
    ref_342165 = ref_33910 # MOV operation
    ref_343293 = ref_342165 # MOV operation
    ref_343299 = ref_343293 # MOV operation
    ref_343303 = (ref_343299 >> (0x1 & 0x3F)) # SHR operation
    ref_343310 = ref_343303 # MOV operation
    ref_343900 = ref_343310 # MOV operation
    ref_343914 = (0xF & ref_343900) # AND operation
    ref_344549 = ref_343914 # MOV operation
    ref_344563 = (0x1 | ref_344549) # OR operation
    ref_345880 = ref_344563 # MOV operation
    ref_345884 = ((0x40 - ref_345880) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_345892 = ref_345884 # MOV operation
    ref_346460 = ref_335455 # MOV operation
    ref_346464 = ref_345892 # MOV operation
    ref_346466 = ref_346460 # MOV operation
    ref_346468 = (ref_346464 & 0xFFFFFFFF) # MOV operation
    ref_346470 = ((ref_346466 << ((ref_346468 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_346477 = ref_346470 # MOV operation
    ref_351787 = ref_281375 # MOV operation
    ref_358497 = ref_33910 # MOV operation
    ref_359625 = ref_358497 # MOV operation
    ref_359631 = ref_359625 # MOV operation
    ref_359635 = (ref_359631 >> (0x1 & 0x3F)) # SHR operation
    ref_359642 = ref_359635 # MOV operation
    ref_360232 = ref_359642 # MOV operation
    ref_360246 = (0xF & ref_360232) # AND operation
    ref_360881 = ref_360246 # MOV operation
    ref_360895 = (0x1 | ref_360881) # OR operation
    ref_361338 = ref_351787 # MOV operation
    ref_361342 = ref_360895 # MOV operation
    ref_361344 = ref_361338 # MOV operation
    ref_361346 = (ref_361342 & 0xFFFFFFFF) # MOV operation
    ref_361348 = (ref_361344 >> ((ref_361346 & 0xFF) & 0x3F)) # SHR operation
    ref_361355 = ref_361348 # MOV operation
    ref_361985 = ref_361355 # MOV operation
    ref_361997 = ref_346477 # MOV operation
    ref_361999 = (ref_361997 | ref_361985) # OR operation
    ref_368734 = ref_188492 # MOV operation
    ref_374024 = ref_169361 # MOV operation
    ref_374694 = ref_374024 # MOV operation
    ref_374706 = ref_368734 # MOV operation
    ref_374708 = (ref_374706 ^ ref_374694) # XOR operation
    ref_375861 = ref_374708 # MOV operation
    ref_375867 = ref_375861 # MOV operation
    ref_375871 = (ref_375867 >> (0x3 & 0x3F)) # SHR operation
    ref_375878 = ref_375871 # MOV operation
    ref_376468 = ref_375878 # MOV operation
    ref_376482 = (0xF & ref_376468) # AND operation
    ref_377117 = ref_376482 # MOV operation
    ref_377131 = (0x1 | ref_377117) # OR operation
    ref_377704 = ref_361999 # MOV operation
    ref_377708 = ref_377131 # MOV operation
    ref_377710 = ref_377704 # MOV operation
    ref_377712 = (ref_377708 & 0xFFFFFFFF) # MOV operation
    ref_377714 = ((ref_377710 << ((ref_377712 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_377721 = ref_377714 # MOV operation
    ref_378351 = ref_377721 # MOV operation
    ref_378363 = ref_330145 # MOV operation
    ref_378365 = (ref_378363 | ref_378351) # OR operation
    ref_383582 = ref_378365 # MOV operation
    ref_384790 = ref_383582 # MOV operation
    ref_384792 = ref_384790 # MOV operation
    endb = ref_384792


else:
    ref_385067 = SymVar_0
    ref_385082 = ref_385067 # MOV operation
    ref_391839 = ref_385082 # MOV operation
    ref_392409 = ref_391839 # MOV operation
    ref_392423 = (0x222C2AFC & ref_392409) # AND operation
    ref_393018 = ref_392423 # MOV operation
    ref_393032 = ref_393018 # MOV operation
    ref_393034 = ((ref_393032 - 0x14582014) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_393042 = ref_393034 # MOV operation
    ref_398330 = ref_393042 # MOV operation
    ref_403555 = ref_385082 # MOV operation
    ref_404843 = ref_403555 # MOV operation
    ref_404849 = ((0x22722B13 + ref_404843) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_410875 = ref_398330 # MOV operation
    ref_412233 = ref_410875 # MOV operation
    ref_412239 = (((sx(0x40, 0x1DF2339F) * sx(0x40, ref_412233)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_412843 = ref_412239 # MOV operation
    ref_412845 = ((ref_412843 + 0x608C69) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_413449 = ref_404849 # MOV operation
    ref_413453 = ref_412845 # MOV operation
    ref_413455 = ((ref_413453 + ref_413449) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_418749 = ref_413455 # MOV operation
    ref_425394 = ref_385082 # MOV operation
    ref_425964 = ref_425394 # MOV operation
    ref_425978 = (0x140538E4 & ref_425964) # AND operation
    ref_426573 = ref_425978 # MOV operation
    ref_426587 = ref_426573 # MOV operation
    ref_426589 = ((ref_426587 - 0x5F1E4CE7) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_426597 = ref_426589 # MOV operation
    ref_431885 = ref_426597 # MOV operation
    ref_437110 = ref_385082 # MOV operation
    ref_442400 = ref_418749 # MOV operation
    ref_449110 = ref_431885 # MOV operation
    ref_450238 = ref_449110 # MOV operation
    ref_450244 = ref_450238 # MOV operation
    ref_450248 = (ref_450244 >> (0x3 & 0x3F)) # SHR operation
    ref_450255 = ref_450248 # MOV operation
    ref_450845 = ref_450255 # MOV operation
    ref_450859 = (0x7 & ref_450845) # AND operation
    ref_451494 = ref_450859 # MOV operation
    ref_451508 = (0x1 | ref_451494) # OR operation
    ref_451951 = ref_442400 # MOV operation
    ref_451955 = ref_451508 # MOV operation
    ref_451957 = ref_451951 # MOV operation
    ref_451959 = (ref_451955 & 0xFFFFFFFF) # MOV operation
    ref_451961 = (ref_451957 >> ((ref_451959 & 0xFF) & 0x3F)) # SHR operation
    ref_451968 = ref_451961 # MOV operation
    ref_452566 = ref_437110 # MOV operation
    ref_452570 = ref_451968 # MOV operation
    ref_452572 = ((ref_452570 + ref_452566) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_457866 = ref_452572 # MOV operation
    ref_488230 = ref_418749 # MOV operation
    ref_488800 = ref_488230 # MOV operation
    ref_488814 = (0x7 & ref_488800) # AND operation
    ref_490097 = ref_488814 # MOV operation
    ref_490103 = ref_490097 # MOV operation
    ref_490107 = ((ref_490103 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_490114 = ref_490107 # MOV operation
    ref_495424 = ref_398330 # MOV operation
    ref_496034 = ref_495424 # MOV operation
    ref_496046 = ref_490114 # MOV operation
    ref_496048 = (ref_496046 | ref_496034) # OR operation
    ref_501341 = ref_496048 # MOV operation
    ref_507969 = ref_418749 # MOV operation
    ref_508539 = ref_507969 # MOV operation
    ref_508553 = (0x7 & ref_508539) # AND operation
    ref_509836 = ref_508553 # MOV operation
    ref_509842 = ref_509836 # MOV operation
    ref_509846 = ((ref_509842 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_509853 = ref_509846 # MOV operation
    ref_515163 = ref_501341 # MOV operation
    ref_515773 = ref_515163 # MOV operation
    ref_515785 = ref_509853 # MOV operation
    ref_515787 = (ref_515785 | ref_515773) # OR operation
    ref_521080 = ref_515787 # MOV operation
    ref_526390 = ref_521080 # MOV operation
    ref_533100 = ref_418749 # MOV operation
    ref_534228 = ref_533100 # MOV operation
    ref_534234 = ref_534228 # MOV operation
    ref_534238 = (ref_534234 >> (0x1 & 0x3F)) # SHR operation
    ref_534245 = ref_534238 # MOV operation
    ref_534835 = ref_534245 # MOV operation
    ref_534849 = (0xF & ref_534835) # AND operation
    ref_535484 = ref_534849 # MOV operation
    ref_535498 = (0x1 | ref_535484) # OR operation
    ref_536815 = ref_535498 # MOV operation
    ref_536819 = ((0x40 - ref_536815) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_536827 = ref_536819 # MOV operation
    ref_537395 = ref_526390 # MOV operation
    ref_537399 = ref_536827 # MOV operation
    ref_537401 = ref_537395 # MOV operation
    ref_537403 = (ref_537399 & 0xFFFFFFFF) # MOV operation
    ref_537405 = ((ref_537401 << ((ref_537403 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_537412 = ref_537405 # MOV operation
    ref_542722 = ref_521080 # MOV operation
    ref_549432 = ref_418749 # MOV operation
    ref_550560 = ref_549432 # MOV operation
    ref_550566 = ref_550560 # MOV operation
    ref_550570 = (ref_550566 >> (0x1 & 0x3F)) # SHR operation
    ref_550577 = ref_550570 # MOV operation
    ref_551167 = ref_550577 # MOV operation
    ref_551181 = (0xF & ref_551167) # AND operation
    ref_551816 = ref_551181 # MOV operation
    ref_551830 = (0x1 | ref_551816) # OR operation
    ref_552273 = ref_542722 # MOV operation
    ref_552277 = ref_551830 # MOV operation
    ref_552279 = ref_552273 # MOV operation
    ref_552281 = (ref_552277 & 0xFFFFFFFF) # MOV operation
    ref_552283 = (ref_552279 >> ((ref_552281 & 0xFF) & 0x3F)) # SHR operation
    ref_552290 = ref_552283 # MOV operation
    ref_552920 = ref_552290 # MOV operation
    ref_552932 = ref_537412 # MOV operation
    ref_552934 = (ref_552932 | ref_552920) # OR operation
    ref_559669 = ref_457866 # MOV operation
    ref_564959 = ref_431885 # MOV operation
    ref_565629 = ref_564959 # MOV operation
    ref_565641 = ref_559669 # MOV operation
    ref_565643 = (ref_565641 ^ ref_565629) # XOR operation
    ref_566796 = ref_565643 # MOV operation
    ref_566802 = ref_566796 # MOV operation
    ref_566806 = (ref_566802 >> (0x3 & 0x3F)) # SHR operation
    ref_566813 = ref_566806 # MOV operation
    ref_567403 = ref_566813 # MOV operation
    ref_567417 = (0xF & ref_567403) # AND operation
    ref_568052 = ref_567417 # MOV operation
    ref_568066 = (0x1 | ref_568052) # OR operation
    ref_569383 = ref_568066 # MOV operation
    ref_569387 = ((0x40 - ref_569383) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_569395 = ref_569387 # MOV operation
    ref_569833 = ref_552934 # MOV operation
    ref_569837 = ref_569395 # MOV operation
    ref_569839 = ref_569833 # MOV operation
    ref_569841 = (ref_569837 & 0xFFFFFFFF) # MOV operation
    ref_569843 = (ref_569839 >> ((ref_569841 & 0xFF) & 0x3F)) # SHR operation
    ref_569850 = ref_569843 # MOV operation
    ref_575160 = ref_521080 # MOV operation
    ref_581870 = ref_418749 # MOV operation
    ref_582998 = ref_581870 # MOV operation
    ref_583004 = ref_582998 # MOV operation
    ref_583008 = (ref_583004 >> (0x1 & 0x3F)) # SHR operation
    ref_583015 = ref_583008 # MOV operation
    ref_583605 = ref_583015 # MOV operation
    ref_583619 = (0xF & ref_583605) # AND operation
    ref_584254 = ref_583619 # MOV operation
    ref_584268 = (0x1 | ref_584254) # OR operation
    ref_585585 = ref_584268 # MOV operation
    ref_585589 = ((0x40 - ref_585585) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_585597 = ref_585589 # MOV operation
    ref_586165 = ref_575160 # MOV operation
    ref_586169 = ref_585597 # MOV operation
    ref_586171 = ref_586165 # MOV operation
    ref_586173 = (ref_586169 & 0xFFFFFFFF) # MOV operation
    ref_586175 = ((ref_586171 << ((ref_586173 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_586182 = ref_586175 # MOV operation
    ref_591492 = ref_521080 # MOV operation
    ref_598202 = ref_418749 # MOV operation
    ref_599330 = ref_598202 # MOV operation
    ref_599336 = ref_599330 # MOV operation
    ref_599340 = (ref_599336 >> (0x1 & 0x3F)) # SHR operation
    ref_599347 = ref_599340 # MOV operation
    ref_599937 = ref_599347 # MOV operation
    ref_599951 = (0xF & ref_599937) # AND operation
    ref_600586 = ref_599951 # MOV operation
    ref_600600 = (0x1 | ref_600586) # OR operation
    ref_601043 = ref_591492 # MOV operation
    ref_601047 = ref_600600 # MOV operation
    ref_601049 = ref_601043 # MOV operation
    ref_601051 = (ref_601047 & 0xFFFFFFFF) # MOV operation
    ref_601053 = (ref_601049 >> ((ref_601051 & 0xFF) & 0x3F)) # SHR operation
    ref_601060 = ref_601053 # MOV operation
    ref_601690 = ref_601060 # MOV operation
    ref_601702 = ref_586182 # MOV operation
    ref_601704 = (ref_601702 | ref_601690) # OR operation
    ref_608439 = ref_457866 # MOV operation
    ref_613729 = ref_431885 # MOV operation
    ref_614399 = ref_613729 # MOV operation
    ref_614411 = ref_608439 # MOV operation
    ref_614413 = (ref_614411 ^ ref_614399) # XOR operation
    ref_615566 = ref_614413 # MOV operation
    ref_615572 = ref_615566 # MOV operation
    ref_615576 = (ref_615572 >> (0x3 & 0x3F)) # SHR operation
    ref_615583 = ref_615576 # MOV operation
    ref_616173 = ref_615583 # MOV operation
    ref_616187 = (0xF & ref_616173) # AND operation
    ref_616822 = ref_616187 # MOV operation
    ref_616836 = (0x1 | ref_616822) # OR operation
    ref_617409 = ref_601704 # MOV operation
    ref_617413 = ref_616836 # MOV operation
    ref_617415 = ref_617409 # MOV operation
    ref_617417 = (ref_617413 & 0xFFFFFFFF) # MOV operation
    ref_617419 = ((ref_617415 << ((ref_617417 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_617426 = ref_617419 # MOV operation
    ref_618056 = ref_617426 # MOV operation
    ref_618068 = ref_569850 # MOV operation
    ref_618070 = (ref_618068 | ref_618056) # OR operation
    ref_623287 = ref_618070 # MOV operation
    ref_624495 = ref_623287 # MOV operation
    ref_624497 = ref_624495 # MOV operation
    endb = ref_624497


print(endb & 0xffffffffffffffff)
