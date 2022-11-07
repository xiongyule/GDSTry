import gdsfactory as gf

c = gf.components.coupler_ring(gap=0.2, radius=5.0, length_x=4.0, coupler90='coupler90', bend='bend_euler', straight='straight', coupler_straight='coupler_straight', cross_section='strip')
c.plot()