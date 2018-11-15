
import datetime

AVERAGE_LIFESPAN =  80

SMOKER_PENALIZATION = 10
DRINKER_PENALIZATION = 10
SEDENTARY_PENALIZATION = 20

def print_with_underscores(message):
    print(message)
    print(len(message) * "-")

def ask_yes_or_not(message):
    response = None

    while response != "S" and response != "N":
        response = input(message + "[S/N]")
    return response


print_with_underscores("Averigua cuanto te queda de vida")
print("Completa esta encuesta para saber cuantos años te quedan")


birth_date = input("¿Cual es tu fecha de nacimiento (formato dd/mm/yyyy)?")


birth_date = datetime.datetime.strptime(birth_date, "%d/%m/%Y")

years_losts = 0


if ask_yes_or_not("¿Fumas?"):
    years_losts += SMOKER_PENALIZATION

if ask_yes_or_not("¿Bebes?"):
    years_losts += DRINKER_PENALIZATION

if  not ask_yes_or_not("¿Haces deporte?"):
    years_losts += SEDENTARY_PENALIZATION


lifespan = AVERAGE_LIFESPAN - years_losts

death_day = birth_date + datetime.timedelta(days = lifespan*365)

print("Fecha de muerte: {}".format(death_day.strftime("%d/%m/%Y")))