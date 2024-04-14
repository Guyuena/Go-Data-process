#
# a = "Bqp,Wmp,Bdc,Wcp,Bpc,Wqe,Bop,Wod,Boc,Wdd,Bcd,Wep,Bec,Wnd,Bmc,Wdi,Bjp,Whq,Bmd,Wph,Bnf,Wmn,Bce,Wgi,Bqj,Wio,Bko,Wme,Bpd,Wpe,Boe,Wne,Bof,Wmf,Bnh,Wmg,Boh,Wnc,Bnb,Wmb,Bpi,Wob,Bpb,Wna,Brd,Wqd,Brc,Wqc,Bqb,Wre,Brb,Wqh,Bri,Wkm,Bdo,Wdp,Bck,Wrh,Boj,Wpa,Bsd,Wnq,Boq,Wkn,Bsb,Wdk,Bdl,Wcj,Bek,Wdj,Bem,Wfl,Bel,Wbk,Bcl,Wbl,Bgj,Whj,Bgk,Wfi,Bhk,Wij,Bgn,Whm,Beo,Wfo,Bfn,Wcm,Bhp,Wip,Bfp,Wfq,Bgp,Wgq,Bco,Wgc,Bhd,Wgd,Bge,Whe,Bhc,Whb,Bib,Wgb,Bic,Wfe,Bgf,Whf,Bff,Wef,Bee,Wfd,Beg,Wdf,Bdg,Wcf,Bfg,Wcg,Bfb,Wdh,Bhg,Wig,Bga,Wfh,Bha,Wgg,Bgh,Weh,Bom,Wnr,Bor,Wos,Bps,Wns,Bqr,Won,Bno,Wnn,Bmo,Wpm,Bjq,Wlo,Blp,Wln,Blq,Wkr,Bjr,Wpk,Brk,Wlr,Bmq,Wjo,Bmr,Wql,Brl,Wrm,Bli,Wnj,Bmh,Wnk,Bpf,Wgl,Bfk,Wlh,Bmi,Wkh,Bkc,Wbm,Bdn,Wbo,Blb,Wro,Brp,Wdm,Bfm,Wok,Bqi,Wir,Bjs,Wje,Bbf,Wbg,Bbe,Wsp,Bsq,Wso,Brr,Woo,Bnp,Wld,Blc,Wkd,Bjd,Wie,Bed,Wgg,Blk,Wqo,Bhl,Wde,Bag,Wah,Baf,Wiq,Bkj,Wki,Bjj,Wji,Bml,Wnl,Bhn,Wim,Bgm,Wfc,Bdb,Wcn,Bgo,Wsl,Bsk,Wsm,Bis,Whs,Bkp,Wjk,Bmm,Wsi,Bsj,Wqk,Bsh,Wnm,Bin,Wjm,Bla,Wid,Bjc,Wpp,Bpq,Wng,Bog,Wpo,Bqa,Wik,Bll,Wej,Bpj,Wni,Boi,Wil,Bkl,Wmj,Blj,Woa,Bjn,Wnb,Bkk,Wlm,Bma,Wmk,Bho,Wjl,Bfj,Wff,Bqf,Whh,Bqg,Wol,Bse,WC,Brf,WC,Brg,WC,Bms,WC,Bkq,Wle,Bpg,WC,Bns,WC,BC"
#
#
#
#
#
#
# print(a)
# print(list(a))
#
# print(len(a))
#
# # result = [x +','  for x in a.split(',')]
# # print(result)
#
# import re
# text = 'Lolita,light of my life,fire of my loins.My sin,my soul.'
#
# # 分割的方式
# pattern1 = re.compile(' ')
# list1 = pattern1.split(a)
#
# # 查找的方式
# pattern2 = re.compile('\w+')
# list2 = pattern2.findall(a)
#
# # 打印出来，比较一下
# print("list1=",list1)
# print(list2)
# print(type(list1))
# print(type(list2))
#
#
#
#
#
# # for i in list2:
# #     print(i)
#
# vocab2id=  {'CLS': 0, 'SEP': 1, 'MASK': 2, 'PAD': 3, 'UNK': 4, 'Bdp': 5, 'Wqp': 6, 'Bqd': 7, 'Wdc': 8, 'Bpp': 9, 'Wqq': 10, 'Bdd': 11, 'Wcd': 12, 'Bod': 13, 'Wed': 14, 'Bde': 15, 'Wce': 16, 'Bdf': 17, 'Wfc': 18, 'Bpo': 19, 'Wpq': 20, 'Bcf': 21, 'Wcq': 22, 'Bcc': 23, 'Wbc': 24, 'Bcb': 25, 'Wbb': 26, 'Bbf': 27, 'Wdb': 28, 'Bbd': 29, 'Wca': 30, 'Bcp': 31, 'Wdq': 32, 'Bep': 33, 'Weq': 34, 'Bfp': 35, 'Wfq': 36, 'Bdj': 37, 'Wgp': 38, 'Bgo': 39, 'Who': 40, 'Bgn': 41, 'Whp': 42, 'Bnp': 43, 'Wqn': 44, 'Blc': 45, 'Wpn': 46, 'Bkq': 47, 'Wmq': 48, 'Bmp': 49, 'Wlp': 50, 'Blq': 51, 'Wmr': 52, 'Bko': 53, 'Wlo': 54, 'Bln': 55, 'Wmo': 56, 'Bkp': 57, 'Wmn': 58, 'Bmm': 59, 'Wnn': 60, 'Blr': 61, 'Wor': 62, 'Bhn': 63, 'Wkn': 64, 'Blm': 65, 'Wjn': 66, 'Bio': 67, 'Win': 68, 'Bim': 69, 'Wjo': 70, 'Bip': 71, 'Wjp': 72, 'Biq': 73, 'Wjq': 74, 'Bgq': 75, 'Wjr': 76, 'Bpi': 77, 'Wjc': 78, 'Bgf': 79, 'Whg': 80, 'Bom': 81, 'Won': 82, 'Bjg': 83, 'Whf': 84, 'Bje': 85, 'Wkd': 86, 'Bhe': 87, 'Wge': 88, 'Bhd': 89, 'Wld': 90, 'Bmc': 91, 'Wmd': 92, 'Bnd': 93, 'Wmf': 94, 'Bff': 95, 'Wif': 96, 'Bjf': 97, 'Wie': 98, 'Bjd': 99, 'Wid': 100, 'Bkc': 101, 'Wic': 102, 'Blh': 103, 'Wni': 104, 'Bng': 105, 'Woh': 106, 'Bqg': 107, 'Wpf': 108, 'Bnf': 109, 'Wli': 110, 'Bki': 111, 'Wlj': 112, 'Bqk': 113, 'Wmh': 114, 'Bmg': 115, 'Wgr': 116, 'Bhr': 117, 'Wkj': 118, 'Bpg': 119, 'Wfj': 120, 'Bbq': 121, 'Wbr': 122, 'Bbp': 123, 'War': 124, 'Bfr': 125, 'Wer': 126, 'Bek': 127, 'Wfk': 128, 'Bfl': 129, 'Wgl': 130, 'Bei': 131, 'Wfi': 132, 'Bfm': 133, 'Weh': 134, 'Bdh': 135, 'Wok': 136, 'Brl': 137, 'Wej': 138, 'Bdi': 139, 'Wil': 140, 'Bgs': 141, 'Wkh': 142, 'Bds': 143, 'Wlg': 144, 'Blf': 145, 'Wkf': 146, 'Bme': 147, 'Wkg': 148, 'Bke': 149, 'Whm': 150, 'Bgm': 151, 'Whl': 152, 'Boj': 153, 'Wnj': 154, 'Bol': 155, 'Wpl': 156, 'Bpk': 157, 'Wnk': 158, 'Bpm': 159, 'Wnm': 160, 'Bqm': 161, 'Wjh': 162, 'Bfe': 163, 'Wgd': 164, 'Brn': 165, 'Wro': 166, 'Bbe': 167, 'Wig': 168, 'Ble': 169, 'Wsn': 170, 'Bes': 171, 'Wkb': 172, 'Blb': 173, 'Wjb': 174, 'Brm': 175, 'Weg': 176, 'Bce': 177, 'Wdg': 178, 'Bcg': 179, 'Wgg': 180, 'Boi': 181, 'Wnh': 182, 'Bph': 183, 'Wog': 184, 'Bof': 185, 'Wir': 186, 'Bhq': 187, 'Wnl': 188, 'Bsm': 189, 'Wso': 190, 'Bfd': 191, 'Wgc': 192, 'Bee': 193, 'Wec': 194, 'Bad': 195, 'Wla': 196, 'Bma': 197, 'Wka': 198, 'Bfg': 199, 'Wfh': 200, 'Bac': 201, 'Wab': 202, 'Bis': 203, 'Wjs': 204, 'Bhs': 205, 'Wef': 206, 'Bcd': 207, 'Wcb': 208, 'BC': 209, 'Wnq': 210, 'Bcr': 211, 'Whc': 212, 'Bdr': 213, 'Wjm': 214, 'Bbs': 215, 'Wqo': 216, 'Bqf': 217, 'Woo': 218, 'Bpe': 219, 'Wop': 220, 'Bql': 221, 'Wkr': 222, 'Baq': 223, 'Wls': 224, 'Bas': 225, 'Wll': 226, 'Wkm': 227, 'Wji': 228, 'Wml': 229, 'Wno': 230, 'WC': 231, 'Boh': 232, 'Bib': 233, 'Wmb': 234, 'Bmd': 235, 'Wle': 236, 'Bkf': 237, 'Boo': 238, 'Wlq': 239, 'Bjq': 240, 'Whd': 241, 'Bgd': 242, 'Bdq': 243, 'Ber': 244, 'Wdp': 245, 'Bgb': 246, 'Wfd': 247, 'Bfc': 248, 'Wmm': 249, 'Bno': 250, 'Wmp': 251, 'Bnl': 252, 'Whq': 253, 'Bgr': 254, 'Wfr': 255, 'Bfs': 256, 'Bhp': 257, 'Wip': 258, 'Bjp': 259, 'Wio': 260, 'Bjo': 261, 'Bkm': 262, 'Bnk': 263, 'Wmk': 264, 'Bkk': 265, 'Wmi': 266, 'Bmj': 267, 'Bnj': 268, 'Wlk': 269, 'Bji': 270, 'Bjj': 271, 'Wkl': 272, 'Bjl': 273, 'Wjk': 274, 'Bik': 275, 'Bjn': 276, 'Wim': 277, 'Bll': 278, 'Wlm': 279, 'Bkl': 280, 'Bjk': 281, 'Wko': 282, 'Bkr': 283, 'Bkh': 284, 'Wng': 285, 'Blg': 286, 'Wne': 287, 'Bpr': 288, 'Wnp': 289, 'Bgj': 290, 'Wgs': 291, 'Bgh': 292, 'Wff': 293, 'Wis': 294, 'Bef': 295, 'Wcg': 296, 'Bci': 297, 'Wck': 298, 'Bdl': 299, 'Wdk': 300, 'Bel': 301, 'Wek': 302, 'Bgk': 303, 'Bhl': 304, 'Wgm': 305, 'Bhm': 306, 'Wgn': 307, 'Bfo': 308, 'Whn': 309, 'Bcl': 310, 'Wbk': 311, 'Bbl': 312, 'Wbi': 313, 'Bbo': 314, 'Wdn': 315, 'Bcn': 316, 'Wdm': 317, 'Bbj': 318, 'Wcj': 319, 'Bbh': 320, 'Waj': 321, 'Bch': 322, 'Wdi': 323, 'Wei': 324, 'Bah': 325, 'Wai': 326, 'Bal': 327, 'Wak': 328, 'Wbq': 329, 'Beb': 330, 'Ban': 331, 'Wbm': 332, 'Bap': 333, 'Wcm': 334, 'Bbb': 335, 'Bbc': 336, 'Wbd': 337, 'Bae': 338, 'Waf': 339, 'Wba': 340, 'Bab': 341, 'Wbe': 342, 'Bbg': 343, 'Bhk': 344, 'Wgi': 345, 'Bhi': 346, 'Bhh': 347, 'Wps': 348, 'Bqs': 349, 'Wos': 350, 'Brr': 351, 'Wia': 352, 'Bhb': 353, 'Bon': 354, 'Waa': 355, 'Bha': 356, 'Boa': 357, 'Wna': 358, 'Bob': 359, 'Beg': 360, 'Wbn': 361, 'Bea': 362, 'Wja': 363, 'Bfn': 364, 'Bda': 365, 'Wac': 366, 'Boe': 367, 'Wof': 368, 'Bpf': 369, 'Wam': 370, 'Wag': 371, 'Bdg': 372, 'Wmc': 373, 'Weo': 374, 'Bsc': 375, 'Bsd': 376, 'Wem': 377, 'Wfp': 378, 'Wen': 379, 'Wkq': 380, 'Bif': 381, 'Wco': 382, 'Bie': 383, 'Wks': 384, 'Bhg': 385, 'Wes': 386, 'Wds': 387, 'Wcr': 388, 'Waq': 389, 'Wpd': 390, 'Bed': 391, 'Bqc': 392, 'Bpc': 393, 'Wod': 394, 'Bnc': 395, 'Bcq': 396, 'Bec': 397, 'Web': 398, 'Bdb': 399, 'Wpi': 400, 'Boq': 401, 'Wpp': 402, 'Wep': 403, 'Bfq': 404, 'Bic': 405, 'Wgb': 406, 'Wdh': 407, 'Blo': 408, 'Bgg': 409, 'Wfa': 410, 'Bfb': 411, 'Wgf': 412, 'Bid': 413, 'Wib': 414, 'Bcm': 415, 'Wjd': 416, 'Bih': 417, 'Wjg': 418, 'Bjh': 419, 'Wln': 420, 'Wqe': 421, 'Bdo': 422, 'Wbo': 423, 'Bdn': 424, 'Wcl': 425, 'Bem': 426, 'Bdm': 427, 'Bkj': 428, 'Bfj': 429, 'Wci': 430, 'Wre': 431, 'Woc': 432, 'Wnb': 433, 'Bpa': 434, 'Brd': 435, 'Bse': 436, 'Wsf': 437, 'Wrg': 438, 'Bms': 439, 'Wns': 440, 'Bls': 441, 'Wfg': 442, 'Wao': 443, 'Bai': 444, 'Bgi': 445, 'Wke': 446, 'Bmh': 447, 'Bli': 448, 'Wme': 449, 'Bin': 450, 'Bcj': 451, 'Wbj': 452, 'Wch': 453, 'Wlb': 454, 'Bos': 455, 'Wnr': 456, 'Brf': 457, 'Wqf': 458, 'Bni': 459, 'Wmj': 460, 'Bjm': 461, 'Bsg': 462, 'Wsh': 463, 'Wrb': 464, 'Bqb': 465, 'Bra': 466, 'Wfb': 467, 'Wmg': 468, 'Wgh': 469, 'Wfe': 470, 'Wal': 471, 'Bej': 472, 'Wlc': 473, 'Wnd': 474, 'Woi': 475, 'Bgl': 476, 'Bho': 477, 'Bsb': 478, 'Brc': 479, 'Beq': 480, 'Wpm': 481, 'Wqk': 482, 'Wrl': 483, 'Wrm': 484, 'Bqo': 485, 'Bqq': 486, 'Wqc': 487, 'Wqd': 488, 'Bqe': 489, 'Wcp': 490, 'Bco': 491, 'Wqb': 492, 'Brb': 493, 'Bbn': 494, 'Wap': 495, 'Woe': 496, 'Wql': 497, 'Wgo': 498, 'Ben': 499, 'Wfn': 500, 'Wdo': 501, 'Wfo': 502, 'Wgj': 503, 'Beh': 504, 'Wjj': 505, 'Bmn': 506, 'Bnn': 507, 'Bnm': 508, 'Bir': 509, 'Whr': 510, 'Bok': 511, 'Wol': 512, 'Bop': 513, 'Woq': 514, 'Bqr': 515, 'Wkp': 516, 'Wiq': 517, 'Bjr': 518, 'Bdk': 519, 'Wdl': 520, 'Bne': 521, 'Wnc': 522, 'Bpb': 523, 'Boc': 524, 'Bmb': 525, 'Bmf': 526, 'Wlf': 527, 'Bna': 528, 'Woj': 529, 'Bqj': 530, 'Wpk': 531, 'Brk': 532, 'Wki': 533, 'Bge': 534, 'Whe': 535, 'Bhf': 536, 'Whi': 537, 'Big': 538, 'Wih': 539, 'Wri': 540, 'Wjf': 541, 'Bhc': 542, 'Bga': 543, 'Wha': 544, 'Bfa': 545, 'Whb': 546, 'Wje': 547, 'Bfh': 548, 'Bps': 549, 'Bqi': 550, 'Wqh': 551, 'Wrj': 552, 'Bla': 553, 'Bkb': 554, 'Wma': 555, 'Bhj': 556, 'Bnb': 557, 'Bia': 558, 'Bbr': 559, 'Bar': 560, 'Wdf': 561, 'Wlh': 562, 'Bmi': 563, 'Wfs': 564, 'Wsk': 565, 'Bsl': 566, 'Wsj': 567, 'Wpj': 568, 'Bnh': 569, 'Wrf': 570, 'Bjs': 571, 'Wnf': 572, 'Wgk': 573, 'Bak': 574, 'Bqa': 575, 'Bbi': 576, 'Bao': 577, 'Bpn': 578, 'Wii': 579, 'Wij': 580, 'Wkc': 581, 'Bqp': 582, 'Wcc': 583, 'Bck': 584, 'Bbk': 585, 'Wdj': 586, 'Wqj': 587, 'Wqm': 588, 'Bro': 589, 'Wpg': 590, 'Bml': 591, 'Bil': 592, 'Wjl': 593, 'Whj': 594, 'Wbf': 595, 'Blj': 596, 'Bgp': 597, 'Wee': 598, 'Bkn': 599, 'Wbg': 600, 'Bre': 601, 'Wrd': 602, 'Wsc': 603, 'Wrc': 604, 'Whh': 605, 'Wik': 606, 'Wsa': 607, 'Bri': 608, 'Bsj': 609, 'Bog': 610, 'Bmk': 611, 'Bbm': 612, 'Wbp': 613, 'Wdr': 614, 'Wpo': 615, 'Bmo': 616, 'Wph': 617, 'Bnq': 618, 'Bij': 619, 'Bfi': 620, 'Wcf': 621, 'Wde': 622, 'Brh': 623, 'Wqg': 624, 'Bqh': 625, 'Wrn': 626, 'Bpl': 627, 'Wrp': 628, 'Brg': 629, 'Brj': 630, 'Wrk': 631, 'Wsb': 632, 'Wse': 633, 'Wqa': 634, 'Wea': 635, 'Wel': 636, 'Bfk': 637, 'Wfm': 638, 'Wgq': 639, 'Beo': 640, 'Wda': 641, 'Wqi': 642, 'Bsk': 643, 'Wbh': 644, 'Baj': 645, 'Bsa': 646, 'Whs': 647, 'Wsg': 648, 'Bsh': 649, 'Baa': 650, 'Blk': 651, 'Wpc': 652, 'Bpq': 653, 'Wpe': 654, 'Blp': 655, 'Bld': 656, 'Wbl': 657, 'Bii': 658, 'Whk': 659, 'Bkd': 660, 'Bkg': 661, 'Wcs': 662, 'Was': 663, 'Brp': 664, 'Brq': 665, 'Wom': 666, 'Bso': 667, 'Bsn': 668, 'Wsm': 669, 'Bsp': 670, 'Wan': 671, 'Bks': 672, 'Wga': 673, 'Woa': 674, 'Wpb': 675, 'Bgc': 676, 'Bjc': 677, 'Wrq': 678, 'Wdd': 679, 'Wob': 680, 'Wfl': 681, 'Bca': 682, 'Bba': 683, 'Wad': 684, 'Wsr': 685, 'Bpj': 686, 'Wkk': 687, 'Wlr': 688, 'Bmq': 689, 'Wsl': 690, 'Bns': 691, 'Bsi': 692, 'Brs': 693, 'Bss': 694, 'Wsq': 695, 'Wcn': 696, 'Bdc': 697, 'Bor': 698, 'Bqn': 699, 'Bag': 700, 'Wms': 701, 'Wsi': 702, 'Wrh': 703, 'Bam': 704, 'Bpd': 705, 'Wra': 706, 'Wah': 707, 'Bka': 708, 'Wae': 709, 'Wrr': 710, 'Bjb': 711, 'Bcs': 712, 'Wsd': 713, 'Wrs': 714, 'Wqs': 715, 'Wbs': 716, 'Wpa': 717, 'Wqr': 718, 'Bsr': 719, 'Bnr': 720, 'Bsf': 721, 'Bja': 722, 'Bmr': 723, 'Wpr': 724, 'Wsp': 725, 'Wss': 726, 'Baf': 727, 'Bsq': 728, 'B': 729, 'W': 730, 'BTR': 731, 'WTR': 732, ',': 733}
#
#
#
#
#
#
# one_sample=[]
# for c in list2:
#     if c in vocab2id:
#         one_sample.append(vocab2id[c])
#
# print(one_sample)
#
#
# if 'WC' in vocab2id:
#     print(vocab2id['WC'])
#
# s = ['Bdp', 'Wqp', 'Bqd', 'Wdc', 'Bpp', 'Wqq', 'Bdd', 'Wcd', 'Bod', 'Wed', 'Bde', 'Wce', 'Bdf', 'Wfc', 'Bpo', 'Wpq', 'Bcf', 'Wcq', 'Bcc', 'Wbc', 'Bcb', 'Wbb', 'Bbf', 'Wdb', 'Bbd', 'Wca', 'Bcp', 'Wdq', 'Bep', 'Weq', 'Bfp', 'Wfq', 'Bdj', 'Wgp', 'Bgo', 'Who', 'Bgn', 'Whp', 'Bnp', 'Wqn', 'Blc', 'Wpn', 'Bkq', 'Wmq', 'Bmp', 'Wlp', 'Blq', 'Wmr', 'Bko', 'Wlo', 'Bln', 'Wmo', 'Bkp', 'Wmn', 'Bmm', 'Wnn', 'Blr', 'Wor', 'Bhn', 'Wkn', 'Blm', 'Wjn', 'Bio', 'Win', 'Bim', 'Wjo', 'Bip', 'Wjp', 'Biq', 'Wjq', 'Bgq', 'Wjr', 'Bpi', 'Wjc', 'Bgf', 'Whg', 'Bom', 'Won', 'Bjg', 'Whf', 'Bje', 'Wkd', 'Bhe', 'Wge', 'Bhd', 'Wld', 'Bmc', 'Wmd', 'Bnd', 'Wmf', 'Bff', 'Wif', 'Bjf', 'Wie', 'Bjd', 'Wid', 'Bkc', 'Wic', 'Blh', 'Wni', 'Bng', 'Woh', 'Bqg', 'Wpf', 'Bnf', 'Wli', 'Bki', 'Wlj', 'Bqk', 'Wmh', 'Bmg', 'Wgr', 'Bhr', 'Wkj', 'Bpg', 'Wfj', 'Bbq', 'Wbr', 'Bbp', 'War', 'Bfr', 'Wer', 'Bek', 'Wfk', 'Bfl', 'Wgl', 'Bei', 'Wfi', 'Bfm', 'Weh', 'Bdh', 'Wok', 'Brl', 'Wej', 'Bdi', 'Wil', 'Bgs', 'Wkh', 'Bds', 'Wlg', 'Blf', 'Wkf', 'Bme', 'Wkg', 'Bke', 'Whm', 'Bgm', 'Whl', 'Boj', 'Wnj', 'Bol', 'Wpl', 'Bpk', 'Wnk', 'Bpm', 'Wnm', 'Bqm', 'Wjh', 'Bfe', 'Wgd', 'Brn', 'Wro', 'Bbe', 'Wig', 'Ble', 'Wsn', 'Bes', 'Wkb', 'Blb', 'Wjb', 'Brm', 'Weg', 'Bce', 'Wdg', 'Bcg', 'Wgg', 'Boi', 'Wnh', 'Bph', 'Wog', 'Bof', 'Wir', 'Bhq', 'Wnl', 'Bsm', 'Wso', 'Bfd', 'Wgc', 'Bee', 'Wec', 'Bad', 'Wla', 'Bma', 'Wka', 'Bfg', 'Wfh', 'Bac', 'Wab', 'Bis', 'Wjs', 'Bhs', 'Wef', 'Bcd', 'Wcb', 'BC', 'Wnq', 'Bcr', 'Whc', 'Bdr', 'Wjm', 'Bbs', 'Wqo', 'Bqf', 'Woo', 'Bpe', 'Wop', 'Bql', 'Wkr', 'Baq', 'Wls', 'Bas', 'Wll', 'Wkm', 'Wji', 'Wml', 'Wno', 'WC', 'Boh', 'Bib', 'Wmb', 'Bmd', 'Wle', 'Bkf', 'Boo', 'Wlq', 'Bjq', 'Whd', 'Bgd', 'Bdq', 'Ber', 'Wdp', 'Bgb', 'Wfd', 'Bfc', 'Wmm', 'Bno', 'Wmp', 'Bnl', 'Whq', 'Bgr', 'Wfr', 'Bfs', 'Bhp', 'Wip', 'Bjp', 'Wio', 'Bjo', 'Bkm', 'Bnk', 'Wmk', 'Bkk', 'Wmi', 'Bmj', 'Bnj', 'Wlk', 'Bji', 'Bjj', 'Wkl', 'Bjl', 'Wjk', 'Bik', 'Bjn', 'Wim', 'Bll', 'Wlm', 'Bkl', 'Bjk', 'Wko', 'Bkr', 'Bkh', 'Wng', 'Blg', 'Wne', 'Bpr', 'Wnp', 'Bgj', 'Wgs', 'Bgh', 'Wff', 'Wis', 'Bef', 'Wcg', 'Bci', 'Wck', 'Bdl', 'Wdk', 'Bel', 'Wek', 'Bgk', 'Bhl', 'Wgm', 'Bhm', 'Wgn', 'Bfo', 'Whn', 'Bcl', 'Wbk', 'Bbl', 'Wbi', 'Bbo', 'Wdn', 'Bcn', 'Wdm', 'Bbj', 'Wcj', 'Bbh', 'Waj', 'Bch', 'Wdi', 'Wei', 'Bah', 'Wai', 'Bal', 'Wak', 'Wbq', 'Beb', 'Ban', 'Wbm', 'Bap', 'Wcm', 'Bbb', 'Bbc', 'Wbd', 'Bae', 'Waf', 'Wba', 'Bab', 'Wbe', 'Bbg', 'Bhk', 'Wgi', 'Bhi', 'Bhh', 'Wps', 'Bqs', 'Wos', 'Brr', 'Wia', 'Bhb', 'Bon', 'Waa', 'Bha', 'Boa', 'Wna', 'Bob', 'Beg', 'Wbn', 'Bea', 'Wja', 'Bfn', 'Bda', 'Wac', 'Boe', 'Wof', 'Bpf', 'Wam', 'Wag', 'Bdg', 'Wmc', 'Weo', 'Bsc', 'Bsd', 'Wem', 'Wfp', 'Wen', 'Wkq', 'Bif', 'Wco', 'Bie', 'Wks', 'Bhg', 'Wes', 'Wds', 'Wcr', 'Waq', 'Wpd', 'Bed', 'Bqc', 'Bpc', 'Wod', 'Bnc', 'Bcq', 'Bec', 'Web', 'Bdb', 'Wpi', 'Boq', 'Wpp', 'Wep', 'Bfq', 'Bic', 'Wgb', 'Wdh', 'Blo', 'Bgg', 'Wfa', 'Bfb', 'Wgf', 'Bid', 'Wib', 'Bcm', 'Wjd', 'Bih', 'Wjg', 'Bjh', 'Wln', 'Wqe', 'Bdo', 'Wbo', 'Bdn', 'Wcl', 'Bem', 'Bdm', 'Bkj', 'Bfj', 'Wci', 'Wre', 'Woc', 'Wnb', 'Bpa', 'Brd', 'Bse', 'Wsf', 'Wrg', 'Bms', 'Wns', 'Bls', 'Wfg', 'Wao', 'Bai', 'Bgi', 'Wke', 'Bmh', 'Bli', 'Wme', 'Bin', 'Bcj', 'Wbj', 'Wch', 'Wlb', 'Bos', 'Wnr', 'Brf', 'Wqf', 'Bni', 'Wmj', 'Bjm', 'Bsg', 'Wsh', 'Wrb', 'Bqb', 'Bra', 'Wfb', 'Wmg', 'Wgh', 'Wfe', 'Wal', 'Bej', 'Wlc', 'Wnd', 'Woi', 'Bgl', 'Bho', 'Bsb', 'Brc', 'Beq', 'Wpm', 'Wqk', 'Wrl', 'Wrm', 'Bqo', 'Bqq', 'Wqc', 'Wqd', 'Bqe', 'Wcp', 'Bco', 'Wqb', 'Brb', 'Bbn', 'Wap', 'Woe', 'Wql', 'Wgo', 'Ben', 'Wfn', 'Wdo', 'Wfo', 'Wgj', 'Beh', 'Wjj', 'Bmn', 'Bnn', 'Bnm', 'Bir', 'Whr', 'Bok', 'Wol', 'Bop', 'Woq', 'Bqr', 'Wkp', 'Wiq', 'Bjr', 'Bdk', 'Wdl', 'Bne', 'Wnc', 'Bpb', 'Boc', 'Bmb', 'Bmf', 'Wlf', 'Bna', 'Woj', 'Bqj', 'Wpk', 'Brk', 'Wki', 'Bge', 'Whe', 'Bhf', 'Whi', 'Big', 'Wih', 'Wri', 'Wjf', 'Bhc', 'Bga', 'Wha', 'Bfa', 'Whb', 'Wje', 'Bfh', 'Bps', 'Bqi', 'Wqh', 'Wrj', 'Bla', 'Bkb', 'Wma', 'Bhj', 'Bnb', 'Bia', 'Bbr', 'Bar', 'Wdf', 'Wlh', 'Bmi', 'Wfs', 'Wsk', 'Bsl', 'Wsj', 'Wpj', 'Bnh', 'Wrf', 'Bjs', 'Wnf', 'Wgk', 'Bak', 'Bqa', 'Bbi', 'Bao', 'Bpn', 'Wii', 'Wij', 'Wkc', 'Bqp', 'Wcc', 'Bck', 'Bbk', 'Wdj', 'Wqj', 'Wqm', 'Bro', 'Wpg', 'Bml', 'Bil', 'Wjl', 'Whj', 'Wbf', 'Blj', 'Bgp', 'Wee', 'Bkn', 'Wbg', 'Bre', 'Wrd', 'Wsc', 'Wrc', 'Whh', 'Wik', 'Wsa', 'Bri', 'Bsj', 'Bog', 'Bmk', 'Bbm', 'Wbp', 'Wdr', 'Wpo', 'Bmo', 'Wph', 'Bnq', 'Bij', 'Bfi', 'Wcf', 'Wde', 'Brh', 'Wqg', 'Bqh', 'Wrn', 'Bpl', 'Wrp', 'Brg', 'Brj', 'Wrk', 'Wsb', 'Wse', 'Wqa', 'Wea', 'Wel', 'Bfk', 'Wfm', 'Wgq', 'Beo', 'Wda', 'Wqi', 'Bsk', 'Wbh', 'Baj', 'Bsa', 'Whs', 'Wsg', 'Bsh', 'Baa', 'Blk', 'Wpc', 'Bpq', 'Wpe', 'Blp', 'Bld', 'Wbl', 'Bii', 'Whk', 'Bkd', 'Bkg', 'Wcs', 'Was', 'Brp', 'Brq', 'Wom', 'Bso', 'Bsn', 'Wsm', 'Bsp', 'Wan', 'Bks', 'Wga', 'Woa', 'Wpb', 'Bgc', 'Bjc', 'Wrq', 'Wdd', 'Wob', 'Wfl', 'Bca', 'Bba', 'Wad', 'Wsr', 'Bpj', 'Wkk', 'Wlr', 'Bmq', 'Wsl', 'Bns', 'Bsi', 'Brs', 'Bss', 'Wsq', 'Wcn', 'Bdc', 'Bor', 'Bqn', 'Bag', 'Wms', 'Wsi', 'Wrh', 'Bam', 'Bpd', 'Wra', 'Wah', 'Bka', 'Wae', 'Wrr', 'Bjb', 'Bcs', 'Wsd', 'Wrs', 'Wqs', 'Wbs', 'Wpa', 'Wqr', 'Bsr', 'Bnr', 'Bsf', 'Bja', 'Bmr', 'Wpr', 'Wsp', 'Wss', 'Baf', 'Bsq', 'B', 'W', 'BTR', 'WTR', ',']
#
#
#
#
# f ="W[]C"
# print(f[:3])
# s =f[:3]
# s2 = s.replace("[", "")
# s3 = s2.replace("]", "")
# print(s3)
#


#
# import graphviz
#
# dot = graphviz.Digraph(comment='围棋神经网络')
#
# # 添加节点
# dot.node('I1', '输入层')
# dot.node('H1', '隐藏层1')
# dot.node('H2', '隐藏层2')
# dot.node('O1', '输出层')
#
# # 添加边
# dot.edge('I1', 'H1')
# dot.edge('H1', 'H2')
# dot.edge('H2', 'O1')
#
# # 绘制图形
# dot.render('go_neural_network', view=True)

# from mayavi import mlab
# import numpy as np
#
# # 生成数据
# x, y, z = np.mgrid[-10:10:20j, -10:10:20j, -10:10:20j]
# scalars = x * x + y * y + z * z
#
# # 绘制3D图
# mlab.contour3d(scalars, contours=8, transparent=True)
# mlab.show()
#
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
#
# # 读取围棋棋谱并转换为二维数组
# board = pd.read_csv('board.csv', header=None)
# board_array = np.array(board)
#
# # 调用神经网络模型，获取每个位置的注意力分布
# attention_map = model.predict(board_array)
#
# # 将注意力分布数据转换为二维数组，并与围棋棋谱数组进行合并
# attention_map = np.reshape(attention_map, (19, 19))
# attention_map_with_board = np.hstack((board_array, attention_map))
#
# # 使用matplotlib库来绘制出合并后的数组，形成注意力分布图
# plt.imshow(attention_map_with_board, cmap='coolwarm')
# plt.axis('off')
# plt.show()





