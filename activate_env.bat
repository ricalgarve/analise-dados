@echo off
echo ==========================================
echo Configurando ambiente virtual Python 3.11...
echo ==========================================

REM Cria o ambiente virtual com Python 3.11 se ainda nao existir
if not exist ".venv" (
    echo Criando ambiente virtual com Python 3.11 .venv...
    py -3.11 -m venv .venv
)

REM Ativa o ambiente virtual
call .venv\Scripts\activate.bat

REM Atualiza pip e instala dependencias
echo.
echo Instalando dependencias do requirements.txt...
python -m pip install --upgrade pip
pip install -r requirements.txt

echo.
echo ==========================================
echo Ambiente Python 3.11 pronto e ativado!
echo ==========================================
echo.
