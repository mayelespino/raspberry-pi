#!/bin/bash

/usr/bin/speedtest-cli > /mnt/ramdisk/speedtest.txt
grep -E '^Upload*|^Download*' /mnt/ramdisk/speedtest.txt | tr  '\n' '  ' >> /mnt/ramdisk/speedtest-history.txt
date  >> /mnt/ramdisk/speedtest-history.txt
