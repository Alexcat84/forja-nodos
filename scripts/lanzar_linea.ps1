# LANZA UNA LINEA DEL ARNES SIN VENTANA Y FUERA DE LA SESION QUE LA PIDE (23 sep 2026).
#
#   powershell -File scripts/lanzar_linea.ps1 -Nombre serial `
#       -Arbol C:\Users\AlexDesk\Documents\forja-nodos `
#       -Variables "RAMA=extraccion-mundo-11 MODO_INSERCION=insertar ..." -Log /tmp/serial.log
#
# TERCER INTENTO, Y LOS DOS PRIMEROS FALLARON DE VERDAD:
#
#   1. `nohup ... &` desde el shell de la sesion de chat (22 sep, 00:03). Las dos lineas
#      murieron cuando la sesion se cerro: Windows se llevo su arbol de procesos entero.
#   2. WMI, `Win32_Process.Create` (23 sep, 06:25). El padre era el servicio WmiPrvSE,
#      pero CADA LINEA ABRIA SU PROPIA VENTANA DE CONSOLA, vacia porque la salida va al
#      log. El fundador las vio vacias y, cerradas o recicladas, las dos lineas murieron a
#      los 90 segundos. Una ventana que parece vacia y es la linea es una trampa.
#
# ESTE: una TAREA PROGRAMADA de Windows (la crea el servicio del programador, no esta
# sesion) que corre `wscript` con un .vbs que arranca el Git Bash con la ventana OCULTA
# (estilo 0) y sin esperarlo. Sin ventana que cerrar, y sin atadura a la sesion.
#
# PRIORIDAD BAJA (decision del fundador, 25 sep 2026). Lo primero que hace el envoltorio es
# bajarse a si mismo a BelowNormal (scripts/prioridad_baja.ps1, con su pid de Windows, que Git
# Bash da en /proc/$$/winpid), y solo despues arranca la orden: todo lo que cuelga de la linea
# nace BelowNormal por herencia. El resultado queda en <Log>.prioridad y este lanzador lo
# muestra. Con cinco barridos a la vez el equipo se trabo el 25 sep; con la prioridad baja,
# el que teclea va primero.
#
# EL PID QUE SE VIGILA es el del bash ENVOLTORIO en el espacio de Git Bash, escrito en
# <Log>.pid por el propio envoltorio. El envoltorio NO hace exec (lleva una orden detras)
# y por eso su pid dura lo que dura la linea. Se comprueba con `kill -0` desde Git Bash.
# Los pids de Windows no sirven: Git Bash cambia de proceso de Windows en cada exec.
param(
    [Parameter(Mandatory = $true)][string]$Nombre,
    [Parameter(Mandatory = $true)][string]$Arbol,
    [Parameter(Mandatory = $true)][string]$Variables,
    [Parameter(Mandatory = $true)][string]$Log,
    [string]$Orden = "bash orquestador_forja.sh"
)

$bash = "C:\Program Files\Git\usr\bin\bash.exe"
if (-not (Test-Path $bash)) { throw "no encuentro el Git Bash en $bash (y bash.exe a secas es el de WSL)" }

$unix = "/" + ($Arbol.Substring(0, 1).ToLower()) + ($Arbol.Substring(2) -replace '\\', '/')
$prioridad = ((Join-Path $PSScriptRoot "prioridad_baja.ps1") -replace '\\', '/')
& $bash -lc "rm -f '$Log.prioridad'"
$linea = "cd '$unix' && echo `$`$ > '$Log.pid' && powershell.exe -NoProfile -ExecutionPolicy Bypass -File '$prioridad' -Id `$(cat /proc/`$`$/winpid) > '$Log.prioridad' 2>&1; env $Variables $Orden > '$Log' 2>&1; echo FIN `$(date) >> '$Log'"

# el .vbs arranca el bash OCULTO (0) y no lo espera (False)
$vbs = Join-Path $env:TEMP "forja_lanzar_$Nombre.vbs"
$q = '""'
$vbsTexto = 'CreateObject("WScript.Shell").Run """' + $bash + '"" -lc ""' + ($linea -replace '"', $q) + '""", 0, False'
Set-Content -Path $vbs -Value $vbsTexto -Encoding ascii

$tarea = "forja_linea_$Nombre"
$accion = New-ScheduledTaskAction -Execute "wscript.exe" -Argument "//B //Nologo `"$vbs`""
$ajustes = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries `
    -ExecutionTimeLimit ([TimeSpan]::Zero) -MultipleInstances IgnoreNew
Register-ScheduledTask -TaskName $tarea -Action $accion -Settings $ajustes -Force | Out-Null
Start-ScheduledTask -TaskName $tarea
Write-Output "LANZADA por la tarea '$tarea', oculta, log $Log, pid en $Log.pid"

# la prioridad baja, comprobada: el envoltorio la escribe en <Log>.prioridad antes de arrancar la orden
$visto = ""
for ($i = 0; $i -lt 60 -and -not $visto; $i++) {
    Start-Sleep -Seconds 1
    $visto = (& $bash -lc "cat '$Log.prioridad' 2>/dev/null") -join " "
}
if ($visto -match "BelowNormal") { Write-Output "PRIORIDAD BAJA: $visto" }
else { Write-Output "AVISO: la prioridad baja no se confirmo en 60 s ($visto); bajala a mano" }
