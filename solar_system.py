import cv2



img=cv2.imread("solar-system.jpg")
print(img)
img = cv2.putText(img,"Sun",(0,215),cv2.FONT_HERSHEY_COMPLEX,1.6,(255,255,255))

img = cv2.putText(img,"Mercury",(110,270),cv2.FONT_HERSHEY_PLAIN,0.9,(255,255,255))

img = cv2.putText(img,"Venus",(195,170),cv2.FONT_HERSHEY_PLAIN,0.9,(255,255,255))

img = cv2.putText(img,"Earth",(290,270),cv2.FONT_HERSHEY_PLAIN,0.9,(255,255,255))

img = cv2.putText(img,"Mars",(390,170),cv2.FONT_HERSHEY_PLAIN,0.9,(255,255,255))

img = cv2.putText(img,"Jupiter",(550,380),cv2.FONT_HERSHEY_PLAIN,1.1,(255,255,255))

img = cv2.putText(img,"Saturn",(810,120),cv2.FONT_HERSHEY_PLAIN,1,(255,255,255))

img = cv2.putText(img,"Neptune",(965,310),cv2.FONT_HERSHEY_PLAIN,0.9,(255,255,255))

img = cv2.putText(img,"Uranus",(1125,130),cv2.FONT_HERSHEY_PLAIN,0.9,(255,255,255))

   

cv2.imshow("output window",img)
cv2.waitKey(0)
