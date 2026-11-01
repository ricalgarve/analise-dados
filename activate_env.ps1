Write-Host "=========================================="
Write-Host "Configurando ambiente virtual Python 3.11..."
Write-Host "=========================================="

if (-not (Test-Path ".venv")) {
    Write-Host "Criando ambiente virtual com Python 3.11..."
    py -3.11 -m venv .venv
}

Write-Host "Ativando ambiente virtual..."
& .\.venv\Scripts\Activate.ps1

Write-Host "`nInstalando dependencias do requirements.txt..."
python -m pip install --upgrade pip
pip install -r requirements.txt

Write-Host "`n=========================================="
Write-Host "Ambiente Python 3.11 pronto e ativado!"
Write-Host "=========================================="
