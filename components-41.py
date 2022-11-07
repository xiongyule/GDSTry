import gdsfactory as gf

c = gf.components.coupler90(gap=0.2, radius=10.0, bend='bend_euler', straight='straight', cross_section='strip')
c.plot()