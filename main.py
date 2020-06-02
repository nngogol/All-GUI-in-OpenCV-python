import numpy as np, cv2 as cv; cv2=cv

# Name your window
root_wind = 'main';
cv.namedWindow(root_wind)

# Create a black image
img = np.ones((512,512,3), np.uint8)
while True:
	
	cv.imshow(root_wind, img)
	
	# keyboard events
	code = cv.waitKey(1)

	if code == ord('q'): break
	
	# change colors:
	if code == ord('e'):
		print('empty')
		img.fill(0)
	
	if code == ord('1'): img.fill(30)
	if code == ord('2'): img.fill(60)
	if code == ord('3'): img.fill(90)
	if code == ord('4'): img.fill(120)
	if code == ord('5'): img[:, :] = 23,45,78
	if code == ord('6'): img[:, :] = 27,34,41
	
	if code == ord('r'):
		print('filled')
		img.fill(255)

cv.destroyAllWindows()