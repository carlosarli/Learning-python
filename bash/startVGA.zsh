#!/bin/zsh
#
if  xrandr | grep -q 'VGA1 connected'; then

    xrandr --newmode "1440x900_60.00"  106.50  1440 1528 1672 1904  900 903 909 934 -hsync +vsync
    xrandr --addmode VGA1 1440x900_60.00
    xrandr --output VGA1 --mode 1440x900_60.00 --right-of LVDS1 --primary
else
    exit 1
fi
