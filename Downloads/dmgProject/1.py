from music21 import stream, note, chord, midi
from pydub import AudioSegment
import subprocess
import os

# Создание потока для мелодии
melody = stream.Stream()

# Добавление аккордов и нот
melody.append(chord.Chord(["C4", "E4", "G4"]))  # Cm
melody.append(note.Rest(quarterLength=1))
melody.append(chord.Chord(["G3", "B3", "D4"]))  # Gm
melody.append(note.Rest(quarterLength=1))
melody.append(chord.Chord(["Ab3", "C4", "Eb4"]))  # Ab
melody.append(note.Rest(quarterLength=1))
melody.append(chord.Chord(["Eb3", "G3", "Bb3"]))  # Eb
melody.append(note.Rest(quarterLength=1))
melody.append(chord.Chord(["F3", "Ab3", "C4"]))  # Fm
melody.append(note.Rest(quarterLength=1))
melody.append(chord.Chord(["Bb2", "D3", "F3"]))  # Bb

# Создание объекта MIDI
mf = midi.translate.music21ObjectToMidiFile(melody)

# Сохранение файла MIDI
midi_file = "Escapism_melody.mid"
mf.open(midi_file, 'wb')
mf.write()
mf.close()

# Конвертация MIDI в WAV
wav_file = "Escapism_melody.wav"
subprocess.call(['timidity', midi_file, '-Ow', '-o', wav_file])

# Загрузка WAV и конвертация в аудиофайл
audio = AudioSegment.from_wav(wav_file)

# Сохранение файла в формате MP3
mp3_file = "Escapism_melody.mp3"
audio.export(mp3_file, format="mp3")

# Удаление временных файлов
os.remove(midi_file)
os.remove(wav_file)

print("MP3 файл создан:", mp3_file)

