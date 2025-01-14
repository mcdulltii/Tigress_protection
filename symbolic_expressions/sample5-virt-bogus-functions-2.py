#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_214 = SymVar_0
ref_225 = ref_214 # MOV operation
ref_237 = ref_225 # MOV operation
ref_239 = ref_237 # MOV operation
ref_295 = ((ref_239 >> 56) & 0xFF) # Byte reference - MOV operation
ref_296 = ((ref_239 >> 48) & 0xFF) # Byte reference - MOV operation
ref_297 = ((ref_239 >> 40) & 0xFF) # Byte reference - MOV operation
ref_298 = ((ref_239 >> 32) & 0xFF) # Byte reference - MOV operation
ref_299 = ((ref_239 >> 24) & 0xFF) # Byte reference - MOV operation
ref_300 = ((ref_239 >> 16) & 0xFF) # Byte reference - MOV operation
ref_301 = ((ref_239 >> 8) & 0xFF) # Byte reference - MOV operation
ref_302 = (ref_239 & 0xFF) # Byte reference - MOV operation
ref_21201 = ref_302 # MOVZX operation
ref_21521 = (ref_21201 & 0xFF) # MOVZX operation
ref_21523 = (ref_21521 & 0xFF) # MOVZX operation
ref_22763 = (ref_21523 & 0xFFFFFFFF) # MOV operation
ref_22765 = (((ref_22763 & 0xFFFFFFFF) + 0x0) & 0xFFFFFFFF) # ADD operation
ref_23525 = (ref_22765 & 0xFFFFFFFF) # MOV operation
ref_24709 = (ref_23525 & 0xFFFFFFFF) # MOV operation
ref_25007 = (ref_24709 & 0xFFFFFFFF) # MOV operation
ref_25025 = (((ref_25007 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_25032 = (ref_25025 & 0xFFFFFFFF) # MOV operation
ref_25858 = (ref_23525 & 0xFFFFFFFF) # MOV operation
ref_26250 = (ref_25858 & 0xFFFFFFFF) # MOV operation
ref_26264 = (ref_25032 & 0xFFFFFFFF) # MOV operation
ref_26266 = (((ref_26264 & 0xFFFFFFFF) + (ref_26250 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_27076 = (ref_26266 & 0xFFFFFFFF) # MOV operation
ref_27854 = (ref_27076 & 0xFFFFFFFF) # MOV operation
ref_28658 = (ref_27854 & 0xFFFFFFFF) # MOV operation
ref_28668 = ((ref_28658 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_28675 = (ref_28668 & 0xFFFFFFFF) # MOV operation
ref_29505 = (ref_27076 & 0xFFFFFFFF) # MOV operation
ref_29907 = (ref_29505 & 0xFFFFFFFF) # MOV operation
ref_29921 = (ref_28675 & 0xFFFFFFFF) # MOV operation
ref_29923 = ((ref_29921 & 0xFFFFFFFF) ^ (ref_29907 & 0xFFFFFFFF)) # XOR operation
ref_30706 = (ref_29923 & 0xFFFFFFFF) # MOV operation
ref_41110 = ref_301 # MOVZX operation
ref_41454 = (ref_41110 & 0xFF) # MOVZX operation
ref_41456 = (ref_41454 & 0xFF) # MOVZX operation
ref_42299 = (ref_30706 & 0xFFFFFFFF) # MOV operation
ref_42701 = (ref_42299 & 0xFFFFFFFF) # MOV operation
ref_42715 = (ref_41456 & 0xFFFFFFFF) # MOV operation
ref_42717 = (((ref_42715 & 0xFFFFFFFF) + (ref_42701 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_43573 = (ref_42717 & 0xFFFFFFFF) # MOV operation
ref_44705 = (ref_43573 & 0xFFFFFFFF) # MOV operation
ref_45031 = (ref_44705 & 0xFFFFFFFF) # MOV operation
ref_45049 = (((ref_45031 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_45056 = (ref_45049 & 0xFFFFFFFF) # MOV operation
ref_45826 = (ref_43573 & 0xFFFFFFFF) # MOV operation
ref_46196 = (ref_45826 & 0xFFFFFFFF) # MOV operation
ref_46210 = (ref_45056 & 0xFFFFFFFF) # MOV operation
ref_46212 = (((ref_46210 & 0xFFFFFFFF) + (ref_46196 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_47074 = (ref_46212 & 0xFFFFFFFF) # MOV operation
ref_47870 = (ref_47074 & 0xFFFFFFFF) # MOV operation
ref_48622 = (ref_47870 & 0xFFFFFFFF) # MOV operation
ref_48632 = ((ref_48622 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_48639 = (ref_48632 & 0xFFFFFFFF) # MOV operation
ref_49469 = (ref_47074 & 0xFFFFFFFF) # MOV operation
ref_49871 = (ref_49469 & 0xFFFFFFFF) # MOV operation
ref_49885 = (ref_48639 & 0xFFFFFFFF) # MOV operation
ref_49887 = ((ref_49885 & 0xFFFFFFFF) ^ (ref_49871 & 0xFFFFFFFF)) # XOR operation
ref_50730 = (ref_49887 & 0xFFFFFFFF) # MOV operation
ref_61134 = ref_300 # MOVZX operation
ref_61530 = (ref_61134 & 0xFF) # MOVZX operation
ref_61532 = (ref_61530 & 0xFF) # MOVZX operation
ref_62232 = (ref_50730 & 0xFFFFFFFF) # MOV operation
ref_62697 = (ref_62232 & 0xFFFFFFFF) # MOV operation
ref_62711 = (ref_61532 & 0xFFFFFFFF) # MOV operation
ref_62713 = (((ref_62711 & 0xFFFFFFFF) + (ref_62697 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_63525 = (ref_62713 & 0xFFFFFFFF) # MOV operation
ref_64701 = (ref_63525 & 0xFFFFFFFF) # MOV operation
ref_65079 = (ref_64701 & 0xFFFFFFFF) # MOV operation
ref_65097 = (((ref_65079 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_65104 = (ref_65097 & 0xFFFFFFFF) # MOV operation
ref_65850 = (ref_63525 & 0xFFFFFFFF) # MOV operation
ref_66252 = (ref_65850 & 0xFFFFFFFF) # MOV operation
ref_66266 = (ref_65104 & 0xFFFFFFFF) # MOV operation
ref_66268 = (((ref_66266 & 0xFFFFFFFF) + (ref_66252 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_67020 = (ref_66268 & 0xFFFFFFFF) # MOV operation
ref_67868 = (ref_67020 & 0xFFFFFFFF) # MOV operation
ref_68638 = (ref_67868 & 0xFFFFFFFF) # MOV operation
ref_68648 = ((ref_68638 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_68655 = (ref_68648 & 0xFFFFFFFF) # MOV operation
ref_69433 = (ref_67020 & 0xFFFFFFFF) # MOV operation
ref_69791 = (ref_69433 & 0xFFFFFFFF) # MOV operation
ref_69805 = (ref_68655 & 0xFFFFFFFF) # MOV operation
ref_69807 = ((ref_69805 & 0xFFFFFFFF) ^ (ref_69791 & 0xFFFFFFFF)) # XOR operation
ref_70694 = (ref_69807 & 0xFFFFFFFF) # MOV operation
ref_81098 = ref_299 # MOVZX operation
ref_81450 = (ref_81098 & 0xFF) # MOVZX operation
ref_81452 = (ref_81450 & 0xFF) # MOVZX operation
ref_82308 = (ref_70694 & 0xFFFFFFFF) # MOV operation
ref_82606 = (ref_82308 & 0xFFFFFFFF) # MOV operation
ref_82620 = (ref_81452 & 0xFFFFFFFF) # MOV operation
ref_82622 = (((ref_82620 & 0xFFFFFFFF) + (ref_82606 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_83521 = (ref_82622 & 0xFFFFFFFF) # MOV operation
ref_84725 = (ref_83521 & 0xFFFFFFFF) # MOV operation
ref_85127 = (ref_84725 & 0xFFFFFFFF) # MOV operation
ref_85145 = (((ref_85127 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_85152 = (ref_85145 & 0xFFFFFFFF) # MOV operation
ref_85898 = (ref_83521 & 0xFFFFFFFF) # MOV operation
ref_86248 = (ref_85898 & 0xFFFFFFFF) # MOV operation
ref_86262 = (ref_85152 & 0xFFFFFFFF) # MOV operation
ref_86264 = (((ref_86262 & 0xFFFFFFFF) + (ref_86248 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_87076 = (ref_86264 & 0xFFFFFFFF) # MOV operation
ref_87814 = (ref_87076 & 0xFFFFFFFF) # MOV operation
ref_88636 = (ref_87814 & 0xFFFFFFFF) # MOV operation
ref_88646 = ((ref_88636 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_88653 = (ref_88646 & 0xFFFFFFFF) # MOV operation
ref_89449 = (ref_87076 & 0xFFFFFFFF) # MOV operation
ref_89755 = (ref_89449 & 0xFFFFFFFF) # MOV operation
ref_89769 = (ref_88653 & 0xFFFFFFFF) # MOV operation
ref_89771 = ((ref_89769 & 0xFFFFFFFF) ^ (ref_89755 & 0xFFFFFFFF)) # XOR operation
ref_90614 = (ref_89771 & 0xFFFFFFFF) # MOV operation
ref_101018 = ref_298 # MOVZX operation
ref_101414 = (ref_101018 & 0xFF) # MOVZX operation
ref_101416 = (ref_101414 & 0xFF) # MOVZX operation
ref_102228 = (ref_90614 & 0xFFFFFFFF) # MOV operation
ref_102630 = (ref_102228 & 0xFFFFFFFF) # MOV operation
ref_102644 = (ref_101416 & 0xFFFFFFFF) # MOV operation
ref_102646 = (((ref_102644 & 0xFFFFFFFF) + (ref_102630 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_103430 = (ref_102646 & 0xFFFFFFFF) # MOV operation
ref_104677 = (ref_103430 & 0xFFFFFFFF) # MOV operation
ref_105079 = (ref_104677 & 0xFFFFFFFF) # MOV operation
ref_105097 = (((ref_105079 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_105104 = (ref_105097 & 0xFFFFFFFF) # MOV operation
ref_105946 = (ref_103430 & 0xFFFFFFFF) # MOV operation
ref_106244 = (ref_105946 & 0xFFFFFFFF) # MOV operation
ref_106258 = (ref_105104 & 0xFFFFFFFF) # MOV operation
ref_106260 = (((ref_106258 & 0xFFFFFFFF) + (ref_106244 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_107072 = (ref_106260 & 0xFFFFFFFF) # MOV operation
ref_107870 = (ref_107072 & 0xFFFFFFFF) # MOV operation
ref_108582 = (ref_107870 & 0xFFFFFFFF) # MOV operation
ref_108592 = ((ref_108582 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_108599 = (ref_108592 & 0xFFFFFFFF) # MOV operation
ref_109447 = (ref_107072 & 0xFFFFFFFF) # MOV operation
ref_109773 = (ref_109447 & 0xFFFFFFFF) # MOV operation
ref_109787 = (ref_108599 & 0xFFFFFFFF) # MOV operation
ref_109789 = ((ref_109787 & 0xFFFFFFFF) ^ (ref_109773 & 0xFFFFFFFF)) # XOR operation
ref_110578 = (ref_109789 & 0xFFFFFFFF) # MOV operation
ref_120982 = ref_297 # MOVZX operation
ref_121378 = (ref_120982 & 0xFF) # MOVZX operation
ref_121380 = (ref_121378 & 0xFF) # MOVZX operation
ref_122192 = (ref_110578 & 0xFFFFFFFF) # MOV operation
ref_122594 = (ref_122192 & 0xFFFFFFFF) # MOV operation
ref_122608 = (ref_121380 & 0xFFFFFFFF) # MOV operation
ref_122610 = (((ref_122608 & 0xFFFFFFFF) + (ref_122594 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_123454 = (ref_122610 & 0xFFFFFFFF) # MOV operation
ref_124610 = (ref_123454 & 0xFFFFFFFF) # MOV operation
ref_125075 = (ref_124610 & 0xFFFFFFFF) # MOV operation
ref_125093 = (((ref_125075 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_125100 = (ref_125093 & 0xFFFFFFFF) # MOV operation
ref_125898 = (ref_123454 & 0xFFFFFFFF) # MOV operation
ref_126268 = (ref_125898 & 0xFFFFFFFF) # MOV operation
ref_126282 = (ref_125100 & 0xFFFFFFFF) # MOV operation
ref_126284 = (((ref_126282 & 0xFFFFFFFF) + (ref_126268 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_127068 = (ref_126284 & 0xFFFFFFFF) # MOV operation
ref_127866 = (ref_127068 & 0xFFFFFFFF) # MOV operation
ref_128638 = (ref_127866 & 0xFFFFFFFF) # MOV operation
ref_128648 = ((ref_128638 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_128655 = (ref_128648 & 0xFFFFFFFF) # MOV operation
ref_129393 = (ref_127068 & 0xFFFFFFFF) # MOV operation
ref_129779 = (ref_129393 & 0xFFFFFFFF) # MOV operation
ref_129793 = (ref_128655 & 0xFFFFFFFF) # MOV operation
ref_129795 = ((ref_129793 & 0xFFFFFFFF) ^ (ref_129779 & 0xFFFFFFFF)) # XOR operation
ref_130596 = (ref_129795 & 0xFFFFFFFF) # MOV operation
ref_141000 = ref_296 # MOVZX operation
ref_141394 = (ref_141000 & 0xFF) # MOVZX operation
ref_141396 = (ref_141394 & 0xFF) # MOVZX operation
ref_142156 = (ref_130596 & 0xFFFFFFFF) # MOV operation
ref_142514 = (ref_142156 & 0xFFFFFFFF) # MOV operation
ref_142528 = (ref_141396 & 0xFFFFFFFF) # MOV operation
ref_142530 = (((ref_142528 & 0xFFFFFFFF) + (ref_142514 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_143418 = (ref_142530 & 0xFFFFFFFF) # MOV operation
ref_144686 = (ref_143418 & 0xFFFFFFFF) # MOV operation
ref_144984 = (ref_144686 & 0xFFFFFFFF) # MOV operation
ref_145002 = (((ref_144984 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_145009 = (ref_145002 & 0xFFFFFFFF) # MOV operation
ref_145894 = (ref_143418 & 0xFFFFFFFF) # MOV operation
ref_146220 = (ref_145894 & 0xFFFFFFFF) # MOV operation
ref_146234 = (ref_145009 & 0xFFFFFFFF) # MOV operation
ref_146236 = (((ref_146234 & 0xFFFFFFFF) + (ref_146220 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_147092 = (ref_146236 & 0xFFFFFFFF) # MOV operation
ref_147862 = (ref_147092 & 0xFFFFFFFF) # MOV operation
ref_148634 = (ref_147862 & 0xFFFFFFFF) # MOV operation
ref_148644 = ((ref_148634 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_148651 = (ref_148644 & 0xFFFFFFFF) # MOV operation
ref_149449 = (ref_147092 & 0xFFFFFFFF) # MOV operation
ref_149747 = (ref_149449 & 0xFFFFFFFF) # MOV operation
ref_149761 = (ref_148651 & 0xFFFFFFFF) # MOV operation
ref_149763 = ((ref_149761 & 0xFFFFFFFF) ^ (ref_149747 & 0xFFFFFFFF)) # XOR operation
ref_150602 = (ref_149763 & 0xFFFFFFFF) # MOV operation
ref_161006 = ref_295 # MOVZX operation
ref_161392 = (ref_161006 & 0xFF) # MOVZX operation
ref_161394 = (ref_161392 & 0xFF) # MOVZX operation
ref_162172 = (ref_150602 & 0xFFFFFFFF) # MOV operation
ref_162478 = (ref_162172 & 0xFFFFFFFF) # MOV operation
ref_162492 = (ref_161394 & 0xFFFFFFFF) # MOV operation
ref_162494 = (((ref_162492 & 0xFFFFFFFF) + (ref_162478 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_163338 = (ref_162494 & 0xFFFFFFFF) # MOV operation
ref_164606 = (ref_163338 & 0xFFFFFFFF) # MOV operation
ref_165008 = (ref_164606 & 0xFFFFFFFF) # MOV operation
ref_165026 = (((ref_165008 & 0xFFFFFFFF) << (0xA & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_165033 = (ref_165026 & 0xFFFFFFFF) # MOV operation
ref_165803 = (ref_163338 & 0xFFFFFFFF) # MOV operation
ref_166153 = (ref_165803 & 0xFFFFFFFF) # MOV operation
ref_166167 = (ref_165033 & 0xFFFFFFFF) # MOV operation
ref_166169 = (((ref_166167 & 0xFFFFFFFF) + (ref_166153 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_167044 = (ref_166169 & 0xFFFFFFFF) # MOV operation
ref_167886 = (ref_167044 & 0xFFFFFFFF) # MOV operation
ref_168630 = (ref_167886 & 0xFFFFFFFF) # MOV operation
ref_168640 = ((ref_168630 & 0xFFFFFFFF) >> (0x6 & 0x1F)) # SHR operation
ref_168647 = (ref_168640 & 0xFFFFFFFF) # MOV operation
ref_169445 = (ref_167044 & 0xFFFFFFFF) # MOV operation
ref_169771 = (ref_169445 & 0xFFFFFFFF) # MOV operation
ref_169785 = (ref_168647 & 0xFFFFFFFF) # MOV operation
ref_169787 = ((ref_169785 & 0xFFFFFFFF) ^ (ref_169771 & 0xFFFFFFFF)) # XOR operation
ref_170570 = (ref_169787 & 0xFFFFFFFF) # MOV operation
ref_175410 = (ref_170570 & 0xFFFFFFFF) # MOV operation
ref_175812 = (ref_175410 & 0xFFFFFFFF) # MOV operation
ref_175830 = (((ref_175812 & 0xFFFFFFFF) << (0x3 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_175837 = (ref_175830 & 0xFFFFFFFF) # MOV operation
ref_176555 = (ref_170570 & 0xFFFFFFFF) # MOV operation
ref_177020 = (ref_176555 & 0xFFFFFFFF) # MOV operation
ref_177034 = (ref_175837 & 0xFFFFFFFF) # MOV operation
ref_177036 = (((ref_177034 & 0xFFFFFFFF) + (ref_177020 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_177848 = (ref_177036 & 0xFFFFFFFF) # MOV operation
ref_178690 = (ref_177848 & 0xFFFFFFFF) # MOV operation
ref_179410 = (ref_178690 & 0xFFFFFFFF) # MOV operation
ref_179420 = ((ref_179410 & 0xFFFFFFFF) >> (0xB & 0x1F)) # SHR operation
ref_179427 = (ref_179420 & 0xFFFFFFFF) # MOV operation
ref_180173 = (ref_177848 & 0xFFFFFFFF) # MOV operation
ref_180575 = (ref_180173 & 0xFFFFFFFF) # MOV operation
ref_180589 = (ref_179427 & 0xFFFFFFFF) # MOV operation
ref_180591 = ((ref_180589 & 0xFFFFFFFF) ^ (ref_180575 & 0xFFFFFFFF)) # XOR operation
ref_181342 = (ref_180591 & 0xFFFFFFFF) # MOV operation
ref_182552 = (ref_181342 & 0xFFFFFFFF) # MOV operation
ref_182952 = (ref_182552 & 0xFFFFFFFF) # MOV operation
ref_182970 = (((ref_182952 & 0xFFFFFFFF) << (0xF & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_182977 = (ref_182970 & 0xFFFFFFFF) # MOV operation
ref_183755 = (ref_181342 & 0xFFFFFFFF) # MOV operation
ref_184113 = (ref_183755 & 0xFFFFFFFF) # MOV operation
ref_184127 = (ref_182977 & 0xFFFFFFFF) # MOV operation
ref_184129 = (((ref_184127 & 0xFFFFFFFF) + (ref_184113 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_185017 = (ref_184129 & 0xFFFFFFFF) # MOV operation
ref_186263 = (ref_185017 & 0xFFFFFFFF) # MOV operation
ref_186555 = (ref_186263 & 0xFFFFFFFF) # MOV operation
ref_186592 = (ref_186555 & 0xFFFFFFFF) # MOV operation
ref_186600 = (ref_186592 & 0xFFFFFFFF) # MOV operation
ref_186602 = (ref_186600 & 0xFFFFFFFF) # MOV operation

print(ref_186602 & 0xffffffffffffffff)
