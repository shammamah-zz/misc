import pyowm 

owm = pyowm.OWM('c18c66b469910fc53ab0b61689050ceb')

current = owm.weather_at_place('Montreal').get_weather()
temp = current.get_temperature('celsius')
status = current.get_status()

print('current status: '+status.lower())
print('temperature: '+str(temp['temp'])+'C')
