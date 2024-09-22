# Swoon Half Xiao'd

> Yet another diode matrix rework of the
> [Ferris Sweep Half Swept](https://github.com/davidphilipbarr/Sweep/tree/main/Sweep%20half-swept)
> for
> [Seeed Xiao nRF52840](https://www.seeedstudio.com/Seeed-XIAO-BLE-nRF52840-p-5201.html).

![Swoon Half Xiao'd](.images/swoon.jpg)

## Motivations

- Utilise Seeed Xiao—it's cuter
- Experiment with parts consignment for PCBA of hotswaps
- Choose a battery that can be easily changed by users who do not solder
- Explore using CI/CD for board variants, case, and top plate generation
- Locate each half's components on its respective top side for more affordable
  assembly and lower overall height

## Variants

### **Flip**

A flippable variant for hand-soldering, like the original half-swept. **Flip**
is also the most cost conscious variant—about $7.60 to get 5 of the boards
produced, enough for 2 full keyboads and a nice... coaster? You'll need to
solder the upward facing jumpers on each half under the Xiao before use.

#### BOM

|      QTY      |                   Part                   | JLCPCB Part # |
| :-----------: | :--------------------------------------: | :-----------: |
|       2       |         0906-2-15-20-75-14-11-0          |   C5261048    |
|       2       |            BAT-SMD_MY-LR44-02            |   C2902345    |
|       4       |  310-13-107-41-001000/MF254V-11-07-0743  |   C5504401    |
| 34 (optional) |         3305-0-15-80-47-27-10-0          |   C17370797   |
|       2       |              MST22D18G2125               |   C2906280    |
|      34       | CD4148WS (or 1N4148 SOD-323 from Amazon) |   C38587762   |
|      34       |      Your ChocV1 switches of choice      |      N/A      |

### **Left** and **Right**

These variants are designed to be produced and assembled by JLCPCB. Each zip
file has the a gerbers/drill zip, a cpl, and bom file. They should be fully
assemblable, but you'll need to preorder the parts through global sourcing
before paying. The 3305s aren't cheap and they cost extra to assemble.

Each half is pre-jumpered in the gerbers so you can print and go.

## CI/CD

This project is mostly setup for production and assembly variants in GitHub
actions. Production variants are newer to KiCad and there's still a few kinks,
but hopefully they'll be worked out soon. In the mean time, use the files in the
[jlcpcb](/jlcpcb/) directory.

## Case

There's a case [[step](/case/case.step)] [[stl](/case/case.stl)]. It's really
more of a skin. Print in TPU (polymaker TPU seems to work well) and place the
pcb directly in it. TPU is relatively non-slip, and it absorbs and distributes
the force of typing very nicely, so no bumpons needed.
