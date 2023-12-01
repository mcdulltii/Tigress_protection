#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_18096 = ref_278 # MOV operation
ref_19868 = ref_18096 # MOV operation
ref_19874 = (0x1F02C962 | ref_19868) # OR operation
ref_21671 = ref_19874 # MOV operation
ref_21677 = (0x1F8797B2 & ref_21671) # AND operation
ref_22572 = ref_21677 # MOV operation
ref_36017 = ref_278 # MOV operation
ref_43203 = ref_22572 # MOV operation
ref_44073 = ref_36017 # MOV operation
ref_44077 = ref_43203 # MOV operation
ref_44079 = (ref_44077 & ref_44073) # AND operation
ref_44974 = ref_44079 # MOV operation
ref_58419 = ref_278 # MOV operation
ref_60191 = ref_58419 # MOV operation
ref_60197 = (((sx(0x40, 0x66AF1DF) * sx(0x40, ref_60191)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_68307 = ref_44974 # MOV operation
ref_69169 = ref_68307 # MOV operation
ref_69183 = (ref_69169 >> (0x7 & 0x3F)) # SHR operation
ref_77296 = ref_44974 # MOV operation
ref_78158 = ref_77296 # MOV operation
ref_78172 = ((ref_78158 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_79067 = ref_69183 # MOV operation
ref_79071 = ref_78172 # MOV operation
ref_79073 = (ref_79071 | ref_79067) # OR operation
ref_79968 = ref_60197 # MOV operation
ref_79972 = ref_79073 # MOV operation
ref_79974 = ((ref_79972 + ref_79968) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_80870 = ref_79974 # MOV operation
ref_156252 = ref_80870 # MOV operation
ref_166116 = ref_80870 # MOV operation
ref_166986 = ref_156252 # MOV operation
ref_166990 = ref_166116 # MOV operation
ref_166992 = ((ref_166990 + ref_166986) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_167888 = ref_166992 # MOV operation
ref_186774 = ref_80870 # MOV operation
ref_195736 = ref_44974 # MOV operation
ref_197508 = ref_195736 # MOV operation
ref_197514 = (0x7 & ref_197508) # AND operation
ref_198401 = ref_197514 # MOV operation
ref_198415 = ((ref_198401 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_199310 = ref_186774 # MOV operation
ref_199314 = ref_198415 # MOV operation
ref_199316 = (ref_199314 | ref_199310) # OR operation
ref_200211 = ref_199316 # MOV operation
ref_200213 = ((ref_200211 >> 56) & 0xFF) # Byte reference - MOV operation
ref_200214 = ((ref_200211 >> 48) & 0xFF) # Byte reference - MOV operation
ref_200215 = ((ref_200211 >> 40) & 0xFF) # Byte reference - MOV operation
ref_200216 = ((ref_200211 >> 32) & 0xFF) # Byte reference - MOV operation
ref_200217 = ((ref_200211 >> 24) & 0xFF) # Byte reference - MOV operation
ref_200218 = ((ref_200211 >> 16) & 0xFF) # Byte reference - MOV operation
ref_200219 = ((ref_200211 >> 8) & 0xFF) # Byte reference - MOV operation
ref_200220 = (ref_200211 & 0xFF) # Byte reference - MOV operation
ref_216331 = ref_200213 # MOVZX operation
ref_217193 = (ref_216331 & 0xFF) # MOVZX operation
ref_246715 = ref_200220 # MOVZX operation
ref_247577 = (ref_246715 & 0xFF) # MOVZX operation
ref_247579 = (ref_247577 & 0xFF) # Byte reference - MOV operation
ref_263689 = (ref_217193 & 0xFF) # MOVZX operation
ref_264551 = (ref_263689 & 0xFF) # MOVZX operation
ref_264553 = (ref_264551 & 0xFF) # Byte reference - MOV operation
ref_278073 = ref_22572 # MOV operation
ref_288839 = ((((((((ref_247579) << 8 | ref_200214) << 8 | ref_200215) << 8 | ref_200216) << 8 | ref_200217) << 8 | ref_200218) << 8 | ref_200219) << 8 | ref_264553) # MOV operation
ref_296899 = ref_44974 # MOV operation
ref_297769 = ref_288839 # MOV operation
ref_297773 = ref_296899 # MOV operation
ref_297775 = (ref_297773 & ref_297769) # AND operation
ref_299572 = ref_297775 # MOV operation
ref_299578 = (0x1F & ref_299572) # AND operation
ref_300465 = ref_299578 # MOV operation
ref_300479 = ((ref_300465 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_301374 = ref_278073 # MOV operation
ref_301378 = ref_300479 # MOV operation
ref_301380 = (ref_301378 | ref_301374) # OR operation
ref_302275 = ref_301380 # MOV operation
ref_329220 = ref_167888 # MOV operation
ref_339084 = ref_167888 # MOV operation
ref_339954 = ref_329220 # MOV operation
ref_339958 = ref_339084 # MOV operation
ref_339960 = ((ref_339958 + ref_339954) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_340856 = ref_339960 # MOV operation
ref_359742 = ref_340856 # MOV operation
ref_368704 = ((((((((ref_247579) << 8 | ref_200214) << 8 | ref_200215) << 8 | ref_200216) << 8 | ref_200217) << 8 | ref_200218) << 8 | ref_200219) << 8 | ref_264553) # MOV operation
ref_370476 = ref_368704 # MOV operation
ref_370482 = (0x7 & ref_370476) # AND operation
ref_371369 = ref_370482 # MOV operation
ref_371383 = ((ref_371369 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_372278 = ref_359742 # MOV operation
ref_372282 = ref_371383 # MOV operation
ref_372284 = (ref_372282 | ref_372278) # OR operation
ref_373179 = ref_372284 # MOV operation
ref_373181 = ((ref_373179 >> 56) & 0xFF) # Byte reference - MOV operation
ref_373182 = ((ref_373179 >> 48) & 0xFF) # Byte reference - MOV operation
ref_373183 = ((ref_373179 >> 40) & 0xFF) # Byte reference - MOV operation
ref_373184 = ((ref_373179 >> 32) & 0xFF) # Byte reference - MOV operation
ref_373185 = ((ref_373179 >> 24) & 0xFF) # Byte reference - MOV operation
ref_373186 = ((ref_373179 >> 16) & 0xFF) # Byte reference - MOV operation
ref_373187 = ((ref_373179 >> 8) & 0xFF) # Byte reference - MOV operation
ref_373188 = (ref_373179 & 0xFF) # Byte reference - MOV operation
ref_389299 = ref_373181 # MOVZX operation
ref_390161 = (ref_389299 & 0xFF) # MOVZX operation
ref_419683 = ref_373188 # MOVZX operation
ref_420545 = (ref_419683 & 0xFF) # MOVZX operation
ref_420547 = (ref_420545 & 0xFF) # Byte reference - MOV operation
ref_436657 = (ref_390161 & 0xFF) # MOVZX operation
ref_437519 = (ref_436657 & 0xFF) # MOVZX operation
ref_437521 = (ref_437519 & 0xFF) # Byte reference - MOV operation
ref_451041 = ref_302275 # MOV operation
ref_461807 = ((((((((ref_420547) << 8 | ref_373182) << 8 | ref_373183) << 8 | ref_373184) << 8 | ref_373185) << 8 | ref_373186) << 8 | ref_373187) << 8 | ref_437521) # MOV operation
ref_469867 = ((((((((ref_247579) << 8 | ref_200214) << 8 | ref_200215) << 8 | ref_200216) << 8 | ref_200217) << 8 | ref_200218) << 8 | ref_200219) << 8 | ref_264553) # MOV operation
ref_470737 = ref_461807 # MOV operation
ref_470741 = ref_469867 # MOV operation
ref_470743 = (ref_470741 & ref_470737) # AND operation
ref_472540 = ref_470743 # MOV operation
ref_472546 = (0x1F & ref_472540) # AND operation
ref_473433 = ref_472546 # MOV operation
ref_473447 = ((ref_473433 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_474342 = ref_451041 # MOV operation
ref_474346 = ref_473447 # MOV operation
ref_474348 = (ref_474346 | ref_474342) # OR operation
ref_475243 = ref_474348 # MOV operation
ref_501167 = ((((((((ref_247579) << 8 | ref_200214) << 8 | ref_200215) << 8 | ref_200216) << 8 | ref_200217) << 8 | ref_200218) << 8 | ref_200219) << 8 | ref_264553) # MOV operation
ref_508353 = ((((((((ref_420547) << 8 | ref_373182) << 8 | ref_373183) << 8 | ref_373184) << 8 | ref_373185) << 8 | ref_373186) << 8 | ref_373187) << 8 | ref_437521) # MOV operation
ref_509223 = ref_501167 # MOV operation
ref_509227 = ref_508353 # MOV operation
ref_509229 = (ref_509227 | ref_509223) # OR operation
ref_511026 = ref_509229 # MOV operation
ref_511032 = (0xF & ref_511026) # AND operation
ref_512829 = ref_511032 # MOV operation
ref_512835 = (0x1 | ref_512829) # OR operation
ref_520948 = ref_44974 # MOV operation
ref_521810 = ref_520948 # MOV operation
ref_521824 = (ref_521810 >> (0x1 & 0x3F)) # SHR operation
ref_523621 = ref_521824 # MOV operation
ref_523627 = (0xF & ref_523621) # AND operation
ref_525424 = ref_523627 # MOV operation
ref_525430 = (0x1 | ref_525424) # OR operation
ref_532641 = ref_475243 # MOV operation
ref_533503 = ref_532641 # MOV operation
ref_533515 = ref_525430 # MOV operation
ref_533517 = (ref_533503 >> ((ref_533515 & 0xFF) & 0x3F)) # SHR operation
ref_541630 = ref_44974 # MOV operation
ref_542492 = ref_541630 # MOV operation
ref_542506 = (ref_542492 >> (0x1 & 0x3F)) # SHR operation
ref_544303 = ref_542506 # MOV operation
ref_544309 = (0xF & ref_544303) # AND operation
ref_546106 = ref_544309 # MOV operation
ref_546112 = (0x1 | ref_546106) # OR operation
ref_547913 = ref_546112 # MOV operation
ref_547915 = ((0x40 - ref_547913) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_547923 = ref_547915 # MOV operation
ref_555129 = ref_475243 # MOV operation
ref_555991 = ref_555129 # MOV operation
ref_556003 = ref_547923 # MOV operation
ref_556005 = ((ref_555991 << ((ref_556003 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_556900 = ref_533517 # MOV operation
ref_556904 = ref_556005 # MOV operation
ref_556906 = (ref_556904 | ref_556900) # OR operation
ref_557793 = ref_556906 # MOV operation
ref_557805 = ref_512835 # MOV operation
ref_557807 = ((ref_557793 << ((ref_557805 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_565018 = ((((((((ref_247579) << 8 | ref_200214) << 8 | ref_200215) << 8 | ref_200216) << 8 | ref_200217) << 8 | ref_200218) << 8 | ref_200219) << 8 | ref_264553) # MOV operation
ref_572204 = ((((((((ref_420547) << 8 | ref_373182) << 8 | ref_373183) << 8 | ref_373184) << 8 | ref_373185) << 8 | ref_373186) << 8 | ref_373187) << 8 | ref_437521) # MOV operation
ref_573074 = ref_565018 # MOV operation
ref_573078 = ref_572204 # MOV operation
ref_573080 = (ref_573078 | ref_573074) # OR operation
ref_574877 = ref_573080 # MOV operation
ref_574883 = (0xF & ref_574877) # AND operation
ref_576680 = ref_574883 # MOV operation
ref_576686 = (0x1 | ref_576680) # OR operation
ref_578487 = ref_576686 # MOV operation
ref_578489 = ((0x40 - ref_578487) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_578497 = ref_578489 # MOV operation
ref_586605 = ref_44974 # MOV operation
ref_587467 = ref_586605 # MOV operation
ref_587481 = (ref_587467 >> (0x1 & 0x3F)) # SHR operation
ref_589278 = ref_587481 # MOV operation
ref_589284 = (0xF & ref_589278) # AND operation
ref_591081 = ref_589284 # MOV operation
ref_591087 = (0x1 | ref_591081) # OR operation
ref_598298 = ref_475243 # MOV operation
ref_599160 = ref_598298 # MOV operation
ref_599172 = ref_591087 # MOV operation
ref_599174 = (ref_599160 >> ((ref_599172 & 0xFF) & 0x3F)) # SHR operation
ref_607287 = ref_44974 # MOV operation
ref_608149 = ref_607287 # MOV operation
ref_608163 = (ref_608149 >> (0x1 & 0x3F)) # SHR operation
ref_609960 = ref_608163 # MOV operation
ref_609966 = (0xF & ref_609960) # AND operation
ref_611763 = ref_609966 # MOV operation
ref_611769 = (0x1 | ref_611763) # OR operation
ref_613570 = ref_611769 # MOV operation
ref_613572 = ((0x40 - ref_613570) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_613580 = ref_613572 # MOV operation
ref_620786 = ref_475243 # MOV operation
ref_621648 = ref_620786 # MOV operation
ref_621660 = ref_613580 # MOV operation
ref_621662 = ((ref_621648 << ((ref_621660 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_622557 = ref_599174 # MOV operation
ref_622561 = ref_621662 # MOV operation
ref_622563 = (ref_622561 | ref_622557) # OR operation
ref_623450 = ref_622563 # MOV operation
ref_623462 = ref_578497 # MOV operation
ref_623464 = (ref_623450 >> ((ref_623462 & 0xFF) & 0x3F)) # SHR operation
ref_624359 = ref_557807 # MOV operation
ref_624363 = ref_623464 # MOV operation
ref_624365 = (ref_624363 | ref_624359) # OR operation
ref_625260 = ref_624365 # MOV operation
ref_627043 = ref_625260 # MOV operation
ref_627045 = ref_627043 # MOV operation

print(ref_627045 & 0xffffffffffffffff)
