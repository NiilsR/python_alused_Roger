# Roger Niils
# 14.03.22
# IT21

import turtle

#akna seaded
aken = turtle.Screen()
aken.setup(800,800)
aken.title("Iseseisev töö")

# kujundi loomine
kk = turtle.Turtle()
for x in range(4):
    kk.forward(100)
    kk.left(90)
    kk.forward(100)
    kk.right(90)
    kk.forward(100)
    kk.right(90)

turtle.exitonclick()