from hcsr04sensor import sensor
TRIG = 17
ECHO = 18
Temp_f = 70
SAM = 1

m.sensor.Measurement(TRIG,ECHO,TEMP_f,'metric')
dist = m.raw_distance(sample_size=SAM)
print(dist)
