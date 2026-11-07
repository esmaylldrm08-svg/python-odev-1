# ==============================================================================
# Ad Soyad   : Esma Yıldırım
# Öğrenci No : 20253004004
# Tarih      : 07.11.2026
# Açıklama   : Görev 5 - turtle modülü ile bir kare ve üstüne bir üçgen çizerek
#              ev oluşturan ve evin yanına ad yazdıran program.
# ==============================================================================

import turtle

# Çizim hızını ve kalem özelliklerini ayarlayalım
turtle.speed(3)
turtle.pensize(3)

# 1. Aşama: Evin kare gövdesini çizelim
# Çizime uygun bir başlangıç noktasından (-100, -80) başlayalım
turtle.penup()
turtle.goto(-100, -80)
turtle.pendown()

turtle.color("navy")
turtle.forward(120)  # Taban çizgisi
turtle.left(90)
turtle.forward(120)  # Sağ duvar
turtle.left(90)
turtle.forward(120)  # Tavan çizgisi
turtle.left(90)
turtle.forward(120)  # Sol duvar
turtle.left(90)

# 2. Aşama: Evin üçgen çatısını çizelim
# Çatının başlangıç noktası olan sol üst köşeye (-100, 40) çıkalım
turtle.left(90)
turtle.forward(120)
turtle.right(90)

# Üçgen çatı (Eşkenar üçgen: kenar uzunluğu 120 birim)
turtle.color("darkred")
turtle.left(60)
turtle.forward(120)  # Çatının sol eğimi (tepe noktasına varış)
turtle.right(120)
turtle.forward(120)  # Çatının sağ eğimi (sağ üst köşeye varış)

# 3. Aşama: Evin yanına ad ve soyad yazdıralım
turtle.penup()
turtle.goto(40, 10)  # Evin hemen sağ tarafına konumlanma
turtle.color("darkgreen")
turtle.write("Esma Yıldırım", font=("Arial", 16, "bold"))

# Kaplumbağa imlecini gizleyelim ve çizim penceresini açık tutalım
turtle.hideturtle()
turtle.done()
