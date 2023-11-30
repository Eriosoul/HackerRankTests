import calendar

# Crear una instancia de la clase TextCalendar
cal = calendar.TextCalendar(calendar.SUNDAY)

# Mostrar un calendario mensual para un año y mes específicos
year = 2015
month = 8
day = 5

# Utilizar la función weekday() para obtener el día de la semana (0: lunes, 6: domingo)
day_of_week = cal.weekday(year, month, day)

# Convertir el índice del día de la semana a un nombre
day_name = calendar.day_name[day_of_week]

print(day_name.upper())