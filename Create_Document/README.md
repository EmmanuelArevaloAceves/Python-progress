
# Create_Document Instructions

This document provides instructions on how to use the "Create_Document" folder. This folder simulates a system for creating and counting three types of documents: PDF, Word, and Text.

When you create any type of document, a global counter is incremented to keep track of how many documents have been created. This counter is implemented using the Singleton design pattern to ensure that only one instance exists throughout the entire program.




## Features

- Create different types of documents: PDF, Word, and Text.
- Keep track of the total number of documents created.
- Factory Pattern used to create documents dynamically.
- Singleton Pattern used to maintain a global document counter.


## How to run the program

    1. Clone this repository or download the folder.
    2. Navigate to the project directory.
    3. Run the main file:


python principal.py


## Proyect Structure


- `documento.py`: Defines the base class and document types.
- `fabrica.py`: Contains the factory that creates document instances.
- `contador.py`: Implements the Singleton document counter.
- `principal.py`: The main CLI interface for interacting with the system.

## Technologies Used

- Python 3.x
- Object-Oriented Programming
- Design Patterns: Factory and Singleton
## Example Output

```bash
===== MENÚ DE DOCUMENTOS =====
1. Crear documento
2. Ver número de documentos creados
3. Salir
Selecciona una opción (1-3): 1
Ingresa tipo de documento (pdf, word, text): pdf
Leyendo documento PDF.

===== MENÚ DE DOCUMENTOS =====
1. Crear documento
2. Ver número de documentos creados
3. Salir
Selecciona una opción (1-3): 2
 Total de documentos creados: 1

===== MENÚ DE DOCUMENTOS =====
1. Crear documento
2. Ver número de documentos creados
3. Salir
Selecciona una opción (1-3): 3
¡Gracias por usar el sistema de documentos!

Process finished with exit code 0