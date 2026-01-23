# word.py
# Struktur: {"Gün 1": [(fars, tələffüz, tərcümə), ...], "Gün 2": [...], ...}

daily_words = {
    "Gün 1": [
        ("سلام", "salam", "Salam"),
        ("خوب", "xub", "Yaxşı"),
        ("دوست", "dust", "Dost"),
        ("کتاب", "ketab", "Kitab"),
        ("خانه", "xane", "Ev")
    ],
    "Gün 2": [
        ("مدرسه", "madrese", "Məktəb"),
        ("معلم", "moalem", "Müəllim"),
        ("دانشجو", "daneshju", "Tələbə"),
        ("درس", "dars", "Dərs"),
        ("قلم", "qalam", "Qələm")
    ],
    "Gün 3": [
        ("میز", "miz", "Masa"),
        ("صندلی", "sandali", "Stul"),
        ("پنجره", "panjere", "Pəncərə"),
        ("در", "dar", "Qapı"),
        ("دیوار", "divar", "Divar")
    ],
    "Gün 4": [
        ("ماشین", "mashin", "Maşın"),
        ("دوچرخه", "docharkhe", "Velosiped"),
        ("اتوبوس", "otobus", "Avtobus"),
        ("قطار", "ghatar", "Qatar"),
        ("هواپیما", "havapeyma", "Təyyarə")
    ],
    "Gün 5": [
    ("سیب", "sib", "Alma"),
    ("موز", "moz", "Banan"),
    ("پرتقال", "porteghal", "Portağal"),
    ("انگور", "angur", "Üzüm"),
    ("هندوانه", "hendavane", "Qarpız"),
    ("انار", "anar", "Nar"),
    ("گلابی", "golabi", "Armud"),
    ("هلو", "holu", "Şaftalı"),
    ("گیلاس", "gilas", "Albalı"),
    ("لیمو", "limu", "Limon")
    ],
"Gün 6": [
    ("آب", "ab", "Su"),
    ("چای", "chay", "Çay"),
    ("قهوه", "ghahve", "Qəhvə"),
    ("شیر", "shir", "Süd"),
    ("نان", "nan", "Çörək"),
    ("آبمیوه", "ab-mive", "Şirə"),
    ("دوغ", "dugh", "Ayran"),
    ("عسل", "asal", "Bal"),
    ("پنیر", "panir", "Pendir"),
    ("کره", "kare", "Kərə yağı")
],

"Gün 7": [
    ("خورشید", "khorshid", "Günəş"),
    ("ماه", "mah", "Ay"),
    ("ستاره", "setare", "Ulduz"),
    ("آسمان", "aseman", "Səma"),
    ("ابر", "abr", "Bulud"),
    ("باران", "baran", "Yağış"),
    ("برف", "barf", "Qar"),
    ("باد", "bad", "Külək"),
    ("رعد", "ra'd", "Göy gurultusu"),
    ("نور", "nur", "İşıq")
],

"Gün 8": [
    ("زمین", "zamin", "Yer"),
    ("کوه", "kuh", "Dağ"),
    ("دریا", "darya", "Dəniz"),
    ("رود", "rud", "Çay"),
    ("جنگل", "jangal", "Meşə"),
    ("بیابان", "biyaban", "Səhra"),
    ("دشت", "dasht", "Düzənlik"),
    ("جزیره", "jazire", "Ada"),
    ("ساحل", "sahel", "Sahil"),
    ("غار", "ghar", "Mağara")
],

"Gün 9": [
    ("پدر", "pedar", "Ata"),
    ("مادر", "madar", "Ana"),
    ("برادر", "baradar", "Qardaş"),
    ("خواهر", "khahar", "Bacı"),
    ("خانواده", "khanevade", "Ailə"),
    ("پدربزرگ", "pedarbozorg", "Baba"),
    ("مادربزرگ", "madarbozorg", "Nənə"),
    ("عمو", "amu", "Əmi"),
    ("دایی", "dayi", "Dayı"),
    ("خاله", "khale", "Xala")
],

"Gün 10": [
    ("دو", "do", "İki"),
    ("سه", "se", "Üç"),
    ("چهار", "chahar", "Dörd"),
    ("پنج", "panj", "Beş"),
    ("شش", "shesh", "Altı"),
    ("هفت", "haft", "Yeddi"),
    ("هشت", "hasht", "Səkkiz"),
    ("نه", "noh", "Doqquz"),
    ("ده", "dah", "On"),
    ("یازده", "yazdah", "On bir")
],
    
"Gün 11": [
    ("هفت", "haft", "Yeddi"),
    ("هشت", "hasht", "Səkkiz"),
    ("نه", "noh", "Doqquz"),
    ("ده", "dah", "On"),
    ("بیست", "bist", "İyirmi"),
    ("یازده", "yazdah", "On bir"),
    ("دوازده", "davazdah", "On iki"),
    ("سیزده", "sizdah", "On üç"),
    ("چهارده", "chahardah", "On dörd"),
    ("پانزده", "panzdah", "On beş")
],

"Gün 12": [
    ("صبح", "sobh", "Səhər"),
    ("ظهر", "zohr", "Günorta"),
    ("عصر", "asr", "Axşamüstü"),
    ("غروب", "ghorub", "Gün batımı"),
    ("شب", "shab", "Gecə"),
    ("امروز", "emruz", "Bu gün"),
    ("فردا", "farda", "Sabah"),
    ("دیروز", "dirooz", "Dünən"),
    ("هفته", "hafte", "Həftə"),
    ("ماه", "mah", "Ay")
],

"Gün 13": [
    ("دویدن", "davidan", "Qaçmaq"),
    ("خوابیدن", "khabidan", "Yatmaq"),
    ("خواندن", "khandan", "Oxumaq"),
    ("نوشتن", "neveshtan", "Yazmaq"),
    ("خوردن", "khordan", "Yemək"),
    ("آشامیدن", "ashamidan", "İçmək"),
    ("نشستن", "neshastan", "Oturmaq"),
    ("ایستادن", "istadan", "Durmaq"),
    ("دیدن", "didan", "Görmək"),
    ("گفتن", "goftan", "Demək")
],

"Gün 14": [
    ("شنیدن", "shenidan", "Eşitmək"),
    ("رفتن", "raftan", "Getmək"),
    ("آمدن", "amadan", "Gəlmək"),
    ("خریدن", "kharidan", "Almaq"),
    ("فروختن", "forukhtan", "Satmaq"),
    ("باز کردن", "baz kardan", "Açmaq"),
    ("بستن", "bastan", "Bağlamaq"),
    ("کمک کردن", "komak kardan", "Kömək etmək"),
    ("یاد گرفتن", "yad gereftan", "Öyrənmək"),
    ("آموختن", "amukhtan", "Öyrətmək")
],

"Gün 15": [
    ("لباس", "lebas", "Paltar"),
    ("کفش", "kafsh", "Ayaqqabı"),
    ("کلاه", "kolah", "Papaq"),
    ("کیف", "kif", "Çanta"),
    ("ساعت", "sa'at", "Saat"),
    ("پیراهن", "pirahan", "Köynək"),
    ("شلوار", "shalvar", "Şalvar"),
    ("جوراب", "jurab", "Corab"),
    ("کمربند", "kamarband", "Kəmər"),
    ("کت", "kot", "Pencək")
],

"Gün 16": [
    ("دوست داشتن", "dust dashtan", "Sevmək"),
    ("نفرت داشتن", "nefrat dashtan", "Nifrət etmək"),
    ("خندیدن", "khandidan", "Gülmək"),
    ("گریه کردن", "gerye kardan", "Ağlamaq"),
    ("صحبت کردن", "sohbat kardan", "Danışmaq"),
    ("فکر کردن", "fekr kardan", "Düşünmək"),
    ("باور کردن", "bavar kardan", "İnanmaq"),
    ("ترسیدن", "tarsidan", "Qorxmaq"),
    ("خوشحال بودن", "khoshhal budan", "Sevinmək"),
    ("ناراحت بودن", "narahat budan", "Kədərlənmək")
],

"Gün 17": [
    ("بزرگ", "bozorg", "Böyük"),
    ("کوچک", "kuchak", "Kiçik"),
    ("بلند", "boland", "Uzun"),
    ("کوتاه", "kutah", "Qısa"),
    ("سریع", "sari'", "Sürətli"),
    ("کند", "kond", "Yavaş"),
    ("سنگین", "sangin", "Ağır"),
    ("سبک", "sabok", "Yüngül"),
    ("گرم", "garm", "İsti"),
    ("سرد", "sard", "Soyuq")
],

"Gün 18": [
    ("زیبا", "ziba", "Gözəl"),
    ("زشت", "zesht", "Çirkin"),
    ("جالب", "jaleb", "Maraqlı"),
    ("سخت", "sakht", "Çətin"),
    ("ساده", "sade", "Sadə"),
    ("آسان", "asan", "Asan"),
    ("گران", "geran", "Bahalı"),
    ("ارزان", "arzan", "Ucuz"),
    ("نو", "now", "Yeni"),
    ("قدیمی", "ghadimi", "Köhnə")
],

"Gün 19": [
    ("سیب زمینی", "sib zamini", "Kartof"),
    ("گوجه", "goje", "Pomidor"),
    ("هویج", "hivij", "Kök"),
    ("کلم", "kalam", "Kələm"),
    ("پیاز", "piyaz", "Soğan"),
    ("سیر", "sir", "Sarımsaq"),
    ("خیار", "khiyar", "Xiyar"),
    ("بادمجان", "bademjan", "Badımcan"),
    ("فلفل", "felfel", "Bibər"),
    ("کدو", "kadu", "Balqabaq")
],

"Gün 20": [
    ("ماشین لباسشویی", "mashin lebasshuyi", "Paltaryuyan maşın"),
    ("یخچال", "yakhchal", "Soyuducu"),
    ("تلویزیون", "televizion", "Televizor"),
    ("موبایل", "mobile", "Mobil telefon"),
    ("کامپیوتر", "computer", "Kompüter"),
    ("رادیو", "radio", "Radio"),
    ("جاروبرقی", "jarubargui", "Tozsoran"),
    ("اتو", "uto", "Ütü"),
    ("پنکه", "panke", "Ventilyator"),
    ("چراغ", "cheragh", "Lampa")
],

"Gün 21": [
    ("بازار", "bazar", "Bazar"),
    ("فروشگاه", "forushgah", "Mağaza"),
    ("کتابفروشی", "ketabforushi", "Kitab mağazası"),
    ("رستوران", "resturan", "Restoran"),
    ("هتل", "hotel", "Otel"),
    ("بانک", "bank", "Bank"),
    ("داروخانه", "darukhane", "Aptek"),
    ("پارک", "park", "Park"),
    ("سینما", "sinama", "Kino"),
    ("بیمارستان", "bimarestan", "Xəstəxana")
],

"Gün 22": [
    ("دوست", "dust", "Dost"),
    ("همکار", "hamkar", "Həmkar"),
    ("معلم", "moalem", "Müəllim"),
    ("دانشجو", "daneshju", "Tələbə"),
    ("مربی", "morabbi", "Məşqçi"),
    ("پزشک", "pezeshk", "Həkim"),
    ("پرستار", "parastar", "Tibb bacısı"),
    ("کارگر", "kargar", "Fəhlə"),
    ("مدیر", "modir", "Direktor"),
    ("راننده", "ranande", "Sürücü")
],

"Gün 23": [
    ("صبحانه", "sobhan-e", "Səhər yeməyi"),
    ("ناهار", "nahar", "Nahar"),
    ("شام", "sham", "Axşam yeməyi"),
    ("میوه", "mive", "Meyvə"),
    ("سبزی", "sabzi", "Tərəvəz"),
    ("گوشت", "gusht", "Ət"),
    ("ماهی", "mahi", "Balıq"),
    ("برنج", "berenj", "Düyü"),
    ("سوپ", "sup", "Şorba"),
    ("سالاد", "salad", "Salat")
],

"Gün 24": [
    ("مداد", "medad", "Qələm"),
    ("پاک‌کن", "pak-kon", "Silgi"),
    ("دفتر", "daftar", "Dəftər"),
    ("کتابچه", "ketabche", "Kiçik kitab"),
    ("خط‌کش", "khatkesh", "Xətkeş"),
    ("خودکار", "khodkar", "Qələm"),
    ("کیف مدرسه", "kif madrese", "Məktəb çantası"),
    ("تخته", "takhte", "Lövhə"),
    ("گچ", "gach", "Təbaşir"),
    ("ماژیک", "mazhik", "Marker")
],

"Gün 25": [
    ("آبمیوه", "ab-mive", "Şirə"),
    ("چای سبز", "chay-e sabz", "Yaşıl çay"),
    ("قهوه", "ghahve", "Qəhvə"),
    ("شیرینی", "shirini", "Şirniyyat"),
    ("شکلات", "shokolat", "Şokolad"),
    ("کیک", "kik", "Keks"),
    ("بیسکویت", "biskvit", "Peçenye"),
    ("بستنی", "bastani", "Dondurma"),
    ("عسل", "asal", "Bal"),
    ("مربا", "morabba", "Mürəbbə")
],

"Gün 26": [
    ("کتابخانه", "ketabkhane", "Kitabxana"),
    ("مدرسه", "madrese", "Məktəb"),
    ("دانشگاه", "daneshgah", "Universitet"),
    ("کتابفروشی", "ketabforushi", "Kitab mağazası"),
    ("آزمایشگاه", "azmayeshgah", "Laboratoriya"),
    ("کلاس", "kelas", "Sinif"),
    ("امتحان", "emtehan", "İmtahan"),
    ("درس", "dars", "Dərs"),
    ("تکلیف", "taklif", "Ev tapşırığı"),
    ("نمره", "nomre", "Qiymət")
],

"Gün 27": [
    ("سیب", "sib", "Alma"),
    ("موز", "moz", "Banan"),
    ("پرتقال", "porteghal", "Portağal"),
    ("انار", "anar", "Nar"),
    ("هندوانه", "hendavane", "Qarpız"),
    ("انگور", "angur", "Üzüm"),
    ("گلابی", "golabi", "Armud"),
    ("هلو", "holu", "Şaftalı"),
    ("گیلاس", "gilas", "Albalı"),
    ("لیمو", "limu", "Limon")
],

"Gün 28": [
    ("باران", "baran", "Yağış"),
    ("برف", "barf", "Qar"),
    ("باد", "bad", "Külək"),
    ("آفتاب", "aftab", "Günəş"),
    ("رعد و برق", "ra'd o barq", "İldırım"),
    ("ابر", "abr", "Bulud"),
    ("مه", "meh", "Duman"),
    ("طوفان", "tufan", "Fırtına"),
    ("هوا", "hava", "Hava"),
    ("گرما", "garma", "İstilik")
],

"Gün 29": [
    ("خانه", "xane", "Ev"),
    ("مدرسه", "madrese", "Məktəb"),
    ("دفتر", "daftar", "Dəftər"),
    ("کتاب", "ketab", "Kitab"),
    ("موبایل", "mobile", "Mobil telefon"),
    ("میز", "miz", "Masa"),
    ("صندلی", "sandali", "Stul"),
    ("پنجره", "panjere", "Pəncərə"),
    ("در", "dar", "Qapı"),
    ("اتاق", "otagh", "Otaq")
],

"Gün 30": [
    ("دو", "do", "İki"),
    ("سه", "se", "Üç"),
    ("چهار", "chahar", "Dörd"),
    ("پنج", "panj", "Beş"),
    ("شش", "shesh", "Altı"),
    ("هفت", "haft", "Yeddi"),
    ("هشت", "hasht", "Səkkiz"),
    ("نه", "noh", "Doqquz"),
    ("ده", "dah", "On"),
    ("یازده", "yazdah", "On bir")
],

"Gün 31": [
    ("دوازده", "davazdah", "On iki"),
    ("سیزده", "sizdah", "On üç"),
    ("چهارده", "chahardah", "On dörd"),
    ("پانزده", "panzdah", "On beş"),
    ("شانزده", "shanzdah", "On altı"),
    ("هفده", "hefdah", "On yeddi"),
    ("هجده", "hejdah", "On səkkiz"),
    ("نوزده", "nozdah", "On doqquz"),
    ("بیست", "bist", "İyirmi"),
    ("بیست و یک", "bist o yek", "İyirmi bir")
],

"Gün 32": [
    ("بیست و دو", "bist o do", "İyirmi iki"),
    ("بیست و سه", "bist o se", "İyirmi üç"),
    ("بیست و چهار", "bist o chahar", "İyirmi dörd"),
    ("بیست و پنج", "bist o panj", "İyirmi beş"),
    ("بیست و شش", "bist o shesh", "İyirmi altı"),
    ("بیست و هفت", "bist o haft", "İyirmi yeddi"),
    ("بیست و هشت", "bist o hasht", "İyirmi səkkiz"),
    ("بیست و نه", "bist o noh", "İyirmi doqquz"),
    ("سی", "si", "Otuz"),
    ("سی و یک", "si o yek", "Otuz bir")
],

"Gün 33": [
    ("سی و دو", "si o do", "Otuz iki"),
    ("سی و سه", "si o se", "Otuz üç"),
    ("سی و چهار", "si o chahar", "Otuz dörd"),
    ("سی و پنج", "si o panj", "Otuz beş"),
    ("سی و شش", "si o shesh", "Otuz altı"),
    ("سی و هفت", "si o haft", "Otuz yeddi"),
    ("سی و هشت", "si o hasht", "Otuz səkkiz"),
    ("سی و نه", "si o noh", "Otuz doqquz"),
    ("چهل", "chehel", "Qırx"),
    ("چهل و یک", "chehel o yek", "Qırx bir")
],

"Gün 34": [
    ("چهل و دو", "chehel o do", "Qırx iki"),
    ("چهل و سه", "chehel o se", "Qırx üç"),
    ("چهل و چهار", "chehel o chahar", "Qırx dörd"),
    ("چهل و پنج", "chehel o panj", "Qırx beş"),
    ("چهل و شش", "chehel o shesh", "Qırx altı"),
    ("چهل و هفت", "chehel o haft", "Qırx yeddi"),
    ("چهل و هشت", "chehel o hasht", "Qırx səkkiz"),
    ("چهل و نه", "chehel o noh", "Qırx doqquz"),
    ("پنجاه", "panjah", "Əlli"),
    ("پنجاه و یک", "panjah o yek", "Əlli bir")
],

"Gün 35": [
    ("پنجاه و دو", "panjah o do", "Əlli iki"),
    ("پنجاه و سه", "panjah o se", "Əlli üç"),
    ("پنجاه و چهار", "panjah o chahar", "Əlli dörd"),
    ("پنجاه و پنج", "panjah o panj", "Əlli beş"),
    ("پنجاه و شش", "panjah o shesh", "Əlli altı"),
    ("پنجاه و هفت", "panjah o haft", "Əlli yeddi"),
    ("پنجاه و هشت", "panjah o hasht", "Əlli səkkiz"),
    ("پنجاه و نه", "panjah o noh", "Əlli doqquz"),
    ("شصت", "shast", "Altmış"),
    ("شصت و یک", "shast o yek", "Altmış bir")
],

"Gün 36": [
    ("شصت و دو", "shast o do", "Altmış iki"),
    ("شصت و سه", "shast o se", "Altmış üç"),
    ("شصت و چهار", "shast o chahar", "Altmış dörd"),
    ("شصت و پنج", "shast o panj", "Altmış beş"),
    ("شصت و شش", "shast o shesh", "Altmış altı"),
    ("شصت و هفت", "shast o haft", "Altmış yeddi"),
    ("شصت و هشت", "shast o hasht", "Altmış səkkiz"),
    ("شصت و نه", "shast o noh", "Altmış doqquz"),
    ("هفتاد", "haftad", "Yetmiş"),
    ("هفتاد و یک", "haftad o yek", "Yetmiş bir")
],

"Gün 37": [
    ("هفتاد و دو", "haftad o do", "Yetmiş iki"),
    ("هفتاد و سه", "haftad o se", "Yetmiş üç"),
    ("هفتاد و چهار", "haftad o chahar", "Yetmiş dörd"),
    ("هفتاد و پنج", "haftad o panj", "Yetmiş beş"),
    ("هفتاد و شش", "haftad o shesh", "Yetmiş altı"),
    ("هفتاد و هفت", "haftad o haft", "Yetmiş yeddi"),
    ("هفتاد و هشت", "haftad o hasht", "Yetmiş səkkiz"),
    ("هفتاد و نه", "haftad o noh", "Yetmiş doqquz"),
    ("هشتاد", "hashtad", "Səksən"),
    ("هشتاد و یک", "hashtad o yek", "Səksən bir")
],

"Gün 38": [
    ("هشتاد و دو", "hashtad o do", "Səksən iki"),
    ("هشتاد و سه", "hashtad o se", "Səksən üç"),
    ("هشتاد و چهار", "hashtad o chahar", "Səksən dörd"),
    ("هشتاد و پنج", "hashtad o panj", "Səksən beş"),
    ("هشتاد و شش", "hashtad o shesh", "Səksən altı"),
    ("هشتاد و هفت", "hashtad o haft", "Səksən yeddi"),
    ("هشتاد و هشت", "hashtad o hasht", "Səksən səkkiz"),
    ("هشتاد و نه", "hashtad o noh", "Səksən doqquz"),
    ("نود", "navad", "Doxsan"),
    ("نود و یک", "navad o yek", "Doxsan bir")
],

"Gün 39": [
    ("نود و دو", "navad o do", "Doxsan iki"),
    ("نود و سه", "navad o se", "Doxsan üç"),
    ("نود و چهار", "navad o chahar", "Doxsan dörd"),
    ("نود و پنج", "navad o panj", "Doxsan beş"),
    ("نود و شش", "navad o shesh", "Doxsan altı"),
    ("نود و هفت", "navad o haft", "Doxsan yeddi"),
    ("نود و هشت", "navad o hasht", "Doxsan səkkiz"),
    ("نود و نه", "navad o noh", "Doxsan doqquz"),
    ("صد", "sad", "Yüz"),
    ("صد و یک", "sad o yek", "Yüz bir")
],

"Gün 40": [
    ("صد و دو", "sad o do", "Yüz iki"),
    ("صد و سه", "sad o se", "Yüz üç"),
    ("صد و چهار", "sad o chahar", "Yüz dörd"),
    ("صد و پنج", "sad o panj", "Yüz beş"),
    ("صد و شش", "sad o shesh", "Yüz altı"),
    ("صد و هفت", "sad o haft", "Yüz yeddi"),
    ("صد و هشت", "sad o hasht", "Yüz səkkiz"),
    ("صد و نه", "sad o noh", "Yüz doqquz"),
    ("صد و ده", "sad o dah", "Yüz on"),
    ("صد و یازده", "sad o yazdah", "Yüz on bir")
]
}
