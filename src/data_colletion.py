from selenium import webdriver
from time import sleep
from PIL import Image
from io import BytesIO

# path = "C:\\geckodriver-v0.30.0-win64\\geckodriver.exe"

driver = webdriver.Firefox()
driver.get('https://bhuvanlite.nrsc.gov.in/?x=78.0425123&y=27.1747201&z=25')
sleep(3)

# driver.get_screenshot_as_file("TajMahal1.jpeg")
png = driver.get_screenshot_as_png()
driver.quit()
print("end...")
im = Image.open(BytesIO(png))
width, height = im.size
# print(f"height = {height}")

left = 150
top = 75
right = 1200
bottom = 800
im1 = im.crop((left, top, right, bottom)) # defines crop points
im1.save('TajMahal.png') # saves new cropped image
im1.show()

left = 260
top = 90
right = 1545
bottom = 1080
im1 = im.crop((left, top, right, bottom)) # defines crop points
im1.save('TajMahalLT.png')
# im1.show()

left = 300
top = 90
right = 1545
bottom = 700
im1 = im.crop((left, top, right, bottom)) # defines crop points
im1.save('TajMahalLB.png')
# im1.show()

left = 55
top = 170
right = 1100
bottom = 1080
im1 = im.crop((left, top, right, bottom)) # defines crop points
im1.save('TajMahalRT.png')
# im1.show()

left = 50
top = 100
right = 1100
bottom = 600
im1 = im.crop((left, top, right, bottom)) # defines crop points
im1.save('TajMahalRB.png')
im1.show()
