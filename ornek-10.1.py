# ****************** Yusuf Göktuğ Aydemir ****************** #
  # ***************** Python Örnekleri ********************* #
import turtle
kalem = turtle.Turtle()
kalem.shape('turtle')
for y in range(4):
    for x in range(4):
        kalem.up()
        kalem.forward(20)
        kalem.dot()
        kalem.down()
        kalem.forward(20)
        kalem.dot()
    kalem.right(90)

turtle.done()