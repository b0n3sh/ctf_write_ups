#!/bin/bash

strings hex_editor.jpg | tail -n 1 | cut -d '"' -f2
