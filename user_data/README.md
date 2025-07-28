### To run Bayeswave on any data.dat file specified with the user, we need

1) Seperate Frame and Cache files for each detector with the correspoding detector data as a timeseries
2) cache-files dictionary in the [datafind] section that points to the location of these Cache files
3)  --skip-datafind tag in the bayeswave_pipe command so that [datafind] does not try to get real LIGO data.

```bash
python3 frame_and_cache.py 
```

### uses data-H1.dat and data-L1.dat (with times and un-whitened strain) and to write separate Frame and Cache file for each detector H1 and L1. 

```bash
./submit.sh
```

updates the cache-files placeholder in the MDC_realnoise.ini file's [datafind] section and submits the run to bayeswave_pipe.
