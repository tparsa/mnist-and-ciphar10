from rgb_image import Rgb_image as image
import numpy as np
import csv
from skimage.transform import rotate

class Images_Container:

    def __init__(self, data_file_address, label_file_address, image_size):
        self.images = []
        with open(data_file_address, 'r') as csv_data_file:
            csv_label_file = open(label_file_address, 'r')
            data_file_reader = csv.reader(csv_data_file, delimiter=',')
            label_file_reader = list(csv.reader(csv_label_file, delimiter=','))
            for i, row in enumerate(data_file_reader):
                cur_row = list(row)

                pixels = [[] for i in range(image_size)]
                pixel_index = 0
                cur_pixel = [0, 0, 0]
                for data_index in range(len(cur_row)):
                    cur_pixel[data_index % 3] = int(cur_row[data_index]) / 255
                    if(data_index % 3 == 2):
                        pixels[pixel_index // image_size].append(tuple(cur_pixel))
                        pixel_index += 1
                self.images.append(image(28, np.array(pixels, dtype='float'), str(label_file_reader[i][0] if i < len(label_file_reader) else "")))

    def complete_train_data(self):
        new_images = []
        for img in self.images:
            for i in range(-90, 91, 10):
                if(i != 0):
                    new_images.append(image(img.size, rotate(img.data, i) , img.label))
        self.images = self.images + new_images

    def accept(self,visitor):
        for i, img in enumerate(self.images):
            if(i % 2000 == 0):
                print(i)
            visitor.visit(img)

    def show(self, index):
        self.images[index].show()
