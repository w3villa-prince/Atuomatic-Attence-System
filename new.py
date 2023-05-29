import cv2
import face_recognition

# Load the known faces and their names
known_faces = []
known_names = []
# Add your known faces and their corresponding names to the lists

# Load the image or capture video from a webcam
image = cv2.imread("image.jpg")
# Alternatively, you can capture video from a webcam using:
# cap = cv2.VideoCapture(0)

# Convert the image to RGB format
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Detect faces in the image
face_locations = face_recognition.face_locations(rgb_image)
face_encodings = face_recognition.face_encodings(rgb_image, face_locations)

# Iterate over the detected faces
for face_encoding in face_encodings:
    # Compare the face encoding with the known faces
    matches = face_recognition.compare_faces(known_faces, face_encoding)
    name = "Unknown"

    # Check if there is a match
    if True in matches:
        match_index = matches.index(True)
        name = known_names[match_index]

    # Draw a rectangle and display the name on the image
    for (top, right, bottom, left) in face_locations:
        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(image, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# Display the image with detected faces and names
cv2.imshow("Face Detection and Matching", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
