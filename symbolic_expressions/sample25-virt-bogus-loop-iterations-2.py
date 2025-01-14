#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_163542 = ref_278 # MOV operation
ref_173438 = ref_163542 # MOV operation
ref_173452 = ((ref_173438 << (0xD & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_262786 = ref_278 # MOV operation
ref_272682 = ref_262786 # MOV operation
ref_272696 = (ref_272682 >> (0x33 & 0x3F)) # SHR operation
ref_282625 = ref_173452 # MOV operation
ref_282629 = ref_272696 # MOV operation
ref_282631 = (ref_282629 | ref_282625) # OR operation
ref_292560 = ref_282631 # MOV operation
ref_451451 = ref_278 # MOV operation
ref_461347 = ref_451451 # MOV operation
ref_461363 = ((((0x0) << 64 | ref_461347) / 0x6) & 0xFFFFFFFFFFFFFFFF) # DIV operation
ref_481224 = ref_461363 # MOV operation
ref_481230 = (((sx(0x40, 0xFA0000000002C90C) * sx(0x40, ref_481224)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_491156 = ref_481230 # MOV operation
ref_640196 = ref_292560 # MOV operation
ref_719654 = ref_491156 # MOV operation
ref_729558 = ref_640196 # MOV operation
ref_729562 = ref_719654 # MOV operation
ref_729564 = (ref_729562 | ref_729558) # OR operation
ref_808962 = ref_278 # MOV operation
ref_818858 = ref_808962 # MOV operation
ref_818870 = ref_729564 # MOV operation
ref_818872 = ((ref_818870 + ref_818858) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_828802 = ref_818872 # MOV operation
ref_997714 = ref_292560 # MOV operation
ref_1017554 = ref_997714 # MOV operation
ref_1017560 = ((ref_1017554 - 0x2ED5CD7E) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_1017568 = ref_1017560 # MOV operation
ref_1027496 = ref_1017568 # MOV operation
ref_1027498 = ((0x28E5FC28 - ref_1027496) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_1027506 = ref_1027498 # MOV operation
ref_1037422 = ref_1027506 # MOV operation
ref_1037436 = (ref_1037422 >> (0x2 & 0x3F)) # SHR operation
ref_1057301 = ref_1037436 # MOV operation
ref_1057307 = (0x7 & ref_1057301) # AND operation
ref_1077172 = ref_1057307 # MOV operation
ref_1077178 = (0x1 | ref_1077172) # OR operation
ref_1156661 = ref_491156 # MOV operation
ref_1236034 = ref_278 # MOV operation
ref_1245930 = ref_1236034 # MOV operation
ref_1245942 = ref_1156661 # MOV operation
ref_1245944 = ((ref_1245942 + ref_1245930) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_1255866 = ref_1245944 # MOV operation
ref_1255878 = ref_1077178 # MOV operation
ref_1255880 = (ref_1255866 >> ((ref_1255878 & 0xFF) & 0x3F)) # SHR operation
ref_1265809 = ref_1255880 # MOV operation
ref_1424785 = ref_1265809 # MOV operation
ref_1434681 = ref_1424785 # MOV operation
ref_1434695 = (ref_1434681 >> (0x1 & 0x3F)) # SHR operation
ref_1454560 = ref_1434695 # MOV operation
ref_1454566 = (0x7 & ref_1454560) # AND operation
ref_1474431 = ref_1454566 # MOV operation
ref_1474437 = (0x1 | ref_1474431) # OR operation
ref_1553920 = ref_1265809 # MOV operation
ref_1563816 = ref_1553920 # MOV operation
ref_1563828 = ref_1474437 # MOV operation
ref_1563830 = (ref_1563816 >> ((ref_1563828 & 0xFF) & 0x3F)) # SHR operation
ref_1573759 = ref_1563830 # MOV operation
ref_1573761 = ((ref_1573759 >> 56) & 0xFF) # Byte reference - MOV operation
ref_1573762 = ((ref_1573759 >> 48) & 0xFF) # Byte reference - MOV operation
ref_1573763 = ((ref_1573759 >> 40) & 0xFF) # Byte reference - MOV operation
ref_1573764 = ((ref_1573759 >> 32) & 0xFF) # Byte reference - MOV operation
ref_1573765 = ((ref_1573759 >> 24) & 0xFF) # Byte reference - MOV operation
ref_1573766 = ((ref_1573759 >> 16) & 0xFF) # Byte reference - MOV operation
ref_1573767 = ((ref_1573759 >> 8) & 0xFF) # Byte reference - MOV operation
ref_1573768 = (ref_1573759 & 0xFF) # Byte reference - MOV operation
ref_1812164 = ref_828802 # MOV operation
ref_1911466 = ref_292560 # MOV operation
ref_1931306 = ref_1911466 # MOV operation
ref_1931312 = (0x7 & ref_1931306) # AND operation
ref_1941233 = ref_1931312 # MOV operation
ref_1941247 = ((ref_1941233 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_1951176 = ref_1812164 # MOV operation
ref_1951180 = ref_1941247 # MOV operation
ref_1951182 = (ref_1951180 | ref_1951176) # OR operation
ref_1961111 = ref_1951182 # MOV operation
ref_2110063 = ((((ref_1573761) << 8 | ref_1573762) << 8 | ref_1573763) << 8 | ref_1573764) # MOV operation
ref_2119963 = (ref_2110063 & 0xFFFFFFFF) # MOV operation
ref_2388051 = ((((ref_1573765) << 8 | ref_1573766) << 8 | ref_1573767) << 8 | ref_1573768) # MOV operation
ref_2397951 = (ref_2388051 & 0xFFFFFFFF) # MOV operation
ref_2546899 = (ref_2119963 & 0xFFFFFFFF) # MOV operation
ref_2556799 = (ref_2546899 & 0xFFFFFFFF) # MOV operation
ref_2824980 = ref_1961111 # MOV operation
ref_2924282 = ref_1961111 # MOV operation
ref_2944122 = ref_2924282 # MOV operation
ref_2944128 = (0x7 & ref_2944122) # AND operation
ref_2954049 = ref_2944128 # MOV operation
ref_2954063 = ((ref_2954049 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_2963992 = ref_2824980 # MOV operation
ref_2963996 = ref_2954063 # MOV operation
ref_2963998 = (ref_2963996 | ref_2963992) # OR operation
ref_2973927 = ref_2963998 # MOV operation
ref_3122879 = (ref_2397951 & 0xFFFFFFFF) # MOV operation
ref_3132779 = (ref_3122879 & 0xFFFFFFFF) # MOV operation
ref_3400867 = (ref_2556799 & 0xFFFFFFFF) # MOV operation
ref_3410767 = (ref_3400867 & 0xFFFFFFFF) # MOV operation
ref_3410769 = (((ref_3410767 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_3410770 = (((ref_3410767 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_3410771 = (((ref_3410767 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_3410772 = ((ref_3410767 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_3559715 = (ref_3132779 & 0xFFFFFFFF) # MOV operation
ref_3569615 = (ref_3559715 & 0xFFFFFFFF) # MOV operation
ref_3569617 = (((ref_3569615 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_3569618 = (((ref_3569615 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_3569619 = (((ref_3569615 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_3569620 = ((ref_3569615 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_3857521 = ref_2973927 # MOV operation
ref_3936979 = ((((((((ref_3410769) << 8 | ref_3410770) << 8 | ref_3410771) << 8 | ref_3410772) << 8 | ref_3569617) << 8 | ref_3569618) << 8 | ref_3569619) << 8 | ref_3569620) # MOV operation
ref_3956819 = ref_3936979 # MOV operation
ref_3956825 = (((sx(0x40, 0x4E1A7F2) * sx(0x40, ref_3956819)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_3966751 = ref_3857521 # MOV operation
ref_3966755 = ref_3956825 # MOV operation
ref_3966757 = (ref_3966755 ^ ref_3966751) # XOR operation
ref_3986622 = ref_3966757 # MOV operation
ref_3986628 = (0xF & ref_3986622) # AND operation
ref_4006493 = ref_3986628 # MOV operation
ref_4006499 = (0x1 | ref_4006493) # OR operation
ref_4085982 = ref_292560 # MOV operation
ref_4165440 = ref_491156 # MOV operation
ref_4175344 = ref_4085982 # MOV operation
ref_4175348 = ref_4165440 # MOV operation
ref_4175350 = (((sx(0x40, ref_4175348) * sx(0x40, ref_4175344)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_4185268 = ref_4175350 # MOV operation
ref_4185280 = ref_4006499 # MOV operation
ref_4185282 = ((ref_4185268 << ((ref_4185280 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_4274701 = ref_2973927 # MOV operation
ref_4354159 = ((((((((ref_3410769) << 8 | ref_3410770) << 8 | ref_3410771) << 8 | ref_3410772) << 8 | ref_3569617) << 8 | ref_3569618) << 8 | ref_3569619) << 8 | ref_3569620) # MOV operation
ref_4373999 = ref_4354159 # MOV operation
ref_4374005 = (((sx(0x40, 0x4E1A7F2) * sx(0x40, ref_4373999)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_4383931 = ref_4274701 # MOV operation
ref_4383935 = ref_4374005 # MOV operation
ref_4383937 = (ref_4383935 ^ ref_4383931) # XOR operation
ref_4403802 = ref_4383937 # MOV operation
ref_4403808 = (0xF & ref_4403802) # AND operation
ref_4423673 = ref_4403808 # MOV operation
ref_4423679 = (0x1 | ref_4423673) # OR operation
ref_4433612 = ref_4423679 # MOV operation
ref_4433614 = ((0x40 - ref_4433612) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_4433622 = ref_4433614 # MOV operation
ref_4513100 = ref_292560 # MOV operation
ref_4592558 = ref_491156 # MOV operation
ref_4602462 = ref_4513100 # MOV operation
ref_4602466 = ref_4592558 # MOV operation
ref_4602468 = (((sx(0x40, ref_4602466) * sx(0x40, ref_4602462)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_4612386 = ref_4602468 # MOV operation
ref_4612398 = ref_4433622 # MOV operation
ref_4612400 = (ref_4612386 >> ((ref_4612398 & 0xFF) & 0x3F)) # SHR operation
ref_4622329 = ref_4185282 # MOV operation
ref_4622333 = ref_4612400 # MOV operation
ref_4622335 = (ref_4622333 | ref_4622329) # OR operation
ref_4632264 = ref_4622335 # MOV operation
ref_4652115 = ref_4632264 # MOV operation
ref_4652117 = ref_4652115 # MOV operation

print(ref_4652117 & 0xffffffffffffffff)
