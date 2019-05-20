import wave
import numpy
import math

inFileName = "../data/pingpong.wav"
outFileName = '../data/pingpong1000both.csv'   # change to whatever you want
outDataRate = 1000      # points per second

# read in the raw .wav file
# NOTE THAT THIS MUST BE MONAURAL!!

with wave.open(inFileName, 'rb') as f:
    WAVparams = f.getparams()
    s01 = "There are " + repr(WAVparams.nframes) + " frames."
    print(s01)

    bytesData = f.readframes(WAVparams.nframes)

WAVdata = numpy.frombuffer(bytesData, dtype=numpy.dtype('i2'))  # answer is an ndarray

i = 0
tPerFrame = 1000.0 / outDataRate    # milliseconds per frame

with open(outFileName, 'w') as out:

# write the first line to the .csv. Has variable names.
    out.write('time, wave, vol\n')   # if you only want one value (mean or SD or...) change this

# now write the rest!
# we want to aggregate the data in chunks until we've come to the end.

    iStart = 0   # the INDEX of the start of the current chunk
    tStart = 0   # the start time of the range for the current chunk
    dataEndTime = WAVparams.nframes * 1000 / WAVparams.framerate    # milliseconds

    while tStart < dataEndTime:
        tEnd = tStart + tPerFrame   # the end time of this chunk
        iEnd = math.ceil(tEnd / 1000.00 * WAVparams.framerate)   # index of the end
        if iEnd > WAVparams.nframes:    #  for the last chunk
            iEnd = WAVparams.nframes
        theMean = numpy.mean(WAVdata[iStart:iEnd])  # could use std() instead of mean()
        theSD = numpy.std(WAVdata[iStart:iEnd])  # could use mean() instead of std()

        theLine = '{:g}, {:g}, {:g}\n'.format(tStart, theMean, theSD)  # if you only want one version, change this
        out.write(theLine)  # write this chunk to the .csv

        tStart = tEnd
        iStart = iEnd
        i += 1

message = "Wrote {} lines to {}".format(i, outFileName)
print(message)
