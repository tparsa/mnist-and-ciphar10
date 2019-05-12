import numpy as np

class Smoother:
    @staticmethod
    def inRange(i, j, k, l, height, width):
        return( 0 <= i + k and i + k < height and 0 <= j + l and j + l < width)

    @staticmethod
    def visit(image):
        new_data = []
        for i in range(len(image.data)):
            new_data_row = []
            for j in range(len(image.data[i])):
                new_pixel = [0, 0, 0]
                cnt = 0
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        for idx in range(3):
                            new_pixel[idx] += (0 if not Smoother.inRange(i, j, k, l, len(image.data), len(image.data[0])) else image.data[i+k][j+l][idx])
                            cnt += 1
                for idx in range(3):
                    new_pixel[idx] /= cnt
                new_data_row.append(tuple(new_pixel))
            new_data.append(new_data_row)
        image.data = np.array(new_data)

