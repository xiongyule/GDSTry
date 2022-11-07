import gdsfactory as gf

c = gf.components.coupler_asymmetric(gap=0.234, dy=5.0, dx=10.0, cross_section='strip')
c.plot()