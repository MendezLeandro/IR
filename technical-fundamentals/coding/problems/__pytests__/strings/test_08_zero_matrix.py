from python_solutions.strings import zero_matrix


def test_zeroes_2x2_matrix():
    matrix = [
        [0, 2],
        [3, 4],
    ]
    expected = [
        [0, 0],
        [0, 4],
    ]
    zero_matrix(matrix)
    assert matrix == expected


def test_zeroes_3x3_matrix():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 0, 9],
    ]
    expected = [
        [1, 0, 3],
        [4, 0, 6],
        [0, 0, 0],
    ]
    zero_matrix(matrix)
    assert matrix == expected


def test_zeroes_4x4_matrix():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 0, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    expected = [
        [1, 2, 0, 4],
        [0, 0, 0, 0],
        [9, 10, 0, 12],
        [13, 14, 0, 16],
    ]
    zero_matrix(matrix)
    assert matrix == expected


def test_two_zeroes_4x4_matrix():
    matrix = [
        [0, 2, 3, 4],
        [5, 6, 0, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    expected = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 10, 0, 12],
        [0, 14, 0, 16],
    ]
    zero_matrix(matrix)
    assert matrix == expected

