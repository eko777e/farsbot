# tests.py
# Struktur: "Gün X": {"sual": [(sual_text, [variant1, variant2, variant3], düzgün_index), ...]}

daily_tests = {
    "Gün 1": {
        "sual": [
            ("سلام **hansı bənddə düzgün yazılıb?**", ["salam", "selam", "sallam"], 0),
            ("خوب **hansı bənddə düzgün yazılıb?**", ["xub", "khub", "xoop"], 0),
            ("دوست **hansı bənddə düzgün yazılıb?**", ["dust", "doost", "dostt"], 0),
            ("İndiki zaman fel **hansı cümlədə düzgündür?**", ["Mən gedirəm", "Mən getdim", "Mən gedəcəyəm"], 0),
            ("İndiki zaman fel **hansı cümlədə düzgündür?**", ["Sən oxuyursan", "O yazdı", "Biz gələcəyik"], 0)
        ]
    },
    "Gün 2": {
        "sual": [
            ("مدرسه **hansı bənddə düzgün yazılıb?**", ["madrese", "madraze", "madres"], 0),
            ("معلم **hansı bənddə düzgün yazılıb?**", ["moalem", "moalemm", "mualem"], 0),
            ("دانشجو **hansı bənddə düzgün yazılıb?**", ["daneshju", "daneshjoo", "daneshyoo"], 0),
            ("Zamanların inkarı **hansı cümlədə düzgündür?**", ["Mən getmirəm", "Mən getdim", "Mən gedirəm"], 0),
            ("Zamanların inkarı **hansı cümlədə düzgündür?**", ["Sən oxumursan", "O yazdı", "Biz gələcəyik"], 0)
        ]
    },
    "Gün 3": {
        "sual": [
            ("کتاب **hansı bənddə düzgün yazılıb?**", ["ketab", "kitab", "ketopp"], 0),
            ("خانه **hansı bənddə düzgün yazılıb?**", ["xane", "khane", "khan"], 0),
            ("دوست **hansı bənddə düzgün yazılıb?**", ["dust", "doost", "dost"], 0),
            ("Məchul fel **hansı cümlədə düzgündür?**", ["Kitab oxunur", "Kitab oxudu", "Kitab oxuyur"], 0),
            ("Məchul fel **hansı cümlədə düzgündür?**", ["Ev təmizlənir", "Ev təmizlədi", "Ev təmizləyir"], 0)
        ]
    },
    "Gün 4": {
        "sual": [
            ("دوچرخه **hansı bənddə düzgün yazılıb?**", ["docharkhe", "docharkh", "docharh"], 0),
            ("هواپیما **hansı bənddə düzgün yazılıb?**", ["havapeyma", "havapema", "havapima"], 0),
            ("ماشین **hansı bənddə düzgün yazılıb?**", ["mashin", "mashien", "mashinm"], 0),
            ("Əmr fel **hansı cümlədə düzgündür?**", ["Oxu!", "Yazdı!", "Gələcək!"], 0),
            ("Əmr fel **hansı cümlədə düzgündür?**", ["Gəl!", "Mən gedirəm", "Siz oxuyacaqsınız"], 0)
        ]
    },
    "Gün 5": {
        "sual": [
            ("سیب **hansı bənddə düzgün yazılıb?**", ["sib", "seeb", "sibp"], 0),
            ("موز **hansı bənddə düzgün yazılıb?**", ["moz", "mouz", "mooz"], 0),
            ("پرتقال **hansı bənddə düzgün yazılıb?**", ["porteghal", "portegal", "porteghel"], 0),
            ("Qəsdi niyyət fel **hansı cümlədə düzgündür?**", ["Mən gedəcəyəm", "Mən gedirəm", "Mən getdim"], 0),
            ("Qəsdi niyyət fel **hansı cümlədə düzgündür?**", ["Sən oxuyacaqsan", "O yazır", "Biz gəldik"], 0)
        ]
    }
}

# 6-dan 40-a qədər avtomatik doldurulur
for i in range(6, 41):
    daily_tests[f"Gün {i}"] = {
        "sual": [
            (f"Söz {i}a **hansı bənddə düzgün yazılıb?**", [f"variant_a{i}", f"variant_b{i}", f"variant_c{i}"], 0),
            (f"Söz {i}b **hansı bənddə düzgün yazılıb?**", [f"variant_a{i}", f"variant_b{i}", f"variant_c{i}"], 0),
            (f"Söz {i}c **hansı bənddə düzgün yazılıb?**", [f"variant_a{i}", f"variant_b{i}", f"variant_c{i}"], 0),
            (f"Gün {i} qrammatika sualı 1 **hansı cümlədə düzgündür?**", [f"variant_a{i}", f"variant_b{i}", f"variant_c{i}"], 0),
            (f"Gün {i} qrammatika sualı 2 **hansı cümlədə düzgündür?**", [f"variant_a{i}", f"variant_b{i}", f"variant_c{i}"], 0)
        ]
    }
