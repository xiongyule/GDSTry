import gdsfactory as gf

c = gf.components.grating_coupler_elliptical_arbitrary(gaps=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1], widths=[0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5], taper_length=16.6, taper_angle=60.0, wavelength=1.554, fiber_angle=15.0, neff=2.638, nclad=1.443, layer_slab='SLAB150', slab_xmin=-3.0, polarization='te', fiber_marker_width=11.0, fiber_marker_layer='TE', spiked=True, bias_gap=0, cross_section='strip')
c.plot()