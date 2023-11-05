# import packages
import numpy as np
import cv2
import os
import matplotlib.pyplot as plt
# caution
print  ("\n********************************************************************")
print("*\tThis programme is used to identify a green colour colonies,*")
print("*\tand the count result, is based on the image you upload     *")
print("*                                                                  *")
print("********************************************************************\n")
print("\t\t\tCaution")
print ("Upload a good image with extantion to count colonies in the image.\n")
#cheek image path
def image_not_found_handler(image_path):
    if os.path.exists(image_path):
        # Image file exists
        print(f"Image '{image_path}' found.\n You can proceed to obtain\n")
    else:
        # Image file does not exist
        print(f"Image '{image_path}' not found. Please provide a valid image path.")
if __name__ == "__main__":
    image_path = input("Enter the path of image file\n ")
    image_not_found_handler(image_path)
img = cv2.imread(image_path)
# blur and convert to grey scale
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(grey, (11, 11), 0)
# canny edge detector
edges = cv2.Canny(blur, 30, 150)
# locate edges
(cnts, _) = cv2.findContours(edges, cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE)
# draw edges - drawing on img will over write the original
result = img.copy()
cv2.drawContours(result, cnts, -1, (1, 255, 0), 2)
# count the number of colony
print("Result\n")
if len== 0:
    print("no cell found")
# write how many heads there are
cv2.putText(result, str(len(cnts)) + " colonys", (0, 70), cv2.FONT_HERSHEY_DUPLEX,
            1.5, (255, 0, 0))
cv2.waitKey(0)
# Draw a Grid on image
image = cv2.imread(image_path)
# Define the number of rows and columns for the grid
num_rows = 6
num_cols = 6
# Get the height and width of the image
height, width, _ = image.shape
# Calculate the spacing between grid lines
row_spacing = height // num_rows
col_spacing = width // num_cols
# Draw horizontal grid lines
for i in range(1, num_rows):
    y = i * row_spacing
    cv2.line(image, (0, y), (width, y), (0, 0, 255), 1)  # Red lines
# Draw vertical grid lines
for j in range(1, num_cols):
    x = j * col_spacing
    cv2.line(image, (x, 0), (x, height), (0, 0, 255), 1)  # Red lines
#Green
# Convert the image to the HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# Define the lower and upper HSV range for green color (adjust as needed)
lower_green = np.array([40, 50, 40])
upper_green = np.array([90, 255, 255])
# Create a mask to extract green regions
mask = cv2.inRange(hsv, lower_green, upper_green)
# Find contours in the mask
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Filter out small contours (adjust the minimum area as needed)
min_contour_area = 100
green_objects = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour_area]
# Count and display the number of green objects
num_green_objects = len(green_objects)
print(f'Number of green objects in the petri dish: {num_green_objects}')
# draw the green circule on the original image
cv2.drawContours(image, green_objects, -1, (0, 255, 0), 2)
# Display the image with green contours
print(len(cnts),"total colonies in image\n")
#cv2.imshow('Green Objects in Petri Dish', image)
print("If you like to save a colour grid image, save it yourself.")
# Display the image with the grid
plt.imshow(image)
plt.waitforbuttonpress()
plt.close('all')
cv2.destroyAllWindows()
print ("Slice image saved for you recod with name green.jpg")
#save green image count in floder
imask = mask>0
green = np.zeros_like(img, np.uint8)
green[imask] = img[imask]
cv2.imwrite("green.jpg",green)
img = cv2.imread("green.jpg")
plt.imshow(img)
plt.waitforbuttonpress()
plt.close('all')

print("Close a window by clicking on it.\n")
print ("Information picture\n")
print("You upload this image to obtain the result.")
print(image_path)
input("enter to exit")
##Computational screening of green colour colonies from petri dish through python tool GD.A1.
##Muhammad Aziz email aziz1sh@hotmail.com
