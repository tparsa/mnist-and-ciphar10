from sklearn.neighbors import KNeighborsClassifier
import numpy as np

class Mnist_Classifier:
    @staticmethod
    def K_nearest_neighbors_test(train_images_container, test_images_container, test_real_labels, n_neighbors, weight, alg='auto'):
        X = []
        Y = []
        for img in train_images_container.images:
            x = []
            for row in img.data:
                for tup in row:
                    for d in tup:
                        x.append(d)
            X.append(x)
            Y.append(img.label)
        neigh = KNeighborsClassifier(n_neighbors=n_neighbors, algorithm=alg, weights=weight)
        neigh.fit(X, Y)
        test_predicted_labels = []
        print(len(test_images_container.images))
        for img in test_images_container.images:
            x = []
            for row in img.data:
                for tup in row:
                    for d in tup:
                        x.append(d)
            test_predicted_labels.append(neigh.predict([x]))

        correct_predictions_cnt = 0
        for i, label in enumerate(test_predicted_labels):
            if(label[0] == test_real_labels[i][0]):
                correct_predictions_cnt += 1
            else:
                print(label, test_real_labels[i])
        return correct_predictions_cnt / len(test_predicted_labels)