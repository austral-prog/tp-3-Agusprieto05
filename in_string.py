def check_vowels():
    name = str(input("Nombre: "))
    print(f"Contiene a: {"a" in name or "A" in name or "á" in name or "Á" in name}")
    print(f"Contiene e: {"e" in name or "E" in name or "é" in name or "É" in name}")
    print(f"Contiene i: {"i" in name or "I" in name or "í" in name or "Í" in name}")
    print(f"Contiene o: {"o" in name or "O" in name}")
    print(f"Contiene u: {"u" in name or "U" in name}")


