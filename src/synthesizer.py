import music_sheet_reader
import note_frequency

class Synthesizer:
    def __init__(self, file1):
        self.notes = note_frequency.note_frequency
        self.file1 = file1

    def translate(self):
        times, notes, durations = music_sheet_reader.msr(self.file1)
        frequencies = []
        for note in notes:
            frequency = self.notes(note)
            frequencies.append(frequency)
        return frequencies
        
