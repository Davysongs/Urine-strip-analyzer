import cv2
import numpy as np

def process_image(image):
    # Convert the image to a numpy array
    np_img = np.frombuffer(image.read(), np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    # Convert the image to grayscale and apply thresholding to create a binary image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Sort contours from top to bottom
    contours = sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[1])

    # Define the order of test regions on the strip
    test_regions = ['URO', 'BIL', 'KET', 'BLD', 'PRO', 'NIT', 'LEU', 'GLU', 'SG', 'PH']

    # Initialize a dictionary to store RGB values
    colors = {}

    # Loop through the detected contours and extract RGB values
    for i, contour in enumerate(contours[:len(test_regions)]):
        # Get the bounding box of the contour
        x, y, w, h = cv2.boundingRect(contour)
        
        # Extract the region of interest (ROI) from the image
        roi = img[y:y+h, x:x+w]
        
        # Calculate the mean RGB values of the ROI
        mean_color = cv2.mean(roi)[:3]
        
        # Store the RGB values in the dictionary
        colors[test_regions[i]] = [int(mean_color[2]), int(mean_color[1]), int(mean_color[0])]  # Convert to RGB

    return colors
