<h1 align="center">
  Proof Of Concept
</h1>

<p align="center">
  <i align="center">All the resources required to show a Proof Of Concept </i>😨
</p>

## Overview
This repository contains all the notable assets, codes and others for our Proof Of Concept in Week 8 that covers Station 4 - Reaction Training.

In the Proof Of Concept, we will be using a Master Station, shared with the other teams. In which in the venue, there are 12 Speakers and the participant will be standing in the middle of the room to play their game.

For the Proof Of Concept, the demonstration will only last a stage long (e.g. The Tutorial Stage) to make it swift, short and simple.

## Hardware & Software Setup
```mermaid
graph LR
B[GrandMA3] --SACN--> C[Moving Heads]
D[LaunchPad] --USB C--> E[Raspberry Pi 1]
E --WiFi --> B
E --WiFi--> F[Reaper DAW]
F --DANTE VSC--> G[LISA Processor]
G --Meta Data--> H[LISA Controller]
H --DANTE--> I[Yamaha QL1]
I --DANTE--> J[Amplifier]
J --Spk Cable--> K[Speakers]
```
To setup the hardware and software connections, please read through the following:
1. **[Backlog 1 Sprint 1](NYP-EGL314-MSP1/Backlog1%20Sprint1/B1S1.md)** - Base foundation on controlling the GrandMA3
2. **[Backlog 2 Sprint 1](NYP-EGL314-MSP1/Backlog%202%20Sprint1/B2S1.md)** - Configuring L-ISA Studio and Reaper DAW for OSC and MTC control
3. **[Backlog 2 Sprint 2](NYP-EGL314-MSP1/Backlog%202%20Sprint2/B2S2.md)** - Configuring a LaunchPad, sending MIDI commands to Reaper DAW, L-ISA Controller and GrandMA3

## Assets
Here, are all the varying assets used for the POC. This includes:
1. **[Digital Posters](./Assets/Poster)** - Includes a GIF and JPG version of the Digital Poster
2. **[Audio Assets](./Assets/Audio%20Assets)** - Includes a Master Reaper File, a Master L-ISA Controller File and the varying audio assets.
3. **[GrandMA3](./Assets/GrandMA3)** - Includes a Master GrandMA3 file (With lights and IP addresses patched.)

## Code Files
In this folder, there are 5 python files, in which all are needed to run this one stage for the demonstration.
1. **[gui.py](./Codes/gui.py)** - A GUI to control functions of GrandMA3 and L-ISA Controller.
2. **[osc_client_Grandma3.py](./Codes/osc_client_Grandma3.py)** - A file containing functions for different features that can be controlled and will happen with the lights. These include - Off, Pause and Sequences.
3. **[osc_client_LISA.py](./Codes/osc_client_LISA.py)** - A file containing the controls to trigger varying snaps, for the POC, it will only be for snapshots 1 - 4.
4. **[StartGame.py](./Codes/StartGame.py)** - The main file that is to be ran. In which, pressing the start on the LaunchPad will run the game by calling midi.py
5. **[midi.py](./Codes/midi.py)** - The in-depth game file that includes marker jumping, counter before projectile hits the player and dictates if the stage is passed, if the player failed the stage etc.
6. **[play_stop(1).py](./Codes/play_stop(1).py)** - This file has the command to play and stop the Reaper DAW playback.
7. **[reaper_markers.py](./Codes/reaper_markers.py)** - This file has the command to jump to various markers that are already present in the Reaper DAW.

<details><summary><b>The Specifics</b></summary>
  
  1. **[gui.py](./Codes/gui.py)**
  
  In [gui.py](./Codes/gui.py), there are 2 pages. One for L-ISA Controller and the other for GrandMA3. 
  
  For the L-ISA Controller page, it is calling functions from [osc_client_LISA.py](./Codes/osc_client_LISA.py) where it's firing various snapshots. As said earlier, the snapshots that can be called in [gui.py](./Codes/gui.py) range from snapshots 1-4.

  For the GrandMA3 page, it is calling functions from [osc_client_Grandma3.py](./Codes/osc_client_Grandma3.py) where it's able to execute various sequences to be used and being able to turn off all sequences being carried out.

  2. **[osc_client_Grandma3.py](./Codes/osc_client_Grandma3.py)**

     In **[osc_client_Grandma3.py](./Codes/osc_client_Grandma3.py)** you will have to adjust the IP address and Port number to that of your GrandMA3 console. This can be found on line 18 and 19:
     
     ```
     # FOR INFO: IP address and port of the receiving Raspberry Pi
     PI_A_ADDR = "192.168.254.137"		# ip of GrandMA3 ras pi (When swapping network please check) Line 18
     PORT = 23                        # Line 19
     addr = "/print"
     ```

     Following this, there are multiple functions that include:
     - Executing the various sequences
     - Pausing
     - Oops
     - Everything Off
    
     Which all can be called via the GUI and also called during the gameplay.

  3. **[osc_client_LISA.py](./Codes/osc_client_LISA.py)**

     In **[osc_client_LISA.py](./Codes/osc_client_LISA.py)**, you will also have to adjust the IP address and ensure that the Port Number is 8880 (L-ISA receives on this port) to that of your device running L-ISA Controller at line 35.

     ```
     # FOR INFO: IP address and port of the receiving Raspberry Pi

     PI_A_ADDR = "192.168.254.30"		# ip of L-ISA controller(When swapping network please check) Line 35

     PORT = 8880
     ```
     Following this, you will be able to fire snapshots from 1 to 4. If you choose to uncomment snapshots 1 to 10, then it will be able to fire snapshots 1 to 10.
  
</details>
