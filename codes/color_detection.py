import cv2 as cv
import webcolors
import matplotlib.pyplot as plt

color_names = {
    "#FF0000": "Red",
    "#00FF00": "Green",
    "#0000FF": "Blue",
    "#FFFFFF": "White",
    "#000000": "Black",
    # Add more colors as needed
    
    
}

def closest_color(rgb):
    differences={}
    for color_hex, color_name in color_names.items():
        r ,g,b = webcolors.hex_to_rgb(color_hex)
        differences[sum([(r-rgb[0]) **2,
                         (g-rgb[1] **2,),
                         (b-rgb[2]) ** 2])] = color_name
    return differences[min(differences.keys())]    

color=(113,241,244)

try:
    cname= webcolors.rgb_to_name(color)
    print(f"The color is exactly{cname}")

except ValueError:
    cname = closest_color(color)
    print(f"The color is closest to {cname}")

plt.imshow([color])
plt.show()
    