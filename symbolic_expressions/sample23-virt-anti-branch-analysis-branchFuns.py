#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_269 = SymVar_0
ref_284 = ref_269 # MOV operation
ref_13217 = ref_284 # MOV operation
ref_14358 = ref_13217 # MOV operation
ref_14364 = ((0x3F22161B + ref_14358) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_19053 = ref_14364 # MOV operation
ref_25526 = ref_19053 # MOV operation
ref_26058 = ref_25526 # MOV operation
ref_26060 = (((sx(0x40, ref_26058) * sx(0x40, 0x378AED0A)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_26627 = ref_26060 # MOV operation
ref_26629 = (((sx(0x40, ref_26627) * sx(0x40, 0xDF2B78B)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_27804 = ref_26629 # MOV operation
ref_27812 = (ref_27804 >> (0x1 & 0x3F)) # SHR operation
ref_27819 = ref_27812 # MOV operation
ref_28376 = ref_27819 # MOV operation
ref_28390 = (0xF & ref_28376) # AND operation
ref_29652 = ref_28390 # MOV operation
ref_29658 = (0x1 | ref_29652) # OR operation
ref_35105 = ref_284 # MOV operation
ref_35567 = ref_35105 # MOV operation
ref_35581 = ((ref_35567 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_40447 = ref_284 # MOV operation
ref_41587 = ref_40447 # MOV operation
ref_41595 = (ref_41587 >> (0x39 & 0x3F)) # SHR operation
ref_41602 = ref_41595 # MOV operation
ref_42203 = ref_35581 # MOV operation
ref_42207 = ref_41602 # MOV operation
ref_42209 = (ref_42207 | ref_42203) # OR operation
ref_42696 = ref_42209 # MOV operation
ref_42708 = ref_29658 # MOV operation
ref_42710 = ((ref_42696 << ((ref_42708 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_48197 = ref_284 # MOV operation
ref_48659 = ref_48197 # MOV operation
ref_48673 = ((ref_48659 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_53539 = ref_284 # MOV operation
ref_54679 = ref_53539 # MOV operation
ref_54687 = (ref_54679 >> (0x39 & 0x3F)) # SHR operation
ref_54694 = ref_54687 # MOV operation
ref_55295 = ref_48673 # MOV operation
ref_55299 = ref_54694 # MOV operation
ref_55301 = (ref_55299 | ref_55295) # OR operation
ref_61779 = ref_19053 # MOV operation
ref_62311 = ref_61779 # MOV operation
ref_62313 = (((sx(0x40, ref_62311) * sx(0x40, 0x378AED0A)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_62880 = ref_62313 # MOV operation
ref_62882 = (((sx(0x40, ref_62880) * sx(0x40, 0xDF2B78B)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_64057 = ref_62882 # MOV operation
ref_64065 = (ref_64057 >> (0x1 & 0x3F)) # SHR operation
ref_64072 = ref_64065 # MOV operation
ref_64629 = ref_64072 # MOV operation
ref_64643 = (0xF & ref_64629) # AND operation
ref_65905 = ref_64643 # MOV operation
ref_65911 = (0x1 | ref_65905) # OR operation
ref_67077 = ref_65911 # MOV operation
ref_67079 = ((0x40 - ref_67077) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_67087 = ref_67079 # MOV operation
ref_67674 = ref_55301 # MOV operation
ref_67678 = ref_67087 # MOV operation
ref_67680 = (ref_67678 & 0xFFFFFFFF) # MOV operation
ref_67682 = (ref_67674 >> ((ref_67680 & 0xFF) & 0x3F)) # SHR operation
ref_67689 = ref_67682 # MOV operation
ref_68290 = ref_42710 # MOV operation
ref_68294 = ref_67689 # MOV operation
ref_68296 = (ref_68294 | ref_68290) # OR operation
ref_72966 = ref_68296 # MOV operation
ref_77787 = ref_284 # MOV operation
ref_82377 = ref_72966 # MOV operation
ref_83518 = ref_82377 # MOV operation
ref_83524 = ((0xAD6EED + ref_83518) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_84088 = ref_77787 # MOV operation
ref_84092 = ref_83524 # MOV operation
ref_84094 = ((ref_84092 + ref_84088) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_88783 = ref_84094 # MOV operation
ref_93604 = ref_284 # MOV operation
ref_98194 = ref_19053 # MOV operation
ref_98762 = ref_93604 # MOV operation
ref_98766 = ref_98194 # MOV operation
ref_98768 = (ref_98766 | ref_98762) # OR operation
ref_103383 = ref_72966 # MOV operation
ref_104524 = ref_103383 # MOV operation
ref_104530 = ((0x2B6B05ED + ref_104524) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_109164 = ref_88783 # MOV operation
ref_109688 = ref_109164 # MOV operation
ref_109700 = ref_104530 # MOV operation
ref_109702 = (ref_109700 & ref_109688) # AND operation
ref_110295 = ref_98768 # MOV operation
ref_110299 = ref_109702 # MOV operation
ref_110301 = ((ref_110299 + ref_110295) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_114990 = ref_110301 # MOV operation
ref_119600 = ref_114990 # MOV operation
ref_125432 = ref_88783 # MOV operation
ref_125956 = ref_125432 # MOV operation
ref_125970 = (0x3F & ref_125956) # AND operation
ref_126505 = ref_125970 # MOV operation
ref_126519 = ((ref_126505 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_127152 = ref_119600 # MOV operation
ref_127156 = ref_126519 # MOV operation
ref_127158 = (ref_127156 | ref_127152) # OR operation
ref_131828 = ref_127158 # MOV operation
ref_137059 = ref_72966 # MOV operation
ref_138199 = ref_137059 # MOV operation
ref_138207 = (ref_138199 >> (0x4 & 0x3F)) # SHR operation
ref_138214 = ref_138207 # MOV operation
ref_138771 = ref_138214 # MOV operation
ref_138785 = (0xF & ref_138771) # AND operation
ref_140047 = ref_138785 # MOV operation
ref_140053 = (0x1 | ref_140047) # OR operation
ref_144668 = ref_19053 # MOV operation
ref_145130 = ref_144668 # MOV operation
ref_145142 = ref_140053 # MOV operation
ref_145144 = ((ref_145130 << ((ref_145142 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_149799 = ref_19053 # MOV operation
ref_155010 = ref_72966 # MOV operation
ref_156150 = ref_155010 # MOV operation
ref_156158 = (ref_156150 >> (0x4 & 0x3F)) # SHR operation
ref_156165 = ref_156158 # MOV operation
ref_156722 = ref_156165 # MOV operation
ref_156736 = (0xF & ref_156722) # AND operation
ref_157998 = ref_156736 # MOV operation
ref_158004 = (0x1 | ref_157998) # OR operation
ref_159170 = ref_158004 # MOV operation
ref_159172 = ((0x40 - ref_159170) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_159180 = ref_159172 # MOV operation
ref_159767 = ref_149799 # MOV operation
ref_159771 = ref_159180 # MOV operation
ref_159773 = (ref_159771 & 0xFFFFFFFF) # MOV operation
ref_159775 = (ref_159767 >> ((ref_159773 & 0xFF) & 0x3F)) # SHR operation
ref_159782 = ref_159775 # MOV operation
ref_160383 = ref_145144 # MOV operation
ref_160387 = ref_159782 # MOV operation
ref_160389 = (ref_160387 | ref_160383) # OR operation
ref_165004 = ref_88783 # MOV operation
ref_169594 = ref_131828 # MOV operation
ref_170114 = ref_165004 # MOV operation
ref_170118 = ref_169594 # MOV operation
ref_170120 = ((ref_170118 + ref_170114) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_170692 = ref_160389 # MOV operation
ref_170696 = ref_170120 # MOV operation
ref_170698 = (((sx(0x40, ref_170696) * sx(0x40, ref_170692)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_175627 = ref_170698 # MOV operation
ref_176747 = ref_175627 # MOV operation
ref_176749 = ref_176747 # MOV operation

print(ref_176749 & 0xffffffffffffffff)
