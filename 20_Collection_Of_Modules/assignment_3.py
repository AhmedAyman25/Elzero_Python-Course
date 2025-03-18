from PIL import Image
myImage = Image.open("H:\\Learn_Python\\20_Collection_Of_Modules\\Elzero.png")
# myImage.show()
# Image Size on my device (1342 x 896)

# Extratct Letter "L" From The Image

"""
left = 1342/3 = 447.33
top = 0
right = 1342/3 * 2 = 894.66
bottom = 896/2 = 448

"""
left = 447.33
top = 0
right = 894.66 
bottom = 448
box = (left, top, right, bottom)
L_Image = myImage.crop(box)
L_Image.show()

# Convert The Image To Grayscale
L_Image = L_Image.convert("L")
L_Image.show()

# Save The Image beside the original image
L_Image.save("H:\\Learn_Python\\20_Collection_Of_Modules\\L_Image.png")

# Crop the second row of the image
box = (0, 448, 1342, 896)
second_row = myImage.crop(box)
second_row.show()

# Rotate the second row 180 degrees
second_row_rotated = second_row.rotate(180).convert("L")
second_row_rotated.show()

# Save the rotated image
second_row_rotated.save("H:\\Learn_Python\\20_Collection_Of_Modules\\second_row_rotated.png")