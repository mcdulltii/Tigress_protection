#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_6813 = ref_278 # MOV operation
ref_7097 = ref_6813 # MOV operation
ref_7105 = ((ref_7097 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_7112 = ref_7105 # MOV operation
ref_8254 = ref_278 # MOV operation
ref_8493 = ref_8254 # MOV operation
ref_8501 = (ref_8493 >> (0x7 & 0x3F)) # SHR operation
ref_8508 = ref_8501 # MOV operation
ref_8637 = ref_8508 # MOV operation
ref_8649 = ref_7112 # MOV operation
ref_8651 = (ref_8649 | ref_8637) # OR operation
ref_8775 = ref_8651 # MOV operation
ref_11123 = ref_8775 # MOV operation
ref_11402 = ref_11123 # MOV operation
ref_11404 = ((ref_11402 + 0x2D4AF89B) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_11533 = ref_11404 # MOV operation
ref_11535 = (ref_11533 & 0x1D5ABF66) # AND operation
ref_12682 = ref_278 # MOV operation
ref_12966 = ref_12682 # MOV operation
ref_12974 = ((ref_12966 << (0x35 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_12981 = ref_12974 # MOV operation
ref_14123 = ref_278 # MOV operation
ref_14362 = ref_14123 # MOV operation
ref_14370 = (ref_14362 >> (0xB & 0x3F)) # SHR operation
ref_14377 = ref_14370 # MOV operation
ref_14506 = ref_14377 # MOV operation
ref_14518 = ref_12981 # MOV operation
ref_14520 = (ref_14518 | ref_14506) # OR operation
ref_14654 = ref_14520 # MOV operation
ref_14666 = ref_11535 # MOV operation
ref_14668 = ((ref_14654 - ref_14666) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_14676 = ref_14668 # MOV operation
ref_14795 = ref_14676 # MOV operation
ref_17121 = ref_278 # MOV operation
ref_17230 = ref_17121 # MOV operation
ref_17244 = ((ref_17230 - 0xE8D4346) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_17252 = ref_17244 # MOV operation
ref_17371 = ref_17252 # MOV operation
ref_19719 = ref_8775 # MOV operation
ref_19828 = ref_19719 # MOV operation
ref_19842 = ((0x20453EE3 + ref_19828) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_20990 = ref_278 # MOV operation
ref_21099 = ref_20990 # MOV operation
ref_21111 = ref_19842 # MOV operation
ref_21113 = ((ref_21099 - ref_21111) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_21121 = ref_21113 # MOV operation
ref_21240 = ref_21121 # MOV operation
ref_24927 = ref_8775 # MOV operation
ref_26508 = ref_17371 # MOV operation
ref_26617 = ref_26508 # MOV operation
ref_26629 = ref_24927 # MOV operation
ref_26631 = (ref_26629 | ref_26617) # OR operation
ref_26913 = ref_26631 # MOV operation
ref_26919 = (0x3F & ref_26913) # AND operation
ref_27228 = ref_26919 # MOV operation
ref_27236 = ((ref_27228 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_27243 = ref_27236 # MOV operation
ref_28537 = ref_8775 # MOV operation
ref_28646 = ref_28537 # MOV operation
ref_28658 = ref_27243 # MOV operation
ref_28660 = (ref_28658 | ref_28646) # OR operation
ref_28784 = ref_28660 # MOV operation
ref_31411 = ref_14795 # MOV operation
ref_32843 = ref_28784 # MOV operation
ref_33082 = ref_32843 # MOV operation
ref_33090 = (ref_33082 >> (0x1 & 0x3F)) # SHR operation
ref_33097 = ref_33090 # MOV operation
ref_33374 = ref_33097 # MOV operation
ref_33380 = (0xF & ref_33374) # AND operation
ref_33514 = ref_33380 # MOV operation
ref_33528 = (0x1 | ref_33514) # OR operation
ref_33832 = ref_33528 # MOV operation
ref_33834 = ((0x40 - ref_33832) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_33842 = ref_33834 # MOV operation
ref_33988 = ref_31411 # MOV operation
ref_33992 = ref_33842 # MOV operation
ref_33994 = (ref_33992 & 0xFFFFFFFF) # MOV operation
ref_33996 = ((ref_33988 << ((ref_33994 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_34003 = ref_33996 # MOV operation
ref_35167 = ref_14795 # MOV operation
ref_36599 = ref_28784 # MOV operation
ref_36838 = ref_36599 # MOV operation
ref_36846 = (ref_36838 >> (0x1 & 0x3F)) # SHR operation
ref_36853 = ref_36846 # MOV operation
ref_37130 = ref_36853 # MOV operation
ref_37136 = (0xF & ref_37130) # AND operation
ref_37270 = ref_37136 # MOV operation
ref_37284 = (0x1 | ref_37270) # OR operation
ref_37390 = ref_35167 # MOV operation
ref_37394 = ref_37284 # MOV operation
ref_37396 = (ref_37394 & 0xFFFFFFFF) # MOV operation
ref_37398 = (ref_37390 >> ((ref_37396 & 0xFF) & 0x3F)) # SHR operation
ref_37405 = ref_37398 # MOV operation
ref_37534 = ref_37405 # MOV operation
ref_37546 = ref_34003 # MOV operation
ref_37548 = (ref_37546 | ref_37534) # OR operation
ref_37672 = ref_37548 # MOV operation
ref_39862 = ref_21240 # MOV operation
ref_41443 = ref_37672 # MOV operation
ref_41552 = ref_41443 # MOV operation
ref_41564 = ref_39862 # MOV operation
ref_41566 = ((ref_41552 - ref_41564) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_41574 = ref_41566 # MOV operation
ref_41693 = ref_41574 # MOV operation
ref_45663 = ref_28784 # MOV operation
ref_46965 = ref_14795 # MOV operation
ref_47222 = ref_46965 # MOV operation
ref_47228 = (0xF & ref_47222) # AND operation
ref_47362 = ref_47228 # MOV operation
ref_47376 = (0x1 | ref_47362) # OR operation
ref_47680 = ref_47376 # MOV operation
ref_47682 = ((0x40 - ref_47680) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_47690 = ref_47682 # MOV operation
ref_47836 = ref_45663 # MOV operation
ref_47840 = ref_47690 # MOV operation
ref_47842 = (ref_47840 & 0xFFFFFFFF) # MOV operation
ref_47844 = ((ref_47836 << ((ref_47842 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_47851 = ref_47844 # MOV operation
ref_49015 = ref_28784 # MOV operation
ref_50317 = ref_14795 # MOV operation
ref_50574 = ref_50317 # MOV operation
ref_50580 = (0xF & ref_50574) # AND operation
ref_50714 = ref_50580 # MOV operation
ref_50728 = (0x1 | ref_50714) # OR operation
ref_50834 = ref_49015 # MOV operation
ref_50838 = ref_50728 # MOV operation
ref_50840 = (ref_50838 & 0xFFFFFFFF) # MOV operation
ref_50842 = (ref_50834 >> ((ref_50840 & 0xFF) & 0x3F)) # SHR operation
ref_50849 = ref_50842 # MOV operation
ref_50978 = ref_50849 # MOV operation
ref_50990 = ref_47851 # MOV operation
ref_50992 = (ref_50990 | ref_50978) # OR operation
ref_52319 = ref_21240 # MOV operation
ref_53463 = ref_41693 # MOV operation
ref_53572 = ref_53463 # MOV operation
ref_53584 = ref_52319 # MOV operation
ref_53586 = (ref_53584 | ref_53572) # OR operation
ref_53850 = ref_53586 # MOV operation
ref_53858 = (ref_53850 >> (0x1 & 0x3F)) # SHR operation
ref_53865 = ref_53858 # MOV operation
ref_54142 = ref_53865 # MOV operation
ref_54148 = (0x7 & ref_54142) # AND operation
ref_54282 = ref_54148 # MOV operation
ref_54296 = (0x1 | ref_54282) # OR operation
ref_54447 = ref_50992 # MOV operation
ref_54451 = ref_54296 # MOV operation
ref_54453 = (ref_54451 & 0xFFFFFFFF) # MOV operation
ref_54455 = ((ref_54447 << ((ref_54453 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_54462 = ref_54455 # MOV operation
ref_54581 = ref_54462 # MOV operation
ref_54813 = ref_54581 # MOV operation
ref_54815 = ref_54813 # MOV operation

print(ref_54815 & 0xffffffffffffffff)
