import math

from Renderer3D import Renderer3D

from Cylinder import Cylinder
from Mesh import Mesh
from Torus import Torus
from Circle import Circle
from LatheMesh import LatheMesh
from Frustum import Frustum
from Trapezoid import Trapezoid

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

king = Mesh()

king.merge(circle1)
king.merge(torus1)
king.merge(torus2)
king.merge(cylinder1)
king.merge(torus3)
king.merge(torus4)

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

king.merge(lathe)

torus5 = Torus(major_radius=0.5, minor_radius=0.1, major_segments=64, minor_segments=32)
torus5.translate(0, 2.74, 0)

torus6 = Torus(major_radius=0.5, minor_radius=0.1, major_segments=64, minor_segments=32)
torus6.translate(0, 2.9, 0)

# frustum = Frustum(  
#     bottom_radius=0.4,
#     top_radius=0.6,
#     height=0.1,
#     segments=64
# )
# frustum.translate(0, 3, 0)

cylinder2 = Cylinder(radius=0.5, height=0.4, segments=64)

cylinder2.translate(0, 2.94, 0)

torus7 = Torus(major_radius=0.45, minor_radius=0.1, major_segments=64, minor_segments=32)
torus7.translate(0, 3.2, 0)

frustum = Frustum(

    bottom_radius=0.4,
    top_radius=0.6,
    height=0.5,
    segments=64
)

frustum.translate(0, 3.4, 0)

torus8 = Torus(major_radius=0.4, minor_radius=0.1, major_segments=64, minor_segments=32)
torus8.translate(0, 3.65, 0)

torus9 = Torus(major_radius=0.2, minor_radius=0.1, major_segments=64, minor_segments=32)
torus9.translate(0, 3.76, 0)

frustum1 = Frustum(

    bottom_radius=0.1,
    top_radius=0.1,
    height=0.1,
    segments=64
)

frustum1.translate(0, 3.9, 0)

center_y = 4.3
offset = 0.15

# Frente
trap1 = Trapezoid(
    bottom_width=0.2,
    top_width=0.4,
    height=0.4,
    depth=0.1
)

# Trás
trap2 = Trapezoid(
    bottom_width=0.2,
    top_width=0.4,
    height=0.4,
    depth=0.1
)

# Direita
trap3 = Trapezoid(
    bottom_width=0.4,
    top_width=0.2,
    height=0.4,
    depth=0.1
)

# Esquerda
trap4 = Trapezoid(
    bottom_width=0.4,
    top_width=0.2,
    height=0.4,
    depth=0.1
)

# cima
trap1.translate(0, center_y + offset, 0)

# baixo
trap2.rotate_x(math.radians(180))
trap2.translate(0, center_y - offset, 0)

# direita
trap3.rotate_z(math.radians(90))
trap3.translate(offset, center_y, 0)

# esquerda
trap4.rotate_z(math.radians(-90))
trap4.translate(-offset, center_y, 0)

king.merge(torus5) 
king.merge(torus6) 
king.merge(cylinder2)
king.merge(torus7)
king.merge(frustum) 
king.merge(torus8)
king.merge(torus9)
king.merge(frustum1)
king.merge(trap1)
king.merge(trap2)
king.merge(trap3)
king.merge(trap4)
renderer = Renderer3D()

renderer.render_faces(king)

king.export_obj('king.obj')