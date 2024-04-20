import serial

def setup(port):
    return serial.Serial(port)

def update(s, state):
    l = s.readline().decode("ascii").replace("\r\n", "")
    if not l.startswith("^"): return state
    l = l[1:]
    ls = [i for i in l.split(";") if i]
    for val in ls:
        v = val.split(":")
        try: state[v[0]] = float(v[1])
        except:
            try: state[v[0]] = bool(v[1])
            except: state[v[0]] = v[1]
    return state

def unsetdown(s):
    s.close()
