import cv2
import numpy as np
from PIL import Image, ImageDraw

def save_patology_mask(fn):
    hsv_min = np.array((0, 0, 0), np.uint8)
    hsv_max_patology = np.array((255, 255, 158), np.uint8)
    img = cv2.imread(fn)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
    thresh = cv2.inRange(hsv, hsv_min, hsv_max_patology)
    cv2.imwrite("patology_mask.jpg",thresh)

def save_bone_mask(fn):
    hsv_min = np.array((0, 0, 0), np.uint8)
    hsv_max_bone = np.array((255, 255, 250), np.uint8)
    img = cv2.imread(fn)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
    thresh = cv2.inRange(hsv, hsv_min, hsv_max_bone)
    cv2.imwrite("bone_mask.jpg",thresh)

def draw_patology(fn):
    save_bone_mask(fn)
    save_patology_mask(fn)

    image = Image.open(fn)  # Открываем изображение
    image_patology = Image.open("patology_mask.jpg")
    image_bone = Image.open("bone_mask.jpg")
    draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования
    width = image.size[0]  # Определяем ширину
    height = image.size[1]  # Определяем высоту

    pix_patology = image_patology.load()
    pix_bone = image_bone.load()

    for x in range(width):
        for y in range(height):
            patology_index, bone_index = pix_patology[x, y], pix_bone[x, y]
            if patology_index==0 and bone_index>0:
                draw.point((x, y), (255, 192, 0)) #рисуем пиксель

    image.save(fn[:-4]+"_result.jpg", "JPEG")


# for fn in glob.glob("draw_test/*"):
#     draw_patology(fn)
