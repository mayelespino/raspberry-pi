#!/bin/sh
at now + ${1} minutes << EOF
/usr/bin/curl -X POST http://localhost:5000/mute/
EOF
