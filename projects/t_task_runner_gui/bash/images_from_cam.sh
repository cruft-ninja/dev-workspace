#!/bin/sh
# Transfers images from a Canon Digital Camera to the local Pictures/W directory.
# This script relies on the gvfs mount being active for the camera.
mv -v /run/user/1000/gvfs/gphoto2:host=Canon_Inc._Canon_Digital_Camera_9F65452D82504A4987BA451E77B95025/DCIM/* /home/ninja/Pictures/W