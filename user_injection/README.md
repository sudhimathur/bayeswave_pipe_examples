### To inject a waveform template from a .dat file into LIGO data, we need

1) A single Frame and Cache file with the template as a timeseries.
2) Correct channel names and frame types to get LIGO data at the specified GPS time
3) [injections] section in the .ini that points to the cache file

### Run the example using

```bash
python3 frame_and_cache.py
```

uses template.dat (with times and un-whitened strain) and channel names to write the single frame and cache file for a single/multi-detector injection. 

```bash
./submit.sh
```

updates the mdc-cache placeholder in the MDC_realnoise.ini file's [injection] section and submits the run to bayeswave_pipe.
