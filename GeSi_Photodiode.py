"""GeSi Photodiode."""
import gdsfactory as gf
from gdsfactory.snap import snap_to_grid

@gf.cell
def GeSi_Photodiode()->gf.Component:
    """Returns a GeSi Photodiode.

    Args:
        length: width (um).
        
    """
    c = gf.Component()
    SiBase = c << gf.components.rectangle(size=[16, 22], layer=1)
    #P doping at Si base
    SiDoping = gf.components.rectangle(size=[14.4, 22.5], layer=(3, 0))
    SiDoping = c << SiDoping
    SiDoping.movex(0.8)
    SiDoping.movey(-0.2)

    #P++ doping at Si base for electrode
    SiDopingPlus = gf.components.rectangle(size=[4.7, 22.5], layer=(6, 0))
    SiDopingPlus = c << SiDopingPlus
    SiDopingPlus.movex(0.55)
    SiDopingPlus.movey(-0.2)

    SiDopingPlus2 = gf.components.rectangle(size=[4.7, 22.5], layer=(6, 0))
    SiDopingPlus2 = c << SiDopingPlus2
    SiDopingPlus2.movex(10.75)
    SiDopingPlus2.movey(-0.2)

    #Contact Via for Si base
    for i in range(0,3):
        for j in range(0,13):
            ViaSi = gf.components.rectangle(size=[0.8, 0.8], layer=(40, 0))
            ViaSi = c << ViaSi
            ViaSi.movex(1.05+1.4*i)
            ViaSi.movey(0.7+1.6*j)

    for i in range(0,3):
        for j in range(0,13):
            ViaSi = gf.components.rectangle(size=[0.8, 0.8], layer=(40, 0))
            ViaSi = c << ViaSi
            ViaSi.movex(11.35+1.4*i)
            ViaSi.movey(0.7+1.6*j)
    
    #Ge layer
    Ge = gf.components.rectangle(size=[4, 20], layer=(5, 0))
    Ge = c << Ge
    Ge.movex(6)
    Ge.movey(0.5)

    #N++ doping at Ge layer
    GeDoping = gf.components.rectangle(size=[2, 18], layer=(7, 0))
    GeDoping = c << GeDoping
    GeDoping.movex(7)
    GeDoping.movey(1.5)

    #Contact via for Ge layer
    for i in range(0,2):
        for j in range(0,16):
            ViaGe = gf.components.rectangle(size=[0.5, 0.5], layer=(40, 0))
            ViaGe = c << ViaGe
            ViaGe.movex(7.23+i)
            ViaGe.movey(2.73+j)

    #Metal 1 layer for Si 
    M1forSi = gf.components.rectangle(size=[4.4, 23.1], layer=(41, 0))
    M1forSi = c << M1forSi
    M1forSi.movex(0.65)
    M1forSi.movey(-0.6)

    M1forSi2 = gf.components.rectangle(size=[4.4, 23.1], layer=(41, 0))
    M1forSi2 = c << M1forSi2
    M1forSi2.movex(10.95)
    M1forSi2.movey(-0.6)

    #Contact Via for M1 at Si base
    for i in range(0,3):
        for j in range(0,13):
            ViaM1Si = gf.components.rectangle(size=[0.8, 0.8], layer=(44, 0))
            ViaM1Si = c << ViaM1Si
            ViaM1Si.movex(1.05+1.4*i)
            ViaM1Si.movey(0.7+1.6*j)

    for i in range(0,3):
        for j in range(0,13):
            ViaM1Si = gf.components.rectangle(size=[0.8, 0.8], layer=(44, 0))
            ViaM1Si = c << ViaM1Si
            ViaM1Si.movex(11.35+1.4*i)
            ViaM1Si.movey(0.7+1.6*j)

    #Metal 2 layer for Si 
    M2forSi = gf.components.rectangle(size=[4.54, 24.2], layer=(45, 0))
    M2forSi = c << M2forSi
    M2forSi.movex(0.465)
    M2forSi.movey(-1.155)

    M2forSi = gf.components.rectangle(size=[122.45, 20], layer=(45, 0))
    M2forSi = c << M2forSi
    M2forSi.movex(-121.975)
    M2forSi.movey(0.26)

    M2forSi = gf.components.rectangle(size=[10, 110], layer=(45, 0))
    M2forSi = c << M2forSi
    M2forSi.movex(-121.975)
    M2forSi.movey(20.26)

    M2forSi2 = gf.components.rectangle(size=[4.54, 24.2], layer=(45, 0))
    M2forSi2 = c << M2forSi2
    M2forSi2.movex(11)
    M2forSi2.movey(-1.155)

    M2forSi2 = gf.components.rectangle(size=[122.45, 20], layer=(45, 0))
    M2forSi2 = c << M2forSi2
    M2forSi2.movex(15.485+0.09)
    M2forSi2.movey(0.26)

    M2forSi2 = gf.components.rectangle(size=[10, 110], layer=(45, 0))
    M2forSi2 = c << M2forSi2
    M2forSi2.movex(250-121.975)
    M2forSi2.movey(20.26)

    #Metal 1 layer for Ge 
    M1forGe = gf.components.rectangle(size=[3, 22.1], layer=(41, 0))
    M1forGe = c << M1forGe
    M1forGe.movex(6.525)
    M1forGe.movey(0.373)

    #Contact via for M1 above Ge layer
    for i in range(0,2):
        for j in range(0,13):
            ViaM1Ge = gf.components.rectangle(size=[0.8, 0.8], layer=(44, 0))
            ViaM1Ge = c << ViaM1Ge
            ViaM1Ge.movex(6.93+1.4*i)
            ViaM1Ge.movey(1.25+1.6*j)

    #Metal 2 layer for Ge 
    M2forGe = gf.components.rectangle(size=[3, 22.65], layer=(45, 0))
    M2forGe = c << M2forGe
    M2forGe.movex(6.525)
    M2forGe.movey(0.373)

    #Metal 2 taper for Ge layer
    poly1 = c.add_polygon([(6.525, 9.525, 9.525+3.5, 6.525-3.5), (23, 23, 23+7.21, 23+7.21)], layer=(45, 0))
    poly2 = c.add_polygon([(6.525-3.5, 9.525+3.5, 9.525+3.5, 6.525-3.5), (23+7.21+100.05, 23+7.21+100.05, 23+7.21, 23+7.21)], layer=(45, 0))

    #Metal 2 pad for GSG
    poly3 = c.add_polygon([(6.525-38.5, 9.525+38.5, 9.525+38.5, 6.525-38.5), (23+7.21+100.05, 23+7.21+100.05, 23+7.21+180.05, 23+7.21+180.05)], layer=(45, 0))
    poly4 = c.add_polygon([(6.525-38.5-125, 9.525+38.5-125, 9.525+38.5-125, 6.525-38.5-125), (23+7.21+100.05, 23+7.21+100.05, 23+7.21+180.05, 23+7.21+180.05)], layer=(45, 0))
    poly5 = c.add_polygon([(6.525-38.5+125, 9.525+38.5+125, 9.525+38.5+125, 6.525-38.5+125), (23+7.21+100.05, 23+7.21+100.05, 23+7.21+180.05, 23+7.21+180.05)], layer=(45, 0))

    #Via for pad open
    poly6 = c.add_polygon([(6.525-38.5, 9.525+38.5, 9.525+38.5, 6.525-38.5), (23+7.21+100.05, 23+7.21+100.05, 23+7.21+180.05, 23+7.21+180.05)], layer=(43, 0))
    poly7 = c.add_polygon([(6.525-38.5-125, 9.525+38.5-125, 9.525+38.5-125, 6.525-38.5-125), (23+7.21+100.05, 23+7.21+100.05, 23+7.21+180.05, 23+7.21+180.05)], layer=(43, 0))
    poly8 = c.add_polygon([(6.525-38.5+125, 9.525+38.5+125, 9.525+38.5+125, 6.525-38.5+125), (23+7.21+100.05, 23+7.21+100.05, 23+7.21+180.05, 23+7.21+180.05)], layer=(43, 0))

    #pad open
    poly6 = c.add_polygon([(6.525-38.5+2, 9.525+38.5-2, 9.525+38.5-2, 6.525-38.5+2), (23+7.21+100.05+2, 23+7.21+100.05+2, 23+7.21+180.05-2, 23+7.21+180.05-2)], layer=(46, 0))
    poly7 = c.add_polygon([(6.525-38.5-125+2, 9.525+38.5-125-2, 9.525+38.5-125-2, 6.525-38.5-125+2), (23+7.21+100.05+2, 23+7.21+100.05+2, 23+7.21+180.05-2, 23+7.21+180.05-2)], layer=(46, 0))
    poly8 = c.add_polygon([(6.525-38.5+125+2, 9.525+38.5+125-2, 9.525+38.5+125-2, 6.525-38.5+125+2), (23+7.21+100.05+2, 23+7.21+100.05+2, 23+7.21+180.05-2, 23+7.21+180.05-2)], layer=(46, 0))

    #Si waveguide taper for light input
    t = gf.components.taper(length=50, width1=0.5,width2=2,with_two_ports=False)
    t = c << t
    t.rotate(90)
    t.movex(8)
    t.movey(-50)

    #c.add_port(name="o1", center=[0, width / 2], width=width, orientation=180, layer=(1,12))
    c.add_port(name="o1", port=t.ports['o1'])

    return c


if __name__ == "__main__":
    c = GeSi_Photodiode()
    c.show()

