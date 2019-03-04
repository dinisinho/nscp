import psutil
import sys

porcentaxe = psutil.virtual_memory()[2]

if porcentaxe < 80:
    print "Uso de RAM correcto: "+str(porcentaxe)
    saida = 0
elif porcentaxe >= 80 and porcentaxe <= 90:
    print "Uso de RAM superior ao 80%: "+str(porcentaxe)
    saida = 1
elif porcentaxe > 90:
    print "Uso de RAM superior ao 90%: "+str(porcentaxe)
    saida = 2
else:
    saida = 3

sys.exit(saida)
