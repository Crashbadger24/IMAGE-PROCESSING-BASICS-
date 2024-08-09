import numpy as np
import matplotlib.pyplot as plt
import cv2 

def denoise_image(image_path):
    noisy_image = cv2.imread(image_path)
    noisy_image_rgb = cv2.cvtColor(noisy_image, cv2.COLOR_BGR2RGB)
    
    gaussian_denoised = cv2.GaussianBlur(noisy_image, ksize=(5,5), sigmaX=5)
    gaussian_denoised_rgb = cv2.cvtColor(gaussian_denoised, cv2.COLOR_BGR2RGB)
    
    median_denoised = cv2.medianBlur(noisy_image_rgb, ksize=5)
    median_denoised_rgb = cv2.cvtColor(median_denoised, cv2.COLOR_BGR2RGB)
    
    bilateral_denoised = cv2.bilateralFilter(noisy_image, d=6, sigmaColor=175, sigmaSpace=175)
    bilateral_denoised_rgb = cv2.cvtColor(bilateral_denoised, cv2.COLOR_BGR2RGB)
    
    plt.figure(figsize=(15, 15))
    plt.subplot(2, 2, 1)
    plt.title('Noisy Image')
    plt.imshow(noisy_image_rgb)
    plt.axis('off')
    
    plt.subplot(2, 2, 2)
    plt.title('Gaussian Denoised')
    plt.imshow(gaussian_denoised_rgb)
    plt.axis('off')
    
    plt.subplot(2, 2, 3)
    plt.title('Median Blur')
    plt.imshow(median_denoised_rgb)
    plt.axis('off')
    
    plt.subplot(2, 2, 4)
    plt.title('Bilateral Denoised')
    plt.imshow(bilateral_denoised_rgb)
    plt.axis('off')
    
    plt.show()

denoise_image(r"D:\python\Learning_ML\Imageprocessing\Noise_cancellation\noisy_image2.jpg")
