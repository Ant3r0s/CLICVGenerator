import argparse
from cvcraft.generator import generate_cv  # Importamos la función que generará el CV

def main():
    # Configuramos los argumentos de la CLI
    parser = argparse.ArgumentParser(description="Genera un CV en PDF con estilos personalizados.")
    
    # Argumentos principales
    parser.add_argument('--name', type=str, required=True, help="Nombre completo del usuario.")
    parser.add_argument('--job', type=str, required=True, help="Título del trabajo o profesión.")
    parser.add_argument('--email', type=str, help="Correo electrónico (opcional).")
    
    # Nuevos argumentos: experiencia laboral y educación
    parser.add_argument('--experience', type=str, nargs='+', help="Lista de experiencias laborales (separadas por comas).")
    parser.add_argument('--education', type=str, nargs='+', help="Lista de grados educativos (separadas por comas).")
    
    # Argumento para la salida del archivo
    parser.add_argument('--output', type=str, required=True, help="Nombre del archivo de salida (ej. output.pdf).")

    # Parseamos los argumentos
    args = parser.parse_args()
    
    # Pasamos los argumentos a la función generadora de CV
    generate_cv(
        name=args.name,
        job=args.job,
        email=args.email,
        experience=args.experience,
        education=args.education,
        output_file=args.output
    )

if __name__ == "__main__":
    main()
import argparse
from cvcraft.generator import generate_cv  # Importamos la función que generará el CV

def main():
    # Configuramos los argumentos de la CLI
    parser = argparse.ArgumentParser(description="Genera un CV en PDF con estilos personalizados.")
    
    # Definimos los argumentos que va a recibir la CLI
    parser.add_argument('--name', type=str, required=True, help="Nombre completo del usuario.")
    parser.add_argument('--job', type=str, required=True, help="Título del trabajo o profesión.")
    parser.add_argument('--output', type=str, required=True, help="Nombre del archivo de salida (ej. output.pdf).")

    # Parseamos los argumentos
    args = parser.parse_args()
    
    # Pasamos los argumentos a la función generadora de CV
    generate_cv(args.name, args.job, args.output)

if __name__ == "__main__":
    main()
