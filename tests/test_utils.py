import index_calculator._utils as utils


def test_normalize_pandas_freq_year_aliases():
    assert utils.normalize_pandas_freq("AS") == "YS"
    assert utils.normalize_pandas_freq("AS-JAN") == "YS-JAN"
    assert utils.normalize_pandas_freq("A") == "YE"
    assert utils.normalize_pandas_freq("A-DEC") == "YE-DEC"
    assert utils.normalize_pandas_freq("5AS") == "5YS"
    assert utils.normalize_pandas_freq("5AS-JUL") == "5YS-JUL"
    assert utils.normalize_pandas_freq("5A") == "5YE"
    assert utils.normalize_pandas_freq("10A-DEC") == "10YE-DEC"


def test_normalize_pandas_freq_quarter_aliases():
    assert utils.normalize_pandas_freq("Q") == "QE"
    assert utils.normalize_pandas_freq("Q-FEB") == "QE-FEB"
    assert utils.normalize_pandas_freq("2Q-FEB") == "2QE-FEB"
    assert utils.normalize_pandas_freq("BQ") == "BQE"
    assert utils.normalize_pandas_freq("BQ-FEB") == "BQE-FEB"
