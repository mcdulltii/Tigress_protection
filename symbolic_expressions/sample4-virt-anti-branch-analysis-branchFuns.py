#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_258 = SymVar_0
ref_269 = ref_258 # MOV operation
ref_281 = ref_269 # MOV operation
ref_283 = ref_281 # MOV operation
ref_317 = ((ref_283 >> 56) & 0xFF) # Byte reference - MOV operation
ref_318 = ((ref_283 >> 48) & 0xFF) # Byte reference - MOV operation
ref_319 = ((ref_283 >> 40) & 0xFF) # Byte reference - MOV operation
ref_320 = ((ref_283 >> 32) & 0xFF) # Byte reference - MOV operation
ref_321 = ((ref_283 >> 24) & 0xFF) # Byte reference - MOV operation
ref_322 = ((ref_283 >> 16) & 0xFF) # Byte reference - MOV operation
ref_323 = ((ref_283 >> 8) & 0xFF) # Byte reference - MOV operation
ref_324 = (ref_283 & 0xFF) # Byte reference - MOV operation
ref_24680 = ref_324 # MOVZX operation
ref_25009 = (ref_24680 & 0xFF) # MOVZX operation
ref_25011 = (ref_25009 & 0xFF) # MOVZX operation
ref_25359 = (ref_25011 & 0xFFFFFFFF) # MOV operation
ref_25361 = (((ref_25359 & 0xFFFFFFFF) + 0x1) & 0xFFFFFFFF) # ADD operation
ref_27119 = (ref_25361 & 0xFFFFFFFF) # MOV operation
ref_27128 = ((((0x0) << 32 | (ref_27119 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_27130 = (ref_27128 & 0xFFFFFFFF) # MOV operation
ref_27573 = (ref_27130 & 0xFFFFFFFF) # MOV operation
ref_29709 = (ref_27573 & 0xFFFFFFFF) # MOV operation
ref_30061 = (ref_29709 & 0xFFFFFFFF) # MOV operation
ref_30063 = (((ref_30061 & 0xFFFFFFFF) + 0x0) & 0xFFFFFFFF) # ADD operation
ref_31821 = (ref_30063 & 0xFFFFFFFF) # MOV operation
ref_31830 = ((((0x0) << 32 | (ref_31821 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_31832 = (ref_31830 & 0xFFFFFFFF) # MOV operation
ref_32275 = (ref_31832 & 0xFFFFFFFF) # MOV operation
ref_39088 = (ref_27573 & 0xFFFFFFFF) # MOV operation
ref_42734 = ref_323 # MOVZX operation
ref_43063 = (ref_42734 & 0xFF) # MOVZX operation
ref_43065 = (ref_43063 & 0xFF) # MOVZX operation
ref_43409 = (ref_39088 & 0xFFFFFFFF) # MOV operation
ref_43413 = (ref_43065 & 0xFFFFFFFF) # MOV operation
ref_43415 = (((ref_43413 & 0xFFFFFFFF) + (ref_43409 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_45173 = (ref_43415 & 0xFFFFFFFF) # MOV operation
ref_45182 = ((((0x0) << 32 | (ref_45173 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_45184 = (ref_45182 & 0xFFFFFFFF) # MOV operation
ref_45627 = (ref_45184 & 0xFFFFFFFF) # MOV operation
ref_46928 = (ref_32275 & 0xFFFFFFFF) # MOV operation
ref_47763 = (ref_45627 & 0xFFFFFFFF) # MOV operation
ref_48111 = (ref_46928 & 0xFFFFFFFF) # MOV operation
ref_48115 = (ref_47763 & 0xFFFFFFFF) # MOV operation
ref_48117 = (((ref_48115 & 0xFFFFFFFF) + (ref_48111 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_49875 = (ref_48117 & 0xFFFFFFFF) # MOV operation
ref_49884 = ((((0x0) << 32 | (ref_49875 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_49886 = (ref_49884 & 0xFFFFFFFF) # MOV operation
ref_50329 = (ref_49886 & 0xFFFFFFFF) # MOV operation
ref_57142 = (ref_45627 & 0xFFFFFFFF) # MOV operation
ref_60788 = ref_322 # MOVZX operation
ref_61117 = (ref_60788 & 0xFF) # MOVZX operation
ref_61119 = (ref_61117 & 0xFF) # MOVZX operation
ref_61463 = (ref_57142 & 0xFFFFFFFF) # MOV operation
ref_61467 = (ref_61119 & 0xFFFFFFFF) # MOV operation
ref_61469 = (((ref_61467 & 0xFFFFFFFF) + (ref_61463 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_63227 = (ref_61469 & 0xFFFFFFFF) # MOV operation
ref_63236 = ((((0x0) << 32 | (ref_63227 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_63238 = (ref_63236 & 0xFFFFFFFF) # MOV operation
ref_63681 = (ref_63238 & 0xFFFFFFFF) # MOV operation
ref_64982 = (ref_50329 & 0xFFFFFFFF) # MOV operation
ref_65817 = (ref_63681 & 0xFFFFFFFF) # MOV operation
ref_66165 = (ref_64982 & 0xFFFFFFFF) # MOV operation
ref_66169 = (ref_65817 & 0xFFFFFFFF) # MOV operation
ref_66171 = (((ref_66169 & 0xFFFFFFFF) + (ref_66165 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_67929 = (ref_66171 & 0xFFFFFFFF) # MOV operation
ref_67938 = ((((0x0) << 32 | (ref_67929 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_67940 = (ref_67938 & 0xFFFFFFFF) # MOV operation
ref_68383 = (ref_67940 & 0xFFFFFFFF) # MOV operation
ref_75196 = (ref_63681 & 0xFFFFFFFF) # MOV operation
ref_78842 = ref_321 # MOVZX operation
ref_79171 = (ref_78842 & 0xFF) # MOVZX operation
ref_79173 = (ref_79171 & 0xFF) # MOVZX operation
ref_79517 = (ref_75196 & 0xFFFFFFFF) # MOV operation
ref_79521 = (ref_79173 & 0xFFFFFFFF) # MOV operation
ref_79523 = (((ref_79521 & 0xFFFFFFFF) + (ref_79517 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_81281 = (ref_79523 & 0xFFFFFFFF) # MOV operation
ref_81290 = ((((0x0) << 32 | (ref_81281 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_81292 = (ref_81290 & 0xFFFFFFFF) # MOV operation
ref_81735 = (ref_81292 & 0xFFFFFFFF) # MOV operation
ref_83036 = (ref_68383 & 0xFFFFFFFF) # MOV operation
ref_83871 = (ref_81735 & 0xFFFFFFFF) # MOV operation
ref_84219 = (ref_83036 & 0xFFFFFFFF) # MOV operation
ref_84223 = (ref_83871 & 0xFFFFFFFF) # MOV operation
ref_84225 = (((ref_84223 & 0xFFFFFFFF) + (ref_84219 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_85983 = (ref_84225 & 0xFFFFFFFF) # MOV operation
ref_85992 = ((((0x0) << 32 | (ref_85983 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_85994 = (ref_85992 & 0xFFFFFFFF) # MOV operation
ref_86437 = (ref_85994 & 0xFFFFFFFF) # MOV operation
ref_93250 = (ref_81735 & 0xFFFFFFFF) # MOV operation
ref_96896 = ref_320 # MOVZX operation
ref_97225 = (ref_96896 & 0xFF) # MOVZX operation
ref_97227 = (ref_97225 & 0xFF) # MOVZX operation
ref_97571 = (ref_93250 & 0xFFFFFFFF) # MOV operation
ref_97575 = (ref_97227 & 0xFFFFFFFF) # MOV operation
ref_97577 = (((ref_97575 & 0xFFFFFFFF) + (ref_97571 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_99335 = (ref_97577 & 0xFFFFFFFF) # MOV operation
ref_99344 = ((((0x0) << 32 | (ref_99335 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_99346 = (ref_99344 & 0xFFFFFFFF) # MOV operation
ref_99789 = (ref_99346 & 0xFFFFFFFF) # MOV operation
ref_101090 = (ref_86437 & 0xFFFFFFFF) # MOV operation
ref_101925 = (ref_99789 & 0xFFFFFFFF) # MOV operation
ref_102273 = (ref_101090 & 0xFFFFFFFF) # MOV operation
ref_102277 = (ref_101925 & 0xFFFFFFFF) # MOV operation
ref_102279 = (((ref_102277 & 0xFFFFFFFF) + (ref_102273 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_104037 = (ref_102279 & 0xFFFFFFFF) # MOV operation
ref_104046 = ((((0x0) << 32 | (ref_104037 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_104048 = (ref_104046 & 0xFFFFFFFF) # MOV operation
ref_104491 = (ref_104048 & 0xFFFFFFFF) # MOV operation
ref_111304 = (ref_99789 & 0xFFFFFFFF) # MOV operation
ref_114950 = ref_319 # MOVZX operation
ref_115279 = (ref_114950 & 0xFF) # MOVZX operation
ref_115281 = (ref_115279 & 0xFF) # MOVZX operation
ref_115625 = (ref_111304 & 0xFFFFFFFF) # MOV operation
ref_115629 = (ref_115281 & 0xFFFFFFFF) # MOV operation
ref_115631 = (((ref_115629 & 0xFFFFFFFF) + (ref_115625 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_117389 = (ref_115631 & 0xFFFFFFFF) # MOV operation
ref_117398 = ((((0x0) << 32 | (ref_117389 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_117400 = (ref_117398 & 0xFFFFFFFF) # MOV operation
ref_117843 = (ref_117400 & 0xFFFFFFFF) # MOV operation
ref_119144 = (ref_104491 & 0xFFFFFFFF) # MOV operation
ref_119979 = (ref_117843 & 0xFFFFFFFF) # MOV operation
ref_120327 = (ref_119144 & 0xFFFFFFFF) # MOV operation
ref_120331 = (ref_119979 & 0xFFFFFFFF) # MOV operation
ref_120333 = (((ref_120331 & 0xFFFFFFFF) + (ref_120327 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_122091 = (ref_120333 & 0xFFFFFFFF) # MOV operation
ref_122100 = ((((0x0) << 32 | (ref_122091 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_122102 = (ref_122100 & 0xFFFFFFFF) # MOV operation
ref_122545 = (ref_122102 & 0xFFFFFFFF) # MOV operation
ref_129358 = (ref_117843 & 0xFFFFFFFF) # MOV operation
ref_133004 = ref_318 # MOVZX operation
ref_133333 = (ref_133004 & 0xFF) # MOVZX operation
ref_133335 = (ref_133333 & 0xFF) # MOVZX operation
ref_133679 = (ref_129358 & 0xFFFFFFFF) # MOV operation
ref_133683 = (ref_133335 & 0xFFFFFFFF) # MOV operation
ref_133685 = (((ref_133683 & 0xFFFFFFFF) + (ref_133679 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_135443 = (ref_133685 & 0xFFFFFFFF) # MOV operation
ref_135452 = ((((0x0) << 32 | (ref_135443 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_135454 = (ref_135452 & 0xFFFFFFFF) # MOV operation
ref_135897 = (ref_135454 & 0xFFFFFFFF) # MOV operation
ref_137198 = (ref_122545 & 0xFFFFFFFF) # MOV operation
ref_138033 = (ref_135897 & 0xFFFFFFFF) # MOV operation
ref_138381 = (ref_137198 & 0xFFFFFFFF) # MOV operation
ref_138385 = (ref_138033 & 0xFFFFFFFF) # MOV operation
ref_138387 = (((ref_138385 & 0xFFFFFFFF) + (ref_138381 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_140145 = (ref_138387 & 0xFFFFFFFF) # MOV operation
ref_140154 = ((((0x0) << 32 | (ref_140145 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_140156 = (ref_140154 & 0xFFFFFFFF) # MOV operation
ref_140599 = (ref_140156 & 0xFFFFFFFF) # MOV operation
ref_147412 = (ref_135897 & 0xFFFFFFFF) # MOV operation
ref_151058 = ref_317 # MOVZX operation
ref_151387 = (ref_151058 & 0xFF) # MOVZX operation
ref_151389 = (ref_151387 & 0xFF) # MOVZX operation
ref_151733 = (ref_147412 & 0xFFFFFFFF) # MOV operation
ref_151737 = (ref_151389 & 0xFFFFFFFF) # MOV operation
ref_151739 = (((ref_151737 & 0xFFFFFFFF) + (ref_151733 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_153497 = (ref_151739 & 0xFFFFFFFF) # MOV operation
ref_153506 = ((((0x0) << 32 | (ref_153497 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_153508 = (ref_153506 & 0xFFFFFFFF) # MOV operation
ref_153951 = (ref_153508 & 0xFFFFFFFF) # MOV operation
ref_155252 = (ref_140599 & 0xFFFFFFFF) # MOV operation
ref_156087 = (ref_153951 & 0xFFFFFFFF) # MOV operation
ref_156435 = (ref_155252 & 0xFFFFFFFF) # MOV operation
ref_156439 = (ref_156087 & 0xFFFFFFFF) # MOV operation
ref_156441 = (((ref_156439 & 0xFFFFFFFF) + (ref_156435 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_158199 = (ref_156441 & 0xFFFFFFFF) # MOV operation
ref_158208 = ((((0x0) << 32 | (ref_158199 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_158210 = (ref_158208 & 0xFFFFFFFF) # MOV operation
ref_158653 = (ref_158210 & 0xFFFFFFFF) # MOV operation
ref_166217 = (ref_153951 & 0xFFFFFFFF) # MOV operation
ref_167428 = (ref_158653 & 0xFFFFFFFF) # MOV operation
ref_167842 = (ref_167428 & 0xFFFFFFFF) # MOV operation
ref_167858 = (((ref_167842 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_167865 = (ref_167858 & 0xFFFFFFFF) # MOV operation
ref_168305 = (ref_167865 & 0xFFFFFFFF) # MOV operation
ref_168317 = (ref_166217 & 0xFFFFFFFF) # MOV operation
ref_168319 = ((ref_168317 & 0xFFFFFFFF) | (ref_168305 & 0xFFFFFFFF)) # OR operation
ref_168732 = (ref_168319 & 0xFFFFFFFF) # MOV operation
ref_169975 = (ref_168732 & 0xFFFFFFFF) # MOV operation
ref_170368 = (ref_169975 & 0xFFFFFFFF) # MOV operation
ref_170393 = (ref_170368 & 0xFFFFFFFF) # MOV operation
ref_170401 = (ref_170393 & 0xFFFFFFFF) # MOV operation
ref_170403 = (ref_170401 & 0xFFFFFFFF) # MOV operation

print(ref_170403 & 0xffffffffffffffff)
