# Customizing SSD card 
## use the entire SSD for "/" root partition
* link: https://www.youtube.com/watch?v=R4VovMDnsIE
```
$fdisk -uc /dev/mmcblk0
# type P
# type d
# type 2
# type n
# type p (primary)
# type 2 (same as the one you deleted)
# copy paste the start of the partition 2 (shuould still be on the screen)
# hit enter to take the default, the entire SSD card.
# type w
$reboot now
$resize2fs -p /dev/mmcblk0p2
```
* add hostname
```
$sudo vi /etc/hostname
```
* add message of the day (MOTD)
```
$sudo vi /etc/motd
```
