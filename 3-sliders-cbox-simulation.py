# made at 2020-06-02 15:16:45
# by nngogol
import numpy as np, cv2 as cv
cv2=cv

def make_cbox(state:bool, radio_id:str, root_win_name:str, on_change_callback=lambda x: x):
	cv2.createTrackbar(radio_id, root_win_name, 0, 1, on_change_callback); cv2.setTrackbarPos(radio_id, root_win_name, 1 if state else 0)
def getcbox(*ids, root_wind:str):
	try:
		results = [cv2.getTrackbarPos(idd, root_wind) == 1 for idd in ids]
		return results[0] if len(results) == 1 else results
	except Exception as e:
		print(f'Error in getting cbox value - {str(e)}')
def setcbox(id_:str, state:bool, root_wind:str):
	cv2.setTrackbarPos(id_, root_wind, 1 if state else 0)

# Name your window
root_wind = 'main';
cv.namedWindow(root_wind)

cboxes = [
	make_cbox(True,  'draw face', root_wind),
	make_cbox(False, 'draw legs', root_wind),
	make_cbox(False, 'draw hands', root_wind)
]


# Create a black image
img = np.ones((700,400,3), np.uint8)
while True:
	
	cv.imshow(root_wind, img)
	
	code = cv.waitKey(1)

	
	if code == ord('q'):
		break
	
	if code == ord('w'):
		draw_face, draw_legs, draw_hands = getcbox('draw face', 'draw legs', 'draw hands', root_wind=root_wind)

		# clear
		img.fill(0)

		# body
		cv.rectangle(img,  (-300+408,  159),  (-300+408+194,  159+320),  (33,33,133), 3, 1)

		if draw_face:
			# face
			cv.rectangle(img,  (-300+408,   14),  (-300+408+194,  14+142),  (33,133,33), 3, 1)

		if draw_hands:
			# hands
			cv.rectangle(img,  (-300+354,  159),  ( -300+354+51,  159+222),  (133,33,33), 3, 1)
			cv.rectangle(img,  (-300+605,  159),  ( -300+605+54,  159+211),  (133,33,33), 3, 1)
			
		if draw_legs:
			# legs
			cv.rectangle(img,  (-300+408,  482),  ( -300+408+51,  482+125),  (255,33,33), 3, 1)
			cv.rectangle(img,  (-300+551,  482),  ( -300+551+51,  482+125),  (255,33,33), 3, 1)


	
cv.destroyAllWindows()