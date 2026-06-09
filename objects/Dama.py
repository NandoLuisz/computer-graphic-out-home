from Cylinder import Cylinder 
from Tube import Tube 
from Renderer3D import Renderer3D
from Mesh import Mesh

dama = Mesh()

base1 = Cylinder(

    radius=2,
    height=1.0,
    segments=64
)

ring1 = Tube(

    outer_radius=1.7,
    inner_radius=1.4,
    height=0.5,
    segments=64
)

ring1.translate(0, 0.5, 0)

ring2 = Tube(

    outer_radius=1.2,
    inner_radius=0.8,
    height=0.5,
    segments=64
)

ring3 = Tube(

    outer_radius=0.8,
    inner_radius=0.5,
    height=0.5,
    segments=64
)

ring3.translate(0, 0.5, 0)

dama.merge(base1)

dama.merge(ring1)

dama.merge(ring2)

dama.merge(ring3)

renderer = Renderer3D()

renderer.render_faces(dama)