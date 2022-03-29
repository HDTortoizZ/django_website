import sys
from pathlib import Path
import os
sys.path.append(os.path.join(Path(__file__).resolve().parent.parent.parent))
import pandas
from libraries.data_separator.data_splitting_generator import data_partition_generator


class DataPartitioner:
    def __init__(self, filename, partition_columns, data):
        if type(filename) == str:
            self._filename = filename
        else:
            raise TypeError("filename parameter must be a str")
        try:
            partition_columns[0]
        except TypeError:
            raise TypeError("partitions_columns parameter is not subscriptable")
        self._partitions_columns = partition_columns
        if type(data) != pandas.DataFrame:
            raise TypeError("data parameter is not a pandas.DataFrame")
        self._data = data
        self._partitioned_data = self.partition_data()

    @property
    def filename(self):
        return self._filename

    @property
    def partition_columns(self):
        return self._partitions_columns

    @property
    def data(self):
        return self._data

    def get_partition(self, column_values):
        for partition in self._partitioned_data:
            if partition.column_values == column_values:
                return partition.partition_of_data
        raise KeyError(f"Data Partitioned with {column_values} not found in this instance of DataPartitioner.")

    def partition_data(self):
        data = self.data
        columns = self.partition_columns
        partition_generator = data_partition_generator(data, columns)
        partitions_list = list()
        while True:
            try:
                current_partition = next(partition_generator)
                current_partition = current_partition.drop(['index'], axis=1)
                column_values = [current_partition[col][0].item() for col in columns]
                partitions_list.append(DataPartition(columns, column_values, current_partition))
            except StopIteration:
                break
        return partitions_list


class DataPartition:
    def __init__(self, columns, column_values, partition_of_data):
        self._columns = columns
        self._column_values = column_values
        self._partition_of_data = partition_of_data

    @property
    def columns(self):
        return self._columns

    @property
    def column_values(self):
        return self._column_values

    @property
    def partition_of_data(self):
        return self._partition_of_data


if __name__ == '__main__':
    df = pandas.read_csv(os.path.join(Path(__file__).resolve().parent.parent.parent,
                                      'media/testing_files/test_separator_generator.csv'))
    data_partitioner = DataPartitioner('test_separator_generator.csv', ['col1', 'col2'], df)
    print(data_partitioner.get_partition([3, 4]))

