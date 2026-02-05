#!/bin/bash
# Update all .tex files to use local T0_preamble_standalone_De

count=0
for f in *.tex; do
  # Skip preamble files themselves
  if [[ "$f" == "T0_preamble_De.tex" ]] || [[ "$f" == "T0_preamble_standalone_De.tex" ]]; then
    continue
  fi
  
  # Replace any T0_preamble input with local standalone version
  if grep -q "\\\\input{.*T0_preamble" "$f"; then
    sed -i 's|\\input{[^}]*T0_preamble[^}]*}|\\input{T0_preamble_standalone_De}|g' "$f"
    count=$((count + 1))
    echo "Updated: $f"
  fi
done

echo ""
echo "Total files updated: $count"
