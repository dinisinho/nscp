from psutil import cpu_percent
import sys

if cpu_percent() < 90:
    print cpu_percent()
    saida = 0
elif cpu_percent() >= 90 and cpu_percent < 99:
    print "Uso de CPU superior ao 90%"
    saida = 1
elif cpu_percent() == 100:
    print "Uso de CPU ao 100%"
    saida = 2
else:
    saida = 3

sys.exit(saida)
