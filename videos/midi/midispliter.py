import mido
import os
import sys
def divide_midi(file_path, num_files):
    # Load the MIDI file
    mid = mido.MidiFile(file_path)
    length = int(mid.length / num_files)

    for i in range(num_files):
        # Create a new MIDI file
        new_mid = mido.MidiFile()
        new_mid.ticks_per_beat = mid.ticks_per_beat

        # Copy the tracks from the original file
        for j, track in enumerate(mid.tracks):
            new_track = mido.MidiTrack()
            start = length * i
            end = length * (i + 1)
            new_track.extend(track[start:end])
            new_mid.tracks.append(new_track)

        # Save the new MIDI file
        filename, _ = os.path.splitext(file_path)
        new_file_path = f'{filename}_{i}.mid'
        new_mid.save(new_file_path)

# Example usage
divide_midi("test.mid", 4)

