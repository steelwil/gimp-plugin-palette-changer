#!/usr/bin/env python

#   Gimp-Python - allows the writing of Gimp plugins in Python.
#   Copyright (C) 2015  William Bell <william.bell@frog.za.net>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gimpfu import *
import time
from array import array

gettext.install("gimp20-python", gimp.locale_directory, unicode=True)

def palette_change(img, layer, red, green, blue):
    gimp.progress_init("Processing" + layer.name + "...")
    pdb.gimp_undo_push_group_start(img)

    layername = "render " + layer.name

    # Create the new layer:
    srcWidth, srcHeight = layer.width, layer.height

    destDrawable = gimp.Layer(img, layername, srcWidth, srcHeight,
                              layer.type, layer.opacity, layer.mode)
    img.add_layer(destDrawable, 0)
    xoff, yoff = layer.offsets

    destDrawable.translate(xoff, yoff)

    srcRgn = layer.get_pixel_rgn(0, 0, srcWidth, srcHeight, False, False)
    src_pixels = array("B", srcRgn[0:srcWidth, 0:srcHeight])

    dstRgn = destDrawable.get_pixel_rgn(0, 0, srcWidth, srcHeight, True, True)
    p_size = len(srcRgn[0,0])
    dest_pixels = array("B", [0] * (srcWidth * srcHeight * p_size))

    # Finally, loop over the region:
    for x in xrange(0, srcWidth - 1) :
        for y in xrange(0, srcHeight) :
            src_pos = (x + srcWidth * y) * p_size
            dest_pos = src_pos

            newval = src_pixels[src_pos: src_pos + p_size]
            newval[0] = int(int(newval[0]/256.0*red) * 255.0/(red-1))
            newval[1] = int(int(newval[1]/256.0*green) * 255.0/(green-1))
            newval[2] = int(int(newval[2]/256.0*blue) * 255.0/(blue-1))
            dest_pixels[dest_pos : dest_pos + p_size] = newval

        progress = float(x)/layer.width
        if (int(progress * 100) % 200 == 0) :
            gimp.progress_update(progress)

    # Copy the whole array back to the pixel region:
    dstRgn[0:srcWidth, 0:srcHeight] = dest_pixels.tostring()

    destDrawable.flush()
    destDrawable.merge_shadow(True)
    destDrawable.update(0, 0, srcWidth,srcHeight)

    # Remove the old layer
    #img.remove_layer(layer)
    layer.visible = False

    pdb.gimp_selection_none(img)
    pdb.gimp_image_undo_group_end(img)


register(
    "python-fu-palette_change",
    N_("reduce colors to simulate a different palettes.\n2bit = 4 colors\n3bit = 8 colors\n4bit = 16 colors\n5bit = 32 colors\n8bit = 256 colors"),
    "Adds a new layer to the image",
    "William Bell",
    "William Bell",
    "2015",
    N_("_Palette..."),
    "RGB*",
    [
        (PF_IMAGE, "image",       "Input image", None),
        (PF_DRAWABLE, "drawable", "Input drawable", None),
        (PF_SPINNER, "red",    _("Red"),    8, (2, 256, 1)),
        (PF_SPINNER, "blue",   _("Green"),  8, (2, 256, 1)),
        (PF_SPINNER, "green",  _("Blue"),   8, (2, 256, 1)),
    ],
    [],
    palette_change,
    menu="<Image>/Filters/Render",
    domain=("gimp20-python", gimp.locale_directory)
    )

main()
