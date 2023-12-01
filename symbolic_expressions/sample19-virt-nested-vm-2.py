#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_112431 = ref_278 # MOV operation
ref_112523 = ref_112431 # MOV operation
ref_122852 = ref_112523 # MOV operation
ref_122936 = ref_122852 # MOV operation
ref_122950 = ((ref_122936 - 0x35CEDE6D) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_122958 = ref_122950 # MOV operation
ref_123070 = ref_122958 # MOV operation
ref_224712 = ref_123070 # MOV operation
ref_224804 = ref_224712 # MOV operation
ref_316674 = ref_278 # MOV operation
ref_316766 = ref_316674 # MOV operation
ref_339464 = ref_316766 # MOV operation
ref_339548 = ref_339464 # MOV operation
ref_339564 = ((((0x0) << 64 | ref_339548) / 0x7) & 0xFFFFFFFFFFFFFFFF) # DIV operation
ref_339677 = ref_339564 # MOV operation
ref_441319 = ref_339677 # MOV operation
ref_441411 = ref_441319 # MOV operation
ref_533281 = ref_278 # MOV operation
ref_533373 = ref_533281 # MOV operation
ref_694336 = ref_441411 # MOV operation
ref_694428 = ref_694336 # MOV operation
ref_717126 = ref_694428 # MOV operation
ref_717210 = ref_717126 # MOV operation
ref_717224 = (ref_717210 >> (0x3 & 0x3F)) # SHR operation
ref_717341 = ref_717224 # MOV operation
ref_730194 = ref_717341 # MOV operation
ref_730278 = ref_730194 # MOV operation
ref_730292 = (0xF & ref_730278) # AND operation
ref_730409 = ref_730292 # MOV operation
ref_741148 = ref_730409 # MOV operation
ref_743354 = ref_741148 # MOV operation
ref_743360 = (0x1 | ref_743354) # OR operation
ref_743477 = ref_743360 # MOV operation
ref_766585 = ref_743477 # MOV operation
ref_768795 = ref_766585 # MOV operation
ref_768797 = ((0x40 - ref_768795) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_768805 = ref_768797 # MOV operation
ref_768917 = ref_768805 # MOV operation
ref_779656 = ref_768917 # MOV operation
ref_781866 = ref_779656 # MOV operation
ref_781868 = (0x7A11169 >> ((ref_781866 & 0xFF) & 0x3F)) # SHR operation
ref_781985 = ref_781868 # MOV operation
ref_920734 = ref_441411 # MOV operation
ref_920826 = ref_920734 # MOV operation
ref_943524 = ref_920826 # MOV operation
ref_943608 = ref_943524 # MOV operation
ref_943622 = (ref_943608 >> (0x3 & 0x3F)) # SHR operation
ref_943739 = ref_943622 # MOV operation
ref_956592 = ref_943739 # MOV operation
ref_956676 = ref_956592 # MOV operation
ref_956690 = (0xF & ref_956676) # AND operation
ref_956807 = ref_956690 # MOV operation
ref_967546 = ref_956807 # MOV operation
ref_969752 = ref_967546 # MOV operation
ref_969758 = (0x1 | ref_969752) # OR operation
ref_969875 = ref_969758 # MOV operation
ref_980614 = ref_969875 # MOV operation
ref_982824 = ref_980614 # MOV operation
ref_982826 = ((0x7A11169 << ((ref_982824 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_982943 = ref_982826 # MOV operation
ref_993682 = ref_982943 # MOV operation
ref_995796 = ref_781985 # MOV operation
ref_995888 = ref_993682 # MOV operation
ref_995892 = ref_995796 # MOV operation
ref_995894 = (ref_995892 | ref_995888) # OR operation
ref_996011 = ref_995894 # MOV operation
ref_1021233 = ref_996011 # MOV operation
ref_1021317 = ref_1021233 # MOV operation
ref_1021331 = (ref_1021317 >> (0x4 & 0x3F)) # SHR operation
ref_1021448 = ref_1021331 # MOV operation
ref_1034301 = ref_1021448 # MOV operation
ref_1034385 = ref_1034301 # MOV operation
ref_1034399 = (0xF & ref_1034385) # AND operation
ref_1034516 = ref_1034399 # MOV operation
ref_1045255 = ref_1034516 # MOV operation
ref_1047461 = ref_1045255 # MOV operation
ref_1047467 = (0x1 | ref_1047461) # OR operation
ref_1047584 = ref_1047467 # MOV operation
ref_1070692 = ref_1047584 # MOV operation
ref_1072902 = ref_1070692 # MOV operation
ref_1072904 = ((0x40 - ref_1072902) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_1072912 = ref_1072904 # MOV operation
ref_1073024 = ref_1072912 # MOV operation
ref_1083763 = ref_1073024 # MOV operation
ref_1085877 = ref_533373 # MOV operation
ref_1085961 = ref_1085877 # MOV operation
ref_1085973 = ref_1083763 # MOV operation
ref_1085975 = (ref_1085961 >> ((ref_1085973 & 0xFF) & 0x3F)) # SHR operation
ref_1086092 = ref_1085975 # MOV operation
ref_1177962 = ref_278 # MOV operation
ref_1178054 = ref_1177962 # MOV operation
ref_1339017 = ref_441411 # MOV operation
ref_1339109 = ref_1339017 # MOV operation
ref_1361807 = ref_1339109 # MOV operation
ref_1361891 = ref_1361807 # MOV operation
ref_1361905 = (ref_1361891 >> (0x3 & 0x3F)) # SHR operation
ref_1362022 = ref_1361905 # MOV operation
ref_1374875 = ref_1362022 # MOV operation
ref_1374959 = ref_1374875 # MOV operation
ref_1374973 = (0xF & ref_1374959) # AND operation
ref_1375090 = ref_1374973 # MOV operation
ref_1385829 = ref_1375090 # MOV operation
ref_1388035 = ref_1385829 # MOV operation
ref_1388041 = (0x1 | ref_1388035) # OR operation
ref_1388158 = ref_1388041 # MOV operation
ref_1411266 = ref_1388158 # MOV operation
ref_1413476 = ref_1411266 # MOV operation
ref_1413478 = ((0x40 - ref_1413476) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_1413486 = ref_1413478 # MOV operation
ref_1413598 = ref_1413486 # MOV operation
ref_1424337 = ref_1413598 # MOV operation
ref_1426547 = ref_1424337 # MOV operation
ref_1426549 = (0x7A11169 >> ((ref_1426547 & 0xFF) & 0x3F)) # SHR operation
ref_1426666 = ref_1426549 # MOV operation
ref_1565415 = ref_441411 # MOV operation
ref_1565507 = ref_1565415 # MOV operation
ref_1588205 = ref_1565507 # MOV operation
ref_1588289 = ref_1588205 # MOV operation
ref_1588303 = (ref_1588289 >> (0x3 & 0x3F)) # SHR operation
ref_1588420 = ref_1588303 # MOV operation
ref_1601273 = ref_1588420 # MOV operation
ref_1601357 = ref_1601273 # MOV operation
ref_1601371 = (0xF & ref_1601357) # AND operation
ref_1601488 = ref_1601371 # MOV operation
ref_1612227 = ref_1601488 # MOV operation
ref_1614433 = ref_1612227 # MOV operation
ref_1614439 = (0x1 | ref_1614433) # OR operation
ref_1614556 = ref_1614439 # MOV operation
ref_1625295 = ref_1614556 # MOV operation
ref_1627505 = ref_1625295 # MOV operation
ref_1627507 = ((0x7A11169 << ((ref_1627505 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_1627624 = ref_1627507 # MOV operation
ref_1638363 = ref_1627624 # MOV operation
ref_1640477 = ref_1426666 # MOV operation
ref_1640569 = ref_1638363 # MOV operation
ref_1640573 = ref_1640477 # MOV operation
ref_1640575 = (ref_1640573 | ref_1640569) # OR operation
ref_1640692 = ref_1640575 # MOV operation
ref_1665914 = ref_1640692 # MOV operation
ref_1665998 = ref_1665914 # MOV operation
ref_1666012 = (ref_1665998 >> (0x4 & 0x3F)) # SHR operation
ref_1666129 = ref_1666012 # MOV operation
ref_1678982 = ref_1666129 # MOV operation
ref_1679066 = ref_1678982 # MOV operation
ref_1679080 = (0xF & ref_1679066) # AND operation
ref_1679197 = ref_1679080 # MOV operation
ref_1689936 = ref_1679197 # MOV operation
ref_1692142 = ref_1689936 # MOV operation
ref_1692148 = (0x1 | ref_1692142) # OR operation
ref_1692265 = ref_1692148 # MOV operation
ref_1703004 = ref_1692265 # MOV operation
ref_1705118 = ref_1178054 # MOV operation
ref_1705202 = ref_1705118 # MOV operation
ref_1705214 = ref_1703004 # MOV operation
ref_1705216 = ((ref_1705202 << ((ref_1705214 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_1705333 = ref_1705216 # MOV operation
ref_1716072 = ref_1705333 # MOV operation
ref_1718186 = ref_1086092 # MOV operation
ref_1718278 = ref_1716072 # MOV operation
ref_1718282 = ref_1718186 # MOV operation
ref_1718284 = (ref_1718282 | ref_1718278) # OR operation
ref_1718401 = ref_1718284 # MOV operation
ref_1820043 = ref_1718401 # MOV operation
ref_1820135 = ref_1820043 # MOV operation
ref_1924374 = ref_278 # MOV operation
ref_1924466 = ref_1924374 # MOV operation
ref_1934795 = ref_1924466 # MOV operation
ref_1934879 = ref_1934795 # MOV operation
ref_1934893 = ((ref_1934879 - 0x297EE8A1) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_1934901 = ref_1934893 # MOV operation
ref_1935013 = ref_1934901 # MOV operation
ref_1960235 = ref_1935013 # MOV operation
ref_1960319 = ref_1960235 # MOV operation
ref_1960333 = (((sx(0x40, 0x1471C5DA) * sx(0x40, ref_1960319)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_1960447 = ref_1960333 # MOV operation
ref_2062089 = ref_1960447 # MOV operation
ref_2062181 = ref_2062089 # MOV operation
ref_2062183 = ((ref_2062181 >> 56) & 0xFF) # Byte reference - MOV operation
ref_2062184 = ((ref_2062181 >> 48) & 0xFF) # Byte reference - MOV operation
ref_2062185 = ((ref_2062181 >> 40) & 0xFF) # Byte reference - MOV operation
ref_2062186 = ((ref_2062181 >> 32) & 0xFF) # Byte reference - MOV operation
ref_2062187 = ((ref_2062181 >> 24) & 0xFF) # Byte reference - MOV operation
ref_2062188 = ((ref_2062181 >> 16) & 0xFF) # Byte reference - MOV operation
ref_2062189 = ((ref_2062181 >> 8) & 0xFF) # Byte reference - MOV operation
ref_2062190 = (ref_2062181 & 0xFF) # Byte reference - MOV operation
ref_2231707 = ((ref_2062185) << 8 | ref_2062186) # MOVZX operation
ref_2231793 = (ref_2231707 & 0xFFFF) # MOVZX operation
ref_2253945 = (ref_2231793 & 0xFFFF) # MOVZX operation
ref_2254031 = (ref_2253945 & 0xFFFF) # MOVZX operation
ref_2423551 = ((ref_2062187) << 8 | ref_2062188) # MOVZX operation
ref_2423637 = (ref_2423551 & 0xFFFF) # MOVZX operation
ref_2590633 = (ref_2423637 & 0xFFFF) # MOVZX operation
ref_2590719 = (ref_2590633 & 0xFFFF) # MOVZX operation
ref_2615395 = (ref_2254031 & 0xFFFF) # MOVZX operation
ref_2615481 = (ref_2615395 & 0xFFFF) # MOVZX operation
ref_2782477 = (ref_2615481 & 0xFFFF) # MOVZX operation
ref_2782563 = (ref_2782477 & 0xFFFF) # MOVZX operation
ref_2782565 = (((ref_2782563 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_2782566 = ((ref_2782563 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_3704359 = ref_1820135 # MOV operation
ref_3704451 = ref_3704359 # MOV operation
ref_3714780 = ref_3704451 # MOV operation
ref_3714864 = ref_3714780 # MOV operation
ref_3714878 = (0x1F & ref_3714864) # AND operation
ref_3714995 = ref_3714878 # MOV operation
ref_3740217 = ref_3714995 # MOV operation
ref_3740301 = ref_3740217 # MOV operation
ref_3740315 = ((ref_3740301 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_3740432 = ref_3740315 # MOV operation
ref_3842074 = ref_441411 # MOV operation
ref_3842166 = ref_3842074 # MOV operation
ref_3850381 = ref_3842166 # MOV operation
ref_3852495 = ref_3740432 # MOV operation
ref_3852587 = ref_3850381 # MOV operation
ref_3852591 = ref_3852495 # MOV operation
ref_3852593 = (ref_3852591 | ref_3852587) # OR operation
ref_3852710 = ref_3852593 # MOV operation
ref_3954352 = ref_3852710 # MOV operation
ref_3954444 = ref_3954352 # MOV operation
ref_4068455 = ref_3954444 # MOV operation
ref_4068547 = ref_4068455 # MOV operation
ref_4078876 = ref_4068547 # MOV operation
ref_4078960 = ref_4078876 # MOV operation
ref_4078974 = (0xF & ref_4078960) # AND operation
ref_4079091 = ref_4078974 # MOV operation
ref_4104313 = ref_4079091 # MOV operation
ref_4104397 = ref_4104313 # MOV operation
ref_4104411 = ((ref_4104397 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_4104528 = ref_4104411 # MOV operation
ref_4206170 = ref_3954444 # MOV operation
ref_4206262 = ref_4206170 # MOV operation
ref_4214477 = ref_4206262 # MOV operation
ref_4216591 = ref_4104528 # MOV operation
ref_4216683 = ref_4214477 # MOV operation
ref_4216687 = ref_4216591 # MOV operation
ref_4216689 = (ref_4216687 | ref_4216683) # OR operation
ref_4216806 = ref_4216689 # MOV operation
ref_4318448 = ref_4216806 # MOV operation
ref_4318540 = ref_4318448 # MOV operation
ref_4495645 = ((ref_2062183) << 8 | ref_2062184) # MOVZX operation
ref_4495731 = (ref_4495645 & 0xFFFF) # MOVZX operation
ref_4517883 = (ref_4495731 & 0xFFFF) # MOVZX operation
ref_4517969 = (ref_4517883 & 0xFFFF) # MOVZX operation
ref_4687489 = ((ref_2062189) << 8 | ref_2062190) # MOVZX operation
ref_4687575 = (ref_4687489 & 0xFFFF) # MOVZX operation
ref_4854571 = (ref_4687575 & 0xFFFF) # MOVZX operation
ref_4854657 = (ref_4854571 & 0xFFFF) # MOVZX operation
ref_4854659 = (((ref_4854657 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_4854660 = ((ref_4854657 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_4879333 = (ref_4517969 & 0xFFFF) # MOVZX operation
ref_4879419 = (ref_4879333 & 0xFFFF) # MOVZX operation
ref_5046415 = (ref_4879419 & 0xFFFF) # MOVZX operation
ref_5046501 = (ref_5046415 & 0xFFFF) # MOVZX operation
ref_5216021 = (ref_5046501 & 0xFFFF) # MOVZX operation
ref_5216107 = (ref_5216021 & 0xFFFF) # MOVZX operation
ref_5238259 = (ref_5216107 & 0xFFFF) # MOVZX operation
ref_5238345 = (ref_5238259 & 0xFFFF) # MOVZX operation
ref_5407865 = (ref_2590719 & 0xFFFF) # MOVZX operation
ref_5407951 = (ref_5407865 & 0xFFFF) # MOVZX operation
ref_5574947 = (ref_5407951 & 0xFFFF) # MOVZX operation
ref_5575033 = (ref_5574947 & 0xFFFF) # MOVZX operation
ref_5575035 = (((ref_5575033 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_5575036 = ((ref_5575033 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_5599709 = (ref_5238345 & 0xFFFF) # MOVZX operation
ref_5599795 = (ref_5599709 & 0xFFFF) # MOVZX operation
ref_5766791 = (ref_5599795 & 0xFFFF) # MOVZX operation
ref_5766877 = (ref_5766791 & 0xFFFF) # MOVZX operation
ref_5766879 = (((ref_5766877 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_5766880 = ((ref_5766877 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_5868513 = ref_224804 # MOV operation
ref_5868605 = ref_5868513 # MOV operation
ref_5992461 = ref_4318540 # MOV operation
ref_5992553 = ref_5992461 # MOV operation
ref_6002882 = ref_5992553 # MOV operation
ref_6002966 = ref_6002882 # MOV operation
ref_6002980 = (0xF & ref_6002966) # AND operation
ref_6003097 = ref_6002980 # MOV operation
ref_6013836 = ref_6003097 # MOV operation
ref_6016042 = ref_6013836 # MOV operation
ref_6016048 = (0x1 | ref_6016042) # OR operation
ref_6016165 = ref_6016048 # MOV operation
ref_6039273 = ref_6016165 # MOV operation
ref_6041483 = ref_6039273 # MOV operation
ref_6041485 = ((0x40 - ref_6041483) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_6041493 = ref_6041485 # MOV operation
ref_6041605 = ref_6041493 # MOV operation
ref_6052344 = ref_6041605 # MOV operation
ref_6054458 = ref_5868605 # MOV operation
ref_6054542 = ref_6054458 # MOV operation
ref_6054554 = ref_6052344 # MOV operation
ref_6054556 = (ref_6054542 >> ((ref_6054554 & 0xFF) & 0x3F)) # SHR operation
ref_6054673 = ref_6054556 # MOV operation
ref_6156315 = ref_224804 # MOV operation
ref_6156407 = ref_6156315 # MOV operation
ref_6280263 = ref_4318540 # MOV operation
ref_6280355 = ref_6280263 # MOV operation
ref_6290684 = ref_6280355 # MOV operation
ref_6290768 = ref_6290684 # MOV operation
ref_6290782 = (0xF & ref_6290768) # AND operation
ref_6290899 = ref_6290782 # MOV operation
ref_6301638 = ref_6290899 # MOV operation
ref_6303844 = ref_6301638 # MOV operation
ref_6303850 = (0x1 | ref_6303844) # OR operation
ref_6303967 = ref_6303850 # MOV operation
ref_6314706 = ref_6303967 # MOV operation
ref_6316820 = ref_6156407 # MOV operation
ref_6316904 = ref_6316820 # MOV operation
ref_6316916 = ref_6314706 # MOV operation
ref_6316918 = ((ref_6316904 << ((ref_6316916 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_6317035 = ref_6316918 # MOV operation
ref_6327774 = ref_6317035 # MOV operation
ref_6329888 = ref_6054673 # MOV operation
ref_6329980 = ref_6327774 # MOV operation
ref_6329984 = ref_6329888 # MOV operation
ref_6329986 = (ref_6329984 | ref_6329980) # OR operation
ref_6330103 = ref_6329986 # MOV operation
ref_6456483 = ref_1820135 # MOV operation
ref_6456575 = ref_6456483 # MOV operation
ref_6580431 = ((((((((ref_4854659) << 8 | ref_4854660) << 8 | ref_5766879) << 8 | ref_5766880) << 8 | ref_2782565) << 8 | ref_2782566) << 8 | ref_5575035) << 8 | ref_5575036) # MOV operation
ref_6580523 = ref_6580431 # MOV operation
ref_6603221 = ref_6580523 # MOV operation
ref_6603305 = ref_6603221 # MOV operation
ref_6603319 = (ref_6603305 >> (0x2 & 0x3F)) # SHR operation
ref_6603436 = ref_6603319 # MOV operation
ref_6616289 = ref_6603436 # MOV operation
ref_6616373 = ref_6616289 # MOV operation
ref_6616387 = (0xF & ref_6616373) # AND operation
ref_6616504 = ref_6616387 # MOV operation
ref_6627243 = ref_6616504 # MOV operation
ref_6629449 = ref_6627243 # MOV operation
ref_6629455 = (0x1 | ref_6629449) # OR operation
ref_6629572 = ref_6629455 # MOV operation
ref_6652680 = ref_6629572 # MOV operation
ref_6654890 = ref_6652680 # MOV operation
ref_6654892 = ((0x40 - ref_6654890) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_6654900 = ref_6654892 # MOV operation
ref_6655012 = ref_6654900 # MOV operation
ref_6665751 = ref_6655012 # MOV operation
ref_6667865 = ref_6456575 # MOV operation
ref_6667949 = ref_6667865 # MOV operation
ref_6667961 = ref_6665751 # MOV operation
ref_6667963 = (ref_6667949 >> ((ref_6667961 & 0xFF) & 0x3F)) # SHR operation
ref_6668080 = ref_6667963 # MOV operation
ref_6769722 = ref_1820135 # MOV operation
ref_6769814 = ref_6769722 # MOV operation
ref_6893670 = ((((((((ref_4854659) << 8 | ref_4854660) << 8 | ref_5766879) << 8 | ref_5766880) << 8 | ref_2782565) << 8 | ref_2782566) << 8 | ref_5575035) << 8 | ref_5575036) # MOV operation
ref_6893762 = ref_6893670 # MOV operation
ref_6916460 = ref_6893762 # MOV operation
ref_6916544 = ref_6916460 # MOV operation
ref_6916558 = (ref_6916544 >> (0x2 & 0x3F)) # SHR operation
ref_6916675 = ref_6916558 # MOV operation
ref_6929528 = ref_6916675 # MOV operation
ref_6929612 = ref_6929528 # MOV operation
ref_6929626 = (0xF & ref_6929612) # AND operation
ref_6929743 = ref_6929626 # MOV operation
ref_6940482 = ref_6929743 # MOV operation
ref_6942688 = ref_6940482 # MOV operation
ref_6942694 = (0x1 | ref_6942688) # OR operation
ref_6942811 = ref_6942694 # MOV operation
ref_6953550 = ref_6942811 # MOV operation
ref_6955664 = ref_6769814 # MOV operation
ref_6955748 = ref_6955664 # MOV operation
ref_6955760 = ref_6953550 # MOV operation
ref_6955762 = ((ref_6955748 << ((ref_6955760 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_6955879 = ref_6955762 # MOV operation
ref_6966618 = ref_6955879 # MOV operation
ref_6968732 = ref_6668080 # MOV operation
ref_6968824 = ref_6966618 # MOV operation
ref_6968828 = ref_6968732 # MOV operation
ref_6968830 = (ref_6968828 | ref_6968824) # OR operation
ref_6968947 = ref_6968830 # MOV operation
ref_6994169 = ref_6968947 # MOV operation
ref_6994253 = ref_6994169 # MOV operation
ref_6994267 = (ref_6994253 >> (0x4 & 0x3F)) # SHR operation
ref_6994384 = ref_6994267 # MOV operation
ref_7007237 = ref_6994384 # MOV operation
ref_7007321 = ref_7007237 # MOV operation
ref_7007335 = (0xF & ref_7007321) # AND operation
ref_7007452 = ref_7007335 # MOV operation
ref_7018191 = ref_7007452 # MOV operation
ref_7020397 = ref_7018191 # MOV operation
ref_7020403 = (0x1 | ref_7020397) # OR operation
ref_7020520 = ref_7020403 # MOV operation
ref_7043628 = ref_7020520 # MOV operation
ref_7045838 = ref_7043628 # MOV operation
ref_7045840 = ((0x40 - ref_7045838) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_7045848 = ref_7045840 # MOV operation
ref_7045960 = ref_7045848 # MOV operation
ref_7056699 = ref_7045960 # MOV operation
ref_7058813 = ref_6330103 # MOV operation
ref_7058897 = ref_7058813 # MOV operation
ref_7058909 = ref_7056699 # MOV operation
ref_7058911 = ((ref_7058897 << ((ref_7058909 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_7059028 = ref_7058911 # MOV operation
ref_7160670 = ref_224804 # MOV operation
ref_7160762 = ref_7160670 # MOV operation
ref_7284618 = ref_4318540 # MOV operation
ref_7284710 = ref_7284618 # MOV operation
ref_7295039 = ref_7284710 # MOV operation
ref_7295123 = ref_7295039 # MOV operation
ref_7295137 = (0xF & ref_7295123) # AND operation
ref_7295254 = ref_7295137 # MOV operation
ref_7305993 = ref_7295254 # MOV operation
ref_7308199 = ref_7305993 # MOV operation
ref_7308205 = (0x1 | ref_7308199) # OR operation
ref_7308322 = ref_7308205 # MOV operation
ref_7331430 = ref_7308322 # MOV operation
ref_7333640 = ref_7331430 # MOV operation
ref_7333642 = ((0x40 - ref_7333640) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_7333650 = ref_7333642 # MOV operation
ref_7333762 = ref_7333650 # MOV operation
ref_7344501 = ref_7333762 # MOV operation
ref_7346615 = ref_7160762 # MOV operation
ref_7346699 = ref_7346615 # MOV operation
ref_7346711 = ref_7344501 # MOV operation
ref_7346713 = (ref_7346699 >> ((ref_7346711 & 0xFF) & 0x3F)) # SHR operation
ref_7346830 = ref_7346713 # MOV operation
ref_7448472 = ref_224804 # MOV operation
ref_7448564 = ref_7448472 # MOV operation
ref_7572420 = ref_4318540 # MOV operation
ref_7572512 = ref_7572420 # MOV operation
ref_7582841 = ref_7572512 # MOV operation
ref_7582925 = ref_7582841 # MOV operation
ref_7582939 = (0xF & ref_7582925) # AND operation
ref_7583056 = ref_7582939 # MOV operation
ref_7593795 = ref_7583056 # MOV operation
ref_7596001 = ref_7593795 # MOV operation
ref_7596007 = (0x1 | ref_7596001) # OR operation
ref_7596124 = ref_7596007 # MOV operation
ref_7606863 = ref_7596124 # MOV operation
ref_7608977 = ref_7448564 # MOV operation
ref_7609061 = ref_7608977 # MOV operation
ref_7609073 = ref_7606863 # MOV operation
ref_7609075 = ((ref_7609061 << ((ref_7609073 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_7609192 = ref_7609075 # MOV operation
ref_7619931 = ref_7609192 # MOV operation
ref_7622045 = ref_7346830 # MOV operation
ref_7622137 = ref_7619931 # MOV operation
ref_7622141 = ref_7622045 # MOV operation
ref_7622143 = (ref_7622141 | ref_7622137) # OR operation
ref_7622260 = ref_7622143 # MOV operation
ref_7748640 = ref_1820135 # MOV operation
ref_7748732 = ref_7748640 # MOV operation
ref_7872588 = ((((((((ref_4854659) << 8 | ref_4854660) << 8 | ref_5766879) << 8 | ref_5766880) << 8 | ref_2782565) << 8 | ref_2782566) << 8 | ref_5575035) << 8 | ref_5575036) # MOV operation
ref_7872680 = ref_7872588 # MOV operation
ref_7895378 = ref_7872680 # MOV operation
ref_7895462 = ref_7895378 # MOV operation
ref_7895476 = (ref_7895462 >> (0x2 & 0x3F)) # SHR operation
ref_7895593 = ref_7895476 # MOV operation
ref_7908446 = ref_7895593 # MOV operation
ref_7908530 = ref_7908446 # MOV operation
ref_7908544 = (0xF & ref_7908530) # AND operation
ref_7908661 = ref_7908544 # MOV operation
ref_7919400 = ref_7908661 # MOV operation
ref_7921606 = ref_7919400 # MOV operation
ref_7921612 = (0x1 | ref_7921606) # OR operation
ref_7921729 = ref_7921612 # MOV operation
ref_7944837 = ref_7921729 # MOV operation
ref_7947047 = ref_7944837 # MOV operation
ref_7947049 = ((0x40 - ref_7947047) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_7947057 = ref_7947049 # MOV operation
ref_7947169 = ref_7947057 # MOV operation
ref_7957908 = ref_7947169 # MOV operation
ref_7960022 = ref_7748732 # MOV operation
ref_7960106 = ref_7960022 # MOV operation
ref_7960118 = ref_7957908 # MOV operation
ref_7960120 = (ref_7960106 >> ((ref_7960118 & 0xFF) & 0x3F)) # SHR operation
ref_7960237 = ref_7960120 # MOV operation
ref_8061879 = ref_1820135 # MOV operation
ref_8061971 = ref_8061879 # MOV operation
ref_8185827 = ((((((((ref_4854659) << 8 | ref_4854660) << 8 | ref_5766879) << 8 | ref_5766880) << 8 | ref_2782565) << 8 | ref_2782566) << 8 | ref_5575035) << 8 | ref_5575036) # MOV operation
ref_8185919 = ref_8185827 # MOV operation
ref_8208617 = ref_8185919 # MOV operation
ref_8208701 = ref_8208617 # MOV operation
ref_8208715 = (ref_8208701 >> (0x2 & 0x3F)) # SHR operation
ref_8208832 = ref_8208715 # MOV operation
ref_8221685 = ref_8208832 # MOV operation
ref_8221769 = ref_8221685 # MOV operation
ref_8221783 = (0xF & ref_8221769) # AND operation
ref_8221900 = ref_8221783 # MOV operation
ref_8232639 = ref_8221900 # MOV operation
ref_8234845 = ref_8232639 # MOV operation
ref_8234851 = (0x1 | ref_8234845) # OR operation
ref_8234968 = ref_8234851 # MOV operation
ref_8245707 = ref_8234968 # MOV operation
ref_8247821 = ref_8061971 # MOV operation
ref_8247905 = ref_8247821 # MOV operation
ref_8247917 = ref_8245707 # MOV operation
ref_8247919 = ((ref_8247905 << ((ref_8247917 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_8248036 = ref_8247919 # MOV operation
ref_8258775 = ref_8248036 # MOV operation
ref_8260889 = ref_7960237 # MOV operation
ref_8260981 = ref_8258775 # MOV operation
ref_8260985 = ref_8260889 # MOV operation
ref_8260987 = (ref_8260985 | ref_8260981) # OR operation
ref_8261104 = ref_8260987 # MOV operation
ref_8286326 = ref_8261104 # MOV operation
ref_8286410 = ref_8286326 # MOV operation
ref_8286424 = (ref_8286410 >> (0x4 & 0x3F)) # SHR operation
ref_8286541 = ref_8286424 # MOV operation
ref_8299394 = ref_8286541 # MOV operation
ref_8299478 = ref_8299394 # MOV operation
ref_8299492 = (0xF & ref_8299478) # AND operation
ref_8299609 = ref_8299492 # MOV operation
ref_8310348 = ref_8299609 # MOV operation
ref_8312554 = ref_8310348 # MOV operation
ref_8312560 = (0x1 | ref_8312554) # OR operation
ref_8312677 = ref_8312560 # MOV operation
ref_8323416 = ref_8312677 # MOV operation
ref_8325530 = ref_7622260 # MOV operation
ref_8325614 = ref_8325530 # MOV operation
ref_8325626 = ref_8323416 # MOV operation
ref_8325628 = (ref_8325614 >> ((ref_8325626 & 0xFF) & 0x3F)) # SHR operation
ref_8325745 = ref_8325628 # MOV operation
ref_8336484 = ref_8325745 # MOV operation
ref_8338598 = ref_7059028 # MOV operation
ref_8338690 = ref_8336484 # MOV operation
ref_8338694 = ref_8338598 # MOV operation
ref_8338696 = (ref_8338694 | ref_8338690) # OR operation
ref_8338813 = ref_8338696 # MOV operation
ref_8430692 = ref_8338813 # MOV operation
ref_8430784 = ref_8430692 # MOV operation
ref_8445257 = ref_8430784 # MOV operation
ref_8445259 = ref_8445257 # MOV operation

print(ref_8445259 & 0xffffffffffffffff)
