import cv2
import os
import string
import platform  # Import platform module

# Load the image
img = cv2.imread("mypic.jpg")  # Replace with the correct image path
if img is None:
    print("Error: Image not found.")
    exit()

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

m = 0
n = 0
z = 0

for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

cv2.imwrite("encryptedImage.jpg", img)

# Open the encrypted image based on the operating system
if platform.system() == "Windows":
    os.system("start encryptedImage.jpg")
elif platform.system() == "Darwin":  # macOS
    os.system("open encryptedImage.jpg")
else:  # Linux
    os.system("xdg-open encryptedImage.jpg")

message = ""
n = 0
m = 0
z = 0

pas = input("Enter passcode for Decryption: ")
if password == pas:
    for i in range(len(msg)):
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("Decrypted message:", message)
else:
    print("YOU ARE NOT authorized")