import os
import time
import mido
import sys

# Pemetaan not piano ke koordinat layar
note_coordinates = {
    'f1': (176, 720), 'f2': (377, 720), 'f3': (580, 720),
    'q': (256, 1000), '1': (340, 900), 'w': (400, 1000),
    '2': (459, 900), 'e': (542, 1000), 'r': (658, 1000),
    '3': (727, 900), 't': (791, 1000), '4': (852, 900),
    'y': (907, 1000), '5': (983, 900), 'u': (1042, 1000),
    'i': (1178, 1000), '6': (1250, 900), 'o': (1300, 1000), 
    '7': (1354, 900), 'p': (1438, 1000), '[': (1556, 1000), 
    '8': (1638, 900), ']': (1696, 1000), '9': (1775, 900),
    '\\': (1838, 1000), '0': (1900, 900), '-': (1956, 1000),
    '=': (2080, 1000)
}

def map_piano_note_to_key(note):
    piano_G = ['f1', 'f2', 'f3']
    piano_keymap = ['q', '1', 'w', '2', 'e', 'r', '3', 't', '4', 'y', '5',
                    'u', 'i', '6', 'o', '7', 'p', '[', '8', ']', '9', '\\', '0', '-', '=']
    if not (36 <= note <= 96):
        return '', ''

    if 36 <= note <= 59:
        change_G = piano_G[0]
        baseline = 36
    elif 60 <= note <= 83:
        change_G = piano_G[1]
        baseline = 60
    else:
        change_G = piano_G[2]
        baseline = 84

    key_index = note - baseline

    if 0 <= key_index < len(piano_keymap):
        return change_G, piano_keymap[key_index]

    return '', ''

def play_midi(path, pitch_modulation=10):
    midi = mido.MidiFile(path)
    print("Tekan Enter untuk mulai memainkan. Tekan Ctrl+C untuk berhenti.")
    input("Tekan Enter untuk memulai...")

    curr_pitch = 'f2'
    os.system(f"adb shell input tap {note_coordinates[curr_pitch][0]} {note_coordinates[curr_pitch][1]}")

    try:
        notes_to_play = []
        for msg in midi.play():
            if msg.type == 'note_on' and msg.velocity != 0:
                pitch, key = map_piano_note_to_key(msg.note + pitch_modulation)
                if pitch and pitch in note_coordinates and curr_pitch != pitch:
                    os.system(f"adb shell input tap {note_coordinates[pitch][0]} {note_coordinates[pitch][1]}")
                    curr_pitch = pitch
                if key and key in note_coordinates:
                    notes_to_play.append(note_coordinates[key])
                    print(f"Klik pada not di koordinat ({note_coordinates[key][0]}, {note_coordinates[key][1]})")

            if msg.time > 0:
                for coord in notes_to_play:
                    os.system(f"adb shell input tap {coord[0]} {coord[1]}")
                notes_to_play.clear()
                time.sleep(msg.time)  # Tambahkan waktu tidur berdasarkan waktu pesan MIDI

    except KeyboardInterrupt:
        print("Pemutaran dihentikan oleh pengguna.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python macro.py 'path'")
        sys.exit(1)

    midi_path = sys.argv[1]
    play_midi(midi_path, pitch_modulation=10)
