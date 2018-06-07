__author__ = "Anton"
"""This is a program to compute the areas of selected shapes based on user input."""
# Programmer: Anton Lachmaniucu
# Date: October 16th, 2017


def main():
    import time
    # Instantiate the lists that will contain all the volumes
    cvolumes = []
    pvolumes = []
    evolumes = []
    # While sentinel
    isquit = "FALSE"
    # Error sentinel
    iserror = "FALSE"
    # Dealing with user input recursively
    while isquit == "FALSE":
        if iserror == "FALSE":
            print("There are three shape options, cube, ellipsoid, pyramid:")
            shapetype = input("Please enter which shape you want the volume computed for: ").upper()
        if shapetype == "CUBE":
            # Dimensional inputs
            sidelength = float(input("Please enter the side length for the cube: "))
            # Append volumes to list
            cvolumes.append(cubevolume(sidelength))
            iserror = "FALSE"
        elif shapetype == "PYRAMID":
            # Dimensional inputs
            lengthofbase = float(input("Please enter the base length of the pyramid: "))
            pyramidheight = float(input("Please enter the pyramid height: "))
            # Append volumes to list
            pvolumes.append(pyramidvolume(lengthofbase, pyramidheight))
            iserror = "FALSE"
        elif shapetype == "ELLIPSOID":
            # Dimensional inputs
            radii1 = float(input("Please enter the first radius of the ellipsoid: "))
            radii2 = float(input("Please enter the second radius of the ellipsoid: "))
            radii3 = float(input("Please enter the third radius of the ellipsoid: "))
            # Append volumes to list
            evolumes.append(ellipsoidvolume(radii1, radii2, radii3))
            iserror = "FALSE"
        elif shapetype == "QUIT":
            # Sentinel activation
            isquit = "TRUE"
        else:
            shapetype = input("That shape type is not valid, please enter a valid shape: ").upper()
            iserror = "TRUE"
    if isquit == "TRUE":
        print("You have reached the end of the session!")
        # Check for empty lists and print out statements accordingly
        if cvolumes != [] and pvolumes != [] and evolumes != []:
            print("The values you have computed are below: ")
            print("CUBE ", end=": ")
            cvolumes.sort()
            listwobrackets(cvolumes)
            print("PYRAMID ", end=": ")
            pvolumes.sort()
            listwobrackets(pvolumes)
            print("ELLIPSOID ", end=": ")
            evolumes.sort()
            listwobrackets(evolumes)
            # Done to allow for the viewing of the final answers with the command prompt as well
            time.sleep(5.5)
        elif cvolumes == [] and pvolumes != [] and evolumes != []:
            print("The values you have computed are below: ")
            print("CUBE : No Computations for this shape.")
            print("PYRAMID ", end=": ")
            pvolumes.sort()
            listwobrackets(pvolumes)
            print("ELLIPSOID :", sorted(evolumes))
            evolumes.sort()
            listwobrackets(evolumes)
            # Done to allow for the viewing of the final answers with the command prompt as well
            time.sleep(5.5)
        elif cvolumes != [] and pvolumes == [] and evolumes != []:
            print("The values you have computed are below: ")
            print("CUBE ", end=": ")
            cvolumes.sort()
            listwobrackets(cvolumes)
            print("PYRAMID : No Computations for this shape.")
            print("ELLIPSOID ", end=": ")
            evolumes.sort()
            listwobrackets(evolumes)
            # Done to allow for the viewing of the final answers with the command prompt as well
            time.sleep(5.5)
        elif cvolumes != [] and pvolumes != [] and evolumes == []:
            print("The values you have computed are below: ")
            print("CUBE ", end=": ")
            cvolumes.sort()
            listwobrackets(cvolumes)
            print("PYRAMID ", end=": ")
            pvolumes.sort()
            listwobrackets(pvolumes)
            # Done to allow for the viewing of the final answers with the command prompt as well
            time.sleep(5.5)
            print("ELLIPSOID : No Computations for this shape.")
        elif cvolumes == [] and pvolumes != [] and evolumes == []:
            print("The values you have computed are below: ")
            print("CUBE : No Computations for this shape.")
            print("PYRAMID ", end=": ")
            pvolumes.sort()
            listwobrackets(pvolumes)
            print("ELLIPSOID : No Computations for this shape.")
            # Done to allow for the viewing of the final answers with the command prompt as well
            time.sleep(5.5)
        elif cvolumes == [] and pvolumes == [] and evolumes != []:
            print("The values you have computed are below: ")
            print("CUBE : No Computations for this shape.")
            print("PYRAMID : No Computations for this shape.")
            print("ELLIPSOID ", end=": ")
            evolumes.sort()
            listwobrackets(evolumes)
            # Done to allow for the viewing of the final answers with the command prompt as well
            time.sleep(5.5)
        elif cvolumes != [] and pvolumes == [] and evolumes == []:
            print("The values you have computed are below: ")
            print("CUBE ", end=": ")
            cvolumes.sort()
            listwobrackets(cvolumes)
            print("PYRAMID : No Computations for this shape.")
            print("ELLIPSOID : No Computations for this shape.")
            # Done to allow for the viewing of the final answers with the command prompt as well
            time.sleep(5.5)
    else:
        # If all the lists are empty
        print("You did not perform any volume calculations.")
        # Done to allow for the viewing of the final answers with the command prompt as well
        time.sleep(5.5)


# Function to calculate cube volume for non zero dimensions
def cubevolume(lengthofside):
    while True:
        if lengthofside > 0:
            volume = round(lengthofside**3, 1)
            print("The volume of a cube with a side length of {} is: {}".format(round(lengthofside, 1), round(volume,1)))
            break
        else:
            lengthofside = float(input("Please enter a non zero length for the cube: "))
    return float(volume)


# Function to calculate pyramid volume for non zero dimensions
def pyramidvolume(baselength, height):
    while True:
        if baselength <= 0:
            baselength = float(input("Please enter a non zero base length: "))
            continue
        elif height <= 0:
            height = float(input("Please enter a non zero pyramid height: "))
            continue
        else:
            volume = round(((baselength**2)*height)/3, 1)
            print("The volume of the pyramid with base length of {} and height {} is: {}".format(round(baselength, 1), round(height, 1), round(volume, 1)))
            break
    return float(volume)


# Function to calculate ellipsoid volume for non zero dimensions
def ellipsoidvolume(radius1, radius2, radius3):
    from math import pi
    while True:
        if radius1 <= 0:
            radius1 = float(input("Please enter a non zero value for the first radius: "))
            continue
        elif radius2 <= 0:
            radius2 = float(input("Please enter a non zero value for the second radius: "))
            continue
        elif radius3 <= 0:
            radius3 = float(input("Please enter a non zero value for the third radius: "))
        else:
            volume = round((4*pi*radius1*radius2*radius3)/3, 1)
            print("The volume of an ellipsoid with dimensions of {} by {} by {} is: {}".format(round(radius1, 1), round(radius2, 1), round(radius3, 1), round(volume, 1)))
            break
    return float(volume)

# Function to print out list elements without brackets.
def listwobrackets(listelements):
    for i in range(len(listelements)):
        if listelements[i] == listelements[len(listelements) - 1]:
            print(listelements[i])
        else:
            print(listelements[i], end=", ")


main()
