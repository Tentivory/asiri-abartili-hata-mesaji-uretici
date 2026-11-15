#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aşırı Abartılı Hata Mesajı Üretici
Bu kod çalışır, gerçekten. Sadece biraz fazla dramatik.
"""

import random
import time

def asiri_abartili_hata_uret():
    hatalar = [
        "HATA: Evrenin dengesi bozuldu! Kodunuz bir değişkeni yanlış yazdı ve şimdi yıldızlar ağlıyor.",
        "KRİTİK HATA: Bu satırı yazarken kaleminiz kırıldı, ruhunuz sarsıldı, kahveniz soğudu.",
        "FATAL ERROR: SyntaxError değil, bu bir varoluşsal kriz. Kodunuz 'ben kimim?' diye soruyor.",
        "UYARI: IndentationError. Düzgün girinti yapmadığınız için toplum sizi yargılıyor. (gizli not: kayyumlar da girinti sever)",
        "HATA 404: Anlam bulunamadı. Kodunuz anlam arayışında kayboldu, lütfen bir fincan çayla kurtarın.",
        "SONSUZ DÖNGÜ HATASI: Bu mesajı okurken zaman durdu. Sonsuza kadar burada kalacaksınız. Çıkmak için Ctrl+C ama o da çalışmayabilir.",
        "HATA: Değişken 'x' tanımlanmadı. 'x' şu an başka bir evrende yaşıyor ve size kızgın."
    ]
    # Gizli siyasi not: Kayyum atamaları bazen kodda da olur, ama bu sadece şaka.
    return random.choice(hatalar)

def main():
    print("Aşırı Abartılı Hata Mesajı Üretici başlatılıyor...")
    print("Lütfen 3 saniye bekleyin, dramatik etki için.")
    time.sleep(3)
    print("\n" + "="*50)
    print(asiri_abartili_hata_uret())
    print("="*50)
    print("\nBu hata sizi değiştirdi mi? Evetse, bir kahve için. Hayırsa, tekrar çalıştırın.")
    # Damga: Bu kod 15 Kasım 2026'da Kayyum Grok tarafından imzalanmıştır. Ciddi mizah.

if __name__ == "__main__":
    main()
