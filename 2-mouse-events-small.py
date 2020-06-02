# made at 2020-06-02 15:16:45
# by nngogol

import numpy as np, cv2 as cv; cv2=cv

# Name your window
root_wind = 'main';
cv.namedWindow(root_wind)

def on_mouse_event(event, x, y, flags, param):
    if event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
        print('click L, ' + str([x, y]))
        cv.circle(img,(x,y),12,(0,0,255),1)

    # Lclick hold n drag  + shift
    if event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON | cv.EVENT_FLAG_SHIFTKEY:
        print('click L, ' + str([x, y]))
        cv.circle(img,(x-10,y+10),25,(155,0,0),1)
        cv.circle(img,(x+10,y-10),25,(155,0,0),1)
        cv.circle(img,(x-10,y-10),25,(155,0,0),1)
        cv.circle(img,(x+10,y+10),25,(155,0,0),1)
    
    # shift is pressed
    if flags == cv.EVENT_FLAG_SHIFTKEY:
        cv.circle(img,(x,y),150,(155,0,0),1)
    
    # Mclick
    if event == cv.EVENT_MBUTTONUP:
        print('click M, ' + str([x, y]))

        a_line_height = 5
        a_color = (255, 0, 140)
        cv.rectangle(img, (x-20,y-20), (x+20,y+20), a_color, a_line_height)

cv.setMouseCallback(root_wind, on_mouse_event)


# Create a black image
img = np.ones((512,512,3), np.uint8)
while True:
    
    cv.imshow(root_wind, img)
    
    code = cv.waitKey(1)

    if code == ord('q'):
        break


cv.destroyAllWindows()