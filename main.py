
import sys
from computation import pixel_to_triangle, triangle_to_pixel

def main():
    command = sys.argv[1].lower()

    if command == "pixel_to_triangle":
        x = int(sys.argv[2])
        y = int(sys.argv[3])

        if y > 259:
            raise ValueError("Y coordinate outside of range: Try again.")

        location = pixel_to_triangle(x,y)
        print(location)

    elif command == "triangle_to_pixel":
        label = sys.argv[2]

        pixels = triangle_to_pixel(label)
        print(pixels)
            
    else:
        raise ValueError("Invalid input: Try again.")


if __name__ == "__main__":
    main()