#!/usr/bin/env bash
set -euo pipefail
rg -e "([ -]+)(.*) Type: (.*)$" -C 0 ./examples |
  sed -E 's/^[^:]+: +(- )?//g' |
  awk -F ': ' '
    {
      y=$1 "=" $2
      x[y]++
    }
    END {
      for (i in x) {
         print i
      }
    }' |
  sort
