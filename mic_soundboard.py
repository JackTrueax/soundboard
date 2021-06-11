import PySimpleGUI as sg
import pyglet
import os
import time
from pygame import mixer
import config

class Soundboard():
    # >>> from pygame._sdl2 import get_num_audio_devices, get_audio_device_name                     # Get playback device names
    # >>> mixer.init()                                                                              # Initialize the mixer, this will allow the next command to work
    # >>> print( [get_audio_device_name(x, 0).decode() for x in range(get_num_audio_devices(0))] )  # Returns playback devices
    # ['Headphones (Oculus Virtual Audio Device)', 'MONITOR (2- NVIDIA High Definition Audio)', 'Speakers (High Definition Audio Device)', 'Speakers (NVIDIA RTX Voice)', 'CABLE Input (VB-Audio Virtual Cable)']
    # >>> mixer.quit()                                                                              # Quit the mixer as it's initialized on your main playback device
    
    def __init__(self, window_title="soundboard", sounds_folder="audio_files" , device_name="CABLE Input (VB-Audio Virtual Cable)", turbo_delay_secs=.25, theme="Black"):
        mixer.init(devicename=device_name)                  # Initialize it with the correct device
        self.folder_prefix = sounds_folder
        self.sound_names = os.listdir(self.folder_prefix)
        self.sounds_played = 0
        self.turbo_delay_secs = turbo_delay_secs
        sg.theme(theme)
        self.layout_creator()                               # generate layout
        self.window = sg.Window(window_title, self.layout)  # Create the window

    def play_sound(self, file_name, overlap_type = "interrupt_multi_channel"):
        # overlap types: "play_to_completion_multi_channel", "interrupt_multi_channel", "interrupt_single_channel"
        full_path = f'{self.folder_prefix}/{file_name}'
        empty_channel = mixer.find_channel() # find an unused audio channel
        if empty_channel and overlap_type != "interrupt_single_channel":
            s = mixer.Sound(full_path)  # load sound
            empty_channel.play(s)       # play sound on free channel
            self.sounds_played += 1
            print(f'playing {file_name} - sounds_played = {self.sounds_played}')
        elif overlap_type in {"interrupt_single_channel", "interrupt_multi_channel"}:
            mixer.music.load(full_path) # load sound
            mixer.music.play()          # play sound on unavailable channel
            self.sounds_played += 1
            print(f'playing {file_name} - sounds_played = {self.sounds_played}')

    # window setup
    def layout_creator(self):
        column_height = 30
        self.layout = [[]]  # , sg.Text(key='txtbox')]]

        num_columns = (len(self.sound_names)//column_height) +1
        for column_index in range(num_columns -1):
            column = []
            for file_name in self.sound_names[column_index*column_height : (column_index+1)*column_height]:
                column.append([sg.Button(file_name)])
            self.layout[0].append(sg.Column(column))
        column = []
        for file_name in self.sound_names[(num_columns-1)*column_height:]:
            column.append([sg.Button(file_name)])
        self.layout[0].append(sg.Column(column))
        self.layout[0].append(sg.Slider(range=(0,1), default_value=self.turbo_delay_secs, resolution=.01))
        self.layout[0].append([sg.Button(f'turbo')])
        # self.layout[0].append(sg.VSeperator()) # vertical seperator line

# sb = Soundboard(window_title, sounds_folder, device_name, turbo_delay_secs, theme)
sb = Soundboard(config.window_title, config.audio_file_directory, config.input_device_name, config.default_turbo_delay_seconds, config.theme)

# event loop
overlap_type = config.overlap_type
while True:
    event, values = sb.window.read()
    if event:
        if event == "turbo":
            print(f"turbo delay = {sb.turbo_delay_secs} seconds")
            repeat_loop = True

            while True: # wait for turbo event
                event, values = sb.window.read()
                if event == sg.WIN_CLOSED or event == "turbo":
                    repeat_loop = False
                    break
                if event:
                    sb.turbo_delay_secs = values[0]
                    repeat_sound = event
                    break
            
            start_time = time.perf_counter()
            while repeat_loop: # repeater loop

                current_time = time.perf_counter()
                time_elapsed = current_time - start_time
                if time_elapsed >= sb.turbo_delay_secs:
                    sb.play_sound(repeat_sound, overlap_type)
                    start_time = time.perf_counter()

                event, values = sb.window.read(timeout=1)
                if event == sg.WIN_CLOSED or event == "turbo":
                        break
                elif event != sg.TIMEOUT_EVENT:
                    repeat_sound = event
                sb.turbo_delay_secs = values[0]
        else:
            sb.play_sound(event, overlap_type)
    if event == sg.WIN_CLOSED:
        break

sb.window.close()