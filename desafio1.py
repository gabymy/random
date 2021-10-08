import pytz
from datetime import datetime

pais = input('ingrese el lugar que quiera saber la hora:  ')
time_zone = pytz.timezone(pais)
ahora = datetime.now(time_zone)

print(ahora.strftime(f'Hora actual en {time_zone} es %H:%M:%S'))
