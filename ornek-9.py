# ****************** Yusuf Göktuğ Aydemir ****************** #
  # ***************** Python Örnekleri ********************* #
import turtle
kalem = turtle.Turtle()
kalem.shape('turtle')
kalem.forward(100)
kalem.penup()
kalem.goto(0, 100)
for x in range(5):
    kalem.dot()
    kalem.forward(20)
turtle.done()