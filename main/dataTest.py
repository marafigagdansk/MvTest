import datetime
import calendar

# Obtendo a data atual
now = datetime.datetime.now()

# Calculando o último dia do mês atual
last_day_of_month = calendar.monthrange(now.year, now.month)[1]

# Criando uma data com o último dia do mês atual
last_date = datetime.date(now.year, now.month, last_day_of_month)

print("O último dia do mês atual é:", last_date)    