
import turtle

def draw_square(some_turtle):
    for i in range (1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(50)
    angie = turtle.Turtle()
    angie.shape("turtle")
    angie.color("yellow")
    angie.speed(50)
    red = turtle.Turtle()
    red.shape("arrow")
    red.color("blue")
    red.speed(50)
    black = turtle.Turtle()
    black.shape("arrow")
    black.color("black")
    black.speed(50)
    for i in range (1,37):
        draw_square(brad)
        brad.right(10)
    for i in range (1,46):
        draw_square(angie)
        angie.left(8)
    for i in range (1,60):
        draw_square(red)
        red.right(6)
    for i in range (1,90):
        draw_square(black)
        black.left(4)
    for i in range (1,360):
        draw_square(angie)
        angie.left(2)
    for i in range (1,560):
        draw_square(red)
        red.right(1) 
        window.exitonclick()
draw_art()
