#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_13198 = ref_278 # MOV operation
ref_14189 = ref_13198 # MOV operation
ref_14197 = ((ref_14189 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_14204 = ref_14197 # MOV operation
ref_18201 = ref_278 # MOV operation
ref_19447 = ref_18201 # MOV operation
ref_19455 = (ref_19447 >> (0x7 & 0x3F)) # SHR operation
ref_19462 = ref_19455 # MOV operation
ref_20081 = ref_19462 # MOV operation
ref_20093 = ref_14204 # MOV operation
ref_20095 = (ref_20093 | ref_20081) # OR operation
ref_20689 = ref_20095 # MOV operation
ref_29638 = ref_20689 # MOV operation
ref_30888 = ref_29638 # MOV operation
ref_30890 = ((ref_30888 + 0x2D4AF89B) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_31527 = ref_30890 # MOV operation
ref_31529 = (ref_31527 & 0x1D5ABF66) # AND operation
ref_35531 = ref_278 # MOV operation
ref_36522 = ref_35531 # MOV operation
ref_36530 = ((ref_36522 << (0x35 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_36537 = ref_36530 # MOV operation
ref_40534 = ref_278 # MOV operation
ref_41780 = ref_40534 # MOV operation
ref_41788 = (ref_41780 >> (0xB & 0x3F)) # SHR operation
ref_41795 = ref_41788 # MOV operation
ref_42414 = ref_41795 # MOV operation
ref_42426 = ref_36537 # MOV operation
ref_42428 = (ref_42426 | ref_42414) # OR operation
ref_42797 = ref_42428 # MOV operation
ref_42809 = ref_31529 # MOV operation
ref_42811 = ((ref_42797 - ref_42809) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_42819 = ref_42811 # MOV operation
ref_43408 = ref_42819 # MOV operation
ref_52017 = ref_278 # MOV operation
ref_52361 = ref_52017 # MOV operation
ref_52375 = ((ref_52361 - 0xE8D4346) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_52383 = ref_52375 # MOV operation
ref_52972 = ref_52383 # MOV operation
ref_61921 = ref_20689 # MOV operation
ref_62520 = ref_61921 # MOV operation
ref_62534 = ((0x20453EE3 + ref_62520) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_66537 = ref_278 # MOV operation
ref_66881 = ref_66537 # MOV operation
ref_66893 = ref_62534 # MOV operation
ref_66895 = ((ref_66881 - ref_66893) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_66903 = ref_66895 # MOV operation
ref_67492 = ref_66903 # MOV operation
ref_81148 = ref_20689 # MOV operation
ref_87099 = ref_52972 # MOV operation
ref_87698 = ref_87099 # MOV operation
ref_87710 = ref_81148 # MOV operation
ref_87712 = (ref_87710 | ref_87698) # OR operation
ref_88983 = ref_87712 # MOV operation
ref_88989 = (0x3F & ref_88983) # AND operation
ref_90005 = ref_88989 # MOV operation
ref_90013 = ((ref_90005 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_90020 = ref_90013 # MOV operation
ref_94713 = ref_20689 # MOV operation
ref_95312 = ref_94713 # MOV operation
ref_95324 = ref_90020 # MOV operation
ref_95326 = (ref_95324 | ref_95312) # OR operation
ref_95920 = ref_95326 # MOV operation
ref_105864 = ref_43408 # MOV operation
ref_111176 = ref_95920 # MOV operation
ref_112422 = ref_111176 # MOV operation
ref_112430 = (ref_112422 >> (0x1 & 0x3F)) # SHR operation
ref_112437 = ref_112430 # MOV operation
ref_113703 = ref_112437 # MOV operation
ref_113709 = (0xF & ref_113703) # AND operation
ref_114333 = ref_113709 # MOV operation
ref_114347 = (0x1 | ref_114333) # OR operation
ref_115367 = ref_114347 # MOV operation
ref_115369 = ((0x40 - ref_115367) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_115377 = ref_115369 # MOV operation
ref_115749 = ref_105864 # MOV operation
ref_115753 = ref_115377 # MOV operation
ref_115755 = (ref_115753 & 0xFFFFFFFF) # MOV operation
ref_115757 = ((ref_115749 << ((ref_115755 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_115764 = ref_115757 # MOV operation
ref_120101 = ref_43408 # MOV operation
ref_125413 = ref_95920 # MOV operation
ref_126659 = ref_125413 # MOV operation
ref_126667 = (ref_126659 >> (0x1 & 0x3F)) # SHR operation
ref_126674 = ref_126667 # MOV operation
ref_127940 = ref_126674 # MOV operation
ref_127946 = (0xF & ref_127940) # AND operation
ref_128570 = ref_127946 # MOV operation
ref_128584 = (0x1 | ref_128570) # OR operation
ref_129216 = ref_120101 # MOV operation
ref_129220 = ref_128584 # MOV operation
ref_129222 = (ref_129220 & 0xFFFFFFFF) # MOV operation
ref_129224 = (ref_129216 >> ((ref_129222 & 0xFF) & 0x3F)) # SHR operation
ref_129231 = ref_129224 # MOV operation
ref_129850 = ref_129231 # MOV operation
ref_129862 = ref_115764 # MOV operation
ref_129864 = (ref_129862 | ref_129850) # OR operation
ref_130458 = ref_129864 # MOV operation
ref_138768 = ref_67492 # MOV operation
ref_144719 = ref_130458 # MOV operation
ref_145063 = ref_144719 # MOV operation
ref_145075 = ref_138768 # MOV operation
ref_145077 = ((ref_145063 - ref_145075) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_145085 = ref_145077 # MOV operation
ref_145674 = ref_145085 # MOV operation
ref_160618 = ref_95920 # MOV operation
ref_165574 = ref_43408 # MOV operation
ref_166820 = ref_165574 # MOV operation
ref_166826 = (0xF & ref_166820) # AND operation
ref_167450 = ref_166826 # MOV operation
ref_167464 = (0x1 | ref_167450) # OR operation
ref_168484 = ref_167464 # MOV operation
ref_168486 = ((0x40 - ref_168484) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_168494 = ref_168486 # MOV operation
ref_168866 = ref_160618 # MOV operation
ref_168870 = ref_168494 # MOV operation
ref_168872 = (ref_168870 & 0xFFFFFFFF) # MOV operation
ref_168874 = ((ref_168866 << ((ref_168872 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_168881 = ref_168874 # MOV operation
ref_173218 = ref_95920 # MOV operation
ref_178174 = ref_43408 # MOV operation
ref_179420 = ref_178174 # MOV operation
ref_179426 = (0xF & ref_179420) # AND operation
ref_180050 = ref_179426 # MOV operation
ref_180064 = (0x1 | ref_180050) # OR operation
ref_180696 = ref_173218 # MOV operation
ref_180700 = ref_180064 # MOV operation
ref_180702 = (ref_180700 & 0xFFFFFFFF) # MOV operation
ref_180704 = (ref_180696 >> ((ref_180702 & 0xFF) & 0x3F)) # SHR operation
ref_180711 = ref_180704 # MOV operation
ref_181330 = ref_180711 # MOV operation
ref_181342 = ref_168881 # MOV operation
ref_181344 = (ref_181342 | ref_181330) # OR operation
ref_186325 = ref_67492 # MOV operation
ref_190642 = ref_145674 # MOV operation
ref_191241 = ref_190642 # MOV operation
ref_191253 = ref_186325 # MOV operation
ref_191255 = (ref_191253 | ref_191241) # OR operation
ref_192526 = ref_191255 # MOV operation
ref_192534 = (ref_192526 >> (0x1 & 0x3F)) # SHR operation
ref_192541 = ref_192534 # MOV operation
ref_193807 = ref_192541 # MOV operation
ref_193813 = (0x7 & ref_193807) # AND operation
ref_194437 = ref_193813 # MOV operation
ref_194451 = (0x1 | ref_194437) # OR operation
ref_194828 = ref_181344 # MOV operation
ref_194832 = ref_194451 # MOV operation
ref_194834 = (ref_194832 & 0xFFFFFFFF) # MOV operation
ref_194836 = ((ref_194828 << ((ref_194834 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_194843 = ref_194836 # MOV operation
ref_195432 = ref_194843 # MOV operation
ref_196179 = ref_195432 # MOV operation
ref_196181 = ref_196179 # MOV operation

print(ref_196181 & 0xffffffffffffffff)
