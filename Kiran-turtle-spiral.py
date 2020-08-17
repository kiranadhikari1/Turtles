import turtle

t = turtle.Turtle()

count = 0
t.speed(300)
while count < 350:
    t.forward(50)
    t.right(20 + count/5)
    count = count + 1

input()
