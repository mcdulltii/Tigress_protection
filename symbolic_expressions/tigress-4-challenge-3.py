#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_152885 = SymVar_0
ref_152900 = ref_152885 # MOV operation
ref_32614386 = ref_152900 # MOV operation
ref_32615543 = ref_32614386 # MOV operation
ref_34495133 = ref_32615543 # MOV operation
ref_34496180 = ref_34495133 # MOV operation
ref_34496194 = ref_34496180 # MOV operation
ref_34496198 = ((ref_34496194 << (0xD & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_34496205 = ref_34496198 # MOV operation
ref_34497480 = ref_34496205 # MOV operation
ref_40889346 = ref_152900 # MOV operation
ref_40890503 = ref_40889346 # MOV operation
ref_41560297 = ref_40890503 # MOV operation
ref_41562903 = ref_41560297 # MOV operation
ref_41562917 = ref_41562903 # MOV operation
ref_41562921 = (ref_41562917 >> (0x33 & 0x3F)) # SHR operation
ref_41562928 = ref_41562921 # MOV operation
ref_41564230 = ref_41562928 # MOV operation
ref_42259713 = ref_41564230 # MOV operation
ref_42313404 = ref_34497480 # MOV operation
ref_42318404 = ref_42313404 # MOV operation
ref_42318416 = ref_42259713 # MOV operation
ref_42318418 = (ref_42318416 | ref_42318404) # OR operation
ref_42319743 = ref_42318418 # MOV operation
ref_42745357 = ref_42319743 # MOV operation
ref_42746514 = ref_42745357 # MOV operation
ref_54225495 = ref_152900 # MOV operation
ref_54226652 = ref_54225495 # MOV operation
ref_54624747 = ref_54226652 # MOV operation
ref_54683832 = ref_54624747 # MOV operation
ref_54683850 = ((((0x0) << 64 | ref_54683832) / ((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x6)) & 0xFFFFFFFFFFFFFFFF) # DIV operation
ref_54685091 = ref_54683850 # MOV operation
ref_56317860 = ref_54685091 # MOV operation
ref_56372134 = ref_56317860 # MOV operation
ref_56372140 = (((sx(0x40, 0xFA0000000002C90C) * sx(0x40, ref_56372134)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_56373403 = ref_56372140 # MOV operation
ref_56799017 = ref_56373403 # MOV operation
ref_56800174 = ref_56799017 # MOV operation
ref_67232865 = ref_152900 # MOV operation
ref_67234022 = ref_67232865 # MOV operation
ref_73185140 = ref_42746514 # MOV operation
ref_73186297 = ref_73185140 # MOV operation
ref_79137415 = ref_56800174 # MOV operation
ref_79138572 = ref_79137415 # MOV operation
ref_79781926 = ref_79138572 # MOV operation
ref_79835617 = ref_73186297 # MOV operation
ref_79840617 = ref_79835617 # MOV operation
ref_79840629 = ref_79781926 # MOV operation
ref_79840631 = (ref_79840629 | ref_79840617) # OR operation
ref_79841956 = ref_79840631 # MOV operation
ref_80237678 = ref_67234022 # MOV operation
ref_80291369 = ref_79841956 # MOV operation
ref_80294913 = ref_80237678 # MOV operation
ref_80294917 = ref_80291369 # MOV operation
ref_80294919 = ((ref_80294917 + ref_80294913) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_80296200 = ref_80294919 # MOV operation
ref_80721814 = ref_80296200 # MOV operation
ref_80722971 = ref_80721814 # MOV operation
ref_93905913 = ref_42746514 # MOV operation
ref_93907070 = ref_93905913 # MOV operation
ref_94903876 = ref_93907070 # MOV operation
ref_94907759 = ref_94903876 # MOV operation
ref_94907773 = ref_94907759 # MOV operation
ref_94907775 = ((ref_94907773 - 0x2ED5CD7E) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_94907783 = ref_94907775 # MOV operation
ref_94909076 = ref_94907783 # MOV operation
ref_96950610 = ref_94909076 # MOV operation
ref_97008196 = ref_96950610 # MOV operation
ref_97008200 = ((0x28E5FC28 - ref_97008196) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_97008208 = ref_97008200 # MOV operation
ref_97009501 = ref_97008208 # MOV operation
ref_97731424 = ref_97009501 # MOV operation
ref_97734030 = ref_97731424 # MOV operation
ref_97734044 = ref_97734030 # MOV operation
ref_97734048 = (ref_97734044 >> (0x2 & 0x3F)) # SHR operation
ref_97734055 = ref_97734048 # MOV operation
ref_97735357 = ref_97734055 # MOV operation
ref_99176558 = ref_97735357 # MOV operation
ref_99177514 = ref_99176558 # MOV operation
ref_99177528 = (0x7 & ref_99177514) # AND operation
ref_99178855 = ref_99177528 # MOV operation
ref_100974319 = ref_99178855 # MOV operation
ref_100979319 = ref_100974319 # MOV operation
ref_100979333 = (0x1 | ref_100979319) # OR operation
ref_100980658 = ref_100979333 # MOV operation
ref_106326234 = ref_152900 # MOV operation
ref_106327391 = ref_106326234 # MOV operation
ref_112278509 = ref_56800174 # MOV operation
ref_112279666 = ref_112278509 # MOV operation
ref_112623259 = ref_106327391 # MOV operation
ref_112676950 = ref_112279666 # MOV operation
ref_112680494 = ref_112623259 # MOV operation
ref_112680498 = ref_112676950 # MOV operation
ref_112680500 = ((ref_112680498 + ref_112680494) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_112681781 = ref_112680500 # MOV operation
ref_113350013 = ref_100980658 # MOV operation
ref_113403704 = ref_112681781 # MOV operation
ref_113406310 = ref_113403704 # MOV operation
ref_113406322 = ref_113350013 # MOV operation
ref_113406324 = ref_113406310 # MOV operation
ref_113406326 = (ref_113406322 & 0xFFFFFFFF) # MOV operation
ref_113406328 = (ref_113406324 >> ((ref_113406326 & 0xFF) & 0x3F)) # SHR operation
ref_113406335 = ref_113406328 # MOV operation
ref_113407637 = ref_113406335 # MOV operation
ref_113833251 = ref_113407637 # MOV operation
ref_113834408 = ref_113833251 # MOV operation
ref_125971060 = ref_113834408 # MOV operation
ref_125972217 = ref_125971060 # MOV operation
ref_126642011 = ref_125972217 # MOV operation
ref_126644617 = ref_126642011 # MOV operation
ref_126644631 = ref_126644617 # MOV operation
ref_126644635 = (ref_126644631 >> (0x1 & 0x3F)) # SHR operation
ref_126644642 = ref_126644635 # MOV operation
ref_126645944 = ref_126644642 # MOV operation
ref_128087145 = ref_126645944 # MOV operation
ref_128088101 = ref_128087145 # MOV operation
ref_128088115 = (0x7 & ref_128088101) # AND operation
ref_128089442 = ref_128088115 # MOV operation
ref_129884906 = ref_128089442 # MOV operation
ref_129889906 = ref_129884906 # MOV operation
ref_129889920 = (0x1 | ref_129889906) # OR operation
ref_129891245 = ref_129889920 # MOV operation
ref_135894492 = ref_113834408 # MOV operation
ref_135895649 = ref_135894492 # MOV operation
ref_136511752 = ref_129891245 # MOV operation
ref_136565443 = ref_135895649 # MOV operation
ref_136568049 = ref_136565443 # MOV operation
ref_136568061 = ref_136511752 # MOV operation
ref_136568063 = ref_136568049 # MOV operation
ref_136568065 = (ref_136568061 & 0xFFFFFFFF) # MOV operation
ref_136568067 = (ref_136568063 >> ((ref_136568065 & 0xFF) & 0x3F)) # SHR operation
ref_136568074 = ref_136568067 # MOV operation
ref_136569376 = ref_136568074 # MOV operation
ref_136994990 = ref_136569376 # MOV operation
ref_136996147 = ref_136994990 # MOV operation
ref_136996149 = ((ref_136996147 >> 56) & 0xFF) # Byte reference - MOV operation
ref_136996150 = ((ref_136996147 >> 48) & 0xFF) # Byte reference - MOV operation
ref_136996151 = ((ref_136996147 >> 40) & 0xFF) # Byte reference - MOV operation
ref_136996152 = ((ref_136996147 >> 32) & 0xFF) # Byte reference - MOV operation
ref_136996153 = ((ref_136996147 >> 24) & 0xFF) # Byte reference - MOV operation
ref_136996154 = ((ref_136996147 >> 16) & 0xFF) # Byte reference - MOV operation
ref_136996155 = ((ref_136996147 >> 8) & 0xFF) # Byte reference - MOV operation
ref_136996156 = (ref_136996147 & 0xFF) # Byte reference - MOV operation
ref_155712227 = ref_80722971 # MOV operation
ref_155713384 = ref_155712227 # MOV operation
ref_162476140 = ref_42746514 # MOV operation
ref_162477297 = ref_162476140 # MOV operation
ref_163866369 = ref_162477297 # MOV operation
ref_163867325 = ref_163866369 # MOV operation
ref_163867339 = (0x7 & ref_163867325) # AND operation
ref_163868666 = ref_163867339 # MOV operation
ref_165800385 = ref_163868666 # MOV operation
ref_165801432 = ref_165800385 # MOV operation
ref_165801446 = ref_165801432 # MOV operation
ref_165801450 = ((ref_165801446 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_165801457 = ref_165801450 # MOV operation
ref_165802732 = ref_165801457 # MOV operation
ref_166498215 = ref_165802732 # MOV operation
ref_166551906 = ref_155713384 # MOV operation
ref_166556906 = ref_166551906 # MOV operation
ref_166556918 = ref_166498215 # MOV operation
ref_166556920 = (ref_166556918 | ref_166556906) # OR operation
ref_166558245 = ref_166556920 # MOV operation
ref_166983859 = ref_166558245 # MOV operation
ref_166985016 = ref_166983859 # MOV operation
ref_178164179 = ((((ref_136996149) << 8 | ref_136996150) << 8 | ref_136996151) << 8 | ref_136996152) # MOV operation
ref_178167539 = (ref_178164179 & 0xFFFFFFFF) # MOV operation
ref_178975206 = (ref_178167539 & 0xFFFFFFFF) # MOV operation
ref_178978566 = (ref_178975206 & 0xFFFFFFFF) # MOV operation
ref_198709634 = ((((ref_136996153) << 8 | ref_136996154) << 8 | ref_136996155) << 8 | ref_136996156) # MOV operation
ref_198712994 = (ref_198709634 & 0xFFFFFFFF) # MOV operation
ref_199520661 = (ref_198712994 & 0xFFFFFFFF) # MOV operation
ref_199524021 = (ref_199520661 & 0xFFFFFFFF) # MOV operation
ref_210703217 = (ref_178978566 & 0xFFFFFFFF) # MOV operation
ref_210706577 = (ref_210703217 & 0xFFFFFFFF) # MOV operation
ref_211514244 = (ref_210706577 & 0xFFFFFFFF) # MOV operation
ref_211517604 = (ref_211514244 & 0xFFFFFFFF) # MOV operation
ref_232545889 = ref_166985016 # MOV operation
ref_232547046 = ref_232545889 # MOV operation
ref_239309802 = ref_166985016 # MOV operation
ref_239310959 = ref_239309802 # MOV operation
ref_240700031 = ref_239310959 # MOV operation
ref_240700987 = ref_240700031 # MOV operation
ref_240701001 = (0x7 & ref_240700987) # AND operation
ref_240702328 = ref_240701001 # MOV operation
ref_242634047 = ref_240702328 # MOV operation
ref_242635094 = ref_242634047 # MOV operation
ref_242635108 = ref_242635094 # MOV operation
ref_242635112 = ((ref_242635108 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_242635119 = ref_242635112 # MOV operation
ref_242636394 = ref_242635119 # MOV operation
ref_243331877 = ref_242636394 # MOV operation
ref_243385568 = ref_232547046 # MOV operation
ref_243390568 = ref_243385568 # MOV operation
ref_243390580 = ref_243331877 # MOV operation
ref_243390582 = (ref_243390580 | ref_243390568) # OR operation
ref_243391907 = ref_243390582 # MOV operation
ref_243817521 = ref_243391907 # MOV operation
ref_243818678 = ref_243817521 # MOV operation
ref_254997841 = (ref_199524021 & 0xFFFFFFFF) # MOV operation
ref_255001201 = (ref_254997841 & 0xFFFFFFFF) # MOV operation
ref_255808868 = (ref_255001201 & 0xFFFFFFFF) # MOV operation
ref_255812228 = (ref_255808868 & 0xFFFFFFFF) # MOV operation
ref_275543296 = (ref_211517604 & 0xFFFFFFFF) # MOV operation
ref_275546656 = (ref_275543296 & 0xFFFFFFFF) # MOV operation
ref_276354323 = (ref_275546656 & 0xFFFFFFFF) # MOV operation
ref_276357683 = (ref_276354323 & 0xFFFFFFFF) # MOV operation
ref_276357685 = (((ref_276357683 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_276357686 = (((ref_276357683 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_276357687 = (((ref_276357683 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_276357688 = ((ref_276357683 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_287536879 = (ref_255812228 & 0xFFFFFFFF) # MOV operation
ref_287540239 = (ref_287536879 & 0xFFFFFFFF) # MOV operation
ref_288347906 = (ref_287540239 & 0xFFFFFFFF) # MOV operation
ref_288351266 = (ref_288347906 & 0xFFFFFFFF) # MOV operation
ref_288351268 = (((ref_288351266 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_288351269 = (((ref_288351266 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_288351270 = (((ref_288351266 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_288351271 = ((ref_288351266 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_309492434 = ref_42746514 # MOV operation
ref_309493591 = ref_309492434 # MOV operation
ref_315444709 = ref_56800174 # MOV operation
ref_315445866 = ref_315444709 # MOV operation
ref_315980216 = ref_309493591 # MOV operation
ref_316033907 = ref_315445866 # MOV operation
ref_316034490 = ref_315980216 # MOV operation
ref_316034494 = ref_316033907 # MOV operation
ref_316034496 = (((sx(0x40, ref_316034494) * sx(0x40, ref_316034490)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_316035759 = ref_316034496 # MOV operation
ref_322039006 = ref_243818678 # MOV operation
ref_322040163 = ref_322039006 # MOV operation
ref_327991281 = ((((((((ref_276357685) << 8 | ref_276357686) << 8 | ref_276357687) << 8 | ref_276357688) << 8 | ref_288351268) << 8 | ref_288351269) << 8 | ref_288351270) << 8 | ref_288351271) # MOV operation
ref_327992438 = ref_327991281 # MOV operation
ref_329573078 = ref_327992438 # MOV operation
ref_329627352 = ref_329573078 # MOV operation
ref_329627358 = (((sx(0x40, 0x4E1A7F2) * sx(0x40, ref_329627352)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_329628621 = ref_329627358 # MOV operation
ref_330405857 = ref_329628621 # MOV operation
ref_330459548 = ref_322040163 # MOV operation
ref_330465179 = ref_330459548 # MOV operation
ref_330465191 = ref_330405857 # MOV operation
ref_330465193 = (ref_330465191 ^ ref_330465179) # XOR operation
ref_330466467 = ref_330465193 # MOV operation
ref_331907668 = ref_330466467 # MOV operation
ref_331908624 = ref_331907668 # MOV operation
ref_331908638 = (0xF & ref_331908624) # AND operation
ref_331909965 = ref_331908638 # MOV operation
ref_333705429 = ref_331909965 # MOV operation
ref_333710429 = ref_333705429 # MOV operation
ref_333710443 = (0x1 | ref_333710429) # OR operation
ref_333711768 = ref_333710443 # MOV operation
ref_334543506 = ref_333711768 # MOV operation
ref_334597197 = ref_316035759 # MOV operation
ref_334598244 = ref_334597197 # MOV operation
ref_334598256 = ref_334543506 # MOV operation
ref_334598258 = ref_334598244 # MOV operation
ref_334598260 = (ref_334598256 & 0xFFFFFFFF) # MOV operation
ref_334598262 = ((ref_334598258 << ((ref_334598260 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_334598269 = ref_334598262 # MOV operation
ref_334599544 = ref_334598269 # MOV operation
ref_340602791 = ref_243818678 # MOV operation
ref_340603948 = ref_340602791 # MOV operation
ref_346555066 = ((((((((ref_276357685) << 8 | ref_276357686) << 8 | ref_276357687) << 8 | ref_276357688) << 8 | ref_288351268) << 8 | ref_288351269) << 8 | ref_288351270) << 8 | ref_288351271) # MOV operation
ref_346556223 = ref_346555066 # MOV operation
ref_348136863 = ref_346556223 # MOV operation
ref_348191137 = ref_348136863 # MOV operation
ref_348191143 = (((sx(0x40, 0x4E1A7F2) * sx(0x40, ref_348191137)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_348192406 = ref_348191143 # MOV operation
ref_348969642 = ref_348192406 # MOV operation
ref_349023333 = ref_340603948 # MOV operation
ref_349028964 = ref_349023333 # MOV operation
ref_349028976 = ref_348969642 # MOV operation
ref_349028978 = (ref_349028976 ^ ref_349028964) # XOR operation
ref_349030252 = ref_349028978 # MOV operation
ref_350471453 = ref_349030252 # MOV operation
ref_350472409 = ref_350471453 # MOV operation
ref_350472423 = (0xF & ref_350472409) # AND operation
ref_350473750 = ref_350472423 # MOV operation
ref_352269214 = ref_350473750 # MOV operation
ref_352274214 = ref_352269214 # MOV operation
ref_352274228 = (0x1 | ref_352274214) # OR operation
ref_352275553 = ref_352274228 # MOV operation
ref_354317087 = ref_352275553 # MOV operation
ref_354374673 = ref_354317087 # MOV operation
ref_354374677 = ((0x40 - ref_354374673) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_354374685 = ref_354374677 # MOV operation
ref_354375978 = ref_354374685 # MOV operation
ref_360379225 = ref_42746514 # MOV operation
ref_360380382 = ref_360379225 # MOV operation
ref_366331500 = ref_56800174 # MOV operation
ref_366332657 = ref_366331500 # MOV operation
ref_366867007 = ref_360380382 # MOV operation
ref_366920698 = ref_366332657 # MOV operation
ref_366921281 = ref_366867007 # MOV operation
ref_366921285 = ref_366920698 # MOV operation
ref_366921287 = (((sx(0x40, ref_366921285) * sx(0x40, ref_366921281)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_366922550 = ref_366921287 # MOV operation
ref_367590782 = ref_354375978 # MOV operation
ref_367644473 = ref_366922550 # MOV operation
ref_367647079 = ref_367644473 # MOV operation
ref_367647091 = ref_367590782 # MOV operation
ref_367647093 = ref_367647079 # MOV operation
ref_367647095 = (ref_367647091 & 0xFFFFFFFF) # MOV operation
ref_367647097 = (ref_367647093 >> ((ref_367647095 & 0xFF) & 0x3F)) # SHR operation
ref_367647104 = ref_367647097 # MOV operation
ref_367648406 = ref_367647104 # MOV operation
ref_368343889 = ref_367648406 # MOV operation
ref_368397580 = ref_334599544 # MOV operation
ref_368402580 = ref_368397580 # MOV operation
ref_368402592 = ref_368343889 # MOV operation
ref_368402594 = (ref_368402592 | ref_368402580) # OR operation
ref_368403919 = ref_368402594 # MOV operation
ref_368829533 = ref_368403919 # MOV operation
ref_368830690 = ref_368829533 # MOV operation
ref_370178820 = ref_368830690 # MOV operation
ref_370178822 = ref_370178820 # MOV operation

print(ref_370178822 & 0xffffffffffffffff)
