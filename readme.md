# microphone soundboard

## setup
you need to download the audio driver from this link:
https://vb-audio.com/Cable/

1. extract and run vcable_setup

<img src="pictures/vcable_files.png" title="vcable files" width="35%" height="35%" />
<!-- ![](pictures/vcable_files.png) -->


2. open control panel
    - select "Hardware and Sound"
    - select "Sound"

<img src="pictures/control_panel.png" title="playback devices" width="35%" height="35%" />
<img src="pictures/control_panel_sound.png" title="playback devices" width="35%" height="35%" />


3. set your usual speakers/headphones as the default playback device

<img src="pictures/playback_default.png" title="playback devices" width="35%" height="35%" />
<!-- ![](pictures/playback_default.png) -->

4. set CABLE Output as the default recording device
5. go to your usual microphone's properties
	- go to the listen tab
	- check "listen to this device"
	- change "Playback through this device" from "Default Playback Device" to "CABLE Input (VB-Audio Virtual Cable)" and apply

<img src="pictures/recording_default.png" title="recording devices and listen to this device" width="60%" height="60%" />
<!-- ![](pictures/recording_default.png) -->

6.
    - ***Any sound played through the "CABLE Input" playback device will be relayed to the "CABLE Output" recording device.***
        - this app plays sound through this device
    - ***Any sound played through your usual microphone/recording device will also be relayed to the "CABLE Output" recording device***
    - ^ this is why ***CABLE Output*** is the default microphone/recording device ^, it will take the place of your usual microphone

***to test the soundboard:***
    go to the "CABLE Output"'s properties and check "Listen to this device" through "Default Playback Device". you should hear your usual mic's output alongside the soundboard's output.

 <img src="pictures/listen_test.png" title="CABLE Output > Listen to this device" width="60%" height="60%" />

---

# using the app
<!-- <img src="pictures/app.png" title="recording devices and listen to this device" width="35%" height="35%" /> -->
![](pictures/app.png)

there are 3 main inputs:
- sound buttons
- turbo mode
    - turbo button
        - press it once to activate turbo mode
        - press any of the audio files to repeat the sound until turbo is pressed again
        - you can change which sound to repeat while turbo mode is active
    - turbo slider
        - the vertical slider on the right side represents the period of the repeating sound, in seconds

by default sounds will overlap (up to 8 sounds at a time) before interrupting a currently playing sound