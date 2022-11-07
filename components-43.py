import gdsfactory as gf

c = gf.components.coupler90circular(gap=0.2, radius=10.0, straight='straight', cross_section='strip')
c.plot()