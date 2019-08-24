#!/bin/bash

(echo 'root'; echo 'hellokitty') | nc 2018shell.picoctf.com 35225 | rev | cut -d " " -f1 | rev
