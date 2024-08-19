# Swoon Half Xiao'd

A diode matrix rework of the Sweep Half Swept for Seeed Xiao nRF52840. 

Use with [301020 10mm x 22mm x 3mm](https://www.aliexpress.us/item/3256806150189359.html) with jst-SH 1.0mm 2 pin connector. 

Battery 350820 is also a candidate (8.2mm x22mmx 3.8mm). It's enough skinnier to fit an additional pogo pin for reset, but the board is flippable for those who wish to self assemble, and squeezing another set of pogo pins wasn't great. Use the reset button on the Xiao, or include a bootloader reference in your ZMK config.

This board comes with conflicting goals: 

- To be as affordable as possible
- To be as low as possible

You can have JLCPCB assemble it for you from the files in jlcpcb/production_files, but you will need to provide the 3305-0-15-80-47-27-10-0 receptacles and the 0906-2-15-20-75-14-11-0 pogo pins via consignment. All components are top placed to make the board as low as possible, and also to make fabrication cheaper. 


If you're hand soldering, SOD-323 diodes should fit on the 0805 smd pads fine and are easier to get on Amazon. 