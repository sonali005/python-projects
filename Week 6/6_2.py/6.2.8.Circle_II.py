"""Begin implementing the circle drawing function to handle depths of 0 
and 1.
16
● Open your activities module and create a function named “circles” that 
declares parameters for radius and recursion depth.
● Implement the base case for a depth of 0.
○ Do not draw a circle.
○ Return a circumference of 0.
● Implement another base case for a depth of 1.
○ Draw a circle of the specified radius.
○ Return the circumference of the circle just drawn.
○ You may import the math module and use math.pi if you wish.
● Test your function from mai"""

import turtle
import math

def circles(radius, depth):
    if depth == 0:
        return 0
    
    elif depth == 1:
        turtle.penup()
        turtle.goto(0, -radius)  # Position turtle to start circle drawing
        turtle.pendown()
        turtle.circle(radius)  # Draw circle with turtle
        return 2 * math.pi * radius  # Return the circumference

if __name__ == "__main__":
    turtle.speed(1)  # Set speed for drawing (1 is slow, adjust if needed)
    
    # Test the circles function with depth 0 and 1
    print("Testing circles function with depth 0 and 1:")
    circumference_depth_0 = circles(50, 0)
    print(f"Circumference at depth 0: {circumference_depth_0}")

    circumference_depth_1 = circles(50, 1)
    print(f"Circumference at depth 1: {circumference_depth_1}")
    
    turtle.done()


