def is_mutant(dna):
    def check_sequence(matrix, n, m, delta_x, delta_y):
        """Comprueba si hay una secuencia consecutiva en una dirección."""
        count = 1
        x, y = n, m
        while (
            0 <= x + delta_x < len(matrix) and
            0 <= y + delta_y < len(matrix[0]) and
            matrix[x][y] == matrix[x + delta_x][y + delta_y]
        ):
            count += 1
            x += delta_x
            y += delta_y
            if count == 4:
                return True
        return False

    sequences = 0
    matrix = [list(row) for row in dna]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (
                check_sequence(matrix, i, j, 1, 0) or  # Vertical
                check_sequence(matrix, i, j, 0, 1) or  # Horizontal
                check_sequence(matrix, i, j, 1, 1) or  # Diagonal hacia abajo
                check_sequence(matrix, i, j, 1, -1)   # Diagonal hacia arriba
            ):
                sequences += 1
                if sequences > 1:
                    return True
    return False
