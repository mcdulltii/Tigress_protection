#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_17155 = ref_278 # MOV operation
ref_18689 = ref_17155 # MOV operation
ref_18697 = (ref_18689 >> (0x5 & 0x3F)) # SHR operation
ref_18704 = ref_18697 # MOV operation
ref_19359 = ref_18704 # MOV operation
ref_19373 = (0x1376783EF7559EA & ref_19359) # AND operation
ref_20187 = ref_19373 # MOV operation
ref_20189 = ((ref_20187 >> 56) & 0xFF) # Byte reference - MOV operation
ref_20190 = ((ref_20187 >> 48) & 0xFF) # Byte reference - MOV operation
ref_20191 = ((ref_20187 >> 40) & 0xFF) # Byte reference - MOV operation
ref_20192 = ((ref_20187 >> 32) & 0xFF) # Byte reference - MOV operation
ref_20193 = ((ref_20187 >> 24) & 0xFF) # Byte reference - MOV operation
ref_20194 = ((ref_20187 >> 16) & 0xFF) # Byte reference - MOV operation
ref_20195 = ((ref_20187 >> 8) & 0xFF) # Byte reference - MOV operation
ref_20196 = (ref_20187 & 0xFF) # Byte reference - MOV operation
ref_31123 = ref_278 # MOV operation
ref_32581 = ref_31123 # MOV operation
ref_32587 = (0x1A5612E2 | ref_32581) # OR operation
ref_39045 = ref_20187 # MOV operation
ref_39680 = ref_39045 # MOV operation
ref_39694 = (0x7063FB7 & ref_39680) # AND operation
ref_40108 = ref_32587 # MOV operation
ref_40112 = ref_39694 # MOV operation
ref_40114 = ((ref_40112 + ref_40108) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_40929 = ref_40114 # MOV operation
ref_40931 = ((ref_40929 >> 56) & 0xFF) # Byte reference - MOV operation
ref_40932 = ((ref_40929 >> 48) & 0xFF) # Byte reference - MOV operation
ref_40933 = ((ref_40929 >> 40) & 0xFF) # Byte reference - MOV operation
ref_40934 = ((ref_40929 >> 32) & 0xFF) # Byte reference - MOV operation
ref_40935 = ((ref_40929 >> 24) & 0xFF) # Byte reference - MOV operation
ref_40936 = ((ref_40929 >> 16) & 0xFF) # Byte reference - MOV operation
ref_40937 = ((ref_40929 >> 8) & 0xFF) # Byte reference - MOV operation
ref_40938 = (ref_40929 & 0xFF) # Byte reference - MOV operation
ref_53218 = ref_40929 # MOV operation
ref_54752 = ref_53218 # MOV operation
ref_54760 = (ref_54752 >> (0x3 & 0x3F)) # SHR operation
ref_54767 = ref_54760 # MOV operation
ref_55422 = ref_54767 # MOV operation
ref_55436 = (0xF & ref_55422) # AND operation
ref_56919 = ref_55436 # MOV operation
ref_56925 = (0x1 | ref_56919) # OR operation
ref_58088 = ref_56925 # MOV operation
ref_58090 = ((0x3162E74F << ((ref_58088 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_65331 = ref_40929 # MOV operation
ref_66865 = ref_65331 # MOV operation
ref_66873 = (ref_66865 >> (0x3 & 0x3F)) # SHR operation
ref_66880 = ref_66873 # MOV operation
ref_67535 = ref_66880 # MOV operation
ref_67549 = (0xF & ref_67535) # AND operation
ref_69032 = ref_67549 # MOV operation
ref_69038 = (0x1 | ref_69032) # OR operation
ref_70347 = ref_69038 # MOV operation
ref_70349 = ((0x40 - ref_70347) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_70357 = ref_70349 # MOV operation
ref_71132 = ref_70357 # MOV operation
ref_71134 = (ref_71132 & 0xFFFFFFFF) # MOV operation
ref_71136 = (0x3162E74F >> ((ref_71134 & 0xFF) & 0x3F)) # SHR operation
ref_71143 = ref_71136 # MOV operation
ref_71838 = ref_58090 # MOV operation
ref_71842 = ref_71143 # MOV operation
ref_71844 = (ref_71842 | ref_71838) # OR operation
ref_73403 = ref_71844 # MOV operation
ref_73411 = (ref_73403 >> (0x4 & 0x3F)) # SHR operation
ref_73418 = ref_73411 # MOV operation
ref_74073 = ref_73418 # MOV operation
ref_74087 = (0x7 & ref_74073) # AND operation
ref_75570 = ref_74087 # MOV operation
ref_75576 = (0x1 | ref_75570) # OR operation
ref_82247 = ref_278 # MOV operation
ref_82736 = ref_82247 # MOV operation
ref_82750 = ((ref_82736 - 0x2907943) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_82758 = ref_82750 # MOV operation
ref_83121 = ref_82758 # MOV operation
ref_83133 = ref_75576 # MOV operation
ref_83135 = ((ref_83121 << ((ref_83133 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_83949 = ref_83135 # MOV operation
ref_95668 = ref_278 # MOV operation
ref_96157 = ref_95668 # MOV operation
ref_96171 = ((ref_96157 - 0x3C563FC) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_96179 = ref_96171 # MOV operation
ref_96988 = ref_96179 # MOV operation
ref_114261 = ref_96988 # MOV operation
ref_123252 = ref_40929 # MOV operation
ref_123887 = ref_123252 # MOV operation
ref_123901 = (0xF & ref_123887) # AND operation
ref_124269 = ref_123901 # MOV operation
ref_124283 = ((ref_124269 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_124983 = ref_114261 # MOV operation
ref_124987 = ref_124283 # MOV operation
ref_124989 = (ref_124987 | ref_124983) # OR operation
ref_125803 = ref_124989 # MOV operation
ref_136526 = ref_83949 # MOV operation
ref_143742 = ref_125803 # MOV operation
ref_144377 = ref_143742 # MOV operation
ref_144391 = (0x1F & ref_144377) # AND operation
ref_144759 = ref_144391 # MOV operation
ref_144773 = ((ref_144759 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_145473 = ref_136526 # MOV operation
ref_145477 = ref_144773 # MOV operation
ref_145479 = (ref_145477 | ref_145473) # OR operation
ref_146293 = ref_145479 # MOV operation
ref_157016 = ref_125803 # MOV operation
ref_166007 = ref_40929 # MOV operation
ref_166642 = ref_166007 # MOV operation
ref_166656 = (0xF & ref_166642) # AND operation
ref_167024 = ref_166656 # MOV operation
ref_167038 = ((ref_167024 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_167738 = ref_157016 # MOV operation
ref_167742 = ref_167038 # MOV operation
ref_167744 = (ref_167742 | ref_167738) # OR operation
ref_168558 = ref_167744 # MOV operation
ref_187606 = ref_168558 # MOV operation
ref_196597 = ref_168558 # MOV operation
ref_197232 = ref_196597 # MOV operation
ref_197246 = (0xF & ref_197232) # AND operation
ref_197614 = ref_197246 # MOV operation
ref_197628 = ((ref_197614 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_198328 = ref_187606 # MOV operation
ref_198332 = ref_197628 # MOV operation
ref_198334 = (ref_198332 | ref_198328) # OR operation
ref_199148 = ref_198334 # MOV operation
ref_209871 = ref_146293 # MOV operation
ref_217087 = ref_199148 # MOV operation
ref_217722 = ref_217087 # MOV operation
ref_217736 = (0x1F & ref_217722) # AND operation
ref_218104 = ref_217736 # MOV operation
ref_218118 = ((ref_218104 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_218818 = ref_209871 # MOV operation
ref_218822 = ref_218118 # MOV operation
ref_218824 = (ref_218822 | ref_218818) # OR operation
ref_219638 = ref_218824 # MOV operation
ref_219640 = ((ref_219638 >> 56) & 0xFF) # Byte reference - MOV operation
ref_219641 = ((ref_219638 >> 48) & 0xFF) # Byte reference - MOV operation
ref_219642 = ((ref_219638 >> 40) & 0xFF) # Byte reference - MOV operation
ref_219643 = ((ref_219638 >> 32) & 0xFF) # Byte reference - MOV operation
ref_219644 = ((ref_219638 >> 24) & 0xFF) # Byte reference - MOV operation
ref_219645 = ((ref_219638 >> 16) & 0xFF) # Byte reference - MOV operation
ref_219646 = ((ref_219638 >> 8) & 0xFF) # Byte reference - MOV operation
ref_219647 = (ref_219638 & 0xFF) # Byte reference - MOV operation
ref_230361 = ref_199148 # MOV operation
ref_239352 = ref_199148 # MOV operation
ref_239987 = ref_239352 # MOV operation
ref_240001 = (0xF & ref_239987) # AND operation
ref_240369 = ref_240001 # MOV operation
ref_240383 = ((ref_240369 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_241083 = ref_230361 # MOV operation
ref_241087 = ref_240383 # MOV operation
ref_241089 = (ref_241087 | ref_241083) # OR operation
ref_241903 = ref_241089 # MOV operation
ref_292182 = ref_241903 # MOV operation
ref_299398 = ref_219638 # MOV operation
ref_305048 = ref_219638 # MOV operation
ref_305437 = ref_299398 # MOV operation
ref_305441 = ref_305048 # MOV operation
ref_305443 = ((ref_305441 + ref_305437) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_306104 = ref_305443 # MOV operation
ref_306118 = (0x7 & ref_306104) # AND operation
ref_306486 = ref_306118 # MOV operation
ref_306500 = ((ref_306486 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_307200 = ref_292182 # MOV operation
ref_307204 = ref_306500 # MOV operation
ref_307206 = (ref_307204 | ref_307200) # OR operation
ref_308020 = ref_307206 # MOV operation
ref_317428 = ((((ref_219640) << 8 | ref_219641) << 8 | ref_219642) << 8 | ref_219643) # MOV operation
ref_318678 = (ref_317428 & 0xFFFFFFFF) # MOV operation
ref_328082 = ((((ref_219644) << 8 | ref_219645) << 8 | ref_219646) << 8 | ref_219647) # MOV operation
ref_337258 = (ref_328082 & 0xFFFFFFFF) # MOV operation
ref_337260 = (((ref_337258 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_337261 = (((ref_337258 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_337262 = (((ref_337258 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_337263 = ((ref_337258 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_338736 = (ref_318678 & 0xFFFFFFFF) # MOV operation
ref_347912 = (ref_338736 & 0xFFFFFFFF) # MOV operation
ref_347914 = (((ref_347912 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_347915 = (((ref_347912 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_347916 = (((ref_347912 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_347917 = ((ref_347912 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_358111 = ref_20191 # MOVZX operation
ref_358854 = (ref_358111 & 0xFF) # MOVZX operation
ref_376975 = ref_20192 # MOVZX operation
ref_377718 = (ref_376975 & 0xFF) # MOVZX operation
ref_377720 = (ref_377718 & 0xFF) # Byte reference - MOV operation
ref_387913 = (ref_358854 & 0xFF) # MOVZX operation
ref_388656 = (ref_387913 & 0xFF) # MOVZX operation
ref_388658 = (ref_388656 & 0xFF) # Byte reference - MOV operation
ref_398851 = ref_20190 # MOVZX operation
ref_399594 = (ref_398851 & 0xFF) # MOVZX operation
ref_417715 = ref_20196 # MOVZX operation
ref_418458 = (ref_417715 & 0xFF) # MOVZX operation
ref_418460 = (ref_418458 & 0xFF) # Byte reference - MOV operation
ref_428653 = (ref_399594 & 0xFF) # MOVZX operation
ref_429396 = (ref_428653 & 0xFF) # MOVZX operation
ref_429398 = (ref_429396 & 0xFF) # Byte reference - MOV operation
ref_438796 = ((((ref_40935) << 8 | ref_40936) << 8 | ref_40937) << 8 | ref_40938) # MOV operation
ref_440046 = (ref_438796 & 0xFFFFFFFF) # MOV operation
ref_449450 = ((((ref_40931) << 8 | ref_40932) << 8 | ref_40933) << 8 | ref_40934) # MOV operation
ref_458626 = (ref_449450 & 0xFFFFFFFF) # MOV operation
ref_458628 = (((ref_458626 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_458629 = (((ref_458626 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_458630 = (((ref_458626 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_458631 = ((ref_458626 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_460104 = (ref_440046 & 0xFFFFFFFF) # MOV operation
ref_469280 = (ref_460104 & 0xFFFFFFFF) # MOV operation
ref_469282 = (((ref_469280 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_469283 = (((ref_469280 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_469284 = (((ref_469280 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_469285 = ((ref_469280 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_488296 = ((((((((ref_469282) << 8 | ref_469283) << 8 | ref_469284) << 8 | ref_469285) << 8 | ref_458628) << 8 | ref_458629) << 8 | ref_458630) << 8 | ref_458631) # MOV operation
ref_497287 = ((((((((ref_20189) << 8 | ref_418460) << 8 | ref_377720) << 8 | ref_388658) << 8 | ref_20193) << 8 | ref_20194) << 8 | ref_20195) << 8 | ref_429398) # MOV operation
ref_497922 = ref_497287 # MOV operation
ref_497936 = (0x3F & ref_497922) # AND operation
ref_498304 = ref_497936 # MOV operation
ref_498318 = ((ref_498304 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_499018 = ref_488296 # MOV operation
ref_499022 = ref_498318 # MOV operation
ref_499024 = (ref_499022 | ref_499018) # OR operation
ref_499838 = ref_499024 # MOV operation
ref_520089 = ((((((((ref_337260) << 8 | ref_337261) << 8 | ref_337262) << 8 | ref_337263) << 8 | ref_347914) << 8 | ref_347915) << 8 | ref_347916) << 8 | ref_347917) # MOV operation
ref_527305 = ref_308020 # MOV operation
ref_533738 = ref_499838 # MOV operation
ref_535272 = ref_533738 # MOV operation
ref_535280 = (ref_535272 >> (0x3 & 0x3F)) # SHR operation
ref_535287 = ref_535280 # MOV operation
ref_535942 = ref_535287 # MOV operation
ref_535956 = (0xF & ref_535942) # AND operation
ref_537439 = ref_535956 # MOV operation
ref_537445 = (0x1 | ref_537439) # OR operation
ref_538221 = ref_527305 # MOV operation
ref_538225 = ref_537445 # MOV operation
ref_538227 = (ref_538225 & 0xFFFFFFFF) # MOV operation
ref_538229 = (ref_538221 >> ((ref_538227 & 0xFF) & 0x3F)) # SHR operation
ref_538236 = ref_538229 # MOV operation
ref_544689 = ref_499838 # MOV operation
ref_546223 = ref_544689 # MOV operation
ref_546231 = (ref_546223 >> (0x3 & 0x3F)) # SHR operation
ref_546238 = ref_546231 # MOV operation
ref_546893 = ref_546238 # MOV operation
ref_546907 = (0xF & ref_546893) # AND operation
ref_548390 = ref_546907 # MOV operation
ref_548396 = (0x1 | ref_548390) # OR operation
ref_549705 = ref_548396 # MOV operation
ref_549707 = ((0x40 - ref_549705) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_549715 = ref_549707 # MOV operation
ref_555385 = ref_308020 # MOV operation
ref_555728 = ref_555385 # MOV operation
ref_555740 = ref_549715 # MOV operation
ref_555742 = ((ref_555728 << ((ref_555740 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_556442 = ref_538236 # MOV operation
ref_556446 = ref_555742 # MOV operation
ref_556448 = (ref_556446 | ref_556442) # OR operation
ref_557108 = ref_556448 # MOV operation
ref_557122 = (0xF & ref_557108) # AND operation
ref_557490 = ref_557122 # MOV operation
ref_557504 = ((ref_557490 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_558204 = ref_520089 # MOV operation
ref_558208 = ref_557504 # MOV operation
ref_558210 = (ref_558208 | ref_558204) # OR operation
ref_559024 = ref_558210 # MOV operation
ref_570752 = ref_499838 # MOV operation
ref_572286 = ref_570752 # MOV operation
ref_572294 = (ref_572286 >> (0x3 & 0x3F)) # SHR operation
ref_572301 = ref_572294 # MOV operation
ref_572956 = ref_572301 # MOV operation
ref_572970 = (0x7 & ref_572956) # AND operation
ref_574453 = ref_572970 # MOV operation
ref_574459 = (0x1 | ref_574453) # OR operation
ref_580134 = ((((((((ref_20189) << 8 | ref_418460) << 8 | ref_377720) << 8 | ref_388658) << 8 | ref_20193) << 8 | ref_20194) << 8 | ref_20195) << 8 | ref_429398) # MOV operation
ref_580477 = ref_580134 # MOV operation
ref_580489 = ref_574459 # MOV operation
ref_580491 = ((ref_580477 << ((ref_580489 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_586166 = ref_559024 # MOV operation
ref_591816 = ref_308020 # MOV operation
ref_592491 = ref_586166 # MOV operation
ref_592495 = ref_591816 # MOV operation
ref_592497 = (ref_592495 | ref_592491) # OR operation
ref_593197 = ref_580491 # MOV operation
ref_593201 = ref_592497 # MOV operation
ref_593203 = (ref_593201 | ref_593197) # OR operation
ref_594017 = ref_593203 # MOV operation
ref_595124 = ref_594017 # MOV operation
ref_595126 = ref_595124 # MOV operation

print(ref_595126 & 0xffffffffffffffff)
