from python_solutions.strings import improved_rotate_matrix


def test_rotates_2x2_matrix_clockwise():
    matrix = [
        [1, 2],
        [3, 4],
    ]
    expected = [
        [3, 1],
        [4, 2],
    ]
    improved_rotate_matrix(matrix)
    assert matrix == expected


def test_rotates_3x3_matrix_clockwise():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    expected = [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
    ]
    improved_rotate_matrix(matrix)
    assert matrix == expected


def test_rotates_4x4_matrix_clockwise():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    expected = [
        [13, 9, 5, 1],
        [14, 10, 6, 2],
        [15, 11, 7, 3],
        [16, 12, 8, 4],
    ]
    improved_rotate_matrix(matrix)
    assert matrix == expected


def test_rotates_5x5_matrix_clockwise():
    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]
    expected = [
        [21, 16, 11, 6, 1],
        [22, 17, 12, 7, 2],
        [23, 18, 13, 8, 3],
        [24, 19, 14, 9, 4],
        [25, 20, 15, 10, 5],
    ]
    improved_rotate_matrix(matrix)
    assert matrix == expected

