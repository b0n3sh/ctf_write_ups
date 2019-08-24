#!/bin/bash
strings data.pcap | grep -oi picoctf{.*} --color=none
