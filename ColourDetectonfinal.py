import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # getting center of screen
    height, width, _ = frame.shape
    cx = int(width / 2)
    cy = int(height / 2)

    # pick pixel value
    pixel_center = hsv_frame[cy, cx]

    # define color range from hues & saturations
    hue_value = pixel_center[0]
    sat_value = pixel_center[1]
    val_value = pixel_center[2]
    colour = "Undefined"
    if (
        hue_value < 85
        and (sat_value > 10 and sat_value < 100)
        and (val_value > 75 and val_value < 190)
    ):
        colour = "Green"
    if (
        (hue_value > 90 and hue_value < 130)
        and (sat_value > 50 and sat_value < 255)
        and (val_value > 50 and val_value < 255)
    ):
        colour = "Blue"
    if (
        (hue_value < 5)
        and (sat_value > 100 and sat_value < 140)
        and (val_value > 110 and val_value < 255)
    ):
        colour = "Red"
    if (
        (hue_value > 12 and hue_value <= 70)
        and (sat_value > 140 and sat_value <= 200)
        and (val_value > 80 and val_value <= 250)
    ):
        colour = "Yellow"
    if (
        hue_value < 33
        and (sat_value > 43 and sat_value < 100)
        and (val_value > 50 and val_value < 250)
    ):
        colour = "Brown"
    if (
        hue_value < 22
        and (sat_value > 100 and sat_value < 180)
        and (val_value > 100 and val_value < 270)
    ):
        colour = "Orange"
    if (
        hue_value == 0
        and (sat_value >= 0 and sat_value < 30)
        and (val_value >= 0 and val_value < 70)
    ):
        colour = "Black"

    if (
        hue_value >= 0
        and hue_value < 164
        and (sat_value >= 0 and sat_value < 20)
        and (val_value > 80 and val_value < 255)
    ):
        colour = "Gray"

    print(pixel_center)
    cv2.putText(frame, colour, (10, 50), 0, 1, (255, 0, 0), 2)
    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)

    cv2.imshow("Colour Detection", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
