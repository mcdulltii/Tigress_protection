#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_41270 = ref_278 # MOV operation
ref_43524 = ref_41270 # MOV operation
ref_43538 = ((ref_43524 - 0x35CEDE6D) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_43546 = ref_43538 # MOV operation
ref_45828 = ref_43546 # MOV operation
ref_80153 = ref_278 # MOV operation
ref_84709 = ref_80153 # MOV operation
ref_84717 = ((((0x0) << 64 | ref_84709) / 0x7) & 0xFFFFFFFFFFFFFFFF) # DIV operation
ref_87000 = ref_84717 # MOV operation
ref_125998 = ref_87000 # MOV operation
ref_128252 = ref_125998 # MOV operation
ref_128266 = (ref_128252 >> (0x3 & 0x3F)) # SHR operation
ref_132847 = ref_128266 # MOV operation
ref_132853 = (0xF & ref_132847) # AND operation
ref_137434 = ref_132853 # MOV operation
ref_137440 = (0x1 | ref_137434) # OR operation
ref_142025 = ref_137440 # MOV operation
ref_142027 = ((0x7A11169 << ((ref_142025 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_162668 = ref_87000 # MOV operation
ref_164922 = ref_162668 # MOV operation
ref_164936 = (ref_164922 >> (0x3 & 0x3F)) # SHR operation
ref_169517 = ref_164936 # MOV operation
ref_169523 = (0xF & ref_169517) # AND operation
ref_174104 = ref_169523 # MOV operation
ref_174110 = (0x1 | ref_174104) # OR operation
ref_178695 = ref_174110 # MOV operation
ref_178697 = ((0x40 - ref_178695) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_178705 = ref_178697 # MOV operation
ref_183285 = ref_178705 # MOV operation
ref_183287 = (0x7A11169 >> ((ref_183285 & 0xFF) & 0x3F)) # SHR operation
ref_185574 = ref_142027 # MOV operation
ref_185578 = ref_183287 # MOV operation
ref_185580 = (ref_185578 | ref_185574) # OR operation
ref_187859 = ref_185580 # MOV operation
ref_187873 = (ref_187859 >> (0x4 & 0x3F)) # SHR operation
ref_192454 = ref_187873 # MOV operation
ref_192460 = (0xF & ref_192454) # AND operation
ref_197041 = ref_192460 # MOV operation
ref_197047 = (0x1 | ref_197041) # OR operation
ref_215309 = ref_278 # MOV operation
ref_217563 = ref_215309 # MOV operation
ref_217575 = ref_197047 # MOV operation
ref_217577 = ((ref_217563 << ((ref_217575 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_240512 = ref_87000 # MOV operation
ref_242766 = ref_240512 # MOV operation
ref_242780 = (ref_242766 >> (0x3 & 0x3F)) # SHR operation
ref_247361 = ref_242780 # MOV operation
ref_247367 = (0xF & ref_247361) # AND operation
ref_251948 = ref_247367 # MOV operation
ref_251954 = (0x1 | ref_251948) # OR operation
ref_256539 = ref_251954 # MOV operation
ref_256541 = ((0x7A11169 << ((ref_256539 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_277182 = ref_87000 # MOV operation
ref_279436 = ref_277182 # MOV operation
ref_279450 = (ref_279436 >> (0x3 & 0x3F)) # SHR operation
ref_284031 = ref_279450 # MOV operation
ref_284037 = (0xF & ref_284031) # AND operation
ref_288618 = ref_284037 # MOV operation
ref_288624 = (0x1 | ref_288618) # OR operation
ref_293209 = ref_288624 # MOV operation
ref_293211 = ((0x40 - ref_293209) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_293219 = ref_293211 # MOV operation
ref_297799 = ref_293219 # MOV operation
ref_297801 = (0x7A11169 >> ((ref_297799 & 0xFF) & 0x3F)) # SHR operation
ref_300088 = ref_256541 # MOV operation
ref_300092 = ref_297801 # MOV operation
ref_300094 = (ref_300092 | ref_300088) # OR operation
ref_302373 = ref_300094 # MOV operation
ref_302387 = (ref_302373 >> (0x4 & 0x3F)) # SHR operation
ref_306968 = ref_302387 # MOV operation
ref_306974 = (0xF & ref_306968) # AND operation
ref_311555 = ref_306974 # MOV operation
ref_311561 = (0x1 | ref_311555) # OR operation
ref_316146 = ref_311561 # MOV operation
ref_316148 = ((0x40 - ref_316146) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_316156 = ref_316148 # MOV operation
ref_334413 = ref_278 # MOV operation
ref_336667 = ref_334413 # MOV operation
ref_336679 = ref_316156 # MOV operation
ref_336681 = (ref_336667 >> ((ref_336679 & 0xFF) & 0x3F)) # SHR operation
ref_338968 = ref_217577 # MOV operation
ref_338972 = ref_336681 # MOV operation
ref_338974 = (ref_338972 | ref_338968) # OR operation
ref_341261 = ref_338974 # MOV operation
ref_377880 = ref_278 # MOV operation
ref_380134 = ref_377880 # MOV operation
ref_380148 = ((ref_380134 - 0x297EE8A1) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_380156 = ref_380148 # MOV operation
ref_384732 = ref_380156 # MOV operation
ref_384738 = (((sx(0x40, 0x1471C5DA) * sx(0x40, ref_384732)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_387022 = ref_384738 # MOV operation
ref_387024 = ((ref_387022 >> 56) & 0xFF) # Byte reference - MOV operation
ref_387025 = ((ref_387022 >> 48) & 0xFF) # Byte reference - MOV operation
ref_387026 = ((ref_387022 >> 40) & 0xFF) # Byte reference - MOV operation
ref_387027 = ((ref_387022 >> 32) & 0xFF) # Byte reference - MOV operation
ref_387028 = ((ref_387022 >> 24) & 0xFF) # Byte reference - MOV operation
ref_387029 = ((ref_387022 >> 16) & 0xFF) # Byte reference - MOV operation
ref_387030 = ((ref_387022 >> 8) & 0xFF) # Byte reference - MOV operation
ref_387031 = (ref_387022 & 0xFF) # Byte reference - MOV operation
ref_419038 = ((ref_387026) << 8 | ref_387027) # MOVZX operation
ref_423600 = (ref_419038 & 0xFFFF) # MOVZX operation
ref_455610 = ((ref_387028) << 8 | ref_387029) # MOVZX operation
ref_487608 = (ref_455610 & 0xFFFF) # MOVZX operation
ref_492182 = (ref_423600 & 0xFFFF) # MOVZX operation
ref_524180 = (ref_492182 & 0xFFFF) # MOVZX operation
ref_524182 = (((ref_524180 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_524183 = ((ref_524180 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_707474 = ref_87000 # MOV operation
ref_728090 = ref_341261 # MOV operation
ref_732646 = ref_728090 # MOV operation
ref_732652 = (0x1F & ref_732646) # AND operation
ref_734931 = ref_732652 # MOV operation
ref_734945 = ((ref_734931 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_737232 = ref_707474 # MOV operation
ref_737236 = ref_734945 # MOV operation
ref_737238 = (ref_737236 | ref_737232) # OR operation
ref_739525 = ref_737238 # MOV operation
ref_773935 = ref_739525 # MOV operation
ref_794551 = ref_739525 # MOV operation
ref_799107 = ref_794551 # MOV operation
ref_799113 = (0xF & ref_799107) # AND operation
ref_801392 = ref_799113 # MOV operation
ref_801406 = ((ref_801392 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_803693 = ref_773935 # MOV operation
ref_803697 = ref_801406 # MOV operation
ref_803699 = (ref_803697 | ref_803693) # OR operation
ref_805986 = ref_803699 # MOV operation
ref_840264 = ((ref_387024) << 8 | ref_387025) # MOVZX operation
ref_844826 = (ref_840264 & 0xFFFF) # MOVZX operation
ref_876836 = ((ref_387030) << 8 | ref_387031) # MOVZX operation
ref_908834 = (ref_876836 & 0xFFFF) # MOVZX operation
ref_908836 = (((ref_908834 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_908837 = ((ref_908834 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_913408 = (ref_844826 & 0xFFFF) # MOVZX operation
ref_945406 = (ref_913408 & 0xFFFF) # MOVZX operation
ref_977416 = (ref_945406 & 0xFFFF) # MOVZX operation
ref_981978 = (ref_977416 & 0xFFFF) # MOVZX operation
ref_1013988 = (ref_487608 & 0xFFFF) # MOVZX operation
ref_1045986 = (ref_1013988 & 0xFFFF) # MOVZX operation
ref_1045988 = (((ref_1045986 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_1045989 = ((ref_1045986 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_1050560 = (ref_981978 & 0xFFFF) # MOVZX operation
ref_1082558 = (ref_1050560 & 0xFFFF) # MOVZX operation
ref_1082560 = (((ref_1082558 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_1082561 = ((ref_1082558 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_1121474 = ((((((((ref_908836) << 8 | ref_908837) << 8 | ref_1082560) << 8 | ref_1082561) << 8 | ref_524182) << 8 | ref_524183) << 8 | ref_1045988) << 8 | ref_1045989) # MOV operation
ref_1123728 = ref_1121474 # MOV operation
ref_1123742 = (ref_1123728 >> (0x2 & 0x3F)) # SHR operation
ref_1128323 = ref_1123742 # MOV operation
ref_1128329 = (0xF & ref_1128323) # AND operation
ref_1132910 = ref_1128329 # MOV operation
ref_1132916 = (0x1 | ref_1132910) # OR operation
ref_1151263 = ref_341261 # MOV operation
ref_1153517 = ref_1151263 # MOV operation
ref_1153529 = ref_1132916 # MOV operation
ref_1153531 = ((ref_1153517 << ((ref_1153529 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_1174172 = ((((((((ref_908836) << 8 | ref_908837) << 8 | ref_1082560) << 8 | ref_1082561) << 8 | ref_524182) << 8 | ref_524183) << 8 | ref_1045988) << 8 | ref_1045989) # MOV operation
ref_1176426 = ref_1174172 # MOV operation
ref_1176440 = (ref_1176426 >> (0x2 & 0x3F)) # SHR operation
ref_1181021 = ref_1176440 # MOV operation
ref_1181027 = (0xF & ref_1181021) # AND operation
ref_1185608 = ref_1181027 # MOV operation
ref_1185614 = (0x1 | ref_1185608) # OR operation
ref_1190199 = ref_1185614 # MOV operation
ref_1190201 = ((0x40 - ref_1190199) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_1190209 = ref_1190201 # MOV operation
ref_1208551 = ref_341261 # MOV operation
ref_1210805 = ref_1208551 # MOV operation
ref_1210817 = ref_1190209 # MOV operation
ref_1210819 = (ref_1210805 >> ((ref_1210817 & 0xFF) & 0x3F)) # SHR operation
ref_1213106 = ref_1153531 # MOV operation
ref_1213110 = ref_1210819 # MOV operation
ref_1213112 = (ref_1213110 | ref_1213106) # OR operation
ref_1215391 = ref_1213112 # MOV operation
ref_1215405 = (ref_1215391 >> (0x4 & 0x3F)) # SHR operation
ref_1219986 = ref_1215405 # MOV operation
ref_1219992 = (0xF & ref_1219986) # AND operation
ref_1224573 = ref_1219992 # MOV operation
ref_1224579 = (0x1 | ref_1224573) # OR operation
ref_1242926 = ref_805986 # MOV operation
ref_1247482 = ref_1242926 # MOV operation
ref_1247488 = (0xF & ref_1247482) # AND operation
ref_1252069 = ref_1247488 # MOV operation
ref_1252075 = (0x1 | ref_1252069) # OR operation
ref_1270422 = ref_45828 # MOV operation
ref_1272676 = ref_1270422 # MOV operation
ref_1272688 = ref_1252075 # MOV operation
ref_1272690 = ((ref_1272676 << ((ref_1272688 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_1291037 = ref_805986 # MOV operation
ref_1295593 = ref_1291037 # MOV operation
ref_1295599 = (0xF & ref_1295593) # AND operation
ref_1300180 = ref_1295599 # MOV operation
ref_1300186 = (0x1 | ref_1300180) # OR operation
ref_1304771 = ref_1300186 # MOV operation
ref_1304773 = ((0x40 - ref_1304771) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_1304781 = ref_1304773 # MOV operation
ref_1323123 = ref_45828 # MOV operation
ref_1325377 = ref_1323123 # MOV operation
ref_1325389 = ref_1304781 # MOV operation
ref_1325391 = (ref_1325377 >> ((ref_1325389 & 0xFF) & 0x3F)) # SHR operation
ref_1327678 = ref_1272690 # MOV operation
ref_1327682 = ref_1325391 # MOV operation
ref_1327684 = (ref_1327682 | ref_1327678) # OR operation
ref_1329963 = ref_1327684 # MOV operation
ref_1329975 = ref_1224579 # MOV operation
ref_1329977 = (ref_1329963 >> ((ref_1329975 & 0xFF) & 0x3F)) # SHR operation
ref_1352912 = ((((((((ref_908836) << 8 | ref_908837) << 8 | ref_1082560) << 8 | ref_1082561) << 8 | ref_524182) << 8 | ref_524183) << 8 | ref_1045988) << 8 | ref_1045989) # MOV operation
ref_1355166 = ref_1352912 # MOV operation
ref_1355180 = (ref_1355166 >> (0x2 & 0x3F)) # SHR operation
ref_1359761 = ref_1355180 # MOV operation
ref_1359767 = (0xF & ref_1359761) # AND operation
ref_1364348 = ref_1359767 # MOV operation
ref_1364354 = (0x1 | ref_1364348) # OR operation
ref_1382701 = ref_341261 # MOV operation
ref_1384955 = ref_1382701 # MOV operation
ref_1384967 = ref_1364354 # MOV operation
ref_1384969 = ((ref_1384955 << ((ref_1384967 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_1405610 = ((((((((ref_908836) << 8 | ref_908837) << 8 | ref_1082560) << 8 | ref_1082561) << 8 | ref_524182) << 8 | ref_524183) << 8 | ref_1045988) << 8 | ref_1045989) # MOV operation
ref_1407864 = ref_1405610 # MOV operation
ref_1407878 = (ref_1407864 >> (0x2 & 0x3F)) # SHR operation
ref_1412459 = ref_1407878 # MOV operation
ref_1412465 = (0xF & ref_1412459) # AND operation
ref_1417046 = ref_1412465 # MOV operation
ref_1417052 = (0x1 | ref_1417046) # OR operation
ref_1421637 = ref_1417052 # MOV operation
ref_1421639 = ((0x40 - ref_1421637) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_1421647 = ref_1421639 # MOV operation
ref_1439989 = ref_341261 # MOV operation
ref_1442243 = ref_1439989 # MOV operation
ref_1442255 = ref_1421647 # MOV operation
ref_1442257 = (ref_1442243 >> ((ref_1442255 & 0xFF) & 0x3F)) # SHR operation
ref_1444544 = ref_1384969 # MOV operation
ref_1444548 = ref_1442257 # MOV operation
ref_1444550 = (ref_1444548 | ref_1444544) # OR operation
ref_1446829 = ref_1444550 # MOV operation
ref_1446843 = (ref_1446829 >> (0x4 & 0x3F)) # SHR operation
ref_1451424 = ref_1446843 # MOV operation
ref_1451430 = (0xF & ref_1451424) # AND operation
ref_1456011 = ref_1451430 # MOV operation
ref_1456017 = (0x1 | ref_1456011) # OR operation
ref_1460602 = ref_1456017 # MOV operation
ref_1460604 = ((0x40 - ref_1460602) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_1460612 = ref_1460604 # MOV operation
ref_1478954 = ref_805986 # MOV operation
ref_1483510 = ref_1478954 # MOV operation
ref_1483516 = (0xF & ref_1483510) # AND operation
ref_1488097 = ref_1483516 # MOV operation
ref_1488103 = (0x1 | ref_1488097) # OR operation
ref_1506450 = ref_45828 # MOV operation
ref_1508704 = ref_1506450 # MOV operation
ref_1508716 = ref_1488103 # MOV operation
ref_1508718 = ((ref_1508704 << ((ref_1508716 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_1527065 = ref_805986 # MOV operation
ref_1531621 = ref_1527065 # MOV operation
ref_1531627 = (0xF & ref_1531621) # AND operation
ref_1536208 = ref_1531627 # MOV operation
ref_1536214 = (0x1 | ref_1536208) # OR operation
ref_1540799 = ref_1536214 # MOV operation
ref_1540801 = ((0x40 - ref_1540799) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_1540809 = ref_1540801 # MOV operation
ref_1559151 = ref_45828 # MOV operation
ref_1561405 = ref_1559151 # MOV operation
ref_1561417 = ref_1540809 # MOV operation
ref_1561419 = (ref_1561405 >> ((ref_1561417 & 0xFF) & 0x3F)) # SHR operation
ref_1563706 = ref_1508718 # MOV operation
ref_1563710 = ref_1561419 # MOV operation
ref_1563712 = (ref_1563710 | ref_1563706) # OR operation
ref_1565991 = ref_1563712 # MOV operation
ref_1566003 = ref_1460612 # MOV operation
ref_1566005 = ((ref_1565991 << ((ref_1566003 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_1568292 = ref_1329977 # MOV operation
ref_1568296 = ref_1566005 # MOV operation
ref_1568298 = (ref_1568296 | ref_1568292) # OR operation
ref_1570585 = ref_1568298 # MOV operation
ref_1575152 = ref_1570585 # MOV operation
ref_1575154 = ref_1575152 # MOV operation

print(ref_1575154 & 0xffffffffffffffff)
