# ==============================================================================
# Ad Soyad   : Esma Yıldırım
# Öğrenci No : 20253004004
# Tarih      : 07.11.2026
# Açıklama   : Bonus Görev - turtle modülü ile birbirine geçmiş beş adet
#              olimpiyat halkasını (mavi, siyah, kırmızı, sarı, yeşil) çizen
#              program.
# ==============================================================================

import turtle

# Kalem kalınlığı ve çizim hızı ayarları
turtle.speed(3)
turtle.pensize(5)

# Dairelerin yarıçapı
yaricap = 45

# ------------------------------------------------------------------------------
# 1. Üst Sıra - 1. Daire: Mavi Halka (Sol)
# ------------------------------------------------------------------------------
turtle.penup()
turtle.goto(-110, -25)
turtle.pendown()
turtle.color("blue")
turtle.circle(yaricap)

# ------------------------------------------------------------------------------
# 2. Üst Sıra - 2. Daire: Siyah Halka (Orta)
# ------------------------------------------------------------------------------
turtle.penup()
turtle.goto(0, -25)
turtle.pendown()
turtle.color("black")
turtle.circle(yaricap)

# ------------------------------------------------------------------------------
# 3. Üst Sıra - 3. Daire: Kırmızı Halka (Sağ)
# ------------------------------------------------------------------------------
turtle.penup()
turtle.goto(110, -25)
turtle.pendown()
turtle.color("red")
turtle.circle(yaricap)

# ------------------------------------------------------------------------------
# 4. Alt Sıra - 4. Daire: Sarı Halka (Mavi ve Siyah arasına geçiş)
# ------------------------------------------------------------------------------
turtle.penup()
turtle.goto(-55, -70)
turtle.pendown()
turtle.color("gold")
turtle.circle(yaricap)

# ------------------------------------------------------------------------------
# 5. Alt Sıra - 5. Daire: Yeşil Halka (Siyah ve Kırmızı arasına geçiş)
# ------------------------------------------------------------------------------
turtle.penup()
turtle.goto(55, -70)
turtle.pendown()
turtle.color("green")
turtle.circle(yaricap)

# Kaplumbağa imlecini gizleyelim ve pencereyi açık tutalım
turtle.hideturtle()
turtle.done()
