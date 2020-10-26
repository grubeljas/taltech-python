import pytest

from inception import countdown, add_commas, stonks, quic_mafs, sum_squares


def test():

    assert countdown(5) == [5, 4, 3, 2, 1, 0]
    assert add_commas(1000) == '1,000'
    assert stonks(1000, 10, 10) == 2593
    assert quic_mafs(4, 2) == [0, 2]
    assert sum_squares([1, 2, 3]) == 14
    assert countdown(-2) == []
    assert add_commas(12903) == '12,903'
    assert stonks(1000, 10, 1) == 1100
    assert quic_mafs(0, 2) == [0, 2]
    assert sum_squares([1, [5]]) == 26
    assert quic_mafs(155, 1) == [1, 1]
