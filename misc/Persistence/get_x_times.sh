#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <url> <number_of_requests>"
    exit 1
fi

url="$1"
num_requests="$2"
output_file="responses.txt"

# Check if the number of requests is a positive integer
if ! [[ "$num_requests" =~ ^[0-9]+$ ]]; then
    echo "Error: number_of_requests must be a positive integer."
    exit 2
fi

# Clear or create the output file
echo "" > "$output_file"

# Send X number of GET requests using curl and save responses to the output file
for i in $(seq 1 $num_requests); do
    echo "Iteration: $i" | tee -a "$output_file"
    echo | tee -a "$output_file"
    curl -s "$url" | tee -a "$output_file"
    echo | tee -a "$output_file"
    echo "-------------------------------------" | tee -a "$output_file"
done