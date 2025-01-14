#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_75299 = ref_278 # MOV operation
ref_75499 = ref_75299 # MOV operation
ref_75507 = ((ref_75499 << (0x3D & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_75514 = ref_75507 # MOV operation
ref_76347 = ref_278 # MOV operation
ref_76547 = ref_76347 # MOV operation
ref_76555 = (ref_76547 >> (0x3 & 0x3F)) # SHR operation
ref_76562 = ref_76555 # MOV operation
ref_76658 = ref_76562 # MOV operation
ref_76670 = ref_75514 # MOV operation
ref_76672 = (ref_76670 | ref_76658) # OR operation
ref_76773 = ref_76672 # MOV operation
ref_76787 = ((ref_76773 - 0x3FEFFF7F) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_76795 = ref_76787 # MOV operation
ref_77721 = ref_76795 # MOV operation
ref_77723 = ((ref_77721 >> 56) & 0xFF) # Byte reference - MOV operation
ref_77724 = ((ref_77721 >> 48) & 0xFF) # Byte reference - MOV operation
ref_77725 = ((ref_77721 >> 40) & 0xFF) # Byte reference - MOV operation
ref_77726 = ((ref_77721 >> 32) & 0xFF) # Byte reference - MOV operation
ref_77727 = ((ref_77721 >> 24) & 0xFF) # Byte reference - MOV operation
ref_77728 = ((ref_77721 >> 16) & 0xFF) # Byte reference - MOV operation
ref_77729 = ((ref_77721 >> 8) & 0xFF) # Byte reference - MOV operation
ref_77730 = (ref_77721 & 0xFF) # Byte reference - MOV operation
ref_78755 = ref_77721 # MOV operation
ref_79568 = ref_278 # MOV operation
ref_79644 = ref_79568 # MOV operation
ref_79656 = ref_78755 # MOV operation
ref_79658 = (ref_79656 | ref_79644) # OR operation
ref_79759 = ref_79658 # MOV operation
ref_79773 = ((ref_79759 - 0x11E59B96) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_79781 = ref_79773 # MOV operation
ref_80707 = ref_79781 # MOV operation
ref_80709 = ((ref_80707 >> 56) & 0xFF) # Byte reference - MOV operation
ref_80710 = ((ref_80707 >> 48) & 0xFF) # Byte reference - MOV operation
ref_80711 = ((ref_80707 >> 40) & 0xFF) # Byte reference - MOV operation
ref_80712 = ((ref_80707 >> 32) & 0xFF) # Byte reference - MOV operation
ref_80713 = ((ref_80707 >> 24) & 0xFF) # Byte reference - MOV operation
ref_80714 = ((ref_80707 >> 16) & 0xFF) # Byte reference - MOV operation
ref_80715 = ((ref_80707 >> 8) & 0xFF) # Byte reference - MOV operation
ref_80716 = (ref_80707 & 0xFF) # Byte reference - MOV operation
ref_81540 = ref_278 # MOV operation
ref_82438 = ref_77721 # MOV operation
ref_82522 = ref_81540 # MOV operation
ref_82526 = ref_82438 # MOV operation
ref_82528 = (((sx(0x40, ref_82526) * sx(0x40, ref_82522)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_83448 = ref_80707 # MOV operation
ref_83648 = ref_83448 # MOV operation
ref_83656 = ((ref_83648 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_83663 = ref_83656 # MOV operation
ref_83767 = ref_82528 # MOV operation
ref_83771 = ref_83663 # MOV operation
ref_83773 = (((sx(0x40, ref_83771) * sx(0x40, ref_83767)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_84701 = ref_83773 # MOV operation
ref_85650 = ref_278 # MOV operation
ref_85726 = ref_85650 # MOV operation
ref_85740 = ((ref_85726 - 0x2000000007A4C37E) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_85748 = ref_85740 # MOV operation
ref_86674 = ref_85748 # MOV operation
ref_89271 = ((((ref_77723) << 8 | ref_77724) << 8 | ref_77725) << 8 | ref_77726) # MOV operation
ref_89479 = (ref_89271 & 0xFFFFFFFF) # MOV operation
ref_91087 = ((((ref_77727) << 8 | ref_77728) << 8 | ref_77729) << 8 | ref_77730) # MOV operation
ref_92683 = (ref_91087 & 0xFFFFFFFF) # MOV operation
ref_92685 = (((ref_92683 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_92686 = (((ref_92683 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_92687 = (((ref_92683 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_92688 = ((ref_92683 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_92903 = (ref_89479 & 0xFFFFFFFF) # MOV operation
ref_94499 = (ref_92903 & 0xFFFFFFFF) # MOV operation
ref_94501 = (((ref_94499 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_94502 = (((ref_94499 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_94503 = (((ref_94499 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_94504 = ((ref_94499 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_95733 = ref_84701 # MOV operation
ref_96631 = ref_84701 # MOV operation
ref_96715 = ref_95733 # MOV operation
ref_96719 = ref_96631 # MOV operation
ref_96721 = ((ref_96719 + ref_96715) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_96947 = ref_96721 # MOV operation
ref_96953 = (0x3F & ref_96947) # AND operation
ref_97178 = ref_96953 # MOV operation
ref_97186 = ((ref_97178 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_97193 = ref_97186 # MOV operation
ref_98199 = ((((((((ref_92685) << 8 | ref_92686) << 8 | ref_92687) << 8 | ref_92688) << 8 | ref_94501) << 8 | ref_94502) << 8 | ref_94503) << 8 | ref_94504) # MOV operation
ref_98275 = ref_98199 # MOV operation
ref_98287 = ref_97193 # MOV operation
ref_98289 = (ref_98287 | ref_98275) # OR operation
ref_99308 = ref_98289 # MOV operation
ref_102225 = ((((ref_80709) << 8 | ref_80710) << 8 | ref_80711) << 8 | ref_80712) # MOV operation
ref_102433 = (ref_102225 & 0xFFFFFFFF) # MOV operation
ref_104041 = ((((ref_80713) << 8 | ref_80714) << 8 | ref_80715) << 8 | ref_80716) # MOV operation
ref_105637 = (ref_104041 & 0xFFFFFFFF) # MOV operation
ref_105639 = (((ref_105637 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_105640 = (((ref_105637 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_105641 = (((ref_105637 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_105642 = ((ref_105637 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_105857 = (ref_102433 & 0xFFFFFFFF) # MOV operation
ref_107453 = (ref_105857 & 0xFFFFFFFF) # MOV operation
ref_107455 = (((ref_107453 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_107456 = (((ref_107453 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_107457 = (((ref_107453 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_107458 = ((ref_107453 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_108687 = ref_86674 # MOV operation
ref_109585 = ref_84701 # MOV operation
ref_109669 = ref_108687 # MOV operation
ref_109673 = ref_109585 # MOV operation
ref_109675 = ((ref_109673 + ref_109669) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_109901 = ref_109675 # MOV operation
ref_109907 = (0x3F & ref_109901) # AND operation
ref_110132 = ref_109907 # MOV operation
ref_110140 = ((ref_110132 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_110147 = ref_110140 # MOV operation
ref_111153 = ((((((((ref_105639) << 8 | ref_105640) << 8 | ref_105641) << 8 | ref_105642) << 8 | ref_107455) << 8 | ref_107456) << 8 | ref_107457) << 8 | ref_107458) # MOV operation
ref_111229 = ref_111153 # MOV operation
ref_111241 = ref_110147 # MOV operation
ref_111243 = (ref_111241 | ref_111229) # OR operation
ref_112262 = ref_111243 # MOV operation
ref_112264 = ((ref_112262 >> 56) & 0xFF) # Byte reference - MOV operation
ref_112265 = ((ref_112262 >> 48) & 0xFF) # Byte reference - MOV operation
ref_112266 = ((ref_112262 >> 40) & 0xFF) # Byte reference - MOV operation
ref_112267 = ((ref_112262 >> 32) & 0xFF) # Byte reference - MOV operation
ref_112268 = ((ref_112262 >> 24) & 0xFF) # Byte reference - MOV operation
ref_112269 = ((ref_112262 >> 16) & 0xFF) # Byte reference - MOV operation
ref_112270 = ((ref_112262 >> 8) & 0xFF) # Byte reference - MOV operation
ref_112271 = (ref_112262 & 0xFF) # Byte reference - MOV operation
ref_115380 = ref_112266 # MOVZX operation
ref_115456 = (ref_115380 & 0xFF) # MOVZX operation
ref_118400 = ref_112270 # MOVZX operation
ref_118476 = (ref_118400 & 0xFF) # MOVZX operation
ref_118478 = (ref_118476 & 0xFF) # Byte reference - MOV operation
ref_120120 = (ref_115456 & 0xFF) # MOVZX operation
ref_120196 = (ref_120120 & 0xFF) # MOVZX operation
ref_120198 = (ref_120196 & 0xFF) # Byte reference - MOV operation
ref_121106 = ref_99308 # MOV operation
ref_122004 = ((((((((ref_112264) << 8 | ref_112265) << 8 | ref_118478) << 8 | ref_112267) << 8 | ref_112268) << 8 | ref_112269) << 8 | ref_120198) << 8 | ref_112271) # MOV operation
ref_122088 = ref_121106 # MOV operation
ref_122092 = ref_122004 # MOV operation
ref_122094 = ((ref_122092 + ref_122088) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_123134 = ref_84701 # MOV operation
ref_124032 = ref_86674 # MOV operation
ref_124116 = ref_123134 # MOV operation
ref_124120 = ref_124032 # MOV operation
ref_124122 = (ref_124120 & ref_124116) # AND operation
ref_124347 = ref_124122 # MOV operation
ref_124353 = (0xF & ref_124347) # AND operation
ref_124454 = ref_124353 # MOV operation
ref_124468 = (0x1 | ref_124454) # OR operation
ref_124697 = ref_124468 # MOV operation
ref_124699 = ((0x40 - ref_124697) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_124707 = ref_124699 # MOV operation
ref_124811 = ref_122094 # MOV operation
ref_124815 = ref_124707 # MOV operation
ref_124817 = (ref_124815 & 0xFFFFFFFF) # MOV operation
ref_124819 = (ref_124811 >> ((ref_124817 & 0xFF) & 0x3F)) # SHR operation
ref_124826 = ref_124819 # MOV operation
ref_125744 = ref_99308 # MOV operation
ref_126642 = ((((((((ref_112264) << 8 | ref_112265) << 8 | ref_118478) << 8 | ref_112267) << 8 | ref_112268) << 8 | ref_112269) << 8 | ref_120198) << 8 | ref_112271) # MOV operation
ref_126726 = ref_125744 # MOV operation
ref_126730 = ref_126642 # MOV operation
ref_126732 = ((ref_126730 + ref_126726) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_127772 = ref_84701 # MOV operation
ref_128670 = ref_86674 # MOV operation
ref_128754 = ref_127772 # MOV operation
ref_128758 = ref_128670 # MOV operation
ref_128760 = (ref_128758 & ref_128754) # AND operation
ref_128985 = ref_128760 # MOV operation
ref_128991 = (0xF & ref_128985) # AND operation
ref_129092 = ref_128991 # MOV operation
ref_129106 = (0x1 | ref_129092) # OR operation
ref_129215 = ref_126732 # MOV operation
ref_129219 = ref_129106 # MOV operation
ref_129221 = (ref_129219 & 0xFFFFFFFF) # MOV operation
ref_129223 = ((ref_129215 << ((ref_129221 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_129230 = ref_129223 # MOV operation
ref_129326 = ref_129230 # MOV operation
ref_129338 = ref_124826 # MOV operation
ref_129340 = (ref_129338 | ref_129326) # OR operation
ref_130195 = ref_129340 # MOV operation
ref_130406 = ref_130195 # MOV operation
ref_130408 = ref_130406 # MOV operation

print(ref_130408 & 0xffffffffffffffff)
