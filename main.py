from grammar_loader import GrammarLoader
from epsilon_remover import EpsilonRemover
from exceptions import GrammarError

def menu():
    """
    Despliega un menú para que el usuario elija cuál archivo de gramática cargar.
    
    Returns:
        str: El nombre del archivo de gramática seleccionado.
    """
    print("Seleccione el archivo de gramática a cargar:")
    print("1. Gramatica 1 (gramatica1.txt)")
    print("2. Gramatica 2 (gramatica2.txt)")
    
    while True:
        choice = input("Ingrese el número de su elección: ")
        if choice == '1':
            return "gramatica1.txt"
        elif choice == '2':
            return "gramatica2.txt"
        else:
            print("Opción no válida. Por favor ingrese '1' o '2'.")

def main():
    # Mostrar menú y obtener archivo seleccionado
    grammar_file = menu()
    loader = GrammarLoader(grammar_file)
    
    try:
        # Cargar la gramática seleccionada
        grammar = loader.load_grammar()
        print(f"\nGramática cargada desde {grammar_file}:")
        from grammar_utils import display_grammar
        display_grammar(grammar)

        # Eliminar producciones-ε
        print("\nEliminando producciones-ε...")
        remover = EpsilonRemover(grammar)
        grammar_without_epsilon = remover.remove_epsilon_productions()
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except GrammarError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
