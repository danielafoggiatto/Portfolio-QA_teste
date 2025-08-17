def count_letters_digits(texto: str) -> dict:
   
    letras = sum(c.isalpha() for c in texto)
    digitos = sum(c.isdigit() for c in texto)

    return {"letras": letras, "digitos": digitos}
