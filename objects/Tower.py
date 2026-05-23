from Renderer3D import Renderer3D

from Cylinder import Cylinder
from Tube import Tube
from Mesh import Mesh
from Torus import Torus
from Circle import Circle
from LatheMesh import LatheMesh
from Frustum import Frustum
from Box import Box

import math

circle1 = Circle(radius=0.9, segments=64)

torus1 = Torus(

    major_radius=0.9,
    minor_radius=0.1,

    major_segments=64,
    minor_segments=32
)

torus2 = Torus(

    major_radius=0.5,
    minor_radius=0.4,

    major_segments=64,
    minor_segments=32
)


cylinder1 = Cylinder(radius=0.6, height=0.1, segments=64)

torus3 = Torus(

    major_radius=0.6,
    minor_radius=0.1,

    major_segments=64,
    minor_segments=32
)


torus4 = Torus(

    major_radius=0.6,
    minor_radius=0.1,

    major_segments=64,
    minor_segments=32
)

torus2.translate(0, 0.4, 0)

cylinder1.translate(0, 0.85, 0)

torus3.translate(0, 1.0, 0)

torus4.translate(0, 1.2, 0)

tower = Mesh()

tower.merge(circle1)
tower.merge(torus1)
tower.merge(torus2)
tower.merge(cylinder1)
tower.merge(torus3)
tower.merge(torus4)

# =====================================
# LATHE
# =====================================

profile = [

    (0.60, 1.30),
    (0.59, 1.40),
    (0.58, 1.50),

    (0.57, 1.60),
    (0.56, 1.70),

    (0.55, 1.80),
    (0.54, 1.90),

    (0.53, 2.00),
    (0.52, 2.10),

    (0.51, 2.20),
    (0.50, 2.30),

    (0.51, 2.40),
    (0.52, 2.50),

    (0.53, 2.60),
    (0.54, 2.70),
]

lathe = LatheMesh(

    profile_points=profile,

    segments=64
)

tower.merge(lathe)

cylinder2 = Cylinder(radius=0.6, height=0.08, segments=64)
cylinder2.translate(0, 2.74, 0)

frustum = Frustum(

    bottom_radius=0.4,
    top_radius=0.6,
    height=0.1,
    segments=64
)

frustum.translate(0, 2.79, 0)

cylinder3 = Cylinder(radius=0.6, height=0.2, segments=64)

cylinder3.translate(0, 2.94, 0)

box1 = Box(
    width=0.6,
    height=0.40,
    depth=0.1
)
box1.rotate_y(math.radians(0))
box1.translate(0, 3.09, 0.62)


box2 = Box(
    width=0.6,
    height=0.40,
    depth=0.1
)
box2.rotate_y(math.radians(180))
box2.translate(0, 3.09, -0.62)


box3 = Box(
    width=0.6,
    height=0.40,
    depth=0.1
)
box3.rotate_y(math.radians(90))
box3.translate(0.62, 3.09, 0)


box4 = Box(
    width=0.6,
    height=0.40,
    depth=0.1
)
box4.rotate_y(math.radians(270))
box4.translate(-0.62, 3.09, 0)

tower.merge(cylinder2) 
tower.merge(frustum) 
tower.merge(cylinder3) 
tower.merge(box1) 
tower.merge(box2) 
tower.merge(box3) 
tower.merge(box4)

renderer = Renderer3D()

renderer.render_faces(tower)