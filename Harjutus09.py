# Roger Niils
# Harjutus09
# 28.02.22

#isikukood

isik = "50506240220"

aasta = int(isik[1]+isik[2])+2000
kuu = int(isik[3]+isik[4])
päev = int(isik[5]+isik[6])
print(aasta,kuu,päev)

import datetime
from datetime import timedelta

import locale
locale.setlocale(locale.LC_ALL, 'ET')

kuupaev = datetime.datetime.now()

print(kuupaev.strftime("%d.%B.%Y"))