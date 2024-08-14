#!/bin/bash

interface_ax = $1
interface_ac = $2
interface_usb = $3

function habilitar_todas_interfaces{
    sudo ifconfig ${interface_ax} up
    sudo ifconfig ${interface_ac} up
    sudo ifconfig ${interface_usb} up 
}

habilitar_todas_interfaces()