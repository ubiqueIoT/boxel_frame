
import board
import terminalio
import displayio
from adafruit_display_text import label
from adafruit_st7789 import ST7789
import adafruit_imageload

spi = board.SPI()
spi = board.SPI()

while not spi.try_lock():
    pass

spi.configure(baudrate=24000000)  # Configure SPI for 24MHz
spi.unlock()

tft_cs = board.D2
tft_dc = board.D1

# Release any resources currently in use for the displays
displayio.release_displays()
display_bus = displayio.FourWire(
    spi, command=tft_dc, chip_select=tft_cs, reset=board.D0
)

display = ST7789(display_bus, width=240, height=240, rowstart=80, rotation=180)

background_sheet, background_palette = adafruit_imageload.load("/tree.bmp",
                                                bitmap=displayio.Bitmap,
                                                palette=displayio.Palette)

# Create the background TileGrid
background = displayio.TileGrid(background_sheet, pixel_shader=background_palette,
                            width = 1,
                            height = 1,
                            tile_width = 240,
                            tile_height = 240)

# Create a Group to hold the background and add it
background_group = displayio.Group(scale=1)
background_group.append(background)

# Create a Group to hold the sprite and background
group = displayio.Group()
group.append(background_group)

display.show(group)

while True:
    pass

