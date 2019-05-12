import csv

class Personal_csv_reader:
    @staticmethod
    def read(file_address, delim = ','):
        with open(file_address, 'r') as csv_file:
            file_data = list(csv.reader(csv_file, delimiter = delim))
            return file_data