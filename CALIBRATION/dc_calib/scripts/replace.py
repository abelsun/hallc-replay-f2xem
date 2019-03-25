import string

with open("main_calib.C", "r") as file:
    line=file.read()
line = line.replace("SHMS", spect)

with open("main_calib.C", "r") as file:
    file.write(line)
