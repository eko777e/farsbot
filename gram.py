# gram.py

# Struktur: { "Gün 1": {"ders": "...", "izah": "...", "nümunə": "..." } }

grammar_lessons = {
    "Gün 1": {
        "ders": "Əvvəl indiki zaman",
        "izah": "İndiki zaman fellərin indiki zamanda halını göstərir. Fəaliyyətin hazırda baş verdiyini bildirir.",
        "nümunə": "Mən gedirəm, sən oxuyursan, o yazır, biz oxuyuruq, siz gəlirsiniz, onlar danışırlar"
    },
    "Gün 2": {
        "ders": "Zamanların inkarı",
        "izah": "Müəyyən zaman fellərinin inkar formasını göstərir. Fellər 'mə', 'məy' şəkli ilə inkar olunur.",
        "nümunə": "Mən getmirəm, sən oxumursan, o yazmır, biz gəlmirik, siz danışmırsınız, onlar getmirlər"
    },
    "Gün 3": {
        "ders": "Məchul",
        "izah": "Məchul (passive voice) fəaliyyəti edən subyektin gizli olduğu haldır.",
        "nümunə": "Kitab oxunur, məktəb tikilir, məktəbə gedilir"
    },
    "Gün 4": {
        "ders": "Əmr",
        "izah": "Əmr felləri müəyyən şəxsə yönəlmiş göstəriş və ya əmri bildirir.",
        "nümunə": "Oxu! Yaz! Gəl!"
    },
    "Gün 5": {
        "ders": "Qəsdi niyyət / Lazımi fellər",
        "izah": "Gələcəkdə ediləcək fəaliyyətləri və ya məqsədli niyyətləri göstərir.",
        "nümunə": "Mən gedəcəyəm, sən oxuyacaqsan, o yazacaq, biz gələcəyik, siz danışacaqsınız, onlar oxuyacaqlar"
    },
    "Gün 6": {
        "ders": "Keçmiş sadə",
        "izah": "Keçmişdə tamamlanmış fəaliyyətləri göstərir.",
        "nümunə": "Mən getdim, sən oxudun, o yazdı, biz gəldik, siz danışdınız, onlar oxudular"
    },
    "Gün 7": {
        "ders": "Yaxın keçmiş nəqli",
        "izah": "Keçmişdə baş vermiş fəaliyyətin nəticəsinin indi hiss olunduğu hal.",
        "nümunə": "Mən getmişəm, sən oxumusan, o yazıb, biz gəlmişik, siz danışmısınız, onlar oxuyublar"
    },
    "Gün 8": {
        "ders": "Keçmiş davamedici",
        "izah": "Keçmişdə müəyyən bir müddət ərzində davam edən fəaliyyəti göstərir.",
        "nümunə": "Mən gedirdim, sən oxuyurdun, o yazırdı, biz gəlirdik, siz danışırdınız, onlar oxuyurdular"
    },
    "Gün 9": {
        "ders": "Uzaq keçmiş",
        "izah": "Çox əvvəl baş vermiş fəaliyyətləri göstərir, nəticəsi indiyə təsir etmir.",
        "nümunə": "Mən getmişdim, sən oxumuşdun, o yazmışdı, biz gəlmişdik, siz danışmışdınız, onlar oxumuşdular"
    },
    "Gün 10": {
        "ders": "Fellərin hallanması",
        "izah": "Fellərin 6 şəxsin hamısında necə dəyişdiyini göstərir.",
        "nümunə": "Mən gedirəm, sən gedirsən, o gedir, biz gedirik, siz gedirsiniz, onlar gedirlər"
    },
    "Gün 11": {
        "ders": "Sifət",
        "izah": "İsimləri təsvir edən sözlərdir. Sifət isimlərin xüsusiyyətini bildirir.",
        "nümunə": "Böyük ev, gözəl gün, maraqlı kitab"
    },
    "Gün 12": {
        "ders": "Say məchul/məful",
        "izah": "Məchul və məful hallarda sayı bildirir.",
        "nümunə": "İki kitab oxundu, üç məktəb tikildi, beş məktəbə gedildi"
    },
    "Gün 13": {
        "ders": "Şəxs əvəzlikləri",
        "izah": "Fəaliyyəti edən və ya isim yerinə istifadə olunan sözlər.",
        "nümunə": "Mən, sən, o, biz, siz, onlar"
    },
    "Gün 14": {
        "ders": "Bitişik şəxs əvəzlikləri",
        "izah": "İsim və əvəzlik birləşərək şəkilçi alır.",
        "nümunə": "Kitabım, evimiz, dostunuz"
    },
    "Gün 15": {
        "ders": "Gizli fellər",
        "izah": "Fəaliyyətin subyekti açıq göstərilməyən fellər.",
        "nümunə": "Getdim (mən), Oxudun (sən), Yazdı (o)"
    },
    "Gün 16": {
        "ders": "Cümlə qurluşu",
        "izah": "Cümlənin düzgün quruluşunu göstərir.",
        "nümunə": "Mən məktəbə gedirəm. O kitab oxuyur. Biz parka gedirik."
    },
    "Gün 17": {
        "ders": "İsmin hal şəkilçiləri",
        "izah": "İsimlərin hallanmasını bildirən şəkilçilər.",
        "nümunə": "Evin (genitiv), evə (dativ), evi (məf'ul)"
    },
    "Gün 18": {
        "ders": "Qəti indiki hal xəbər cümləsi",
        "izah": "İndiki zamanda baş verən hadisəni xəbər verən qəti cümlə.",
        "nümunə": "Mən indi gedirəm, sən indi oxuyursan, o indi yazır, biz gəlirik, siz danışırsınız, onlar oxuyurlar"
    }
    # Gün 19-30 üçün istəsən əlavə edə bilərik
}
