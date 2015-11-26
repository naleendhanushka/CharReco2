#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Naleen'

import numpy as np

def char_map(lowerZoneClass, middleZoneClass, upperZoneClass):
    char_array=np.array([["l3", "m1", "u0", "අ"],
                    ["l9", "m2", "u0", "උ"],
                    ["l0", "m3", "u0", "ඏ"],
                    ["l0", "m4", "u1", "ඔ "],
                    ["l0", "m4", "u5", " ඕ"],
                    ["l0", "m5", "u3", "එ"],
                    ["l0", "m5", "u9", "ඒ"],
                    ["l0", "m6", "u3", "ළු"],
                    ["l1", "m7", "u0", "ඉ"],
                    ["l0", "m8", "u0", "ක"],
                    ["l0", "m8", "u12", "කි"],
                    ["l0", "m8", "u13", "කී"],
                    ["l4", "m8", "u0", "කු"],
                    ["l5", "m8", "u0", " කූ"],
                    ["l0", "m8", "u8", "ක්"],
                    ["l6", "m8", "u0", " ක්‍ර"], 
                    ["l0", "m9", "u1", "ඛ"],
                    ["l0", "m9", "u6", "ඛි"],
                    ["l0", "m9", "u7", "ඛී"],
                    ["l7", "m9", "u1", "ඛු"],
                    ["l8", "m9", "u1", "ඛූ"],
                    ["l0", "m9", "u5", "ඛ්"],
                    ["l0", "m10", "u0", "ග"],
                    ["l0", "m10", "u12", "ගි"],
                    ["l0", "m10", "u13", "ගී"],
                    ["l4", "m10", "u0", "ගු"],
                    ["l5", "m10", "u0", "ගූ"],
                    ["l0", "m10", "u8", "ග්"],
                    ["l6", "m10", "u0", "ග්‍ර"],
                    ["l0", "m11", "u0", "ඝ"],
                    ["l0", "m11", "u12", "ඝි"],
                    ["l0", "m11", "u13", "ඝී"],
                    ["l7", "m11", "u0", "ඝු"],
                    ["l8", "m11", "u0", "ඝූ"],
                    ["l0", "m11", "u8", "ඝ්"],
                    ["l6", "m11", "u0", "ඝ්‍ර"],
                    ["l0", "m12", "u0", "ඟ"],
                    ["l0", "m12", "u12", "ඟි"],
                    ["l0", "m12", "u13", "ඟී"],
                    ["l4", "m12", "u0", "ඟු"],
                    ["l5", "m12", "u0", "ඟූ"],
                    ["l0", "m12", "u8", "ඟ්"],
                    ["l0", "m13", "u1", "ච"],
                    ["l0", "m13", "u6", "චි"],
                    ["l0", "m13", "u7", "චී"],
                    ["l7", "m13", "u1", "චු"],
                    ["l8", "m13", "u1", "චූ"],
                    ["l0", "m13", "u5", "ච්"],
                    ["l6", "m13", "u1", "ච්‍ර"],
                    ["l0", "m14", "u4", "ඡ"],
                    ["l0", "m14", "u14", "ඡි"],
                    ["l0", "m14", "u15", "ඡී"],
                    ["l7", "m14", "u4", "ඡු"],
                    ["l8", "m14", "u4", "ඡූ"],
                    ["l0", "m14", "u16", "ඡ්"],
                    ["l6", "m14", "u4", "ඡ්‍ර"],
                    ["l0", "m15", "u4", "ජ"],
                    ["l0", "m15", "u14", "ජි"],
                    ["l0", "m15", "u15", "ජී"],
                    ["l7", "m15", "u4", "ජු"],
                    ["l8", "m15", "u4", "ජූ"],
                    ["l0", "m15", "u16", "ජ්"],
                    ["l6", "m15", "u4", "ජ්‍ර"],
                    ["l0", "m16", "u1", "ඣ"],
                    ["l0", "m16", "u6", "ඣි"],
                    ["l0", "m16", "u7", "ඣී"],
                    ["l7", "m16", "u1", "ඣු"],
                    ["l8", "m16", "u1", "ඣූ"],
                    ["l0", "m16", "u5", "ඣ්"],
                    ["l6", "m16", "u1", "ඣ්‍ර"],
                    ["l2", "m17", "u0", "ඤ"],
                    ["l2", "m17", "u12", "ඤි"],
                    ["l2", "m17", "u13", "ඤී"],
                    ["l7", "m17", "u0", "ඤු"],
                    ["l8", "m17", "u0", "ඤූ"],
                    ["l2", "m17", "u8", "ඤ්"],
                    ["l6", "m17", "u0", "ඤ්‍ර"],
                    ["l0", "m18", "u4", "ඦ"],
                    ["l0", "m18", "u14", "ඦි"],
                    ["l0", "m18", "u15", "ඦී"],
                    ["l7", "m18", "u4", "ඦු"],
                    ["l8", "m18", "u4", "ඦූ"],
                    ["l0", "m18", "u16", "ඦ්"],
                    ["l6", "m18", "u4", "ඦ්‍ර"],
                    ["l0", "m19", "u1", "ට"],
                    ["l0", "m19", "u6", "ටි"],
                    ["l0", "m19", "u7", "ටී"],
                    ["l7", "m19", "u1", "ටු"],
                    ["l8", "m19", "u1", "ටූ"],
                    ["l0", "m19", "u5", "ට්"],
                    ["l6", "m19", "u1", "ට්‍ර"],
                    ["l0", "m19", "u3", "ථ"],
                    ["l0", "m19", "u10", "ථි"],
                    ["l0", "m19", "u11", "ථී"],
                    ["l7", "m19", "u3", "ථු"],
                    ["l8", "m19", "u3", "ථූ"],
                    ["l0", "m19", "u9", "ථ්"],
                    ["l6", "m19", "u3", "ථ්‍ර"],
                    ["l0", "m20", "u3", "ඨ"],
                    ["l0", "m20", "u10", "ඨි"],
                    ["l0", "m20", "u11", "ඨී"],
                    ["l7", "m20", "u3", "ඨු"],
                    ["l8", "m20", "u3", "ඨූ"],
                    ["l0", "m20", "u9", "ඨ්"],
                    ["l6", "m20", "u3", "ඨ්‍ර"],
                    ["l0", "m20", "u1", "ධ"],
                    ["l0", "m20", "u6", "ධි"],
                    ["l0", "m20", "u7", "ධී"],
                    ["l7", "m20", "u1", "ධු"],
                    ["l8", "m20", "u1", "ධූ"],
                    ["l0", "m20", "u5", "ධ්"],
                    ["l6", "m20", "u1", "ධ්‍ර"],
                    ["l0", "m21", "u1", "ඩ"],
                    ["l0", "m21", "u6", "ඩි"],
                    ["l0", "m21", "u7", "ඩී"],
                    ["l7", "m21", "u1", "ඩු"],
                    ["l8", "m21", "u1", "ඩූ"],
                    ["l0", "m21", "u5", "ඩ්"],
                    ["l6", "m21", "u1", "ඩ්‍ර"],
                    ["l0", "m21", "u3", "ඪ"],
                    ["l0", "m21", "u10", "ඪි"],
                    ["l0", "m21", "u11", "ඪී"],
                    ["l7", "m21", "u3", "ඪු"],
                    ["l8", "m21", "u3", "ඪූ"],
                    ["l0", "m21", "u9", "ඪ්"],
                    ["l6", "m21", "u3", "ඪ්‍ර"],
                    ["l0", "m22", "u4", "ණ"],
                    ["l0", "m22", "u14", "ණි"],
                    ["l0", "m22", "u15", "ණී"],
                    ["l7", "m22", "u4", "ණු"],
                    ["l8", "m22", "u4", "ණූ"],
                    ["l0", "m22", "u", "ණ්"],
                    ["l6", "m22", "u4", "ණ්‍ර"],
                    ["l0", "m23", "u1", "ඬ"],
                    ["l0", "m23", "u6", "ඬි"],
                    ["l0", "m23", "u7", "ඬී"],
                    ["l7", "m23", "u1", "ඬු"],
                    ["l8", "m23", "u1", "ඬූ"],
                    ["l0", "m23", "u5", "ඬ්"],
                    ["l6", "m23", "u1", "ඬ්‍ර"],
                    ["l0", "m24", "u0", "ත"],
                    ["l0", "m24", "u12", "ති"],
                    ["l0", "m24", "u13", "තී"],
                    ["l4", "m24", "u0", "තු"],
                    ["l5", "m24", "u0", "තූ"],
                    ["l0", "m24", "u8", "ත්"],
                    ["l6", "m24", "u0", "ත්‍ර"],
                    ["l2", "m25", "u0", "ද"],
                    ["l2", "m25", "u12", "දි"],
                    ["l2", "m25", "u13", "දී"],
                    ["l7", "m25", "u0", "දු"],
                    ["l8", "m25", "u0", "දූ"],
                    ["l2", "m25", "u8", "ද්"],
                    ["l6", "m25", "u0", "ද්‍ර"],
                    ["l0", "m26", "u0", "න"],
                    ["l0", "m26", "u12", "නි"],
                    ["l0", "m26", "u13", "නී"],
                    ["l7", "m26", "u0", "නු"],
                    ["l8", "m26", "u0", "නූ"],
                    ["l0", "m26", "u8", "න්"],
                    ["l6", "m26", "u0", "න්‍ර"],
                    ["l2", "m27", "u0", "ඳ"],
                    ["l2", "m27", "u12", "ඳි"],
                    ["l2", "m27", "u13", "ඳී"],
                    ["l7", "m27", "u0", "ඳු"],
                    ["l8", "m27", "u0", "ඳූ"],
                    ["l2", "m27", "u8", "ඳ්"],
                    ["l6", "m27", "u0", "ඳ්‍ර"],
                    ["l0", "m28", "u0", "ප"],
                    ["l0", "m28", "u12", "පි"],
                    ["l0", "m28", "u13", "පී"],
                    ["l7", "m28", "u0", "පු"],
                    ["l8", "m28", "u0", "පූ"],
                    ["l0", "m28", "u8", "ප්"],
                    ["l6", "m28", "u0", "ප්‍ර"],
                    ["l0", "m29", "u3", "ඵ"],
                    ["l0", "m29", "u10", "ඵි"],
                    ["l0", "m29", "u11", "ඵී"],
                    ["l7", "m29", "u3", "ඵු"],
                    ["l8", "m29", "u3", "ඵූ"],
                    ["l0", "m29", "u9", "ඵ්"],
                    ["l6", "m29", "u3", "ඵ්‍ර"],
                    ["l0", "m30", "u1", "බ"],
                    ["l0", "m30", "u6", "බි"],
                    ["l0", "m30", "u7", "බී"],
                    ["l7", "m30", "u1", "බු"],
                    ["l8", "m30", "u1", "බූ"],
                    ["l0", "m30", "u5", "බ්"],
                    ["l6", "m30", "u1", "බ්‍ර"],
                    ["l0", "m31", "u0", "භ"],
                    ["l0", "m31", "u12", "භි"],
                    ["l0", "m31", "u13", "භී"],
                    ["l4", "m31", "u0", "භු"],
                    ["l5", "m31", "u0", "භූ"],
                    ["l0", "m31", "u8", "භ්"],
                    ["l6", "m31", "u0", "භ්‍ර"],
                    ["l0", "m32", "u1", "ම"],
                    ["l0", "m32", "u6", "මි"],
                    ["l0", "m32", "u7", "මී"],
                    ["l7", "m32", "u1", "මු"],
                    ["l8", "m32", "u1", "මූ"],
                    ["l0", "m32", "u5", "ම්"],
                    ["l6", "m32", "u1", "ම්‍ර"],
                    ["l0", "m33", "u1", "ඹ"],
                    ["l0", "m33", "u6", "ඹි"],
                    ["l0", "m33", "u7", "ඹී"],
                    ["l7", "m33", "u1", "ඹු"],
                    ["l8", "m33", "u1", "ඹූ"],
                    ["l0", "m33", "u5", "ඹ්"],
                    ["l6", "m33", "u1", "ඹ්‍ර"],
                    ["l0", "m34", "u0", "ය"],
                    ["l0", "m34", "u12", "යි"],
                    ["l0", "m34", "u13", "යී"],
                    ["l7", "m34", "u0", "යු"],
                    ["l8", "m34", "u0", "යූ"],
                    ["l0", "m34", "u8", "ය්"],
                    ["l6", "m34", "u0", "ය්‍ර"],
                    ["l0", "m35", "u4", "ර"],
                    ["l0", "m35", "u14", "රි"],
                    ["l0", "m35", "u15", "රී"],
                    ["l0", "m35", "u16", "ර්"],
                    ["l0", "m35", "u2", "ඊ"],
                    ["l9", "m36", "u0", "ල"],
                    ["l9", "m36", "u12", "ලි"],
                    ["l9", "m36", "u13", "ලී"],
                    ["l10", "m36", "u0", "ලු"],
                    ["l11", "m36", "u0", "ලූ"],
                    ["l9", "m36", "u8", "ල්"],
                    ["l6", "m36", "u0", "ල්‍ර"],
                    ["l0", "m37", "u1", "ව"],
                    ["l0", "m37", "u6", "වි"],
                    ["l0", "m37", "u7", "වී"],
                    ["l7", "m37", "u1", "වු"],
                    ["l8", "m37", "u1", "වූ"],
                    ["l0", "m37", "u5", "ව්"],
                    ["l6", "m37", "u1", "ව්‍ර"],
                    ["l0", "m38", "u0", "ශ"],
                    ["l0", "m38", "u12", "ශි"],
                    ["l0", "m38", "u13", "ශී"],
                    ["l4", "m38", "u0", "ශු"],
                    ["l5", "m38", "u0", "ශූ"],
                    ["l0", "m38", "u8", "ශ්"],
                    ["l6", "m38", "u0", "ශ්‍ර"],
                    ["l0", "m39", "u0", "ෂ"],
                    ["l0", "m39", "u12", "ෂි"],
                    ["l0", "m39", "u13", "ෂී"],
                    ["l7", "m39", "u0", "ෂු"],
                    ["l0", "m39", "u8", "ෂ්"],
                    ["l6", "m39", "u0", "ෂ්‍ර"],
                    ["l0", "m40", "u0", "ස"],
                    ["l0", "m40", "u12", "සි"],
                    ["l0", "m40", "u13", "සී"],
                    ["l7", "m40", "u0", "සු"],
                    ["l8", "m40", "u0", "සූ"],
                    ["l0", "m40", "u8", "ස්"],
                    ["l6", "m40", "u0", "ස්‍ර"],
                    ["l0", "m41", "u0", "හ"],
                    ["l0", "m41", "u12", "හි"],
                    ["l0", "m41", "u13", "හී"],
                    ["l7", "m41", "u0", "හු"],
                    ["l8", "m41", "u0", "හූ"],
                    ["l0", "m41", "u8", "හ්"],
                    ["l6", "m41", "u0", "හ්‍ර"],
                    ["l9", "m42", "u0", "ළ"],
                    ["l9", "m42", "u12", "ළි"],
                    ["l9", "m42", "u13", "ළී"],
                    ["l0", "m42", "u3", "ළු"],
                    ["l0", "m42", "u3", "ළූ"],
                    ["l9", "m42", "u8", "ළ්"],
                    ["l6", "m42", "u3", "ළ්‍ර"],
                    ["l0", "m43", "u0", "ෆ"],
                    ["l0", "m43", "u12", "ෆි"],
                    ["l0", "m43", "u13", "ෆී"],
                    ["l7", "m43", "u0", "ෆු"],
                    ["l8", "m43", "u0", "ෆූ"],
                    ["l0", "m43", "u8", "ෆ්"],
                    ["l6", "m43", "u0", "ෆ්‍ර"],
                    ["l2", "m44", "u0", "ඥ"],
                    ["l2", "m44", "u12", "ඥි"],
                    ["l2", "m44", "u13", "ඥී"],
                    ["l7", "m44", "u0", "ඥු"],
                    ["l8", "m44", "u0", "ඥූ"],
                    ["l2", "m44", "u8", "ඥ්"],
                    ["l6", "m44", "u0", "ඥ්‍ර"],
                    ["l0", "m45", "u0", "ා"],
                    ["l0", "m46", "u0", "ෘ"],
                    ["l0", "m47", "u0", "ෳ"],
                    ["l0", "m48", "u0", "ක්‍ය"],
                    ["l0", "m49", "u0", "ැ"],
                    ["l0", "m50", "u0", "කෙ"],
                    ["l0", "m51", "u0", "ෑ"],
                    ["l0", "m52", "u0", "ඃ"],
                    ["l0", "m53", "u0", "ං"],
                    ["l0", "m54", "u8", "කෝ"]])

    for char in char_array:
        if char[0] == lowerZoneClass and char[1] == middleZoneClass and char[2] == upperZoneClass:
            return char[3]

