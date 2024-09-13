from fpdf import FPDF

def generate_cv(name, job, email=None, experience=None, education=None, output_file="output.pdf"):
    pdf = FPDF()
    pdf.add_page()

    # Título del CV
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, f"CV de {name}", ln=True, align='C')

    # Información básica
    pdf.set_font("Arial", 'I', 12)
    pdf.cell(200, 10, f"Puesto: {job}", ln=True, align='C')
    
    if email:
        pdf.cell(200, 10, f"Email: {email}", ln=True, align='C')

    # Añadir experiencia laboral
    if experience:
        pdf.ln(10)  # Espacio
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(200, 10, "Experiencia Laboral:", ln=True)
        
        pdf.set_font("Arial", '', 12)
        for exp in experience:
            pdf.cell(200, 10, f"- {exp}", ln=True)

    # Añadir educación
    if education:
        pdf.ln(10)  # Espacio
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(200, 10, "Educación:", ln=True)
        
        pdf.set_font("Arial", '', 12)
        for edu in education:
            pdf.cell(200, 10, f"- {edu}", ln=True)
    
    # Guardar el archivo PDF
    pdf.output(output_file)
from fpdf import FPDF

def generate_cv(name, job, output_file):
    pdf = FPDF()
    pdf.add_page()

    # Título del CV
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, f"CV de {name}", ln=True, align='C')

    # Título del trabajo
    pdf.set_font("Arial", 'I', 12)
    pdf.cell(200, 10, f"Puesto: {job}", ln=True, align='C')
    
    # Guardamos el archivo PDF
    pdf.output(output_file)
