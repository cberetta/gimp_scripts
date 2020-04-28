#!/usr/bin/env python

# python-fu-masslayermode - Change the layer-mode for all (visible) layers

from gimpfu import *

# Layer-modes :
# NORMAL_MODE (0)
# DISSOLVE_MODE (1)
# BEHIND_MODE (2)
# MULTIPLY_MODE (3)
# SCREEN_MODE (4)
# OVERLAY_MODE (5)
# DIFFERENCE_MODE (6)
# ADDITION_MODE (7)
# SUBTRACT_MODE (8)
# DARKEN_ONLY_MODE (9)
# LIGHTEN_ONLY_MODE (10)
# HUE_MODE (11)
# SATURATION_MODE (12)
# COLOR_MODE (13)
# VALUE_MODE (14)
# DIVIDE_MODE (15)
# DODGE_MODE (16)
# BURN_MODE (17)
# HARDLIGHT_MODE (18)
# SOFTLIGHT_MODE (19)
# GRAIN_EXTRACT_MODE (20)
# GRAIN_MERGE_MODE (21)
# COLOR_ERASE_MODE (22)
# ERASE_MODE (23)
# REPLACE_MODE (24)
# ANTI_ERASE_MODE (25)

# do the work ===============================================================
def masslayermode(image, layer, mode, onlyvisible):

	gimp.context_push()
	image.undo_group_start()

	# https://gimplearn.net/viewtopic.php/getting-layers-of-an-image-in-python-fu-script?t=55
	# Loop on all layers
	for layer in image.layers:
		# "True" if first option, so its value is 0 which is False
		# I use not to toggle value
		if not onlyvisible:
			if layer.visible:
				layer.mode = mode
		else:
			layer.mode = mode
		pass

	image.undo_group_end()
	gimp.context_pop()


# Register the script into menu: Layer => Stack =============================
register(
	"python-fu-masslayermode",
	"Massively change layer-mode",
	"Massively change layer-mode",
	"Beretta Costantino",
	"Beretta Costantino",
	"2020",
	"Massively change layer mode",
	"*",
	[
		(PF_IMAGE, "image", "Input image", None),
		(PF_DRAWABLE, "drawable", "Input drawable", None),
		(PF_OPTION, "mode", "Mode", 0, ["Normal", "Dissolve", "Behind", "Multiply", "Screen", "Overlay", "Difference", "Addition", "Subtract", "Darken_only", "Lighten_only", "Hue", "Saturation", "Color", "Value", "Divide", "Dodge", "Burn", "Hardlight", "Softlight", "Grain_extract", "Grain_merge", "Color_erase", "Erase", "Replace", "Anti_erase"]),
		(PF_OPTION, "onlyvisible", "Only visible", 0, ["True", "False"]),
	],
	[],
	masslayermode,
	menu="<Image>/Layer/Stack",
	)

main()

