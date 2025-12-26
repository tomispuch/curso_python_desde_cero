#Trabajando con fechas y horas en Python

from datetime import datetime, timedelta 

# Obtener la fecha y hora actuales
print("Fecha y hora actuales:")
now = datetime.now()
print(now)

# Crear una fecha específica
print("\nFecha específica:")
specific_date = datetime(2023, 1, 15) #Año, Mes, Día
print(specific_date)

# Formatear fechas
#METODO STRFTIME
print("\nFecha formateada:")
formatted_date = now.strftime("%d/%m/%Y %H:%M:%S") #Día/Mes/Año Hora:Minuto:Segundo 
#Para más formatos, consultar la documentación oficial de Python
#https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
print(formatted_date)

# Operaciones con fechas

print("\nOperaciones con fechas:")
# Sumar 10 días a la fecha actual
ten_days_later = now + timedelta(days=10)
print("Fecha actual + 10 días:", ten_days_later)

# Restar 5 horas a la fecha actual
five_hours_earlier = now - timedelta(hours=5)
print("Fecha actual - 5 horas:", five_hours_earlier)

# Diferencia entre dos fechas
date1 = datetime(2023, 5, 1)
date2 = datetime(2023, 6, 1)
difference = date2 - date1
print("Diferencia entre", date2.date(), "y", date1.date(), "es de", difference.days, "días")

#Obtener las partes de una fecha

print("\nPartes de una fecha:")
print("Año:", now.year)
print("Mes:", now.month)
print("Día:", now.day)
print("Hora:", now.hour)
print("Minuto:", now.minute)
print("Segundo:", now.second)

