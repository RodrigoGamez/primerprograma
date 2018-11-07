#video pokemons minuto 30 segundo 20



pokemon_elegido = input("¿Contra que pokemon quieres luchar? (Squirtle/Charmander/Bulbasur): ").upper()

vida_pikachu = 100
vida_enemigo = 0
ataque_pokemon = 0

if pokemon_elegido == "SQUIRTLE":
    vida_enemigo = 90
    nombre_pokemon = "Squirtle"
    ataque_pokemon = 8

elif pokemon_elegido == "CHARMANDER":
    vida_enemigo = 80
    ataque_pokemon = 7
    nombre_pokemon = "Charmander"

elif pokemon_elegido == "BULBASUR":
    nombre_pokemon = "Bulbasur"
    ataque_pokemon = 10
    vida_enemigo = 100



while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input("¿Que ataque quieres usar? (Chispazo/Bola voltio): ").upper()

    if ataque_elegido == "CHISPAZO":
        vida_enemigo -=10

    if ataque_elegido == "BOLA VOLTIO":
        vida_enemigo -=12

    print("La vida del {} ha bajado aahora es de: {}".format(nombre_pokemon, vida_enemigo))

    if pokemon_elegido == "SQUIRTLE":
        print("{} te ha hecho un ataque de {} de daño".format(nombre_pokemon, ataque_pokemon))
        vida_pikachu -= ataque_pokemon

    print("Tu vida ha bajado ahora es de: {}".format(vida_pikachu))

if vida_pikachu <= 0:
    print("Has perdido")
else:
    print("Has ganado")