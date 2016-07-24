#!/bin/bash

sudo service ntpd stop
sudo ntpd -gq
sudo service ntpd start