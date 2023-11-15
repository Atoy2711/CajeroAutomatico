import subprocess

# Ruta al archivo .jrxml
jrxml_file = "tu_informe.jrxml"

# Ruta al archivo de datos
data_file = "tus_datos.json"

# Comando para generar el informe y abrirlo en un visor PDF externo
command = [
    "jasperstarter", "process",
    jrxml_file,
    "--format", "pdf",  # Puedes elegir otro formato si lo deseas
    "--locale", "es",   # Especifica tu locale si es necesario
    "--data", data_file,
    "--output", "tu_informe.pdf"
]

subprocess.run(command)

# Abre el informe en el visor PDF predeterminado
subprocess.run(["xdg-open", "tu_informe.pdf"])  # En sistemas basados en Linux

# Puedes ajustar la apertura del visor PDF según tu sistema operativo

def generar_informe_diario():
    # Implementar generación de informe diario
    # Mostrar transacciones, saldos, ganancias, etc.
    pass