import aifc
import wave
import numpy

inFile = "pingpong.wav"
f = wave.open(inFile, 'rb')
params = f.getparams()
s01 = "There are " + repr(params.nframes) + " frames."
print(s01)

bytesData = f.readframes(params.nframes)
f.close()

a = numpy.frombuffer(bytesData, dtype = numpy.dtype('i2')) # answer is an ndarray

i = 0

outFileName = 'pingpong raw.csv'

with open(outFileName, 'w') as out:

    out.write('time, sound\n')

    i = 0
    for val in a:
        time = 1000 * i / params.framerate  # milliseconds
        theLine = '{:g}, {:g}\n'.format(time, val)
        out.write(theLine)
        i += 1



