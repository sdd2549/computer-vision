import cv2 as cv
import numpy as np

# Read the given image as gray scale
img = cv.imread('./data/mandril_color.tif', cv.IMREAD_GRAYSCALE)

if img is not None:
    # Configure the intensity control
    contrast = 1.6
    contrast_step = 0.1
    brightness = -40
    brightness_step = 1

    while True:
        # Apply contrast and brightness
        img_tran = contrast * img + brightness # Alternative) cv.equalizeHist(), cv.intensity_transform
        img_tran[img_tran < 0] = 0
        img_tran[img_tran > 255] = 255         # Saturate values
        img_tran = img_tran.astype(np.uint8)

        # Show all images
        info = f'Contrast: {contrast:.1f}, Brightness: {brightness:.0f}'
        cv.putText(img_tran, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, 255, thickness=2)
        cv.putText(img_tran, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, 0)
        merge = np.hstack((img, img_tran))
        cv.imshow('Image Intensity Control: Original | Contrast/Brightness', merge)

        # Process the key event
        key = cv.waitKey(10)
        if key == 27: # ESC
            break
        elif key == ord('+') or key == ord('='):
            contrast += contrast_step
        elif key == ord('-') or key == ord('_'):
            contrast -= contrast_step
        elif key == ord(']') or key == ord('}'):
            brightness += brightness_step
        elif key == ord('[') or key == ord('{'):
            brightness -= brightness_step

    cv.destroyAllWindows()