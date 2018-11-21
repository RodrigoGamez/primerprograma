

from time import sleep
import datetime

NIGHT_STARTS = 19
DAY_STARTS = 8
HOUR_DURATION = 1


def main():
    current_time = datetime.datetime.now()
    while True:
        sleep(HOUR_DURATION)
        current_time += datetime.timedelta(hours=1)

        if current_time.hour >= NIGHT_STARTS or current_time.hour <= DAY_STARTS:
            day_or_night = "Noche"

        else:
            day_or_night = "Dia"

        with open("horas.txt", "w") as hours_file:
            time_text = "La hora actual es: {}, es de: {}\n".format(current_time, day_or_night)
            hours_file.write(time_text)



if __name__ == "__main__":
    main()