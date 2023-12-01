#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])

ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_106042 = ref_278 # MOV operation
ref_106242 = ref_106042 # MOV operation
ref_106248 = (0x1D2C27F0 | ref_106242) # OR operation
ref_106349 = ref_106248 # MOV operation
ref_106363 = ((ref_106349 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_107201 = ref_278 # MOV operation
ref_107401 = ref_107201 # MOV operation
ref_107407 = (0x1D2C27F0 | ref_107401) # OR operation
ref_107632 = ref_107407 # MOV operation
ref_107640 = (ref_107632 >> (0x37 & 0x3F)) # SHR operation
ref_107647 = ref_107640 # MOV operation
ref_107751 = ref_106363 # MOV operation
ref_107755 = ref_107647 # MOV operation
ref_107757 = (ref_107755 | ref_107751) # OR operation
ref_108688 = ref_107757 # MOV operation
ref_109521 = ref_278 # MOV operation
ref_110535 = ref_108688 # MOV operation
ref_110611 = ref_110535 # MOV operation
ref_110625 = ((ref_110611 << (0xD & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_111548 = ref_108688 # MOV operation
ref_111748 = ref_111548 # MOV operation
ref_111756 = (ref_111748 >> (0x33 & 0x3F)) # SHR operation
ref_111763 = ref_111756 # MOV operation
ref_111867 = ref_110625 # MOV operation
ref_111871 = ref_111763 # MOV operation
ref_111873 = (ref_111871 | ref_111867) # OR operation
ref_111982 = ref_109521 # MOV operation
ref_111986 = ref_111873 # MOV operation
ref_111988 = (ref_111986 | ref_111982) # OR operation
ref_112919 = ref_111988 # MOV operation
ref_113868 = ref_278 # MOV operation
ref_113944 = ref_113868 # MOV operation
ref_113958 = ((0x6402BE2 + ref_113944) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_114890 = ref_113958 # MOV operation
ref_115723 = ref_278 # MOV operation
ref_115923 = ref_115723 # MOV operation
ref_115929 = (0x3544223F | ref_115923) # OR operation
ref_116968 = ref_114890 # MOV operation
ref_117866 = ref_112919 # MOV operation
ref_117950 = ref_116968 # MOV operation
ref_117954 = ref_117866 # MOV operation
ref_117956 = (((sx(0x40, ref_117954) * sx(0x40, ref_117950)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_118066 = ref_117956 # MOV operation
ref_118068 = (((sx(0x40, ref_118066) * sx(0x40, 0x3BE31211)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_118174 = ref_115929 # MOV operation
ref_118178 = ref_118068 # MOV operation
ref_118180 = (((sx(0x40, ref_118178) * sx(0x40, ref_118174)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_119108 = ref_118180 # MOV operation
ref_120026 = ref_114890 # MOV operation
ref_121156 = ref_119108 # MOV operation
ref_121232 = ref_121156 # MOV operation
ref_121246 = (0x1F & ref_121232) # AND operation
ref_121347 = ref_121246 # MOV operation
ref_121361 = ((ref_121347 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_121470 = ref_120026 # MOV operation
ref_121474 = ref_121361 # MOV operation
ref_121476 = (ref_121474 | ref_121470) # OR operation
ref_122407 = ref_121476 # MOV operation
ref_123525 = ref_112919 # MOV operation
ref_123725 = ref_123525 # MOV operation
ref_123733 = (ref_123725 >> (0x1 & 0x3F)) # SHR operation
ref_123740 = ref_123733 # MOV operation
ref_123836 = ref_123740 # MOV operation
ref_123850 = (0xF & ref_123836) # AND operation
ref_124075 = ref_123850 # MOV operation
ref_124081 = (0x1 | ref_124075) # OR operation
ref_125004 = ref_108688 # MOV operation
ref_125080 = ref_125004 # MOV operation
ref_125092 = ref_124081 # MOV operation
ref_125094 = ((ref_125080 << ((ref_125092 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_126017 = ref_108688 # MOV operation
ref_127031 = ref_112919 # MOV operation
ref_127231 = ref_127031 # MOV operation
ref_127239 = (ref_127231 >> (0x1 & 0x3F)) # SHR operation
ref_127246 = ref_127239 # MOV operation
ref_127342 = ref_127246 # MOV operation
ref_127356 = (0xF & ref_127342) # AND operation
ref_127581 = ref_127356 # MOV operation
ref_127587 = (0x1 | ref_127581) # OR operation
ref_127816 = ref_127587 # MOV operation
ref_127818 = ((0x40 - ref_127816) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_127826 = ref_127818 # MOV operation
ref_127930 = ref_126017 # MOV operation
ref_127934 = ref_127826 # MOV operation
ref_127936 = (ref_127934 & 0xFFFFFFFF) # MOV operation
ref_127938 = (ref_127930 >> ((ref_127936 & 0xFF) & 0x3F)) # SHR operation
ref_127945 = ref_127938 # MOV operation
ref_128049 = ref_125094 # MOV operation
ref_128053 = ref_127945 # MOV operation
ref_128055 = (ref_128053 | ref_128049) # OR operation
ref_128978 = ref_122407 # MOV operation
ref_129992 = ref_119108 # MOV operation
ref_130192 = ref_129992 # MOV operation
ref_130200 = (ref_130192 >> (0x3 & 0x3F)) # SHR operation
ref_130207 = ref_130200 # MOV operation
ref_130303 = ref_130207 # MOV operation
ref_130317 = (0x7 & ref_130303) # AND operation
ref_130542 = ref_130317 # MOV operation
ref_130548 = (0x1 | ref_130542) # OR operation
ref_130657 = ref_128978 # MOV operation
ref_130661 = ref_130548 # MOV operation
ref_130663 = (ref_130661 & 0xFFFFFFFF) # MOV operation
ref_130665 = (ref_130657 >> ((ref_130663 & 0xFF) & 0x3F)) # SHR operation
ref_130672 = ref_130665 # MOV operation
ref_130776 = ref_128055 # MOV operation
ref_130780 = ref_130672 # MOV operation
ref_130782 = ((ref_130776 - ref_130780) & 0xFFFFFFFFFFFFFFFF) # CMP operation
ref_130784 = ((((ref_130776 ^ (ref_130780 ^ ref_130782)) ^ ((ref_130776 ^ ref_130782) & (ref_130776 ^ ref_130780))) >> 63) & 0x1) # Carry flag
ref_130788 = (0x1 if (ref_130782 == 0x0) else 0x0) # Zero flag
ref_130790 = ((((ref_130780 >> 8) & 0xFFFFFFFFFFFFFF)) << 8 | (0x1 if ((ref_130784 | ref_130788) == 0x1) else 0x0)) # SETBE operation
ref_130792 = (ref_130790 & 0xFF) # MOVZX operation
ref_130880 = (ref_130792 & 0xFFFFFFFF) # MOV operation
ref_130882 = ((ref_130880 & 0xFFFFFFFF) & (ref_130880 & 0xFFFFFFFF)) # TEST operation
ref_130887 = (0x1 if (ref_130882 == 0x0) else 0x0) # Zero flag
ref_130889 = (0x165B if (ref_130887 == 0x1) else 0x163D) # Program Counter


if (ref_130887 == 0x1):
    ref_263 = SymVar_0
    ref_278 = ref_263 # MOV operation
    ref_106042 = ref_278 # MOV operation
    ref_106242 = ref_106042 # MOV operation
    ref_106248 = (0x1D2C27F0 | ref_106242) # OR operation
    ref_106349 = ref_106248 # MOV operation
    ref_106363 = ((ref_106349 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_107201 = ref_278 # MOV operation
    ref_107401 = ref_107201 # MOV operation
    ref_107407 = (0x1D2C27F0 | ref_107401) # OR operation
    ref_107632 = ref_107407 # MOV operation
    ref_107640 = (ref_107632 >> (0x37 & 0x3F)) # SHR operation
    ref_107647 = ref_107640 # MOV operation
    ref_107751 = ref_106363 # MOV operation
    ref_107755 = ref_107647 # MOV operation
    ref_107757 = (ref_107755 | ref_107751) # OR operation
    ref_108688 = ref_107757 # MOV operation
    ref_109521 = ref_278 # MOV operation
    ref_110535 = ref_108688 # MOV operation
    ref_110611 = ref_110535 # MOV operation
    ref_110625 = ((ref_110611 << (0xD & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_111548 = ref_108688 # MOV operation
    ref_111748 = ref_111548 # MOV operation
    ref_111756 = (ref_111748 >> (0x33 & 0x3F)) # SHR operation
    ref_111763 = ref_111756 # MOV operation
    ref_111867 = ref_110625 # MOV operation
    ref_111871 = ref_111763 # MOV operation
    ref_111873 = (ref_111871 | ref_111867) # OR operation
    ref_111982 = ref_109521 # MOV operation
    ref_111986 = ref_111873 # MOV operation
    ref_111988 = (ref_111986 | ref_111982) # OR operation
    ref_112919 = ref_111988 # MOV operation
    ref_113868 = ref_278 # MOV operation
    ref_113944 = ref_113868 # MOV operation
    ref_113958 = ((0x6402BE2 + ref_113944) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_114890 = ref_113958 # MOV operation
    ref_115723 = ref_278 # MOV operation
    ref_115923 = ref_115723 # MOV operation
    ref_115929 = (0x3544223F | ref_115923) # OR operation
    ref_116968 = ref_114890 # MOV operation
    ref_117866 = ref_112919 # MOV operation
    ref_117950 = ref_116968 # MOV operation
    ref_117954 = ref_117866 # MOV operation
    ref_117956 = (((sx(0x40, ref_117954) * sx(0x40, ref_117950)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_118066 = ref_117956 # MOV operation
    ref_118068 = (((sx(0x40, ref_118066) * sx(0x40, 0x3BE31211)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_118174 = ref_115929 # MOV operation
    ref_118178 = ref_118068 # MOV operation
    ref_118180 = (((sx(0x40, ref_118178) * sx(0x40, ref_118174)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_119108 = ref_118180 # MOV operation
    ref_120026 = ref_114890 # MOV operation
    ref_121156 = ref_119108 # MOV operation
    ref_121232 = ref_121156 # MOV operation
    ref_121246 = (0x1F & ref_121232) # AND operation
    ref_121347 = ref_121246 # MOV operation
    ref_121361 = ((ref_121347 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_121470 = ref_120026 # MOV operation
    ref_121474 = ref_121361 # MOV operation
    ref_121476 = (ref_121474 | ref_121470) # OR operation
    ref_122407 = ref_121476 # MOV operation
    ref_131900 = ref_112919 # MOV operation
    ref_133030 = ref_112919 # MOV operation
    ref_133106 = ref_133030 # MOV operation
    ref_133120 = (0xF & ref_133106) # AND operation
    ref_133221 = ref_133120 # MOV operation
    ref_133235 = ((ref_133221 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_133344 = ref_131900 # MOV operation
    ref_133348 = ref_133235 # MOV operation
    ref_133350 = (ref_133348 | ref_133344) # OR operation
    ref_134281 = ref_133350 # MOV operation
    ref_135399 = ref_134281 # MOV operation
    ref_135599 = ref_135399 # MOV operation
    ref_135607 = (ref_135599 >> (0x3 & 0x3F)) # SHR operation
    ref_135614 = ref_135607 # MOV operation
    ref_135710 = ref_135614 # MOV operation
    ref_135724 = (0xF & ref_135710) # AND operation
    ref_135949 = ref_135724 # MOV operation
    ref_135955 = (0x1 | ref_135949) # OR operation
    ref_136878 = ref_108688 # MOV operation
    ref_136954 = ref_136878 # MOV operation
    ref_136966 = ref_135955 # MOV operation
    ref_136968 = ((ref_136954 << ((ref_136966 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_137891 = ref_108688 # MOV operation
    ref_138905 = ref_134281 # MOV operation
    ref_139105 = ref_138905 # MOV operation
    ref_139113 = (ref_139105 >> (0x3 & 0x3F)) # SHR operation
    ref_139120 = ref_139113 # MOV operation
    ref_139216 = ref_139120 # MOV operation
    ref_139230 = (0xF & ref_139216) # AND operation
    ref_139455 = ref_139230 # MOV operation
    ref_139461 = (0x1 | ref_139455) # OR operation
    ref_139690 = ref_139461 # MOV operation
    ref_139692 = ((0x40 - ref_139690) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_139700 = ref_139692 # MOV operation
    ref_139804 = ref_137891 # MOV operation
    ref_139808 = ref_139700 # MOV operation
    ref_139810 = (ref_139808 & 0xFFFFFFFF) # MOV operation
    ref_139812 = (ref_139804 >> ((ref_139810 & 0xFF) & 0x3F)) # SHR operation
    ref_139819 = ref_139812 # MOV operation
    ref_139923 = ref_136968 # MOV operation
    ref_139927 = ref_139819 # MOV operation
    ref_139929 = (ref_139927 | ref_139923) # OR operation
    ref_140852 = ref_122407 # MOV operation
    ref_141866 = ref_119108 # MOV operation
    ref_141942 = ref_141866 # MOV operation
    ref_141956 = ((0x369A4780 + ref_141942) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_142066 = ref_140852 # MOV operation
    ref_142070 = ref_141956 # MOV operation
    ref_142072 = (((sx(0x40, ref_142070) * sx(0x40, ref_142066)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_142178 = ref_139929 # MOV operation
    ref_142182 = ref_142072 # MOV operation
    ref_142184 = (((sx(0x40, ref_142182) * sx(0x40, ref_142178)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_143036 = ref_142184 # MOV operation
    ref_143247 = ref_143036 # MOV operation
    ref_143249 = ref_143247 # MOV operation
    endb = ref_143249


else:
    ref_143569 = SymVar_0
    ref_143584 = ref_143569 # MOV operation
    ref_249353 = ref_143584 # MOV operation
    ref_249553 = ref_249353 # MOV operation
    ref_249559 = (0x1D2C27F0 | ref_249553) # OR operation
    ref_249660 = ref_249559 # MOV operation
    ref_249674 = ((ref_249660 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_250512 = ref_143584 # MOV operation
    ref_250712 = ref_250512 # MOV operation
    ref_250718 = (0x1D2C27F0 | ref_250712) # OR operation
    ref_250943 = ref_250718 # MOV operation
    ref_250951 = (ref_250943 >> (0x37 & 0x3F)) # SHR operation
    ref_250958 = ref_250951 # MOV operation
    ref_251062 = ref_249674 # MOV operation
    ref_251066 = ref_250958 # MOV operation
    ref_251068 = (ref_251066 | ref_251062) # OR operation
    ref_251999 = ref_251068 # MOV operation
    ref_252832 = ref_143584 # MOV operation
    ref_253846 = ref_251999 # MOV operation
    ref_253922 = ref_253846 # MOV operation
    ref_253936 = ((ref_253922 << (0xD & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_254859 = ref_251999 # MOV operation
    ref_255059 = ref_254859 # MOV operation
    ref_255067 = (ref_255059 >> (0x33 & 0x3F)) # SHR operation
    ref_255074 = ref_255067 # MOV operation
    ref_255178 = ref_253936 # MOV operation
    ref_255182 = ref_255074 # MOV operation
    ref_255184 = (ref_255182 | ref_255178) # OR operation
    ref_255293 = ref_252832 # MOV operation
    ref_255297 = ref_255184 # MOV operation
    ref_255299 = (ref_255297 | ref_255293) # OR operation
    ref_256230 = ref_255299 # MOV operation
    ref_256232 = ((ref_256230 >> 56) & 0xFF) # Byte reference - MOV operation
    ref_256233 = ((ref_256230 >> 48) & 0xFF) # Byte reference - MOV operation
    ref_256234 = ((ref_256230 >> 40) & 0xFF) # Byte reference - MOV operation
    ref_256235 = ((ref_256230 >> 32) & 0xFF) # Byte reference - MOV operation
    ref_256236 = ((ref_256230 >> 24) & 0xFF) # Byte reference - MOV operation
    ref_256237 = ((ref_256230 >> 16) & 0xFF) # Byte reference - MOV operation
    ref_256238 = ((ref_256230 >> 8) & 0xFF) # Byte reference - MOV operation
    ref_256239 = (ref_256230 & 0xFF) # Byte reference - MOV operation
    ref_257179 = ref_143584 # MOV operation
    ref_257255 = ref_257179 # MOV operation
    ref_257269 = ((0x6402BE2 + ref_257255) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_258201 = ref_257269 # MOV operation
    ref_259034 = ref_143584 # MOV operation
    ref_259234 = ref_259034 # MOV operation
    ref_259240 = (0x3544223F | ref_259234) # OR operation
    ref_260279 = ref_258201 # MOV operation
    ref_261177 = ref_256230 # MOV operation
    ref_261261 = ref_260279 # MOV operation
    ref_261265 = ref_261177 # MOV operation
    ref_261267 = (((sx(0x40, ref_261265) * sx(0x40, ref_261261)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_261377 = ref_261267 # MOV operation
    ref_261379 = (((sx(0x40, ref_261377) * sx(0x40, 0x3BE31211)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_261485 = ref_259240 # MOV operation
    ref_261489 = ref_261379 # MOV operation
    ref_261491 = (((sx(0x40, ref_261489) * sx(0x40, ref_261485)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_262419 = ref_261491 # MOV operation
    ref_263337 = ref_258201 # MOV operation
    ref_264467 = ref_262419 # MOV operation
    ref_264543 = ref_264467 # MOV operation
    ref_264557 = (0x1F & ref_264543) # AND operation
    ref_264658 = ref_264557 # MOV operation
    ref_264672 = ((ref_264658 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_264781 = ref_263337 # MOV operation
    ref_264785 = ref_264672 # MOV operation
    ref_264787 = (ref_264785 | ref_264781) # OR operation
    ref_265718 = ref_264787 # MOV operation
    ref_275134 = ref_262419 # MOV operation
    ref_275334 = ref_275134 # MOV operation
    ref_275342 = ((((0x0) << 64 | ref_275334) / 0x8) & 0xFFFFFFFFFFFFFFFF) # DIV operation
    ref_276269 = ref_275342 # MOV operation
    ref_276271 = ((ref_276269 >> 56) & 0xFF) # Byte reference - MOV operation
    ref_276272 = ((ref_276269 >> 48) & 0xFF) # Byte reference - MOV operation
    ref_276273 = ((ref_276269 >> 40) & 0xFF) # Byte reference - MOV operation
    ref_276274 = ((ref_276269 >> 32) & 0xFF) # Byte reference - MOV operation
    ref_276275 = ((ref_276269 >> 24) & 0xFF) # Byte reference - MOV operation
    ref_276276 = ((ref_276269 >> 16) & 0xFF) # Byte reference - MOV operation
    ref_276277 = ((ref_276269 >> 8) & 0xFF) # Byte reference - MOV operation
    ref_276278 = (ref_276269 & 0xFF) # Byte reference - MOV operation
    ref_277921 = ref_256237 # MOVZX operation
    ref_277997 = (ref_277921 & 0xFF) # MOVZX operation
    ref_280941 = ref_256234 # MOVZX operation
    ref_281017 = (ref_280941 & 0xFF) # MOVZX operation
    ref_281019 = (ref_281017 & 0xFF) # Byte reference - MOV operation
    ref_282661 = (ref_277997 & 0xFF) # MOVZX operation
    ref_282737 = (ref_282661 & 0xFF) # MOVZX operation
    ref_282739 = (ref_282737 & 0xFF) # Byte reference - MOV operation
    ref_284381 = ref_256232 # MOVZX operation
    ref_284457 = (ref_284381 & 0xFF) # MOVZX operation
    ref_287401 = ref_256239 # MOVZX operation
    ref_287477 = (ref_287401 & 0xFF) # MOVZX operation
    ref_287479 = (ref_287477 & 0xFF) # Byte reference - MOV operation
    ref_289121 = (ref_284457 & 0xFF) # MOVZX operation
    ref_289197 = (ref_289121 & 0xFF) # MOVZX operation
    ref_289199 = (ref_289197 & 0xFF) # Byte reference - MOV operation
    ref_290841 = ref_276274 # MOVZX operation
    ref_290917 = (ref_290841 & 0xFF) # MOVZX operation
    ref_293861 = ref_276278 # MOVZX operation
    ref_293937 = (ref_293861 & 0xFF) # MOVZX operation
    ref_293939 = (ref_293937 & 0xFF) # Byte reference - MOV operation
    ref_295581 = (ref_290917 & 0xFF) # MOVZX operation
    ref_295657 = (ref_295581 & 0xFF) # MOVZX operation
    ref_295659 = (ref_295657 & 0xFF) # Byte reference - MOV operation
    ref_296767 = ((((((((ref_287479) << 8 | ref_256233) << 8 | ref_282739) << 8 | ref_256235) << 8 | ref_256236) << 8 | ref_281019) << 8 | ref_256238) << 8 | ref_289199) # MOV operation
    ref_296967 = ref_296767 # MOV operation
    ref_296975 = (ref_296967 >> (0x3 & 0x3F)) # SHR operation
    ref_296982 = ref_296975 # MOV operation
    ref_297078 = ref_296982 # MOV operation
    ref_297092 = (0xF & ref_297078) # AND operation
    ref_297317 = ref_297092 # MOV operation
    ref_297323 = (0x1 | ref_297317) # OR operation
    ref_298246 = ((((((((ref_276271) << 8 | ref_276272) << 8 | ref_276273) << 8 | ref_293939) << 8 | ref_276275) << 8 | ref_276276) << 8 | ref_276277) << 8 | ref_295659) # MOV operation
    ref_298322 = ref_298246 # MOV operation
    ref_298334 = ref_297323 # MOV operation
    ref_298336 = ((ref_298322 << ((ref_298334 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_299259 = ((((((((ref_276271) << 8 | ref_276272) << 8 | ref_276273) << 8 | ref_293939) << 8 | ref_276275) << 8 | ref_276276) << 8 | ref_276277) << 8 | ref_295659) # MOV operation
    ref_300273 = ((((((((ref_287479) << 8 | ref_256233) << 8 | ref_282739) << 8 | ref_256235) << 8 | ref_256236) << 8 | ref_281019) << 8 | ref_256238) << 8 | ref_289199) # MOV operation
    ref_300473 = ref_300273 # MOV operation
    ref_300481 = (ref_300473 >> (0x3 & 0x3F)) # SHR operation
    ref_300488 = ref_300481 # MOV operation
    ref_300584 = ref_300488 # MOV operation
    ref_300598 = (0xF & ref_300584) # AND operation
    ref_300823 = ref_300598 # MOV operation
    ref_300829 = (0x1 | ref_300823) # OR operation
    ref_301058 = ref_300829 # MOV operation
    ref_301060 = ((0x40 - ref_301058) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_301068 = ref_301060 # MOV operation
    ref_301172 = ref_299259 # MOV operation
    ref_301176 = ref_301068 # MOV operation
    ref_301178 = (ref_301176 & 0xFFFFFFFF) # MOV operation
    ref_301180 = (ref_301172 >> ((ref_301178 & 0xFF) & 0x3F)) # SHR operation
    ref_301187 = ref_301180 # MOV operation
    ref_301291 = ref_298336 # MOV operation
    ref_301295 = ref_301187 # MOV operation
    ref_301297 = (ref_301295 | ref_301291) # OR operation
    ref_302220 = ref_265718 # MOV operation
    ref_303234 = ref_262419 # MOV operation
    ref_303310 = ref_303234 # MOV operation
    ref_303324 = ((0x369A4780 + ref_303310) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_303434 = ref_302220 # MOV operation
    ref_303438 = ref_303324 # MOV operation
    ref_303440 = (((sx(0x40, ref_303438) * sx(0x40, ref_303434)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_303546 = ref_301297 # MOV operation
    ref_303550 = ref_303440 # MOV operation
    ref_303552 = (((sx(0x40, ref_303550) * sx(0x40, ref_303546)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_304404 = ref_303552 # MOV operation
    ref_304615 = ref_304404 # MOV operation
    ref_304617 = ref_304615 # MOV operation
    endb = ref_304617


print(endb & 0xffffffffffffffff)
