import turtle

def draw_pifagor_tree(branch_length, t, angle, level):
    if level == 0:
        return
    else:
        t.forward(branch_length)
        t.left(angle)
        draw_pifagor_tree(0.7 * branch_length, t, angle, level-1)
        t.right(2 * angle)
        draw_pifagor_tree(0.7 * branch_length, t, angle, level-1)
        t.left(angle)
        t.backward(branch_length)

def main():
    level = int(input("Введіть рівень рекурсії: "))
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.color("blue")

    branch_length = 100
    angle = 45    

    t.left(90)
    draw_pifagor_tree(branch_length, t, angle, level)

    screen.exitonclick()

if __name__ == "__main__":
    main()
