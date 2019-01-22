import wave
import numpy
import math

inFileName = "data/pingpong.wav"
outFileName = 'data/pingpong1000.csv'
outDataRate = 1000      # points per second

with wave.open(inFileName, 'rb') as f:
    WAVparams = f.getparams()
    s01 = "There are " + repr(WAVparams.nframes) + " frames."
    print(s01)

    bytesData = f.readframes(WAVparams.nframes)

WAVdata = numpy.frombuffer(bytesData, dtype=numpy.dtype('i2'))  # answer is an ndarray

i = 0
tPerFrame = 1000.0 / outDataRate    # milliseconds per frame

with open(outFileName, 'w') as out:

    out.write('time, sound\n')

    iStart = 0
    tStart = 0
    dataEndTime = WAVparams.nframes * 1000 / WAVparams.framerate    # milliseconds

    while tStart < dataEndTime:
        tEnd = tStart + tPerFrame
        iEnd = math.ceil(tEnd / 1000.00 * WAVparams.framerate)
        if iEnd > WAVparams.nframes:
            iEnd = WAVparams.nframes
        theMean = numpy.mean(WAVdata[iStart:iEnd])  # could use std() instead of mean()

        theLine = '{:g}, {:g}\n'.format(tStart, theMean)
        out.write(theLine)

        tStart = tEnd
        iStart = iEnd
        i += 1

message = "Wrote {} lines to {}".format(i, outFileName)
print(message)
