#
# Given a list of numbers, L, find a number, x, that
# minimizes the sum of the square of the difference
# between each element in L and x: SUM_{i=0}^{n-1} (L[i] - x)^2
# 
# Your code should run in Theta(n) time
# 

def minimize_square(L):
    return int(round((sum(L) + 0.0)/len(L)))

def test():
    L = [84, 20, 48, 49, 59, 44, 21, 80, 51, 59, 60, 96, 66, 71, 69, 30, 10, 86, 49, 91]
    print minimize_square(L)

def test_1():
    L = [2,2,3,4]
    print minimize_square(L)

def test_2():
    L = [8969, 10783, 6779, 641, 242, 8300, 10004, 12049, 5174, 10455, 8831, 1069, 2922, 2973, 3233, 6440, 3809, 821, 226, 9829, 1031, 8421, 1953, 940, 9741, 5194, 2677, 8316, 4178, 179, 252, 293, 1160, 10890, 6777, 11550, 5803, 1799, 5036, 3251, 5742, 2799, 7501, 7302, 475, 2186, 8949, 6660, 3637, 7033, 4661, 7902, 4774, 602, 1889, 9466, 11970, 10695, 7428, 5320, 887, 10666, 5848, 1212, 2268, 3169, 835, 4000, 11394, 324, 6198, 4659, 4942, 4966, 2741, 10901, 5056, 2048, 6615, 7209, 541, 1461, 11856, 11512, 11762, 6271, 3643, 1875, 1998, 1953, 1984, 10114, 3217, 1214, 1262, 7726, 104, 11975, 974, 7483, 8073, 648, 7954, 3323, 1782, 290, 4587, 480, 3554, 3738, 810, 1834, 1270, 7160, 3999, 166, 533, 12053, 9326, 11758, 2437, 461, 7581, 8945, 1974, 1323, 11086, 215, 9519, 3784, 10869, 7177, 1932, 1258, 745, 1340, 3906, 7638, 9528, 260, 1296, 2553, 728, 7728, 2260, 1238, 3974, 5042, 2791, 8101, 357, 423, 3532, 6018, 339, 10280, 8776, 6627, 10733, 5482, 2238, 11702, 649, 10638, 635, 1664, 10631, 136, 2740, 4075, 3730, 5166, 785, 757, 1403, 301, 4480, 6710, 8603, 157, 401, 1869, 113, 3666, 428, 5508, 1614, 2478, 7006, 609, 430, 5900, 1537, 685, 1199, 10260, 1718, 4616, 3368, 111, 1984, 7272, 7823, 1956, 1025, 403, 131, 235, 10533, 6268, 11254, 174, 2209, 7555, 2876, 7084, 6791, 7834, 10450, 3187, 5984, 10309, 1982, 289, 5443, 731, 4257, 236, 6328, 10689, 10621, 812, 1010, 5023, 409, 11170, 156, 8206, 1900, 203, 3575, 324, 10242, 6837, 434, 1544, 304, 10124, 4524, 6616, 6955, 618, 207, 11248, 9815, 3486, 5675, 1921, 5366, 10507, 9788, 3941, 100, 7162, 744, 892, 902, 2862, 3636, 599, 3821, 2898, 977, 3272, 10715, 10505, 2391, 407, 152, 3860, 794, 7490, 2764, 7001, 5278, 5792, 1081, 11230, 7371, 7850, 309, 10177, 11768, 10661, 512, 7613, 11633, 2745, 884, 3398, 10021, 8709, 2850, 3185, 481, 118, 11580, 2002, 319, 8252, 2780, 10704, 6422, 7518, 100, 123, 4632, 8404, 3394, 3460, 2949, 578, 4193, 5979, 8146, 4498, 7178, 141, 1453, 7497, 188, 9582, 8972, 2916, 1446, 8694, 1886, 1492, 153, 2397, 6588, 9159, 6533, 5931, 5358, 5153, 705, 3894, 7257, 4926, 4013, 7012, 6504, 6249, 464, 400, 9832, 3065, 12074, 912, 7092, 3722, 577, 675, 10197, 6359, 3242, 12059, 1095, 6071, 3983, 1627, 4100, 1496, 6319, 5450, 552, 9508, 11961, 10315, 4620, 436, 6183, 5701, 8700, 5620, 1570, 3199, 1642, 1532, 2168, 3181, 2054, 2711, 4789, 1002, 931, 9273, 10833, 4734, 11477, 9197, 1030, 262, 5259, 3884, 2534, 766, 9946, 7478, 9205, 5082, 3096, 470, 7509, 5332, 7450, 1844, 3549, 1129, 2818, 1800, 10995, 2347, 3775, 3673, 2053, 1748, 170, 359, 1183, 1382, 5471, 4871, 233, 1032, 315, 2224, 1283, 256, 7125, 142, 4850, 9883, 7687, 573, 3783, 5929, 11868, 199, 10891, 6271, 9826, 3401, 6215, 9701, 11837, 5795, 7146, 935, 884, 10106, 5155, 7135, 4995, 3121, 1572, 566, 4965, 6323, 916, 5838, 760, 4002, 1878, 5737, 941, 386, 379, 112, 715, 11625, 4477, 246, 3008, 303, 3010, 3979, 4140, 479, 104, 3720, 6694, 10671, 9943, 8457, 5531, 2112, 838, 522, 5227, 2317, 471, 738, 2357, 290, 7981, 4264, 445, 2789, 8762, 8297, 8068, 2707, 9427, 8989, 482, 6410, 7012, 5660, 6405, 5116, 3775, 2572, 959, 4237, 4396, 101, 3079, 9287, 5061, 1796, 620, 10814, 8007, 7617, 441, 1151, 3265, 3904, 4711, 524, 2161, 7368, 140, 8926, 7809, 3294, 4227, 7613, 4086, 117, 10279, 1084, 8818, 2158, 107, 11277, 10138, 9528, 10938, 10402, 1213, 836, 12084, 2115, 105, 9989, 4955, 8999, 7551, 8622, 5203, 6811, 2913, 110, 7167, 9336, 503, 4715, 1523, 472, 4650, 4131, 10929, 1240, 9908, 7713, 2237, 8571, 210, 6383, 8933, 9010, 2937, 826, 8764, 3113, 247, 6971, 2937, 6717, 5323, 312, 7589, 1293, 5838, 152, 432, 200, 7728, 8045, 4035, 267, 6332, 1511, 879, 4579, 887, 10454, 943, 10965, 2627, 187, 2328, 10617, 4971, 9918, 210, 693, 1175, 2693, 3649, 3511, 922, 11917, 6900, 4228, 6091, 1878, 2137, 1452, 615, 4989, 5780, 1375, 10225, 6500, 9211, 1150, 1224, 9655, 5583, 6916, 3738, 3368, 528, 7801, 11371, 4949, 2002, 6660, 4196, 190, 2231, 7118, 4258, 2825, 9850, 4513, 231, 10667, 623, 3964, 1569, 8556, 141, 6949, 1087, 6779, 2026, 6494, 11347, 1341, 7163, 7190, 7064, 9666, 9012, 10872, 10663, 10840, 7521, 2494, 167, 5447, 129, 11100, 6178, 1983, 1660, 1821, 2848, 174, 4817, 881, 5800, 5610, 3810, 9716, 9730, 2274, 279, 11516, 2786, 930, 5396, 1897, 2825, 8787, 6409, 3365, 11182, 3630, 508, 806, 5861, 317, 9527, 4377, 212, 3563, 6159, 6072, 572, 8272, 156, 11350, 8914, 8567, 4949, 8007, 1678, 208, 2586, 9312, 1503, 1679, 7932, 473, 4866, 882, 149, 912, 4954, 7966, 5678, 1233, 9293, 429, 220, 11823, 6006, 736, 2413, 11654, 11420, 234, 3937, 11527, 1159, 4080, 577, 7010, 11743, 169, 10832, 3554, 5333, 12087, 4637, 5629, 2075, 4835, 3747, 335, 6583, 1868, 7099, 1293, 3062, 1649, 5164, 6003, 10342, 4856, 205, 9579, 4364, 4621, 7655, 120, 2893, 3959, 11973, 7140, 6441, 8033, 6613, 5554, 778, 3788, 3645, 9675, 384, 542, 11141, 2451, 2488, 11093, 618, 592, 1301, 511, 7217, 4587, 11183, 5398, 246, 1653, 1581, 11667, 1930, 4076, 736, 3825, 173, 11481, 6886, 290, 807, 9428, 5692, 11924, 5189, 7782, 874, 3735, 240, 1415, 1808, 7786, 2634, 529, 4893, 7478, 1477, 4431, 1498, 3413, 2505, 601, 4232, 1229, 11906, 566, 3361, 7459, 6629, 4619, 984, 6447, 7434, 6538, 1237, 11810, 1979, 11139, 8706, 4783, 3531, 10313, 1548, 11541, 3404, 5205, 8826, 2032, 2661, 819, 9811, 6007, 773, 6912, 2982, 297, 9877, 2475, 4321, 11806, 4042, 451, 6456, 1070, 2982, 8613, 10331, 1384, 10190, 3719, 5863, 2625, 1143, 1284, 2154, 629, 12066, 7303, 10647, 8153, 10543, 249, 591, 7261, 1919, 1974, 4137, 365, 4741, 5712, 3688, 2617, 366, 7801, 8135, 226, 10257, 2581, 1595, 938, 10244, 3913, 665, 768, 5973, 2180, 8855, 11213, 8867, 125, 10089, 105, 2038, 1587, 195, 6886, 465, 394, 4165, 714, 11878, 3618, 5908, 177, 3109, 1992, 5799, 1680, 4404, 173, 4361, 2006, 779, 1048, 3798, 1146, 1783, 4069, 2392, 116, 5962, 8403, 1239, 11389, 8289, 3097, 3991, 6056, 7878, 2926, 5252, 399, 10352, 7044, 5724, 250, 1569, 648, 6467, 4877]
    print minimize_square(L)