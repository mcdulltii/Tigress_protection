#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])

ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_41762 = ref_278 # MOV operation
ref_43910 = ref_41762 # MOV operation
ref_43924 = ((ref_43910 << (0xB & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_63526 = ref_278 # MOV operation
ref_65674 = ref_63526 # MOV operation
ref_65688 = (ref_65674 >> (0x35 & 0x3F)) # SHR operation
ref_67869 = ref_43924 # MOV operation
ref_67873 = ref_65688 # MOV operation
ref_67875 = (ref_67873 | ref_67869) # OR operation
ref_70048 = ref_67875 # MOV operation
ref_70062 = (ref_70048 >> (0x1 & 0x3F)) # SHR operation
ref_72243 = ref_70062 # MOV operation
ref_105063 = ref_72243 # MOV operation
ref_109407 = ref_105063 # MOV operation
ref_109413 = (((sx(0x40, 0x6B33F46) * sx(0x40, ref_109407)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_126824 = ref_278 # MOV operation
ref_131168 = ref_126824 # MOV operation
ref_131176 = ((((0x0) << 64 | ref_131168) / 0x3) & 0xFFFFFFFFFFFFFFFF) # DIV operation
ref_133345 = ref_131176 # MOV operation
ref_133357 = ref_109413 # MOV operation
ref_133359 = ((ref_133345 - ref_133357) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_133367 = ref_133359 # MOV operation
ref_135543 = ref_133367 # MOV operation
ref_174927 = ref_135543 # MOV operation
ref_177075 = ref_174927 # MOV operation
ref_177089 = (ref_177075 >> (0x7 & 0x3F)) # SHR operation
ref_179262 = ref_177089 # MOV operation
ref_179276 = (ref_179262 >> (0x2 & 0x3F)) # SHR operation
ref_181449 = ref_179276 # MOV operation
ref_181463 = (0x7 & ref_181449) # AND operation
ref_185832 = ref_181463 # MOV operation
ref_185838 = (0x1 | ref_185832) # OR operation
ref_205440 = ref_278 # MOV operation
ref_207588 = ref_205440 # MOV operation
ref_207602 = ((0x9919884 + ref_207588) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_209776 = ref_207602 # MOV operation
ref_209788 = ref_185838 # MOV operation
ref_209790 = (ref_209776 >> ((ref_209788 & 0xFF) & 0x3F)) # SHR operation
ref_211971 = ref_209790 # MOV operation
ref_246894 = ref_278 # MOV operation
ref_249042 = ref_246894 # MOV operation
ref_249056 = ((0x1E5EA08F8 + ref_249042) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_251238 = ref_249056 # MOV operation
ref_316763 = ref_211971 # MOV operation
ref_345149 = ref_211971 # MOV operation
ref_347297 = ref_345149 # MOV operation
ref_347311 = (0x3F & ref_347297) # AND operation
ref_349484 = ref_347311 # MOV operation
ref_349498 = ((ref_349484 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_351679 = ref_316763 # MOV operation
ref_351683 = ref_349498 # MOV operation
ref_351685 = (ref_351683 | ref_351679) # OR operation
ref_353866 = ref_351685 # MOV operation
ref_417160 = ref_353866 # MOV operation
ref_443386 = ref_135543 # MOV operation
ref_445534 = ref_443386 # MOV operation
ref_445548 = (ref_445534 >> (0x2 & 0x3F)) # SHR operation
ref_447721 = ref_445548 # MOV operation
ref_447735 = (0xF & ref_447721) # AND operation
ref_452104 = ref_447735 # MOV operation
ref_452110 = (0x1 | ref_452104) # OR operation
ref_469609 = ref_72243 # MOV operation
ref_471757 = ref_469609 # MOV operation
ref_471769 = ref_452110 # MOV operation
ref_471771 = ((ref_471757 << ((ref_471769 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_493646 = ref_135543 # MOV operation
ref_495794 = ref_493646 # MOV operation
ref_495808 = (ref_495794 >> (0x2 & 0x3F)) # SHR operation
ref_497981 = ref_495808 # MOV operation
ref_497995 = (0xF & ref_497981) # AND operation
ref_502364 = ref_497995 # MOV operation
ref_502370 = (0x1 | ref_502364) # OR operation
ref_506743 = ref_502370 # MOV operation
ref_506745 = ((0x40 - ref_506743) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_506753 = ref_506745 # MOV operation
ref_524247 = ref_72243 # MOV operation
ref_526395 = ref_524247 # MOV operation
ref_526407 = ref_506753 # MOV operation
ref_526409 = (ref_526395 >> ((ref_526407 & 0xFF) & 0x3F)) # SHR operation
ref_528590 = ref_471771 # MOV operation
ref_528594 = ref_526409 # MOV operation
ref_528596 = (ref_528594 | ref_528590) # OR operation
ref_530769 = ref_528596 # MOV operation
ref_530783 = (0x7 & ref_530769) # AND operation
ref_532956 = ref_530783 # MOV operation
ref_532970 = ((ref_532956 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_535151 = ref_417160 # MOV operation
ref_535155 = ref_532970 # MOV operation
ref_535157 = (ref_535155 | ref_535151) # OR operation
ref_537338 = ref_535157 # MOV operation
ref_561364 = ref_251238 # MOV operation
ref_563512 = ref_561364 # MOV operation
ref_563526 = (ref_563512 >> (0x4 & 0x3F)) # SHR operation
ref_565699 = ref_563526 # MOV operation
ref_565713 = (0xF & ref_565699) # AND operation
ref_570082 = ref_565713 # MOV operation
ref_570088 = (0x1 | ref_570082) # OR operation
ref_587587 = ref_537338 # MOV operation
ref_589735 = ref_587587 # MOV operation
ref_589747 = ref_570088 # MOV operation
ref_589749 = (ref_589735 >> ((ref_589747 & 0xFF) & 0x3F)) # SHR operation
ref_611624 = ref_251238 # MOV operation
ref_613772 = ref_611624 # MOV operation
ref_613786 = (ref_613772 >> (0x4 & 0x3F)) # SHR operation
ref_615959 = ref_613786 # MOV operation
ref_615973 = (0xF & ref_615959) # AND operation
ref_620342 = ref_615973 # MOV operation
ref_620348 = (0x1 | ref_620342) # OR operation
ref_624721 = ref_620348 # MOV operation
ref_624723 = ((0x40 - ref_624721) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_624731 = ref_624723 # MOV operation
ref_642225 = ref_537338 # MOV operation
ref_644373 = ref_642225 # MOV operation
ref_644385 = ref_624731 # MOV operation
ref_644387 = ((ref_644373 << ((ref_644385 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_646568 = ref_589749 # MOV operation
ref_646572 = ref_644387 # MOV operation
ref_646574 = (ref_646572 | ref_646568) # OR operation
ref_668449 = ref_135543 # MOV operation
ref_670597 = ref_668449 # MOV operation
ref_670611 = (ref_670597 >> (0x3 & 0x3F)) # SHR operation
ref_672784 = ref_670611 # MOV operation
ref_672798 = (0xF & ref_672784) # AND operation
ref_677167 = ref_672798 # MOV operation
ref_677173 = (0x1 | ref_677167) # OR operation
ref_694672 = ref_72243 # MOV operation
ref_696820 = ref_694672 # MOV operation
ref_696832 = ref_677173 # MOV operation
ref_696834 = (ref_696820 >> ((ref_696832 & 0xFF) & 0x3F)) # SHR operation
ref_718709 = ref_135543 # MOV operation
ref_720857 = ref_718709 # MOV operation
ref_720871 = (ref_720857 >> (0x3 & 0x3F)) # SHR operation
ref_723044 = ref_720871 # MOV operation
ref_723058 = (0xF & ref_723044) # AND operation
ref_727427 = ref_723058 # MOV operation
ref_727433 = (0x1 | ref_727427) # OR operation
ref_731806 = ref_727433 # MOV operation
ref_731808 = ((0x40 - ref_731806) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_731816 = ref_731808 # MOV operation
ref_749310 = ref_72243 # MOV operation
ref_751458 = ref_749310 # MOV operation
ref_751470 = ref_731816 # MOV operation
ref_751472 = ((ref_751458 << ((ref_751470 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_753653 = ref_696834 # MOV operation
ref_753657 = ref_751472 # MOV operation
ref_753659 = (ref_753657 | ref_753653) # OR operation
ref_755832 = ref_753659 # MOV operation
ref_755844 = ref_646574 # MOV operation
ref_755846 = ((ref_755832 - ref_755844) & 0xFFFFFFFFFFFFFFFF) # CMP operation
ref_755848 = ((((ref_755832 ^ (ref_755844 ^ ref_755846)) ^ ((ref_755832 ^ ref_755846) & (ref_755832 ^ ref_755844))) >> 63) & 0x1) # Carry flag
ref_755852 = (0x1 if (ref_755846 == 0x0) else 0x0) # Zero flag
ref_755854 = ((((ref_755844 >> 8) & 0xFFFFFFFFFFFFFF)) << 8 | (0x1 if (((~(ref_755848) & 0x1) & (~(ref_755852) & 0x1)) == 0x1) else 0x0)) # SETA operation
ref_755856 = (ref_755854 & 0xFF) # MOVZX operation
ref_758016 = (ref_755856 & 0xFFFFFFFF) # MOV operation
ref_758018 = ((ref_758016 & 0xFFFFFFFF) & (ref_758016 & 0xFFFFFFFF)) # TEST operation
ref_758023 = (0x1 if (ref_758018 == 0x0) else 0x0) # Zero flag
ref_758025 = (0x1A74 if (ref_758023 == 0x1) else 0x1A56) # Program Counter


if (ref_758023 == 0x1):
    ref_263 = SymVar_0
    ref_278 = ref_263 # MOV operation
    ref_41762 = ref_278 # MOV operation
    ref_43910 = ref_41762 # MOV operation
    ref_43924 = ((ref_43910 << (0xB & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_63526 = ref_278 # MOV operation
    ref_65674 = ref_63526 # MOV operation
    ref_65688 = (ref_65674 >> (0x35 & 0x3F)) # SHR operation
    ref_67869 = ref_43924 # MOV operation
    ref_67873 = ref_65688 # MOV operation
    ref_67875 = (ref_67873 | ref_67869) # OR operation
    ref_70048 = ref_67875 # MOV operation
    ref_70062 = (ref_70048 >> (0x1 & 0x3F)) # SHR operation
    ref_72243 = ref_70062 # MOV operation
    ref_105063 = ref_72243 # MOV operation
    ref_109407 = ref_105063 # MOV operation
    ref_109413 = (((sx(0x40, 0x6B33F46) * sx(0x40, ref_109407)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_126824 = ref_278 # MOV operation
    ref_131168 = ref_126824 # MOV operation
    ref_131176 = ((((0x0) << 64 | ref_131168) / 0x3) & 0xFFFFFFFFFFFFFFFF) # DIV operation
    ref_133345 = ref_131176 # MOV operation
    ref_133357 = ref_109413 # MOV operation
    ref_133359 = ((ref_133345 - ref_133357) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_133367 = ref_133359 # MOV operation
    ref_135543 = ref_133367 # MOV operation
    ref_174927 = ref_135543 # MOV operation
    ref_177075 = ref_174927 # MOV operation
    ref_177089 = (ref_177075 >> (0x7 & 0x3F)) # SHR operation
    ref_179262 = ref_177089 # MOV operation
    ref_179276 = (ref_179262 >> (0x2 & 0x3F)) # SHR operation
    ref_181449 = ref_179276 # MOV operation
    ref_181463 = (0x7 & ref_181449) # AND operation
    ref_185832 = ref_181463 # MOV operation
    ref_185838 = (0x1 | ref_185832) # OR operation
    ref_205440 = ref_278 # MOV operation
    ref_207588 = ref_205440 # MOV operation
    ref_207602 = ((0x9919884 + ref_207588) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_209776 = ref_207602 # MOV operation
    ref_209788 = ref_185838 # MOV operation
    ref_209790 = (ref_209776 >> ((ref_209788 & 0xFF) & 0x3F)) # SHR operation
    ref_211971 = ref_209790 # MOV operation
    ref_246894 = ref_278 # MOV operation
    ref_249042 = ref_246894 # MOV operation
    ref_249056 = ((0x1E5EA08F8 + ref_249042) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_251238 = ref_249056 # MOV operation
    ref_316763 = ref_211971 # MOV operation
    ref_345149 = ref_211971 # MOV operation
    ref_347297 = ref_345149 # MOV operation
    ref_347311 = (0x3F & ref_347297) # AND operation
    ref_349484 = ref_347311 # MOV operation
    ref_349498 = ((ref_349484 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_351679 = ref_316763 # MOV operation
    ref_351683 = ref_349498 # MOV operation
    ref_351685 = (ref_351683 | ref_351679) # OR operation
    ref_353866 = ref_351685 # MOV operation
    ref_417160 = ref_353866 # MOV operation
    ref_443386 = ref_135543 # MOV operation
    ref_445534 = ref_443386 # MOV operation
    ref_445548 = (ref_445534 >> (0x2 & 0x3F)) # SHR operation
    ref_447721 = ref_445548 # MOV operation
    ref_447735 = (0xF & ref_447721) # AND operation
    ref_452104 = ref_447735 # MOV operation
    ref_452110 = (0x1 | ref_452104) # OR operation
    ref_469609 = ref_72243 # MOV operation
    ref_471757 = ref_469609 # MOV operation
    ref_471769 = ref_452110 # MOV operation
    ref_471771 = ((ref_471757 << ((ref_471769 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_493646 = ref_135543 # MOV operation
    ref_495794 = ref_493646 # MOV operation
    ref_495808 = (ref_495794 >> (0x2 & 0x3F)) # SHR operation
    ref_497981 = ref_495808 # MOV operation
    ref_497995 = (0xF & ref_497981) # AND operation
    ref_502364 = ref_497995 # MOV operation
    ref_502370 = (0x1 | ref_502364) # OR operation
    ref_506743 = ref_502370 # MOV operation
    ref_506745 = ((0x40 - ref_506743) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_506753 = ref_506745 # MOV operation
    ref_524247 = ref_72243 # MOV operation
    ref_526395 = ref_524247 # MOV operation
    ref_526407 = ref_506753 # MOV operation
    ref_526409 = (ref_526395 >> ((ref_526407 & 0xFF) & 0x3F)) # SHR operation
    ref_528590 = ref_471771 # MOV operation
    ref_528594 = ref_526409 # MOV operation
    ref_528596 = (ref_528594 | ref_528590) # OR operation
    ref_530769 = ref_528596 # MOV operation
    ref_530783 = (0x7 & ref_530769) # AND operation
    ref_532956 = ref_530783 # MOV operation
    ref_532970 = ((ref_532956 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_535151 = ref_417160 # MOV operation
    ref_535155 = ref_532970 # MOV operation
    ref_535157 = (ref_535155 | ref_535151) # OR operation
    ref_537338 = ref_535157 # MOV operation
    ref_793010 = ref_135543 # MOV operation
    ref_814860 = ref_135543 # MOV operation
    ref_817008 = ref_814860 # MOV operation
    ref_817022 = (0xF & ref_817008) # AND operation
    ref_819195 = ref_817022 # MOV operation
    ref_819209 = ((ref_819195 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_821390 = ref_793010 # MOV operation
    ref_821394 = ref_819209 # MOV operation
    ref_821396 = (ref_821394 | ref_821390) # OR operation
    ref_823577 = ref_821396 # MOV operation
    ref_856397 = ref_72243 # MOV operation
    ref_878247 = ref_823577 # MOV operation
    ref_895721 = ref_537338 # MOV operation
    ref_897869 = ref_895721 # MOV operation
    ref_897881 = ref_878247 # MOV operation
    ref_897883 = (ref_897881 & ref_897869) # AND operation
    ref_900056 = ref_897883 # MOV operation
    ref_900070 = (0x1F & ref_900056) # AND operation
    ref_902243 = ref_900070 # MOV operation
    ref_902257 = ((ref_902243 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_904438 = ref_856397 # MOV operation
    ref_904442 = ref_902257 # MOV operation
    ref_904444 = (ref_904442 | ref_904438) # OR operation
    ref_906625 = ref_904444 # MOV operation
    ref_941525 = ref_906625 # MOV operation
    ref_958999 = ref_823577 # MOV operation
    ref_961155 = ref_941525 # MOV operation
    ref_961159 = ref_958999 # MOV operation
    ref_961161 = (ref_961159 | ref_961155) # OR operation
    ref_978660 = ref_537338 # MOV operation
    ref_996134 = ref_251238 # MOV operation
    ref_998290 = ref_978660 # MOV operation
    ref_998294 = ref_996134 # MOV operation
    ref_998296 = (((sx(0x40, ref_998294) * sx(0x40, ref_998290)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_1000474 = ref_961161 # MOV operation
    ref_1000478 = ref_998296 # MOV operation
    ref_1000480 = (((sx(0x40, ref_1000478) * sx(0x40, ref_1000474)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_1002658 = ref_1000480 # MOV operation
    ref_1007013 = ref_1002658 # MOV operation
    ref_1007015 = ref_1007013 # MOV operation
    endb = ref_1007015


else:
    ref_1007335 = SymVar_0
    ref_1007350 = ref_1007335 # MOV operation
    ref_1048839 = ref_1007350 # MOV operation
    ref_1050987 = ref_1048839 # MOV operation
    ref_1051001 = ((ref_1050987 << (0xB & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_1070603 = ref_1007350 # MOV operation
    ref_1072751 = ref_1070603 # MOV operation
    ref_1072765 = (ref_1072751 >> (0x35 & 0x3F)) # SHR operation
    ref_1074946 = ref_1051001 # MOV operation
    ref_1074950 = ref_1072765 # MOV operation
    ref_1074952 = (ref_1074950 | ref_1074946) # OR operation
    ref_1077125 = ref_1074952 # MOV operation
    ref_1077139 = (ref_1077125 >> (0x1 & 0x3F)) # SHR operation
    ref_1079320 = ref_1077139 # MOV operation
    ref_1112140 = ref_1079320 # MOV operation
    ref_1116484 = ref_1112140 # MOV operation
    ref_1116490 = (((sx(0x40, 0x6B33F46) * sx(0x40, ref_1116484)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_1133901 = ref_1007350 # MOV operation
    ref_1138245 = ref_1133901 # MOV operation
    ref_1138253 = ((((0x0) << 64 | ref_1138245) / 0x3) & 0xFFFFFFFFFFFFFFFF) # DIV operation
    ref_1140422 = ref_1138253 # MOV operation
    ref_1140434 = ref_1116490 # MOV operation
    ref_1140436 = ((ref_1140422 - ref_1140434) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_1140444 = ref_1140436 # MOV operation
    ref_1142620 = ref_1140444 # MOV operation
    ref_1182004 = ref_1142620 # MOV operation
    ref_1184152 = ref_1182004 # MOV operation
    ref_1184166 = (ref_1184152 >> (0x7 & 0x3F)) # SHR operation
    ref_1186339 = ref_1184166 # MOV operation
    ref_1186353 = (ref_1186339 >> (0x2 & 0x3F)) # SHR operation
    ref_1188526 = ref_1186353 # MOV operation
    ref_1188540 = (0x7 & ref_1188526) # AND operation
    ref_1192909 = ref_1188540 # MOV operation
    ref_1192915 = (0x1 | ref_1192909) # OR operation
    ref_1212517 = ref_1007350 # MOV operation
    ref_1214665 = ref_1212517 # MOV operation
    ref_1214679 = ((0x9919884 + ref_1214665) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_1216853 = ref_1214679 # MOV operation
    ref_1216865 = ref_1192915 # MOV operation
    ref_1216867 = (ref_1216853 >> ((ref_1216865 & 0xFF) & 0x3F)) # SHR operation
    ref_1219048 = ref_1216867 # MOV operation
    ref_1253971 = ref_1007350 # MOV operation
    ref_1256119 = ref_1253971 # MOV operation
    ref_1256133 = ((0x1E5EA08F8 + ref_1256119) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_1258315 = ref_1256133 # MOV operation
    ref_1323840 = ref_1219048 # MOV operation
    ref_1352226 = ref_1219048 # MOV operation
    ref_1354374 = ref_1352226 # MOV operation
    ref_1354388 = (0x3F & ref_1354374) # AND operation
    ref_1356561 = ref_1354388 # MOV operation
    ref_1356575 = ((ref_1356561 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_1358756 = ref_1323840 # MOV operation
    ref_1358760 = ref_1356575 # MOV operation
    ref_1358762 = (ref_1358760 | ref_1358756) # OR operation
    ref_1360943 = ref_1358762 # MOV operation
    ref_1424237 = ref_1360943 # MOV operation
    ref_1450463 = ref_1142620 # MOV operation
    ref_1452611 = ref_1450463 # MOV operation
    ref_1452625 = (ref_1452611 >> (0x2 & 0x3F)) # SHR operation
    ref_1454798 = ref_1452625 # MOV operation
    ref_1454812 = (0xF & ref_1454798) # AND operation
    ref_1459181 = ref_1454812 # MOV operation
    ref_1459187 = (0x1 | ref_1459181) # OR operation
    ref_1476686 = ref_1079320 # MOV operation
    ref_1478834 = ref_1476686 # MOV operation
    ref_1478846 = ref_1459187 # MOV operation
    ref_1478848 = ((ref_1478834 << ((ref_1478846 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_1500723 = ref_1142620 # MOV operation
    ref_1502871 = ref_1500723 # MOV operation
    ref_1502885 = (ref_1502871 >> (0x2 & 0x3F)) # SHR operation
    ref_1505058 = ref_1502885 # MOV operation
    ref_1505072 = (0xF & ref_1505058) # AND operation
    ref_1509441 = ref_1505072 # MOV operation
    ref_1509447 = (0x1 | ref_1509441) # OR operation
    ref_1513820 = ref_1509447 # MOV operation
    ref_1513822 = ((0x40 - ref_1513820) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_1513830 = ref_1513822 # MOV operation
    ref_1531324 = ref_1079320 # MOV operation
    ref_1533472 = ref_1531324 # MOV operation
    ref_1533484 = ref_1513830 # MOV operation
    ref_1533486 = (ref_1533472 >> ((ref_1533484 & 0xFF) & 0x3F)) # SHR operation
    ref_1535667 = ref_1478848 # MOV operation
    ref_1535671 = ref_1533486 # MOV operation
    ref_1535673 = (ref_1535671 | ref_1535667) # OR operation
    ref_1537846 = ref_1535673 # MOV operation
    ref_1537860 = (0x7 & ref_1537846) # AND operation
    ref_1540033 = ref_1537860 # MOV operation
    ref_1540047 = ((ref_1540033 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_1542228 = ref_1424237 # MOV operation
    ref_1542232 = ref_1540047 # MOV operation
    ref_1542234 = (ref_1542232 | ref_1542228) # OR operation
    ref_1544415 = ref_1542234 # MOV operation
    ref_1544417 = ((ref_1544415 >> 56) & 0xFF) # Byte reference - MOV operation
    ref_1544418 = ((ref_1544415 >> 48) & 0xFF) # Byte reference - MOV operation
    ref_1544419 = ((ref_1544415 >> 40) & 0xFF) # Byte reference - MOV operation
    ref_1544420 = ((ref_1544415 >> 32) & 0xFF) # Byte reference - MOV operation
    ref_1544421 = ((ref_1544415 >> 24) & 0xFF) # Byte reference - MOV operation
    ref_1544422 = ((ref_1544415 >> 16) & 0xFF) # Byte reference - MOV operation
    ref_1544423 = ((ref_1544415 >> 8) & 0xFF) # Byte reference - MOV operation
    ref_1544424 = (ref_1544415 & 0xFF) # Byte reference - MOV operation
    ref_1802314 = ref_1258315 # MOV operation
    ref_1804462 = ref_1802314 # MOV operation
    ref_1804476 = (ref_1804462 >> (0x3 & 0x3F)) # SHR operation
    ref_1806649 = ref_1804476 # MOV operation
    ref_1806663 = (0xF & ref_1806649) # AND operation
    ref_1811032 = ref_1806663 # MOV operation
    ref_1811038 = (0x1 | ref_1811032) # OR operation
    ref_1828537 = ref_1258315 # MOV operation
    ref_1830685 = ref_1828537 # MOV operation
    ref_1830697 = ref_1811038 # MOV operation
    ref_1830699 = ((ref_1830685 << ((ref_1830697 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_1852574 = ref_1258315 # MOV operation
    ref_1854722 = ref_1852574 # MOV operation
    ref_1854736 = (ref_1854722 >> (0x3 & 0x3F)) # SHR operation
    ref_1856909 = ref_1854736 # MOV operation
    ref_1856923 = (0xF & ref_1856909) # AND operation
    ref_1861292 = ref_1856923 # MOV operation
    ref_1861298 = (0x1 | ref_1861292) # OR operation
    ref_1865671 = ref_1861298 # MOV operation
    ref_1865673 = ((0x40 - ref_1865671) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_1865681 = ref_1865673 # MOV operation
    ref_1883175 = ref_1258315 # MOV operation
    ref_1885323 = ref_1883175 # MOV operation
    ref_1885335 = ref_1865681 # MOV operation
    ref_1885337 = (ref_1885323 >> ((ref_1885335 & 0xFF) & 0x3F)) # SHR operation
    ref_1887518 = ref_1830699 # MOV operation
    ref_1887522 = ref_1885337 # MOV operation
    ref_1887524 = (ref_1887522 | ref_1887518) # OR operation
    ref_1889705 = ref_1887524 # MOV operation
    ref_1920237 = ref_1544423 # MOVZX operation
    ref_1924585 = (ref_1920237 & 0xFF) # MOVZX operation
    ref_1955109 = ref_1544421 # MOVZX operation
    ref_1985621 = (ref_1955109 & 0xFF) # MOVZX operation
    ref_1985623 = (ref_1985621 & 0xFF) # Byte reference - MOV operation
    ref_1989981 = (ref_1924585 & 0xFF) # MOVZX operation
    ref_2020493 = (ref_1989981 & 0xFF) # MOVZX operation
    ref_2020495 = (ref_2020493 & 0xFF) # Byte reference - MOV operation
    ref_2055385 = ref_1889705 # MOV operation
    ref_2072859 = ref_1142620 # MOV operation
    ref_2075015 = ref_2055385 # MOV operation
    ref_2075019 = ref_2072859 # MOV operation
    ref_2075021 = (ref_2075019 | ref_2075015) # OR operation
    ref_2092520 = ((((((((ref_1544417) << 8 | ref_1544418) << 8 | ref_1544419) << 8 | ref_1544420) << 8 | ref_2020495) << 8 | ref_1544422) << 8 | ref_1985623) << 8 | ref_1544424) # MOV operation
    ref_2109994 = ref_1258315 # MOV operation
    ref_2112150 = ref_2092520 # MOV operation
    ref_2112154 = ref_2109994 # MOV operation
    ref_2112156 = (((sx(0x40, ref_2112154) * sx(0x40, ref_2112150)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_2114334 = ref_2075021 # MOV operation
    ref_2114338 = ref_2112156 # MOV operation
    ref_2114340 = (((sx(0x40, ref_2114338) * sx(0x40, ref_2114334)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_2116518 = ref_2114340 # MOV operation
    ref_2120873 = ref_2116518 # MOV operation
    ref_2120875 = ref_2120873 # MOV operation
    endb = ref_2120875


print(endb & 0xffffffffffffffff)
