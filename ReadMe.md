## Convert images to simulate palettes of ancient displays
if you have GEGL 0.4 or higher rather use Tools -> GEGL Opereation -> Color Reduction

### The following can be simulated
#### Regular RGB palettes
* 3-bit RGB 2 colors per channel 8 colors in total
* 6-bit RGB 4 colors per channel 64 colors in total
* 9-bit RGB 8 colors per channel 512 colors in total
* 12-bit RGB 16 colors per channel 4,096 colors in total
* 15-bit RGB 32 colors per channel 32,768 colors in total
* 18-bit RGB 64 colors per channel 262,144 colors in total
* change any number of colors per channel 2-256 colors

#### Non-regular RGB palettes
* 3-3-2 bit RGB 8 8 4 colors, 256 colors in total
* 5-6-5 bit RGB 32 64 32 colors, 65,536 colors in total (16-bit RGB)
* 3-level RGB 3 3 3 colors, 27 colors in total

### To do
* greyscale (can be simulated by first converting to Greyscale and then to RGB.
* intensity (cannot do 4-bit RGBI)
* dithering
* custom palettes
* maximum simultaneous colors

## Prerequisites
* [Gimp 2.8](http://www.gimp.org/)
* [Python](https://www.python.org/)

## Installation
* copy palette_change.py to your ~/.gimp-2.8/plug-ins directory.
* make sure that palette_change.py is marked as executable (sudo chmod +x palette_change.py)

## References
* [https://en.wikipedia.org/wiki/List_of_monochrome_and_RGB_palettes](https://en.wikipedia.org/wiki/List_of_monochrome_and_RGB_palettes)
* [https://en.wikipedia.org/wiki/List_of_color_palettes](https://en.wikipedia.org/wiki/List_of_color_palettes)
* [http://gimpbook.com/scripting/](http://gimpbook.com/scripting/)
* [http://www.gimp.org/docs/python/index.html](http://www.gimp.org/docs/python/index.html)
