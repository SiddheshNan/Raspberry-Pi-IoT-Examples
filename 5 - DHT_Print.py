import Adafruit_DHT

hum,temp=Adafruit_DHT.read_retry(11,2)

print (hum,temp)
