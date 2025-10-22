import math

cell_w = 10
cell_h = 10

def pixel_to_triangle(x,y):
    '''
    This function will compute and return the triangle the provided pixel coordinates are
    located in.
    '''

    if (x % cell_w) == 0 or (y % cell_h) == 0:
         raise ValueError("Unable to determine triangle - this value lands on a border of the cell")

    col = math.floor(x / cell_w)
    row = math.floor(y / cell_h)

    cell_x = x % cell_w 
    cell_y = y % cell_h
    
    line_y = (cell_h / cell_w) * cell_x


    #determine if pixels are above or below diagonal line
    if cell_y > line_y:
        #below line in cell
        triangle_num = (col * 2) + 1

    elif cell_y == line_y:
         #landing on diagaonal line
         raise ValueError("Unable to determine triangle - " \
         "this value lands on the middle of the diagonal line that seperates the cell.")
    else:
        #above line in cell
        triangle_num = (col * 2) + 2

    letter = chr((ord("A") + row)).upper()

    return f"{letter}{triangle_num}"

def triangle_to_pixel(label):
    '''
    This function will compute and return the central pixel coordinates for the given triangle designator.
    '''

    number = int(label[1:])
    letter = label[0].upper()

    if ord(letter) < 65 or ord(letter) > 90:
            #number is below or above "A" or "Z" on ascii table
            raise ValueError("Y coordinate outside of range: Try again.")

    row = (ord(letter) - ord("A")) + 1
    col = math.ceil(number / 2)

    cell_x = col * cell_w
    cell_y = row * cell_h

    if number % 2 == 1:
        #below line in cell
        x_pixel = cell_x - (2 * cell_w / 3)
        y_pixel = cell_y - (cell_h / 3)
    else:
        #above line in cell
        x_pixel = cell_x - (cell_w / 3)
        y_pixel = cell_y - (2 * cell_h / 3) 

    if x_pixel <= 0 or y_pixel <= 0:
         raise TypeError("Coordinates not valid - they are outside of bounds: Try again.")

    return (x_pixel, y_pixel)