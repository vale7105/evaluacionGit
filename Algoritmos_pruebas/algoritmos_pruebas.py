"""
Algoritmos_pruebas/validar_documento.py
Script de prueba basico para el proyecto de microservicios de la EPS.
Valida el formato de un numero de documento de identidad (cedula).
"""


def validar_documento(numero_documento: str) -> bool:
    """
    Valida que el numero de documento contenga solo digitos
    y tenga una longitud entre 6 y 10 caracteres.
    """
    return numero_documento.isdigit() and 6 <= len(numero_documento) <= 10


def validar_correo(correo: str) -> bool:
    """
    Valida de forma basica que un correo tenga arroba y un punto
    despues de la arroba.
    """
    if "@" not in correo:
        return False
    usuario, dominio = correo.split("@", 1)
    return len(usuario) > 0 and "." in dominio


if __name__ == "__main__":
    casos_documento = ["1234567", "12", "abc1234", "1122334455"]
    for caso in casos_documento:
        print(f"Documento '{caso}' valido: {validar_documento(caso)}")

    casos_correo = ["paciente@eps.com", "correo-invalido", "usuario@dominio"]
    for caso in casos_correo:
        print(f"Correo '{caso}' valido: {validar_correo(caso)}")
