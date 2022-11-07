import gdsfactory as gf

c = gf.components.add_fidutials(gap=50, left='cross', right='cross', offset=[0, 0])
c.plot()