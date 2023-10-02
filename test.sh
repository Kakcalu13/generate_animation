#!/bin/bash

input_folder="$1"
output_folder="gen/"

mkdir -p "$output_folder"

count=0
count_files=$(find . -type f -name "*.png" | wc -l)
total_files=$((count_files-1))
num_digits=${#total_files}

# Calculate the width for padding zeros
width=$((num_digits > 4 ? num_digits : 4))

for file in "$input_folder"/*.png; do
    new_filename=$(printf "filename-%0*d.png" "$width" "$count")  # Updated format specifier
    output_path="$output_folder/$new_filename"
    cp "$file" "$output_path"
    echo "Processed: $file -> $new_filename"
    count=$((count + 1))
done

