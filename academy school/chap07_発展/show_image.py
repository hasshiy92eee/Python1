import cv2

img = cv2.imread('block.jpg')
height = img.shape[0]
width = img.shape[1]
resized_img = cv2.resize(img, (int(width/2), int(height/2)))
gray_img = cv2.cvtColor(resized_img, cv2.COLOR_RGBA2GRAY)
canny_img = cv2.Canny(gray_img, 50, 100)

cv2.imwrite('canny.jpg', canny_img)
cv2.imshow('canny_img', canny_img)
cv2.waitKey(0) # 'qで抜けれる'
cv2.destroyAllWindows()
