#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])

ref_9275 = SymVar_0
ref_9290 = ref_9275 # MOV operation
ref_17335 = ref_9290 # MOV operation
ref_17777 = ref_17335 # MOV operation
ref_17785 = (0x1D2C27F0 | ref_17777) # OR operation
ref_18007 = ref_17785 # MOV operation
ref_18025 = ((ref_18007 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_18032 = ref_18025 # MOV operation
ref_19835 = ref_9290 # MOV operation
ref_20277 = ref_19835 # MOV operation
ref_20285 = (0x1D2C27F0 | ref_20277) # OR operation
ref_20750 = ref_20285 # MOV operation
ref_20760 = (ref_20750 >> (0x37 & 0x3F)) # SHR operation
ref_20767 = ref_20760 # MOV operation
ref_20992 = ref_18032 # MOV operation
ref_20998 = ref_20767 # MOV operation
ref_21000 = (ref_20998 | ref_20992) # OR operation
ref_21230 = ref_21000 # MOV operation
ref_24700 = ref_9290 # MOV operation
ref_26801 = ref_21230 # MOV operation
ref_27000 = ref_26801 # MOV operation
ref_27018 = ((ref_27000 << (0xD & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_27025 = ref_27018 # MOV operation
ref_28909 = ref_21230 # MOV operation
ref_29351 = ref_28909 # MOV operation
ref_29361 = (ref_29351 >> (0x33 & 0x3F)) # SHR operation
ref_29368 = ref_29361 # MOV operation
ref_29593 = ref_27025 # MOV operation
ref_29599 = ref_29368 # MOV operation
ref_29601 = (ref_29599 | ref_29593) # OR operation
ref_29831 = ref_24700 # MOV operation
ref_29837 = ref_29601 # MOV operation
ref_29839 = (ref_29837 | ref_29831) # OR operation
ref_30069 = ref_29839 # MOV operation
ref_33774 = ref_9290 # MOV operation
ref_33973 = ref_33774 # MOV operation
ref_33989 = ((0x6402BE2 + ref_33973) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_34220 = ref_33989 # MOV operation
ref_37690 = ref_9290 # MOV operation
ref_38132 = ref_37690 # MOV operation
ref_38140 = (0x3544223F | ref_38132) # OR operation
ref_40264 = ref_34220 # MOV operation
ref_42130 = ref_30069 # MOV operation
ref_42337 = ref_40264 # MOV operation
ref_42343 = ref_42130 # MOV operation
ref_42345 = (((sx(0x40, ref_42343) * sx(0x40, ref_42337)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_42578 = ref_42345 # MOV operation
ref_42580 = (((sx(0x40, ref_42578) * sx(0x40, 0x3BE31211)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_42807 = ref_38140 # MOV operation
ref_42813 = ref_42580 # MOV operation
ref_42815 = (((sx(0x40, ref_42813) * sx(0x40, ref_42807)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_43042 = ref_42815 # MOV operation
ref_46593 = ref_34220 # MOV operation
ref_48929 = ref_43042 # MOV operation
ref_49128 = ref_48929 # MOV operation
ref_49144 = (0x1F & ref_49128) # AND operation
ref_49366 = ref_49144 # MOV operation
ref_49384 = ((ref_49366 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_49391 = ref_49384 # MOV operation
ref_49616 = ref_46593 # MOV operation
ref_49622 = ref_49391 # MOV operation
ref_49624 = (ref_49622 | ref_49616) # OR operation
ref_49854 = ref_49624 # MOV operation
ref_52189 = ref_30069 # MOV operation
ref_52631 = ref_52189 # MOV operation
ref_52641 = (ref_52631 >> (0x1 & 0x3F)) # SHR operation
ref_52648 = ref_52641 # MOV operation
ref_52865 = ref_52648 # MOV operation
ref_52881 = (0xF & ref_52865) # AND operation
ref_53346 = ref_52881 # MOV operation
ref_53354 = (0x1 | ref_53346) # OR operation
ref_55243 = ref_21230 # MOV operation
ref_55442 = ref_55243 # MOV operation
ref_55456 = ref_53354 # MOV operation
ref_55458 = (ref_55456 & 0xFFFFFFFF) # MOV operation
ref_55460 = ((ref_55442 << ((ref_55458 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_55467 = ref_55460 # MOV operation
ref_57351 = ref_21230 # MOV operation
ref_59452 = ref_30069 # MOV operation
ref_59894 = ref_59452 # MOV operation
ref_59904 = (ref_59894 >> (0x1 & 0x3F)) # SHR operation
ref_59911 = ref_59904 # MOV operation
ref_60128 = ref_59911 # MOV operation
ref_60144 = (0xF & ref_60128) # AND operation
ref_60609 = ref_60144 # MOV operation
ref_60617 = (0x1 | ref_60609) # OR operation
ref_61088 = ref_60617 # MOV operation
ref_61090 = ((0x40 - ref_61088) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_61098 = ref_61090 # MOV operation
ref_61323 = ref_57351 # MOV operation
ref_61329 = ref_61098 # MOV operation
ref_61331 = (ref_61329 & 0xFFFFFFFF) # MOV operation
ref_61333 = (ref_61323 >> ((ref_61331 & 0xFF) & 0x3F)) # SHR operation
ref_61340 = ref_61333 # MOV operation
ref_61565 = ref_55467 # MOV operation
ref_61571 = ref_61340 # MOV operation
ref_61573 = (ref_61571 | ref_61565) # OR operation
ref_63462 = ref_49854 # MOV operation
ref_65563 = ref_43042 # MOV operation
ref_66005 = ref_65563 # MOV operation
ref_66015 = (ref_66005 >> (0x3 & 0x3F)) # SHR operation
ref_66022 = ref_66015 # MOV operation
ref_66239 = ref_66022 # MOV operation
ref_66255 = (0x7 & ref_66239) # AND operation
ref_66720 = ref_66255 # MOV operation
ref_66728 = (0x1 | ref_66720) # OR operation
ref_66958 = ref_63462 # MOV operation
ref_66964 = ref_66728 # MOV operation
ref_66966 = (ref_66964 & 0xFFFFFFFF) # MOV operation
ref_66968 = (ref_66958 >> ((ref_66966 & 0xFF) & 0x3F)) # SHR operation
ref_66975 = ref_66968 # MOV operation
ref_67200 = ref_61573 # MOV operation
ref_67206 = ref_66975 # MOV operation
ref_67208 = ((ref_67200 - ref_67206) & 0xFFFFFFFFFFFFFFFF) # CMP operation
ref_67210 = ((((ref_67200 ^ (ref_67206 ^ ref_67208)) ^ ((ref_67200 ^ ref_67208) & (ref_67200 ^ ref_67206))) >> 63) & 0x1) # Carry flag
ref_67214 = (0x1 if (ref_67208 == 0x0) else 0x0) # Zero flag
ref_67216 = ((((ref_67206 >> 8) & 0xFFFFFFFFFFFFFF)) << 8 | (0x1 if ((ref_67210 | ref_67214) == 0x1) else 0x0)) # SETBE operation
ref_67218 = (ref_67216 & 0xFF) # MOVZX operation
ref_67425 = (ref_67218 & 0xFFFFFFFF) # MOV operation
ref_67427 = ((ref_67425 & 0xFFFFFFFF) & (ref_67425 & 0xFFFFFFFF)) # TEST operation
ref_67432 = (0x1 if (ref_67427 == 0x0) else 0x0) # Zero flag
ref_67434 = (0x51E8 if (ref_67432 == 0x1) else 0x51C6) # Program Counter


if (ref_67432 == 0x1):
    ref_9275 = SymVar_0
    ref_9290 = ref_9275 # MOV operation
    ref_17335 = ref_9290 # MOV operation
    ref_17777 = ref_17335 # MOV operation
    ref_17785 = (0x1D2C27F0 | ref_17777) # OR operation
    ref_18007 = ref_17785 # MOV operation
    ref_18025 = ((ref_18007 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_18032 = ref_18025 # MOV operation
    ref_19835 = ref_9290 # MOV operation
    ref_20277 = ref_19835 # MOV operation
    ref_20285 = (0x1D2C27F0 | ref_20277) # OR operation
    ref_20750 = ref_20285 # MOV operation
    ref_20760 = (ref_20750 >> (0x37 & 0x3F)) # SHR operation
    ref_20767 = ref_20760 # MOV operation
    ref_20992 = ref_18032 # MOV operation
    ref_20998 = ref_20767 # MOV operation
    ref_21000 = (ref_20998 | ref_20992) # OR operation
    ref_21230 = ref_21000 # MOV operation
    ref_24700 = ref_9290 # MOV operation
    ref_26801 = ref_21230 # MOV operation
    ref_27000 = ref_26801 # MOV operation
    ref_27018 = ((ref_27000 << (0xD & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_27025 = ref_27018 # MOV operation
    ref_28909 = ref_21230 # MOV operation
    ref_29351 = ref_28909 # MOV operation
    ref_29361 = (ref_29351 >> (0x33 & 0x3F)) # SHR operation
    ref_29368 = ref_29361 # MOV operation
    ref_29593 = ref_27025 # MOV operation
    ref_29599 = ref_29368 # MOV operation
    ref_29601 = (ref_29599 | ref_29593) # OR operation
    ref_29831 = ref_24700 # MOV operation
    ref_29837 = ref_29601 # MOV operation
    ref_29839 = (ref_29837 | ref_29831) # OR operation
    ref_30069 = ref_29839 # MOV operation
    ref_33774 = ref_9290 # MOV operation
    ref_33973 = ref_33774 # MOV operation
    ref_33989 = ((0x6402BE2 + ref_33973) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_34220 = ref_33989 # MOV operation
    ref_37690 = ref_9290 # MOV operation
    ref_38132 = ref_37690 # MOV operation
    ref_38140 = (0x3544223F | ref_38132) # OR operation
    ref_40264 = ref_34220 # MOV operation
    ref_42130 = ref_30069 # MOV operation
    ref_42337 = ref_40264 # MOV operation
    ref_42343 = ref_42130 # MOV operation
    ref_42345 = (((sx(0x40, ref_42343) * sx(0x40, ref_42337)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_42578 = ref_42345 # MOV operation
    ref_42580 = (((sx(0x40, ref_42578) * sx(0x40, 0x3BE31211)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_42807 = ref_38140 # MOV operation
    ref_42813 = ref_42580 # MOV operation
    ref_42815 = (((sx(0x40, ref_42813) * sx(0x40, ref_42807)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_43042 = ref_42815 # MOV operation
    ref_46593 = ref_34220 # MOV operation
    ref_48929 = ref_43042 # MOV operation
    ref_49128 = ref_48929 # MOV operation
    ref_49144 = (0x1F & ref_49128) # AND operation
    ref_49366 = ref_49144 # MOV operation
    ref_49384 = ((ref_49366 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_49391 = ref_49384 # MOV operation
    ref_49616 = ref_46593 # MOV operation
    ref_49622 = ref_49391 # MOV operation
    ref_49624 = (ref_49622 | ref_49616) # OR operation
    ref_49854 = ref_49624 # MOV operation
    ref_71208 = ref_30069 # MOV operation
    ref_73544 = ref_30069 # MOV operation
    ref_73743 = ref_73544 # MOV operation
    ref_73759 = (0xF & ref_73743) # AND operation
    ref_73981 = ref_73759 # MOV operation
    ref_73999 = ((ref_73981 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_74006 = ref_73999 # MOV operation
    ref_74231 = ref_71208 # MOV operation
    ref_74237 = ref_74006 # MOV operation
    ref_74239 = (ref_74237 | ref_74231) # OR operation
    ref_74469 = ref_74239 # MOV operation
    ref_78399 = ref_74469 # MOV operation
    ref_78841 = ref_78399 # MOV operation
    ref_78851 = (ref_78841 >> (0x3 & 0x3F)) # SHR operation
    ref_78858 = ref_78851 # MOV operation
    ref_79075 = ref_78858 # MOV operation
    ref_79091 = (0xF & ref_79075) # AND operation
    ref_79556 = ref_79091 # MOV operation
    ref_79564 = (0x1 | ref_79556) # OR operation
    ref_81453 = ref_21230 # MOV operation
    ref_81652 = ref_81453 # MOV operation
    ref_81666 = ref_79564 # MOV operation
    ref_81668 = (ref_81666 & 0xFFFFFFFF) # MOV operation
    ref_81670 = ((ref_81652 << ((ref_81668 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_81677 = ref_81670 # MOV operation
    ref_83561 = ref_21230 # MOV operation
    ref_85662 = ref_74469 # MOV operation
    ref_86104 = ref_85662 # MOV operation
    ref_86114 = (ref_86104 >> (0x3 & 0x3F)) # SHR operation
    ref_86121 = ref_86114 # MOV operation
    ref_86338 = ref_86121 # MOV operation
    ref_86354 = (0xF & ref_86338) # AND operation
    ref_86819 = ref_86354 # MOV operation
    ref_86827 = (0x1 | ref_86819) # OR operation
    ref_87298 = ref_86827 # MOV operation
    ref_87300 = ((0x40 - ref_87298) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_87308 = ref_87300 # MOV operation
    ref_87533 = ref_83561 # MOV operation
    ref_87539 = ref_87308 # MOV operation
    ref_87541 = (ref_87539 & 0xFFFFFFFF) # MOV operation
    ref_87543 = (ref_87533 >> ((ref_87541 & 0xFF) & 0x3F)) # SHR operation
    ref_87550 = ref_87543 # MOV operation
    ref_87775 = ref_81677 # MOV operation
    ref_87781 = ref_87550 # MOV operation
    ref_87783 = (ref_87781 | ref_87775) # OR operation
    ref_89672 = ref_49854 # MOV operation
    ref_91773 = ref_43042 # MOV operation
    ref_91972 = ref_91773 # MOV operation
    ref_91988 = ((0x369A4780 + ref_91972) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_92219 = ref_89672 # MOV operation
    ref_92225 = ref_91988 # MOV operation
    ref_92227 = (((sx(0x40, ref_92225) * sx(0x40, ref_92219)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_92454 = ref_87783 # MOV operation
    ref_92460 = ref_92227 # MOV operation
    ref_92462 = (((sx(0x40, ref_92460) * sx(0x40, ref_92454)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_92689 = ref_92462 # MOV operation
    ref_93179 = ref_92689 # MOV operation
    ref_93181 = ref_93179 # MOV operation
    endb = ref_93181


else:
    ref_102513 = SymVar_0
    ref_102528 = ref_102513 # MOV operation
    ref_110578 = ref_102528 # MOV operation
    ref_111020 = ref_110578 # MOV operation
    ref_111028 = (0x1D2C27F0 | ref_111020) # OR operation
    ref_111250 = ref_111028 # MOV operation
    ref_111268 = ((ref_111250 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_111275 = ref_111268 # MOV operation
    ref_113078 = ref_102528 # MOV operation
    ref_113520 = ref_113078 # MOV operation
    ref_113528 = (0x1D2C27F0 | ref_113520) # OR operation
    ref_113993 = ref_113528 # MOV operation
    ref_114003 = (ref_113993 >> (0x37 & 0x3F)) # SHR operation
    ref_114010 = ref_114003 # MOV operation
    ref_114235 = ref_111275 # MOV operation
    ref_114241 = ref_114010 # MOV operation
    ref_114243 = (ref_114241 | ref_114235) # OR operation
    ref_114473 = ref_114243 # MOV operation
    ref_117943 = ref_102528 # MOV operation
    ref_120044 = ref_114473 # MOV operation
    ref_120243 = ref_120044 # MOV operation
    ref_120261 = ((ref_120243 << (0xD & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_120268 = ref_120261 # MOV operation
    ref_122152 = ref_114473 # MOV operation
    ref_122594 = ref_122152 # MOV operation
    ref_122604 = (ref_122594 >> (0x33 & 0x3F)) # SHR operation
    ref_122611 = ref_122604 # MOV operation
    ref_122836 = ref_120268 # MOV operation
    ref_122842 = ref_122611 # MOV operation
    ref_122844 = (ref_122842 | ref_122836) # OR operation
    ref_123074 = ref_117943 # MOV operation
    ref_123080 = ref_122844 # MOV operation
    ref_123082 = (ref_123080 | ref_123074) # OR operation
    ref_123312 = ref_123082 # MOV operation
    ref_123314 = ((ref_123312 >> 56) & 0xFF) # Byte reference - MOV operation
    ref_123315 = ((ref_123312 >> 48) & 0xFF) # Byte reference - MOV operation
    ref_123316 = ((ref_123312 >> 40) & 0xFF) # Byte reference - MOV operation
    ref_123317 = ((ref_123312 >> 32) & 0xFF) # Byte reference - MOV operation
    ref_123318 = ((ref_123312 >> 24) & 0xFF) # Byte reference - MOV operation
    ref_123319 = ((ref_123312 >> 16) & 0xFF) # Byte reference - MOV operation
    ref_123320 = ((ref_123312 >> 8) & 0xFF) # Byte reference - MOV operation
    ref_123321 = (ref_123312 & 0xFF) # Byte reference - MOV operation
    ref_127017 = ref_102528 # MOV operation
    ref_127216 = ref_127017 # MOV operation
    ref_127232 = ((0x6402BE2 + ref_127216) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_127463 = ref_127232 # MOV operation
    ref_130933 = ref_102528 # MOV operation
    ref_131375 = ref_130933 # MOV operation
    ref_131383 = (0x3544223F | ref_131375) # OR operation
    ref_133507 = ref_127463 # MOV operation
    ref_135373 = ref_123312 # MOV operation
    ref_135580 = ref_133507 # MOV operation
    ref_135586 = ref_135373 # MOV operation
    ref_135588 = (((sx(0x40, ref_135586) * sx(0x40, ref_135580)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_135821 = ref_135588 # MOV operation
    ref_135823 = (((sx(0x40, ref_135821) * sx(0x40, 0x3BE31211)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_136050 = ref_131383 # MOV operation
    ref_136056 = ref_135823 # MOV operation
    ref_136058 = (((sx(0x40, ref_136056) * sx(0x40, ref_136050)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_136285 = ref_136058 # MOV operation
    ref_139836 = ref_127463 # MOV operation
    ref_142172 = ref_136285 # MOV operation
    ref_142371 = ref_142172 # MOV operation
    ref_142387 = (0x1F & ref_142371) # AND operation
    ref_142609 = ref_142387 # MOV operation
    ref_142627 = ((ref_142609 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_142634 = ref_142627 # MOV operation
    ref_142859 = ref_139836 # MOV operation
    ref_142865 = ref_142634 # MOV operation
    ref_142867 = (ref_142865 | ref_142859) # OR operation
    ref_143097 = ref_142867 # MOV operation
    ref_164492 = ref_136285 # MOV operation
    ref_164691 = ref_164492 # MOV operation
    ref_164709 = ((((0x0) << 64 | ref_164691) / 0x8) & 0xFFFFFFFFFFFFFFFF) # DIV operation
    ref_164935 = ref_164709 # MOV operation
    ref_164937 = ((ref_164935 >> 56) & 0xFF) # Byte reference - MOV operation
    ref_164938 = ((ref_164935 >> 48) & 0xFF) # Byte reference - MOV operation
    ref_164939 = ((ref_164935 >> 40) & 0xFF) # Byte reference - MOV operation
    ref_164940 = ((ref_164935 >> 32) & 0xFF) # Byte reference - MOV operation
    ref_164941 = ((ref_164935 >> 24) & 0xFF) # Byte reference - MOV operation
    ref_164942 = ((ref_164935 >> 16) & 0xFF) # Byte reference - MOV operation
    ref_164943 = ((ref_164935 >> 8) & 0xFF) # Byte reference - MOV operation
    ref_164944 = (ref_164935 & 0xFF) # Byte reference - MOV operation
    ref_168155 = ref_123319 # MOVZX operation
    ref_168601 = (ref_168155 & 0xFF) # MOVZX operation
    ref_171813 = ref_123316 # MOVZX operation
    ref_175015 = (ref_171813 & 0xFF) # MOVZX operation
    ref_175017 = (ref_175015 & 0xFF) # Byte reference - MOV operation
    ref_175471 = (ref_168601 & 0xFF) # MOVZX operation
    ref_178673 = (ref_175471 & 0xFF) # MOVZX operation
    ref_178675 = (ref_178673 & 0xFF) # Byte reference - MOV operation
    ref_181885 = ref_123314 # MOVZX operation
    ref_182331 = (ref_181885 & 0xFF) # MOVZX operation
    ref_185543 = ref_123321 # MOVZX operation
    ref_188745 = (ref_185543 & 0xFF) # MOVZX operation
    ref_188747 = (ref_188745 & 0xFF) # Byte reference - MOV operation
    ref_189201 = (ref_182331 & 0xFF) # MOVZX operation
    ref_192403 = (ref_189201 & 0xFF) # MOVZX operation
    ref_192405 = (ref_192403 & 0xFF) # Byte reference - MOV operation
    ref_195615 = ref_164940 # MOVZX operation
    ref_196061 = (ref_195615 & 0xFF) # MOVZX operation
    ref_199273 = ref_164944 # MOVZX operation
    ref_202475 = (ref_199273 & 0xFF) # MOVZX operation
    ref_202477 = (ref_202475 & 0xFF) # Byte reference - MOV operation
    ref_202931 = (ref_196061 & 0xFF) # MOVZX operation
    ref_206133 = (ref_202931 & 0xFF) # MOVZX operation
    ref_206135 = (ref_206133 & 0xFF) # Byte reference - MOV operation
    ref_210055 = ((((((((ref_188747) << 8 | ref_123315) << 8 | ref_178675) << 8 | ref_123317) << 8 | ref_123318) << 8 | ref_175017) << 8 | ref_123320) << 8 | ref_192405) # MOV operation
    ref_210497 = ref_210055 # MOV operation
    ref_210507 = (ref_210497 >> (0x3 & 0x3F)) # SHR operation
    ref_210514 = ref_210507 # MOV operation
    ref_210731 = ref_210514 # MOV operation
    ref_210747 = (0xF & ref_210731) # AND operation
    ref_211212 = ref_210747 # MOV operation
    ref_211220 = (0x1 | ref_211212) # OR operation
    ref_213109 = ((((((((ref_164937) << 8 | ref_164938) << 8 | ref_164939) << 8 | ref_202477) << 8 | ref_164941) << 8 | ref_164942) << 8 | ref_164943) << 8 | ref_206135) # MOV operation
    ref_213308 = ref_213109 # MOV operation
    ref_213322 = ref_211220 # MOV operation
    ref_213324 = (ref_213322 & 0xFFFFFFFF) # MOV operation
    ref_213326 = ((ref_213308 << ((ref_213324 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_213333 = ref_213326 # MOV operation
    ref_215217 = ((((((((ref_164937) << 8 | ref_164938) << 8 | ref_164939) << 8 | ref_202477) << 8 | ref_164941) << 8 | ref_164942) << 8 | ref_164943) << 8 | ref_206135) # MOV operation
    ref_217318 = ((((((((ref_188747) << 8 | ref_123315) << 8 | ref_178675) << 8 | ref_123317) << 8 | ref_123318) << 8 | ref_175017) << 8 | ref_123320) << 8 | ref_192405) # MOV operation
    ref_217760 = ref_217318 # MOV operation
    ref_217770 = (ref_217760 >> (0x3 & 0x3F)) # SHR operation
    ref_217777 = ref_217770 # MOV operation
    ref_217994 = ref_217777 # MOV operation
    ref_218010 = (0xF & ref_217994) # AND operation
    ref_218475 = ref_218010 # MOV operation
    ref_218483 = (0x1 | ref_218475) # OR operation
    ref_218954 = ref_218483 # MOV operation
    ref_218956 = ((0x40 - ref_218954) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_218964 = ref_218956 # MOV operation
    ref_219189 = ref_215217 # MOV operation
    ref_219195 = ref_218964 # MOV operation
    ref_219197 = (ref_219195 & 0xFFFFFFFF) # MOV operation
    ref_219199 = (ref_219189 >> ((ref_219197 & 0xFF) & 0x3F)) # SHR operation
    ref_219206 = ref_219199 # MOV operation
    ref_219431 = ref_213333 # MOV operation
    ref_219437 = ref_219206 # MOV operation
    ref_219439 = (ref_219437 | ref_219431) # OR operation
    ref_221328 = ref_143097 # MOV operation
    ref_223429 = ref_136285 # MOV operation
    ref_223628 = ref_223429 # MOV operation
    ref_223644 = ((0x369A4780 + ref_223628) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_223875 = ref_221328 # MOV operation
    ref_223881 = ref_223644 # MOV operation
    ref_223883 = (((sx(0x40, ref_223881) * sx(0x40, ref_223875)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_224110 = ref_219439 # MOV operation
    ref_224116 = ref_223883 # MOV operation
    ref_224118 = (((sx(0x40, ref_224116) * sx(0x40, ref_224110)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
    ref_224345 = ref_224118 # MOV operation
    ref_224835 = ref_224345 # MOV operation
    ref_224837 = ref_224835 # MOV operation
    endb = ref_224837


print(endb & 0xffffffffffffffff)
