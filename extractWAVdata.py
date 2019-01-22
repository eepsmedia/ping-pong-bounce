import wave
import numpy

inFileName = "data/pingpong.wav"
outFileName = 'data/pingpong raw redux.csv'

f = wave.open(inFileName, 'rb')
params = f.getparams()

print("There are {} frames.".format(params.nframes))

bytesData = f.readframes(params.nframes)
f.close()

a = numpy.frombuffer(bytesData, dtype = numpy.dtype('i2')) # answer is an ndarray

i = 0

with open(outFileName, 'w') as out:

    out.write('time, sound\n')

    i = 0
    for val in a:
        time = 1000 * i / params.framerate  # milliseconds
        theLine = '{:g}, {:g}\n'.format(time, val)
        out.write(theLine)
        i += 1

print("Wrote {} frames.".format(i))
