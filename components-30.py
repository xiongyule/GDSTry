import gdsfactory as gf

c = gf.components.circle(radius=10.0, angle_resolution=2.5, layer='WG')
c.plot()