def generate_combinations(production, nullable):
    """
    Genera todas las combinaciones posibles eliminando los símbolos anulables de una producción.
    
    Args:
        production (str): Producción original.
        nullable (set): Conjunto de símbolos anulables.
    
    Returns:
        set: Conjunto de producciones generadas.
    """
    symbols = list(production)
    results = set()

    def backtrack(index, current):
        if index == len(symbols):
            if current:
                results.add("".join(current))
            return
        if symbols[index] in nullable:
            backtrack(index + 1, current)
        backtrack(index + 1, current + [symbols[index]])

    backtrack(0, [])
    
    return results


def display_grammar(grammar):
    """
    Muestra la gramática de forma legible.
    
    Args:
        grammar (dict): Diccionario que representa la gramática cargada.
    """
    for non_terminal, productions in grammar.items():
        print(f"{non_terminal} -> {' | '.join(productions)}")
