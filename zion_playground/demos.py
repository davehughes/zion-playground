


DEMOS = [
    {
        "title": "Hello World",
        "slug": "hello-world",
        "program": '''
module _

fn main() {
    print("Hello Zion!")
}
''',
    },
    {
        "title": "8 Queens",
        "slug": "eight-queens",
        "program": '''
module _

fn queens(rows int, columns int) [[int]] {
    var solutions [[int]]
    var solution [int]

    # Introduce an empty solution upon which the dynamic programming algorithm can build
    append(solutions, solution)

    for row in range(rows) {
        solutions = add_one_queen(row, columns, solutions)
    }

    return solutions
}

fn add_one_queen(new_row int, columns int, prev_solutions [[int]]) [[int]] {
    var solutions [[int]]
    reserve(solutions, 92)

    for solution in prev_solutions {
        for new_column in range(columns) {
            if no_conflict(new_row, new_column, solution) {
                append(solutions, copy(solution, new_column))
            }
        }
    }

    return solutions
}

fn no_conflict(new_row int, new_column int, solution [int]) bool {
    for row in range(new_row) {
        condition := (
            solution[row]       != new_column           and
            solution[row] + row != new_column + new_row and
            solution[row] - row != new_column - new_row)
                        
        if not condition {
            return false
        }
    }

    return true
}

fn main() {
    solutions := queens(8, 8)

    for solution in solutions {
        print(solution)
    }
}
'''
    },
]

DEMOS_BY_SLUG = {d['slug']: d for d in DEMOS}
