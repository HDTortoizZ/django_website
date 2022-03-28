"""The code in this module is simply to test the speed of two different methods for the partitioning of datasets."""
from datetime import datetime
import os
import pandas
from test_settings import base_dir
from libraries.data_separator.data_splitting_generator import data_partition_generator


def speed_test():
    """Test the speeds of the generator for the partitions against a method for trying the loc function using all the
    different combinations of Show Number and Value in the Jeopardy dataset. Which I got from this website:
    https://domohelp.domo.com/hc/en-us/articles/360043931814-Fun-Sample-DataSets, the file is too large for me to
    reasonably upload to GitHub (216930 rows and 7 columns).

    :return: None
    """
    test_data = pandas.read_csv(os.path.join(base_dir, 'media/testing_files/JEOPARDY_CSV.csv'))

    loc_start = datetime.now()
    loc_test_sorted = test_data.sort_values(by=['Show Number', ' Value'])
    first_column_set = sorted(set(test_data['Show Number'].tolist()))
    second_column_set = sorted(set(test_data[' Value'].tolist()))
    combinations = list()
    for show in first_column_set:
        for val in second_column_set:
            combinations.append((show, val))
    loc_partition = [loc_test_sorted.loc[(loc_test_sorted['Show Number'] == show) &
                                         (loc_test_sorted[' Value'] == val)] for show, val in combinations]
    # Time reported on my local machine is 1:13:42, way too long, although could probably be more efficient if we took
    # the set of the second column within the DataFrame provided by
    # sorted(set(.loc[data[first_col] == first_vals][second_col].tolist())
    print(f'Time taken with regular loc function: {datetime.now() - loc_start}')

    generator_start = datetime.now()
    partition_gen = data_partition_generator(test_data, ['Show Number', ' Value'])
    gen_partition = list(partition_gen)

    # Time reported on my local machine is 0:02:01, safe to say it's more efficient and also doesn't list empty
    # DataFrames.
    print(f'Time taken with generator function: {datetime.now() - generator_start}')


if __name__ == '__main__':
    speed_test()
