def msr(file1):
    with open(file1, 'r') as f:
        notes = []
        times = []
        durations = []
        for line in f:
            line_elems = line.split(' ')
            time = line_elems[0]
            times.append(time)
            note = line_elems[1]
            notes.append(note)
            duration = line_elems[2]
            durations.append(duration)
        return times, notes, durations

msr('Androide.txt')