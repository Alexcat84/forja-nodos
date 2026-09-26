# BAJA A PRIORIDAD BAJA (BelowNormal) EL PROCESO DE WINDOWS QUE SE LE PASA (decision del fundador, 25 sep 2026).
#
# Lo llama el envoltorio bash de cada linea (scripts/lanzar_linea.ps1) con su propio pid de Windows,
# ANTES de arrancar el orquestador: todo lo que el envoltorio lance despues (extractor, auditor,
# barridos, aduanas y los procesos del reparto) HEREDA la prioridad baja, porque en Windows un hijo
# de un padre BelowNormal nace BelowNormal. Asi la maquina sigue respondiendo con la serial en marcha.
#
#   powershell -NoProfile -File scripts/prioridad_baja.ps1 -Id <pid de Windows>
param([Parameter(Mandatory = $true)][int]$Id)

$proceso = Get-Process -Id $Id -ErrorAction Stop
$proceso.PriorityClass = [System.Diagnostics.ProcessPriorityClass]::BelowNormal
$proceso.Refresh()
Write-Output ("prioridad del envoltorio (pid de Windows {0}): {1}" -f $Id, $proceso.PriorityClass)
if ($proceso.PriorityClass -ne [System.Diagnostics.ProcessPriorityClass]::BelowNormal) { exit 1 }
