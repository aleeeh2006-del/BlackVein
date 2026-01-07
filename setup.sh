#!/bin/bash
echo "Instalando Blackvein OSINT Engine..."
pkg update && pkg upgrade -y
pkg install python -y
pip install aiohttp colorama
chmod +x blackvein.py
echo "python ~/blackvein/blackvein.py" > $PREFIX/bin/blackvein
chmod +x $PREFIX/bin/blackvein
echo "Instalação concluída! Digite 'blackvein' para iniciar."

