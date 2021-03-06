from difflib import SequenceMatcher

real2name = {
1: "республика адыгея",
2: "республика башкортостан",
102: "республика башкортостан",
3: "республика бурятия",
4: "республика алтай",
5: "республика дагестан",
6: "республика ингушетия",
7: "кабардино-балкарская республика",
8: "республика калмыкия",
9: "республика карачаево-черкессия",
10: "республика карелия",
11: "республика коми",
12: "республика марий эл",
13: "республика мордовия",
113: "республика мордовия",
14: "республика саха",
15: "республика северная осетия",
16: " республика татарстан",
116: "республика татарстан",
716: "республика татарстан",
17: "республика тыва",
18: "удмуртская республика",
19: "республика хакасия",
21: "чувашская республика",
121: "чувашская республика",
22: "алтайский край",
23: "краснодарский край",
93: "краснодарский край",
123: "краснодарский край",
24: "красноярский край",
84: "красноярский край",
88: "красноярский край",
124: "красноярский край",
25: " приморский край",
125: "приморский край",
26: "ставропольский край",
126: "ставропольский край",
27: "хабаровский край",
28: "амурская область",
29: "архангельская область",
30: "астраханская область",
31: "белгородская область",
32: "брянская область",
33: "владимирская область",
34: "волгоградская область",
134: "волгоградская область",
35: "вологодская область",
36: "воронежская область",
136: "воронежская область",
37: "ивановская область",
38: "иркутская область",
85: "иркутская область",
138: "иркутская область",
39: "калининградская область",
91: "калининградская область",
40: "калужская область",
41: "камчатский край",
42: "кемеровская область",
142: "кемеровская область",
43: "кировская область",
44: "костромская область",
45: "курганская область",
46: "курская область",
47: "ленинградская область",
147: "ленинградская область",
48: "липецкая область",
49: "магаданская область",
50: "московская область",
90: "московская область",
150: "московская область",
190: "московская область",
750: "московская область",
51: "мурманская область",
52: "нижегородская область",
152: "нижегородская область",
53: "новгородская область",
54: "новосибирская область",
154: "новосибирская область",
55: "омская область",
56: "оренбургская область",
57: "орловская область",
58: "пензенская область",
59: "пермский край",
81: "пермский край",
159: "пермский край",
60: "псковская область",
61: "ростовская область",
161: "ростовская область",
62: "рязанская область",
63: "самарская область",
163: "самарская область",
763: "самарская область",
64: "саратовская область",
164: "саратовская область",
65: "сахалинская область",
66: "свердловская область",
96: "свердловская область",
196: "свердловская область",
67: "смоленская область",
68: "тамбовская область",
69: "тверская область",
70: "томская область",
71: "тульская область",
72: "тюменская область",
73: "ульяновская область",
173: "ульяновская область",
74: "челябинская область",
174: "челябинская область",
75: "забайкальский край",
80: "забайкальский край",
76: "ярославская область",
77: "москва",
97: "москва",
99: "москва",
177: "москва",
197: "москва",
199: "москва",
777: "москва",
799: "москва",
78: "санкт-петербург",
98: "санкт-петербург",
178: "санкт-петербург",
198: "санкт-петербург",
79: "еврейская автономная область",
82: "республика крым",
83: "ненецкий автономный округ",
86: " ханты-мансийский автономный округ ",
186: "ханты-мансийский автономный округ",
87: "чукотский автономный округ",
89: "ямало-ненецкий автономный округ",
92: "севастополь",
95: "чеченская республика"
}

name2real = {
'республика адыгея': [1],
'республика башкортостан': [2, 102],
'республика бурятия': [3],
'республика алтай': [4],
'республика дагестан': [5],
'республика ингушетия': [6],
'кабардино-балкарская республика': [7],
'республика калмыкия': [8],
'республика карачаево-черкессия': [9],
'республика карелия': [10],
'республика коми': [11],
'республика марий Эл': [12],
'республика мордовия': [13, 113],
'республика саха (якутия)': [14],
'республика северная осетия': [15],
'республика татарстан': [16, 116, 716],
'республика тыва': [17],
'удмуртская республика': [18],
'республика хакасия': [19],
'чувашская республика': [21, 121],
'алтайский край': [22],
'краснодарский край': [23, 93, 123],
'красноярский край': [24, 84, 88, 124],
'приморский край': [25],
'приморский край': [125],
'ставропольский край': [26, 126],
'хабаровский край': [27],
'амурская область': [28],
'архангельская область': [29],
'астраханская область': [30],
'белгородская область': [31],
'брянская область': [32],
'владимирская область': [33],
'волгоградская область': [34, 134],
'вологодская область': [35],
'воронежская область': [36, 136],
'ивановская область': [37],
'иркутская область': [38, 85, 138],
'калининградская область': [39, 91],
'калужская область': [40],
'камчатский край': [41],
'кемеровская область': [42, 142],
'кировская область': [43],
'костромская область': [44],
'курганская область': [45],
'курская область': [46],
'ленинградская область': [47, 147],
'липецкая область': [48],
'магаданская область': [49],
'московская область': [50, 90, 150, 190, 750],
'мурманская область': [51],
'нижегородская область': [52, 152],
'новгородская область': [53],
'новосибирская область': [54, 154],
'омская область': [55],
'оренбургская область': [56],
'орловская область': [57],
'пензенская область': [58],
'пермский край': [59, 81, 159],
'псковская область': [60],
'ростовская область': [61, 161],
'рязанская область': [62],
'самарская область': [63, 163, 763],
'саратовская область': [64, 164],
'сахалинская область': [65],
'свердловская область': [66, 96, 196],
'смоленская область': [67],
'тамбовская область': [68],
'тверская область': [69],
'томская область': [70],
'тульская область': [71],
'тюменская область': [72],
'ульяновская область': [73, 173],
'челябинская область': [74, 174],
'забайкальский край': [75, 80],
'ярославская область': [76],
'москва': [77, 97, 99, 177, 197, 199, 777, 799],
'санкт-петербург': [78, 98, 178, 198],
'еврейская автономная область': [79],
'республика крым': [82],
'ненецкий автономный округ': [83],
'ханты-мансийский автономный округ ': [86],
'ханты-мансийский автономный округ': [186],
'чукотский автономный округ': [87],
'ямало-ненецкий автономный округ': [89],
'севастополь': [92],
'чеченская республика': [95]
}

first2names = {'не': ['ненецкий автономный округ'],
'ни': ['нижегородская область'],
'вл': ['владимирская область'],
'кр': ['красноярский край',
'краснодарский край'],
'св': ['свердловская область'],
'во': ['волгоградская область',
'вологодская область',
'воронежская область'],
'тю': ['тюменская область'],
'ка': ['камчатский край',
'калининградская область',
'кабардино-балкарская республика',
'калужская область'],
'ст': ['ставропольский край'],
'ре': ['республика калмыкия',
'республика хакасия',
'республика башкортостан',
'республика алтай',
'республика тыва',
'республика крым',
'республика карелия',
'республика северная осетия',
'республика дагестан',
'республика мордовия',
'республика бурятия',
'республика коми',
'республика адыгея',
'республика татарстан',
'республика ингушетия',
'республика саха',
'республика марий эл',
'республика карачаево-черкессия'],
'чу': ['чувашская республика',
'чукотский автономный округ'],
'ту': ['тульская область'],
'ас': ['астраханская область'],
'ро': ['ростовская область'],
'пр': ['приморский край'],
'см': ['смоленская область'],
'пе': ['пермский край',
'пензенская область'],
'са': ['сахалинская область',
'санкт-петербург',
'саратовская область',
'самарская область'],
'ря': ['рязанская область'],
'ки': ['кировская область'],
'ив': ['ивановская область'],
'му': ['мурманская область'],
'ха': ['хабаровский край',
'ханты-мансийский автономный округ ',
'ханты-мансийский автономный округ'],
'ма': ['магаданская область'],
'за': ['забайкальский край'],
'но': ['новгородская область',
'новосибирская область'],
'тв': ['тверская область'],
'се': ['севастополь'],
'бе': ['белгородская область'],
'ку': ['курганская область',
'курская область'],
'ар': ['архангельская область'],
'ор': ['оренбургская область',
'орловская область'],
'ке': ['кемеровская область'],
'то': ['томская область'],
'яр': ['ярославская область'],
'ев': ['еврейская автономная область'],
'мо': ['московская область',
'москва'],
'ям': ['ямало-ненецкий автономный округ'],
'ко': ['костромская область'],
'ле': ['ленинградская область'],
'ли': ['липецкая область'],
'ул': ['ульяновская область'],
'ом': ['омская область'],
'ал': ['алтайский край'],
'ам': ['амурская область'],
'че': ['чеченская республика',
       'челябинская область'],
'пс': ['псковская область'],
'та': ['тамбовская область'],
'уд': ['удмуртская республика'],
'ир': ['иркутская область'],
'бр': ['брянская область']
}

def get_nearest(name: str):
    name = name.lower()
    candidates = first2names[name[:2]]
    nearest = 0
    best = candidates[0]
    for candidate in candidates:
        rat = SequenceMatcher(None, name, candidate).ratio()
        if rat > nearest:
            nearest = rat
            best = candidate
    return best
