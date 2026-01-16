# tests.py
# Struktur: "Gün X": [(sual_text, [variant1, variant2, variant3], düzgün_index)]

daily_tests = {
    "Gün 1": [
        ("سلام **hansı bənddə düzgün yazılıb?**", ["salam", "selam", "sallam"], 0),
        ("دوست **hansı bənddə düzgün yazılıb?**", ["dust", "dostt", "doost"], 0),
        ("کتاب **hansı bənddə düzgün yazılıb?**", ["ketab", "kitab", "katab"], 0),
        ("İndiki zaman fel **hansı cümlədə düzgündür?**", ["من می‌روم", "من رفتم", "من خواهم رفت"], 0),
        ("İndiki zaman fel **hansı cümlədə düzgündür?**", ["تو می‌خوانی", "او نوشت", "ما خواهیم آمد"], 0)
    ],
    "Gün 2": [
        ("مدرسه **hansı bənddə düzgün yazılıb?**", ["madrese", "madraze", "madres"], 0),
        ("معلم **hansı bənddə düzgün yazılıb?**", ["moalem", "moalemm", "mualem"], 0),
        ("دانشجو **hansı bənddə düzgün yazılıb?**", ["daneshju", "daneshjoo", "daneshyoo"], 0),
        ("Zamanların inkarı **hansı cümlədə düzgündür?**", ["من نمی‌روم", "من رفتم", "من می‌روم"], 0),
        ("Zamanların inkarı **hansı cümlədə düzgündür?**", ["تو نمی‌خوانی", "او نوشت", "ما خواهیم آمد"], 0)
    ],    
    "Gün 3": [
        ("خانه **hansı bənddə düzgün yazılıb?**", ["xane", "khane", "khan"], 0),
        ("دوست **hansı bənddə düzgün yazılıb?**", ["dust", "doost", "dost"], 0),
        ("کتاب **hansı bənddə düzgün yazılıb?**", ["ketab", "kitab", "katab"], 0),
        ("Məchul fel **hansı cümlədə düzgündür?**", ["کتاب خوانده می‌شود", "کتاب خواند", "کتاب می‌خواند"], 0),
        ("Məchul fel **hansı cümlədə düzgündür?**", ["خانه تمیز می‌شود", "خانه تمیز کرد", "خانه تمیز می‌کند"], 0)
    ],
    "Gün 4": [
        ("دوچرخه **hansı bənddə düzgün yazılıb?**", ["docharkhe", "docharkh", "docharh"], 0),
        ("هواپیما **hansı bənddə düzgün yazılıb?**", ["havapeyma", "havapema", "havapima"], 0),
        ("ماشین **hansı bənddə düzgün yazılıb?**", ["mashin", "mashien", "mashinm"], 0),
        ("Əmr fel **hansı cümlədə düzgündür?**", ["بخوان!", "نوشت!", "خواهد آمد!"], 0),
        ("Əmr fel **hansı cümlədə düzgündür?**", ["بیایید!", "من می‌روم", "شما خواهید خواند"], 0)
    ],
    "Gün 5": [
        ("سیب **hansı bənddə düzgün yazılıb?**", ["sib", "seeb", "sibp"], 0),
        ("موز **hansı bənddə düzgün yazılıb?**", ["moz", "mouz", "mooz"], 0),
        ("پرتقال **hansı bənddə düzgün yazılıb?**", ["porteghal", "portegal", "porteghel"], 0),
        ("Əmr fel **hansı cümlədə düzgündür?**", ["بخوان!", "نوشت!", "خواهد آمد!"], 0),
("Əmr fel **hansı cümlədə düzgündür?**", ["بیایید!", "من می‌روم", "شما خواهید خواند"], 0)
    ],

    "Gün 6": [
        ("کتابخانه **hansı bənddə düzgün yazılıb?**", ["ketabkhane", "ketabkhan", "kitabkhane"], 0),
        ("میز **hansı bənddə düzgün yazılıb?**", ["miz", "meez", "mis"], 0),
        ("پنجره **hansı bənddə düzgün yazılıb?**", ["panjare", "panjaraa", "panjareh"], 0),
        ("Keçmiş sadə fel **hansı cümlədə düzgündür?**", ["من رفتم", "من می‌روم", "من خواهم رفت"], 0),
("Keçmiş sadə fel **hansı cümlədə düzgündür?**", ["او نوشت", "ما می‌خوانیم", "شما خواهید آمد"], 0)
    ],
    "Gün 7": [
        ("دوست **hansı bənddə düzgün yazılıb?**", ["dust", "dost", "doost"], 0),
        ("قلم **hansı bənddə düzgün yazılıb?**", ["qalam", "qalem", "qaalem"], 0),
        ("دفتر **hansı bənddə düzgün yazılıb?**", ["daftar", "defter", "daftarr"], 0),
        ("Yaxın keçmiş nəqli **hansı cümlədə düzgündür?**", ["من رفته‌ام", "من می‌روم", "من خواهم رفت"], 0),
("Yaxın keçmiş nəqli **hansı cümlədə düzgündür?**", ["تو خوانده‌ای", "او نوشت", "ما خواهیم آمد"], 0)
    ],
    # Gün 8
    "Gün 8": [
        ("پنیر **hansı bənddə düzgün yazılıb?**", ["panir", "penir", "peynir"], 0),
        ("نان **hansı bənddə düzgün yazılıb?**", ["nan", "naan", "nann"], 0),
        ("چای **hansı bənddə düzgün yazılıb?**", ["chay", "chai", "chayy"], 0),
        ("Keçmiş davamedici fel **hansı cümlədə düzgündür?**", ["من می‌رفتم", "من رفته‌ام", "من خواهم رفت"], 0),
("Keçmiş davamedici fel **hansı cümlədə düzgündür?**", ["او می‌نوشت", "ما می‌خوانیم", "شما خواهید آمد"], 0)
    ],
    # Gün 9
    "Gün 9": [
        ("سیب **hansı bənddə düzgün yazılıb?**", ["sib", "seeb", "sibp"], 0),
        ("موز **hansı bənddə düzgün yazılıb?**", ["moz", "mooz", "moozz"], 0),
        ("پرتقال **hansı bənddə düzgün yazılıb?**", ["porteghal", "portegal", "porteghel"], 0),
        ("Uzaq keçmiş **hansı cümlədə düzgündür?**", ["من رفته بودم", "من می‌روم", "من خواهم رفت"], 0),
("Uzaq keçmiş **hansı cümlədə düzgündür?**", ["او نوشت", "ما می‌خوانیم", "شما خواهید آمد"], 0)
    ],
    # Gün 10
"Gün 10": [
    ("خانه **hansı bənddə düzgün yazılıb?**", ["xane", "khane", "khan"], 0),
    ("کتاب **hansı bənddə düzgün yazılıb?**", ["ketab", "kitab", "katab"], 0),
    ("دوست **hansı bənddə düzgün yazılıb?**", ["dust", "dost", "doost"], 0),
    ("Fellərin hallanması **hansı cümlədə düzgündür?**", ["من می‌روم", "من رفتم", "من خواهم رفت"], 0),
    ("Fellərin hallanması **hansı cümlədə düzgündür?**", ["تو می‌روی", "او رفت", "ما خواهیم آمد"], 0)
],

"Gün 11": [
    ("کتابچه **hansı bənddə düzgün yazılıb?**", ["ketabche", "ketabch", "kitabche"], 0),
    ("مداد **hansı bənddə düzgün yazılıb?**", ["medad", "maddad", "medaad"], 0),
    ("کاغذ **hansı bənddə düzgün yazılıb?**", ["kaghaz", "kagaz", "kaghazz"], 0),
    ("Sifət **hansı cümlədə düzgündür?**", ["خانه بزرگ", "خانه بزرگ است", "خانه می‌رود"], 0),
    ("Sifət **hansı cümlədə düzgündür?**", ["روز زیبا", "ما زیبا می‌رویم", "زیبا می‌خواند"], 0)
],

"Gün 12": [
    ("دوچرخه **hansı bənddə düzgün yazılıb?**", ["docharkhe", "docharh", "dochark"], 0),
    ("هواپیما **hansı bənddə düzgün yazılıb?**", ["havapeyma", "havapema", "havapima"], 0),
    ("ماشین **hansı bənddə düzgün yazılıb?**", ["mashin", "mashien", "mashine"], 0),
    ("Say məchul/məful **hansı cümlədə düzgündür?**", ["دو کتاب خوانده شد", "کتاب دو خوانده شد", "دو خوانده شد کتاب"], 0),
    ("Say məchul/məful **hansı cümlədə düzgündür?**", ["سه مدرسه ساخته شد", "مدرسه سه ساخته شد", "سه ساخته شد مدرسه"], 0)
],

"Gün 13": [
    ("دوست **hansı bənddə düzgün yazılıb?**", ["dust", "doost", "dost"], 0),
    ("قلم **hansı bənddə düzgün yazılıb?**", ["qalam", "qalem", "qaalem"], 0),
    ("دفتر **hansı bənddə düzgün yazılıb?**", ["daftar", "defter", "daftarr"], 0),
    ("Şəxs əvəzlikləri **hansı cümlədə düzgündür?**", ["من می‌روم", "تو می‌خوانی", "ما خواهیم رفت"], 0),
    ("Şəxs əvəzlikləri **hansı cümlədə düzgündür?**", ["او می‌نویسد", "من رفتم", "شما می‌خوانید"], 0)
],

"Gün 14": [
    ("پنیر **hansı bənddə düzgün yazılıb?**", ["panir", "penir", "peynir"], 0),
    ("نان **hansı bənddə düzgün yazılıb?**", ["nan", "naan", "nann"], 0),
    ("چای **hansı bənddə düzgün yazılıb?**", ["chay", "chai", "chayy"], 0),
    ("Bitişik şəxs əvəzlikləri **hansı cümlədə düzgündür?**", ["کتابم", "من کتابم", "کتابم من"], 0),
    ("Bitişik şəxs əvəzlikləri **hansı cümlədə düzgündür?**", ["خانه ما", "ما خانه ما", "خانه ما ما"], 0)
],

"Gün 15": [
    ("سیب **hansı bənddə düzgün yazılıb?**", ["sib", "seeb", "sibp"], 0),
    ("موز **hansı bənddə düzgün yazılıb?**", ["moz", "mouz", "mooz"], 0),
    ("پرتقال **hansı bənddə düzgün yazılıb?**", ["porteghal", "portegal", "porteghel"], 0),
    ("Gizli fellər **hansı cümlədə düzgündür?**", ["رفتم (من)", "من رفتم", "رفتم من"], 0),
    ("Gizli fellər **hansı cümlədə düzgündür?**", ["خواندی (تو)", "تو خواندی", "خواندی تو"], 0)
],

"Gün 16": [
    ("خانه **hansı bənddə düzgün yazılıb?**", ["xane", "khane", "khan"], 0),
    ("کتاب **hansı bənddə düzgün yazılıb?**", ["ketab", "kitab", "katab"], 0),
    ("دوست **hansı bənddə düzgün yazılıb?**", ["dust", "doost", "dost"], 0),
    ("Cümlə qurluşu **hansı cümlədə düzgündür?**", ["من به مدرسه می‌روم", "مدرسه من می‌روم", "من می‌روم به مدرسه"], 0),
    ("Cümlə qurluşu **hansı cümlədə düzgündür?**", ["او کتاب می‌خواند", "کتاب او می‌خواند", "می‌خواند او کتاب"], 0)
],

"Gün 17": [
    ("دوچرخه **hansı bənddə düzgün yazılıb?**", ["docharkhe", "docharh", "dochark"], 0),
    ("هواپیما **hansı bənddə düzgün yazılıb?**", ["havapeyma", "havapema", "havapima"], 0),
    ("ماشین **hansı bənddə düzgün yazılıb?**", ["mashin", "mashien", "mashine"], 0),
    ("İsmin hal şəkilçiləri **hansı cümlədə düzgündür?**", ["خانه‌ی (مضاف)", "خانه (مضاف) خانه‌ی", "خانه‌ی خانه مضاف"], 0),
    ("İsmin hal şəkilçiləri **hansı cümlədə düzgündür?**", ["به خانه (مجرور)", "مجرور به خانه", "به خانه خانه مجرور"], 0)
],

"Gün 18": [
    ("مدرسه **hansı bənddə düzgün yazılıb?**", ["madrese", "madraze", "madres"], 0),
    ("معلم **hansı bənddə düzgün yazılıb?**", ["moalem", "moalemm", "mualem"], 0),
    ("دانشجو **hansı bənddə düzgün yazılıb?**", ["daneshju", "daneshjoo", "daneshyoo"], 0),
    ("Qəti indiki hal xəbər cümləsi **hansı cümlədə düzgündür?**", ["من الان می‌روم", "من رفتم الان", "الان من می‌روم"], 0),
    ("Qəti indiki hal xəbər cümləsi **hansı cümlədə düzgündür?**", ["تو الان می‌خوانی", "تو می‌خوانی الان", "الان می‌خوانی تو"], 0)
],

"Gün 19": [
    ("کتاب **hansı bənddə düzgün yazılıb?**", ["ketab", "kitab", "katab"], 0),
    ("قلم **hansı bənddə düzgün yazılıb?**", ["qalam", "qalem", "qaalem"], 0),
    ("دفتر **hansı bənddə düzgün yazılıb?**", ["daftar", "defter", "daftarr"], 0),
    ("İndiki zaman fel **hansı cümlədə düzgündür?**", ["من می‌خوانم", "من خواهم خواند", "من خواندم"], 0),
    ("Məchul fel **hansı cümlədə düzgündür?**", ["خانه تمیز می‌شود", "خانه تمیز کرد", "خانه تمیز می‌کند"], 0)
],

"Gün 20": [
    ("دوست **hansı bənddə düzgün yazılıb?**", ["dust", "doost", "dost"], 0),
    ("خانه **hansı bənddə düzgün yazılıb?**", ["xane", "khane", "khan"], 0),
    ("کتابچه **hansı bənddə düzgün yazılıb?**", ["ketabche", "ketabch", "kitabche"], 0),
    ("Keçmiş sadə **hansı cümlədə düzgündür?**", ["من رفتم", "من می‌روم", "من خواهم رفت"], 0),
    ("Keçmiş sadə **hansı cümlədə düzgündür?**", ["تو خواندی", "تو می‌خوانی", "تو خواهی خواند"], 0)
],

"Gün 21": [
    ("سیب **hansı bənddə düzgün yazılıb?**", ["sib", "seeb", "sibp"], 0),
    ("پرتقال **hansı bənddə düzgün yazılıb?**", ["porteghal", "portegal", "porteghel"], 0),
    ("موز **hansı bənddə düzgün yazılıb?**", ["moz", "mouz", "mooz"], 0),
    ("Yaxın keçmiş nəqli **hansı cümlədə düzgündür?**", ["من رفته‌ام", "من رفتم", "من خواهم رفت"], 0),
    ("Yaxın keçmiş nəqli **hansı cümlədə düzgündür?**", ["تو خوانده‌ای", "تو خواهی خواند", "تو خواندی"], 0)
],

"Gün 22": [
    ("دوچرخه **hansı bənddə düzgün yazılıb?**", ["docharkhe", "docharh", "dochark"], 0),
    ("هواپیما **hansı bənddə düzgün yazılıb?**", ["havapeyma", "havapema", "havapima"], 0),
    ("ماشین **hansı bənddə düzgün yazılıb?**", ["mashin", "mashien", "mashine"], 0),
    ("Keçmiş davamedici **hansı cümlədə düzgündür?**", ["من می‌رفتم", "من رفته بودم", "من خواهم رفت"], 0),
    ("Keçmiş davamedici **hansı cümlədə düzgündür?**", ["تو می‌خواندی", "تو خواندی", "تو خواهی خواند"], 0)
],

"Gün 23": [
    ("کتاب **hansı bənddə düzgün yazılıb?**", ["ketab", "kitab", "katab"], 0),
    ("قلم **hansı bənddə düzgün yazılıb?**", ["qalam", "qalem", "qaalem"], 0),
    ("دفتر **hansı bənddə düzgün yazılıb?**", ["daftar", "defter", "daftarr"], 0),
    ("Uzaq keçmiş **hansı cümlədə düzgündür?**", ["من رفته بودم", "من می‌روم", "من رفتم"], 0),
    ("Uzaq keçmiş **hansı cümlədə düzgündür?**", ["تو رفته بودی", "تو خواندی", "تو خواهی خواند"], 0)
],

"Gün 24": [
    ("دوست **hansı bənddə düzgün yazılıb?**", ["dust", "doost", "dost"], 0),
    ("خانه **hansı bənddə düzgün yazılıb?**", ["xane", "khane", "khan"], 0),
    ("کتابچه **hansı bənddə düzgün yazılıb?**", ["ketabche", "ketabch", "kitabche"], 0),
    ("Fellərin hallanması **hansı cümlədə düzgündür?**", ["من می‌روم", "من رفتم", "من خواهم رفت"], 0),
    ("Fellərin hallanması **hansı cümlədə düzgündür?**", ["تو می‌روی", "تو رفتی", "تو خواهی رفت"], 0)
],

    "Gün 25": [
    ("پنیر **hansı bənddə düzgün yazılıb?**", ["panir", "penir", "peynir"], 0),
    ("نان **hansı bənddə düzgün yazılıb?**", ["nan", "naan", "nann"], 0),
    ("چای **hansı bənddə düzgün yazılıb?**", ["chay", "chai", "chayy"], 0),
    ("Sifət **hansı cümlədə düzgündür?**", ["خانه بزرگ", "خانه بزرگ است", "خانه می‌رود"], 0),
    ("Sifət **hansı cümlədə düzgündür?**", ["روز زیبا", "ما زیبا می‌رویم", "زیبا می‌خواند"], 0)
],

"Gün 26": [
    ("سیب **hansı bənddə düzgün yazılıb?**", ["sib", "seeb", "sibp"], 0),
    ("موز **hansı bənddə düzgün yazılıb?**", ["moz", "mouz", "mooz"], 0),
    ("پرتقال **hansı bənddə düzgün yazılıb?**", ["porteghal", "portegal", "porteghel"], 0),
    ("Şəxs əvəzlikləri **hansı cümlədə düzgündür?**", ["من می‌روم", "تو می‌خوانی", "ما خواهیم رفت"], 0),
    ("Şəxs əvəzlikləri **hansı cümlədə düzgündür?**", ["او می‌نویسد", "من رفتم", "شما می‌خوانید"], 0)
],

"Gün 27": [
    ("دوچرخه **hansı bənddə düzgün yazılıb?**", ["docharkhe", "docharh", "dochark"], 0),
    ("هواپیما **hansı bənddə düzgün yazılıb?**", ["havapeyma", "havapema", "havapima"], 0),
    ("ماشین **hansı bənddə düzgün yazılıb?**", ["mashin", "mashien", "mashine"], 0),
    ("Bitişik şəxs əvəzlikləri **hansı cümlədə düzgündür?**", ["کتابم", "من کتابم", "کتابم من"], 0),
    ("Bitişik şəxs əvəzlikləri **hansı cümlədə düzgündür?**", ["خانه ما", "ما خانه ما", "خانه ما ما"], 0)
],

"Gün 28": [
    ("کتاب **hansı bənddə düzgün yazılıb?**", ["ketab", "kitab", "katab"], 0),
    ("قلم **hansı bənddə düzgün yazılıb?**", ["qalam", "qalem", "qaalem"], 0),
    ("دفتر **hansı bənddə düzgün yazılıb?**", ["daftar", "defter", "daftarr"], 0),
    ("Gizli fellər **hansı cümlədə düzgündür?**", ["رفتم (من)", "خواندم (من)", "خواهم رفت (من)"], 0),
    ("Gizli fellər **hansı cümlədə düzgündür?**", ["خواندی (تو)", "تو خواندی", "او نوشت"], 0)
],

"Gün 29": [
    ("دوست **hansı bənddə düzgün yazılıb?**", ["dust", "doost", "dost"], 0),
    ("خانه **hansı bənddə düzgün yazılıb?**", ["xane", "khane", "khan"], 0),
    ("کتابچه **hansı bənddə düzgün yazılıb?**", ["ketabche", "ketabch", "kitabche"], 0),
    ("Cümlə qurluşu **hansı cümlədə düzgündür?**", ["من به مدرسه می‌روم", "مدرسه من می‌روم", "من می‌روم به مدرسه"], 0),
    ("Cümlə qurluşu **hansı cümlədə düzgündür?**", ["او کتاب می‌خواند", "کتاب او می‌خواند", "می‌خواند او کتاب"], 0)
],

"Gün 30": [
    ("پنیر **hansı bənddə düzgün yazılıb?**", ["panir", "penir", "peynir"], 0),
    ("نان **hansı bənddə düzgün yazılıb?**", ["nan", "naan", "nann"], 0),
    ("چای **hansı bənddə düzgün yazılıb?**", ["chay", "chai", "chayy"], 0),
    ("İsmin hal şəkilçiləri **hansı cümlədə düzgündür?**", ["خانه‌ی (مضاف)", "به خانه (مجرور)", "خانه (مفعول)"], 0),
    ("İsmin hal şəkilçiləri **hansı cümlədə düzgündür?**", ["او خانه را", "خانه برای او", "خانه او"], 0)
],
}
