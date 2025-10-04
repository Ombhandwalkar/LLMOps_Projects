from io import BytesIO # Creates a memory buffer to store the binary file.
import numpy as np
import cv2


def process_image(image_file):
    # Create memory buffer to store binary file
    in_memory_file= BytesIO()
    image_file.save(in_memory_file)

    # Getting raw values of Binary file
    image_byte= in_memory_file.getvalue()
    # Converting raw values into ND-Array
    nparr= np.frombuffer(image_byte, np.int8)

    # Decode ND-Arry into OpenCV image
    img= cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Converts image to GRAYSCALE,it works better on grayscale iamges.
    gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Load pre-trained Haar-Cascade-Classifier for detecting faces.
    face_cascade= cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Detect faces
    faces= face_cascade.detectMultiScale(gray, 1.1, 5)

    if len(faces) ==0:
        return image_bytes, None

    # If multiple faces found, pick largest one.
    largest_face= max(faces, key=lambda r:r[2]*r[3])
    (x, y, w, h) = largest_face

    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0),3)
    is_sucess, buffer= cv2.imencode(".jpg",img)

    return buffer.tobytes(), largest_face
