import gdsfactory as gf

c = gf.components.edge_coupler_array_with_loopback(cross_section='strip', radius=30, n=8, pitch=127.0, extension_length=1.0, h_mirror=False, v_mirror=False, right_loopback=True, text_offset=[0, 0])
c.plot()