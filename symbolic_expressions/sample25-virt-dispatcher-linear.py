#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_19701 = ref_278 # MOV operation
ref_20872 = ref_19701 # MOV operation
ref_20886 = ((ref_20872 << (0xD & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_28345 = ref_278 # MOV operation
ref_28966 = ref_28345 # MOV operation
ref_28980 = (ref_28966 >> (0x33 & 0x3F)) # SHR operation
ref_30534 = ref_20886 # MOV operation
ref_30538 = ref_28980 # MOV operation
ref_30540 = (ref_30538 | ref_30534) # OR operation
ref_30744 = ref_30540 # MOV operation
ref_45035 = ref_278 # MOV operation
ref_46056 = ref_45035 # MOV operation
ref_46072 = ((((0x0) << 64 | ref_46056) / 0x6) & 0xFFFFFFFFFFFFFFFF) # DIV operation
ref_47283 = ref_46072 # MOV operation
ref_47289 = (((sx(0x40, 0xFA0000000002C90C) * sx(0x40, ref_47283)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_47490 = ref_47289 # MOV operation
ref_62455 = ref_30744 # MOV operation
ref_70563 = ref_47490 # MOV operation
ref_72092 = ref_62455 # MOV operation
ref_72096 = ref_70563 # MOV operation
ref_72098 = (ref_72096 | ref_72092) # OR operation
ref_78596 = ref_278 # MOV operation
ref_80017 = ref_78596 # MOV operation
ref_80029 = ref_72098 # MOV operation
ref_80031 = ((ref_80029 + ref_80017) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_80236 = ref_80031 # MOV operation
ref_97123 = ref_30744 # MOV operation
ref_98513 = ref_97123 # MOV operation
ref_98519 = ((ref_98513 - 0x2ED5CD7E) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_98527 = ref_98519 # MOV operation
ref_98980 = ref_98527 # MOV operation
ref_98982 = ((0x28E5FC28 - ref_98980) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_98990 = ref_98982 # MOV operation
ref_99631 = ref_98990 # MOV operation
ref_99645 = (ref_99631 >> (0x2 & 0x3F)) # SHR operation
ref_100960 = ref_99645 # MOV operation
ref_100966 = (0x7 & ref_100960) # AND operation
ref_103481 = ref_100966 # MOV operation
ref_103487 = (0x1 | ref_103481) # OR operation
ref_111620 = ref_47490 # MOV operation
ref_118093 = ref_278 # MOV operation
ref_119514 = ref_118093 # MOV operation
ref_119526 = ref_111620 # MOV operation
ref_119528 = ((ref_119526 + ref_119514) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_120175 = ref_119528 # MOV operation
ref_120187 = ref_103487 # MOV operation
ref_120189 = (ref_120175 >> ((ref_120187 & 0xFF) & 0x3F)) # SHR operation
ref_120393 = ref_120189 # MOV operation
ref_136319 = ref_120393 # MOV operation
ref_136940 = ref_136319 # MOV operation
ref_136954 = (ref_136940 >> (0x1 & 0x3F)) # SHR operation
ref_138269 = ref_136954 # MOV operation
ref_138275 = (0x7 & ref_138269) # AND operation
ref_140790 = ref_138275 # MOV operation
ref_140796 = (0x1 | ref_140790) # OR operation
ref_148929 = ref_120393 # MOV operation
ref_149550 = ref_148929 # MOV operation
ref_149562 = ref_140796 # MOV operation
ref_149564 = (ref_149550 >> ((ref_149562 & 0xFF) & 0x3F)) # SHR operation
ref_149768 = ref_149564 # MOV operation
ref_149770 = ((ref_149768 >> 56) & 0xFF) # Byte reference - MOV operation
ref_149771 = ((ref_149768 >> 48) & 0xFF) # Byte reference - MOV operation
ref_149772 = ((ref_149768 >> 40) & 0xFF) # Byte reference - MOV operation
ref_149773 = ((ref_149768 >> 32) & 0xFF) # Byte reference - MOV operation
ref_149774 = ((ref_149768 >> 24) & 0xFF) # Byte reference - MOV operation
ref_149775 = ((ref_149768 >> 16) & 0xFF) # Byte reference - MOV operation
ref_149776 = ((ref_149768 >> 8) & 0xFF) # Byte reference - MOV operation
ref_149777 = (ref_149768 & 0xFF) # Byte reference - MOV operation
ref_172423 = ref_80236 # MOV operation
ref_182975 = ref_30744 # MOV operation
ref_184265 = ref_182975 # MOV operation
ref_184271 = (0x7 & ref_184265) # AND operation
ref_185467 = ref_184271 # MOV operation
ref_185481 = ((ref_185467 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_187035 = ref_172423 # MOV operation
ref_187039 = ref_185481 # MOV operation
ref_187041 = (ref_187039 | ref_187035) # OR operation
ref_187245 = ref_187041 # MOV operation
ref_201172 = ((((ref_149770) << 8 | ref_149771) << 8 | ref_149772) << 8 | ref_149773) # MOV operation
ref_201297 = (ref_201172 & 0xFFFFFFFF) # MOV operation
ref_226260 = ((((ref_149774) << 8 | ref_149775) << 8 | ref_149776) << 8 | ref_149777) # MOV operation
ref_226385 = (ref_226260 & 0xFFFFFFFF) # MOV operation
ref_240308 = (ref_201297 & 0xFFFFFFFF) # MOV operation
ref_240433 = (ref_240308 & 0xFFFFFFFF) # MOV operation
ref_266989 = ref_187245 # MOV operation
ref_277541 = ref_187245 # MOV operation
ref_278831 = ref_277541 # MOV operation
ref_278837 = (0x7 & ref_278831) # AND operation
ref_280033 = ref_278837 # MOV operation
ref_280047 = ((ref_280033 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_281601 = ref_266989 # MOV operation
ref_281605 = ref_280047 # MOV operation
ref_281607 = (ref_281605 | ref_281601) # OR operation
ref_281811 = ref_281607 # MOV operation
ref_295738 = (ref_226385 & 0xFFFFFFFF) # MOV operation
ref_295863 = (ref_295738 & 0xFFFFFFFF) # MOV operation
ref_320826 = (ref_240433 & 0xFFFFFFFF) # MOV operation
ref_320951 = (ref_320826 & 0xFFFFFFFF) # MOV operation
ref_320953 = (((ref_320951 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_320954 = (((ref_320951 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_320955 = (((ref_320951 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_320956 = ((ref_320951 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_334874 = (ref_295863 & 0xFFFFFFFF) # MOV operation
ref_334999 = (ref_334874 & 0xFFFFFFFF) # MOV operation
ref_335001 = (((ref_334999 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_335002 = (((ref_334999 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_335003 = (((ref_334999 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_335004 = ((ref_334999 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_361380 = ref_281811 # MOV operation
ref_369488 = ((((((((ref_320953) << 8 | ref_320954) << 8 | ref_320955) << 8 | ref_320956) << 8 | ref_335001) << 8 | ref_335002) << 8 | ref_335003) << 8 | ref_335004) # MOV operation
ref_370678 = ref_369488 # MOV operation
ref_370684 = (((sx(0x40, 0x4E1A7F2) * sx(0x40, ref_370678)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_371285 = ref_361380 # MOV operation
ref_371289 = ref_370684 # MOV operation
ref_371291 = (ref_371289 ^ ref_371285) # XOR operation
ref_372606 = ref_371291 # MOV operation
ref_372612 = (0xF & ref_372606) # AND operation
ref_375127 = ref_372612 # MOV operation
ref_375133 = (0x1 | ref_375127) # OR operation
ref_383266 = ref_30744 # MOV operation
ref_391374 = ref_47490 # MOV operation
ref_391603 = ref_383266 # MOV operation
ref_391607 = ref_391374 # MOV operation
ref_391609 = (((sx(0x40, ref_391607) * sx(0x40, ref_391603)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_392802 = ref_391609 # MOV operation
ref_392814 = ref_375133 # MOV operation
ref_392816 = ((ref_392802 << ((ref_392814 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_401910 = ref_281811 # MOV operation
ref_410018 = ((((((((ref_320953) << 8 | ref_320954) << 8 | ref_320955) << 8 | ref_320956) << 8 | ref_335001) << 8 | ref_335002) << 8 | ref_335003) << 8 | ref_335004) # MOV operation
ref_411208 = ref_410018 # MOV operation
ref_411214 = (((sx(0x40, 0x4E1A7F2) * sx(0x40, ref_411208)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_411815 = ref_401910 # MOV operation
ref_411819 = ref_411214 # MOV operation
ref_411821 = (ref_411819 ^ ref_411815) # XOR operation
ref_413136 = ref_411821 # MOV operation
ref_413142 = (0xF & ref_413136) # AND operation
ref_415657 = ref_413142 # MOV operation
ref_415663 = (0x1 | ref_415657) # OR operation
ref_416121 = ref_415663 # MOV operation
ref_416123 = ((0x40 - ref_416121) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_416131 = ref_416123 # MOV operation
ref_424259 = ref_30744 # MOV operation
ref_432367 = ref_47490 # MOV operation
ref_432596 = ref_424259 # MOV operation
ref_432600 = ref_432367 # MOV operation
ref_432602 = (((sx(0x40, ref_432600) * sx(0x40, ref_432596)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_433245 = ref_432602 # MOV operation
ref_433257 = ref_416131 # MOV operation
ref_433259 = (ref_433245 >> ((ref_433257 & 0xFF) & 0x3F)) # SHR operation
ref_434813 = ref_392816 # MOV operation
ref_434817 = ref_433259 # MOV operation
ref_434819 = (ref_434817 | ref_434813) # OR operation
ref_435023 = ref_434819 # MOV operation
ref_437174 = ref_435023 # MOV operation
ref_437176 = ref_437174 # MOV operation

print(ref_437176 & 0xffffffffffffffff)
