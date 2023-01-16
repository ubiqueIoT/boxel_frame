# Boxel Frame
### Desktop Pixel Art Display

Pixel art has always struck a nostalgic chord. In an effort to perfect my workspace, I thought that a pixel art display case might be in order. This repository details the build process of my pixel frame. I tried to use as many off the shelf components as possible as to keep it easily reproducible.

<img src="https://user-images.githubusercontent.com/8181497/212775334-43bca06f-9f86-4114-a0b5-94ba78a755f6.png" width="500" height="500">

OnShape was used to build the case for this project. You can find the project source [here](https://cad.onshape.com/documents/5000a3d49c7a9077d1572ff0/w/f60200444dc0dcea69f2e1f3/e/457eb17b8405f6b113c2318f?renderMode=0&uiState=63c5c0a977641842e2176192).
3D Prints were ordered from JLC PCB, using their SLA service with Black Resin. The STL files can be found in the 3D directory of this repository. 

<img src="https://user-images.githubusercontent.com/8181497/212772188-89453f68-5566-447a-9408-66733f6073ca.png" width="250" height="300">

KiCAD was used to make the adapter PCB. You can find the Gerber files in the PCB folder of this directory. The boards were ordered through [JLC PCB](https://jlcpcb.com/CWH).

<img src="https://user-images.githubusercontent.com/8181497/212772308-606fd5af-9721-4111-a320-73f6e00edc4a.png" width="250" height="250">

The Seeed Studio [XIAO nRF52840](https://amzn.to/3kjpGdO) is used as the main processor. The [RP2040 variant](https://amzn.to/3kjpGdO) _should_ also work, but remains untested.

<img src="https://user-images.githubusercontent.com/8181497/212772078-28b44a1e-8c66-47e1-b7f4-4dd8f5bf390c.png" width="250" height="250">

The display is a [240x240 TFT SPI module from Aliexpress](https://www.aliexpress.us/item/3256803574008408.html?spm=a2g0o.productlist.main.1.239917ddZtO2b2&algo_pvid=4f8b1cea-cd19-4f80-8319-a5b96f190500&algo_exp_id=4f8b1cea-cd19-4f80-8319-a5b96f190500-0&pdp_ext_f=%7B%22sku_id%22%3A%2212000027073447132%22%7D&pdp_npi=2%40dis%21USD%214.6%213.45%21%21%21%21%21%40211bd3cb16739046656243641d06d9%2112000027073447132%21sea&curPageLogUid=33Dx8JTfaZM6) 

<img src="https://user-images.githubusercontent.com/8181497/212771949-b4c5c71c-58d1-4f68-b738-6f9f391b0951.png" width="250" height="250">

An 8-pin right angle M-F header is required to attach the adapter PCB to the TFT display. 
Longer, [easily available, header rows](https://amzn.to/3Xi4Qdl) can be cut to size using snips.

<img src="https://user-images.githubusercontent.com/8181497/212772782-54499e95-692c-450e-82e7-b89d6e81f9d1.png" width="250" height="250">

As for assembly hardware, a few different lengths of M2 screws are used. 
All of these can be found in [an M2 hardware kit](https://amzn.to/3ZSZl6T).

- 4x 12mm M2 screw
- 1x 10mm M2 screw
- 2x 8mm M2 screw
- 7x M2 nut


