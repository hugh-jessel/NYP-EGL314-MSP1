<h1 align="center">
  <img src="./Assets/NanyangPolyLogo.png" width = 350px height=170px>
</h1>

<h1 align="center">
  Project S.O.N.I.C - Reaction Training
</h1>

<p align="center">
  <i align="center">Train to be a ninja with the use of modern technologies </i>🥷
</p>

<p align="center">
  <a href="https://github.com/hugh-jessel/NYP-EGL314-MSP1/commits/main"><img src="https://img.shields.io/github/last-commit/hugh-jessel/NYP-EGL314-MSP1.svg?style=for-the-badge"/></a>
</p>

## Overview
Project S.O.N.I.C (Sensory Observation Ninja Immersive Challenge) is an experiential/exploratory initiative designed to blend the ancient "ninja training techniques" with modern technologies. Students are to design a range of interactive stations that simulate ninja training scenarios, designed to test and enhance your listening abilities, reaction times and strategic thinking. The stations include:
1. Stealth Walking
2. The Blindfold Challenge
3. Art Of Hearing
4. **Reaction Training**
5. Memory Sequence
6. Graduation Sequence
<p>
  In this repository, the focus will be strictly on Station 4 - Reaction Training.
</p>

## Station 4 - Reaction Training
Reaction Training challenges you to respond swiftly and accurately to sudden cues (e.g Auditory, Visual). Testing the participants' ability to process information quickly and react most effectively.

<details open>
<summary>
  Features
</summary>
<ul>
  <li>L-ISA to create a soundscape of incoming projectiles.</li>
  <li>Players are to touch/press buttons with the correct direction.</li>
  <li>Station to measure accuracy and reaction time, best result wins!</li>
</ul>
</details>

## Dependencies
The codes in this repository had been made using **Python 3.9 or higher**.

## Pre-Requisites
1. Reaper DAW - Click [Here](https://www.reaper.fm/download.php)
2. L-ISA Studio - Click [Here](https://www.l-acoustics.com/products/l-isa-studio/#)
3. loopMIDI - Click [Here](https://www.tobias-erichsen.de/software/loopmidi.html)

## Setting Up
1. Update your Raspberry Pi
   
   ```
   sudo apt update
   sudo apt upgrade
   ```
   
   If update and/or upgrade is unsuccesful, manually set the date and time by
   
   ```
   sudo date -s 'YYYY-MM-DD HH:MM:SS"
   ```
2. Setting up Virtual Environment
   
   To install Virtual Environment

   ```
   sudo apt install virtualenv python3-virtualenv -y
   ```
   To create a new virtual environment

   ```
   virtualenv -p /usr/bin/python3 <environment_name>
   ```
   **THE VIRUTAL ENVIRONMENT IS A FOLDER**
   
   To activate the virtual environment

   ```
   source <environment_folder>/bin/activate
   ```
   To install a package

   ```
   pip3 install python-osc
   ```
   To deactivate environment
   
   ```
   deactivate
   ```
   
## Tutorials
- **[Backlog 1 Sprint 1](./Backlog1%20Sprint1/B1S1.md)** - OSC Installation on Raspberry Pi, Creation of a UI via tkinter, OSC Communication to various devices
- **[Backlog 1 Sprint 2](./Backlog%201%20Sprint2/B1S2.md)** - Configuration and usage of lasers and relay module.
- **[Backlog 2 Sprint 1](./Backlog%202%20Sprint1/B2S1.md)** - Raspberry Pi to Reaper DAW via OSC, Reaper DAW to L-ISA Controller via MTC
- **[Backlog 2 Sprint 2](./Backlog%202%20Sprint2/B2S2.md)** - Configuring of LaunchPad, LaunchPad MIDI to Raspberry Pi, MIDI to Reaper DAW, Foundation code for Reaction Training Game
- **[Proof Of Concept](./POC/README.md)** - All the resources needed to trial run the game for the Proof Of Concept Demonstration
- **[Backlog 3 Sprint 1](./Backlog3%Sprint1/B3S1.md)** - Configurating and usage of lasers and relay modules for 12 different speakers.
- **[Backlog 3 Sprint 2](./Backlog3%sprint2/B3S2.md)** - Ensuring full length of the game being made.
- **[Minimum Viable Product](./MVP/README.md)** - All the resources needed to reach a stage where the game is viable for the Minimum Viable Product Demonstration.
- **[Final Demonstration](./Final-Demonstration/README.md)** - All the resources to reach a stage where the game is fully complete and able to be showcased.

## References
- **[Huats Club - rpistarterkit](https://github.com/huats-club/rpistarterkit)** - Getting started on configuring your Raspberry Pi
- **[Huats Club - oscstarterkit](https://github.com/huats-club/oscstarterkit)** - Getting started on using Python Open Sound Control
- **[Huats Club - mts_sensor_cookbook](https://github.com/huats-club/mts_sensor_cookbook)** - Foundation codes on common sensors
  
## Contributors
[//]: contributor-faces
<a href="https://github.com/hugh-jessel"><img src="https://avatars.githubusercontent.com/u/167043880?v=4" title="hugh-jessel" width="50" height="50"></a>
<a href="https://github.com/Anestesiaa-0512"><img src="https://avatars.githubusercontent.com/u/87161335?v=4" title="Anestesiaa-0512" width="50" height="50"></a>
<a href="https://github.com/isaacgsm"><img src="https://avatars.githubusercontent.com/u/106132526?v=4" title="isaacgsm" width="50" height="50"></a>
<a href="https://github.com/FinnishAnya"><img src="https://avatars.githubusercontent.com/u/167286639?v=4" title="FinnishAnya" width="50" height="50"></a>
