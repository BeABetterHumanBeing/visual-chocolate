# Utility file for working with colors.

# Converts an RGB tuple into an HSV tuple. Inputs are expected to be in the
# range [0, 1]. Outputs are in [0, 1] except for degrees.
def rgb2hsv(rgb):
	red = rgb[0]
	green = rgb[1]
	blue = rgb[2]

	minimum = min(red, green, blue)
	maximum = max(red, green, blue)

	v = maximum
	delta = maximum - minimum

	if delta < 0.00001:
		s = 0.0
		h = 0.0  # Technically undefined.
		return (h, s, v)

	if maximum > 0.0:
		s = delta / maximum
	else:
		s = 0.0
		h = 0.0  # Technically undefined.

	if red == maximum:
		h = (green - blue) / delta
	else:
		if green == maximum:
			h = 2.0 + (blue - red) / delta
		else:
			h = 4.0 + (red - green) / delta

	h *= 60.0  # Degrees

	if h < 0.0:
		h += 360.0

	return (h, s, v)

# Converts an HSV tuple into an RGB tuple. Inputs are expected to be in the
# range [0, 1] except for degrees.
def hsv2rgb(hsv):
	h = hsv[0]
	s = hsv[1]
	v = hsv[2]

	if s <= 0.0:
		r = v
		g = v
		b = v
		return (r, g, b)

	hh = h
	if hh >= 360.0:
		hh = 0.0
	hh /= 60.0

	i = int(hh)

	ff = hh - i

	p = v * (1.0 - s)
	q = v * (1.0 - (s * ff))
	t = v * (1.0 - (s * (1.0 - ff)))

	if i == 0:
		r = v
		g = t
		b = p
	elif i == 1:
		r = q
		g = v
		b = p
	elif i == 2:
		r = p
		g = v
		b = t
	elif i == 3:
		r = p
		g = q
		b = v
	elif i == 4:
		r = t
		g = p
		b = v
	else:  # i == 5
		r = v
		g = p
		b = q

	return (r, g, b)