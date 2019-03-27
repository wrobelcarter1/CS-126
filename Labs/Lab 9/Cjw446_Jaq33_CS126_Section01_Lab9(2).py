# Carter Wrobel & Javier Quintana

# Jaq33 &

# November 6 2017

# CS 126 Section 1 Lab 9

# First import turtle so the program can draw

import turtle

# Set turtle to a small variable to make calling it much easier

t = turtle.Turtle()

# This function will remove the numbers we need for star position


def read_coords(file):

    # Dictionaries that will be holding most of information to plot and size

    coordinates = {}

    magnitudes = {}

    star_name = {}

    list = open(file, "r")

    # Begins to separate the lines we need from the file based on the numbers

    # That we will need (X and Y coordinate, Magnitude, and any possible names

    for line in list:

        point = line.split(" ")

        coordinates[point[3]] = [point[0], point[1]]

        magnitudes[point[3]] = [point[4]]

        if len(point) > 6:
            star_name[point[3]] = [point[6:]]
        else:
            continue

    # Saves all of our information for reference if needed

    star_info = (coordinates, magnitudes, star_name)

    def plot_by_magnitude(picture_size, coordinates_dict,

                          magnitudes_dict):
        # This loop runs through our dictionaries and takes the X and Y

        # coordinates that we split from the original text file

        # In the loop we also define the magnitude that says how long and

        # wide the stars inside the program will be

        for i in coordinates_dict:

            x = float(coordinates_dict[i][0])

            y = float(coordinates_dict[i][1])

            x_scale = x * 250

            y_scale = y * 250

            # Star size is the x-value from the magnitude dict

            magnitude_of_star = float(magnitudes_dict[i][0])

            # Magnitude is set right below here. If the magnitude ends

            # up trying to print bigger than 8x8 we restricted it

            z = round(10/(magnitude_of_star + 2))

            if z > 8:

                z = 8

            else:

                z = z

            # Test print

            # print(z)

            screen = turtle.Screen()

            screen.screensize(500, 500)

            screen.bgcolor("black")

            # This is how fast turtle will draw

            t.speed(0)

            screen.tracer(0)

            # This is where all of the drawing happens and the loop runs the

            # information we saved in those dictionaries

            t.penup()

            t.goto(x_scale, y_scale)

            t.pencolor("white")

            t.begin_fill()

            t.fillcolor("white")

            t.pendown()

            t.forward(z)

            t.left(90)

            t.forward(z)

            t.left(90)

            t.forward(z)

            t.left(90)

            t.forward(z)

            t.end_fill()

            t.penup()

            t.hideturtle()

    plot_by_magnitude(500, coordinates, magnitudes)


print(read_coords('stars.txt'))
