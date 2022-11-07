import gdsfactory as gf

c = gf.components.ring_single(gap=0.2, radius=10.0, length_x=4.0, length_y=0.6, coupler_ring='coupler_ring', bend='bend_euler', cross_section='strip')
c.plot()