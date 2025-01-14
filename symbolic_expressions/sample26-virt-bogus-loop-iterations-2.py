#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_967158 = ref_278 # MOV operation
ref_1087450 = ref_967158 # MOV operation
ref_1087458 = (ref_1087450 >> (0x5 & 0x3F)) # SHR operation
ref_1087465 = ref_1087458 # MOV operation
ref_1147607 = ref_1087465 # MOV operation
ref_1147621 = (0x1376783EF7559EA & ref_1147607) # AND operation
ref_1207776 = ref_1147621 # MOV operation
ref_1207778 = ((ref_1207776 >> 56) & 0xFF) # Byte reference - MOV operation
ref_1207779 = ((ref_1207776 >> 48) & 0xFF) # Byte reference - MOV operation
ref_1207780 = ((ref_1207776 >> 40) & 0xFF) # Byte reference - MOV operation
ref_1207781 = ((ref_1207776 >> 32) & 0xFF) # Byte reference - MOV operation
ref_1207782 = ((ref_1207776 >> 24) & 0xFF) # Byte reference - MOV operation
ref_1207783 = ((ref_1207776 >> 16) & 0xFF) # Byte reference - MOV operation
ref_1207784 = ((ref_1207776 >> 8) & 0xFF) # Byte reference - MOV operation
ref_1207785 = (ref_1207776 & 0xFF) # Byte reference - MOV operation
ref_2110121 = ref_278 # MOV operation
ref_2230413 = ref_2110121 # MOV operation
ref_2230419 = (0x1A5612E2 | ref_2230413) # OR operation
ref_2771872 = ref_1207776 # MOV operation
ref_2831994 = ref_2771872 # MOV operation
ref_2832008 = (0x7063FB7 & ref_2831994) # AND operation
ref_2892163 = ref_2230419 # MOV operation
ref_2892167 = ref_2832008 # MOV operation
ref_2892169 = ((ref_2892167 + ref_2892163) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_2952325 = ref_2892169 # MOV operation
ref_2952327 = ((ref_2952325 >> 56) & 0xFF) # Byte reference - MOV operation
ref_2952328 = ((ref_2952325 >> 48) & 0xFF) # Byte reference - MOV operation
ref_2952329 = ((ref_2952325 >> 40) & 0xFF) # Byte reference - MOV operation
ref_2952330 = ((ref_2952325 >> 32) & 0xFF) # Byte reference - MOV operation
ref_2952331 = ((ref_2952325 >> 24) & 0xFF) # Byte reference - MOV operation
ref_2952332 = ((ref_2952325 >> 16) & 0xFF) # Byte reference - MOV operation
ref_2952333 = ((ref_2952325 >> 8) & 0xFF) # Byte reference - MOV operation
ref_2952334 = (ref_2952325 & 0xFF) # Byte reference - MOV operation
ref_3975079 = ref_2952325 # MOV operation
ref_4095371 = ref_3975079 # MOV operation
ref_4095379 = (ref_4095371 >> (0x3 & 0x3F)) # SHR operation
ref_4095386 = ref_4095379 # MOV operation
ref_4155528 = ref_4095386 # MOV operation
ref_4155542 = (0xF & ref_4155528) # AND operation
ref_4275859 = ref_4155542 # MOV operation
ref_4275865 = (0x1 | ref_4275859) # OR operation
ref_4396186 = ref_4275865 # MOV operation
ref_4396188 = ((0x3162E74F << ((ref_4396186 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_4997803 = ref_2952325 # MOV operation
ref_5118095 = ref_4997803 # MOV operation
ref_5118103 = (ref_5118095 >> (0x3 & 0x3F)) # SHR operation
ref_5118110 = ref_5118103 # MOV operation
ref_5178252 = ref_5118110 # MOV operation
ref_5178266 = (0xF & ref_5178252) # AND operation
ref_5298583 = ref_5178266 # MOV operation
ref_5298589 = (0x1 | ref_5298583) # OR operation
ref_5418910 = ref_5298589 # MOV operation
ref_5418912 = ((0x40 - ref_5418910) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_5418920 = ref_5418912 # MOV operation
ref_5479074 = ref_5418920 # MOV operation
ref_5479076 = (ref_5479074 & 0xFFFFFFFF) # MOV operation
ref_5479078 = (0x3162E74F >> ((ref_5479076 & 0xFF) & 0x3F)) # SHR operation
ref_5479085 = ref_5479078 # MOV operation
ref_5539235 = ref_4396188 # MOV operation
ref_5539239 = ref_5479085 # MOV operation
ref_5539241 = (ref_5539239 | ref_5539235) # OR operation
ref_5659558 = ref_5539241 # MOV operation
ref_5659566 = (ref_5659558 >> (0x4 & 0x3F)) # SHR operation
ref_5659573 = ref_5659566 # MOV operation
ref_5719715 = ref_5659573 # MOV operation
ref_5719729 = (0x7 & ref_5719715) # AND operation
ref_5840046 = ref_5719729 # MOV operation
ref_5840052 = (0x1 | ref_5840046) # OR operation
ref_6381420 = ref_278 # MOV operation
ref_6441542 = ref_6381420 # MOV operation
ref_6441556 = ((ref_6441542 - 0x2907943) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_6441564 = ref_6441556 # MOV operation
ref_6501706 = ref_6441564 # MOV operation
ref_6501718 = ref_5840052 # MOV operation
ref_6501720 = ((ref_6501706 << ((ref_6501718 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_6561875 = ref_6501720 # MOV operation
ref_7524382 = ref_278 # MOV operation
ref_7584504 = ref_7524382 # MOV operation
ref_7584518 = ((ref_7584504 - 0x3C563FC) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_7584526 = ref_7584518 # MOV operation
ref_7644676 = ref_7584526 # MOV operation
ref_9088505 = ref_7644676 # MOV operation
ref_9870553 = ref_2952325 # MOV operation
ref_9930675 = ref_9870553 # MOV operation
ref_9930689 = (0xF & ref_9930675) # AND operation
ref_9990836 = ref_9930689 # MOV operation
ref_9990850 = ((ref_9990836 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_10051005 = ref_9088505 # MOV operation
ref_10051009 = ref_9990850 # MOV operation
ref_10051011 = (ref_10051009 | ref_10051005) # OR operation
ref_10111166 = ref_10051011 # MOV operation
ref_11013596 = ref_6561875 # MOV operation
ref_11615186 = ref_10111166 # MOV operation
ref_11675308 = ref_11615186 # MOV operation
ref_11675322 = (0x1F & ref_11675308) # AND operation
ref_11735469 = ref_11675322 # MOV operation
ref_11735483 = ((ref_11735469 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_11795638 = ref_11013596 # MOV operation
ref_11795642 = ref_11735483 # MOV operation
ref_11795644 = (ref_11795642 | ref_11795638) # OR operation
ref_11855799 = ref_11795644 # MOV operation
ref_12758229 = ref_10111166 # MOV operation
ref_13540277 = ref_2952325 # MOV operation
ref_13600399 = ref_13540277 # MOV operation
ref_13600413 = (0xF & ref_13600399) # AND operation
ref_13660560 = ref_13600413 # MOV operation
ref_13660574 = ((ref_13660560 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_13720729 = ref_12758229 # MOV operation
ref_13720733 = ref_13660574 # MOV operation
ref_13720735 = (ref_13720733 | ref_13720729) # OR operation
ref_13780890 = ref_13720735 # MOV operation
ref_15405177 = ref_13780890 # MOV operation
ref_16187225 = ref_13780890 # MOV operation
ref_16247347 = ref_16187225 # MOV operation
ref_16247361 = (0xF & ref_16247347) # AND operation
ref_16307508 = ref_16247361 # MOV operation
ref_16307522 = ((ref_16307508 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_16367677 = ref_15405177 # MOV operation
ref_16367681 = ref_16307522 # MOV operation
ref_16367683 = (ref_16367681 | ref_16367677) # OR operation
ref_16427838 = ref_16367683 # MOV operation
ref_17330268 = ref_11855799 # MOV operation
ref_17931858 = ref_16427838 # MOV operation
ref_17991980 = ref_17931858 # MOV operation
ref_17991994 = (0x1F & ref_17991980) # AND operation
ref_18052141 = ref_17991994 # MOV operation
ref_18052155 = ((ref_18052141 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_18112310 = ref_17330268 # MOV operation
ref_18112314 = ref_18052155 # MOV operation
ref_18112316 = (ref_18112314 | ref_18112310) # OR operation
ref_18172471 = ref_18112316 # MOV operation
ref_18172473 = ((ref_18172471 >> 56) & 0xFF) # Byte reference - MOV operation
ref_18172474 = ((ref_18172471 >> 48) & 0xFF) # Byte reference - MOV operation
ref_18172475 = ((ref_18172471 >> 40) & 0xFF) # Byte reference - MOV operation
ref_18172476 = ((ref_18172471 >> 32) & 0xFF) # Byte reference - MOV operation
ref_18172477 = ((ref_18172471 >> 24) & 0xFF) # Byte reference - MOV operation
ref_18172478 = ((ref_18172471 >> 16) & 0xFF) # Byte reference - MOV operation
ref_18172479 = ((ref_18172471 >> 8) & 0xFF) # Byte reference - MOV operation
ref_18172480 = (ref_18172471 & 0xFF) # Byte reference - MOV operation
ref_19074901 = ref_16427838 # MOV operation
ref_19856949 = ref_16427838 # MOV operation
ref_19917071 = ref_19856949 # MOV operation
ref_19917085 = (0xF & ref_19917071) # AND operation
ref_19977232 = ref_19917085 # MOV operation
ref_19977246 = ((ref_19977232 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_20037401 = ref_19074901 # MOV operation
ref_20037405 = ref_19977246 # MOV operation
ref_20037407 = (ref_20037405 | ref_20037401) # OR operation
ref_20097562 = ref_20037407 # MOV operation
ref_24368790 = ref_20097562 # MOV operation
ref_24970380 = ref_18172471 # MOV operation
ref_25451646 = ref_18172471 # MOV operation
ref_25511776 = ref_24970380 # MOV operation
ref_25511780 = ref_25451646 # MOV operation
ref_25511782 = ((ref_25511780 + ref_25511776) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_25571930 = ref_25511782 # MOV operation
ref_25571944 = (0x7 & ref_25571930) # AND operation
ref_25632091 = ref_25571944 # MOV operation
ref_25632105 = ((ref_25632091 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_25692260 = ref_24368790 # MOV operation
ref_25692264 = ref_25632105 # MOV operation
ref_25692266 = (ref_25692264 | ref_25692260) # OR operation
ref_25752421 = ref_25692266 # MOV operation
ref_26594589 = ((((ref_18172473) << 8 | ref_18172474) << 8 | ref_18172475) << 8 | ref_18172476) # MOV operation
ref_26714889 = (ref_26594589 & 0xFFFFFFFF) # MOV operation
ref_27557053 = ((((ref_18172477) << 8 | ref_18172478) << 8 | ref_18172479) << 8 | ref_18172480) # MOV operation
ref_28399205 = (ref_27557053 & 0xFFFFFFFF) # MOV operation
ref_28399207 = (((ref_28399205 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_28399208 = (((ref_28399205 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_28399209 = (((ref_28399205 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_28399210 = ((ref_28399205 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_28519517 = (ref_26714889 & 0xFFFFFFFF) # MOV operation
ref_29361669 = (ref_28519517 & 0xFFFFFFFF) # MOV operation
ref_29361671 = (((ref_29361669 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_29361672 = (((ref_29361669 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_29361673 = (((ref_29361669 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_29361674 = ((ref_29361669 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_30264007 = ref_1207780 # MOVZX operation
ref_30324129 = (ref_30264007 & 0xFF) # MOVZX operation
ref_31948315 = ref_1207781 # MOVZX operation
ref_32008437 = (ref_31948315 & 0xFF) # MOVZX operation
ref_32008439 = (ref_32008437 & 0xFF) # Byte reference - MOV operation
ref_32910771 = (ref_30324129 & 0xFF) # MOVZX operation
ref_32970893 = (ref_32910771 & 0xFF) # MOVZX operation
ref_32970895 = (ref_32970893 & 0xFF) # Byte reference - MOV operation
ref_33873227 = ref_1207779 # MOVZX operation
ref_33933349 = (ref_33873227 & 0xFF) # MOVZX operation
ref_35557535 = ref_1207785 # MOVZX operation
ref_35617657 = (ref_35557535 & 0xFF) # MOVZX operation
ref_35617659 = (ref_35617657 & 0xFF) # Byte reference - MOV operation
ref_36519991 = (ref_33933349 & 0xFF) # MOVZX operation
ref_36580113 = (ref_36519991 & 0xFF) # MOVZX operation
ref_36580115 = (ref_36580113 & 0xFF) # Byte reference - MOV operation
ref_37422273 = ((((ref_2952331) << 8 | ref_2952332) << 8 | ref_2952333) << 8 | ref_2952334) # MOV operation
ref_37542573 = (ref_37422273 & 0xFFFFFFFF) # MOV operation
ref_38384737 = ((((ref_2952327) << 8 | ref_2952328) << 8 | ref_2952329) << 8 | ref_2952330) # MOV operation
ref_39226889 = (ref_38384737 & 0xFFFFFFFF) # MOV operation
ref_39226891 = (((ref_39226889 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_39226892 = (((ref_39226889 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_39226893 = (((ref_39226889 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_39226894 = ((ref_39226889 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_39347201 = (ref_37542573 & 0xFFFFFFFF) # MOV operation
ref_40189353 = (ref_39347201 & 0xFFFFFFFF) # MOV operation
ref_40189355 = (((ref_40189353 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_40189356 = (((ref_40189353 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_40189357 = (((ref_40189353 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_40189358 = ((ref_40189353 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_41813576 = ((((((((ref_40189355) << 8 | ref_40189356) << 8 | ref_40189357) << 8 | ref_40189358) << 8 | ref_39226891) << 8 | ref_39226892) << 8 | ref_39226893) << 8 | ref_39226894) # MOV operation
ref_42595624 = ((((((((ref_1207778) << 8 | ref_35617659) << 8 | ref_32008439) << 8 | ref_32970895) << 8 | ref_1207782) << 8 | ref_1207783) << 8 | ref_1207784) << 8 | ref_36580115) # MOV operation
ref_42655746 = ref_42595624 # MOV operation
ref_42655760 = (0x3F & ref_42655746) # AND operation
ref_42715907 = ref_42655760 # MOV operation
ref_42715921 = ((ref_42715907 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_42776076 = ref_41813576 # MOV operation
ref_42776080 = ref_42715921 # MOV operation
ref_42776082 = (ref_42776080 | ref_42776076) # OR operation
ref_42836237 = ref_42776082 # MOV operation
ref_44580777 = ((((((((ref_28399207) << 8 | ref_28399208) << 8 | ref_28399209) << 8 | ref_28399210) << 8 | ref_29361671) << 8 | ref_29361672) << 8 | ref_29361673) << 8 | ref_29361674) # MOV operation
ref_45182367 = ref_25752421 # MOV operation
ref_45723795 = ref_42836237 # MOV operation
ref_45844087 = ref_45723795 # MOV operation
ref_45844095 = (ref_45844087 >> (0x3 & 0x3F)) # SHR operation
ref_45844102 = ref_45844095 # MOV operation
ref_45904244 = ref_45844102 # MOV operation
ref_45904258 = (0xF & ref_45904244) # AND operation
ref_46024575 = ref_45904258 # MOV operation
ref_46024581 = (0x1 | ref_46024575) # OR operation
ref_46084736 = ref_45182367 # MOV operation
ref_46084740 = ref_46024581 # MOV operation
ref_46084742 = (ref_46084740 & 0xFFFFFFFF) # MOV operation
ref_46084744 = (ref_46084736 >> ((ref_46084742 & 0xFF) & 0x3F)) # SHR operation
ref_46084751 = ref_46084744 # MOV operation
ref_46626199 = ref_42836237 # MOV operation
ref_46746491 = ref_46626199 # MOV operation
ref_46746499 = (ref_46746491 >> (0x3 & 0x3F)) # SHR operation
ref_46746506 = ref_46746499 # MOV operation
ref_46806648 = ref_46746506 # MOV operation
ref_46806662 = (0xF & ref_46806648) # AND operation
ref_46926979 = ref_46806662 # MOV operation
ref_46926985 = (0x1 | ref_46926979) # OR operation
ref_47047306 = ref_46926985 # MOV operation
ref_47047308 = ((0x40 - ref_47047306) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_47047316 = ref_47047308 # MOV operation
ref_47528602 = ref_25752421 # MOV operation
ref_47588724 = ref_47528602 # MOV operation
ref_47588736 = ref_47047316 # MOV operation
ref_47588738 = ((ref_47588724 << ((ref_47588736 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_47648893 = ref_46084751 # MOV operation
ref_47648897 = ref_47588738 # MOV operation
ref_47648899 = (ref_47648897 | ref_47648893) # OR operation
ref_47709046 = ref_47648899 # MOV operation
ref_47709060 = (0xF & ref_47709046) # AND operation
ref_47769207 = ref_47709060 # MOV operation
ref_47769221 = ((ref_47769207 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_47829376 = ref_44580777 # MOV operation
ref_47829380 = ref_47769221 # MOV operation
ref_47829382 = (ref_47829380 | ref_47829376) # OR operation
ref_47889537 = ref_47829382 # MOV operation
ref_48852053 = ref_42836237 # MOV operation
ref_48972345 = ref_48852053 # MOV operation
ref_48972353 = (ref_48972345 >> (0x3 & 0x3F)) # SHR operation
ref_48972360 = ref_48972353 # MOV operation
ref_49032502 = ref_48972360 # MOV operation
ref_49032516 = (0x7 & ref_49032502) # AND operation
ref_49152833 = ref_49032516 # MOV operation
ref_49152839 = (0x1 | ref_49152833) # OR operation
ref_49634130 = ((((((((ref_1207778) << 8 | ref_35617659) << 8 | ref_32008439) << 8 | ref_32970895) << 8 | ref_1207782) << 8 | ref_1207783) << 8 | ref_1207784) << 8 | ref_36580115) # MOV operation
ref_49694252 = ref_49634130 # MOV operation
ref_49694264 = ref_49152839 # MOV operation
ref_49694266 = ((ref_49694252 << ((ref_49694264 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_50175557 = ref_47889537 # MOV operation
ref_50656823 = ref_25752421 # MOV operation
ref_50716953 = ref_50175557 # MOV operation
ref_50716957 = ref_50656823 # MOV operation
ref_50716959 = (ref_50716957 | ref_50716953) # OR operation
ref_50777114 = ref_49694266 # MOV operation
ref_50777118 = ref_50716959 # MOV operation
ref_50777120 = (ref_50777118 | ref_50777114) # OR operation
ref_50837275 = ref_50777120 # MOV operation
ref_50957578 = ref_50837275 # MOV operation
ref_50957580 = ref_50957578 # MOV operation

print(ref_50957580 & 0xffffffffffffffff)
