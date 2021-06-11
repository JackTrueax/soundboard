# functional variables:
audio_file_directory            = "audio_files"                             # the directory in which the audio files only are stored "C:/Users/user/audio_files" do not include a terminal "/"
default_turbo_delay_seconds     = .25                                       # the amount of time between sounds when turbo mode is active
input_device_name               = "CABLE Input (VB-Audio Virtual Cable)"    # you shouldn't need to change this, but it's the name of the playback device we will send the sound to
overlap_type                    = "interrupt_multi_channel"                 # overlap types: "play_to_completion_multi_channel", "interrupt_multi_channel", "interrupt_single_channel"

# aesthetics
window_title    = "soundboard"  # title at top of window\
theme           = "Material2"   # theme information: https://www.geeksforgeeks.org/themes-in-pysimplegui/ https://media.geeksforgeeks.org/wp-content/uploads/20200511200254/f19.jpg