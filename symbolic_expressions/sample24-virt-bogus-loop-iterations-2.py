#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])

ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_30134 = ref_278 # MOV operation
ref_31598 = ref_30134 # MOV operation
ref_31612 = ((ref_31598 << (0xB & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_45058 = ref_278 # MOV operation
ref_46522 = ref_45058 # MOV operation
ref_46536 = (ref_46522 >> (0x35 & 0x3F)) # SHR operation
ref_48033 = ref_31612 # MOV operation
ref_48037 = ref_46536 # MOV operation
ref_48039 = (ref_48037 | ref_48033) # OR operation
ref_49528 = ref_48039 # MOV operation
ref_49542 = (ref_49528 >> (0x1 & 0x3F)) # SHR operation
ref_51039 = ref_49542 # MOV operation
ref_73599 = ref_51039 # MOV operation
ref_76575 = ref_73599 # MOV operation
ref_76581 = (((sx(0x40, 0x6B33F46) * sx(0x40, ref_76575)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_88520 = ref_278 # MOV operation
ref_91496 = ref_88520 # MOV operation
ref_91504 = ((((0x0) << 64 | ref_91496) / 0x3) & 0xFFFFFFFFFFFFFFFF) # DIV operation
ref_92989 = ref_91504 # MOV operation
ref_93001 = ref_76581 # MOV operation
ref_93003 = ((ref_92989 - ref_93001) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_93011 = ref_93003 # MOV operation
ref_94503 = ref_93011 # MOV operation
ref_121575 = ref_94503 # MOV operation
ref_123039 = ref_121575 # MOV operation
ref_123053 = (ref_123039 >> (0x7 & 0x3F)) # SHR operation
ref_124542 = ref_123053 # MOV operation
ref_124556 = (ref_124542 >> (0x2 & 0x3F)) # SHR operation
ref_126045 = ref_124556 # MOV operation
ref_126059 = (0x7 & ref_126045) # AND operation
ref_129060 = ref_126059 # MOV operation
ref_129066 = (0x1 | ref_129060) # OR operation
ref_142512 = ref_278 # MOV operation
ref_143976 = ref_142512 # MOV operation
ref_143990 = ((0x9919884 + ref_143976) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_145480 = ref_143990 # MOV operation
ref_145492 = ref_129066 # MOV operation
ref_145494 = (ref_145480 >> ((ref_145492 & 0xFF) & 0x3F)) # SHR operation
ref_146991 = ref_145494 # MOV operation
ref_170970 = ref_278 # MOV operation
ref_172434 = ref_170970 # MOV operation
ref_172448 = ((0x1E5EA08F8 + ref_172434) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_173946 = ref_172448 # MOV operation
ref_218951 = ref_146991 # MOV operation
ref_238445 = ref_146991 # MOV operation
ref_239909 = ref_238445 # MOV operation
ref_239923 = (0x3F & ref_239909) # AND operation
ref_241412 = ref_239923 # MOV operation
ref_241426 = ((ref_241412 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_242923 = ref_218951 # MOV operation
ref_242927 = ref_241426 # MOV operation
ref_242929 = (ref_242927 | ref_242923) # OR operation
ref_244426 = ref_242929 # MOV operation
ref_287884 = ref_244426 # MOV operation
ref_305902 = ref_94503 # MOV operation
ref_307366 = ref_305902 # MOV operation
ref_307380 = (ref_307366 >> (0x2 & 0x3F)) # SHR operation
ref_308869 = ref_307380 # MOV operation
ref_308883 = (0xF & ref_308869) # AND operation
ref_311884 = ref_308883 # MOV operation
ref_311890 = (0x1 | ref_311884) # OR operation
ref_323917 = ref_51039 # MOV operation
ref_325381 = ref_323917 # MOV operation
ref_325393 = ref_311890 # MOV operation
ref_325395 = ((ref_325381 << ((ref_325393 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_340430 = ref_94503 # MOV operation
ref_341894 = ref_340430 # MOV operation
ref_341908 = (ref_341894 >> (0x2 & 0x3F)) # SHR operation
ref_343397 = ref_341908 # MOV operation
ref_343411 = (0xF & ref_343397) # AND operation
ref_346412 = ref_343411 # MOV operation
ref_346418 = (0x1 | ref_346412) # OR operation
ref_349423 = ref_346418 # MOV operation
ref_349425 = ((0x40 - ref_349423) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_349433 = ref_349425 # MOV operation
ref_361455 = ref_51039 # MOV operation
ref_362919 = ref_361455 # MOV operation
ref_362931 = ref_349433 # MOV operation
ref_362933 = (ref_362919 >> ((ref_362931 & 0xFF) & 0x3F)) # SHR operation
ref_364430 = ref_325395 # MOV operation
ref_364434 = ref_362933 # MOV operation
ref_364436 = (ref_364434 | ref_364430) # OR operation
ref_365925 = ref_364436 # MOV operation
ref_365939 = (0x7 & ref_365925) # AND operation
ref_367428 = ref_365939 # MOV operation
ref_367442 = ((ref_367428 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_368939 = ref_287884 # MOV operation
ref_368943 = ref_367442 # MOV operation
ref_368945 = (ref_368943 | ref_368939) # OR operation
ref_370442 = ref_368945 # MOV operation
ref_386944 = ref_173946 # MOV operation
ref_388408 = ref_386944 # MOV operation
ref_388422 = (ref_388408 >> (0x4 & 0x3F)) # SHR operation
ref_389911 = ref_388422 # MOV operation
ref_389925 = (0xF & ref_389911) # AND operation
ref_392926 = ref_389925 # MOV operation
ref_392932 = (0x1 | ref_392926) # OR operation
ref_404959 = ref_370442 # MOV operation
ref_406423 = ref_404959 # MOV operation
ref_406435 = ref_392932 # MOV operation
ref_406437 = (ref_406423 >> ((ref_406435 & 0xFF) & 0x3F)) # SHR operation
ref_421472 = ref_173946 # MOV operation
ref_422936 = ref_421472 # MOV operation
ref_422950 = (ref_422936 >> (0x4 & 0x3F)) # SHR operation
ref_424439 = ref_422950 # MOV operation
ref_424453 = (0xF & ref_424439) # AND operation
ref_427454 = ref_424453 # MOV operation
ref_427460 = (0x1 | ref_427454) # OR operation
ref_430465 = ref_427460 # MOV operation
ref_430467 = ((0x40 - ref_430465) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_430475 = ref_430467 # MOV operation
ref_442497 = ref_370442 # MOV operation
ref_443961 = ref_442497 # MOV operation
ref_443973 = ref_430475 # MOV operation
ref_443975 = ((ref_443961 << ((ref_443973 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_445472 = ref_406437 # MOV operation
ref_445476 = ref_443975 # MOV operation
ref_445478 = (ref_445476 | ref_445472) # OR operation
ref_460513 = ref_94503 # MOV operation
ref_461977 = ref_460513 # MOV operation
ref_461991 = (ref_461977 >> (0x3 & 0x3F)) # SHR operation
ref_463480 = ref_461991 # MOV operation
ref_463494 = (0xF & ref_463480) # AND operation
ref_466495 = ref_463494 # MOV operation
ref_466501 = (0x1 | ref_466495) # OR operation
ref_478528 = ref_51039 # MOV operation
ref_479992 = ref_478528 # MOV operation
ref_480004 = ref_466501 # MOV operation
ref_480006 = (ref_479992 >> ((ref_480004 & 0xFF) & 0x3F)) # SHR operation
ref_495041 = ref_94503 # MOV operation
ref_496505 = ref_495041 # MOV operation
ref_496519 = (ref_496505 >> (0x3 & 0x3F)) # SHR operation
ref_498008 = ref_496519 # MOV operation
ref_498022 = (0xF & ref_498008) # AND operation
ref_501023 = ref_498022 # MOV operation
ref_501029 = (0x1 | ref_501023) # OR operation
ref_504034 = ref_501029 # MOV operation
ref_504036 = ((0x40 - ref_504034) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_504044 = ref_504036 # MOV operation
ref_516066 = ref_51039 # MOV operation
ref_517530 = ref_516066 # MOV operation
ref_517542 = ref_504044 # MOV operation
ref_517544 = ((ref_517530 << ((ref_517542 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_519041 = ref_480006 # MOV operation
ref_519045 = ref_517544 # MOV operation
ref_519047 = (ref_519045 | ref_519041) # OR operation
ref_520536 = ref_519047 # MOV operation
ref_520548 = ref_445478 # MOV operation
ref_520550 = ((ref_520536 - ref_520548) & 0xFFFFFFFFFFFFFFFF) # CMP operation
ref_520552 = ((((ref_520536 ^ (ref_520548 ^ ref_520550)) ^ ((ref_520536 ^ ref_520550) & (ref_520536 ^ ref_520548))) >> 63) & 0x1) # Carry flag
ref_520556 = (0x1 if (ref_520550 == 0x0) else 0x0) # Zero flag
ref_520558 = ((((ref_520548 >> 8) & 0xFFFFFFFFFFFFFF)) << 8 | (0x1 if (((~(ref_520552) & 0x1) & (~(ref_520556) & 0x1)) == 0x1) else 0x0)) # SETA operation
ref_520560 = (ref_520558 & 0xFF) # MOVZX operation
ref_522036 = (ref_520560 & 0xFFFFFFFF) # MOV operation
ref_522038 = ((ref_522036 & 0xFFFFFFFF) & (ref_522036 & 0xFFFFFFFF)) # TEST operation
ref_522043 = (0x1 if (ref_522038 == 0x0) else 0x0) # Zero flag
ref_522045 = (0x1A74 if (ref_522043 == 0x1) else 0x1A56) # Program Counter


if (ref_522043 == 0x1):
    ref_263 = SymVar_0
    ref_278 = ref_263 # MOV operation
    ref_30134 = ref_278 # MOV operation
    ref_31598 = ref_30134 # MOV operation
    ref_31612 = ((ref_31598 << (0xB & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_45058 = ref_278 # MOV operation
    ref_46522 = ref_45058 # MOV operation
    ref_46536 = (ref_46522 >> (0x35 & 0x3F)) # SHR operation
    ref_48033 = ref_31612 # MOV operation
    ref_48037 = ref_46536 # MOV operation
    ref_48039 = (ref_48037 | ref_48033) # OR operation
    ref_49528 = ref_48039 # MOV operation
    ref_49542 = (ref_49528 >> (0x1 & 0x3F)) # SHR operation
    ref_51039 = ref_49542 # MOV operation
    ref_73599 = ref_51039 # MOV operation
    ref_76575 = ref_73599 # MOV operation
    ref_76581 = (((sx(0x40, 0x6B33F46) * sx(0x40, ref_76575)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_88520 = ref_278 # MOV operation
    ref_91496 = ref_88520 # MOV operation
    ref_91504 = ((((0x0) << 64 | ref_91496) / 0x3) & 0xFFFFFFFFFFFFFFFF) # DIV operation
    ref_92989 = ref_91504 # MOV operation
    ref_93001 = ref_76581 # MOV operation
    ref_93003 = ((ref_92989 - ref_93001) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_93011 = ref_93003 # MOV operation
    ref_94503 = ref_93011 # MOV operation
    ref_121575 = ref_94503 # MOV operation
    ref_123039 = ref_121575 # MOV operation
    ref_123053 = (ref_123039 >> (0x7 & 0x3F)) # SHR operation
    ref_124542 = ref_123053 # MOV operation
    ref_124556 = (ref_124542 >> (0x2 & 0x3F)) # SHR operation
    ref_126045 = ref_124556 # MOV operation
    ref_126059 = (0x7 & ref_126045) # AND operation
    ref_129060 = ref_126059 # MOV operation
    ref_129066 = (0x1 | ref_129060) # OR operation
    ref_142512 = ref_278 # MOV operation
    ref_143976 = ref_142512 # MOV operation
    ref_143990 = ((0x9919884 + ref_143976) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_145480 = ref_143990 # MOV operation
    ref_145492 = ref_129066 # MOV operation
    ref_145494 = (ref_145480 >> ((ref_145492 & 0xFF) & 0x3F)) # SHR operation
    ref_146991 = ref_145494 # MOV operation
    ref_170970 = ref_278 # MOV operation
    ref_172434 = ref_170970 # MOV operation
    ref_172448 = ((0x1E5EA08F8 + ref_172434) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_173946 = ref_172448 # MOV operation
    ref_218951 = ref_146991 # MOV operation
    ref_238445 = ref_146991 # MOV operation
    ref_239909 = ref_238445 # MOV operation
    ref_239923 = (0x3F & ref_239909) # AND operation
    ref_241412 = ref_239923 # MOV operation
    ref_241426 = ((ref_241412 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_242923 = ref_218951 # MOV operation
    ref_242927 = ref_241426 # MOV operation
    ref_242929 = (ref_242927 | ref_242923) # OR operation
    ref_244426 = ref_242929 # MOV operation
    ref_287884 = ref_244426 # MOV operation
    ref_305902 = ref_94503 # MOV operation
    ref_307366 = ref_305902 # MOV operation
    ref_307380 = (ref_307366 >> (0x2 & 0x3F)) # SHR operation
    ref_308869 = ref_307380 # MOV operation
    ref_308883 = (0xF & ref_308869) # AND operation
    ref_311884 = ref_308883 # MOV operation
    ref_311890 = (0x1 | ref_311884) # OR operation
    ref_323917 = ref_51039 # MOV operation
    ref_325381 = ref_323917 # MOV operation
    ref_325393 = ref_311890 # MOV operation
    ref_325395 = ((ref_325381 << ((ref_325393 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_340430 = ref_94503 # MOV operation
    ref_341894 = ref_340430 # MOV operation
    ref_341908 = (ref_341894 >> (0x2 & 0x3F)) # SHR operation
    ref_343397 = ref_341908 # MOV operation
    ref_343411 = (0xF & ref_343397) # AND operation
    ref_346412 = ref_343411 # MOV operation
    ref_346418 = (0x1 | ref_346412) # OR operation
    ref_349423 = ref_346418 # MOV operation
    ref_349425 = ((0x40 - ref_349423) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_349433 = ref_349425 # MOV operation
    ref_361455 = ref_51039 # MOV operation
    ref_362919 = ref_361455 # MOV operation
    ref_362931 = ref_349433 # MOV operation
    ref_362933 = (ref_362919 >> ((ref_362931 & 0xFF) & 0x3F)) # SHR operation
    ref_364430 = ref_325395 # MOV operation
    ref_364434 = ref_362933 # MOV operation
    ref_364436 = (ref_364434 | ref_364430) # OR operation
    ref_365925 = ref_364436 # MOV operation
    ref_365939 = (0x7 & ref_365925) # AND operation
    ref_367428 = ref_365939 # MOV operation
    ref_367442 = ((ref_367428 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_368939 = ref_287884 # MOV operation
    ref_368943 = ref_367442 # MOV operation
    ref_368945 = (ref_368943 | ref_368939) # OR operation
    ref_370442 = ref_368945 # MOV operation
    ref_546086 = ref_94503 # MOV operation
    ref_561096 = ref_94503 # MOV operation
    ref_562560 = ref_561096 # MOV operation
    ref_562574 = (0xF & ref_562560) # AND operation
    ref_564063 = ref_562574 # MOV operation
    ref_564077 = ((ref_564063 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_565574 = ref_546086 # MOV operation
    ref_565578 = ref_564077 # MOV operation
    ref_565580 = (ref_565578 | ref_565574) # OR operation
    ref_567077 = ref_565580 # MOV operation
    ref_589637 = ref_51039 # MOV operation
    ref_604647 = ref_567077 # MOV operation
    ref_616649 = ref_370442 # MOV operation
    ref_618113 = ref_616649 # MOV operation
    ref_618125 = ref_604647 # MOV operation
    ref_618127 = (ref_618125 & ref_618113) # AND operation
    ref_619616 = ref_618127 # MOV operation
    ref_619630 = (0x1F & ref_619616) # AND operation
    ref_621119 = ref_619630 # MOV operation
    ref_621133 = ((ref_621119 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_622630 = ref_589637 # MOV operation
    ref_622634 = ref_621133 # MOV operation
    ref_622636 = (ref_622634 | ref_622630) # OR operation
    ref_624133 = ref_622636 # MOV operation
    ref_648089 = ref_624133 # MOV operation
    ref_660091 = ref_567077 # MOV operation
    ref_661563 = ref_648089 # MOV operation
    ref_661567 = ref_660091 # MOV operation
    ref_661569 = (ref_661567 | ref_661563) # OR operation
    ref_673596 = ref_370442 # MOV operation
    ref_685598 = ref_173946 # MOV operation
    ref_687070 = ref_673596 # MOV operation
    ref_687074 = ref_685598 # MOV operation
    ref_687076 = (((sx(0x40, ref_687074) * sx(0x40, ref_687070)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_688570 = ref_661569 # MOV operation
    ref_688574 = ref_687076 # MOV operation
    ref_688576 = (((sx(0x40, ref_688574) * sx(0x40, ref_688570)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_690070 = ref_688576 # MOV operation
    ref_693057 = ref_690070 # MOV operation
    ref_693059 = ref_693057 # MOV operation
    endb = ref_693059


else:
    ref_693379 = SymVar_0
    ref_693394 = ref_693379 # MOV operation
    ref_723255 = ref_693394 # MOV operation
    ref_724719 = ref_723255 # MOV operation
    ref_724733 = ((ref_724719 << (0xB & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_738179 = ref_693394 # MOV operation
    ref_739643 = ref_738179 # MOV operation
    ref_739657 = (ref_739643 >> (0x35 & 0x3F)) # SHR operation
    ref_741154 = ref_724733 # MOV operation
    ref_741158 = ref_739657 # MOV operation
    ref_741160 = (ref_741158 | ref_741154) # OR operation
    ref_742649 = ref_741160 # MOV operation
    ref_742663 = (ref_742649 >> (0x1 & 0x3F)) # SHR operation
    ref_744160 = ref_742663 # MOV operation
    ref_766720 = ref_744160 # MOV operation
    ref_769696 = ref_766720 # MOV operation
    ref_769702 = (((sx(0x40, 0x6B33F46) * sx(0x40, ref_769696)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_781641 = ref_693394 # MOV operation
    ref_784617 = ref_781641 # MOV operation
    ref_784625 = ((((0x0) << 64 | ref_784617) / 0x3) & 0xFFFFFFFFFFFFFFFF) # DIV operation
    ref_786110 = ref_784625 # MOV operation
    ref_786122 = ref_769702 # MOV operation
    ref_786124 = ((ref_786110 - ref_786122) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_786132 = ref_786124 # MOV operation
    ref_787624 = ref_786132 # MOV operation
    ref_814696 = ref_787624 # MOV operation
    ref_816160 = ref_814696 # MOV operation
    ref_816174 = (ref_816160 >> (0x7 & 0x3F)) # SHR operation
    ref_817663 = ref_816174 # MOV operation
    ref_817677 = (ref_817663 >> (0x2 & 0x3F)) # SHR operation
    ref_819166 = ref_817677 # MOV operation
    ref_819180 = (0x7 & ref_819166) # AND operation
    ref_822181 = ref_819180 # MOV operation
    ref_822187 = (0x1 | ref_822181) # OR operation
    ref_835633 = ref_693394 # MOV operation
    ref_837097 = ref_835633 # MOV operation
    ref_837111 = ((0x9919884 + ref_837097) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_838601 = ref_837111 # MOV operation
    ref_838613 = ref_822187 # MOV operation
    ref_838615 = (ref_838601 >> ((ref_838613 & 0xFF) & 0x3F)) # SHR operation
    ref_840112 = ref_838615 # MOV operation
    ref_864091 = ref_693394 # MOV operation
    ref_865555 = ref_864091 # MOV operation
    ref_865569 = ((0x1E5EA08F8 + ref_865555) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_867067 = ref_865569 # MOV operation
    ref_912072 = ref_840112 # MOV operation
    ref_931566 = ref_840112 # MOV operation
    ref_933030 = ref_931566 # MOV operation
    ref_933044 = (0x3F & ref_933030) # AND operation
    ref_934533 = ref_933044 # MOV operation
    ref_934547 = ((ref_934533 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_936044 = ref_912072 # MOV operation
    ref_936048 = ref_934547 # MOV operation
    ref_936050 = (ref_936048 | ref_936044) # OR operation
    ref_937547 = ref_936050 # MOV operation
    ref_981005 = ref_937547 # MOV operation
    ref_999023 = ref_787624 # MOV operation
    ref_1000487 = ref_999023 # MOV operation
    ref_1000501 = (ref_1000487 >> (0x2 & 0x3F)) # SHR operation
    ref_1001990 = ref_1000501 # MOV operation
    ref_1002004 = (0xF & ref_1001990) # AND operation
    ref_1005005 = ref_1002004 # MOV operation
    ref_1005011 = (0x1 | ref_1005005) # OR operation
    ref_1017038 = ref_744160 # MOV operation
    ref_1018502 = ref_1017038 # MOV operation
    ref_1018514 = ref_1005011 # MOV operation
    ref_1018516 = ((ref_1018502 << ((ref_1018514 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_1033551 = ref_787624 # MOV operation
    ref_1035015 = ref_1033551 # MOV operation
    ref_1035029 = (ref_1035015 >> (0x2 & 0x3F)) # SHR operation
    ref_1036518 = ref_1035029 # MOV operation
    ref_1036532 = (0xF & ref_1036518) # AND operation
    ref_1039533 = ref_1036532 # MOV operation
    ref_1039539 = (0x1 | ref_1039533) # OR operation
    ref_1042544 = ref_1039539 # MOV operation
    ref_1042546 = ((0x40 - ref_1042544) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_1042554 = ref_1042546 # MOV operation
    ref_1054576 = ref_744160 # MOV operation
    ref_1056040 = ref_1054576 # MOV operation
    ref_1056052 = ref_1042554 # MOV operation
    ref_1056054 = (ref_1056040 >> ((ref_1056052 & 0xFF) & 0x3F)) # SHR operation
    ref_1057551 = ref_1018516 # MOV operation
    ref_1057555 = ref_1056054 # MOV operation
    ref_1057557 = (ref_1057555 | ref_1057551) # OR operation
    ref_1059046 = ref_1057557 # MOV operation
    ref_1059060 = (0x7 & ref_1059046) # AND operation
    ref_1060549 = ref_1059060 # MOV operation
    ref_1060563 = ((ref_1060549 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_1062060 = ref_981005 # MOV operation
    ref_1062064 = ref_1060563 # MOV operation
    ref_1062066 = (ref_1062064 | ref_1062060) # OR operation
    ref_1063563 = ref_1062066 # MOV operation
    ref_1063565 = ((ref_1063563 >> 56) & 0xFF) # Byte reference - MOV operation
    ref_1063566 = ((ref_1063563 >> 48) & 0xFF) # Byte reference - MOV operation
    ref_1063567 = ((ref_1063563 >> 40) & 0xFF) # Byte reference - MOV operation
    ref_1063568 = ((ref_1063563 >> 32) & 0xFF) # Byte reference - MOV operation
    ref_1063569 = ((ref_1063563 >> 24) & 0xFF) # Byte reference - MOV operation
    ref_1063570 = ((ref_1063563 >> 16) & 0xFF) # Byte reference - MOV operation
    ref_1063571 = ((ref_1063563 >> 8) & 0xFF) # Byte reference - MOV operation
    ref_1063572 = (ref_1063563 & 0xFF) # Byte reference - MOV operation
    ref_1240750 = ref_867067 # MOV operation
    ref_1242214 = ref_1240750 # MOV operation
    ref_1242228 = (ref_1242214 >> (0x3 & 0x3F)) # SHR operation
    ref_1243717 = ref_1242228 # MOV operation
    ref_1243731 = (0xF & ref_1243717) # AND operation
    ref_1246732 = ref_1243731 # MOV operation
    ref_1246738 = (0x1 | ref_1246732) # OR operation
    ref_1258765 = ref_867067 # MOV operation
    ref_1260229 = ref_1258765 # MOV operation
    ref_1260241 = ref_1246738 # MOV operation
    ref_1260243 = ((ref_1260229 << ((ref_1260241 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_1275278 = ref_867067 # MOV operation
    ref_1276742 = ref_1275278 # MOV operation
    ref_1276756 = (ref_1276742 >> (0x3 & 0x3F)) # SHR operation
    ref_1278245 = ref_1276756 # MOV operation
    ref_1278259 = (0xF & ref_1278245) # AND operation
    ref_1281260 = ref_1278259 # MOV operation
    ref_1281266 = (0x1 | ref_1281260) # OR operation
    ref_1284271 = ref_1281266 # MOV operation
    ref_1284273 = ((0x40 - ref_1284271) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_1284281 = ref_1284273 # MOV operation
    ref_1296303 = ref_867067 # MOV operation
    ref_1297767 = ref_1296303 # MOV operation
    ref_1297779 = ref_1284281 # MOV operation
    ref_1297781 = (ref_1297767 >> ((ref_1297779 & 0xFF) & 0x3F)) # SHR operation
    ref_1299278 = ref_1260243 # MOV operation
    ref_1299282 = ref_1297781 # MOV operation
    ref_1299284 = (ref_1299282 | ref_1299278) # OR operation
    ref_1300781 = ref_1299284 # MOV operation
    ref_1321737 = ref_1063571 # MOVZX operation
    ref_1324717 = (ref_1321737 & 0xFF) # MOVZX operation
    ref_1345665 = ref_1063569 # MOVZX operation
    ref_1366601 = (ref_1345665 & 0xFF) # MOVZX operation
    ref_1366603 = (ref_1366601 & 0xFF) # Byte reference - MOV operation
    ref_1369593 = (ref_1324717 & 0xFF) # MOVZX operation
    ref_1390529 = (ref_1369593 & 0xFF) # MOVZX operation
    ref_1390531 = (ref_1390529 & 0xFF) # Byte reference - MOV operation
    ref_1414477 = ref_1300781 # MOV operation
    ref_1426479 = ref_787624 # MOV operation
    ref_1427951 = ref_1414477 # MOV operation
    ref_1427955 = ref_1426479 # MOV operation
    ref_1427957 = (ref_1427955 | ref_1427951) # OR operation
    ref_1439984 = ((((((((ref_1063565) << 8 | ref_1063566) << 8 | ref_1063567) << 8 | ref_1063568) << 8 | ref_1390531) << 8 | ref_1063570) << 8 | ref_1366603) << 8 | ref_1063572) # MOV operation
    ref_1451986 = ref_867067 # MOV operation
    ref_1453458 = ref_1439984 # MOV operation
    ref_1453462 = ref_1451986 # MOV operation
    ref_1453464 = (((sx(0x40, ref_1453462) * sx(0x40, ref_1453458)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_1454958 = ref_1427957 # MOV operation
    ref_1454962 = ref_1453464 # MOV operation
    ref_1454964 = (((sx(0x40, ref_1454962) * sx(0x40, ref_1454958)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_1456458 = ref_1454964 # MOV operation
    ref_1459445 = ref_1456458 # MOV operation
    ref_1459447 = ref_1459445 # MOV operation
    endb = ref_1459447


print(endb & 0xffffffffffffffff)
