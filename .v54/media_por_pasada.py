# -*- coding: utf-8 -*-
"""LA MEDIA POR PASADA, CON SU NUMERADOR Y SU DENOMINADOR NOMBRADOS (D.59).

Regenera la cifra que la vuelta 53 publico mal. No la corrige a mano: la calcula, y
**dice de que la calcula**, que es lo que la regla pide.
"""
SUMA_53 = 4659.0          # suma del reloj de aduana de la vuelta 53
LANZADAS_53 = 11          # pasadas de aduana lanzadas
CON_RELOJ_53 = 9          # pasadas con fichero de reloj
SUMA_52 = 4387.4          # suma del reloj de la vuelta 52
PASADAS_52 = 6.0          # sus pasadas, todas con reloj

print("LA MEDIA POR PASADA DE LA VUELTA 53, con numerador y denominador nombrados")
print("")
print("  numerador : %.1f s, la suma del reloj de aduana de la vuelta 53" % SUMA_53)
print("              (INCLUYE la pasada de 600 s que no dejo fichero de reloj)")
print("")
print("  %-58s %7.1f s" % ("sobre las %d pasadas LANZADAS" % LANZADAS_53,
                           SUMA_53 / LANZADAS_53))
print("  %-58s %7.1f s" % ("sobre las %d pasadas CON fichero de reloj" % CON_RELOJ_53,
                           SUMA_53 / CON_RELOJ_53))
print("")
print("  contraste: la vuelta 52, %.1f s sobre %.1f pasadas" % (SUMA_52, PASADAS_52))
print("  %-58s %7.1f s" % ("su media por pasada", SUMA_52 / PASADAS_52))
print("")
media_53 = SUMA_53 / LANZADAS_53
media_52 = SUMA_52 / PASADAS_52
print("  LA CAIDA POR PASADA, que es la que presupuesta:")
print("  %-58s %7.1f por ciento" % ("(%.1f menos %.1f) sobre %.1f"
                                    % (media_53, media_52, media_52),
                                    (media_53 - media_52) / media_52 * 100.0))
print("")
print("  POR QUE EL DENOMINADOR SON LAS 11 Y NO LAS 9: el numerador ya trae dentro la")
print("  pasada sin fichero de reloj. Dividirlo entre 9 mezcla dos poblaciones, y esa")
print("  mezcla es la caida de la vuelta 53.")
