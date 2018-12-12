import cv2
import numpy as np
import os

path = 'C://Users//user//Desktop//CSC//practice//prospect'

cap = cv2.VideoCapture(0)

# ПОДТЯГИВАЕМ СЛОВАРЬ МАРКЕРОВ, ИСПОЛЬЗУЕМ МАРКЕРЫ 6 на 6 из 50 штук
dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_100)
id_coordinate = dict()

while True:
    _, frame = cap.read()
    #frame = cv2.imread("test.jpg")

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # OpenCV функция для нахождения маркера из выбранного словаря
    corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(gray, dictionary)
#    print(res[0], res[1], len(res[2]))
    # ОТРИСОВЫВАЕТ
    cv2.aruco.drawDetectedMarkers(frame, corners, ids)
    cv2.imshow("Frame", frame)
    if len(corners) == 4:
        print(ids)
        for i, id in enumerate(ids):
            id_coordinate[id[0]] = corners[i][0]
        #id_coordinate[1][2][3] 1 -- отвечает за id arcuo, 2 -- отвечает за угол аруко,
        # 3 -- отвечает  за координату x или y

        #cv2.circle(frame, (id_coordinate[3][2][0], id_coordinate[3][2][1]), 5, (0, 0, 255), -1)

        pts1 = np.float32([[id_coordinate[0][0][0], id_coordinate[0][0][1]],
                           [id_coordinate[2][1][0], id_coordinate[2][1][1]],
                           [id_coordinate[1][3][0], id_coordinate[1][3][1]],
                           [id_coordinate[3][2][0], id_coordinate[3][2][1]]])
        pts2 = np.float32([[0, 0], [590, 0], [0, 840], [590, 840]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)

        result = cv2.warpPerspective(frame, matrix, (590, 840))
        cv2.imwrite(os.path.join(path, 'result_good.jpg'), result)
        #cv2.imshow("Perspective transformation", result)
        break
    # ВЫХОД С ПОМОЩЬЮ КЛАВИШИ 'q'
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    key = cv2.waitKey(1)
    if key == 27:
        break
print(id_coordinate)
cap.release()
cv2.destroyAllWindows()


