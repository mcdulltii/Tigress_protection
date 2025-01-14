#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_26760 = ref_278 # MOV operation
ref_29650 = ref_26760 # MOV operation
ref_29656 = ((0x3F22161B + ref_29650) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_31138 = ref_29656 # MOV operation
ref_57706 = ref_31138 # MOV operation
ref_59148 = ref_57706 # MOV operation
ref_59150 = (((sx(0x40, ref_59148) * sx(0x40, 0x378AED0A)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_60614 = ref_59150 # MOV operation
ref_60616 = (((sx(0x40, ref_60614) * sx(0x40, 0xDF2B78B)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_63546 = ref_60616 # MOV operation
ref_63554 = (ref_63546 >> (0x1 & 0x3F)) # SHR operation
ref_63561 = ref_63554 # MOV operation
ref_65038 = ref_63561 # MOV operation
ref_65052 = (0xF & ref_65038) # AND operation
ref_68012 = ref_65052 # MOV operation
ref_68018 = (0x1 | ref_68012) # OR operation
ref_81257 = ref_278 # MOV operation
ref_82714 = ref_81257 # MOV operation
ref_82728 = ((ref_82714 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_94497 = ref_278 # MOV operation
ref_97405 = ref_94497 # MOV operation
ref_97413 = (ref_97405 >> (0x39 & 0x3F)) # SHR operation
ref_97420 = ref_97413 # MOV operation
ref_98905 = ref_82728 # MOV operation
ref_98909 = ref_97420 # MOV operation
ref_98911 = (ref_98909 | ref_98905) # OR operation
ref_100393 = ref_98911 # MOV operation
ref_100405 = ref_68018 # MOV operation
ref_100407 = ((ref_100393 << ((ref_100405 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_113646 = ref_278 # MOV operation
ref_115103 = ref_113646 # MOV operation
ref_115117 = ((ref_115103 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_126886 = ref_278 # MOV operation
ref_129794 = ref_126886 # MOV operation
ref_129802 = (ref_129794 >> (0x39 & 0x3F)) # SHR operation
ref_129809 = ref_129802 # MOV operation
ref_131294 = ref_115117 # MOV operation
ref_131298 = ref_129809 # MOV operation
ref_131300 = (ref_131298 | ref_131294) # OR operation
ref_147528 = ref_31138 # MOV operation
ref_148970 = ref_147528 # MOV operation
ref_148972 = (((sx(0x40, ref_148970) * sx(0x40, 0x378AED0A)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_150436 = ref_148972 # MOV operation
ref_150438 = (((sx(0x40, ref_150436) * sx(0x40, 0xDF2B78B)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_153368 = ref_150438 # MOV operation
ref_153376 = (ref_153368 >> (0x1 & 0x3F)) # SHR operation
ref_153383 = ref_153376 # MOV operation
ref_154860 = ref_153383 # MOV operation
ref_154874 = (0xF & ref_154860) # AND operation
ref_157834 = ref_154874 # MOV operation
ref_157840 = (0x1 | ref_157834) # OR operation
ref_160795 = ref_157840 # MOV operation
ref_160797 = ((0x40 - ref_160795) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_160805 = ref_160797 # MOV operation
ref_162263 = ref_131300 # MOV operation
ref_162267 = ref_160805 # MOV operation
ref_162269 = (ref_162267 & 0xFFFFFFFF) # MOV operation
ref_162271 = (ref_162263 >> ((ref_162269 & 0xFF) & 0x3F)) # SHR operation
ref_162278 = ref_162271 # MOV operation
ref_163763 = ref_100407 # MOV operation
ref_163767 = ref_162278 # MOV operation
ref_163769 = (ref_163767 | ref_163763) # OR operation
ref_165250 = ref_163769 # MOV operation
ref_187359 = ref_278 # MOV operation
ref_199152 = ref_165250 # MOV operation
ref_202042 = ref_199152 # MOV operation
ref_202048 = ((0xAD6EED + ref_202042) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_203494 = ref_187359 # MOV operation
ref_203498 = ref_202048 # MOV operation
ref_203500 = ((ref_203498 + ref_203494) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_204982 = ref_203500 # MOV operation
ref_227091 = ref_278 # MOV operation
ref_238884 = ref_31138 # MOV operation
ref_240349 = ref_227091 # MOV operation
ref_240353 = ref_238884 # MOV operation
ref_240355 = (ref_240353 | ref_240349) # OR operation
ref_252173 = ref_165250 # MOV operation
ref_255063 = ref_252173 # MOV operation
ref_255069 = ((0x2B6B05ED + ref_255063) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_266888 = ref_204982 # MOV operation
ref_268345 = ref_266888 # MOV operation
ref_268357 = ref_255069 # MOV operation
ref_268359 = (ref_268357 & ref_268345) # AND operation
ref_269804 = ref_240355 # MOV operation
ref_269808 = ref_268359 # MOV operation
ref_269810 = ((ref_269808 + ref_269804) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_271292 = ref_269810 # MOV operation
ref_293450 = ref_271292 # MOV operation
ref_308183 = ref_204982 # MOV operation
ref_309640 = ref_308183 # MOV operation
ref_309654 = (0x3F & ref_309640) # AND operation
ref_311136 = ref_309654 # MOV operation
ref_311150 = ((ref_311136 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_312640 = ref_293450 # MOV operation
ref_312644 = ref_311150 # MOV operation
ref_312646 = (ref_312644 | ref_312640) # OR operation
ref_314127 = ref_312646 # MOV operation
ref_337715 = ref_165250 # MOV operation
ref_340623 = ref_337715 # MOV operation
ref_340631 = (ref_340623 >> (0x4 & 0x3F)) # SHR operation
ref_340638 = ref_340631 # MOV operation
ref_342115 = ref_340638 # MOV operation
ref_342129 = (0xF & ref_342115) # AND operation
ref_345089 = ref_342129 # MOV operation
ref_345095 = (0x1 | ref_345089) # OR operation
ref_356913 = ref_31138 # MOV operation
ref_358370 = ref_356913 # MOV operation
ref_358382 = ref_345095 # MOV operation
ref_358384 = ((ref_358370 << ((ref_358382 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_370202 = ref_31138 # MOV operation
ref_383465 = ref_165250 # MOV operation
ref_386373 = ref_383465 # MOV operation
ref_386381 = (ref_386373 >> (0x4 & 0x3F)) # SHR operation
ref_386388 = ref_386381 # MOV operation
ref_387865 = ref_386388 # MOV operation
ref_387879 = (0xF & ref_387865) # AND operation
ref_390839 = ref_387879 # MOV operation
ref_390845 = (0x1 | ref_390839) # OR operation
ref_393800 = ref_390845 # MOV operation
ref_393802 = ((0x40 - ref_393800) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_393810 = ref_393802 # MOV operation
ref_395268 = ref_370202 # MOV operation
ref_395272 = ref_393810 # MOV operation
ref_395274 = (ref_395272 & 0xFFFFFFFF) # MOV operation
ref_395276 = (ref_395268 >> ((ref_395274 & 0xFF) & 0x3F)) # SHR operation
ref_395283 = ref_395276 # MOV operation
ref_396768 = ref_358384 # MOV operation
ref_396772 = ref_395283 # MOV operation
ref_396774 = (ref_396772 | ref_396768) # OR operation
ref_408592 = ref_204982 # MOV operation
ref_420385 = ref_314127 # MOV operation
ref_421805 = ref_408592 # MOV operation
ref_421809 = ref_420385 # MOV operation
ref_421811 = ((ref_421809 + ref_421805) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_423275 = ref_396774 # MOV operation
ref_423279 = ref_421811 # MOV operation
ref_423281 = (((sx(0x40, ref_423279) * sx(0x40, ref_423275)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_424759 = ref_423281 # MOV operation
ref_427642 = ref_424759 # MOV operation
ref_427644 = ref_427642 # MOV operation

print(ref_427644 & 0xffffffffffffffff)
