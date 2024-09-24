colors = ['\u001b[31m', '\u001b[31;1m', '\u001b[33m', '\u001b[32m', '\u001b[34m', '\u001b[36m', '\u001b[35m']

def text(text):
    pos = 0
    colchar = ""
    for char in text:
        colchar = colchar + colors[pos] + char
        if pos==6:
            pos=0
        else:
            pos += 1
    return colchar
