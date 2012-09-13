#!/bin/zsh
#batteryallarm
while true; do
    if acpi | grep 'Discharging, [4-9]%'; then
       dialog --no-shadow --msgbox "Batteria quasi scarica." 5 40
       mplayer -ao alsa -really-quiet /home/bow/music/vivaldi_alert.mp3
    elif acpi | grep 'Discharging, [1-3]%'; then
       mplayer /home/bow/music/music_windows/Slipknot/Slipknot/15\ Slipknot\ -\ Get\ This.flac
       if dialog --no-shadow --yesno "Battera scarica. Shut, plug or pray. \nShut Down ?" 7 45; then
          halt
       fi
    elif acpi | grep 'Discharging, 0%'; then
         dialog --no-shadow --infobox "Me spengo. \ncaricame, prima de riaccenderme, stronzo" 5 60
        halt
    fi
    sleep 1m 
done
