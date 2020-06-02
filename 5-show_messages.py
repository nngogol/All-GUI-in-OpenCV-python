# made at 2020-06-02 15:16:45
# by nngogol

import numpy as np, cv2 as cv; cv2=cv

#
# press Q, E, A, R, 1, 2, 3, 4
#

# Name your window
root_wind = 'main';
cv.namedWindow(root_wind)

ms_delay=1500
mbox_up = lambda text: cv.displayOverlay(root_wind, text, ms_delay)
mbox_bottom = lambda text: cv.displayStatusBar(root_wind, text, ms_delay)

# Create a black image
img = np.ones((512,512,3), np.uint8)
while True:
	
	cv.imshow(root_wind, img)
	
	# keyboard events
	code = cv.waitKey(1)

	if code == ord('q'): break
	if code == ord('a'): mbox_up('hello')
	
	# change colors:
	if code == ord('e'):
		mbox_up('empty')
		img.fill(30)
	
	if code == ord('1'): img.fill(60)
	if code == ord('2'): img.fill(90)
	if code == ord('3'): img.fill(120)
	if code == ord('4'): img.fill(150)
	
	if code == ord('r'):
		mbox_bottom('filled')
		img.fill(255)

cv.destroyAllWindows()


