#!/bin/sh
MSG="${*:-Hello from Docker}"
figlet "$MSG" | lolcat -f
cowsay "$MSG" | lolcat -f
fortune | cowsay | lolcat -f
