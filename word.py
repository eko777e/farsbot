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
        ("هندوانه", "hendavane", "Qarpız")
    ],
    "Gün 6": [
        ("آب", "ab", "Su"),
        ("چای", "chay", "Çay"),
        ("قهوه", "ghahve", "Qəhvə"),
        ("شیر", "shir", "Süd"),
        ("نان", "nan", "Çörək")
    ],
    "Gün 7": [
        ("خورشید", "khorshid", "Günəş"),
        ("ماه", "mah", "Ay"),
        ("ستاره", "setare", "Ulduz"),
        ("آسمان", "aseman", "Səmada"),
        ("ابر", "abr", "Bulud")
    ],
    "Gün 8": [
        ("زمین", "zamin", "Yer"),
        ("کوه", "kuh", "Dağ"),
        ("دریا", "darya", "Dəniz"),
        ("رود", "rud", "Çay"),
        ("جنگل", "jangal", "Meşə")
    ],
    "Gün 9": [
        ("پدر", "pedar", "Ata"),
        ("مادر", "madar", "Ana"),
        ("برادر", "baradar", "Qardaş"),
        ("خواهر", "khahar", "Qardaş"),
        ("خانواده", "khanevade", "Ailə")
    ],
    "Gün 10": [
        ("دو", "do", "İki"),
        ("سه", "se", "Üç"),
        ("چهار", "chahar", "Dörd"),
        ("پنج", "panj", "Beş"),
        ("شش", "shesh", "Altı")
    ],
    "Gün 11": [
        ("هفت", "haft", "Yeddi"),
        ("هشت", "hasht", "Səkkiz"),
        ("نه", "noh", "Doqquz"),
        ("ده", "dah", "On"),
        ("بیست", "bist", "İyirmi")
    ],
    "Gün 12": [
        ("صبح", "sobh", "Səhər"),
        ("ظهر", "zohr", "Günorta"),
        ("عصر", "asr", "Axşamüstü"),
        ("غروب", "ghorub", "Gün batımı"),
        ("شب", "shab", "Gecə")
    ],
    "Gün 13": [
        ("دویدن", "davidan", "Qaçmaq"),
        ("خوابیدن", "khabidan", "Yatmaq"),
        ("خواندن", "khandan", "Oxumaq"),
        ("نوشتن", "neveshtan", "Yazmaq"),
        ("خوردن", "khordan", "Yemək")
    ],
    "Gün 14": [
        ("دیدن", "didan", "Görmək"),
        ("شنیدن", "shenidan", "Eşitmək"),
        ("رفتن", "raftan", "Getmək"),
        ("آمدن", "amadan", "Gəlmək"),
        ("خریدن", "kharidan", "Almaq")
    ],
    "Gün 15": [
        ("لباس", "lebas", "Paltar"),
        ("کفش", "kafsh", "Ayaqqabı"),
        ("کلاه", "kolah", "Papaq"),
        ("کیف", "kif", "Çanta"),
        ("ساعت", "sa'at", "Saat")
    ],
    "Gün 16": [
        ("دوست داشتن", "dust dashtan", "Sevmək"),
        ("نفرت داشتن", "nefrat dashtan", "Nifrət etmək"),
        ("خندیدن", "khandidan", "Gülmək"),
        ("گریه کردن", "gerye kardan", "Ağlamaq"),
        ("صحبت کردن", "sohbat kardan", "Danışmaq")
    ],
    "Gün 17": [
        ("بزرگ", "bozorg", "Böyük"),
        ("کوچک", "kuchak", "Kiçik"),
        ("بلند", "boland", "Uzun"),
        ("کوتاه", "kutah", "Qısa"),
        ("سریع", "sari'", "Sürətli")
    ],
    "Gün 18": [
        ("کند", "kond", "Yavaş"),
        ("زیبا", "ziba", "Gözəl"),
        ("جالب", "jaleb", "Maraqlı"),
        ("سخت", "sakht", "Çətin"),
        ("ساده", "sade", "Sadə")
    ],
    "Gün 19": [
        ("سیب زمینی", "sib zamini", "Kartof"),
        ("گوجه", "goje", "Pomidor"),
        ("هویج", "hivij", "Kök"),
        ("کلم", "kalam", "Kələm"),
        ("پیاز", "piyaz", "Soğan")
    ],
    "Gün 20": [
        ("ماشین لباسشویی", "mashin lebasshuyi", "Paltaryuyan maşın"),
        ("یخچال", "yakhchal", "Soyuducu"),
        ("تلویزیون", "televizion", "Televizor"),
        ("موبایل", "mobile", "Mobil telefon"),
        ("کامپیوتر", "computer", "Kompüter")
    ],
    "Gün 21": [
        ("بازار", "bazar", "Bazar"),
        ("فروشگاه", "forushgah", "Mağaza"),
        ("کتابفروشی", "ketabforushi", "Kitab mağazası"),
        ("رستوران", "resturan", "Restoran"),
        ("هتل", "hotel", "Otel")
    ],
    "Gün 22": [
        ("دوست", "dust", "Dost"),
        ("همکار", "hamkar", "Həmkar"),
        ("معلم", "moalem", "Müəllim"),
        ("دانشجو", "daneshju", "Tələbə"),
        ("مربی", "morabbi", "Məşqçi")
    ],
    "Gün 23": [
        ("صبحانه", "sobhan-e", "Səhər yeməyi"),
        ("ناهار", "nahar", "Nahar"),
        ("شام", "sham", "Axşam yeməyi"),
        ("میوه", "mive", "Meyvə"),
        ("سبزی", "sabzi", "Tərəvəz")
    ],
    "Gün 24": [
        ("مداد", "medad", "Qələm"),
        ("پاک‌کن", "pak-kon", "Silgi"),
        ("دفتر", "daftar", "Dəftər"),
        ("کتابچه", "ketabche", "Kiçik kitab"),
        ("خط‌کش", "khatkesh", "Xətkeş")
    ],
    "Gün 25": [
        ("آبمیوه", "ab-mive", "Şirə"),
        ("چای سبز", "chay-e sabz", "Yaşıl çay"),
        ("قهوه", "ghahve", "Qəhvə"),
        ("شیرینی", "shirini", "Şirniyyat"),
        ("شکلات", "shokolat", "Şokolad")
    ],
    "Gün 26": [
        ("کتابخانه", "ketabkhane", "Kitabxana"),
        ("مدرسه", "madrese", "Məktəb"),
        ("دانشگاه", "daneshgah", "Universitet"),
        ("کتابفروشی", "ketabforushi", "Kitab mağazası"),
        ("آزمایشگاه", "azmayeshgah", "Laboratoriya")
    ],
    "Gün 27": [
        ("سیب", "sib", "Alma"),
        ("موز", "moz", "Banan"),
        ("پرتقال", "porteghal", "Portağal"),
        ("انار", "anar", "Nar"),
        ("هندوانه", "hendavane", "Qarpız")
    ],
    "Gün 28": [
        ("باران", "baran", "Yağış"),
        ("برف", "barf", "Qar"),
        ("باد", "bad", "Külək"),
        ("آفتاب", "aftab", "Günəş"),
        ("رعد و برق", "ra'd o barq", "İldırım")
    ],
    "Gün 29": [
        ("خانه", "xane", "Ev"),
        ("مدرسه", "madrese", "Məktəb"),
        ("دفتر", "daftar", "Dəftər"),
        ("کتاب", "ketab", "Kitab"),
        ("موبایل", "mobile", "Mobil telefon")
    ],
    "Gün 30": [
        ("دو", "do", "İki"),
        ("سه", "se", "Üç"),
        ("چهار", "chahar", "Dörd"),
        ("پنج", "panj", "Beş"),
        ("شش", "shesh", "Altı")
    ],
    "Gün 31": [
        ("هفت", "haft", "Yeddi"),
        ("هشت", "hasht", "Səkkiz"),
        ("نه", "noh", "Doqquz"),
        ("ده", "dah", "On"),
        ("یازده", "yazdah", "On bir")
    ],
    "Gün 32": [
        ("دوازده", "davazdah", "On iki"),
        ("سیزده", "sizdah", "On üç"),
        ("چهارده", "chahardah", "On dörd"),
        ("پانزده", "panzdah", "On beş"),
        ("شانزده", "shanzdah", "On altı")
    ],
    "Gün 33": [
        ("هفده", "hefdah", "On yeddi"),
        ("هجده", "hejdah", "On səkkiz"),
        ("نوزده", "nozdah", "On doqquz"),
        ("بیست", "bist", "İyirmi"),
        ("بیست و یک", "bist o yek", "İyirmi bir")
    ],
    "Gün 34": [
        ("بیست و دو", "bist o do", "İyirmi iki"),
        ("بیست و سه", "bist o se", "İyirmi üç"),
        ("بیست و چهار", "bist o chahar", "İyirmi dörd"),
        ("بیست و پنج", "bist o panj", "İyirmi beş"),
        ("بیست و شش", "bist o shesh", "İyirmi altı")
    ],
    "Gün 35": [
        ("بیست و هفت", "bist o haft", "İyirmi yeddi"),
        ("بیست و هشت", "bist o hasht", "İyirmi səkkiz"),
        ("بیست و نه", "bist o noh", "İyirmi doqquz"),
        ("سی", "si", "Otuz"),
        ("سی و یک", "si o yek", "Otuz bir")
    ],
    "Gün 36": [
        ("سی و دو", "si o do", "Otuz iki"),
        ("سی و سه", "si o se", "Otuz üç"),
        ("سی و چهار", "si o chahar", "Otuz dörd"),
        ("سی و پنج", "si o panj", "Otuz beş"),
        ("سی و شش", "si o shesh", "Otuz altı")
    ],
    "Gün 37": [
        ("سی و هفت", "si o haft", "Otuz yeddi"),
        ("سی و هشت", "si o hasht", "Otuz səkkiz"),
        ("سی و نه", "si o noh", "Otuz doqquz"),
        ("چهل", "chehel", "Qırx"),
        ("چهل و یک", "chehel o yek", "Qırx bir")
    ],
    "Gün 38": [
        ("چهل و دو", "chehel o do", "Qırx iki"),
        ("چهل و سه", "chehel o se", "Qırx üç"),
        ("چهل و چهار", "chehel o chahar", "Qırx dörd"),
        ("چهل و پنج", "chehel o panj", "Qırx beş")
    ],
    "Gün 39": [
        ("چهل و شش", "chehel o shesh", "Qırx altı"),
        ("چهل و هفت", "chehel o haft", "Qırx yeddi"),
        ("چهل و هشت", "chehel o hasht", "Qırx səkkiz"),
        ("چهل و نه", "chehel o noh", "Qırx doqquz"),
        ("پنجاه", "panjah", "Əlli")
    ],
    "Gün 40": [
        ("پنجاه و یک", "panjah o yek", "Əlli bir"),
        ("پنجاه و دو", "panjah o do", "Əlli iki"),
        ("پنجاه و سه", "panjah o se", "Əlli üç"),
        ("پنجاه و چهار", "panjah o chahar", "Əlli dörd")
    ]
}
