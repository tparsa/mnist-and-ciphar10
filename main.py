from classifiers import Mnist_Classifier as mc
from images import Images_Container
from mnist_data_beautifier import Mnist_data_beautifier as mdb
from personal_csv_reader import Personal_csv_reader
import visitor.smoother as smooth
from skimage.transform import rotate
import matplotlib.pyplot as plt
import visitor.negative as negative

def __main__ ():
    mdb.beautify('dataset/MNIST/test_data.csv', 'dataset/MNIST/test_data_beautify.csv')
    train_image_container = Images_Container('dataset/MNIST/train_data_beautify.csv', 'dataset/MNIST/train_label.csv', 28)
    test_image_container = Images_Container('dataset/MNIST/test_data_beautify.csv', 'dataset/MNIST/test_label.csv', 28)
    test_real_labels = Personal_csv_reader.read('dataset/MNIST/test_label.csv')
    accuracy = {}
    train_image_container.accept(negative.Negative)
    test_image_container.accept(negative.Negative)
    #train_image_container.complete_train_data()
    train_image_container.accept(smooth.Smoother)
    test_image_container.accept(smooth.Smoother)
    for i in range(5, 8):
        for weight in ['uniform', 'distance']:
            accuracy[(i, weight)] = mc.K_nearest_neighbors_test(train_image_container, test_image_container, test_real_labels, i, weight)
    print(accuracy)

__main__()
