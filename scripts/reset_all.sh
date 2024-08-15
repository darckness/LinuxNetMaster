#!/bin/bash

config_file="scripts/configuracoes.txt"

interface_ac=$(grep "Interface AC:" "$config_file" | cut -d':' -f2 | xargs)
interface_ax=$(grep "Interface AX:" "$config_file" | cut -d':' -f2 | xargs)
interface_usb=$(grep "Interface USB:" "$config_file" | cut -d':' -f2 | xargs)
interface_lan=$(grep "Interface LAN:" "$config_file" | cut -d':' -f2 | xargs)

# Definição passada como argumento
definicao="$1"

function habilitar_todas_interfaces {
    sudo ifconfig ${interface_ax} up
    sudo ifconfig ${interface_ac} up
    sudo ifconfig ${interface_usb} up 
}

function caso_plug {
    sudo ifconfig ${interface_ax} up
    sudo ifconfig ${interface_ac} up
    sudo ifconfig ${interface_usb} up
    sudo ip netns exec lan ip link set ${interface_lan} netns 1
    sudo ip -all netns delete
}

if ["$definicao" -eq 3]; then
    caso_plug
else
    habilitar_todas_interfaces
fi