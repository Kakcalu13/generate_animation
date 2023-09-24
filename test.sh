#!/bin/bash

input_folder="$1"
output_folder="gen/"

mkdir -p "$output_folder"

count=0
for file in "$input_folder"/*.png; do
    new_filename=$(printf "filename-%04d.png" "$count")
    output_path="$output_folder/$new_filename"
    cp "$file" "$output_path"
    echo "Processed: $file -> $new_filename"
    count=$((count + 1))
done

