# Script PowerShell para ejecutar todas las pruebas unitarias modularizadas
# Sistema SmartHome DAO - Suite de Pruebas

Write-Host "=================================================================" -ForegroundColor Cyan
Write-Host "    SUITE DE PRUEBAS UNITARIAS - SMARTHOME DAO (MODULARIZADAS)   " -ForegroundColor Cyan
Write-Host "=================================================================" -ForegroundColor Cyan
Write-Host ""

# Verificar que estamos en el directorio correcto
if (!(Test-Path "tests")) {
    Write-Host "❌ Error: Directorio 'tests' no encontrado" -ForegroundColor Red
    Write-Host "   Asegúrate de ejecutar este script desde el directorio raíz del proyecto" -ForegroundColor Yellow
    exit 1
}

Write-Host "📂 Directorio actual: $PWD" -ForegroundColor Green
Write-Host ""

# Opción 1: Ejecutar la suite completa
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host "OPCIÓN 1: Ejecutar TODAS las pruebas (Suite completa)" -ForegroundColor Yellow
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host ""
Write-Host "Ejecutando: python tests/run_all_tests.py" -ForegroundColor White
Write-Host ""

python tests/run_all_tests.py

$exitCode = $LASTEXITCODE

Write-Host ""
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host "OPCIÓN 2: Ejecutar pruebas modulares individuales" -ForegroundColor Yellow
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host ""
Write-Host "Puedes ejecutar módulos específicos con:" -ForegroundColor White
Write-Host ""
Write-Host "  • UsuarioDAO:           python -m unittest tests.test_usuario_dao -v" -ForegroundColor Gray
Write-Host "  • ViviendaDAO:          python -m unittest tests.test_vivienda_dao -v" -ForegroundColor Gray
Write-Host "  • DispositivoDAO:       python -m unittest tests.test_dispositivo_dao -v" -ForegroundColor Gray
Write-Host "  • EventoDispositivoDAO: python -m unittest tests.test_evento_dao -v" -ForegroundColor Gray
Write-Host "  • Encapsulación:        python -m unittest tests.test_dominio -v" -ForegroundColor Gray
Write-Host ""
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host "OPCIÓN 3: Ejecutar con descubrimiento automático" -ForegroundColor Yellow
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host ""
Write-Host "  python -m unittest discover -s tests -p 'test_*.py' -v" -ForegroundColor Gray
Write-Host ""
Write-Host "=================================================================" -ForegroundColor Cyan

# Retornar el código de salida de las pruebas
exit $exitCode
