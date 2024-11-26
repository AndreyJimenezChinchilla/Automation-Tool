#Import of the library that is going to be used.
import pyautogui
import time

#When fail-safe is "True", moving the mouse to any corner will abort the program execution.
pyautogui.FAILSAFE = True 

#This means that the program will start to run in 3 seconds.
time.sleep(3)

Transit = 2

#Network Devices selection in the toolbar (18, 908)
pyautogui.moveTo(18, 908, Transit)
pyautogui.click(18, 908, 1)

#Switches selection in the toolbar (54, 973)
#Multilayer Switch 3650 24PS location (388, 899)
#Switch 2960-24TT location (222, 897)

pyautogui.moveTo(54, 973, Transit)
pyautogui.click(54, 973, 1)
pyautogui.moveTo(388, 899, Transit)
pyautogui.click(388, 899, 1)

#Placing the End Devices on the topology
#1st Multilayer switch
pyautogui.moveTo(296, 458, Transit)
pyautogui.click(296, 458, 1)
#Installing the power supplys into the Multilayer switch 
pyautogui.click(296, 458, 2)
pyautogui.moveTo(1534, 905, Transit)
pyautogui.mouseDown()
pyautogui.moveTo(1219, 220, Transit)
pyautogui.mouseUp()
pyautogui.moveTo(1534, 905, Transit)
pyautogui.mouseDown()
pyautogui.moveTo(1334, 220, Transit)
pyautogui.mouseUp()
#Intalling the ports into the Multilayer switch
pyautogui.moveTo(799, 205, Transit)
pyautogui.click(799, 205, 1)
pyautogui.moveTo(1679, 879, Transit)
pyautogui.mouseDown()
pyautogui.moveTo(1334, 190, Transit)
pyautogui.mouseUp()
pyautogui.moveTo(1679, 879, Transit)
pyautogui.mouseDown()
pyautogui.moveTo(1326, 193, Transit)
pyautogui.mouseUp()
pyautogui.moveTo(1679, 879, Transit)
pyautogui.mouseDown()
pyautogui.moveTo(1364, 192, Transit)
pyautogui.mouseUp()
pyautogui.moveTo(1679, 879, Transit)
pyautogui.mouseDown()
pyautogui.moveTo(1380, 191, Transit)
pyautogui.mouseUp()

#Copying the other 2 Multilayer switches 
pyautogui.moveTo(196, 358, Transit)
pyautogui.mouseDown()
pyautogui.moveTo(396, 558, Transit)
pyautogui.mouseUp()
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('ctrl', 'v')
pyautogui.click()

#Placing the 2nd Multilayer switches
pyautogui.moveTo(284, 403, Transit)
pyautogui.mouseDown()
pyautogui.moveTo(434, 303, Transit)
pyautogui.mouseUp()
#Placing the 3rd Multilayer swithces
pyautogui.moveTo(284, 403, Transit)
pyautogui.mouseDown()
pyautogui.moveTo(596, 458, Transit)
pyautogui.mouseUp()

#1st Switch 
pyautogui.moveTo(222, 897, Transit)
pyautogui.click(222, 897, 1)
pyautogui.moveTo(153, 669, Transit)
pyautogui.click(153, 669, 1)
#2nd Switch 
pyautogui.moveTo(222, 897, Transit)
pyautogui.click(222, 897, 1)
pyautogui.moveTo(353, 669, Transit)
pyautogui.click(353, 669, 1)
#3rd Switch 
pyautogui.moveTo(222, 897, Transit)
pyautogui.click(222, 897, 1)
pyautogui.moveTo(546, 669, Transit)
pyautogui.click(546, 669, 1)
#4th Switch 
pyautogui.moveTo(222, 897, Transit)
pyautogui.click(222, 897, 1)
pyautogui.moveTo(746, 669, Transit)
pyautogui.click(746, 669, 1)

#Cable connections between the devices
#Connections button location (123, 909)
#Copper Cross-Over location (347, 893)
pyautogui.moveTo(123, 909, Transit)
pyautogui.click()

#1st Multilayer Switch
pyautogui.moveTo(347, 893, Transit)
pyautogui.click()
pyautogui.moveTo(296, 458, Transit)
pyautogui.click()
pyautogui.moveTo(370, 821, Transit)
pyautogui.click()
pyautogui.moveTo(434, 303, Transit)
pyautogui.click()
pyautogui.moveTo(526, 818, Transit)
pyautogui.click()
#2nd Multilayer Switch
pyautogui.moveTo(347, 893, Transit)
pyautogui.click()
pyautogui.moveTo(596, 458, Transit)
pyautogui.click()
pyautogui.moveTo(652, 831, Transit)
pyautogui.click()
pyautogui.moveTo(434, 303, Transit)
pyautogui.click()
pyautogui.moveTo(526, 818, Transit)
pyautogui.click()

#1st Switch
pyautogui.moveTo(347, 893, Transit)
pyautogui.click()
pyautogui.moveTo(153, 669, Transit)
pyautogui.click()
pyautogui.moveTo(238, 796, Transit)
pyautogui.click()
pyautogui.moveTo(296, 458, Transit)
pyautogui.click()
pyautogui.moveTo(357, 818, Transit)
pyautogui.click()
#2nd Switch 
pyautogui.moveTo(347, 893, Transit)
pyautogui.click()
pyautogui.moveTo(353, 669, Transit)
pyautogui.click()
pyautogui.moveTo(438, 796, Transit)
pyautogui.click()
pyautogui.moveTo(296, 458, Transit)
pyautogui.click()
pyautogui.moveTo(357, 818, Transit)
pyautogui.click()
#3rd Switch
pyautogui.moveTo(347, 893, Transit)
pyautogui.click()
pyautogui.moveTo(546, 669, Transit)
pyautogui.click()
pyautogui.moveTo(600, 796, Transit)
pyautogui.click()
pyautogui.moveTo(596, 458, Transit)
pyautogui.click()
pyautogui.moveTo(732, 813, Transit)
pyautogui.click()
#4th Switch
pyautogui.moveTo(347, 893, Transit)
pyautogui.click()
pyautogui.moveTo(746, 669, Transit)
pyautogui.click()
pyautogui.moveTo(800, 796, Transit)
pyautogui.click()
pyautogui.moveTo(596, 458, Transit)
pyautogui.click()
pyautogui.moveTo(732, 813, Transit)
pyautogui.click()

#Labeling the Switches
#Label button(149, 109)
pyautogui.moveTo(149, 109, Transit)
pyautogui.click()

#Labeling the Switches
#Label button(149, 109)
pyautogui.moveTo(149, 109, Transit)
pyautogui.click()

#Switches labels
pyautogui.moveTo(113, 700, Transit)
pyautogui.click()
pyautogui.typewrite('Access-1', 0.1)
pyautogui.moveTo(313, 700, Transit)
pyautogui.click()
pyautogui.typewrite('Access-2', 0.1)
pyautogui.moveTo(513, 700, Transit)
pyautogui.click()
pyautogui.typewrite('Access-3', 0.1)
pyautogui.moveTo(713,700, Transit)
pyautogui.click()
pyautogui.typewrite('Access-4', 0.1)

#Multilayer Switches labels
pyautogui.moveTo(200,420, Transit)
pyautogui.click()
pyautogui.typewrite('Radial-1', 0.1)
pyautogui.moveTo(620,420, Transit)
pyautogui.click()
pyautogui.typewrite('Radial-2', 0.1)
pyautogui.moveTo(425, 250, Transit)
pyautogui.click()
pyautogui.typewrite('Core', 0.1)
pyautogui.moveTo(18, 107, Transit)
pyautogui.click()

#Configuring the Switches names 
#1st Switch
pyautogui.moveTo(153, 669, Transit)
pyautogui.click()
pyautogui.moveTo(850, 67, Transit)
pyautogui.click()
pyautogui.moveTo(850, 600, Transit)
pyautogui.click()
pyautogui.typewrite('\n')
pyautogui.typewrite('enable\n', 0.1)
pyautogui.typewrite('configure terminal\n', 0.1)
pyautogui.typewrite('hostname Access-1\n', 0.1)
pyautogui.typewrite('end\n', 0.1)
pyautogui.typewrite('wri\n', 0.1)
#2nd Switch
pyautogui.moveTo(353, 669, Transit)
pyautogui.click()
pyautogui.moveTo(850, 67, Transit)
pyautogui.click()
pyautogui.moveTo(850, 600, Transit)
pyautogui.click()
pyautogui.typewrite('\n')
pyautogui.typewrite('enable\n', 0.1)
pyautogui.typewrite('configure terminal\n', 0.1)
pyautogui.typewrite('hostname Access-2\n', 0.1)
pyautogui.typewrite('end\n', 0.1)
pyautogui.typewrite('wri\n', 0.1)
#3rd Switch 
pyautogui.moveTo(553, 669, Transit)
pyautogui.click()
pyautogui.moveTo(850, 67, Transit)
pyautogui.click()
pyautogui.moveTo(850, 600, Transit)
pyautogui.click()
pyautogui.typewrite('\n')
pyautogui.typewrite('enable\n', 0.1)
pyautogui.typewrite('configure terminal\n', 0.1)
pyautogui.typewrite('hostname Access-3\n', 0.1)
pyautogui.typewrite('end\n', 0.1)
pyautogui.typewrite('wri\n', 0.1)
#4th Switch 
pyautogui.moveTo(600, 669, Transit)
pyautogui.click()
pyautogui.moveTo(753, 669, Transit)
pyautogui.click()
pyautogui.moveTo(850, 67, Transit)
pyautogui.click()
pyautogui.moveTo(850, 600, Transit)
pyautogui.click()
pyautogui.typewrite('\n')
pyautogui.typewrite('enable\n', 0.1)
pyautogui.typewrite('configure terminal\n', 0.1)
pyautogui.typewrite('hostname Access-4\n', 0.1)
pyautogui.typewrite('end\n', 0.1)
pyautogui.typewrite('wri\n', 0.1)

#Taking out the PC
#End Devices button location (50, 901)
#PC button location(230, 896)
pyautogui.moveTo(50, 901, Transit)
pyautogui.click()

#1st PC
pyautogui.moveTo(230, 896, Transit)
pyautogui.click()
pyautogui.moveTo(70, 550, Transit)
pyautogui.click()
#2nd PC
pyautogui.moveTo(230, 896, Transit)
pyautogui.click()
pyautogui.moveTo(825, 550, Transit)
pyautogui.click()

#Connecting the PC
#Connections button location (123, 909)
#Automated connection cable location (223, 895)
pyautogui.moveTo(123, 909, Transit)
pyautogui.click()

#1st PC
pyautogui.moveTo(223, 895, Transit)
pyautogui.click()
pyautogui.moveTo(70, 550, Transit)
pyautogui.click()
pyautogui.moveTo(153, 669, Transit)
pyautogui.click()
#2nd PC
pyautogui.moveTo(223, 895, Transit)
pyautogui.click()
pyautogui.moveTo(825, 550, Transit)
pyautogui.click()
pyautogui.moveTo(753, 669, Transit)
pyautogui.click()

time.sleep(3)

#Configuring the IP on the PC
#1st IP and Subnet Mask
pyautogui.moveTo(70, 550, Transit)
pyautogui.click()
pyautogui.moveTo(868, 70, Transit)
pyautogui.click()
pyautogui.moveTo(784, 154, Transit)
pyautogui.click()
pyautogui.moveTo(1070, 230, Transit)
pyautogui.click()
pyautogui.typewrite('192.168.1.20\n', 0.2)
pyautogui.moveTo(70, 500, Transit)
pyautogui.click()

#2nd IP and Subnet Mask
pyautogui.moveTo(825, 550, Transit)
pyautogui.click()
pyautogui.moveTo(868, 70, Transit)
pyautogui.click()
pyautogui.moveTo(784, 154, Transit)
pyautogui.click()
pyautogui.moveTo(1070, 230, Transit)
pyautogui.click()
pyautogui.typewrite('192.168.1.21\n', 0.2)

#Making time so that the PC2 can connect
time.sleep(5)

#Sending a Package from PC1 to PC2
pyautogui.moveTo(1840, 861, Transit)
pyautogui.click()
pyautogui.moveTo(310, 105, Transit)
pyautogui.click()

pyautogui.moveTo(70, 550, Transit)
pyautogui.click()
pyautogui.moveTo(825, 550, Transit)
pyautogui.click()

pyautogui.moveTo(1726, 596, Transit)
pyautogui.mouseDown()
pyautogui.moveTo(1840, 596, Transit)
pyautogui.mouseUp()

pyautogui.moveTo(1726, 566, Transit)
pyautogui.click()

time.sleep (25)

pyautogui.click()
#End of the code