
def load():
    define_database_schema()
    data_file = genernate_data()
    load_data(data_file)


def define_database_schema():
    """create database table

    Args:

    Returns:

    """

    pass


def genernate_data():
    """Randomly generate a set of test data

    Args:

    Returns:
        full path of the generated data file.
    """

    pass


def load_data(data_file):
    """Load generated data into database table

    Args:
        data_file: the full path of input data file

    Returns:

    """

    pass


if __name__ == '__main__':
    load()