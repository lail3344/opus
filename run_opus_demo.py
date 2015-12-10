import os
import subprocess
import numpy as np

run_cmd = "./opus_demo -e voip 48000 2 48000 examples/music_orig.wav test.opus"

cmd = "date +%s.%N"
total=[]

for i in range(1,10):
    start = subprocess.check_output(['date','+%s.%N'])

    os.system(run_cmd)

    end = subprocess.check_output(['date','+%s.%N'])

    execution_time = float(end) - float(start)

    total.append(execution_time)

print ("average = %f" % np.mean(total))
