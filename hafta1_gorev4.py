# ==============================================================================
# Ad Soyad   : Esma Yıldırım
# Öğrenci No : 20253004004
# Tarih      : 07.11.2026
# Açıklama   : Görev 4 - Verilen üç koddaki hata türlerini (sözdizimi, çalışma
#              zamanı, mantık) ve nedenlerini yorum satırlarıyla açıklayıp
#              kodları düzelten program.
# ==============================================================================

# ------------------------------------------------------------------------------
# Program A
# Orijinal Kod : print("Merhaba Dünya)
# Hata Türü    : Sözdizimi Hatası (Syntax Error)
# Hata Nedeni  : Çift tırnak ile açılan metin dizesinin (string literal) kapatma
#                tırnağı unutulmuştur. Python satır sonuna geldiğinde metnin
#                kapanmadığını fark eder ve 'SyntaxError' verir.
# Düzeltilmiş Hali:
print("Merhaba Dünya")

# ------------------------------------------------------------------------------
# Program B
# Orijinal Kod : print(10 / 0)
# Hata Türü    : Çalışma Zamanı Hatası (Runtime Error - ZeroDivisionError)
# Hata Nedeni  : Matematikte bir sayının sıfıra bölünmesi tanımsızdır. Python
#                kodu sözdizimi açısından doğru kabul etse de çalıştırma anında
#                bir sayıyı 0'a bölemez ve 'ZeroDivisionError' fırlatarak çöker.
# Düzeltilmiş Hali:
# Payda kısmı sıfır olmayan geçerli bir sayıya (örneğin 2) dönüştürülmüştür.
print(10 / 2)

# ------------------------------------------------------------------------------
# Program C
# Orijinal Kod : print(3 + 5 / 2)
# Hata Türü    : Mantık Hatası (Logic Error)
# Hata Nedeni  : Program sözdizimi ve çalışma zamanı açısından hatasız çalışır
#                ancak amaç 3 ve 5'in ortalamasını (4.0) bulmaktır. Matematiksel
#                işlem önceliği gereği Python önce bölme işlemini yapar
#                (5 / 2 = 2.5), ardından 3 ile toplayarak 5.5 sonucunu üretir.
#                Ortalamanın doğru hesaplanabilmesi için toplama işleminin
#                parantez içine alınması gerekir.
# Düzeltilmiş Hali:
print((3 + 5) / 2)
