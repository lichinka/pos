cat /dev/stdin | sed -e 's/{/\n{/g' | sed -e 's/}},/}},\n/g' | sed -e 's/}}]/}}\n]\n/g'
