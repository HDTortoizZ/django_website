import types
import pandas


def data_partition_generator(data: pandas.DataFrame, cols):
    """The purpose of this generator is to partition the data with respect to the columns specified by the cols
    parameter. 28/03/2022 For some reason when I initialized all the outputs with a tuple constructor, I found that I
    needed to remove an index column for the unit test.

    :param data: The data which you want to partition.
    :param cols: The columns of the data you want to partition by.
    :return: An iterable object that returns the next part of the partition of the data.
    """
    # Sort the data for easier partition.
    data = data.sort_values(by=cols)
    value_for_check_column = 1
    check_column = pandas.Series(dtype=int)
    column_values = [data[0:1][col].item() for col in cols]
    for i in range(data.shape[0]):
        next_row = data[i + 1:i + 2]
        check_column = pandas.concat([check_column, pandas.Series([value_for_check_column], dtype=int)],
                                     ignore_index=True)
        if not next_row.empty:
            next_column_values = [data[i + 1:i + 2][col].item() for col in cols]
            if column_values != next_column_values:
                value_for_check_column = value_for_check_column + 1
                column_values = next_column_values

    data['check'] = check_column

    for i in range(value_for_check_column):
        wanted_data = data.loc[data['check'] == i + 1]
        yield wanted_data.drop(['check'], axis=1).reset_index()


if __name__ == '__main__':
    data = pandas.read_csv('../../media/testing_files/test_separator_generator.csv')
    separated_data = data_splitting_generator(data, ['col1', 'col2'])
    print(next(separated_data))
    print(next(separated_data))
    print(next(separated_data))
    print(next(separated_data))
    print(next(separated_data))


