import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('iu.jpg')

# Grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imshow('Gray Image', gray_img)
# cv2.waitKey(0)
# plt.imshow(grau_img, 'gray')
# plt.show()

# Thresholding
_, bin_thres = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
_, inv_bin_thres = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY_INV)
_, trunc_thres = cv2.threshold(gray_img, 127, 255, cv2.THRESH_TRUNC)
_, to_zero_thres = cv2.threshold(gray_img, 127, 255, cv2.THRESH_TOZERO)
_, inv_to_zero_thres = cv2.threshold(gray_img, 127, 255, cv2.THRESH_TOZERO_INV)
_, otsu_thres = cv2.threshold(gray_img, 127, 255, cv2.THRESH_OTSU)

adap_mean_thres = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 5)
adap_gaussian_thres = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 5)


# result_img = [gray_img, bin_thres, inv_bin_thres, trunc_thres, to_zero_thres, inv_to_zero_thres, adap_mean_thres, adap_gaussian_thres]
# result_title = ['GRAY', 'BINARY', 'INV BINARY', 'TRUNC', 'TO ZERO', 'INV TO ZERO', 'ADAPTIVE MEAN', 'ADAPTIVE GAUSSIAN']

# for i, (curr_img, curr_title) in enumerate(zip(result_img, result_title)):
#     plt.subplot(3, 3, (i+1))
#     plt.imshow(curr_img, 'gray')
#     plt.title(curr_title)
#     plt.xticks([])
#     plt.yticks([])
# plt.show()

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# FILTERING
# BLUR
blur_img = cv2.blur(img, (11, 11))
median_blur_img = cv2.medianBlur(img, 11)
gauss_blurr_img = cv2.GaussianBlur(img, (11, 11), 5.0)
billateral_blur_img = cv2.bilateralFilter(img, 11, 150, 150)

result_img = [img, blur_img, median_blur_img, gauss_blurr_img, billateral_blur_img ]
result_title = ['IMAGE', 'BLUR', 'MEDIAN BLUR', 'GAUSSIAN BLUR', 'BILATERAL BLUR']

# for i, (curr_img, curr_title) in enumerate(zip(result_img, result_title)):
#     plt.subplot(3, 3, (i+1))
#     plt.imshow(curr_img, 'gray')
#     plt.title(curr_title)
#     plt.xticks([])
#     plt.yticks([])
# plt.show()



# # gk pake padding
# def manual_mean_blur(img, ksize):
#     offset = ksize - 1
#     np_img = np.array(img)
#     for i in range(np_img.shape[0] - offset):
#         for j in range(np_img.shape[1] - offset):
#             arr = np.array(np_img[i:(i+ksize), j:(j+ksize)]).flatten()
#             mean = np.mean(arr)
#             np_img[i+ksize//2, j+ksize//2] = mean        
#     return np_img

# pake padding
def manual_mean_blur(img, ksize):
    offset = ksize - 1
    np_img = np.array(gray_img)
    np_img = np.pad(np_img, ksize//2)
    for i in range(np_img.shape[0] - offset):
        for j in range(np_img.shape[1] - offset):
            arr = np.array(np_img[i:(i+ksize), j:(j+ksize)]).flatten()
            mean = np.mean(arr)
            np_img[i+ksize//2, j+ksize//2] = mean 
    np_img = np_img[ksize//2:np_img.shape[0] - ksize//2, ksize//2:np_img.shape[1] - ksize//2]        
    return np_img

def manual_median_blur(img, ksize):
    offset = ksize - 1
    np_img = np.array(gray_img)
    np_img = np.pad(np_img, ksize//2)
    for i in range(np_img.shape[0] - offset):
        for j in range(np_img.shape[1] - offset):
            arr = np.array(np_img[i:(i+ksize), j:(j+ksize)]).flatten()
            median = np.median(arr)
            np_img[i+ksize//2, j+ksize//2] = median 
    np_img = np_img[ksize//2:np_img.shape[0] - ksize//2, ksize//2:np_img.shape[1] - ksize//2]        
    return np_img

manual_mean_blur_img = manual_mean_blur(img, 11)
manual_median_blur_img = manual_median_blur(img, 11)
cv2.imshow('result blur', np.hstack((manual_mean_blur_img, manual_median_blur_img)))
cv2.waitKey(0)

