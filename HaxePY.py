import turtle
import keyboard

turtle.title("HaxePY engine free")

class window:
    def title(title):
        turtle.title(title)
    def run():
        turtle.mainloop()
class player:
    def player(shape, size, speed, color, x, y):
        global player
        player = turtle.Turtle()
        player.penup()
        player.pendown()
        player.shape(shape)
        player.turtlesize(size)
        player.color(color)
        player.goto(x, y)
        player.speed(speed)
        while True:
            if keyboard.is_pressed('up'):
                player.forward(50)
            elif keyboard.is_pressed('down'):
                player.back(50)
            elif keyboard.is_pressed('left'):
                player.left(50)
            elif keyboard.is_pressed('right'):
                player.right(50)
            elif keyboard.is_pressed('esc'):
                quit()

        