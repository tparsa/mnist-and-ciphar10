import numpy as np

class Negative :
    @staticmethod
    def visit(image):
        new_data = []
        for i in range(len(image.data)):
            new_data_row = []
            for j in range(len(image.data[i])):
                new_pixel = [0, 0, 0]
                for k in range(3):
                    new_pixel[k] = 1-image.data[i][j][k]
                new_data_row.append(tuple(new_pixel))
            new_data.append(new_data_row)
        image.data = np.array(new_data)
