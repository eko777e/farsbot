# tests.py
# Struktur: "Gün X": {"sual": [(sual_text, [variant1, variant2, variant3], düzgün_index), ...], "cavab": [...]}

daily_tests = {
    "Gün 1": {
        "sual": [
            ("سلام **hansı bənddə düzgün yazılıb?**", ["salam", "selam", "sallam"], 0),
            ("دوست **hansı bənddə düzgün yazılıb?**", ["dust", "dostt", "doost"], 0),
            ("کتاب **hansı bənddə düzgün yazılıb?**", ["ketab", "kitab", "ketopp"], 0),
            # Qrammatika sualları
            ("İndiki zaman fel **hansı cümlədə düzgündür?**", ["Mən gedirəm", "Mən gedəcəm", "Mən getdim"], 0),
            ("Məchul fel **hansı cümlədə düzgündür?**", ["Ev təmizlənir", "Ev təmizləndi", "Ev təmizləyir"], 0)
        ],
        "cavab": [
            "salam",
            "dust",
            "ketab",
            "Mən gedirəm",
            "Ev təmizlənir"
        ]
    },
    "Gün 2": {
        "sual": [
            ("مدرسه **hansı bənddə düzgün yazılıb?**", ["madrese", "madraze", "madres"], 0),
            ("معلم **hansı bənddə düzgün yazılıb?**", ["moalem", "moalemm", "mualem"], 0),
            ("دانشجو **hansı bənddə düzgün yazılıb?**", ["daneshju", "daneshjoo", "daneshyoo"], 0),
            # Qrammatika sualları
            ("Zamanların inkari **hansı cümlədə düzgündür?**", ["Mən getmirəm", "Mən getdim", "Mən gedirəm"], 0),
            ("Məchul fel **hansı cümlədə düzgündür?**", ["Ev təmizlənir", "Ev təmizlədi", "Ev təmizləyir"], 0)
        ],
        "cavab": [
            "madrese",
            "moalem",
            "daneshju",
            "Mən getmirəm",
            "Ev təmizlənir"
        ]
    }
}
