import numpy as np
from gwpy.timeseries import TimeSeries, TimeSeriesDict
from gwpy.detector import Channel
from numpy.random import random
import os

srate=4096
t0 = 1268903505
ifo = 'HL' # Can also be 'H' or 'L' incase of single detector injection
event_type = 'BBH'
frame_file_label = 'Sample' # For injections, this could be anything. Useful for naming conventions and for writing condor jobs with different frame files.

# Template injection - (assuming .dat file with times and un-whitened strain)
# Channel names and Frame types for timeseries near any LIGO event can be found in the GWOSC catalog: https://gwosc.org/eventapi/html/GWTC/
injection = np.loadtxt('template.dat')
td = {'H1':TimeSeries(injection[:,1],t0=t0,sample_rate=srate), 'L1':TimeSeries(injection[:,1],t0=t0,sample_rate=srate)}
td = TimeSeriesDict(td)
td['H1'].channel = Channel('H1:DCS-CALIB_STRAIN_CLEAN_SUB60HZ_C01',sample_rate=srate)
td['H1'].name = td['H1'].channel.name
td['L1'].channel = Channel('L1:DCS-CALIB_STRAIN_CLEAN_SUB60HZ_C01',sample_rate=srate)
td['L1'].name = td['L1'].channel.name

# --- Writing the Frame file ---
# For injections in LIGO data, we need a single frame file for any number of detectors.
cache_dir = os.path.dirname(os.path.abspath(__file__)) #(same directory as this script)
frame_file = f"{ifo}-{frame_file_label}-{t0}-{srate}.gwf"
td.write(f"{cache_dir}/{frame_file}")

# --- Writing the Cache file --- 
cache_file = os.path.join(cache_dir, f"MDC.cache")
print(cache_file)

# Cache files contain five columns with 1) ifo_label - example 'HL', 'H' or 'L' 2) Event description - example 'BBH' for BBH merger type injection 3) GPS start time 3) sampling rate 4) Absolute path to the frame file containing the injection timeseries.
cache_content = (f"{ifo} {event_type} {t0} {srate} " f"{cache_dir}/{frame_file}\n")

print(f"Writing Template Injection cache file to: {cache_file}")
with open(cache_file, "w") as f:
    f.write(cache_content)

print(f"{ifo}: Cache file written.")
