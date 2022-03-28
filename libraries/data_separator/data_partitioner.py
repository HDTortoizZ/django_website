import pandas
from .data_splitting_generator import data_partition_generator

class DataPartitioner:
    def __init__(self, filename, partition_columns, data):
        if type(filename) == str:
            self._filename = filename
        else:
            raise TypeError("filename parameter must be a str")
        try:
            next(partition_columns)
        except TypeError:
            raise TypeError("partitions_columns parameter is not iterable")
        except StopIteration:
            raise ValueError("partitions_columns parameter is empty")
        self._partitions_columns = partition_columns
        if type(data) != pandas.DataFrame:
            raise TypeError("data parameter is not a pandas.DataFrame")
        self._data = data

    @property
    def filename(self):
        return self._filename

    @property
    def partition_columns(self):
        return self._partitions_columns

    @property
    def data(self):
        return self._data



