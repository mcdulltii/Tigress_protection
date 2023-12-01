#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_9054 = ref_278 # MOV operation
ref_9513 = ref_9054 # MOV operation
ref_9531 = (ref_9513 >> (0x7 & 0x3F)) # SHR operation
ref_9538 = ref_9531 # MOV operation
ref_14252 = ref_278 # MOV operation
ref_14729 = ref_14252 # MOV operation
ref_14747 = ((ref_14729 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_14754 = ref_14747 # MOV operation
ref_15289 = ref_9538 # MOV operation
ref_15295 = ref_14754 # MOV operation
ref_15297 = (ref_15295 | ref_15289) # OR operation
ref_19341 = ref_15297 # MOV operation
ref_23862 = ref_278 # MOV operation
ref_24371 = ref_23862 # MOV operation
ref_24389 = (ref_24371 >> (0xB & 0x3F)) # SHR operation
ref_24396 = ref_24389 # MOV operation
ref_28982 = ref_278 # MOV operation
ref_29423 = ref_28982 # MOV operation
ref_29441 = ((ref_29423 << (0x35 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_29448 = ref_29441 # MOV operation
ref_29961 = ref_24396 # MOV operation
ref_29967 = ref_29448 # MOV operation
ref_29969 = (ref_29967 | ref_29961) # OR operation
ref_34608 = ref_19341 # MOV operation
ref_35099 = ref_34608 # MOV operation
ref_35101 = ((ref_35099 + 0x2D4AF89B) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_36158 = ref_35101 # MOV operation
ref_36160 = (ref_36158 & 0x1D5ABF66) # AND operation
ref_36724 = ref_29969 # MOV operation
ref_36730 = ref_36160 # MOV operation
ref_36732 = ((ref_36724 - ref_36730) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_36740 = ref_36732 # MOV operation
ref_40837 = ref_36740 # MOV operation
ref_44790 = ref_278 # MOV operation
ref_45773 = ref_44790 # MOV operation
ref_45781 = ((ref_45773 - 0xE8D4346) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_45789 = ref_45781 # MOV operation
ref_50035 = ref_45789 # MOV operation
ref_54054 = ref_278 # MOV operation
ref_58129 = ref_19341 # MOV operation
ref_59121 = ref_58129 # MOV operation
ref_59129 = ((0x20453EE3 + ref_59121) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_59672 = ref_54054 # MOV operation
ref_59678 = ref_59129 # MOV operation
ref_59680 = ((ref_59672 - ref_59678) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_59688 = ref_59680 # MOV operation
ref_63772 = ref_59688 # MOV operation
ref_73011 = ref_19341 # MOV operation
ref_79736 = ref_50035 # MOV operation
ref_84229 = ref_19341 # MOV operation
ref_84737 = ref_79736 # MOV operation
ref_84743 = ref_84229 # MOV operation
ref_84745 = (ref_84743 | ref_84737) # OR operation
ref_85277 = ref_84745 # MOV operation
ref_85293 = (0x3F & ref_85277) # AND operation
ref_85753 = ref_85293 # MOV operation
ref_85771 = ((ref_85753 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_85778 = ref_85771 # MOV operation
ref_86321 = ref_73011 # MOV operation
ref_86327 = ref_85778 # MOV operation
ref_86329 = (ref_86327 | ref_86321) # OR operation
ref_90951 = ref_86329 # MOV operation
ref_96590 = ref_90951 # MOV operation
ref_97067 = ref_96590 # MOV operation
ref_97085 = (ref_97067 >> (0x1 & 0x3F)) # SHR operation
ref_97092 = ref_97085 # MOV operation
ref_97515 = ref_97092 # MOV operation
ref_97531 = (0xF & ref_97515) # AND operation
ref_98597 = ref_97531 # MOV operation
ref_98605 = (0x1 | ref_98597) # OR operation
ref_102772 = ref_40837 # MOV operation
ref_103285 = ref_102772 # MOV operation
ref_103299 = ref_98605 # MOV operation
ref_103301 = (ref_103299 & 0xFFFFFFFF) # MOV operation
ref_103303 = (ref_103285 >> ((ref_103301 & 0xFF) & 0x3F)) # SHR operation
ref_103310 = ref_103303 # MOV operation
ref_109421 = ref_90951 # MOV operation
ref_109902 = ref_109421 # MOV operation
ref_109920 = (ref_109902 >> (0x1 & 0x3F)) # SHR operation
ref_109927 = ref_109920 # MOV operation
ref_110465 = ref_109927 # MOV operation
ref_110481 = (0xF & ref_110465) # AND operation
ref_111461 = ref_110481 # MOV operation
ref_111469 = (0x1 | ref_111461) # OR operation
ref_112013 = ref_111469 # MOV operation
ref_112015 = ((0x40 - ref_112013) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_112023 = ref_112015 # MOV operation
ref_116161 = ref_40837 # MOV operation
ref_116638 = ref_116161 # MOV operation
ref_116652 = ref_112023 # MOV operation
ref_116654 = (ref_116652 & 0xFFFFFFFF) # MOV operation
ref_116656 = ((ref_116638 << ((ref_116654 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_116663 = ref_116656 # MOV operation
ref_117103 = ref_103310 # MOV operation
ref_117109 = ref_116663 # MOV operation
ref_117111 = (ref_117109 | ref_117103) # OR operation
ref_122826 = ref_117111 # MOV operation
ref_128413 = ref_122826 # MOV operation
ref_132598 = ref_63772 # MOV operation
ref_133115 = ref_128413 # MOV operation
ref_133121 = ref_132598 # MOV operation
ref_133123 = ((ref_133115 - ref_133121) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_133131 = ref_133123 # MOV operation
ref_137214 = ref_133131 # MOV operation
ref_149314 = ref_137214 # MOV operation
ref_153351 = ref_63772 # MOV operation
ref_153878 = ref_149314 # MOV operation
ref_153884 = ref_153351 # MOV operation
ref_153886 = (ref_153884 | ref_153878) # OR operation
ref_154384 = ref_153886 # MOV operation
ref_154402 = (ref_154384 >> (0x1 & 0x3F)) # SHR operation
ref_154409 = ref_154402 # MOV operation
ref_154932 = ref_154409 # MOV operation
ref_154948 = (0x7 & ref_154932) # AND operation
ref_155967 = ref_154948 # MOV operation
ref_155975 = (0x1 | ref_155967) # OR operation
ref_160567 = ref_40837 # MOV operation
ref_161052 = ref_160567 # MOV operation
ref_161068 = (0xF & ref_161052) # AND operation
ref_162123 = ref_161068 # MOV operation
ref_162131 = (0x1 | ref_162123) # OR operation
ref_166198 = ref_90951 # MOV operation
ref_166605 = ref_166198 # MOV operation
ref_166619 = ref_162131 # MOV operation
ref_166621 = (ref_166619 & 0xFFFFFFFF) # MOV operation
ref_166623 = (ref_166605 >> ((ref_166621 & 0xFF) & 0x3F)) # SHR operation
ref_166630 = ref_166623 # MOV operation
ref_171929 = ref_40837 # MOV operation
ref_172372 = ref_171929 # MOV operation
ref_172388 = (0xF & ref_172372) # AND operation
ref_173375 = ref_172388 # MOV operation
ref_173383 = (0x1 | ref_173375) # OR operation
ref_173875 = ref_173383 # MOV operation
ref_173877 = ((0x40 - ref_173875) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_173885 = ref_173877 # MOV operation
ref_177929 = ref_90951 # MOV operation
ref_178444 = ref_177929 # MOV operation
ref_178458 = ref_173885 # MOV operation
ref_178460 = (ref_178458 & 0xFFFFFFFF) # MOV operation
ref_178462 = ((ref_178444 << ((ref_178460 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_178469 = ref_178462 # MOV operation
ref_178896 = ref_166630 # MOV operation
ref_178902 = ref_178469 # MOV operation
ref_178904 = (ref_178902 | ref_178896) # OR operation
ref_179434 = ref_178904 # MOV operation
ref_179448 = ref_155975 # MOV operation
ref_179450 = (ref_179448 & 0xFFFFFFFF) # MOV operation
ref_179452 = ((ref_179434 << ((ref_179450 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_179459 = ref_179452 # MOV operation
ref_183475 = ref_179459 # MOV operation
ref_184541 = ref_183475 # MOV operation
ref_184543 = ref_184541 # MOV operation

print(ref_184543 & 0xffffffffffffffff)
