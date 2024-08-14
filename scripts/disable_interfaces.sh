#!/bin/bash

interface_ax="$1"
interface_ac="$2"
interface_usb="$3"
definicao="$4"

function desabilitar_IEEE_802_11b_g_n_only_2_4 {
    sudo ifconfig ${interface_ax} down
    sudo ifconfig ${interface_usb} down
#    echo "Rede AC Somente 2.4 Configurada"
}

function desabilitar_IEEE_802_11b_g_n_2_4_usb {
    sudo ifconfig ${interface_ax} down
    sudo ifconfig ${interface_ac} down
#    echo "Rede USB Configurada" 
}

function desabilitar_IEEE_802_11a_g_n_ac_2_4_plug {
    sudo ifconfig ${interface_ax} down
    sudo ifconfig ${interface_usb} down
#    echo "Rede AC 2.4 Plug Configurada"
}

function desabilitar_IEEE_802_11a_b_g_n_ac_2_4 {
    sudo ifconfig ${interface_ax} down
    sudo ifconfig ${interface_usb} down
#    echo "Rede AC 2.4 Configurada"
}

function desabilitar_IEEE_802_11a_b_g_n_ac_5g {
    sudo ifconfig ${interface_ax} down
    sudo ifconfig ${interface_usb} down
#    echo "Rede AC 5GHZ Configurada"
}

function desabilitar_IEEE_802_11a_b_g_n_ac_ax_5g {
    sudo ifconfig ${interface_ac} down
    sudo ifconfig ${interface_usb} down
#    echo "Rede AX 5Ghz Configurada"
}

case "$definicao" in 

    1)
    desabilitar_IEEE_802_11b_g_n_only_2_4
    ;;

    2)
    desabilitar_IEEE_802_11b_g_n_2_4_usb
    ;;

    3)
    desabilitar_IEEE_802_11a_g_n_ac_2_4_plug
    ;;

    4)
    desabilitar_IEEE_802_11a_b_g_n_ac_2_4
    ;;

    5)
    desabilitar_IEEE_802_11a_b_g_n_ac_5g
    ;;

    6)
    desabilitar_IEEE_802_11a_b_g_n_ac_ax_5g
    ;;

esac