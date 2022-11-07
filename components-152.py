import gdsfactory as gf

c = gf.components.ring_single_array(ring='ring_single', spacing=5.0, cross_section='strip')
c.plot()