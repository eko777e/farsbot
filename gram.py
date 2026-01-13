# gram.py

# Struktur: { "Gün 1": {"ders": "...", "izah": "...", "nümunə": "..." } }

grammar_lessons = {
    "Gün 1": {
        "ders": "Əvvəl indiki zaman",
        "izah": "İndiki zaman fellərin indiki zamanda halını göstərir. Fəaliyyətin hazırda baş verdiyini bildirir.",
        "nümunə": "من می‌روم، تو می‌خوانی، او می‌نویسد، ما می‌خوانیم، شما می‌آیید، آنها صحبت می‌کنند"
    },
    "Gün 2": {
        "ders": "Zamanların inkarı",
        "izah": "Müəyyən zaman fellərinin inkar formasını göstərir. Fellər 'mə', 'məy' şəkli ilə inkar olunur.",
        "nümunə": "من نمی‌روم، تو نمی‌خوانی، او نمی‌نویسد، ما نمی‌آییم، شما صحبت نمی‌کنید، آنها نمی‌روند"
    },
    "Gün 3": {
        "ders": "Məchul",
        "izah": "Məchul (passive voice) fəaliyyəti edən subyektin gizli olduğu haldır.",
        "nümunə": "کتاب خوانده می‌شود، مدرسه ساخته می‌شود، به مدرسه می‌روند"
    },
    "Gün 4": {
        "ders": "Əmr",
        "izah": "Əmr felləri müəyyən şəxsə yönəlmiş göstəriş və ya əmri bildirir.",
        "nümunə": "بخوان! بنویس! بیا!"
    },
    "Gün 5": {
        "ders": "Qəsdi niyyət / Lazımi fellər",
        "izah": "Gələcəkdə ediləcək fəaliyyətləri və ya məqsədli niyyətləri göstərir.",
        "nümunə": "من خواهم رفت، تو خواهی خواند، او خواهد نوشت، ما خواهیم آمد، شما خواهید صحبت کرد، آنها خواهند خواند"
    },
    "Gün 6": {
        "ders": "Keçmiş sadə",
        "izah": "Keçmişdə tamamlanmış fəaliyyətləri göstərir.",
        "nümunə": "من رفتم، تو خواندی، او نوشت، ما آمدیم، شما صحبت کردید، آنها رفتند"
    },
    "Gün 7": {
        "ders": "Yaxın keçmiş nəqli",
        "izah": "Keçmişdə baş vermiş fəaliyyətin nəticəsinin indi hiss olunduğu hal.",
        "nümunə": "من رفته‌ام، تو خوانده‌ای، او نوشته است، ما آمده‌ایم، شما صحبت کرده‌اید، آنها رفته‌اند"
    },
    "Gün 8": {
        "ders": "Keçmiş davamedici",
        "izah": "Keçmişdə müəyyən bir müddət ərzində davam edən fəaliyyəti göstərir.",
        "nümunə": "من می‌رفتم، تو می‌خواندی، او می‌نوشت، ما می‌آمدیم، شما صحبت می‌کردید، آنها می‌رفتند"
    },
    "Gün 9": {
        "ders": "Uzaq keçmiş",
        "izah": "Çox əvvəl baş vermiş fəaliyyətləri göstərir, nəticəsi indiyə təsir etmir.",
        "nümunə": "من رفته بودم، تو خوانده بودی، او نوشته بود، ما رفته بودیم، شما صحبت کرده بودید، آنها رفته بودند"
    },
    "Gün 10": {
        "ders": "Fellərin hallanması",
        "izah": "Fellərin 6 şəxsin hamısında necə dəyişdiyini göstərir.",
        "nümunə": "من می‌روم، تو می‌روی، او می‌رود، ما می‌رویم، شما می‌روید، آنها می‌روند"
    },
    "Gün 11": {
        "ders": "Sifət",
        "izah": "İsimləri təsvir edən sözlərdir. Sifət isimlərin xüsusiyyətini bildirir.",
        "nümunə": "خانه بزرگ، روز زیبا، کتاب جالب"
    },
    "Gün 12": {
        "ders": "Say məchul/məful",
        "izah": "Məchul və məful hallarda sayı bildirir.",
        "nümunə": "دو کتاب خوانده شد، سه مدرسه ساخته شد، پنج نفر به مدرسه رفتند"
    },
    "Gün 13": {
        "ders": "Şəxs əvəzlikləri",
        "izah": "Fəaliyyəti edən və ya isim yerinə istifadə olunan sözlər.",
        "nümunə": "من، تو، او، ما، شما، آنها"
    },
    "Gün 14": {
        "ders": "Bitişik şəxs əvəzlikləri",
        "izah": "İsim və əvəzlik birləşərək şəkilçi alır.",
        "nümunə": "کتابم، خانه‌مان، دوستتان"
    },
    "Gün 15": {
        "ders": "Gizli fellər",
        "izah": "Fəaliyyətin subyekti açıq göstərilməyən fellər.",
        "nümunə": "رفتم (من)، خواندی (تو)، نوشت (او)"
    },
    "Gün 16": {
        "ders": "Cümlə qurluşu",
        "izah": "Cümlənin düzgün quruluşunu göstərir.",
        "nümunə": "من به مدرسه می‌روم. او کتاب می‌خواند. ما به پارک می‌رویم."
    },
    "Gün 17": {
        "ders": "İsmin hal şəkilçiləri",
        "izah": "İsimlərin hallanmasını bildirən şəkilçilər.",
        "nümunə": "خانهٔ من (genitiv)، به خانه (dativ)، خانه را (accusative)"
    },
    "Gün 18": {
        "ders": "Qəti indiki hal xəbər cümləsi",
        "izah": "İndiki zamanda baş verən hadisəni xəbər verən qəti cümlə.",
        "nümunə": "من الان می‌روم، تو الان می‌خوانی، او الان می‌نویسد، ما می‌رویم، شما صحبت می‌کنید، آنها می‌روند"
    }
}
