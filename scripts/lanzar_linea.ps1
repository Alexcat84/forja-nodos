# LANZA UNA LINEA DEL ARNES FUERA DEL ARBOL DE PROCESOS DE QUIEN LA LANZA (23 sep 2026).
#
#   powershell -File scripts/lanzar_linea.ps1 -Arbol C:\Users\AlexDesk\Documents\forja-nodos `
#       -Variables "RAMA=extraccion-mundo-11 MODO_INSERCION=insertar ..." -Log /tmp/serial.log
#
# POR QUE EXISTE. El 22 sep a las 00:03 las dos lineas se lanzaron con
# `nohup ... &` desde el shell de la sesion de chat, y MURIERON CON ELLA: al cerrarse
# la sesion, Windows se llevo su arbol de procesos entero, y nohup no protege de eso.
# La serial murio en plena fase ciega, con cuatro ficheros apartados a un directorio
# temporal; Marquet, a mitad del turno de su extractor. Ninguna escribio PARA_ALEXIS,
# porque no pararon: las mataron.
#
# COMO LO EVITA. El proceso se crea A TRAVES DE WMI (Win32_Process.Create), asi que su
# padre es el servicio WmiPrvSE y no el shell que lo pidio. Sobrevive a la sesion que
# lo lanzo. Comprobado el 23 sep: padre WmiPrvSE, el Git Bash de verdad (no el
# C:\WINDOWS\system32\bash.exe, que es el de WSL y corre en otro mundo), el claude del
# PATH en su version nueva, y el mismo /tmp.
#
# Escribe el pid de WINDOWS del bash en <Log>.pid, que es el que entiende tasklist.
param(
    [Parameter(Mandatory = $true)][string]$Arbol,
    [Parameter(Mandatory = $true)][string]$Variables,
    [Parameter(Mandatory = $true)][string]$Log
)

$bash = "C:\Program Files\Git\usr\bin\bash.exe"
if (-not (Test-Path $bash)) { throw "no encuentro el Git Bash en $bash" }

$unix = "/" + ($Arbol.Substring(0, 1).ToLower()) + ($Arbol.Substring(2) -replace '\\', '/')
$linea = "cd '$unix' && env $Variables bash orquestador_forja.sh > '$Log' 2>&1"
$cmd = "`"$bash`" -lc `"$linea`""

$r = Invoke-CimMethod -ClassName Win32_Process -MethodName Create `
    -Arguments @{ CommandLine = $cmd; CurrentDirectory = $Arbol }
if ($r.ReturnValue -ne 0) { throw "Win32_Process.Create devolvio $($r.ReturnValue)" }

$padre = (Get-CimInstance Win32_Process -Filter "ProcessId = $($r.ProcessId)").ParentProcessId
$nombre = (Get-Process -Id $padre -ErrorAction SilentlyContinue).ProcessName
Write-Output "LANZADA: pid $($r.ProcessId), padre $padre ($nombre), log $Log"

$pidUnix = $Log + ".pid"
$pidWin = (& $bash -lc "cygpath -w '$pidUnix'").Trim()
Set-Content -Path $pidWin -Value $r.ProcessId -Encoding ascii
