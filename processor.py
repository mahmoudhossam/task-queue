import csv
from tasks import task


class Processor:
    def __init__(self, filename):
        with open(filename) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                name, email = row
                message = {"name": name, "email": email}
                task.delay(message)


if __name__ == "__main__":
    processor = Processor("data_example.csv")
