def varnum(i, j, d):
    """Satır i, sütun j için değer d'yi temsil eden değişken numarası."""
    return 81 * (i - 1) + 9 * (j - 1) + d


def exactly_one(vars):
    """Bu değişkenlerden tam olarak birinin TRUE olması için gerekli CNF cümleleri."""
    clauses = [vars]  # En az biri TRUE
    for i in range(len(vars)):
        for j in range(i + 1, len(vars)):
            clauses.append([-vars[i], -vars[j]])  # Aynı anda ikisi TRUE olamaz
    return clauses


def sudoku_to_cnf(puzzle):
    clauses = []

    # 1. Her hücrede bir sayı olmalı (satır i, sütun j)
    for i in range(1, 10):
        for j in range(1, 10):
            vars = [varnum(i, j, d) for d in range(1, 10)]
            clauses += exactly_one(vars)

    # 2. Her satırda her sayı yalnızca bir kez
    for i in range(1, 10):
        for d in range(1, 10):
            vars = [varnum(i, j, d) for j in range(1, 10)]
            clauses += exactly_one(vars)

    # 3. Her sütunda her sayı yalnızca bir kez
    for j in range(1, 10):
        for d in range(1, 10):
            vars = [varnum(i, j, d) for i in range(1, 10)]
            clauses += exactly_one(vars)

    # 4. Her 3x3 blokta her sayı yalnızca bir kez
    for block_i in range(0, 3):
        for block_j in range(0, 3):
            for d in range(1, 10):
                vars = []
                for i in range(1 + 3 * block_i, 4 + 3 * block_i):
                    for j in range(1 + 3 * block_j, 4 + 3 * block_j):
                        vars.append(varnum(i, j, d))
                clauses += exactly_one(vars)

    # 5. Önceden verilen sayılar
    for i in range(9):
        for j in range(9):
            d = puzzle[i][j]
            if d != 0:
                clauses.append([varnum(i + 1, j + 1, d)])

    return clauses


def write_cnf_file(clauses, filename):
    with open(filename, 'w') as f:
        f.write(f"p cnf 729 {len(clauses)}\n")
        for clause in clauses:
            f.write(" ".join(str(lit) for lit in clause) + " 0\n")


# Örnek Sudoku (0 = boş hücre)
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

clauses = sudoku_to_cnf(puzzle)
write_cnf_file(clauses, "sudoku.cnf")

print("CNF dosyası oluşturuldu: sudoku.cnf")