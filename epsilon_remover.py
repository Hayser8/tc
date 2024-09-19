from grammar_utils import generate_combinations, display_grammar

class EpsilonRemover:
    def __init__(self, grammar):
        self.grammar = grammar
        self.nullable = set()

    def find_nullable_symbols(self):
        """
        Encuentra los símbolos anulables en la gramática y muestra el proceso en consola.
        
        Returns:
            set: Conjunto de símbolos anulables.
        """
        print("Paso 1: Encontrar símbolos anulables inicialmente.")
        
        for non_terminal, productions in self.grammar.items():
            for production in productions:
                if production == "ε":
                    self.nullable.add(non_terminal)
                    print(f"  - El símbolo '{non_terminal}' es anulable porque tiene la producción 'ε'.")

        print(f"Símbolos anulables iniciales: {self.nullable}\n")
        
        # Propagar anulabilidad
        changed = True
        while changed:
            changed = False
            for non_terminal, productions in self.grammar.items():
                if non_terminal not in self.nullable:
                    for production in productions:
                        if all(symbol in self.nullable for symbol in production):
                            self.nullable.add(non_terminal)
                            changed = True
                            print(f"  - El símbolo '{non_terminal}' es anulable porque todas las producciones de '{production}' son anulables.")
                            break
        
        print(f"Símbolos anulables finales: {self.nullable}\n")

    def remove_epsilon_productions(self):
        """
        Elimina las producciones-ε de la gramática y muestra los pasos en consola.
        
        Returns:
            dict: Gramática sin producciones-ε.
        """
        print("=== Iniciando el proceso de eliminación de producciones-ε ===\n")
        
        self.find_nullable_symbols()
        new_grammar = {}

        print("Paso 2: Generar nuevas producciones eliminando las producciones-ε.")
        
        for non_terminal, productions in self.grammar.items():
            new_productions = set()
            print(f"  - Analizando producciones de '{non_terminal}': {productions}")
            for production in productions:
                if production != "ε":
                    combinations = generate_combinations(production, self.nullable)
                    new_productions.update(combinations)
                    print(f"    - Producción '{production}' genera nuevas combinaciones: {combinations}")
                else:
                    print(f"    - Se elimina la producción-ε en '{non_terminal} -> ε'.")
            
            new_grammar[non_terminal] = list(new_productions)
        
        print("\nPaso 3: Gramática sin producciones-ε:")
        display_grammar(new_grammar)
        
        return new_grammar
