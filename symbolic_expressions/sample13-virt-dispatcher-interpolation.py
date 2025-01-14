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
ref_8265 = ref_239 # MOV operation
ref_8269 = ((0xDEADBEEFDEADBEEF + ref_8265) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_8376 = ref_8269 # MOV operation
ref_8378 = (0xE6ADBEEFDEADBEEF ^ ref_8376) # XOR operation
ref_8399 = ref_8269 # MOV operation
ref_8403 = ref_8399 # MOV operation
ref_8447 = ref_8403 # MOV operation
ref_8451 = rol(0xF, ref_8447) # ROL operation
ref_8455 = ref_8451 # MOV operation
ref_8462 = ref_8455 # MOV operation
ref_8478 = ref_8378 # MOV operation
ref_8482 = ref_8462 # MOV operation
ref_8484 = ((ref_8478 + ref_8482) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_8510 = ref_8484 # MOV operation
ref_8512 = (0x1234 ^ ref_8510) # XOR operation
ref_8533 = ref_8484 # MOV operation
ref_8537 = ref_8533 # MOV operation
ref_8581 = ref_8537 # MOV operation
ref_8585 = rol(0x34, ref_8581) # ROL operation
ref_8589 = ref_8585 # MOV operation
ref_8596 = ref_8589 # MOV operation
ref_8612 = ref_8512 # MOV operation
ref_8616 = ref_8596 # MOV operation
ref_8618 = ((ref_8612 + ref_8616) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_8644 = ref_8618 # MOV operation
ref_8646 = (0x1234 ^ ref_8644) # XOR operation
ref_8667 = ref_8618 # MOV operation
ref_8671 = ref_8667 # MOV operation
ref_8715 = ref_8671 # MOV operation
ref_8719 = rol(0x1A, ref_8715) # ROL operation
ref_8723 = ref_8719 # MOV operation
ref_8730 = ref_8723 # MOV operation
ref_8746 = ref_8646 # MOV operation
ref_8750 = ref_8730 # MOV operation
ref_8752 = ((ref_8746 + ref_8750) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_8774 = ref_8462 # MOV operation
ref_8778 = ref_8752 # MOV operation
ref_8780 = (ref_8774 ^ ref_8778) # XOR operation
ref_8801 = ref_8752 # MOV operation
ref_8805 = ref_8801 # MOV operation
ref_8849 = ref_8805 # MOV operation
ref_8853 = rol(0x33, ref_8849) # ROL operation
ref_8857 = ref_8853 # MOV operation
ref_8864 = ref_8857 # MOV operation
ref_8880 = ref_8780 # MOV operation
ref_8884 = ref_8864 # MOV operation
ref_8886 = ((ref_8880 + ref_8884) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_8908 = ref_8596 # MOV operation
ref_8912 = ref_8886 # MOV operation
ref_8914 = (ref_8908 ^ ref_8912) # XOR operation
ref_8935 = ref_8886 # MOV operation
ref_8939 = ref_8935 # MOV operation
ref_8983 = ref_8939 # MOV operation
ref_8987 = rol(0x1C, ref_8983) # ROL operation
ref_8991 = ref_8987 # MOV operation
ref_8998 = ref_8991 # MOV operation
ref_9014 = ref_8914 # MOV operation
ref_9018 = ref_8998 # MOV operation
ref_9020 = ((ref_9014 + ref_9018) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_9042 = ref_8730 # MOV operation
ref_9046 = ref_9020 # MOV operation
ref_9048 = (ref_9042 ^ ref_9046) # XOR operation
ref_9069 = ref_9020 # MOV operation
ref_9073 = ref_9069 # MOV operation
ref_9117 = ref_9073 # MOV operation
ref_9121 = rol(0x9, ref_9117) # ROL operation
ref_9125 = ref_9121 # MOV operation
ref_9132 = ref_9125 # MOV operation
ref_9148 = ref_9048 # MOV operation
ref_9152 = ref_9132 # MOV operation
ref_9154 = ((ref_9148 + ref_9152) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_9176 = ref_8864 # MOV operation
ref_9180 = ref_9154 # MOV operation
ref_9182 = (ref_9176 ^ ref_9180) # XOR operation
ref_9203 = ref_9154 # MOV operation
ref_9207 = ref_9203 # MOV operation
ref_9251 = ref_9207 # MOV operation
ref_9255 = rol(0x2F, ref_9251) # ROL operation
ref_9259 = ref_9255 # MOV operation
ref_9266 = ref_9259 # MOV operation
ref_9282 = ref_9182 # MOV operation
ref_9286 = ref_9266 # MOV operation
ref_9288 = ((ref_9282 + ref_9286) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_9310 = ref_8998 # MOV operation
ref_9314 = ref_9288 # MOV operation
ref_9316 = (ref_9310 ^ ref_9314) # XOR operation
ref_9337 = ref_9288 # MOV operation
ref_9341 = ref_9337 # MOV operation
ref_9385 = ref_9341 # MOV operation
ref_9389 = rol(0x36, ref_9385) # ROL operation
ref_9393 = ref_9389 # MOV operation
ref_9400 = ref_9393 # MOV operation
ref_9416 = ref_9316 # MOV operation
ref_9420 = ref_9400 # MOV operation
ref_9422 = ((ref_9416 + ref_9420) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_9444 = ref_9132 # MOV operation
ref_9448 = ref_9422 # MOV operation
ref_9450 = (ref_9444 ^ ref_9448) # XOR operation
ref_9471 = ref_9422 # MOV operation
ref_9475 = ref_9471 # MOV operation
ref_9519 = ref_9475 # MOV operation
ref_9523 = rol(0x20, ref_9519) # ROL operation
ref_9527 = ref_9523 # MOV operation
ref_9534 = ref_9527 # MOV operation
ref_9550 = ref_9450 # MOV operation
ref_9554 = ref_9534 # MOV operation
ref_9556 = ((ref_9550 + ref_9554) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_9578 = ref_9266 # MOV operation
ref_9582 = ref_9556 # MOV operation
ref_9584 = (ref_9578 ^ ref_9582) # XOR operation
ref_9605 = ref_9556 # MOV operation
ref_9609 = ref_9605 # MOV operation
ref_9653 = ref_9609 # MOV operation
ref_9657 = rol(0x19, ref_9653) # ROL operation
ref_9661 = ref_9657 # MOV operation
ref_9668 = ref_9661 # MOV operation
ref_9684 = ref_9584 # MOV operation
ref_9688 = ref_9668 # MOV operation
ref_9690 = ((ref_9684 + ref_9688) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_9739 = ref_9690 # MOV operation
ref_9743 = ref_9739 # MOV operation
ref_9787 = ref_9743 # MOV operation
ref_9791 = rol(0x3F, ref_9787) # ROL operation
ref_9795 = ref_9791 # MOV operation
ref_9802 = ref_9795 # MOV operation
ref_9851 = ref_9802 # MOV operation
ref_9913 = ref_9851 # MOV operation
ref_11572 = ref_9913 # MOV operation
ref_11936 = ref_11572 # MOV operation
ref_13309 = ref_11936 # MOV operation
ref_13661 = ref_13309 # MOV operation
ref_13699 = ref_13661 # MOV operation
ref_13711 = ref_13699 # MOV operation
ref_13713 = ref_13711 # MOV operation

print(ref_13713 & 0xffffffffffffffff)
