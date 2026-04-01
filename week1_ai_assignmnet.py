# AI 프로그래밍 입문 - Week 1
# antigravity 세팅해서 간단한 프로젝트 만들어서 github repository 로 push하기

# turtle을 이용해서 네잎크로버 그리기
import turtle

def draw_clover_leaf(t, radius, fwd_length):
    """
    Draws a heart-like clover leaf using forward and semicircle motions.
    The starting angle should be set prior to calling this function.
    """
    t.begin_fill()
    t.forward(fwd_length)
    t.circle(radius, 180) # Left curve
    t.right(90)           # Sharp corner for the heart top
    t.circle(radius, 180) # Right curve
    t.forward(fwd_length)
    t.end_fill()

def draw_clover():
    screen = turtle.Screen()
    screen.bgcolor("#eaffea")
    screen.title("Lucky Guy Clover")

    t = turtle.Turtle()
    t.speed(0) # Fastest drawing speed
    
    center_x = 0
    center_y = 50

    # Draw Stem
    t.penup()
    t.goto(center_x, center_y)
    t.pendown()
    t.color("#1b5e20")
    t.pensize(15)
    t.setheading(285) # Angle downwards
    
    # Draw curved stem
    for _ in range(40):
        t.forward(5)
        t.left(0.5)
        
    # Draw 4 Leaves
    t.pensize(2)
    t.color("#2E7D32", "#4CAF50") # Outline, Fill color
    
    for i in range(4):
        t.penup()
        t.goto(center_x, center_y)
        t.pendown()
        # Angles: 45, 135, 225, 315 gives a nice four-leaf clover spread
        t.setheading(45 + i * 90)
        draw_clover_leaf(t, radius=35, fwd_length=70)

    # Add shadow effect for text
    t.penup()
    t.goto(center_x + 2, center_y - 20 - 2)
    t.color("#1b5e20")
    t.write("lucky_guy", align="center", font=("Arial", 36, "bold"))
    
    # Add main text "lucky_guy"
    t.goto(center_x, center_y - 20)
    t.color("white")
    t.write("lucky_guy", align="center", font=("Arial", 36, "bold"))

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    draw_clover()
