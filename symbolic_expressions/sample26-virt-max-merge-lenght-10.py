#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_5500 = ref_278 # MOV operation
ref_5542 = ref_5500 # MOV operation
ref_5550 = (ref_5542 >> (0x5 & 0x3F)) # SHR operation
ref_5557 = ref_5550 # MOV operation
ref_5589 = ref_5557 # MOV operation
ref_5603 = (0x1376783EF7559EA & ref_5589) # AND operation
ref_5642 = ref_5603 # MOV operation
ref_5644 = ((ref_5642 >> 56) & 0xFF) # Byte reference - MOV operation
ref_5645 = ((ref_5642 >> 48) & 0xFF) # Byte reference - MOV operation
ref_5646 = ((ref_5642 >> 40) & 0xFF) # Byte reference - MOV operation
ref_5647 = ((ref_5642 >> 32) & 0xFF) # Byte reference - MOV operation
ref_5648 = ((ref_5642 >> 24) & 0xFF) # Byte reference - MOV operation
ref_5649 = ((ref_5642 >> 16) & 0xFF) # Byte reference - MOV operation
ref_5650 = ((ref_5642 >> 8) & 0xFF) # Byte reference - MOV operation
ref_5651 = (ref_5642 & 0xFF) # Byte reference - MOV operation
ref_6499 = ref_278 # MOV operation
ref_6541 = ref_6499 # MOV operation
ref_6547 = (0x1A5612E2 | ref_6541) # OR operation
ref_6904 = ref_5642 # MOV operation
ref_6936 = ref_6904 # MOV operation
ref_6950 = (0x7063FB7 & ref_6936) # AND operation
ref_6987 = ref_6547 # MOV operation
ref_6999 = ref_6950 # MOV operation
ref_7001 = ((ref_6999 + ref_6987) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_7041 = ref_7001 # MOV operation
ref_7043 = ((ref_7041 >> 56) & 0xFF) # Byte reference - MOV operation
ref_7044 = ((ref_7041 >> 48) & 0xFF) # Byte reference - MOV operation
ref_7045 = ((ref_7041 >> 40) & 0xFF) # Byte reference - MOV operation
ref_7046 = ((ref_7041 >> 32) & 0xFF) # Byte reference - MOV operation
ref_7047 = ((ref_7041 >> 24) & 0xFF) # Byte reference - MOV operation
ref_7048 = ((ref_7041 >> 16) & 0xFF) # Byte reference - MOV operation
ref_7049 = ((ref_7041 >> 8) & 0xFF) # Byte reference - MOV operation
ref_7050 = (ref_7041 & 0xFF) # Byte reference - MOV operation
ref_7809 = ref_7041 # MOV operation
ref_7859 = ref_7809 # MOV operation
ref_7873 = (ref_7859 >> (0x3 & 0x3F)) # SHR operation
ref_8002 = ref_7873 # MOV operation
ref_8016 = (0xF & ref_8002) # AND operation
ref_8063 = ref_8016 # MOV operation
ref_8069 = (0x1 | ref_8063) # OR operation
ref_8120 = ref_8069 # MOV operation
ref_8122 = ((0x3162E74F << ((ref_8120 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_8541 = ref_7041 # MOV operation
ref_8591 = ref_8541 # MOV operation
ref_8605 = (ref_8591 >> (0x3 & 0x3F)) # SHR operation
ref_8734 = ref_8605 # MOV operation
ref_8748 = (0xF & ref_8734) # AND operation
ref_8795 = ref_8748 # MOV operation
ref_8801 = (0x1 | ref_8795) # OR operation
ref_8852 = ref_8801 # MOV operation
ref_8854 = ((0x40 - ref_8852) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_8862 = ref_8854 # MOV operation
ref_8906 = ref_8862 # MOV operation
ref_8908 = (0x3162E74F >> ((ref_8906 & 0xFF) & 0x3F)) # SHR operation
ref_8945 = ref_8122 # MOV operation
ref_8957 = ref_8908 # MOV operation
ref_8959 = (ref_8957 | ref_8945) # OR operation
ref_9014 = ref_8959 # MOV operation
ref_9028 = (ref_9014 >> (0x4 & 0x3F)) # SHR operation
ref_9157 = ref_9028 # MOV operation
ref_9171 = (0x7 & ref_9157) # AND operation
ref_9218 = ref_9171 # MOV operation
ref_9224 = (0x1 | ref_9218) # OR operation
ref_9674 = ref_278 # MOV operation
ref_9706 = ref_9674 # MOV operation
ref_9720 = ((ref_9706 - 0x2907943) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_9728 = ref_9720 # MOV operation
ref_9760 = ref_9728 # MOV operation
ref_9772 = ref_9224 # MOV operation
ref_9774 = ((ref_9760 << ((ref_9772 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_9813 = ref_9774 # MOV operation
ref_10668 = ref_278 # MOV operation
ref_10700 = ref_10668 # MOV operation
ref_10714 = ((ref_10700 - 0x3C563FC) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_10722 = ref_10714 # MOV operation
ref_10756 = ref_10722 # MOV operation
ref_11918 = ref_10756 # MOV operation
ref_12506 = ref_7041 # MOV operation
ref_12538 = ref_12506 # MOV operation
ref_12552 = (0xF & ref_12538) # AND operation
ref_12589 = ref_12552 # MOV operation
ref_12603 = ((ref_12589 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_12640 = ref_11918 # MOV operation
ref_12652 = ref_12603 # MOV operation
ref_12654 = (ref_12652 | ref_12640) # OR operation
ref_12693 = ref_12654 # MOV operation
ref_13425 = ref_9813 # MOV operation
ref_13841 = ref_12693 # MOV operation
ref_13865 = ref_13841 # MOV operation
ref_13871 = (0x1F & ref_13865) # AND operation
ref_13894 = ref_13871 # MOV operation
ref_13908 = ((ref_13894 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_14045 = ref_13425 # MOV operation
ref_14049 = ref_13908 # MOV operation
ref_14051 = (ref_14049 | ref_14045) # OR operation
ref_14090 = ref_14051 # MOV operation
ref_14716 = ref_12693 # MOV operation
ref_15304 = ref_7041 # MOV operation
ref_15336 = ref_15304 # MOV operation
ref_15350 = (0xF & ref_15336) # AND operation
ref_15387 = ref_15350 # MOV operation
ref_15401 = ((ref_15387 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_15438 = ref_14716 # MOV operation
ref_15450 = ref_15401 # MOV operation
ref_15452 = (ref_15450 | ref_15438) # OR operation
ref_15491 = ref_15452 # MOV operation
ref_16875 = ref_15491 # MOV operation
ref_17463 = ref_15491 # MOV operation
ref_17495 = ref_17463 # MOV operation
ref_17509 = (0xF & ref_17495) # AND operation
ref_17546 = ref_17509 # MOV operation
ref_17560 = ((ref_17546 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_17597 = ref_16875 # MOV operation
ref_17609 = ref_17560 # MOV operation
ref_17611 = (ref_17609 | ref_17597) # OR operation
ref_17650 = ref_17611 # MOV operation
ref_18382 = ref_14090 # MOV operation
ref_18798 = ref_17650 # MOV operation
ref_18822 = ref_18798 # MOV operation
ref_18828 = (0x1F & ref_18822) # AND operation
ref_18851 = ref_18828 # MOV operation
ref_18865 = ((ref_18851 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_19002 = ref_18382 # MOV operation
ref_19006 = ref_18865 # MOV operation
ref_19008 = (ref_19006 | ref_19002) # OR operation
ref_19047 = ref_19008 # MOV operation
ref_19049 = ((ref_19047 >> 56) & 0xFF) # Byte reference - MOV operation
ref_19050 = ((ref_19047 >> 48) & 0xFF) # Byte reference - MOV operation
ref_19051 = ((ref_19047 >> 40) & 0xFF) # Byte reference - MOV operation
ref_19052 = ((ref_19047 >> 32) & 0xFF) # Byte reference - MOV operation
ref_19053 = ((ref_19047 >> 24) & 0xFF) # Byte reference - MOV operation
ref_19054 = ((ref_19047 >> 16) & 0xFF) # Byte reference - MOV operation
ref_19055 = ((ref_19047 >> 8) & 0xFF) # Byte reference - MOV operation
ref_19056 = (ref_19047 & 0xFF) # Byte reference - MOV operation
ref_19673 = ref_17650 # MOV operation
ref_20261 = ref_17650 # MOV operation
ref_20293 = ref_20261 # MOV operation
ref_20307 = (0xF & ref_20293) # AND operation
ref_20344 = ref_20307 # MOV operation
ref_20358 = ((ref_20344 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_20395 = ref_19673 # MOV operation
ref_20407 = ref_20358 # MOV operation
ref_20409 = (ref_20407 | ref_20395) # OR operation
ref_20448 = ref_20409 # MOV operation
ref_23966 = ref_20448 # MOV operation
ref_24382 = ref_19047 # MOV operation
ref_24762 = ref_19047 # MOV operation
ref_24778 = ref_24382 # MOV operation
ref_24790 = ref_24762 # MOV operation
ref_24792 = ((ref_24790 + ref_24778) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_24816 = ref_24792 # MOV operation
ref_24830 = (0x7 & ref_24816) # AND operation
ref_24959 = ref_24830 # MOV operation
ref_24973 = ((ref_24959 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_25010 = ref_23966 # MOV operation
ref_25022 = ref_24973 # MOV operation
ref_25024 = (ref_25022 | ref_25010) # OR operation
ref_25063 = ref_25024 # MOV operation
ref_25587 = ((((ref_19049) << 8 | ref_19050) << 8 | ref_19051) << 8 | ref_19052) # MOV operation
ref_25653 = (ref_25587 & 0xFFFFFFFF) # MOV operation
ref_26279 = ((((ref_19053) << 8 | ref_19054) << 8 | ref_19055) << 8 | ref_19056) # MOV operation
ref_26893 = (ref_26279 & 0xFFFFFFFF) # MOV operation
ref_26895 = (((ref_26893 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_26896 = (((ref_26893 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_26897 = (((ref_26893 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_26898 = ((ref_26893 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_26961 = (ref_25653 & 0xFFFFFFFF) # MOV operation
ref_27595 = (ref_26961 & 0xFFFFFFFF) # MOV operation
ref_27597 = (((ref_27595 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_27598 = (((ref_27595 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_27599 = (((ref_27595 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_27600 = ((ref_27595 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_28265 = ref_5646 # MOVZX operation
ref_28283 = (ref_28265 & 0xFF) # MOVZX operation
ref_29497 = ref_5647 # MOVZX operation
ref_29515 = (ref_29497 & 0xFF) # MOVZX operation
ref_29517 = (ref_29515 & 0xFF) # Byte reference - MOV operation
ref_30191 = (ref_28283 & 0xFF) # MOVZX operation
ref_30209 = (ref_30191 & 0xFF) # MOVZX operation
ref_30211 = (ref_30209 & 0xFF) # Byte reference - MOV operation
ref_30847 = ref_5645 # MOVZX operation
ref_30865 = (ref_30847 & 0xFF) # MOVZX operation
ref_32079 = ref_5651 # MOVZX operation
ref_32097 = (ref_32079 & 0xFF) # MOVZX operation
ref_32099 = (ref_32097 & 0xFF) # Byte reference - MOV operation
ref_32773 = (ref_30865 & 0xFF) # MOVZX operation
ref_32791 = (ref_32773 & 0xFF) # MOVZX operation
ref_32793 = (ref_32791 & 0xFF) # Byte reference - MOV operation
ref_33413 = ((((ref_7047) << 8 | ref_7048) << 8 | ref_7049) << 8 | ref_7050) # MOV operation
ref_33479 = (ref_33413 & 0xFFFFFFFF) # MOV operation
ref_34105 = ((((ref_7043) << 8 | ref_7044) << 8 | ref_7045) << 8 | ref_7046) # MOV operation
ref_34719 = (ref_34105 & 0xFFFFFFFF) # MOV operation
ref_34721 = (((ref_34719 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_34722 = (((ref_34719 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_34723 = (((ref_34719 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_34724 = ((ref_34719 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_34787 = (ref_33479 & 0xFFFFFFFF) # MOV operation
ref_35421 = (ref_34787 & 0xFFFFFFFF) # MOV operation
ref_35423 = (((ref_35421 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_35424 = (((ref_35421 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_35425 = (((ref_35421 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_35426 = ((ref_35421 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_36799 = ((((((((ref_35423) << 8 | ref_35424) << 8 | ref_35425) << 8 | ref_35426) << 8 | ref_34721) << 8 | ref_34722) << 8 | ref_34723) << 8 | ref_34724) # MOV operation
ref_37387 = ((((((((ref_5644) << 8 | ref_32099) << 8 | ref_29517) << 8 | ref_30211) << 8 | ref_5648) << 8 | ref_5649) << 8 | ref_5650) << 8 | ref_32793) # MOV operation
ref_37419 = ref_37387 # MOV operation
ref_37433 = (0x3F & ref_37419) # AND operation
ref_37470 = ref_37433 # MOV operation
ref_37484 = ((ref_37470 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_37521 = ref_36799 # MOV operation
ref_37533 = ref_37484 # MOV operation
ref_37535 = (ref_37533 | ref_37521) # OR operation
ref_37574 = ref_37535 # MOV operation
ref_39128 = ((((((((ref_26895) << 8 | ref_26896) << 8 | ref_26897) << 8 | ref_26898) << 8 | ref_27597) << 8 | ref_27598) << 8 | ref_27599) << 8 | ref_27600) # MOV operation
ref_39544 = ref_25063 # MOV operation
ref_39890 = ref_37574 # MOV operation
ref_39924 = ref_39890 # MOV operation
ref_39938 = (ref_39924 >> (0x3 & 0x3F)) # SHR operation
ref_40047 = ref_39938 # MOV operation
ref_40061 = (0xF & ref_40047) # AND operation
ref_40108 = ref_40061 # MOV operation
ref_40114 = (0x1 | ref_40108) # OR operation
ref_40151 = ref_39544 # MOV operation
ref_40163 = ref_40114 # MOV operation
ref_40165 = (ref_40151 >> ((ref_40163 & 0xFF) & 0x3F)) # SHR operation
ref_40494 = ref_37574 # MOV operation
ref_40528 = ref_40494 # MOV operation
ref_40542 = (ref_40528 >> (0x3 & 0x3F)) # SHR operation
ref_40651 = ref_40542 # MOV operation
ref_40665 = (0xF & ref_40651) # AND operation
ref_40712 = ref_40665 # MOV operation
ref_40718 = (0x1 | ref_40712) # OR operation
ref_40769 = ref_40718 # MOV operation
ref_40771 = ((0x40 - ref_40769) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_40779 = ref_40771 # MOV operation
ref_41159 = ref_25063 # MOV operation
ref_41183 = ref_41159 # MOV operation
ref_41187 = ref_40779 # MOV operation
ref_41189 = (ref_41187 & 0xFFFFFFFF) # MOV operation
ref_41191 = ((ref_41183 << ((ref_41189 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_41198 = ref_41191 # MOV operation
ref_41224 = ref_40165 # MOV operation
ref_41228 = ref_41198 # MOV operation
ref_41230 = (ref_41228 | ref_41224) # OR operation
ref_41359 = ref_41230 # MOV operation
ref_41373 = (0xF & ref_41359) # AND operation
ref_41410 = ref_41373 # MOV operation
ref_41424 = ((ref_41410 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_41461 = ref_39128 # MOV operation
ref_41473 = ref_41424 # MOV operation
ref_41475 = (ref_41473 | ref_41461) # OR operation
ref_41514 = ref_41475 # MOV operation
ref_42268 = ref_37574 # MOV operation
ref_42302 = ref_42268 # MOV operation
ref_42316 = (ref_42302 >> (0x3 & 0x3F)) # SHR operation
ref_42425 = ref_42316 # MOV operation
ref_42439 = (0x7 & ref_42425) # AND operation
ref_42486 = ref_42439 # MOV operation
ref_42492 = (0x1 | ref_42486) # OR operation
ref_42877 = ((((((((ref_5644) << 8 | ref_32099) << 8 | ref_29517) << 8 | ref_30211) << 8 | ref_5648) << 8 | ref_5649) << 8 | ref_5650) << 8 | ref_32793) # MOV operation
ref_42901 = ref_42877 # MOV operation
ref_42905 = ref_42492 # MOV operation
ref_42907 = (ref_42905 & 0xFFFFFFFF) # MOV operation
ref_42909 = ((ref_42901 << ((ref_42907 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_42916 = ref_42909 # MOV operation
ref_43276 = ref_41514 # MOV operation
ref_43656 = ref_25063 # MOV operation
ref_43672 = ref_43276 # MOV operation
ref_43684 = ref_43656 # MOV operation
ref_43686 = (ref_43684 | ref_43672) # OR operation
ref_43803 = ref_42916 # MOV operation
ref_43807 = ref_43686 # MOV operation
ref_43809 = (ref_43807 | ref_43803) # OR operation
ref_43848 = ref_43809 # MOV operation
ref_44075 = ref_43848 # MOV operation
ref_44077 = ref_44075 # MOV operation

print(ref_44077 & 0xffffffffffffffff)
