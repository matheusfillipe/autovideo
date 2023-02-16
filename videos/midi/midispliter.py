import mido
from mido.midifiles import merge_tracks
import os

def divide_midi(file_path, num_files):
    # Load the MIDI file
    mid = mido.MidiFile(file_path)
    # length in ticks
    length = int(sum(msg.time for msg in merge_tracks(mid.tracks)) / num_files) 

    # Create generators for the tracks
    track_generators = [iter(track) for track in mid.tracks]

    for i in range(num_files):
        # Create a new MIDI file
        new_mid = mido.MidiFile()
        new_mid.ticks_per_beat = mid.ticks_per_beat

        # Copy the tracks from the original file
        for track in track_generators:
            new_track = mido.MidiTrack()
            track_length = 0

            # Copy the messages from the original track until the length is reached
            # TODO handle unclosed note_on's and similar
            for msg in track:
                new_track.append(msg)
                track_length += msg.time
                if track_length >= length:
                    print(f'Length of track {i} is {track_length} ticks')
                    break

            new_mid.tracks.append(new_track)

        # Save the new MIDI file
        filename, _ = os.path.splitext(file_path)
        new_file_path = f'{filename}_{i}.mid'
        new_mid.save(new_file_path)

# Example usage
divide_midi("test.mid", 4)

