import cv2
img=cv2.imread("solar-system.jpg")
cv2.imshow("display image",img)
cv2.putText(img,
            "Sun",
            (100,80),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            1,
            (255,255,0),)
cv2.imshow("output",img)
cv2.imwrite("solar_systemwithname.jpg",img)

cv2.waitKey(0)