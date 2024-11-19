def is_mutant(dna):
    """
    Detecta si una secuencia de ADN pertenece a un mutante.
    Args:
        dna (list[str]): Lista de cadenas que representan la matriz NxN de ADN.
    Returns:
        bool: True si es mutante, False si es humano.
    """
    n = len(dna)

    # Validación de que es una matriz NxN
    if not all(len(row) == n for row in dna):
        raise ValueError("La secuencia de ADN debe ser una matriz NxN.")

    # Validación de caracteres
    valid_chars = {'A', 'T', 'C', 'G'}
    for row in dna:
        if any(char not in valid_chars for char in row):
            raise ValueError("La secuencia de ADN contiene caracteres inválidos. Solo se permiten 'A', 'T', 'C', 'G'.")

    mutant_sequences = 0

    def check_sequence(i, j, di, dj):
        """Chequea si hay 4 letras consecutivas iguales en una dirección dada."""
        count = 1
        for _ in range(3):
            i, j = i + di, j + dj
            if 0 <= i < n and 0 <= j < n and dna[i][j] == dna[i - di][j - dj]:
                count += 1
            else:
                break
        return count == 4

    for i in range(n):
        for j in range(n):
            # Revisar horizontal, vertical y diagonales
            if (
                j <= n - 4 and check_sequence(i, j, 0, 1) or  # Horizontal
                i <= n - 4 and check_sequence(i, j, 1, 0) or  # Vertical
                i <= n - 4 and j <= n - 4 and check_sequence(i, j, 1, 1) or  # Diagonal \
                i >= 3 and j <= n - 4 and check_sequence(i, j, -1, 1)  # Diagonal /
            ):
                mutant_sequences += 1
                if mutant_sequences > 1:
                    return True

    return False
