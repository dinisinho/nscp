import psutil
import sys

porcentaxe = psutil.disk_usage("/")[3]

if porcentaxe < 80:
    print "Espazo en dico correcto: "+str(porcentaxe)
    saida = 0
elif porcentaxe >= 80 and porcentaxe <= 90:
    print "Espazo en disco superior ao 80%: "+str(porcentaxe)
    saida = 1
elif porcentaxe > 90:
    print "Espazo en disco superior ao 90%: "+str(porcentaxe)
    saida = 2
else:
    saida = 3

sys.exit(saida)
