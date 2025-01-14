#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])

ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_17899 = ref_278 # MOV operation
ref_19989 = ref_17899 # MOV operation
ref_19997 = ((ref_19989 << (0x33 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_20004 = ref_19997 # MOV operation
ref_25547 = ref_278 # MOV operation
ref_27887 = ref_25547 # MOV operation
ref_27895 = (ref_27887 >> (0xD & 0x3F)) # SHR operation
ref_27902 = ref_27895 # MOV operation
ref_28993 = ref_27902 # MOV operation
ref_29005 = ref_20004 # MOV operation
ref_29007 = (ref_29005 | ref_28993) # OR operation
ref_29403 = ref_29007 # MOV operation
ref_29417 = ((0x2EA4A1C39AF5800 + ref_29403) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_29622 = ref_29417 # MOV operation
ref_42437 = ref_29622 # MOV operation
ref_47960 = ref_278 # MOV operation
ref_48531 = ref_47960 # MOV operation
ref_48543 = ref_42437 # MOV operation
ref_48545 = ((ref_48531 - ref_48543) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_48553 = ref_48545 # MOV operation
ref_48752 = ref_48553 # MOV operation
ref_60382 = ref_278 # MOV operation
ref_62722 = ref_60382 # MOV operation
ref_62730 = (ref_62722 >> (0x37 & 0x3F)) # SHR operation
ref_62737 = ref_62730 # MOV operation
ref_68280 = ref_278 # MOV operation
ref_70370 = ref_68280 # MOV operation
ref_70378 = ((ref_70370 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_70385 = ref_70378 # MOV operation
ref_71476 = ref_70385 # MOV operation
ref_71488 = ref_62737 # MOV operation
ref_71490 = (ref_71488 | ref_71476) # OR operation
ref_71694 = ref_71490 # MOV operation
ref_84235 = ref_278 # MOV operation
ref_85306 = ref_84235 # MOV operation
ref_85320 = (0x3E908497 | ref_85306) # OR operation
ref_85524 = ref_85320 # MOV operation
ref_92931 = ref_85524 # MOV operation
ref_99639 = ref_71694 # MOV operation
ref_100210 = ref_99639 # MOV operation
ref_100222 = ref_92931 # MOV operation
ref_100224 = ((ref_100210 - ref_100222) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_100232 = ref_100224 # MOV operation
ref_106960 = ref_29622 # MOV operation
ref_114579 = ref_48752 # MOV operation
ref_116919 = ref_114579 # MOV operation
ref_116927 = (ref_116919 >> (0x2 & 0x3F)) # SHR operation
ref_116934 = ref_116927 # MOV operation
ref_118394 = ref_116934 # MOV operation
ref_118400 = (0xF & ref_118394) # AND operation
ref_119496 = ref_118400 # MOV operation
ref_119510 = (0x1 | ref_119496) # OR operation
ref_121029 = ref_119510 # MOV operation
ref_121031 = ((0x40 - ref_121029) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_121039 = ref_121031 # MOV operation
ref_122238 = ref_106960 # MOV operation
ref_122242 = ref_121039 # MOV operation
ref_122244 = (ref_122242 & 0xFFFFFFFF) # MOV operation
ref_122246 = ((ref_122238 << ((ref_122244 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_122253 = ref_122246 # MOV operation
ref_128981 = ref_29622 # MOV operation
ref_136600 = ref_48752 # MOV operation
ref_138940 = ref_136600 # MOV operation
ref_138948 = (ref_138940 >> (0x2 & 0x3F)) # SHR operation
ref_138955 = ref_138948 # MOV operation
ref_140415 = ref_138955 # MOV operation
ref_140421 = (0xF & ref_140415) # AND operation
ref_141517 = ref_140421 # MOV operation
ref_141531 = (0x1 | ref_141517) # OR operation
ref_142985 = ref_128981 # MOV operation
ref_142989 = ref_141531 # MOV operation
ref_142991 = (ref_142989 & 0xFFFFFFFF) # MOV operation
ref_142993 = (ref_142985 >> ((ref_142991 & 0xFF) & 0x3F)) # SHR operation
ref_143000 = ref_142993 # MOV operation
ref_144091 = ref_143000 # MOV operation
ref_144103 = ref_122253 # MOV operation
ref_144105 = (ref_144103 | ref_144091) # OR operation
ref_144851 = ref_144105 # MOV operation
ref_144863 = ref_100232 # MOV operation
ref_144865 = ((ref_144851 - ref_144863) & 0xFFFFFFFFFFFFFFFF) # CMP operation
ref_144867 = ((((ref_144851 ^ (ref_144863 ^ ref_144865)) ^ ((ref_144851 ^ ref_144865) & (ref_144851 ^ ref_144863))) >> 63) & 0x1) # Carry flag
ref_144873 = ((((ref_144863 >> 8) & 0xFFFFFFFFFFFFFF)) << 8 | (0x1 if (ref_144867 == 0x1) else 0x0)) # SETB operation
ref_144875 = (ref_144873 & 0xFF) # MOVZX operation
ref_145358 = (ref_144875 & 0xFFFFFFFF) # MOV operation
ref_145360 = ((ref_145358 & 0xFFFFFFFF) & (ref_145358 & 0xFFFFFFFF)) # TEST operation
ref_145365 = (0x1 if (ref_145360 == 0x0) else 0x0) # Zero flag
ref_145367 = (0x1970 if (ref_145365 == 0x1) else 0x1952) # Program Counter


if (ref_145365 == 0x1):
    ref_351107 = SymVar_0
    ref_351122 = ref_351107 # MOV operation
    ref_368748 = ref_351122 # MOV operation
    ref_370838 = ref_368748 # MOV operation
    ref_370846 = ((ref_370838 << (0x33 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_370853 = ref_370846 # MOV operation
    ref_376396 = ref_351122 # MOV operation
    ref_378736 = ref_376396 # MOV operation
    ref_378744 = (ref_378736 >> (0xD & 0x3F)) # SHR operation
    ref_378751 = ref_378744 # MOV operation
    ref_379842 = ref_378751 # MOV operation
    ref_379854 = ref_370853 # MOV operation
    ref_379856 = (ref_379854 | ref_379842) # OR operation
    ref_380252 = ref_379856 # MOV operation
    ref_380266 = ((0x2EA4A1C39AF5800 + ref_380252) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_380471 = ref_380266 # MOV operation
    ref_393286 = ref_380471 # MOV operation
    ref_398809 = ref_351122 # MOV operation
    ref_399380 = ref_398809 # MOV operation
    ref_399392 = ref_393286 # MOV operation
    ref_399394 = ((ref_399380 - ref_399392) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_399402 = ref_399394 # MOV operation
    ref_399601 = ref_399402 # MOV operation
    ref_411231 = ref_351122 # MOV operation
    ref_413571 = ref_411231 # MOV operation
    ref_413579 = (ref_413571 >> (0x37 & 0x3F)) # SHR operation
    ref_413586 = ref_413579 # MOV operation
    ref_419129 = ref_351122 # MOV operation
    ref_421219 = ref_419129 # MOV operation
    ref_421227 = ((ref_421219 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_421234 = ref_421227 # MOV operation
    ref_422325 = ref_421234 # MOV operation
    ref_422337 = ref_413586 # MOV operation
    ref_422339 = (ref_422337 | ref_422325) # OR operation
    ref_422543 = ref_422339 # MOV operation
    ref_435084 = ref_351122 # MOV operation
    ref_436155 = ref_435084 # MOV operation
    ref_436169 = (0x3E908497 | ref_436155) # OR operation
    ref_436373 = ref_436169 # MOV operation
    ref_508543 = ref_380471 # MOV operation
    ref_516162 = ref_399601 # MOV operation
    ref_518502 = ref_516162 # MOV operation
    ref_518510 = (ref_518502 >> (0x4 & 0x3F)) # SHR operation
    ref_518517 = ref_518510 # MOV operation
    ref_519977 = ref_518517 # MOV operation
    ref_519983 = (0xF & ref_519977) # AND operation
    ref_521079 = ref_519983 # MOV operation
    ref_521093 = (0x1 | ref_521079) # OR operation
    ref_522612 = ref_521093 # MOV operation
    ref_522614 = ((0x40 - ref_522612) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_522622 = ref_522614 # MOV operation
    ref_524071 = ref_508543 # MOV operation
    ref_524075 = ref_522622 # MOV operation
    ref_524077 = (ref_524075 & 0xFFFFFFFF) # MOV operation
    ref_524079 = (ref_524071 >> ((ref_524077 & 0xFF) & 0x3F)) # SHR operation
    ref_524086 = ref_524079 # MOV operation
    ref_530814 = ref_380471 # MOV operation
    ref_538433 = ref_399601 # MOV operation
    ref_540773 = ref_538433 # MOV operation
    ref_540781 = (ref_540773 >> (0x4 & 0x3F)) # SHR operation
    ref_540788 = ref_540781 # MOV operation
    ref_542248 = ref_540788 # MOV operation
    ref_542254 = (0xF & ref_542248) # AND operation
    ref_543350 = ref_542254 # MOV operation
    ref_543364 = (0x1 | ref_543350) # OR operation
    ref_544568 = ref_530814 # MOV operation
    ref_544572 = ref_543364 # MOV operation
    ref_544574 = (ref_544572 & 0xFFFFFFFF) # MOV operation
    ref_544576 = ((ref_544568 << ((ref_544574 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_544583 = ref_544576 # MOV operation
    ref_545674 = ref_544583 # MOV operation
    ref_545686 = ref_524086 # MOV operation
    ref_545688 = (ref_545686 | ref_545674) # OR operation
    ref_553332 = ref_436373 # MOV operation
    ref_560040 = ref_422543 # MOV operation
    ref_561111 = ref_560040 # MOV operation
    ref_561123 = ref_553332 # MOV operation
    ref_561125 = (ref_561123 | ref_561111) # OR operation
    ref_563490 = ref_561125 # MOV operation
    ref_563498 = (ref_563490 >> (0x4 & 0x3F)) # SHR operation
    ref_563505 = ref_563498 # MOV operation
    ref_564965 = ref_563505 # MOV operation
    ref_564971 = (0x7 & ref_564965) # AND operation
    ref_566067 = ref_564971 # MOV operation
    ref_566081 = (0x1 | ref_566067) # OR operation
    ref_567535 = ref_545688 # MOV operation
    ref_567539 = ref_566081 # MOV operation
    ref_567541 = (ref_567539 & 0xFFFFFFFF) # MOV operation
    ref_567543 = (ref_567535 >> ((ref_567541 & 0xFF) & 0x3F)) # SHR operation
    ref_567550 = ref_567543 # MOV operation
    ref_567749 = ref_567550 # MOV operation
    ref_569750 = ref_567749 # MOV operation
    ref_569752 = ref_569750 # MOV operation
    endb = ref_569752


else:
    ref_263 = SymVar_0
    ref_278 = ref_263 # MOV operation
    ref_17899 = ref_278 # MOV operation
    ref_19989 = ref_17899 # MOV operation
    ref_19997 = ((ref_19989 << (0x33 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_20004 = ref_19997 # MOV operation
    ref_25547 = ref_278 # MOV operation
    ref_27887 = ref_25547 # MOV operation
    ref_27895 = (ref_27887 >> (0xD & 0x3F)) # SHR operation
    ref_27902 = ref_27895 # MOV operation
    ref_28993 = ref_27902 # MOV operation
    ref_29005 = ref_20004 # MOV operation
    ref_29007 = (ref_29005 | ref_28993) # OR operation
    ref_29403 = ref_29007 # MOV operation
    ref_29417 = ((0x2EA4A1C39AF5800 + ref_29403) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_29622 = ref_29417 # MOV operation
    ref_42437 = ref_29622 # MOV operation
    ref_47960 = ref_278 # MOV operation
    ref_48531 = ref_47960 # MOV operation
    ref_48543 = ref_42437 # MOV operation
    ref_48545 = ((ref_48531 - ref_48543) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_48553 = ref_48545 # MOV operation
    ref_48752 = ref_48553 # MOV operation
    ref_48754 = ((ref_48752 >> 56) & 0xFF) # Byte reference - MOV operation
    ref_48755 = ((ref_48752 >> 48) & 0xFF) # Byte reference - MOV operation
    ref_48756 = ((ref_48752 >> 40) & 0xFF) # Byte reference - MOV operation
    ref_48757 = ((ref_48752 >> 32) & 0xFF) # Byte reference - MOV operation
    ref_48758 = ((ref_48752 >> 24) & 0xFF) # Byte reference - MOV operation
    ref_48759 = ((ref_48752 >> 16) & 0xFF) # Byte reference - MOV operation
    ref_48760 = ((ref_48752 >> 8) & 0xFF) # Byte reference - MOV operation
    ref_48761 = (ref_48752 & 0xFF) # Byte reference - MOV operation
    ref_60382 = ref_278 # MOV operation
    ref_62722 = ref_60382 # MOV operation
    ref_62730 = (ref_62722 >> (0x37 & 0x3F)) # SHR operation
    ref_62737 = ref_62730 # MOV operation
    ref_68280 = ref_278 # MOV operation
    ref_70370 = ref_68280 # MOV operation
    ref_70378 = ((ref_70370 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_70385 = ref_70378 # MOV operation
    ref_71476 = ref_70385 # MOV operation
    ref_71488 = ref_62737 # MOV operation
    ref_71490 = (ref_71488 | ref_71476) # OR operation
    ref_71694 = ref_71490 # MOV operation
    ref_84235 = ref_278 # MOV operation
    ref_85306 = ref_84235 # MOV operation
    ref_85320 = (0x3E908497 | ref_85306) # OR operation
    ref_85524 = ref_85320 # MOV operation
    ref_156887 = ((((ref_48754) << 8 | ref_48755) << 8 | ref_48756) << 8 | ref_48757) # MOV operation
    ref_159385 = (ref_156887 & 0xFFFFFFFF) # MOV operation
    ref_170885 = ((((ref_48758) << 8 | ref_48759) << 8 | ref_48760) << 8 | ref_48761) # MOV operation
    ref_182923 = (ref_170885 & 0xFFFFFFFF) # MOV operation
    ref_182925 = (((ref_182923 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
    ref_182926 = (((ref_182923 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
    ref_182927 = (((ref_182923 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
    ref_182928 = ((ref_182923 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
    ref_184883 = (ref_159385 & 0xFFFFFFFF) # MOV operation
    ref_196921 = (ref_184883 & 0xFFFFFFFF) # MOV operation
    ref_196923 = (((ref_196921 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
    ref_196924 = (((ref_196921 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
    ref_196925 = (((ref_196921 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
    ref_196926 = ((ref_196921 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
    ref_209732 = ref_29622 # MOV operation
    ref_211172 = ref_209732 # MOV operation
    ref_211178 = (0x3F & ref_211172) # AND operation
    ref_213293 = ref_211178 # MOV operation
    ref_213301 = ((ref_213293 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_213308 = ref_213301 # MOV operation
    ref_220036 = ref_29622 # MOV operation
    ref_221107 = ref_220036 # MOV operation
    ref_221119 = ref_213308 # MOV operation
    ref_221121 = (ref_221119 | ref_221107) # OR operation
    ref_221325 = ref_221121 # MOV operation
    ref_234140 = ref_221325 # MOV operation
    ref_235580 = ref_234140 # MOV operation
    ref_235586 = (0x1F & ref_235580) # AND operation
    ref_237701 = ref_235586 # MOV operation
    ref_237709 = ((ref_237701 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_237716 = ref_237709 # MOV operation
    ref_244444 = ref_85524 # MOV operation
    ref_245515 = ref_244444 # MOV operation
    ref_245527 = ref_237716 # MOV operation
    ref_245529 = (ref_245527 | ref_245515) # OR operation
    ref_245733 = ref_245529 # MOV operation
    ref_258548 = ref_71694 # MOV operation
    ref_265256 = ref_221325 # MOV operation
    ref_265627 = ref_265256 # MOV operation
    ref_265639 = ref_258548 # MOV operation
    ref_265641 = ((ref_265639 + ref_265627) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_267107 = ref_265641 # MOV operation
    ref_267113 = (0x1F & ref_267107) # AND operation
    ref_269228 = ref_267113 # MOV operation
    ref_269236 = ((ref_269228 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_269243 = ref_269236 # MOV operation
    ref_275971 = ref_221325 # MOV operation
    ref_277042 = ref_275971 # MOV operation
    ref_277054 = ref_269243 # MOV operation
    ref_277056 = (ref_277054 | ref_277042) # OR operation
    ref_277260 = ref_277056 # MOV operation
    ref_289578 = ref_277260 # MOV operation
    ref_297197 = ((((((((ref_182925) << 8 | ref_182926) << 8 | ref_182927) << 8 | ref_182928) << 8 | ref_196923) << 8 | ref_196924) << 8 | ref_196925) << 8 | ref_196926) # MOV operation
    ref_299537 = ref_297197 # MOV operation
    ref_299545 = (ref_299537 >> (0x4 & 0x3F)) # SHR operation
    ref_299552 = ref_299545 # MOV operation
    ref_301012 = ref_299552 # MOV operation
    ref_301018 = (0xF & ref_301012) # AND operation
    ref_302114 = ref_301018 # MOV operation
    ref_302128 = (0x1 | ref_302114) # OR operation
    ref_303647 = ref_302128 # MOV operation
    ref_303649 = ((0x40 - ref_303647) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_303657 = ref_303649 # MOV operation
    ref_305106 = ref_289578 # MOV operation
    ref_305110 = ref_303657 # MOV operation
    ref_305112 = (ref_305110 & 0xFFFFFFFF) # MOV operation
    ref_305114 = (ref_305106 >> ((ref_305112 & 0xFF) & 0x3F)) # SHR operation
    ref_305121 = ref_305114 # MOV operation
    ref_311849 = ref_277260 # MOV operation
    ref_319468 = ((((((((ref_182925) << 8 | ref_182926) << 8 | ref_182927) << 8 | ref_182928) << 8 | ref_196923) << 8 | ref_196924) << 8 | ref_196925) << 8 | ref_196926) # MOV operation
    ref_321808 = ref_319468 # MOV operation
    ref_321816 = (ref_321808 >> (0x4 & 0x3F)) # SHR operation
    ref_321823 = ref_321816 # MOV operation
    ref_323283 = ref_321823 # MOV operation
    ref_323289 = (0xF & ref_323283) # AND operation
    ref_324385 = ref_323289 # MOV operation
    ref_324399 = (0x1 | ref_324385) # OR operation
    ref_325603 = ref_311849 # MOV operation
    ref_325607 = ref_324399 # MOV operation
    ref_325609 = (ref_325607 & 0xFFFFFFFF) # MOV operation
    ref_325611 = ((ref_325603 << ((ref_325609 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_325618 = ref_325611 # MOV operation
    ref_326709 = ref_325618 # MOV operation
    ref_326721 = ref_305121 # MOV operation
    ref_326723 = (ref_326721 | ref_326709) # OR operation
    ref_334367 = ref_245733 # MOV operation
    ref_341075 = ref_71694 # MOV operation
    ref_342146 = ref_341075 # MOV operation
    ref_342158 = ref_334367 # MOV operation
    ref_342160 = (ref_342158 | ref_342146) # OR operation
    ref_344525 = ref_342160 # MOV operation
    ref_344533 = (ref_344525 >> (0x4 & 0x3F)) # SHR operation
    ref_344540 = ref_344533 # MOV operation
    ref_346000 = ref_344540 # MOV operation
    ref_346006 = (0x7 & ref_346000) # AND operation
    ref_347102 = ref_346006 # MOV operation
    ref_347116 = (0x1 | ref_347102) # OR operation
    ref_348570 = ref_326723 # MOV operation
    ref_348574 = ref_347116 # MOV operation
    ref_348576 = (ref_348574 & 0xFFFFFFFF) # MOV operation
    ref_348578 = (ref_348570 >> ((ref_348576 & 0xFF) & 0x3F)) # SHR operation
    ref_348585 = ref_348578 # MOV operation
    ref_348784 = ref_348585 # MOV operation
    ref_350785 = ref_348784 # MOV operation
    ref_350787 = ref_350785 # MOV operation
    endb = ref_350787


print(endb & 0xffffffffffffffff)
