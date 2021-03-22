#Turning off wifi
sudo ifconfig wlan0 down

#Turning off HDMI
sudo /usr/bin/tvservice -o
#  Add the line to /etc/rc.local to make it permanent
sudo nano /etc/rc.local

#Possible under clock the CPU in 
#rpi-config
#arm_freq_min=250
#core_freq_min=100
#sdram_freq_min=150
#over_voltage_min=0 or 4 if you have overclocked your rasppi

#Turning off blue tooth
sudo systemctl disable bluetooth
sudo service bluetooth stop
sudo systemctl disable hciuart
sudo service  hciuart stop