#!/bin/bash

if [ "$EUID" -ne 0 ]; then
  echo "Proszę uruchomić ten skrypt z uprawnieniami administratora (root)."
  echo "Użyj: sudo ./install.sh"
  exit 1
fi

SCRIPT_NAME="hypaper"
SCRIPT_PATH="/usr/bin/$SCRIPT_NAME"
USER_HOME=$(eval echo ~${SUDO_USER})

cd src/

# Kopiowanie skryptu do /usr/local/bin
echo "Copying script to: $SCRIPT_PATH"
cp main.py "$SCRIPT_PATH"
chmod 755 "$SCRIPT_PATH"

# Nadanie skryptowi praw do wykonywania
echo "Making script executable: $SCRIPT_PATH"
chmod +x "$SCRIPT_PATH"

echo "Installation complete."
