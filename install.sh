#!/bin/bash

if [ "$EUID" -ne 0 ]; then
  echo "Proszę uruchomić ten skrypt z uprawnieniami administratora (root)."
  echo "Użyj: sudo ./install.sh"
  exit 1
fi

SCRIPT_NAME="hypaper"
SCRIPT_PATH="/usr/local/bin/$SCRIPT_NAME"
USER_HOME=$(eval echo ~${SUDO_USER})
DATA_DIR="$USER_HOME/.config/$SCRIPT_NAME"
DATA_PATH="$DATA_DIR/data.json"

cd scr/
# Create the data directory if it doesn't exist
e# Tworzenie katalogu na dane, jeśli nie istnieje
echo "Creating data directory: $DATA_DIR"
mkdir -p "$DATA_DIR"
chown $SUDO_USER:$SUDO_USER "$DATA_DIR"
chmod 755 "$DATA_DIR"

# Kopiowanie skryptu do /usr/local/bin
echo "Copying script to: $SCRIPT_PATH"
cp plugin_test.py "$SCRIPT_PATH"
chmod 755 "$SCRIPT_PATH"

# Kopiowanie pliku danych do katalogu użytkownika
echo "Copying data file to: $DATA_PATH"
cp data.json "$DATA_PATH"
chown $SUDO_USER:$SUDO_USER "$DATA_PATH"
chmod 644 "$DATA_PATH"

# Nadanie skryptowi praw do wykonywania
echo "Making script executable: $SCRIPT_PATH"
chmod +x "$SCRIPT_PATH"

echo "Installation complete."
