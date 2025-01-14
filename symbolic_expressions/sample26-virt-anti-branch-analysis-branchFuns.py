#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_269 = SymVar_0
ref_284 = ref_269 # MOV operation
ref_12885 = ref_284 # MOV operation
ref_13353 = ref_12885 # MOV operation
ref_13367 = (ref_13353 >> (0x5 & 0x3F)) # SHR operation
ref_14218 = ref_13367 # MOV operation
ref_14224 = (0x1376783EF7559EA & ref_14218) # AND operation
ref_17795 = ref_14224 # MOV operation
ref_17797 = ((ref_17795 >> 56) & 0xFF) # Byte reference - MOV operation
ref_17798 = ((ref_17795 >> 48) & 0xFF) # Byte reference - MOV operation
ref_17799 = ((ref_17795 >> 40) & 0xFF) # Byte reference - MOV operation
ref_17800 = ((ref_17795 >> 32) & 0xFF) # Byte reference - MOV operation
ref_17801 = ((ref_17795 >> 24) & 0xFF) # Byte reference - MOV operation
ref_17802 = ((ref_17795 >> 16) & 0xFF) # Byte reference - MOV operation
ref_17803 = ((ref_17795 >> 8) & 0xFF) # Byte reference - MOV operation
ref_17804 = (ref_17795 & 0xFF) # Byte reference - MOV operation
ref_21346 = ref_17795 # MOV operation
ref_22171 = ref_21346 # MOV operation
ref_22177 = (0x7063FB7 & ref_22171) # AND operation
ref_26255 = ref_284 # MOV operation
ref_26651 = ref_26255 # MOV operation
ref_26665 = (0x1A5612E2 | ref_26651) # OR operation
ref_27117 = ref_26665 # MOV operation
ref_27129 = ref_22177 # MOV operation
ref_27131 = ((ref_27129 + ref_27117) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_30707 = ref_27131 # MOV operation
ref_30709 = ((ref_30707 >> 56) & 0xFF) # Byte reference - MOV operation
ref_30710 = ((ref_30707 >> 48) & 0xFF) # Byte reference - MOV operation
ref_30711 = ((ref_30707 >> 40) & 0xFF) # Byte reference - MOV operation
ref_30712 = ((ref_30707 >> 32) & 0xFF) # Byte reference - MOV operation
ref_30713 = ((ref_30707 >> 24) & 0xFF) # Byte reference - MOV operation
ref_30714 = ((ref_30707 >> 16) & 0xFF) # Byte reference - MOV operation
ref_30715 = ((ref_30707 >> 8) & 0xFF) # Byte reference - MOV operation
ref_30716 = (ref_30707 & 0xFF) # Byte reference - MOV operation
ref_34332 = ref_284 # MOV operation
ref_35152 = ref_34332 # MOV operation
ref_35158 = ((ref_35152 - 0x2907943) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_35166 = ref_35158 # MOV operation
ref_40905 = ref_30707 # MOV operation
ref_41373 = ref_40905 # MOV operation
ref_41387 = (ref_41373 >> (0x3 & 0x3F)) # SHR operation
ref_42238 = ref_41387 # MOV operation
ref_42244 = (0xF & ref_42238) # AND operation
ref_42666 = ref_42244 # MOV operation
ref_42680 = (0x1 | ref_42666) # OR operation
ref_43094 = ref_42680 # MOV operation
ref_43096 = ((0x40 - ref_43094) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_43104 = ref_43096 # MOV operation
ref_44040 = ref_43104 # MOV operation
ref_44042 = (0x3162E74F >> ((ref_44040 & 0xFF) & 0x3F)) # SHR operation
ref_48916 = ref_30707 # MOV operation
ref_49384 = ref_48916 # MOV operation
ref_49398 = (ref_49384 >> (0x3 & 0x3F)) # SHR operation
ref_50249 = ref_49398 # MOV operation
ref_50255 = (0xF & ref_50249) # AND operation
ref_50677 = ref_50255 # MOV operation
ref_50691 = (0x1 | ref_50677) # OR operation
ref_51146 = ref_50691 # MOV operation
ref_51148 = (ref_51146 & 0xFFFFFFFF) # MOV operation
ref_51150 = ((0x3162E74F << ((ref_51148 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_51157 = ref_51150 # MOV operation
ref_51561 = ref_51157 # MOV operation
ref_51573 = ref_44042 # MOV operation
ref_51575 = (ref_51573 | ref_51561) # OR operation
ref_52068 = ref_51575 # MOV operation
ref_52082 = (ref_52068 >> (0x4 & 0x3F)) # SHR operation
ref_52933 = ref_52082 # MOV operation
ref_52939 = (0x7 & ref_52933) # AND operation
ref_53361 = ref_52939 # MOV operation
ref_53375 = (0x1 | ref_53361) # OR operation
ref_53826 = ref_35166 # MOV operation
ref_53830 = ref_53375 # MOV operation
ref_53832 = (ref_53830 & 0xFFFFFFFF) # MOV operation
ref_53834 = ((ref_53826 << ((ref_53832 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_53841 = ref_53834 # MOV operation
ref_57394 = ref_53841 # MOV operation
ref_61019 = ref_284 # MOV operation
ref_61839 = ref_61019 # MOV operation
ref_61845 = ((ref_61839 - 0x3C563FC) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_61853 = ref_61845 # MOV operation
ref_65419 = ref_61853 # MOV operation
ref_74383 = ref_30707 # MOV operation
ref_75208 = ref_74383 # MOV operation
ref_75214 = (0xF & ref_75208) # AND operation
ref_76101 = ref_75214 # MOV operation
ref_76109 = ((ref_76101 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_76116 = ref_76109 # MOV operation
ref_79667 = ref_65419 # MOV operation
ref_80063 = ref_79667 # MOV operation
ref_80075 = ref_76116 # MOV operation
ref_80077 = (ref_80075 | ref_80063) # OR operation
ref_83647 = ref_80077 # MOV operation
ref_87198 = ref_83647 # MOV operation
ref_88023 = ref_87198 # MOV operation
ref_88029 = (0x1F & ref_88023) # AND operation
ref_88916 = ref_88029 # MOV operation
ref_88924 = ((ref_88916 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_88931 = ref_88924 # MOV operation
ref_92482 = ref_57394 # MOV operation
ref_92878 = ref_92482 # MOV operation
ref_92890 = ref_88931 # MOV operation
ref_92892 = (ref_92890 | ref_92878) # OR operation
ref_96462 = ref_92892 # MOV operation
ref_101322 = ref_30707 # MOV operation
ref_102147 = ref_101322 # MOV operation
ref_102153 = (0xF & ref_102147) # AND operation
ref_103040 = ref_102153 # MOV operation
ref_103048 = ((ref_103040 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_103055 = ref_103048 # MOV operation
ref_106606 = ref_83647 # MOV operation
ref_107002 = ref_106606 # MOV operation
ref_107014 = ref_103055 # MOV operation
ref_107016 = (ref_107014 | ref_107002) # OR operation
ref_110586 = ref_107016 # MOV operation
ref_120859 = ref_110586 # MOV operation
ref_121684 = ref_120859 # MOV operation
ref_121690 = (0xF & ref_121684) # AND operation
ref_122577 = ref_121690 # MOV operation
ref_122585 = ((ref_122577 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_122592 = ref_122585 # MOV operation
ref_126143 = ref_110586 # MOV operation
ref_126539 = ref_126143 # MOV operation
ref_126551 = ref_122592 # MOV operation
ref_126553 = (ref_126551 | ref_126539) # OR operation
ref_130123 = ref_126553 # MOV operation
ref_133674 = ref_130123 # MOV operation
ref_134499 = ref_133674 # MOV operation
ref_134505 = (0x1F & ref_134499) # AND operation
ref_135392 = ref_134505 # MOV operation
ref_135400 = ((ref_135392 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_135407 = ref_135400 # MOV operation
ref_138958 = ref_96462 # MOV operation
ref_139354 = ref_138958 # MOV operation
ref_139366 = ref_135407 # MOV operation
ref_139368 = (ref_139366 | ref_139354) # OR operation
ref_142938 = ref_139368 # MOV operation
ref_142940 = ((ref_142938 >> 56) & 0xFF) # Byte reference - MOV operation
ref_142941 = ((ref_142938 >> 48) & 0xFF) # Byte reference - MOV operation
ref_142942 = ((ref_142938 >> 40) & 0xFF) # Byte reference - MOV operation
ref_142943 = ((ref_142938 >> 32) & 0xFF) # Byte reference - MOV operation
ref_142944 = ((ref_142938 >> 24) & 0xFF) # Byte reference - MOV operation
ref_142945 = ((ref_142938 >> 16) & 0xFF) # Byte reference - MOV operation
ref_142946 = ((ref_142938 >> 8) & 0xFF) # Byte reference - MOV operation
ref_142947 = (ref_142938 & 0xFF) # Byte reference - MOV operation
ref_147798 = ref_130123 # MOV operation
ref_148623 = ref_147798 # MOV operation
ref_148629 = (0xF & ref_148623) # AND operation
ref_149516 = ref_148629 # MOV operation
ref_149524 = ((ref_149516 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_149531 = ref_149524 # MOV operation
ref_153082 = ref_130123 # MOV operation
ref_153478 = ref_153082 # MOV operation
ref_153490 = ref_149531 # MOV operation
ref_153492 = (ref_153490 | ref_153478) # OR operation
ref_157062 = ref_153492 # MOV operation
ref_185753 = ref_142938 # MOV operation
ref_189296 = ref_142938 # MOV operation
ref_189723 = ref_189296 # MOV operation
ref_189735 = ref_185753 # MOV operation
ref_189737 = ((ref_189735 + ref_189723) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_190593 = ref_189737 # MOV operation
ref_190599 = (0x7 & ref_190593) # AND operation
ref_191486 = ref_190599 # MOV operation
ref_191494 = ((ref_191486 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_191501 = ref_191494 # MOV operation
ref_195052 = ref_157062 # MOV operation
ref_195448 = ref_195052 # MOV operation
ref_195460 = ref_191501 # MOV operation
ref_195462 = (ref_195460 | ref_195448) # OR operation
ref_199032 = ref_195462 # MOV operation
ref_205129 = ((((ref_142940) << 8 | ref_142941) << 8 | ref_142942) << 8 | ref_142943) # MOV operation
ref_206000 = (ref_205129 & 0xFFFFFFFF) # MOV operation
ref_212111 = ((((ref_142944) << 8 | ref_142945) << 8 | ref_142946) << 8 | ref_142947) # MOV operation
ref_218252 = (ref_212111 & 0xFFFFFFFF) # MOV operation
ref_218254 = (((ref_218252 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_218255 = (((ref_218252 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_218256 = (((ref_218252 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_218257 = ((ref_218252 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_219093 = (ref_206000 & 0xFFFFFFFF) # MOV operation
ref_225234 = (ref_219093 & 0xFFFFFFFF) # MOV operation
ref_225236 = (((ref_225234 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_225237 = (((ref_225234 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_225238 = (((ref_225234 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_225239 = ((ref_225234 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_231798 = ref_17799 # MOVZX operation
ref_232306 = (ref_231798 & 0xFF) # MOVZX operation
ref_244162 = ref_17800 # MOVZX operation
ref_244670 = (ref_244162 & 0xFF) # MOVZX operation
ref_244672 = (ref_244670 & 0xFF) # Byte reference - MOV operation
ref_251256 = (ref_232306 & 0xFF) # MOVZX operation
ref_251764 = (ref_251256 & 0xFF) # MOVZX operation
ref_251766 = (ref_251764 & 0xFF) # Byte reference - MOV operation
ref_258350 = ref_17798 # MOVZX operation
ref_258858 = (ref_258350 & 0xFF) # MOVZX operation
ref_270714 = ref_17804 # MOVZX operation
ref_271222 = (ref_270714 & 0xFF) # MOVZX operation
ref_271224 = (ref_271222 & 0xFF) # Byte reference - MOV operation
ref_277808 = (ref_258858 & 0xFF) # MOVZX operation
ref_278316 = (ref_277808 & 0xFF) # MOVZX operation
ref_278318 = (ref_278316 & 0xFF) # Byte reference - MOV operation
ref_284449 = ((((ref_30713) << 8 | ref_30714) << 8 | ref_30715) << 8 | ref_30716) # MOV operation
ref_285320 = (ref_284449 & 0xFFFFFFFF) # MOV operation
ref_291431 = ((((ref_30709) << 8 | ref_30710) << 8 | ref_30711) << 8 | ref_30712) # MOV operation
ref_297572 = (ref_291431 & 0xFFFFFFFF) # MOV operation
ref_297574 = (((ref_297572 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_297575 = (((ref_297572 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_297576 = (((ref_297572 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_297577 = ((ref_297572 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_298413 = (ref_285320 & 0xFFFFFFFF) # MOV operation
ref_304554 = (ref_298413 & 0xFFFFFFFF) # MOV operation
ref_304556 = (((ref_304554 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_304557 = (((ref_304554 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_304558 = (((ref_304554 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_304559 = ((ref_304554 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_313930 = ((((((((ref_17797) << 8 | ref_271224) << 8 | ref_244672) << 8 | ref_251766) << 8 | ref_17801) << 8 | ref_17802) << 8 | ref_17803) << 8 | ref_278318) # MOV operation
ref_314755 = ref_313930 # MOV operation
ref_314761 = (0x3F & ref_314755) # AND operation
ref_315648 = ref_314761 # MOV operation
ref_315656 = ((ref_315648 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_315663 = ref_315656 # MOV operation
ref_319616 = ((((((((ref_304556) << 8 | ref_304557) << 8 | ref_304558) << 8 | ref_304559) << 8 | ref_297574) << 8 | ref_297575) << 8 | ref_297576) << 8 | ref_297577) # MOV operation
ref_320012 = ref_319616 # MOV operation
ref_320024 = ref_315663 # MOV operation
ref_320026 = (ref_320024 | ref_320012) # OR operation
ref_323998 = ref_320026 # MOV operation
ref_333751 = ref_199032 # MOV operation
ref_338599 = ref_323998 # MOV operation
ref_339067 = ref_338599 # MOV operation
ref_339081 = (ref_339067 >> (0x3 & 0x3F)) # SHR operation
ref_339932 = ref_339081 # MOV operation
ref_339938 = (0xF & ref_339932) # AND operation
ref_340360 = ref_339938 # MOV operation
ref_340374 = (0x1 | ref_340360) # OR operation
ref_340788 = ref_340374 # MOV operation
ref_340790 = ((0x40 - ref_340788) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_340798 = ref_340790 # MOV operation
ref_341245 = ref_333751 # MOV operation
ref_341249 = ref_340798 # MOV operation
ref_341251 = (ref_341249 & 0xFFFFFFFF) # MOV operation
ref_341253 = ((ref_341245 << ((ref_341251 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_341260 = ref_341253 # MOV operation
ref_345681 = ref_323998 # MOV operation
ref_346149 = ref_345681 # MOV operation
ref_346163 = (ref_346149 >> (0x3 & 0x3F)) # SHR operation
ref_347014 = ref_346163 # MOV operation
ref_347020 = (0xF & ref_347014) # AND operation
ref_347442 = ref_347020 # MOV operation
ref_347456 = (0x1 | ref_347442) # OR operation
ref_351024 = ref_199032 # MOV operation
ref_351492 = ref_351024 # MOV operation
ref_351504 = ref_347456 # MOV operation
ref_351506 = (ref_351492 >> ((ref_351504 & 0xFF) & 0x3F)) # SHR operation
ref_351928 = ref_351506 # MOV operation
ref_351940 = ref_341260 # MOV operation
ref_351942 = (ref_351940 | ref_351928) # OR operation
ref_352792 = ref_351942 # MOV operation
ref_352798 = (0xF & ref_352792) # AND operation
ref_353685 = ref_352798 # MOV operation
ref_353693 = ((ref_353685 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_353700 = ref_353693 # MOV operation
ref_357251 = ((((((((ref_218254) << 8 | ref_218255) << 8 | ref_218256) << 8 | ref_218257) << 8 | ref_225236) << 8 | ref_225237) << 8 | ref_225238) << 8 | ref_225239) # MOV operation
ref_357647 = ref_357251 # MOV operation
ref_357659 = ref_353700 # MOV operation
ref_357661 = (ref_357659 | ref_357647) # OR operation
ref_361231 = ref_357661 # MOV operation
ref_364782 = ref_199032 # MOV operation
ref_368325 = ref_361231 # MOV operation
ref_368721 = ref_368325 # MOV operation
ref_368733 = ref_364782 # MOV operation
ref_368735 = (ref_368733 | ref_368721) # OR operation
ref_372303 = ((((((((ref_17797) << 8 | ref_271224) << 8 | ref_244672) << 8 | ref_251766) << 8 | ref_17801) << 8 | ref_17802) << 8 | ref_17803) << 8 | ref_278318) # MOV operation
ref_376716 = ref_323998 # MOV operation
ref_377184 = ref_376716 # MOV operation
ref_377198 = (ref_377184 >> (0x3 & 0x3F)) # SHR operation
ref_378049 = ref_377198 # MOV operation
ref_378055 = (0x7 & ref_378049) # AND operation
ref_378477 = ref_378055 # MOV operation
ref_378491 = (0x1 | ref_378477) # OR operation
ref_378942 = ref_372303 # MOV operation
ref_378946 = ref_378491 # MOV operation
ref_378948 = (ref_378946 & 0xFFFFFFFF) # MOV operation
ref_378950 = ((ref_378942 << ((ref_378948 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_378957 = ref_378950 # MOV operation
ref_379361 = ref_378957 # MOV operation
ref_379373 = ref_368735 # MOV operation
ref_379375 = (ref_379373 | ref_379361) # OR operation
ref_383022 = ref_379375 # MOV operation
ref_383837 = ref_383022 # MOV operation
ref_383839 = ref_383837 # MOV operation

print(ref_383839 & 0xffffffffffffffff)
