#!/bin/bash

echo "Begin..."
sudo apt-get update

# for Qt:
sudo apt-get --yes install libxkbcommon-x11-0
sudo apt-get --yes install libsm6 libxext6 ffmpeg libfontconfig1 libxrender1 libgl1-mesa-glx libgl1-mesa-dev
sudo apt-get --yes install libxdamage1

# for wxPython:
sudo apt-get --yes install libgtk-3-dev libgstreamer-plugins-base1.0-dev

# for Tkinter:
sudo apt-get --yes install python3-tk idle3

echo "Done."
