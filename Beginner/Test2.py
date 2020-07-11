from datetime import datetime, timedelta
num = 12
num2 = 2
print (num**num2)
current_date = datetime.now()
print ('Today is : '+ str(current_date))
one_day = timedelta(days=1)
yesterday = current_date- one_day
print ('yestaerday is : '+ str(yesterday))
adir=input('when is your BD ')

israel = datetime.strptime(adir, '%d/%m/%Y')
print(israel)
print ()
print(str(israel.hour))
