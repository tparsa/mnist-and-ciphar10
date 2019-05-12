import matplotlib.pyplot as plt

class Rgb_image:
    def __init__(self, size, rgb_data, label):
        self.size = size
        self.data = rgb_data
        self.label = label

    def show(self):
        plt.figure()
        plt.imshow(self.data)
        plt.xlabel(self.label)
        plt.show()
