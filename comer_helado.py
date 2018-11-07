apetece_helado = input("¿Te apetece un helado? (Si/No): ").upper()
if apetece_helado == "SI":
    apetece_helado = "SI"
elif apetece_helado == "NO":
    apetece_helado = "NO"
else:
    apetece_helado = "NO"
    print("Te he dicho que me digas si o no, como no se que me has dicho, cuento como que no")



tiene_dinero = input("¿Tienes dinero para un helado? (Si/No): ").upper()
if tiene_dinero == "SI":
    tiene_dinero = "SI"
elif tiene_dinero == "NO":
    tiene_dinero = "NO"
else:
    tiene_dinero = "NO"
    print("Te he dicho que me digas si o no, como no se que me has dicho, cuento como que no")



esta_el_señor_de_los_helados = input("¿Esta el señor de los helados? (Si/No): ").upper()
if esta_el_señor_de_los_helados == "SI":
    esta_el_señor_de_los_helados = "SI"
elif esta_el_señor_de_los_helados == "NO":
    esta_el_señor_de_los_helados = "NO"
else:
    esta_el_señor_de_los_helados = "NO"
    print("Te he dicho que me digas si o no, como no se que me has dicho, cuento como que no")



esta_tu_tia = input("¿Estas con tu Tia? (Si/No): ").upper()
if esta_tu_tia == "SI":
    esta_tu_tia = "SI"
elif esta_tu_tia == "NO":
    esta_tu_tia = "NO"
else:
    esta_tu_tia = "NO"
    print("Te he dicho que me digas si o no, como no se que me has dicho, cuento como que no")




if apetece_helado == "SI" and (tiene_dinero == "SI" or esta_tu_tia == "SI") and esta_el_señor_de_los_helados == "SI":
    print("Pues cometelo")
else:
    print("Pues no te lo comas")