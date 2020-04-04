import winsound
frquency=32767
duration=10000000

winsound.Beep(frquency,duration)

def sos():
    for i in range(0,3):
        winsound.Beep(5500,100)
        for i in range(0,3):
            winsound.Beep(5500,400)
            for i in range(0, 3):
                winsound.Beep(5500, 100)

sos()
