microphone soundboard

you need to download the audio driver from this link:
https://vb-audio.com/Cable/

1: extract and run vcable_setup
2. open control panel
    - select "Hardware and Sound"
    - select "Sound"
3: set your usual speakers/headphones as the default playback device
4: set your usual microphone as the default recording device
5: go to your usual microphone's properties
	- go to the listen tab
	- check "listen to this device"
	- change "Playback through this device" to "CABLE Input (VB-Audio Virtual Cable)" and apply
6: 
    - Any sound played through the "CABLE Input" playback device will be relayed to the "CABLE Output" recording device.
        - this app plays sound through this device
    - Any sound played through your usual microphone/recording device will also be relayed to the "CABLE Output" recording device
    - ^ this is why "CABLE Output" is the default microphone/recording device ^, it will take the place of your usual microphone

to test the soundboard:
    go to the "CABLE Output"'s properties and check "Listen to this device" through "Default Playback Device". you should hear your usual mic's output alongside the soundboard's output.


using the app
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