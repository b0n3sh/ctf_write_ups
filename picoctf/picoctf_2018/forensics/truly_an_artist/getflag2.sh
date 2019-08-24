#!/bin/bash
exiftool 2018.png | grep pico | cut -d ':' -f2 | tr -d ' '
