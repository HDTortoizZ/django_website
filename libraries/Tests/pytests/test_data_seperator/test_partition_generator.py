# test partition generator
import os
import pandas
from libraries.Tests.test_settings import base_dir
from libraries.data_separator.data_splitting_generator import data_partition_generator


def test_partition_generator():
    """Test that data is actually partitioned correctly. The indices used in the actual_partition_list have been found
    directly by reading the test data file.

    :return: Assertion that the function works correctly.
    """
    data = pandas.read_csv(os.path.join(base_dir, 'media/testing_files/test_separator_generator.csv'))
    # Initialize the generator for partitions.
    partition_gen = data_partition_generator(data, ['col1', 'col2'])
    # Initialize the actual partitions that should be made. Indices found directly by looking at the test file.
    actual_partition_list = (data[0:2], data[2:4], data[4:11], data[11:14],
                             data[14:16], data[16:17], data[17:21], data[21:])
    # Initialize the values given by the generator by calling the tuple constructor on it.
    test_partition_list = tuple(partition_gen)
    # For some strange reason, there was an index column that needed removing here.
    test_partition_list = [item.drop(['index'], axis=1) for item in test_partition_list]

    equal_elements = (df1.equals(df2) for df1, df2 in zip(actual_partition_list, test_partition_list))
    list(equal_elements)

    assert all(equal_elements)


