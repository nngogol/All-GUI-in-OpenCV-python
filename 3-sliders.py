# made at 2020-06-02 15:16:45
# by nngogol

import numpy as np, cv2 as cv; cv2=cv

# 
# press Q, W, E
# 

def make_slid(a_min:int, a_max:int, curr:int, slider_id:str, root_win_name:str, on_change_callback=lambda x: x):
	cv2.createTrackbar(slider_id, root_win_name, a_min, a_max, on_change_callback)
	cv2.setTrackbarPos(slider_id, root_win_name, curr)
	return slider_id
def getslid(*ids, root_wind:str):
	try:
		results = [cv2.getTrackbarPos(idd, root_wind) for idd in ids]
		return results[0] if len(results) == 1 else results
	except Exception as e:
		print(f'Error in getting slider value - {str(e)}')
		return None
def setslid(id_:str, value:int, root_wind:str):
	cv2.setTrackbarPos(id_, root_wind, value)


# Name your window
root_wind = 'main';
cv.namedWindow(root_wind)

sliders = [
	make_slid(0, 255, 20,  'r', root_wind),
	make_slid(0, 255, 50,  'g', root_wind),
	make_slid(0, 255, 120, 'b', root_wind)
]

# Create a black image
img = np.ones((512,512,3), np.uint8)
while True:
	
	img[:, :] = getslid('r', 'g', 'b', root_wind=root_wind)
	cv.imshow(root_wind, img)
	
	code = cv.waitKey(1)

	if code == ord('q'):
		break
	
	if code == ord('w'):
		r, g, b = getslid('r', 'g', 'b', root_wind=root_wind)
		print(r, g, b)
	
	if code == ord('e'):
		setslid('r', 10, root_wind=root_wind)
		setslid('g', 10, root_wind=root_wind)
		setslid('b', 10, root_wind=root_wind)


cv.destroyAllWindows()