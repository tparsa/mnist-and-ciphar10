import csv

class Mnist_data_beautifier:
    @staticmethod
    def beautify (input_file_address, output_file_address):
        with open(output_file_address, 'w', newline='') as csv_output_file:
            csv_input_file = open(input_file_address, 'r')
            input_data = list(csv.reader(csv_input_file, delimiter=','))
            output_writer = csv.writer(csv_output_file)
            for row in input_data:
                output_data = []
                for x in row:
                    output_data.append(x)
                    output_data.append(x)
                    output_data.append(x)
                output_writer.writerow(output_data)

Mnist_data_beautifier.beautify('dataset/MNIST/train_data.csv', 'dataset/MNIST/train_data_beautify.csv')