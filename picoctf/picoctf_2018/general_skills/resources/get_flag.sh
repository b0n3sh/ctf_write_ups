#! /bin/bash

curl -s "https://picoctf.com/resources" | grep -oEi picoctf{.*}
