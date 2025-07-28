# Writing .ini file with the correct file path to the Injection cache file
dest="$(pwd)/MDC_realNoise_injection.ini"
new_mdc_cache="$(pwd)/MDC.cache"
sed "s|^mdc-cache=.*|mdc-cache=${new_mdc_cache}|" MDC_realNoise.ini > "$dest"

# Extract t0 from the cache file
t0=$(head -n 1 "$new_mdc_cache" | cut -d' ' -f3)

ttrig=$((t0 + 2))
echo "t0 = ${t0}, ttrig = ${ttrig}"

bayeswave_pipe MDC_realNoise_injection.ini \
    --workdir test_injection \
    -t ${ttrig} \
    --condor-submit