#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import time


class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")
        self.parser.add_argument("-red", help="red sets the red value", default="128")
        self.parser.add_argument("-green", help="green sets the green value", default="0")
        self.parser.add_argument("-blue", help="blue sets the blue value", default="255")

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/10x20.bdf")
        pos = offscreen_canvas.width
        my_text = self.args.text
        red = int(self.args.red)
        green = int(self.args.green)
        blue = int(self.args.blue)
        textColor = graphics.Color(red, green, blue)
        len=0

        while (pos + len >= 0):
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, 22, textColor, my_text)
            pos -= 1
            
            time.sleep(0.03)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
