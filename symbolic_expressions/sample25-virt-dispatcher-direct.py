#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_12793 = ref_278 # MOV operation
ref_12837 = ref_12793 # MOV operation
ref_12851 = ((ref_12837 << (0xD & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_13517 = ref_278 # MOV operation
ref_13561 = ref_13517 # MOV operation
ref_13575 = (ref_13561 >> (0x33 & 0x3F)) # SHR operation
ref_13652 = ref_12851 # MOV operation
ref_13656 = ref_13575 # MOV operation
ref_13658 = (ref_13656 | ref_13652) # OR operation
ref_13735 = ref_13658 # MOV operation
ref_14994 = ref_278 # MOV operation
ref_15038 = ref_14994 # MOV operation
ref_15054 = ((((0x0) << 64 | ref_15038) / 0x6) & 0xFFFFFFFFFFFFFFFF) # DIV operation
ref_15211 = ref_15054 # MOV operation
ref_15217 = (((sx(0x40, 0xFA0000000002C90C) * sx(0x40, ref_15211)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_15291 = ref_15217 # MOV operation
ref_16551 = ref_13735 # MOV operation
ref_17193 = ref_15291 # MOV operation
ref_17245 = ref_16551 # MOV operation
ref_17249 = ref_17193 # MOV operation
ref_17251 = (ref_17249 | ref_17245) # OR operation
ref_17833 = ref_278 # MOV operation
ref_17877 = ref_17833 # MOV operation
ref_17889 = ref_17251 # MOV operation
ref_17891 = ((ref_17889 + ref_17877) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_17969 = ref_17891 # MOV operation
ref_19397 = ref_13735 # MOV operation
ref_19533 = ref_19397 # MOV operation
ref_19539 = ((ref_19533 - 0x2ED5CD7E) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_19547 = ref_19539 # MOV operation
ref_19623 = ref_19547 # MOV operation
ref_19625 = ((0x28E5FC28 - ref_19623) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_19633 = ref_19625 # MOV operation
ref_19697 = ref_19633 # MOV operation
ref_19711 = (ref_19697 >> (0x2 & 0x3F)) # SHR operation
ref_19872 = ref_19711 # MOV operation
ref_19878 = (0x7 & ref_19872) # AND operation
ref_20039 = ref_19878 # MOV operation
ref_20045 = (0x1 | ref_20039) # OR operation
ref_20712 = ref_15291 # MOV operation
ref_21269 = ref_278 # MOV operation
ref_21313 = ref_21269 # MOV operation
ref_21325 = ref_20712 # MOV operation
ref_21327 = ((ref_21325 + ref_21313) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_21397 = ref_21327 # MOV operation
ref_21409 = ref_20045 # MOV operation
ref_21411 = (ref_21397 >> ((ref_21409 & 0xFF) & 0x3F)) # SHR operation
ref_21488 = ref_21411 # MOV operation
ref_22832 = ref_21488 # MOV operation
ref_22876 = ref_22832 # MOV operation
ref_22890 = (ref_22876 >> (0x1 & 0x3F)) # SHR operation
ref_23051 = ref_22890 # MOV operation
ref_23057 = (0x7 & ref_23051) # AND operation
ref_23218 = ref_23057 # MOV operation
ref_23224 = (0x1 | ref_23218) # OR operation
ref_23891 = ref_21488 # MOV operation
ref_23935 = ref_23891 # MOV operation
ref_23947 = ref_23224 # MOV operation
ref_23949 = (ref_23935 >> ((ref_23947 & 0xFF) & 0x3F)) # SHR operation
ref_24026 = ref_23949 # MOV operation
ref_24028 = ((ref_24026 >> 56) & 0xFF) # Byte reference - MOV operation
ref_24029 = ((ref_24026 >> 48) & 0xFF) # Byte reference - MOV operation
ref_24030 = ((ref_24026 >> 40) & 0xFF) # Byte reference - MOV operation
ref_24031 = ((ref_24026 >> 32) & 0xFF) # Byte reference - MOV operation
ref_24032 = ((ref_24026 >> 24) & 0xFF) # Byte reference - MOV operation
ref_24033 = ((ref_24026 >> 16) & 0xFF) # Byte reference - MOV operation
ref_24034 = ((ref_24026 >> 8) & 0xFF) # Byte reference - MOV operation
ref_24035 = (ref_24026 & 0xFF) # Byte reference - MOV operation
ref_25997 = ref_17969 # MOV operation
ref_26779 = ref_13735 # MOV operation
ref_26915 = ref_26779 # MOV operation
ref_26921 = (0x7 & ref_26915) # AND operation
ref_26990 = ref_26921 # MOV operation
ref_27004 = ((ref_26990 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_27081 = ref_25997 # MOV operation
ref_27085 = ref_27004 # MOV operation
ref_27087 = (ref_27085 | ref_27081) # OR operation
ref_27164 = ref_27087 # MOV operation
ref_28336 = ((((ref_24028) << 8 | ref_24029) << 8 | ref_24030) << 8 | ref_24031) # MOV operation
ref_28384 = (ref_28336 & 0xFFFFFFFF) # MOV operation
ref_30468 = ((((ref_24032) << 8 | ref_24033) << 8 | ref_24034) << 8 | ref_24035) # MOV operation
ref_30516 = (ref_30468 & 0xFFFFFFFF) # MOV operation
ref_31684 = (ref_28384 & 0xFFFFFFFF) # MOV operation
ref_31732 = (ref_31684 & 0xFFFFFFFF) # MOV operation
ref_33923 = ref_27164 # MOV operation
ref_34705 = ref_27164 # MOV operation
ref_34841 = ref_34705 # MOV operation
ref_34847 = (0x7 & ref_34841) # AND operation
ref_34916 = ref_34847 # MOV operation
ref_34930 = ((ref_34916 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_35007 = ref_33923 # MOV operation
ref_35011 = ref_34930 # MOV operation
ref_35013 = (ref_35011 | ref_35007) # OR operation
ref_35090 = ref_35013 # MOV operation
ref_36262 = (ref_30516 & 0xFFFFFFFF) # MOV operation
ref_36310 = (ref_36262 & 0xFFFFFFFF) # MOV operation
ref_38394 = (ref_31732 & 0xFFFFFFFF) # MOV operation
ref_38442 = (ref_38394 & 0xFFFFFFFF) # MOV operation
ref_38444 = (((ref_38442 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_38445 = (((ref_38442 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_38446 = (((ref_38442 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_38447 = ((ref_38442 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_39610 = (ref_36310 & 0xFFFFFFFF) # MOV operation
ref_39658 = (ref_39610 & 0xFFFFFFFF) # MOV operation
ref_39660 = (((ref_39658 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_39661 = (((ref_39658 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_39662 = (((ref_39658 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_39663 = ((ref_39658 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_41877 = ref_35090 # MOV operation
ref_42519 = ((((((((ref_38444) << 8 | ref_38445) << 8 | ref_38446) << 8 | ref_38447) << 8 | ref_39660) << 8 | ref_39661) << 8 | ref_39662) << 8 | ref_39663) # MOV operation
ref_42655 = ref_42519 # MOV operation
ref_42661 = (((sx(0x40, 0x4E1A7F2) * sx(0x40, ref_42655)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_42735 = ref_41877 # MOV operation
ref_42739 = ref_42661 # MOV operation
ref_42741 = (ref_42739 ^ ref_42735) # XOR operation
ref_42902 = ref_42741 # MOV operation
ref_42908 = (0xF & ref_42902) # AND operation
ref_43069 = ref_42908 # MOV operation
ref_43075 = (0x1 | ref_43069) # OR operation
ref_43742 = ref_13735 # MOV operation
ref_44384 = ref_15291 # MOV operation
ref_44436 = ref_43742 # MOV operation
ref_44440 = ref_44384 # MOV operation
ref_44442 = (((sx(0x40, ref_44440) * sx(0x40, ref_44436)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_44508 = ref_44442 # MOV operation
ref_44520 = ref_43075 # MOV operation
ref_44522 = ((ref_44508 << ((ref_44520 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_45273 = ref_35090 # MOV operation
ref_45915 = ((((((((ref_38444) << 8 | ref_38445) << 8 | ref_38446) << 8 | ref_38447) << 8 | ref_39660) << 8 | ref_39661) << 8 | ref_39662) << 8 | ref_39663) # MOV operation
ref_46051 = ref_45915 # MOV operation
ref_46057 = (((sx(0x40, 0x4E1A7F2) * sx(0x40, ref_46051)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_46131 = ref_45273 # MOV operation
ref_46135 = ref_46057 # MOV operation
ref_46137 = (ref_46135 ^ ref_46131) # XOR operation
ref_46298 = ref_46137 # MOV operation
ref_46304 = (0xF & ref_46298) # AND operation
ref_46465 = ref_46304 # MOV operation
ref_46471 = (0x1 | ref_46465) # OR operation
ref_46552 = ref_46471 # MOV operation
ref_46554 = ((0x40 - ref_46552) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_46562 = ref_46554 # MOV operation
ref_47224 = ref_13735 # MOV operation
ref_47866 = ref_15291 # MOV operation
ref_47918 = ref_47224 # MOV operation
ref_47922 = ref_47866 # MOV operation
ref_47924 = (((sx(0x40, ref_47922) * sx(0x40, ref_47918)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_47990 = ref_47924 # MOV operation
ref_48002 = ref_46562 # MOV operation
ref_48004 = (ref_47990 >> ((ref_48002 & 0xFF) & 0x3F)) # SHR operation
ref_48081 = ref_44522 # MOV operation
ref_48085 = ref_48004 # MOV operation
ref_48087 = (ref_48085 | ref_48081) # OR operation
ref_48164 = ref_48087 # MOV operation
ref_48318 = ref_48164 # MOV operation
ref_48320 = ref_48318 # MOV operation

print(ref_48320 & 0xffffffffffffffff)
