import numpy as np
from gwpy.timeseries import TimeSeries, TimeSeriesDict
from gwpy.detector import Channel
from numpy.random import random
import os

srate=4096
t0 = 1268903505
event_type = 'BBH'
frame_file_label = 'Sample' # For injections, this could be anything. Useful for naming conventions and for writing condor jobs with different frame files.

for ifo in ['H', 'L']:
    # Data for BW to run on - (assuming .dat file with times and un-whitened strain)
    data = np.loadtxt(f"data-{ifo}1.dat")
    td = {f"{ifo}1":TimeSeries(data[:,1],t0=t0,sample_rate=srate)}
    td = TimeSeriesDict(td)
    td[f"{ifo}1"].channel = Channel(f"{ifo}1:DCS-CALIB_STRAIN_CLEAN_SUB60HZ_C01",sample_rate=srate)
    td[f"{ifo}1"].name = td[f"{ifo}1"].channel.name

    # --- Writing Frame files ---
    # To run BW on user data we need a separate frame file for each detector.
    cache_dir = os.path.dirname(os.path.abspath(__file__)) #(same directory as this script)
    frame_file = f"{ifo}-{frame_file_label}-{t0}-{srate}.gwf"
    td.write(f"{cache_dir}/{frame_file}")

    # --- Writing the Cache files --- 
    cache_file = os.path.join(cache_dir, f"MDC-{ifo}1.cache")
    print(cache_file)

    # Cache files contain five columns with 1) ifo_label - example 'HL', 'H' or 'L' 
    # 2) Event description - example 'BBH' for BBH merger type injection 
    # 3) GPS start time 3) sampling rate 
    # 4) Absolute path to the frame file containing the injection timeseries.
    cache_content = (f"{ifo} {event_type} {t0} {srate} " f"{cache_dir}/{frame_file}\n")

    print(f"Writing Template Injection cache file to: {cache_file}")
    with open(cache_file, "w") as f:
        f.write(cache_content)

    print(f"{ifo}1: Cache file written.")