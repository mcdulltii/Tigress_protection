#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_139974 = ref_278 # MOV operation
ref_140174 = ref_139974 # MOV operation
ref_140182 = (ref_140174 >> (0x5 & 0x3F)) # SHR operation
ref_140189 = ref_140182 # MOV operation
ref_140285 = ref_140189 # MOV operation
ref_140299 = (0x1376783EF7559EA & ref_140285) # AND operation
ref_140408 = ref_140299 # MOV operation
ref_140410 = ((ref_140408 >> 56) & 0xFF) # Byte reference - MOV operation
ref_140411 = ((ref_140408 >> 48) & 0xFF) # Byte reference - MOV operation
ref_140412 = ((ref_140408 >> 40) & 0xFF) # Byte reference - MOV operation
ref_140413 = ((ref_140408 >> 32) & 0xFF) # Byte reference - MOV operation
ref_140414 = ((ref_140408 >> 24) & 0xFF) # Byte reference - MOV operation
ref_140415 = ((ref_140408 >> 16) & 0xFF) # Byte reference - MOV operation
ref_140416 = ((ref_140408 >> 8) & 0xFF) # Byte reference - MOV operation
ref_140417 = (ref_140408 & 0xFF) # Byte reference - MOV operation
ref_142063 = ref_278 # MOV operation
ref_142263 = ref_142063 # MOV operation
ref_142269 = (0x1A5612E2 | ref_142263) # OR operation
ref_143308 = ref_140408 # MOV operation
ref_143384 = ref_143308 # MOV operation
ref_143398 = (0x7063FB7 & ref_143384) # AND operation
ref_143507 = ref_142269 # MOV operation
ref_143511 = ref_143398 # MOV operation
ref_143513 = ((ref_143511 + ref_143507) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_143623 = ref_143513 # MOV operation
ref_143625 = ((ref_143623 >> 56) & 0xFF) # Byte reference - MOV operation
ref_143626 = ((ref_143623 >> 48) & 0xFF) # Byte reference - MOV operation
ref_143627 = ((ref_143623 >> 40) & 0xFF) # Byte reference - MOV operation
ref_143628 = ((ref_143623 >> 32) & 0xFF) # Byte reference - MOV operation
ref_143629 = ((ref_143623 >> 24) & 0xFF) # Byte reference - MOV operation
ref_143630 = ((ref_143623 >> 16) & 0xFF) # Byte reference - MOV operation
ref_143631 = ((ref_143623 >> 8) & 0xFF) # Byte reference - MOV operation
ref_143632 = (ref_143623 & 0xFF) # Byte reference - MOV operation
ref_145595 = ref_143623 # MOV operation
ref_145795 = ref_145595 # MOV operation
ref_145803 = (ref_145795 >> (0x3 & 0x3F)) # SHR operation
ref_145810 = ref_145803 # MOV operation
ref_145906 = ref_145810 # MOV operation
ref_145920 = (0xF & ref_145906) # AND operation
ref_146145 = ref_145920 # MOV operation
ref_146151 = (0x1 | ref_146145) # OR operation
ref_146380 = ref_146151 # MOV operation
ref_146382 = ((0x3162E74F << ((ref_146380 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_147537 = ref_143623 # MOV operation
ref_147737 = ref_147537 # MOV operation
ref_147745 = (ref_147737 >> (0x3 & 0x3F)) # SHR operation
ref_147752 = ref_147745 # MOV operation
ref_147848 = ref_147752 # MOV operation
ref_147862 = (0xF & ref_147848) # AND operation
ref_148087 = ref_147862 # MOV operation
ref_148093 = (0x1 | ref_148087) # OR operation
ref_148322 = ref_148093 # MOV operation
ref_148324 = ((0x40 - ref_148322) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_148332 = ref_148324 # MOV operation
ref_148440 = ref_148332 # MOV operation
ref_148442 = (ref_148440 & 0xFFFFFFFF) # MOV operation
ref_148444 = (0x3162E74F >> ((ref_148442 & 0xFF) & 0x3F)) # SHR operation
ref_148451 = ref_148444 # MOV operation
ref_148555 = ref_146382 # MOV operation
ref_148559 = ref_148451 # MOV operation
ref_148561 = (ref_148559 | ref_148555) # OR operation
ref_148786 = ref_148561 # MOV operation
ref_148794 = (ref_148786 >> (0x4 & 0x3F)) # SHR operation
ref_148801 = ref_148794 # MOV operation
ref_148897 = ref_148801 # MOV operation
ref_148911 = (0x7 & ref_148897) # AND operation
ref_149136 = ref_148911 # MOV operation
ref_149142 = (0x1 | ref_149136) # OR operation
ref_150096 = ref_278 # MOV operation
ref_150172 = ref_150096 # MOV operation
ref_150186 = ((ref_150172 - 0x2907943) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_150194 = ref_150186 # MOV operation
ref_150290 = ref_150194 # MOV operation
ref_150302 = ref_149142 # MOV operation
ref_150304 = ((ref_150290 << ((ref_150302 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_150413 = ref_150304 # MOV operation
ref_152184 = ref_278 # MOV operation
ref_152260 = ref_152184 # MOV operation
ref_152274 = ((ref_152260 - 0x3C563FC) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_152282 = ref_152274 # MOV operation
ref_152386 = ref_152282 # MOV operation
ref_155111 = ref_152386 # MOV operation
ref_156561 = ref_143623 # MOV operation
ref_156637 = ref_156561 # MOV operation
ref_156651 = (0xF & ref_156637) # AND operation
ref_156752 = ref_156651 # MOV operation
ref_156766 = ((ref_156752 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_156875 = ref_155111 # MOV operation
ref_156879 = ref_156766 # MOV operation
ref_156881 = (ref_156879 | ref_156875) # OR operation
ref_156990 = ref_156881 # MOV operation
ref_158730 = ref_150413 # MOV operation
ref_159860 = ref_156990 # MOV operation
ref_159936 = ref_159860 # MOV operation
ref_159950 = (0x1F & ref_159936) # AND operation
ref_160051 = ref_159950 # MOV operation
ref_160065 = ((ref_160051 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_160174 = ref_158730 # MOV operation
ref_160178 = ref_160065 # MOV operation
ref_160180 = (ref_160178 | ref_160174) # OR operation
ref_160289 = ref_160180 # MOV operation
ref_162029 = ref_156990 # MOV operation
ref_163479 = ref_143623 # MOV operation
ref_163555 = ref_163479 # MOV operation
ref_163569 = (0xF & ref_163555) # AND operation
ref_163670 = ref_163569 # MOV operation
ref_163684 = ((ref_163670 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_163793 = ref_162029 # MOV operation
ref_163797 = ref_163684 # MOV operation
ref_163799 = (ref_163797 | ref_163793) # OR operation
ref_163908 = ref_163799 # MOV operation
ref_166953 = ref_163908 # MOV operation
ref_168403 = ref_163908 # MOV operation
ref_168479 = ref_168403 # MOV operation
ref_168493 = (0xF & ref_168479) # AND operation
ref_168594 = ref_168493 # MOV operation
ref_168608 = ((ref_168594 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_168717 = ref_166953 # MOV operation
ref_168721 = ref_168608 # MOV operation
ref_168723 = (ref_168721 | ref_168717) # OR operation
ref_168832 = ref_168723 # MOV operation
ref_170572 = ref_160289 # MOV operation
ref_171702 = ref_168832 # MOV operation
ref_171778 = ref_171702 # MOV operation
ref_171792 = (0x1F & ref_171778) # AND operation
ref_171893 = ref_171792 # MOV operation
ref_171907 = ((ref_171893 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_172016 = ref_170572 # MOV operation
ref_172020 = ref_171907 # MOV operation
ref_172022 = (ref_172020 | ref_172016) # OR operation
ref_172131 = ref_172022 # MOV operation
ref_172133 = ((ref_172131 >> 56) & 0xFF) # Byte reference - MOV operation
ref_172134 = ((ref_172131 >> 48) & 0xFF) # Byte reference - MOV operation
ref_172135 = ((ref_172131 >> 40) & 0xFF) # Byte reference - MOV operation
ref_172136 = ((ref_172131 >> 32) & 0xFF) # Byte reference - MOV operation
ref_172137 = ((ref_172131 >> 24) & 0xFF) # Byte reference - MOV operation
ref_172138 = ((ref_172131 >> 16) & 0xFF) # Byte reference - MOV operation
ref_172139 = ((ref_172131 >> 8) & 0xFF) # Byte reference - MOV operation
ref_172140 = (ref_172131 & 0xFF) # Byte reference - MOV operation
ref_173871 = ref_168832 # MOV operation
ref_175321 = ref_168832 # MOV operation
ref_175397 = ref_175321 # MOV operation
ref_175411 = (0xF & ref_175397) # AND operation
ref_175512 = ref_175411 # MOV operation
ref_175526 = ((ref_175512 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_175635 = ref_173871 # MOV operation
ref_175639 = ref_175526 # MOV operation
ref_175641 = (ref_175639 | ref_175635) # OR operation
ref_175750 = ref_175641 # MOV operation
ref_183712 = ref_175750 # MOV operation
ref_184842 = ref_172131 # MOV operation
ref_185740 = ref_172131 # MOV operation
ref_185824 = ref_184842 # MOV operation
ref_185828 = ref_185740 # MOV operation
ref_185830 = ((ref_185828 + ref_185824) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_185932 = ref_185830 # MOV operation
ref_185946 = (0x7 & ref_185932) # AND operation
ref_186047 = ref_185946 # MOV operation
ref_186061 = ((ref_186047 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_186170 = ref_183712 # MOV operation
ref_186174 = ref_186061 # MOV operation
ref_186176 = (ref_186174 | ref_186170) # OR operation
ref_186285 = ref_186176 # MOV operation
ref_187809 = ((((ref_172133) << 8 | ref_172134) << 8 | ref_172135) << 8 | ref_172136) # MOV operation
ref_188017 = (ref_187809 & 0xFFFFFFFF) # MOV operation
ref_189537 = ((((ref_172137) << 8 | ref_172138) << 8 | ref_172139) << 8 | ref_172140) # MOV operation
ref_191045 = (ref_189537 & 0xFFFFFFFF) # MOV operation
ref_191047 = (((ref_191045 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_191048 = (((ref_191045 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_191049 = (((ref_191045 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_191050 = ((ref_191045 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_191265 = (ref_188017 & 0xFFFFFFFF) # MOV operation
ref_192773 = (ref_191265 & 0xFFFFFFFF) # MOV operation
ref_192775 = (((ref_192773 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_192776 = (((ref_192773 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_192777 = (((ref_192773 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_192778 = ((ref_192773 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_194421 = ref_140412 # MOVZX operation
ref_194497 = (ref_194421 & 0xFF) # MOVZX operation
ref_197441 = ref_140413 # MOVZX operation
ref_197517 = (ref_197441 & 0xFF) # MOVZX operation
ref_197519 = (ref_197517 & 0xFF) # Byte reference - MOV operation
ref_199161 = (ref_194497 & 0xFF) # MOVZX operation
ref_199237 = (ref_199161 & 0xFF) # MOVZX operation
ref_199239 = (ref_199237 & 0xFF) # Byte reference - MOV operation
ref_200881 = ref_140411 # MOVZX operation
ref_200957 = (ref_200881 & 0xFF) # MOVZX operation
ref_203901 = ref_140417 # MOVZX operation
ref_203977 = (ref_203901 & 0xFF) # MOVZX operation
ref_203979 = (ref_203977 & 0xFF) # Byte reference - MOV operation
ref_205621 = (ref_200957 & 0xFF) # MOVZX operation
ref_205697 = (ref_205621 & 0xFF) # MOVZX operation
ref_205699 = (ref_205697 & 0xFF) # Byte reference - MOV operation
ref_207213 = ((((ref_143629) << 8 | ref_143630) << 8 | ref_143631) << 8 | ref_143632) # MOV operation
ref_207421 = (ref_207213 & 0xFFFFFFFF) # MOV operation
ref_208941 = ((((ref_143625) << 8 | ref_143626) << 8 | ref_143627) << 8 | ref_143628) # MOV operation
ref_210449 = (ref_208941 & 0xFFFFFFFF) # MOV operation
ref_210451 = (((ref_210449 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_210452 = (((ref_210449 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_210453 = (((ref_210449 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_210454 = ((ref_210449 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_210669 = (ref_207421 & 0xFFFFFFFF) # MOV operation
ref_212177 = (ref_210669 & 0xFFFFFFFF) # MOV operation
ref_212179 = (((ref_212177 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_212180 = (((ref_212177 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_212181 = (((ref_212177 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_212182 = ((ref_212177 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_215158 = ((((((((ref_212179) << 8 | ref_212180) << 8 | ref_212181) << 8 | ref_212182) << 8 | ref_210451) << 8 | ref_210452) << 8 | ref_210453) << 8 | ref_210454) # MOV operation
ref_216608 = ((((((((ref_140410) << 8 | ref_203979) << 8 | ref_197519) << 8 | ref_199239) << 8 | ref_140414) << 8 | ref_140415) << 8 | ref_140416) << 8 | ref_205699) # MOV operation
ref_216684 = ref_216608 # MOV operation
ref_216698 = (0x3F & ref_216684) # AND operation
ref_216799 = ref_216698 # MOV operation
ref_216813 = ((ref_216799 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_216922 = ref_215158 # MOV operation
ref_216926 = ref_216813 # MOV operation
ref_216928 = (ref_216926 | ref_216922) # OR operation
ref_217037 = ref_216928 # MOV operation
ref_220243 = ((((((((ref_191047) << 8 | ref_191048) << 8 | ref_191049) << 8 | ref_191050) << 8 | ref_192775) << 8 | ref_192776) << 8 | ref_192777) << 8 | ref_192778) # MOV operation
ref_221373 = ref_186285 # MOV operation
ref_222387 = ref_217037 # MOV operation
ref_222587 = ref_222387 # MOV operation
ref_222595 = (ref_222587 >> (0x3 & 0x3F)) # SHR operation
ref_222602 = ref_222595 # MOV operation
ref_222698 = ref_222602 # MOV operation
ref_222712 = (0xF & ref_222698) # AND operation
ref_222937 = ref_222712 # MOV operation
ref_222943 = (0x1 | ref_222937) # OR operation
ref_223052 = ref_221373 # MOV operation
ref_223056 = ref_222943 # MOV operation
ref_223058 = (ref_223056 & 0xFFFFFFFF) # MOV operation
ref_223060 = (ref_223052 >> ((ref_223058 & 0xFF) & 0x3F)) # SHR operation
ref_223067 = ref_223060 # MOV operation
ref_224101 = ref_217037 # MOV operation
ref_224301 = ref_224101 # MOV operation
ref_224309 = (ref_224301 >> (0x3 & 0x3F)) # SHR operation
ref_224316 = ref_224309 # MOV operation
ref_224412 = ref_224316 # MOV operation
ref_224426 = (0xF & ref_224412) # AND operation
ref_224651 = ref_224426 # MOV operation
ref_224657 = (0x1 | ref_224651) # OR operation
ref_224886 = ref_224657 # MOV operation
ref_224888 = ((0x40 - ref_224886) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_224896 = ref_224888 # MOV operation
ref_225814 = ref_186285 # MOV operation
ref_225890 = ref_225814 # MOV operation
ref_225902 = ref_224896 # MOV operation
ref_225904 = ((ref_225890 << ((ref_225902 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_226013 = ref_223067 # MOV operation
ref_226017 = ref_225904 # MOV operation
ref_226019 = (ref_226017 | ref_226013) # OR operation
ref_226120 = ref_226019 # MOV operation
ref_226134 = (0xF & ref_226120) # AND operation
ref_226235 = ref_226134 # MOV operation
ref_226249 = ((ref_226235 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_226358 = ref_220243 # MOV operation
ref_226362 = ref_226249 # MOV operation
ref_226364 = (ref_226362 | ref_226358) # OR operation
ref_226473 = ref_226364 # MOV operation
ref_228253 = ref_217037 # MOV operation
ref_228453 = ref_228253 # MOV operation
ref_228461 = (ref_228453 >> (0x3 & 0x3F)) # SHR operation
ref_228468 = ref_228461 # MOV operation
ref_228564 = ref_228468 # MOV operation
ref_228578 = (0x7 & ref_228564) # AND operation
ref_228803 = ref_228578 # MOV operation
ref_228809 = (0x1 | ref_228803) # OR operation
ref_229732 = ((((((((ref_140410) << 8 | ref_203979) << 8 | ref_197519) << 8 | ref_199239) << 8 | ref_140414) << 8 | ref_140415) << 8 | ref_140416) << 8 | ref_205699) # MOV operation
ref_229808 = ref_229732 # MOV operation
ref_229820 = ref_228809 # MOV operation
ref_229822 = ((ref_229808 << ((ref_229820 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_230745 = ref_226473 # MOV operation
ref_231643 = ref_186285 # MOV operation
ref_231727 = ref_230745 # MOV operation
ref_231731 = ref_231643 # MOV operation
ref_231733 = (ref_231731 | ref_231727) # OR operation
ref_231842 = ref_229822 # MOV operation
ref_231846 = ref_231733 # MOV operation
ref_231848 = (ref_231846 | ref_231842) # OR operation
ref_231957 = ref_231848 # MOV operation
ref_232168 = ref_231957 # MOV operation
ref_232170 = ref_232168 # MOV operation

print(ref_232170 & 0xffffffffffffffff)
