import sys
from pathlib import Path
import os
sys.path.append(os.path.join(Path(__file__).resolve().parent.parent.parent))
import pandas
from libraries.data_separator.data_splitting_generator import data_partition_generator


class DataPartitioner:
    """
    This class should partition the data given based on the columns chosen. This will be useful in a web application
    should we want to display each partition on pages dependent on the selection the user provides.
    """
    def __init__(self, filename, partition_columns, data):
        """Initialize the class attributes.

        :param filename: The name of the file that the data was read from.
        :param partition_columns: The columns that the user wants to partition the data by.
        :param data: The data to partition.
        """
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
        """Retrieve the partition corresponding to the column values passed.

        :param column_values: The column values for the partition required.
        :return: The partition corresponding to the column values passed.
        """
        for partition in self._partitioned_data:
            if partition.column_values == column_values:
                return partition.partition_of_data
        raise KeyError(f"Data Partitioned with {column_values} not found in this instance of DataPartitioner.")

    def partition_data(self):
        """Partition the data stored in the class by the column names passed to the constructor using an instance of the
        data_partition_generator.

        :return: A list of DataPartition objects.
        """
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
    """
    This class will store a singular partition so it is easier to find within the DataPartitioner class.
    """
    def __init__(self, columns, column_values, partition_of_data):
        """Initialize the DataPartitioner.

        :param columns: The columns that the data was partitioned by.
        :param column_values: The values of the partition columns for this partition of data.
        :param partition_of_data: The partition of data based with the column values.
        """
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
