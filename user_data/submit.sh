# Writing .ini file with the correct file path to the data cache files
dest="$(pwd)/MDC_userdata.ini"
cache_file="$(pwd)/MDC-H1.cache"

new_cache="{'H1': '$(pwd)/MDC-H1.cache', 'L1':'$(pwd)/MDC-L1.cache'}"
sed "s|^cache-files=.*|cache-files=${new_cache}|" MDC_realNoise.ini > "$dest"

# Extract t0 from the cache file
t0=$(head -n 1 "$cache_file" | cut -d' ' -f3)

ttrig=$((t0 + 2))
echo "t0 = ${t0}, ttrig = ${ttrig}"

bayeswave_pipe MDC_userdata.ini \
        --workdir test_userdata \
        -t ${ttrig} \
        --skip-datafind \
        --condor-submit