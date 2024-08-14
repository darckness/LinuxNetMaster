#!/bin/bash

interface_ac=$(grep "Interface AC:" "$config_file" | cut -d':' -f2 | xargs)
interface_ax=$(grep "Interface AX:" "$config_file" | cut -d':' -f2 | xargs)
interface_usb=$(grep "Interface USB:" "$config_file" | cut -d':' -f2 | xargs)

function habilitar_todas_interfaces{
    sudo ifconfig ${interface_ax} up
    sudo ifconfig ${interface_ac} up
    sudo ifconfig ${interface_usb} up 
}

habilitar_todas_interfaces()