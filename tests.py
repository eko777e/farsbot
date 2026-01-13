# tests.py
# Struktur: "Gün X": [(sual_text, [variant1, variant2, variant3], düzgün_index)]

daily_tests = {
    "Gün 1": [
        ("سلام **hansı bənddə düzgün yazılıb?**", ["salam", "selam", "sallam"], 0),
        ("دوست **hansı bənddə düzgün yazılıb?**", ["dust", "dostt", "doost"], 0),
        ("کتاب **hansı bənddə düzgün yazılıb?**", ["ketab", "kitab", "katab"], 0),
        ("İndiki zaman fel **hansı cümlədə düzgündür?**", ["Mən gedirəm", "Mən getdim", "Mən gedəcəyəm"], 0),
        ("İndiki zaman fel **hansı cümlədə düzgündür?**", ["Sən oxuyursan", "O yazdı", "Biz gələcəyik"], 0)
    ],
    "Gün 2": [
        ("مدرسه **hansı bənddə düzgün yazılıb?**", ["madrese", "madraze", "madres"], 0),
        ("معلم **hansı bənddə düzgün yazılıb?**", ["moalem", "moalemm", "mualem"], 0),
        ("دانشجو **hansı bənddə düzgün yazılıb?**", ["daneshju", "daneshjoo", "daneshyoo"], 0),
        ("Zamanların inkarı **hansı cümlədə düzgündür?**", ["Mən getmirəm", "Mən getdim", "Mən gedirəm"], 0),
        ("Zamanların inkarı **hansı cümlədə düzgündür?**", ["Sən oxumursan", "O yazdı", "Biz gələcəyik"], 0)
    ],
    "Gün 3": [
        ("خانه **hansı bənddə düzgün yazılıb?**", ["xane", "khane", "khan"], 0),
        ("دوست **hansı bənddə düzgün yazılıb?**", ["dust", "doost", "dost"], 0),
        ("کتاب **hansı bənddə düzgün yazılıb?**", ["ketab", "kitab", "katab"], 0),
        ("Məchul fel **hansı cümlədə düzgündür?**", ["Kitab oxunur", "Kitab oxudu", "Kitab oxuyur"], 0),
        ("Məchul fel **hansı cümlədə düzgündür?**", ["Ev təmizlənir", "Ev təmizlədi", "Ev təmizləyir"], 0)
    ],
    "Gün 4": [
        ("دوچرخه **hansı bənddə düzgün yazılıb?**", ["docharkhe", "docharkh", "docharh"], 0),
        ("هواپیما **hansı bənddə düzgün yazılıb?**", ["havapeyma", "havapema", "havapima"], 0),
        ("ماشین **hansı bənddə düzgün yazılıb?**", ["mashin", "mashien", "mashinm"], 0),
        ("Əmr fel **hansı cümlədə düzgündür?**", ["Oxu!", "Yazdı!", "Gələcək!"], 0),
        ("Əmr fel **hansı cümlədə düzgündür?**", ["Gəl!", "Mən gedirəm", "Siz oxuyacaqsınız"], 0)
    ],
    "Gün 5": [
        ("سیب **hansı bənddə düzgün yazılıb?**", ["sib", "seeb", "sibp"], 0),
        ("موز **hansı bənddə düzgün yazılıb?**", ["moz", "mouz", "mooz"], 0),
        ("پرتقال **hansı bənddə düzgün yazılıb?**", ["porteghal", "portegal", "porteghel"], 0),
        ("Qəsdi niyyət fel **hansı cümlədə düzgündür?**", ["Mən gedəcəyəm", "Mən gedirəm", "Mən getdim"], 0),
        ("Qəsdi niyyət fel **hansı cümlədə düzgündür?**", ["Sən oxuyacaqsan", "O yazır", "Biz getdik"], 0)
    ],

    "Gün 6": [
        ("کتابخانه **hansı bənddə düzgün yazılıb?**", ["ketabkhane", "ketabkhan", "kitabkhane"], 0),
        ("میز **hansı bənddə düzgün yazılıb?**", ["miz", "meez", "mis"], 0),
        ("پنجره **hansı bənddə düzgün yazılıb?**", ["panjare", "panjaraa", "panjareh"], 0),
        ("Keçmiş sadə fel **hansı cümlədə düzgündür?**", ["Mən getdim", "Mən gedirəm", "Mən gedəcəyəm"], 0),
        ("Keçmiş sadə fel **hansı cümlədə düzgündür?**", ["O yazdı", "Biz oxuyuruq", "Siz gələcəksiniz"], 0)
    ],
    "Gün 7": [
        ("دوست **hansı bənddə düzgün yazılıb?**", ["dust", "dost", "doost"], 0),
        ("قلم **hansı bənddə düzgün yazılıb?**", ["qalam", "qalem", "qaalem"], 0),
        ("دفتر **hansı bənddə düzgün yazılıb?**", ["daftar", "defter", "daftarr"], 0),
        ("Yaxın keçmiş nəqli **hansı cümlədə düzgündür?**", ["Mən getmişəm", "Mən gedirəm", "Mən gedəcəyəm"], 0),
        ("Yaxın keçmiş nəqli **hansı cümlədə düzgündür?**", ["Sən oxumusan", "O yazdı", "Biz gələcəyik"], 0)
    ],
    # Gün 8
    "Gün 8": [
        ("پنیر **hansı bənddə düzgün yazılıb?**", ["panir", "penir", "peynir"], 0),
        ("نان **hansı bənddə düzgün yazılıb?**", ["nan", "naan", "nann"], 0),
        ("چای **hansı bənddə düzgün yazılıb?**", ["chay", "chai", "chayy"], 0),
        ("Keçmiş davamedici fel **hansı cümlədə düzgündür?**", ["Mən gedirdim", "Mən getmişəm", "Mən gedəcəyəm"], 0),
        ("Keçmiş davamedici fel **hansı cümlədə düzgündür?**", ["O yazırdı", "Biz oxuyuruq", "Siz gələcəksiniz"], 0)
    ],
    # Gün 9
    "Gün 9": [
        ("سیب **hansı bənddə düzgün yazılıb?**", ["sib", "seeb", "sibp"], 0),
        ("موز **hansı bənddə düzgün yazılıb?**", ["moz", "mooz", "moozz"], 0),
        ("پرتقال **hansı bənddə düzgün yazılıb?**", ["porteghal", "portegal", "porteghel"], 0),
        ("Uzaq keçmiş **hansı cümlədə düzgündür?**", ["Mən getmişdim", "Mən gedirəm", "Mən gedəcəyəm"], 0),
        ("Uzaq keçmiş **hansı cümlədə düzgündür?**", ["O yazdı", "Biz oxuyuruq", "Siz gələcəksiniz"], 0)
    ],
    # Gün 10
    "Gün 10": [
        ("خانه **hansı bənddə düzgün yazılıb?**", ["xane", "khane", "khan"], 0),
        ("کتاب **hansı bənddə düzgün yazılıb?**", ["ketab", "kitab", "katab"], 0),
        ("دوست **hansı bənddə düzgün yazılıb?**", ["dust", "dost", "doost"], 0),
        ("Fellərin hallanması **hansı cümlədə düzgündür?**", ["Mən gedirəm", "Mən getdim", "Mən gedəcəyəm"], 0),
        ("Fellərin hallanması **hansı cümlədə düzgündür?**", ["Sən gedirsən", "O getdi", "Biz gələcəyik"], 0)
    ],

    "Gün 11": [
        ("کتابچه **hansı bənddə düzgün yazılıb?**", ["ketabche", "ketabch", "kitabche"], 0),
        ("مداد **hansı bənddə düzgün yazılıb?**", ["medad", "maddad", "medaad"], 0),
        ("کاغذ **hansı bənddə düzgün yazılıb?**", ["kaghaz", "kagaz", "kaghazz"], 0),
        ("Sifət **hansı cümlədə düzgündür?**", ["Böyük ev", "Ev böyükdür", "Ev gedir"], 0),
        ("Sifət **hansı cümlədə düzgündür?**", ["Gözəl gün", "Biz gözəl gedirik", "Gözəl oxuyur"], 0)
    ],
    "Gün 12": [
        ("دوچرخه **hansı bənddə düzgün yazılıb?**", ["docharkhe", "docharh", "dochark"], 0),
        ("هواپیما **hansı bənddə düzgün yazılıb?**", ["havapeyma", "havapema", "havapima"], 0),
        ("ماشین **hansı bənddə düzgün yazılıb?**", ["mashin", "mashien", "mashine"], 0),
        ("Say məchul/məful **hansı cümlədə düzgündür?**", ["İki kitab oxundu", "Kitab iki oxundu", "İki oxundu kitab"], 0),
        ("Say məchul/məful **hansı cümlədə düzgündür?**", ["Üç məktəb tikildi", "Məktəb üç tikildi", "Üç tikildi məktəb"], 0)
    ],
    "Gün 13": [
        ("دوست **hansı bənddə düzgün yazılıb?**", ["dust", "doost", "dost"], 0),
        ("قلم **hansı bənddə düzgün yazılıb?**", ["qalam", "qalem", "qaalem"], 0),
        ("دفتر **hansı bənddə düzgün yazılıb?**", ["daftar", "defter", "daftarr"], 0),
        ("Şəxs əvəzlikləri **hansı cümlədə düzgündür?**", ["Mən gedirəm", "Sən oxuyur", "Biz gedəcəyik"], 0),
        ("Şəxs əvəzlikləri **hansı cümlədə düzgündür?**", ["O yazır", "Mən getdim", "Siz oxuyursunuz"], 0)
    ],
    "Gün 14": [
        ("پنیر **hansı bənddə düzgün yazılıb?**", ["panir", "penir", "peynir"], 0),
        ("نان **hansı bənddə düzgün yazılıb?**", ["nan", "naan", "nann"], 0),
        ("چای **hansı bənddə düzgün yazılıb?**", ["chay", "chai", "chayy"], 0),
        ("Bitişik şəxs əvəzlikləri **hansı cümlədə düzgündür?**", ["Kitabım", "Mən kitabım", "Kitabım mən"], 0),
        ("Bitişik şəxs əvəzlikləri **hansı cümlədə düzgündür?**", ["Evimiz", "Biz evimiz", "Evimiz biz"], 0)
    ],
    "Gün 15": [
        ("سیب **hansı bənddə düzgün yazılıb?**", ["sib", "seeb", "sibp"], 0),
        ("موز **hansı bənddə düzgün yazılıb?**", ["moz", "mouz", "mooz"], 0),
        ("پرتقال **hansı bənddə düzgün yazılıb?**", ["porteghal", "portegal", "porteghel"], 0),
        ("Gizli fellər **hansı cümlədə düzgündür?**", ["Getdim (mən)", "Mən getdim", "Getdim mən"], 0),
        ("Gizli fellər **hansı cümlədə düzgündür?**", ["Oxudun (sən)", "Sən oxudun", "Oxudun sən"], 0)
    ],
    "Gün 16": [
        ("خانه **hansı bənddə düzgün yazılıb?**", ["xane", "khane", "khan"], 0),
        ("کتاب **hansı bənddə düzgün yazılıb?**", ["ketab", "kitab", "katab"], 0),
        ("دوست **hansı bənddə düzgün yazılıb?**", ["dust", "doost", "dost"], 0),
        ("Cümlə qurluşu **hansı cümlədə düzgündür?**", ["Mən məktəbə gedirəm", "Məktəb mən gedirəm", "Mən gedirəm məktəbə"], 0),
        ("Cümlə qurluşu **hansı cümlədə düzgündür?**", ["O kitab oxuyur", "Kitab o oxuyur", "Oxuyur o kitab"], 0)
    ],
    "Gün 17": [
        ("دوچرخه **hansı bənddə düzgün yazılıb?**", ["docharkhe", "docharh", "dochark"], 0),
        ("هواپیما **hansı bənddə düzgün yazılıb?**", ["havapeyma", "havapema", "havapima"], 0),
        ("ماشین **hansı bənddə düzgün yazılıb?**", ["mashin", "mashien", "mashine"], 0),
        ("İsmin hal şəkilçiləri **hansı cümlədə düzgündür?**", ["Evin (genitiv)", "Ev (genitiv) evin", "Evin ev genitiv"], 0),
        ("İsmin hal şəkilçiləri **hansı cümlədə düzgündür?**", ["evə (dativ)", "dativ evə", "evə ev dativ"], 0)
    ],

    "Gün 18": [
        ("مدرسه **hansı bənddə düzgün yazılıb?**", ["madrese", "madraze", "madres"], 0),
        ("معلم **hansı bənddə düzgün yazılıb?**", ["moalem", "moalemm", "mualem"], 0),
        ("دانشجو **hansı bənddə düzgün yazılıb?**", ["daneshju", "daneshjoo", "daneshyoo"], 0),
        ("Qəti indiki hal xəbər cümləsi **hansı cümlədə düzgündür?**", ["Mən indi gedirəm", "Mən getdim indi", "İndi mən gedirəm"], 0),
        ("Qəti indiki hal xəbər cümləsi **hansı cümlədə düzgündür?**", ["Sən indi oxuyursan", "Sən oxuyursan indi", "İndi oxuyursan sən"], 0)
    ],
    "Gün 19": [
        ("کتاب **hansı bənddə düzgün yazılıb?**", ["ketab", "kitab", "katab"], 0),
        ("قلم **hansı bənddə düzgün yazılıb?**", ["qalam", "qalem", "qaalem"], 0),
        ("دفتر **hansı bənddə düzgün yazılıb?**", ["daftar", "defter", "daftarr"], 0),
        ("İndiki zaman fel **hansı cümlədə düzgündür?**", ["Mən oxuyuram", "Mən oxuyacağam", "Mən oxudum"], 0),
        ("Məchul fel **hansı cümlədə düzgündür?**", ["Ev təmizlənir", "Ev təmizlədi", "Ev təmizləyir"], 0)
    ],
    "Gün 20": [
        ("دوست **hansı bənddə düzgün yazılıb?**", ["dust", "doost", "dost"], 0),
        ("خانه **hansı bənddə düzgün yazılıb?**", ["xane", "khane", "khan"], 0),
        ("کتابچه **hansı bənddə düzgün yazılıb?**", ["ketabche", "ketabch", "kitabche"], 0),
        ("Keçmiş sadə **hansı cümlədə düzgündür?**", ["Mən getdim", "Mən gedirəm", "Mən gedəcəyəm"], 0),
        ("Keçmiş sadə **hansı cümlədə düzgündür?**", ["Sən oxudun", "Sən oxuyursan", "Sən oxuyacaqsan"], 0)
    ],
    "Gün 21": [
        ("سیب **hansı bənddə düzgün yazılıb?**", ["sib", "seeb", "sibp"], 0),
        ("پرتقال **hansı bənddə düzgün yazılıb?**", ["porteghal", "portegal", "porteghel"], 0),
        ("موز **hansı bənddə düzgün yazılıb?**", ["moz", "mouz", "mooz"], 0),
        ("Yaxın keçmiş nəqli **hansı cümlədə düzgündür?**", ["Mən getmişəm", "Mən getdim", "Mən gedəcəyəm"], 0),
        ("Yaxın keçmiş nəqli **hansı cümlədə düzgündür?**", ["Sən oxumusan", "Sən oxuyacaqsan", "Sən oxudun"], 0)
    ],
    "Gün 22": [
        ("دوچرخه **hansı bənddə düzgün yazılıb?**", ["docharkhe", "docharh", "dochark"], 0),
        ("هواپیما **hansı bənddə düzgün yazılıb?**", ["havapeyma", "havapema", "havapima"], 0),
        ("ماشین **hansı bənddə düzgün yazılıb?**", ["mashin", "mashien", "mashine"], 0),
        ("Keçmiş davamedici **hansı cümlədə düzgündür?**", ["Mən gedirdim", "Mən getmişdim", "Mən gedəcəyəm"], 0),
        ("Keçmiş davamedici **hansı cümlədə düzgündür?**", ["Sən oxuyurdun", "Sən oxudun", "Sən oxuyacaqsan"], 0)
    ],
    "Gün 23": [
        ("کتاب **hansı bənddə düzgün yazılıb?**", ["ketab", "kitab", "katab"], 0),
        ("قلم **hansı bənddə düzgün yazılıb?**", ["qalam", "qalem", "qaalem"], 0),
        ("دفتر **hansı bənddə düzgün yazılıb?**", ["daftar", "defter", "daftarr"], 0),
        ("Uzaq keçmiş **hansı cümlədə düzgündür?**", ["Mən getmişdim", "Mən gedirəm", "Mən getdim"], 0),
        ("Uzaq keçmiş **hansı cümlədə düzgündür?**", ["Sən oxumuşdun", "Sən oxudun", "Sən oxuyacaqsan"], 0)
    ],
    "Gün 24": [
        ("دوست **hansı bənddə düzgün yazılıb?**", ["dust", "doost", "dost"], 0),
        ("خانه **hansı bənddə düzgün yazılıb?**", ["xane", "khane", "khan"], 0),
        ("کتابچه **hansı bənddə düzgün yazılıb?**", ["ketabche", "ketabch", "kitabche"], 0),
        ("Fellərin hallanması **hansı cümlədə düzgündür?**", ["Mən gedirəm", "Mən getdim", "Mən gedəcəyəm"], 0),
        ("Fellərin hallanması **hansı cümlədə düzgündür?**", ["Sən gedirsən", "Sən getdin", "Sən gedəcəksən"], 0)
    ],
    "Gün 25": [
        ("پنیر **hansı bənddə düzgün yazılıb?**", ["panir", "penir", "peynir"], 0),
        ("نان **hansı bənddə düzgün yazılıb?**", ["nan", "naan", "nann"], 0),
        ("چای **hansı bənddə düzgün yazılıb?**", ["chay", "chai", "chayy"], 0),
        ("Sifət **hansı cümlədə düzgündür?**", ["Böyük ev", "Ev böyükdür", "Ev gedir"], 0),
        ("Sifət **hansı cümlədə düzgündür?**", ["Gözəl gün", "Biz gözəl gedirik", "Gözəl oxuyur"], 0)
    ],
    "Gün 26": [
        ("سیب **hansı bənddə düzgün yazılıb?**", ["sib", "seeb", "sibp"], 0),
        ("موز **hansı bənddə düzgün yazılıb?**", ["moz", "mouz", "mooz"], 0),
        ("پرتقال **hansı bənddə düzgün yazılıb?**", ["porteghal", "portegal", "porteghel"], 0),
        ("Şəxs əvəzlikləri **hansı cümlədə düzgündür?**", ["Mən gedirəm", "Sən oxuyur", "Biz gedəcəyik"], 0),
        ("Şəxs əvəzlikləri **hansı cümlədə düzgündür?**", ["O yazır", "Mən getdim", "Siz oxuyursunuz"], 0)
    ],
    "Gün 27": [
        ("دوچرخه **hansı bənddə düzgün yazılıb?**", ["docharkhe", "docharh", "dochark"], 0),
        ("هواپیما **hansı bənddə düzgün yazılıb?**", ["havapeyma", "havapema", "havapima"], 0),
        ("ماشین **hansı bənddə düzgün yazılıb?**", ["mashin", "mashien", "mashine"], 0),
        ("Bitişik şəxs əvəzlikləri **hansı cümlədə düzgündür?**", ["Kitabım", "Mən kitabım", "Kitabım mən"], 0),
        ("Bitişik şəxs əvəzlikləri **hansı cümlədə düzgündür?**", ["Evimiz", "Biz evimiz", "Evimiz biz"], 0)
    ],
    "Gün 28": [
        ("کتاب **hansı bənddə düzgün yazılıb?**", ["ketab", "kitab", "katab"], 0),
        ("قلم **hansı bənddə düzgün yazılıb?**", ["qalam", "qalem", "qaalem"], 0),
        ("دفتر **hansı bənddə düzgün yazılıb?**", ["daftar", "defter", "daftarr"], 0),
        ("Gizli fellər **hansı cümlədə düzgündür?**", ["Getdim (mən)", "Oxudum (mən)", "Gedəcəyəm (mən)"], 0),
        ("Gizli fellər **hansı cümlədə düzgündür?**", ["Oxudun (sən)", "Sən oxudun", "O yazdı"], 0)
    ],
    "Gün 29": [
        ("دوست **hansı bənddə düzgün yazılıb?**", ["dust", "doost", "dost"], 0),
        ("خانه **hansı bənddə düzgün yazılıb?**", ["xane", "khane", "khan"], 0),
        ("کتابچه **hansı bənddə düzgün yazılıb?**", ["ketabche", "ketabch", "kitabche"], 0),
        ("Cümlə qurluşu **hansı cümlədə düzgündür?**", ["Mən məktəbə gedirəm", "Məktəb mən gedirəm", "Mən gedirəm məktəbə"], 0),
        ("Cümlə qurluşu **hansı cümlədə düzgündür?**", ["O kitab oxuyur", "Kitab o oxuyur", "Oxuyur o kitab"], 0)
    ],
    "Gün 30": [
        ("پنیر **hansı bənddə düzgün yazılıb?**", ["panir", "penir", "peynir"], 0),
        ("نان **hansı bənddə düzgün yazılıb?**", ["nan", "naan", "nann"], 0),
        ("چای **hansı bənddə düzgün yazılıb?**", ["chay", "chai", "chayy"], 0),
        ("İsmin hal şəkilçiləri **hansı cümlədə düzgündür?**", ["Evin (genitiv)", "evə (dativ)", "evi (məf'ul)"], 0),
        ("İsmin hal şəkilçiləri **hansı cümlədə düzgündür?**", ["O evin", "Ev ona", "Evin o"], 0)
    ],
}
