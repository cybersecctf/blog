#!/bin/bash

# Set default values if arguments are not provided
ARG1=${1:-'./strings'}
ARG2=${2:-'pico'}

# Execute the strings command with ARG1 as the argument, pipe the output to grep, and search for ARG2
strings "$ARG1" | grep "$ARG2"
