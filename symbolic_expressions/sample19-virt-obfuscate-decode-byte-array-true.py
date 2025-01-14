#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_145508 = ref_278 # MOV operation
ref_145584 = ref_145508 # MOV operation
ref_145598 = ((ref_145584 - 0x35CEDE6D) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_145606 = ref_145598 # MOV operation
ref_146532 = ref_145606 # MOV operation
ref_147365 = ref_278 # MOV operation
ref_147565 = ref_147365 # MOV operation
ref_147573 = ((((0x0) << 64 | ref_147565) / 0x7) & 0xFFFFFFFFFFFFFFFF) # DIV operation
ref_148500 = ref_147573 # MOV operation
ref_149333 = ref_278 # MOV operation
ref_150579 = ref_148500 # MOV operation
ref_150779 = ref_150579 # MOV operation
ref_150787 = (ref_150779 >> (0x3 & 0x3F)) # SHR operation
ref_150794 = ref_150787 # MOV operation
ref_151014 = ref_150794 # MOV operation
ref_151020 = (0xF & ref_151014) # AND operation
ref_151121 = ref_151020 # MOV operation
ref_151135 = (0x1 | ref_151121) # OR operation
ref_151364 = ref_151135 # MOV operation
ref_151366 = ((0x40 - ref_151364) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_151374 = ref_151366 # MOV operation
ref_151482 = ref_151374 # MOV operation
ref_151484 = (ref_151482 & 0xFFFFFFFF) # MOV operation
ref_151486 = (0x7A11169 >> ((ref_151484 & 0xFF) & 0x3F)) # SHR operation
ref_151493 = ref_151486 # MOV operation
ref_152643 = ref_148500 # MOV operation
ref_152843 = ref_152643 # MOV operation
ref_152851 = (ref_152843 >> (0x3 & 0x3F)) # SHR operation
ref_152858 = ref_152851 # MOV operation
ref_153078 = ref_152858 # MOV operation
ref_153084 = (0xF & ref_153078) # AND operation
ref_153185 = ref_153084 # MOV operation
ref_153199 = (0x1 | ref_153185) # OR operation
ref_153312 = ref_153199 # MOV operation
ref_153314 = (ref_153312 & 0xFFFFFFFF) # MOV operation
ref_153316 = ((0x7A11169 << ((ref_153314 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_153323 = ref_153316 # MOV operation
ref_153419 = ref_153323 # MOV operation
ref_153431 = ref_151493 # MOV operation
ref_153433 = (ref_153431 | ref_153419) # OR operation
ref_153658 = ref_153433 # MOV operation
ref_153666 = (ref_153658 >> (0x4 & 0x3F)) # SHR operation
ref_153673 = ref_153666 # MOV operation
ref_153893 = ref_153673 # MOV operation
ref_153899 = (0xF & ref_153893) # AND operation
ref_154000 = ref_153899 # MOV operation
ref_154014 = (0x1 | ref_154000) # OR operation
ref_154243 = ref_154014 # MOV operation
ref_154245 = ((0x40 - ref_154243) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_154253 = ref_154245 # MOV operation
ref_154357 = ref_149333 # MOV operation
ref_154361 = ref_154253 # MOV operation
ref_154363 = (ref_154361 & 0xFFFFFFFF) # MOV operation
ref_154365 = (ref_154357 >> ((ref_154363 & 0xFF) & 0x3F)) # SHR operation
ref_154372 = ref_154365 # MOV operation
ref_155205 = ref_278 # MOV operation
ref_156451 = ref_148500 # MOV operation
ref_156651 = ref_156451 # MOV operation
ref_156659 = (ref_156651 >> (0x3 & 0x3F)) # SHR operation
ref_156666 = ref_156659 # MOV operation
ref_156886 = ref_156666 # MOV operation
ref_156892 = (0xF & ref_156886) # AND operation
ref_156993 = ref_156892 # MOV operation
ref_157007 = (0x1 | ref_156993) # OR operation
ref_157236 = ref_157007 # MOV operation
ref_157238 = ((0x40 - ref_157236) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_157246 = ref_157238 # MOV operation
ref_157354 = ref_157246 # MOV operation
ref_157356 = (ref_157354 & 0xFFFFFFFF) # MOV operation
ref_157358 = (0x7A11169 >> ((ref_157356 & 0xFF) & 0x3F)) # SHR operation
ref_157365 = ref_157358 # MOV operation
ref_158515 = ref_148500 # MOV operation
ref_158715 = ref_158515 # MOV operation
ref_158723 = (ref_158715 >> (0x3 & 0x3F)) # SHR operation
ref_158730 = ref_158723 # MOV operation
ref_158950 = ref_158730 # MOV operation
ref_158956 = (0xF & ref_158950) # AND operation
ref_159057 = ref_158956 # MOV operation
ref_159071 = (0x1 | ref_159057) # OR operation
ref_159184 = ref_159071 # MOV operation
ref_159186 = (ref_159184 & 0xFFFFFFFF) # MOV operation
ref_159188 = ((0x7A11169 << ((ref_159186 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_159195 = ref_159188 # MOV operation
ref_159291 = ref_159195 # MOV operation
ref_159303 = ref_157365 # MOV operation
ref_159305 = (ref_159303 | ref_159291) # OR operation
ref_159530 = ref_159305 # MOV operation
ref_159538 = (ref_159530 >> (0x4 & 0x3F)) # SHR operation
ref_159545 = ref_159538 # MOV operation
ref_159765 = ref_159545 # MOV operation
ref_159771 = (0xF & ref_159765) # AND operation
ref_159872 = ref_159771 # MOV operation
ref_159886 = (0x1 | ref_159872) # OR operation
ref_159995 = ref_155205 # MOV operation
ref_159999 = ref_159886 # MOV operation
ref_160001 = (ref_159999 & 0xFFFFFFFF) # MOV operation
ref_160003 = ((ref_159995 << ((ref_160001 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_160010 = ref_160003 # MOV operation
ref_160106 = ref_160010 # MOV operation
ref_160118 = ref_154372 # MOV operation
ref_160120 = (ref_160118 | ref_160106) # OR operation
ref_161051 = ref_160120 # MOV operation
ref_162000 = ref_278 # MOV operation
ref_162076 = ref_162000 # MOV operation
ref_162090 = ((ref_162076 - 0x297EE8A1) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_162098 = ref_162090 # MOV operation
ref_162318 = ref_162098 # MOV operation
ref_162324 = (((sx(0x40, 0x1471C5DA) * sx(0x40, ref_162318)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_163252 = ref_162324 # MOV operation
ref_163254 = ((ref_163252 >> 56) & 0xFF) # Byte reference - MOV operation
ref_163255 = ((ref_163252 >> 48) & 0xFF) # Byte reference - MOV operation
ref_163256 = ((ref_163252 >> 40) & 0xFF) # Byte reference - MOV operation
ref_163257 = ((ref_163252 >> 32) & 0xFF) # Byte reference - MOV operation
ref_163258 = ((ref_163252 >> 24) & 0xFF) # Byte reference - MOV operation
ref_163259 = ((ref_163252 >> 16) & 0xFF) # Byte reference - MOV operation
ref_163260 = ((ref_163252 >> 8) & 0xFF) # Byte reference - MOV operation
ref_163261 = (ref_163252 & 0xFF) # Byte reference - MOV operation
ref_164904 = ((ref_163256) << 8 | ref_163257) # MOVZX operation
ref_164982 = (ref_164904 & 0xFFFF) # MOVZX operation
ref_167928 = ((ref_163258) << 8 | ref_163259) # MOVZX operation
ref_168006 = (ref_167928 & 0xFFFF) # MOVZX operation
ref_169652 = (ref_164982 & 0xFFFF) # MOVZX operation
ref_169730 = (ref_169652 & 0xFFFF) # MOVZX operation
ref_169732 = (((ref_169730 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_169733 = ((ref_169730 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_177970 = ref_161051 # MOV operation
ref_178170 = ref_177970 # MOV operation
ref_178176 = (0x1F & ref_178170) # AND operation
ref_178401 = ref_178176 # MOV operation
ref_178409 = ((ref_178401 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_178416 = ref_178409 # MOV operation
ref_179334 = ref_148500 # MOV operation
ref_179410 = ref_179334 # MOV operation
ref_179422 = ref_178416 # MOV operation
ref_179424 = (ref_179422 | ref_179410) # OR operation
ref_180355 = ref_179424 # MOV operation
ref_181273 = ref_180355 # MOV operation
ref_181473 = ref_181273 # MOV operation
ref_181479 = (0xF & ref_181473) # AND operation
ref_181704 = ref_181479 # MOV operation
ref_181712 = ((ref_181704 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_181719 = ref_181712 # MOV operation
ref_182637 = ref_180355 # MOV operation
ref_182713 = ref_182637 # MOV operation
ref_182725 = ref_181719 # MOV operation
ref_182727 = (ref_182725 | ref_182713) # OR operation
ref_183658 = ref_182727 # MOV operation
ref_185394 = ((ref_163254) << 8 | ref_163255) # MOVZX operation
ref_185472 = (ref_185394 & 0xFFFF) # MOVZX operation
ref_188418 = ((ref_163260) << 8 | ref_163261) # MOVZX operation
ref_188496 = (ref_188418 & 0xFFFF) # MOVZX operation
ref_188498 = (((ref_188496 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_188499 = ((ref_188496 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_190142 = (ref_185472 & 0xFFFF) # MOVZX operation
ref_190220 = (ref_190142 & 0xFFFF) # MOVZX operation
ref_191866 = (ref_190220 & 0xFFFF) # MOVZX operation
ref_191944 = (ref_191866 & 0xFFFF) # MOVZX operation
ref_194890 = (ref_168006 & 0xFFFF) # MOVZX operation
ref_194968 = (ref_194890 & 0xFFFF) # MOVZX operation
ref_194970 = (((ref_194968 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_194971 = ((ref_194968 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_196614 = (ref_191944 & 0xFFFF) # MOVZX operation
ref_196692 = (ref_196614 & 0xFFFF) # MOVZX operation
ref_196694 = (((ref_196692 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_196695 = ((ref_196692 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_197604 = ref_146532 # MOV operation
ref_198618 = ref_183658 # MOV operation
ref_198818 = ref_198618 # MOV operation
ref_198824 = (0xF & ref_198818) # AND operation
ref_198925 = ref_198824 # MOV operation
ref_198939 = (0x1 | ref_198925) # OR operation
ref_199168 = ref_198939 # MOV operation
ref_199170 = ((0x40 - ref_199168) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_199178 = ref_199170 # MOV operation
ref_199282 = ref_197604 # MOV operation
ref_199286 = ref_199178 # MOV operation
ref_199288 = (ref_199286 & 0xFFFFFFFF) # MOV operation
ref_199290 = (ref_199282 >> ((ref_199288 & 0xFF) & 0x3F)) # SHR operation
ref_199297 = ref_199290 # MOV operation
ref_200215 = ref_146532 # MOV operation
ref_201229 = ref_183658 # MOV operation
ref_201429 = ref_201229 # MOV operation
ref_201435 = (0xF & ref_201429) # AND operation
ref_201536 = ref_201435 # MOV operation
ref_201550 = (0x1 | ref_201536) # OR operation
ref_201659 = ref_200215 # MOV operation
ref_201663 = ref_201550 # MOV operation
ref_201665 = (ref_201663 & 0xFFFFFFFF) # MOV operation
ref_201667 = ((ref_201659 << ((ref_201665 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_201674 = ref_201667 # MOV operation
ref_201770 = ref_201674 # MOV operation
ref_201782 = ref_199297 # MOV operation
ref_201784 = (ref_201782 | ref_201770) # OR operation
ref_202823 = ref_161051 # MOV operation
ref_203837 = ((((((((ref_188498) << 8 | ref_188499) << 8 | ref_196694) << 8 | ref_196695) << 8 | ref_169732) << 8 | ref_169733) << 8 | ref_194970) << 8 | ref_194971) # MOV operation
ref_204037 = ref_203837 # MOV operation
ref_204045 = (ref_204037 >> (0x2 & 0x3F)) # SHR operation
ref_204052 = ref_204045 # MOV operation
ref_204272 = ref_204052 # MOV operation
ref_204278 = (0xF & ref_204272) # AND operation
ref_204379 = ref_204278 # MOV operation
ref_204393 = (0x1 | ref_204379) # OR operation
ref_204622 = ref_204393 # MOV operation
ref_204624 = ((0x40 - ref_204622) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_204632 = ref_204624 # MOV operation
ref_204736 = ref_202823 # MOV operation
ref_204740 = ref_204632 # MOV operation
ref_204742 = (ref_204740 & 0xFFFFFFFF) # MOV operation
ref_204744 = (ref_204736 >> ((ref_204742 & 0xFF) & 0x3F)) # SHR operation
ref_204751 = ref_204744 # MOV operation
ref_205669 = ref_161051 # MOV operation
ref_206683 = ((((((((ref_188498) << 8 | ref_188499) << 8 | ref_196694) << 8 | ref_196695) << 8 | ref_169732) << 8 | ref_169733) << 8 | ref_194970) << 8 | ref_194971) # MOV operation
ref_206883 = ref_206683 # MOV operation
ref_206891 = (ref_206883 >> (0x2 & 0x3F)) # SHR operation
ref_206898 = ref_206891 # MOV operation
ref_207118 = ref_206898 # MOV operation
ref_207124 = (0xF & ref_207118) # AND operation
ref_207225 = ref_207124 # MOV operation
ref_207239 = (0x1 | ref_207225) # OR operation
ref_207348 = ref_205669 # MOV operation
ref_207352 = ref_207239 # MOV operation
ref_207354 = (ref_207352 & 0xFFFFFFFF) # MOV operation
ref_207356 = ((ref_207348 << ((ref_207354 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_207363 = ref_207356 # MOV operation
ref_207459 = ref_207363 # MOV operation
ref_207471 = ref_204751 # MOV operation
ref_207473 = (ref_207471 | ref_207459) # OR operation
ref_207698 = ref_207473 # MOV operation
ref_207706 = (ref_207698 >> (0x4 & 0x3F)) # SHR operation
ref_207713 = ref_207706 # MOV operation
ref_207933 = ref_207713 # MOV operation
ref_207939 = (0xF & ref_207933) # AND operation
ref_208040 = ref_207939 # MOV operation
ref_208054 = (0x1 | ref_208040) # OR operation
ref_208283 = ref_208054 # MOV operation
ref_208285 = ((0x40 - ref_208283) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_208293 = ref_208285 # MOV operation
ref_208397 = ref_201784 # MOV operation
ref_208401 = ref_208293 # MOV operation
ref_208403 = (ref_208401 & 0xFFFFFFFF) # MOV operation
ref_208405 = ((ref_208397 << ((ref_208403 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_208412 = ref_208405 # MOV operation
ref_209330 = ref_146532 # MOV operation
ref_210344 = ref_183658 # MOV operation
ref_210544 = ref_210344 # MOV operation
ref_210550 = (0xF & ref_210544) # AND operation
ref_210651 = ref_210550 # MOV operation
ref_210665 = (0x1 | ref_210651) # OR operation
ref_210894 = ref_210665 # MOV operation
ref_210896 = ((0x40 - ref_210894) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_210904 = ref_210896 # MOV operation
ref_211008 = ref_209330 # MOV operation
ref_211012 = ref_210904 # MOV operation
ref_211014 = (ref_211012 & 0xFFFFFFFF) # MOV operation
ref_211016 = (ref_211008 >> ((ref_211014 & 0xFF) & 0x3F)) # SHR operation
ref_211023 = ref_211016 # MOV operation
ref_211941 = ref_146532 # MOV operation
ref_212955 = ref_183658 # MOV operation
ref_213155 = ref_212955 # MOV operation
ref_213161 = (0xF & ref_213155) # AND operation
ref_213262 = ref_213161 # MOV operation
ref_213276 = (0x1 | ref_213262) # OR operation
ref_213385 = ref_211941 # MOV operation
ref_213389 = ref_213276 # MOV operation
ref_213391 = (ref_213389 & 0xFFFFFFFF) # MOV operation
ref_213393 = ((ref_213385 << ((ref_213391 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_213400 = ref_213393 # MOV operation
ref_213496 = ref_213400 # MOV operation
ref_213508 = ref_211023 # MOV operation
ref_213510 = (ref_213508 | ref_213496) # OR operation
ref_214549 = ref_161051 # MOV operation
ref_215563 = ((((((((ref_188498) << 8 | ref_188499) << 8 | ref_196694) << 8 | ref_196695) << 8 | ref_169732) << 8 | ref_169733) << 8 | ref_194970) << 8 | ref_194971) # MOV operation
ref_215763 = ref_215563 # MOV operation
ref_215771 = (ref_215763 >> (0x2 & 0x3F)) # SHR operation
ref_215778 = ref_215771 # MOV operation
ref_215998 = ref_215778 # MOV operation
ref_216004 = (0xF & ref_215998) # AND operation
ref_216105 = ref_216004 # MOV operation
ref_216119 = (0x1 | ref_216105) # OR operation
ref_216348 = ref_216119 # MOV operation
ref_216350 = ((0x40 - ref_216348) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_216358 = ref_216350 # MOV operation
ref_216462 = ref_214549 # MOV operation
ref_216466 = ref_216358 # MOV operation
ref_216468 = (ref_216466 & 0xFFFFFFFF) # MOV operation
ref_216470 = (ref_216462 >> ((ref_216468 & 0xFF) & 0x3F)) # SHR operation
ref_216477 = ref_216470 # MOV operation
ref_217395 = ref_161051 # MOV operation
ref_218409 = ((((((((ref_188498) << 8 | ref_188499) << 8 | ref_196694) << 8 | ref_196695) << 8 | ref_169732) << 8 | ref_169733) << 8 | ref_194970) << 8 | ref_194971) # MOV operation
ref_218609 = ref_218409 # MOV operation
ref_218617 = (ref_218609 >> (0x2 & 0x3F)) # SHR operation
ref_218624 = ref_218617 # MOV operation
ref_218844 = ref_218624 # MOV operation
ref_218850 = (0xF & ref_218844) # AND operation
ref_218951 = ref_218850 # MOV operation
ref_218965 = (0x1 | ref_218951) # OR operation
ref_219074 = ref_217395 # MOV operation
ref_219078 = ref_218965 # MOV operation
ref_219080 = (ref_219078 & 0xFFFFFFFF) # MOV operation
ref_219082 = ((ref_219074 << ((ref_219080 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_219089 = ref_219082 # MOV operation
ref_219185 = ref_219089 # MOV operation
ref_219197 = ref_216477 # MOV operation
ref_219199 = (ref_219197 | ref_219185) # OR operation
ref_219424 = ref_219199 # MOV operation
ref_219432 = (ref_219424 >> (0x4 & 0x3F)) # SHR operation
ref_219439 = ref_219432 # MOV operation
ref_219659 = ref_219439 # MOV operation
ref_219665 = (0xF & ref_219659) # AND operation
ref_219766 = ref_219665 # MOV operation
ref_219780 = (0x1 | ref_219766) # OR operation
ref_219889 = ref_213510 # MOV operation
ref_219893 = ref_219780 # MOV operation
ref_219895 = (ref_219893 & 0xFFFFFFFF) # MOV operation
ref_219897 = (ref_219889 >> ((ref_219895 & 0xFF) & 0x3F)) # SHR operation
ref_219904 = ref_219897 # MOV operation
ref_220000 = ref_219904 # MOV operation
ref_220012 = ref_208412 # MOV operation
ref_220014 = (ref_220012 | ref_220000) # OR operation
ref_220869 = ref_220014 # MOV operation
ref_221080 = ref_220869 # MOV operation
ref_221082 = ref_221080 # MOV operation

print(ref_221082 & 0xffffffffffffffff)
