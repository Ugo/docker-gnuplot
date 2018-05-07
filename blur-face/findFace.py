from PIL import Image
import face_recognition
import sys
import cv2

image_file=sys.argv[1]

# Load the jpg file into a numpy array
image = face_recognition.load_image_file(image_file)

# Find all the faces in the image using the default HOG-based model.
# This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
# See also: find_faces_in_picture_cnn.py
face_locations = face_recognition.face_locations(image)

print("I found {} face(s) in this photograph.".format(len(face_locations)))
count = 0;
for top, right, bottom, left in face_locations:
    
 # Extract the region of the image that contains the face
    face_image = image[top:bottom, left:right]
    face_image = cv2.GaussianBlur(face_image, (99, 99), 30)
    image[top:bottom, left:right] = face_image

    count = count + 1;
    # Print the location of each face in this image
    #top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # You can access the actual face itself like this:
    #face_image = image[top:bottom, left:right]
    #pil_image = Image.fromarray(face_image)
imageName = "/iexec/test.bmp"
pil_image = Image.fromarray(image)
pil_image.save(imageName)

