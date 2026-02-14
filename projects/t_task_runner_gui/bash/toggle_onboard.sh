#!/bin/bash
# Toggles the visibility of the Onboard on-screen keyboard using D-Bus.
dbus-send --type=method_call --dest=org.onboard.Onboard /org/onboard/Onboard/Keyboard org.onboard.Onboard.Keyboard.ToggleVisible