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
ref_21521 = ref_316 # MOVZX operation
ref_21587 = (ref_21521 & 0xFF) # MOVZX operation
ref_21589 = (ref_21587 & 0xFF) # MOVZX operation
ref_21673 = (ref_21589 & 0xFFFFFFFF) # MOV operation
ref_21675 = (((ref_21673 & 0xFFFFFFFF) + 0x1) & 0xFFFFFFFF) # ADD operation
ref_22050 = (ref_21675 & 0xFFFFFFFF) # MOV operation
ref_22059 = ((((0x0) << 32 | (ref_22050 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_22061 = (ref_22059 & 0xFFFFFFFF) # MOV operation
ref_22161 = (ref_22061 & 0xFFFFFFFF) # MOV operation
ref_22709 = (ref_22161 & 0xFFFFFFFF) # MOV operation
ref_22793 = (ref_22709 & 0xFFFFFFFF) # MOV operation
ref_22795 = (((ref_22793 & 0xFFFFFFFF) + 0x0) & 0xFFFFFFFF) # ADD operation
ref_23170 = (ref_22795 & 0xFFFFFFFF) # MOV operation
ref_23179 = ((((0x0) << 32 | (ref_23170 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_23181 = (ref_23179 & 0xFFFFFFFF) # MOV operation
ref_23281 = (ref_23181 & 0xFFFFFFFF) # MOV operation
ref_25022 = (ref_22161 & 0xFFFFFFFF) # MOV operation
ref_25920 = ref_315 # MOVZX operation
ref_25986 = (ref_25920 & 0xFF) # MOVZX operation
ref_25988 = (ref_25986 & 0xFF) # MOVZX operation
ref_26068 = (ref_25022 & 0xFFFFFFFF) # MOV operation
ref_26072 = (ref_25988 & 0xFFFFFFFF) # MOV operation
ref_26074 = (((ref_26072 & 0xFFFFFFFF) + (ref_26068 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_26449 = (ref_26074 & 0xFFFFFFFF) # MOV operation
ref_26458 = ((((0x0) << 32 | (ref_26449 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_26460 = (ref_26458 & 0xFFFFFFFF) # MOV operation
ref_26560 = (ref_26460 & 0xFFFFFFFF) # MOV operation
ref_26908 = (ref_23281 & 0xFFFFFFFF) # MOV operation
ref_27108 = (ref_26560 & 0xFFFFFFFF) # MOV operation
ref_27188 = (ref_26908 & 0xFFFFFFFF) # MOV operation
ref_27192 = (ref_27108 & 0xFFFFFFFF) # MOV operation
ref_27194 = (((ref_27192 & 0xFFFFFFFF) + (ref_27188 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_27569 = (ref_27194 & 0xFFFFFFFF) # MOV operation
ref_27578 = ((((0x0) << 32 | (ref_27569 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_27580 = (ref_27578 & 0xFFFFFFFF) # MOV operation
ref_27680 = (ref_27580 & 0xFFFFFFFF) # MOV operation
ref_29421 = (ref_26560 & 0xFFFFFFFF) # MOV operation
ref_30319 = ref_314 # MOVZX operation
ref_30385 = (ref_30319 & 0xFF) # MOVZX operation
ref_30387 = (ref_30385 & 0xFF) # MOVZX operation
ref_30467 = (ref_29421 & 0xFFFFFFFF) # MOV operation
ref_30471 = (ref_30387 & 0xFFFFFFFF) # MOV operation
ref_30473 = (((ref_30471 & 0xFFFFFFFF) + (ref_30467 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_30848 = (ref_30473 & 0xFFFFFFFF) # MOV operation
ref_30857 = ((((0x0) << 32 | (ref_30848 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_30859 = (ref_30857 & 0xFFFFFFFF) # MOV operation
ref_30959 = (ref_30859 & 0xFFFFFFFF) # MOV operation
ref_31307 = (ref_27680 & 0xFFFFFFFF) # MOV operation
ref_31507 = (ref_30959 & 0xFFFFFFFF) # MOV operation
ref_31587 = (ref_31307 & 0xFFFFFFFF) # MOV operation
ref_31591 = (ref_31507 & 0xFFFFFFFF) # MOV operation
ref_31593 = (((ref_31591 & 0xFFFFFFFF) + (ref_31587 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_31968 = (ref_31593 & 0xFFFFFFFF) # MOV operation
ref_31977 = ((((0x0) << 32 | (ref_31968 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_31979 = (ref_31977 & 0xFFFFFFFF) # MOV operation
ref_32079 = (ref_31979 & 0xFFFFFFFF) # MOV operation
ref_33820 = (ref_30959 & 0xFFFFFFFF) # MOV operation
ref_34718 = ref_313 # MOVZX operation
ref_34784 = (ref_34718 & 0xFF) # MOVZX operation
ref_34786 = (ref_34784 & 0xFF) # MOVZX operation
ref_34866 = (ref_33820 & 0xFFFFFFFF) # MOV operation
ref_34870 = (ref_34786 & 0xFFFFFFFF) # MOV operation
ref_34872 = (((ref_34870 & 0xFFFFFFFF) + (ref_34866 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_35247 = (ref_34872 & 0xFFFFFFFF) # MOV operation
ref_35256 = ((((0x0) << 32 | (ref_35247 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_35258 = (ref_35256 & 0xFFFFFFFF) # MOV operation
ref_35358 = (ref_35258 & 0xFFFFFFFF) # MOV operation
ref_35706 = (ref_32079 & 0xFFFFFFFF) # MOV operation
ref_35906 = (ref_35358 & 0xFFFFFFFF) # MOV operation
ref_35986 = (ref_35706 & 0xFFFFFFFF) # MOV operation
ref_35990 = (ref_35906 & 0xFFFFFFFF) # MOV operation
ref_35992 = (((ref_35990 & 0xFFFFFFFF) + (ref_35986 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_36367 = (ref_35992 & 0xFFFFFFFF) # MOV operation
ref_36376 = ((((0x0) << 32 | (ref_36367 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_36378 = (ref_36376 & 0xFFFFFFFF) # MOV operation
ref_36478 = (ref_36378 & 0xFFFFFFFF) # MOV operation
ref_38219 = (ref_35358 & 0xFFFFFFFF) # MOV operation
ref_39117 = ref_312 # MOVZX operation
ref_39183 = (ref_39117 & 0xFF) # MOVZX operation
ref_39185 = (ref_39183 & 0xFF) # MOVZX operation
ref_39265 = (ref_38219 & 0xFFFFFFFF) # MOV operation
ref_39269 = (ref_39185 & 0xFFFFFFFF) # MOV operation
ref_39271 = (((ref_39269 & 0xFFFFFFFF) + (ref_39265 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_39646 = (ref_39271 & 0xFFFFFFFF) # MOV operation
ref_39655 = ((((0x0) << 32 | (ref_39646 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_39657 = (ref_39655 & 0xFFFFFFFF) # MOV operation
ref_39757 = (ref_39657 & 0xFFFFFFFF) # MOV operation
ref_40105 = (ref_36478 & 0xFFFFFFFF) # MOV operation
ref_40305 = (ref_39757 & 0xFFFFFFFF) # MOV operation
ref_40385 = (ref_40105 & 0xFFFFFFFF) # MOV operation
ref_40389 = (ref_40305 & 0xFFFFFFFF) # MOV operation
ref_40391 = (((ref_40389 & 0xFFFFFFFF) + (ref_40385 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_40766 = (ref_40391 & 0xFFFFFFFF) # MOV operation
ref_40775 = ((((0x0) << 32 | (ref_40766 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_40777 = (ref_40775 & 0xFFFFFFFF) # MOV operation
ref_40877 = (ref_40777 & 0xFFFFFFFF) # MOV operation
ref_42618 = (ref_39757 & 0xFFFFFFFF) # MOV operation
ref_43516 = ref_311 # MOVZX operation
ref_43582 = (ref_43516 & 0xFF) # MOVZX operation
ref_43584 = (ref_43582 & 0xFF) # MOVZX operation
ref_43664 = (ref_42618 & 0xFFFFFFFF) # MOV operation
ref_43668 = (ref_43584 & 0xFFFFFFFF) # MOV operation
ref_43670 = (((ref_43668 & 0xFFFFFFFF) + (ref_43664 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_44045 = (ref_43670 & 0xFFFFFFFF) # MOV operation
ref_44054 = ((((0x0) << 32 | (ref_44045 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_44056 = (ref_44054 & 0xFFFFFFFF) # MOV operation
ref_44156 = (ref_44056 & 0xFFFFFFFF) # MOV operation
ref_44504 = (ref_40877 & 0xFFFFFFFF) # MOV operation
ref_44704 = (ref_44156 & 0xFFFFFFFF) # MOV operation
ref_44784 = (ref_44504 & 0xFFFFFFFF) # MOV operation
ref_44788 = (ref_44704 & 0xFFFFFFFF) # MOV operation
ref_44790 = (((ref_44788 & 0xFFFFFFFF) + (ref_44784 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_45165 = (ref_44790 & 0xFFFFFFFF) # MOV operation
ref_45174 = ((((0x0) << 32 | (ref_45165 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_45176 = (ref_45174 & 0xFFFFFFFF) # MOV operation
ref_45276 = (ref_45176 & 0xFFFFFFFF) # MOV operation
ref_47017 = (ref_44156 & 0xFFFFFFFF) # MOV operation
ref_47915 = ref_310 # MOVZX operation
ref_47981 = (ref_47915 & 0xFF) # MOVZX operation
ref_47983 = (ref_47981 & 0xFF) # MOVZX operation
ref_48063 = (ref_47017 & 0xFFFFFFFF) # MOV operation
ref_48067 = (ref_47983 & 0xFFFFFFFF) # MOV operation
ref_48069 = (((ref_48067 & 0xFFFFFFFF) + (ref_48063 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_48444 = (ref_48069 & 0xFFFFFFFF) # MOV operation
ref_48453 = ((((0x0) << 32 | (ref_48444 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_48455 = (ref_48453 & 0xFFFFFFFF) # MOV operation
ref_48555 = (ref_48455 & 0xFFFFFFFF) # MOV operation
ref_48903 = (ref_45276 & 0xFFFFFFFF) # MOV operation
ref_49103 = (ref_48555 & 0xFFFFFFFF) # MOV operation
ref_49183 = (ref_48903 & 0xFFFFFFFF) # MOV operation
ref_49187 = (ref_49103 & 0xFFFFFFFF) # MOV operation
ref_49189 = (((ref_49187 & 0xFFFFFFFF) + (ref_49183 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_49564 = (ref_49189 & 0xFFFFFFFF) # MOV operation
ref_49573 = ((((0x0) << 32 | (ref_49564 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_49575 = (ref_49573 & 0xFFFFFFFF) # MOV operation
ref_49675 = (ref_49575 & 0xFFFFFFFF) # MOV operation
ref_51416 = (ref_48555 & 0xFFFFFFFF) # MOV operation
ref_52314 = ref_309 # MOVZX operation
ref_52380 = (ref_52314 & 0xFF) # MOVZX operation
ref_52382 = (ref_52380 & 0xFF) # MOVZX operation
ref_52462 = (ref_51416 & 0xFFFFFFFF) # MOV operation
ref_52466 = (ref_52382 & 0xFFFFFFFF) # MOV operation
ref_52468 = (((ref_52466 & 0xFFFFFFFF) + (ref_52462 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_52843 = (ref_52468 & 0xFFFFFFFF) # MOV operation
ref_52852 = ((((0x0) << 32 | (ref_52843 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_52854 = (ref_52852 & 0xFFFFFFFF) # MOV operation
ref_52954 = (ref_52854 & 0xFFFFFFFF) # MOV operation
ref_53302 = (ref_49675 & 0xFFFFFFFF) # MOV operation
ref_53502 = (ref_52954 & 0xFFFFFFFF) # MOV operation
ref_53582 = (ref_53302 & 0xFFFFFFFF) # MOV operation
ref_53586 = (ref_53502 & 0xFFFFFFFF) # MOV operation
ref_53588 = (((ref_53586 & 0xFFFFFFFF) + (ref_53582 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_53963 = (ref_53588 & 0xFFFFFFFF) # MOV operation
ref_53972 = ((((0x0) << 32 | (ref_53963 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_53974 = (ref_53972 & 0xFFFFFFFF) # MOV operation
ref_54074 = (ref_53974 & 0xFFFFFFFF) # MOV operation
ref_55976 = (ref_52954 & 0xFFFFFFFF) # MOV operation
ref_56288 = (ref_54074 & 0xFFFFFFFF) # MOV operation
ref_56360 = (ref_56288 & 0xFFFFFFFF) # MOV operation
ref_56376 = (((ref_56360 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_56383 = (ref_56376 & 0xFFFFFFFF) # MOV operation
ref_56475 = (ref_56383 & 0xFFFFFFFF) # MOV operation
ref_56487 = (ref_55976 & 0xFFFFFFFF) # MOV operation
ref_56489 = ((ref_56487 & 0xFFFFFFFF) | (ref_56475 & 0xFFFFFFFF)) # OR operation
ref_56594 = (ref_56489 & 0xFFFFFFFF) # MOV operation
ref_56898 = (ref_56594 & 0xFFFFFFFF) # MOV operation
ref_56966 = (ref_56898 & 0xFFFFFFFF) # MOV operation
ref_56990 = (ref_56966 & 0xFFFFFFFF) # MOV operation
ref_56998 = (ref_56990 & 0xFFFFFFFF) # MOV operation
ref_57000 = (ref_56998 & 0xFFFFFFFF) # MOV operation

print(ref_57000 & 0xffffffffffffffff)
