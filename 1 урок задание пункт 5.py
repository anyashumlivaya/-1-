revenue  = float(input("введите выручку компании "))
costs = float(input(" введите затраты компании "))
if revenue > costs:
	print(f"у вас получена прибыль. ваша рентабельность составила: {(revenue - costs)/costs:.2f} ")
	workers = int(input("введите количество сотрудников "))
	print (f"прибыль на 1 сотрудника -  {(revenue-costs)/workers:.2f}")
elif revenue == costs:
	print(" прибыль отсутствует")
else:
		print ("убыток")