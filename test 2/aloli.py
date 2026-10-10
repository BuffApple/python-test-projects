import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")  # Elegant dark background
screen.title("Heart Drawing for Alaa")

# Create turtle object
pen = turtle.Turtle()
pen.speed(3)  # Moderate speed to enjoy the drawing animation
pen.pensize(3)


# Function to draw the top curved parts of the heart
def draw_curve():
    for _ in range(200):
        pen.right(1)
        pen.forward(1.5)


# Function to draw the entire heart
def draw_heart():
    pen.up()
    pen.goto(0, -150)  # Move starting position down to center the heart
    pen.down()

    # Set colors: Red outline and Red fill
    pen.color("red", "red")
    pen.begin_fill()

    # Draw left side and top curve
    pen.left(140)
    pen.forward(175)
    draw_curve()

    # Draw right top curve and right side
    pen.left(120)
    draw_curve()
    pen.forward(175)

    pen.end_fill()


# Function to write the name in the middle
def write_name():
    pen.up()
    # Lift pen and position it right in the middle of the heart
    pen.goto(0, 35)
    pen.color("white")  # White text stands out on a red background
    pen.write("Alaa", align="center", font=("Arial", 28, "bold"))


# Execute the drawing steps
draw_heart()
write_name()

# Hide the turtle icon and keep the window open
pen.hideturtle()
screen.mainloop()