import os
import re
from exceptions import GrammarError

GRAMMAR_REGEX = re.compile(r"^[A-Z]\s*->\s*([A-Za-z0-9]+(\s*\|\s*[A-Za-z0-9]+)*)|ε$")

class GrammarLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_grammar(self):
        """
        Carga una gramática desde un archivo de texto y valida su formato.
        
        Returns:
            dict: Diccionario que representa la gramática cargada.
        
        Raises:
            FileNotFoundError: Si el archivo no existe.
            GrammarError: Si alguna línea de la gramática tiene un formato incorrecto.
        """
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"El archivo '{self.file_path}' no existe.")
        
        grammar = {}
        with open(self.file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not GRAMMAR_REGEX.match(line):
                    raise GrammarError(f"La línea '{line}' no tiene un formato válido.")
                
                # Separar el lado izquierdo (no terminal) y el derecho (producción)
                left_side, right_side = map(str.strip, line.split('->'))
                productions = list(map(str.strip, right_side.split('|')))
                
                if left_side in grammar:
                    grammar[left_side].extend(productions)
                else:
                    grammar[left_side] = productions
        
        return grammar
