
class CsvReader:
    counter = 0

    def __init__(self, reader):
        self.reader = reader
        # The headers most match the column names in the database
        self.headers = next(self.reader)

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        return self.counter, {k:y for k, y in zip(self.headers, next(self.reader))}
