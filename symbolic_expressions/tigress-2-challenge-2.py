#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_315 = SymVar_0
ref_330 = ref_315 # MOV operation
ref_21618 = ref_330 # MOV operation
ref_21868 = ref_21618 # MOV operation
ref_21884 = (0x2918921B | ref_21868) # OR operation
ref_22415 = ref_21884 # MOV operation
ref_22423 = ((0x17F452 + ref_22415) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_22709 = ref_22423 # MOV operation
ref_26990 = ref_330 # MOV operation
ref_29554 = ref_22709 # MOV operation
ref_29798 = ref_29554 # MOV operation
ref_29814 = (0x1247C27B & ref_29798) # AND operation
ref_30077 = ref_26990 # MOV operation
ref_30083 = ref_29814 # MOV operation
ref_30085 = (((sx(0x40, ref_30083) * sx(0x40, ref_30077)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_30371 = ref_30085 # MOV operation
ref_34717 = ref_30371 # MOV operation
ref_35237 = ref_34717 # MOV operation
ref_35245 = ref_35237 # MOV operation
ref_35247 = ((ref_35245 - 0x7A3FEB) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_35255 = ref_35247 # MOV operation
ref_38684 = ref_22709 # MOV operation
ref_38938 = ref_38684 # MOV operation
ref_38954 = ref_38938 # MOV operation
ref_38958 = (ref_38954 >> (0x4 & 0x3F)) # SHR operation
ref_38965 = ref_38958 # MOV operation
ref_39240 = ref_38965 # MOV operation
ref_39256 = (0xF & ref_39240) # AND operation
ref_39543 = ref_39256 # MOV operation
ref_39559 = (0x1 | ref_39543) # OR operation
ref_39866 = ref_39559 # MOV operation
ref_39870 = ((0x40 - ref_39866) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_39878 = ref_39870 # MOV operation
ref_42099 = ref_330 # MOV operation
ref_42349 = ref_42099 # MOV operation
ref_42363 = ref_39878 # MOV operation
ref_42365 = ref_42349 # MOV operation
ref_42367 = (ref_42363 & 0xFFFFFFFF) # MOV operation
ref_42369 = (ref_42365 >> ((ref_42367 & 0xFF) & 0x3F)) # SHR operation
ref_42376 = ref_42369 # MOV operation
ref_45506 = ref_22709 # MOV operation
ref_45764 = ref_45506 # MOV operation
ref_45780 = ref_45764 # MOV operation
ref_45784 = (ref_45780 >> (0x4 & 0x3F)) # SHR operation
ref_45791 = ref_45784 # MOV operation
ref_46063 = ref_45791 # MOV operation
ref_46079 = (0xF & ref_46063) # AND operation
ref_46372 = ref_46079 # MOV operation
ref_46388 = (0x1 | ref_46372) # OR operation
ref_48597 = ref_330 # MOV operation
ref_48815 = ref_48597 # MOV operation
ref_48829 = ref_46388 # MOV operation
ref_48831 = ref_48815 # MOV operation
ref_48833 = (ref_48829 & 0xFFFFFFFF) # MOV operation
ref_48835 = ((ref_48831 << ((ref_48833 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_48842 = ref_48835 # MOV operation
ref_49114 = ref_48842 # MOV operation
ref_49128 = ref_42376 # MOV operation
ref_49130 = (ref_49128 | ref_49114) # OR operation
ref_49410 = ref_49130 # MOV operation
ref_49424 = ref_35255 # MOV operation
ref_49426 = (ref_49424 | ref_49410) # OR operation
ref_49721 = ref_49426 # MOV operation
ref_54316 = ref_49721 # MOV operation
ref_54587 = ref_54316 # MOV operation
ref_54589 = ((ref_54587 + 0x3E469461) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_56820 = ref_330 # MOV operation
ref_57088 = ref_56820 # MOV operation
ref_57102 = ref_54589 # MOV operation
ref_57104 = (ref_57102 | ref_57088) # OR operation
ref_57397 = ref_57104 # MOV operation
ref_63407 = ref_49721 # MOV operation
ref_63661 = ref_63407 # MOV operation
ref_63677 = ref_63661 # MOV operation
ref_63681 = (ref_63677 >> (0x2 & 0x3F)) # SHR operation
ref_63688 = ref_63681 # MOV operation
ref_63979 = ref_63688 # MOV operation
ref_63995 = (0xF & ref_63979) # AND operation
ref_64236 = ref_63995 # MOV operation
ref_64252 = (0x1 | ref_64236) # OR operation
ref_64543 = ref_64252 # MOV operation
ref_64547 = ((0x40 - ref_64543) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_64555 = ref_64547 # MOV operation
ref_66896 = ref_49721 # MOV operation
ref_67118 = ref_66896 # MOV operation
ref_67132 = ref_64555 # MOV operation
ref_67134 = ref_67118 # MOV operation
ref_67136 = (ref_67132 & 0xFFFFFFFF) # MOV operation
ref_67138 = ((ref_67134 << ((ref_67136 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_67145 = ref_67138 # MOV operation
ref_70309 = ref_49721 # MOV operation
ref_70579 = ref_70309 # MOV operation
ref_70595 = ref_70579 # MOV operation
ref_70599 = (ref_70595 >> (0x2 & 0x3F)) # SHR operation
ref_70606 = ref_70599 # MOV operation
ref_70868 = ref_70606 # MOV operation
ref_70884 = (0xF & ref_70868) # AND operation
ref_71139 = ref_70884 # MOV operation
ref_71155 = (0x1 | ref_71139) # OR operation
ref_73468 = ref_49721 # MOV operation
ref_73700 = ref_73468 # MOV operation
ref_73714 = ref_71155 # MOV operation
ref_73716 = ref_73700 # MOV operation
ref_73718 = (ref_73714 & 0xFFFFFFFF) # MOV operation
ref_73720 = (ref_73716 >> ((ref_73718 & 0xFF) & 0x3F)) # SHR operation
ref_73727 = ref_73720 # MOV operation
ref_73999 = ref_73727 # MOV operation
ref_74013 = ref_67145 # MOV operation
ref_74015 = (ref_74013 | ref_73999) # OR operation
ref_74311 = ref_74015 # MOV operation
ref_74327 = (0x3F & ref_74311) # AND operation
ref_74568 = ref_74327 # MOV operation
ref_74584 = ref_74568 # MOV operation
ref_74588 = ((ref_74584 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_74595 = ref_74588 # MOV operation
ref_76920 = ref_22709 # MOV operation
ref_77190 = ref_76920 # MOV operation
ref_77204 = ref_74595 # MOV operation
ref_77206 = (ref_77204 | ref_77190) # OR operation
ref_77459 = ref_77206 # MOV operation
ref_94215 = ref_57397 # MOV operation
ref_94469 = ref_94215 # MOV operation
ref_94485 = (0x7 & ref_94469) # AND operation
ref_94781 = ref_94485 # MOV operation
ref_94797 = (0x1 | ref_94781) # OR operation
ref_97091 = ref_49721 # MOV operation
ref_97345 = ref_97091 # MOV operation
ref_97359 = ref_94797 # MOV operation
ref_97361 = ref_97345 # MOV operation
ref_97363 = (ref_97359 & 0xFFFFFFFF) # MOV operation
ref_97365 = ((ref_97361 << ((ref_97363 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_97372 = ref_97365 # MOV operation
ref_97660 = ref_97372 # MOV operation
ref_97676 = ref_97660 # MOV operation
ref_97680 = (ref_97676 >> (0x4 & 0x3F)) # SHR operation
ref_97687 = ref_97680 # MOV operation
ref_97927 = ref_97687 # MOV operation
ref_97943 = (0xF & ref_97927) # AND operation
ref_98234 = ref_97943 # MOV operation
ref_98250 = (0x1 | ref_98234) # OR operation
ref_98549 = ref_98250 # MOV operation
ref_98553 = ((0x40 - ref_98549) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_98561 = ref_98553 # MOV operation
ref_101123 = ref_77459 # MOV operation
ref_101393 = ref_101123 # MOV operation
ref_101421 = ((((0x0) << 64 | ref_101393) / ((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x7)) & 0xFFFFFFFFFFFFFFFF) # DIV operation
ref_101684 = ref_101421 # MOV operation
ref_101698 = ref_98561 # MOV operation
ref_101700 = ref_101684 # MOV operation
ref_101702 = (ref_101698 & 0xFFFFFFFF) # MOV operation
ref_101704 = (ref_101700 >> ((ref_101702 & 0xFF) & 0x3F)) # SHR operation
ref_101711 = ref_101704 # MOV operation
ref_105408 = ref_57397 # MOV operation
ref_105662 = ref_105408 # MOV operation
ref_105678 = (0x7 & ref_105662) # AND operation
ref_105958 = ref_105678 # MOV operation
ref_105974 = (0x1 | ref_105958) # OR operation
ref_108285 = ref_49721 # MOV operation
ref_108553 = ref_108285 # MOV operation
ref_108567 = ref_105974 # MOV operation
ref_108569 = ref_108553 # MOV operation
ref_108571 = (ref_108567 & 0xFFFFFFFF) # MOV operation
ref_108573 = ((ref_108569 << ((ref_108571 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_108580 = ref_108573 # MOV operation
ref_108860 = ref_108580 # MOV operation
ref_108876 = ref_108860 # MOV operation
ref_108880 = (ref_108876 >> (0x4 & 0x3F)) # SHR operation
ref_108887 = ref_108880 # MOV operation
ref_109155 = ref_108887 # MOV operation
ref_109171 = (0xF & ref_109155) # AND operation
ref_109426 = ref_109171 # MOV operation
ref_109442 = (0x1 | ref_109426) # OR operation
ref_112041 = ref_77459 # MOV operation
ref_112273 = ref_112041 # MOV operation
ref_112301 = ((((0x0) << 64 | ref_112273) / ((((((((0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x0) << 8 | 0x7)) & 0xFFFFFFFFFFFFFFFF) # DIV operation
ref_112578 = ref_112301 # MOV operation
ref_112592 = ref_109442 # MOV operation
ref_112594 = ref_112578 # MOV operation
ref_112596 = (ref_112592 & 0xFFFFFFFF) # MOV operation
ref_112598 = ((ref_112594 << ((ref_112596 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_112605 = ref_112598 # MOV operation
ref_112877 = ref_112605 # MOV operation
ref_112891 = ref_101711 # MOV operation
ref_112893 = (ref_112891 | ref_112877) # OR operation
ref_113194 = ref_112893 # MOV operation
ref_113748 = ref_113194 # MOV operation
ref_113750 = ref_113748 # MOV operation

print(ref_113750 & 0xffffffffffffffff)
