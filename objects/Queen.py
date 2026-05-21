from Renderer3D import Renderer3D

from Cylinder import Cylinder
from Tube import Tube
from Sphere import Sphere
from Mesh import Mesh
from Trapezoid import Trapezoid
from Frustum import Frustum
from Circle import Circle

circle = Circle()

#----------------- MESH -----------------#

trunk1 = Frustum(
    bottom_radius=1.9,
    top_radius=2,
    height=1.0,
    segments=64
)

trunk2 = Frustum(

    bottom_radius=2,
    top_radius=1.5,
    height=1.0,
    segments=64
)

trunk2.translate(0, 1, 0)

ring1 = Tube(

    outer_radius=1.5,
    inner_radius=1.4,
    height=0.5,
    segments=64
)

ring1.translate(0, 1.5, 0)

trunk3 = Frustum(
    bottom_radius=1.5,
    top_radius=1.6,
    height=0.8,
    segments=64
)

trunk3.translate(0, 2, 0)

trunk4 = Frustum(

    bottom_radius=1.6,
    top_radius=0.8,
    height=1.0,
    segments=64
)

trunk4.translate(0, 2.9, 0)

ring2 = Tube(

    outer_radius=0.8,
    inner_radius=0.7,
    height=0.5,
    segments=64
)

ring2.translate(0, 3.4, 0)

trunk5 = Frustum(

    bottom_radius=0.8,
    top_radius=0.7,
    height=0.2,
    segments=64
)

trunk5.translate(0, 3.75, 0)

ring3 = Tube(

    outer_radius=0.7,
    inner_radius=0.6,
    height=3,
    segments=64
)

ring3.translate(0, 4, 0)

trunk6 = Frustum(

    bottom_radius=0.7,
    top_radius=1.1,
    height=0.1,
    segments=64
)

trunk6.translate(0, 5.5, 0)

ring4 = Tube(

    outer_radius=1.1,
    inner_radius=1,
    height=0.2,
    segments=64
)

ring4.translate(0, 5.7, 0)

trunk7 = Frustum(

    bottom_radius=1.1,
    top_radius=0.7,
    height=0.5,
    segments=64
)

trunk7.translate(0, 6.05, 0)

ring5 = Tube(

    outer_radius=0.7,
    inner_radius=0.6,
    height=0.5,
    segments=64
)

ring5.translate(0, 6.1, 0)

sphere1 = Sphere(

    radius=1.2,

    stacks=32,

    sectors=64
)

sphere1.translate(0, 7.45, 0)
#-----------------------------------------#

#----------------- QUEEN -----------------#
queen = Mesh()
queen.merge(circle)
queen.merge(trunk1)
queen.merge(trunk2)
queen.merge(ring1)
queen.merge(trunk3)
queen.merge(trunk4)
queen.merge(ring2)
queen.merge(trunk5)
queen.merge(ring3)
queen.merge(trunk6)
queen.merge(ring4)
queen.merge(trunk7)
queen.merge(ring5)
queen.merge(sphere1)
#-----------------------------------------#

renderer = Renderer3D()

renderer.render_faces(queen)