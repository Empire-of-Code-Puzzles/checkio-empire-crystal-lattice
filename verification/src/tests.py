TESTS = {
    "Rank": [
        {
            "input": [[['X', 'Z'], ['Z', 'X']], [['Z', 'X'], ['X', 'Z']]],
            "answer": True,
        },
        {
            "input": [[['X', 'Z'], ['Z', 'X']], [['X', 'Z'], ['Z', 'X']]],
            "answer": False,
        },
        {
            "input": [[['X', 'Z', 'X'], ['Z', 'X', 'Z'], ['X', 'Z', 'X']],
                      [['Z', 'X', 'Z'], ['X', 'Z', 'X'], ['Z', 'X', 'Z']],
                      [['X', 'Z', 'X'], ['Z', 'X', 'Z'], ['X', 'Z', 'X']]],
            "answer": True,
        },
        {
            "input": [[['X', 'Z', 'X'], ['Z', 'X', 'Z'], ['X', 'Z', 'X']],
                      [['Z', 'X', 'Z'], ['X', 'X', 'X'], ['Z', 'X', 'Z']],
                      [['X', 'Z', 'X'], ['Z', 'X', 'Z'], ['X', 'Z', 'X']]],
            "answer": False,
        },
        {
            "input": [[['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'],
                       ['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X']],
                      [['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'],
                       ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z']],
                      [['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'],
                       ['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X']],
                      [['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'],
                       ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z']],
                      [['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'],
                       ['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X']]],
            "answer": True,
        },
        {
            "input": [[['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'],
                       ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z']],
                      [['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'],
                       ['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X']],
                      [['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'],
                       ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z']],
                      [['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'],
                       ['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X']],
                      [['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'],
                       ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z']]],
            "answer": True,
        },
        {
            "input": [[['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'],
                       ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z']],
                      [['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'],
                       ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z']],
                      [['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'],
                       ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z']],
                      [['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'],
                       ['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X']],
                      [['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'],
                       ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z']]],
            "answer": False,
        },
        {
            "input": [[['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'],
                       ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z']],
                      [['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'],
                       ['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X']],
                      [['Z', 'X', 'Z', 'X', 'Z'], ['Z', 'X', 'Z', 'X', 'Z'], ['Z', 'X', 'Z', 'X', 'Z'],
                       ['Z', 'X', 'Z', 'X', 'Z'], ['Z', 'X', 'Z', 'X', 'Z']],
                      [['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'],
                       ['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X']],
                      [['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'],
                       ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z']]],
            "answer": False,
        },
    ]
}
