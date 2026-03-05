import random
def estimated_pi():
    try:
        ran = int(input("How many random points you would like to generate? "))
    except ValueError:
        print("Please enter a valid number.")
        return
    points_inside_circle = 0
    for _ in range(ran):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 < 1:
            points_inside_circle += 1
    approx_pi = 4 * (points_inside_circle / ran)
    print(f"Total points generated: {ran}")
    print(f"Points inside circle: {points_inside_circle}")
    print(f"Approximated value of pi: {approx_pi}")
estimated_pi()