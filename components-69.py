import gdsfactory as gf

c = gf.components.delay_snake3(length=1600.0, length0=0.0, n=2, cross_section='strip')
c.plot()