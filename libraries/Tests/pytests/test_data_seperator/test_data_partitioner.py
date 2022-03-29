# test data partitioner
import os
import pandas

from libraries.Tests.test_settings import base_dir
from libraries.data_separator.data_partitioner import DataPartitioner

data = pandas.read_csv(os.path.join(base_dir, 'media/testing_files/test_separator_generator.csv'))
data_partitioner = DataPartitioner('test_separator_generator.csv', ['col1', 'col2'], data)


def test_number_of_partitions():
    """Test that the number of partitions made fo the test_separator_generator data is 8 (found by looking at the file).

    :return: None
    """
    assert len(data_partitioner._partitioned_data) == 8


def test_length_of_partitions():
    """Test that the lengths of the partitions for the data are what we should expect them to be.

    :return: None
    """
    lengths_correct = True
    actual_lengths = [2, 2, 7, 3, 2, 1, 4, 5]
    for i in range(8):
        ith_partition = data_partitioner._partitioned_data[i]
        rows = ith_partition.partition_of_data.shape[0]
        if rows != actual_lengths[i]:
            lengths_correct = False
            break
    assert lengths_correct


def test_different_combinations_found_correctly():
    """Test that the combinations the we expect to come up based on the data can actually be found.

    :return: None
    """
    no_key_error = True
    expected_combinations = [[1, 1], [1, 2], [2, 1], [2, 2], [3, 1], [3, 2], [3, 3], [4, 1]]
    for comb in expected_combinations:
        try:
            data_partitioner.get_partition(comb)
        except KeyError:
            no_key_error = False
            break
    assert no_key_error


def test_key_error_raised():
    """Test that when a combination that doesn't exist is searched for, a key error is raised.

    :return: None
    """
    key_error_raised = False
    try:
        data_partitioner.get_partition([5, 1])
    except KeyError:
        key_error_raised = True
    assert key_error_raised
