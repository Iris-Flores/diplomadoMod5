from django.core.exceptions import ValidationError
import re

def validate_capacity(value):
    if value <10 or value > 20:
        raise ValidationError("La capacidad debe ser mínimo 10 estudiantes y máximo 20")
    
def validate_edad(value):
    if value < 10 or value > 25:
        raise ValidationError("edad mínima de 10 años y máximo 25")

def validate_email(value):
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$", value):
        raise ValidationError("El formato de correo no es válido")