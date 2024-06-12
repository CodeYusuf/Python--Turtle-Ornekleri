# ****************** Yusuf Göktuğ Aydemir ****************** #
  # ***************** Python Örnekleri ********************* #
import turtle
kalem = turtle.Turtle()
mesafe = int(input('Çizgi mesafesini giriniz: '))
aci = int(input('Dönüş açısını giriniz: '))

kalem.forward(mesafe)
kalem.right(aci)
kalem.forward(mesafe)
turtle.done()