import math
from Renderer3D import Renderer3D
from Cylinder import Cylinder
from Tube import Tube
from Sphere import Sphere
from Mesh import Mesh
from Trapezoid import Trapezoid
from Frustum import Frustum
from Circle import Circle

#----------------- MESH -----------------#

# Base da peça (maior e mais imponente que a do peão)
base = Circle(radius=2.4, segments=64)
base.translate(0, -0.6, 0)

# Tronco inferior da base
trunk1 = Frustum(
    bottom_radius=2.4,
    top_radius=2.5,
    height=1.2,
    segments=64
)

# Afunilamento em direção à cintura da peça
trunk2 = Frustum(
    bottom_radius=2.5,
    top_radius=1.8,
    height=1.2,
    segments=64
)
trunk2.translate(0, 1.2, 0)

# Primeiro anel estético (anel da cintura)
ring1 = Tube(
    outer_radius=1.8,
    inner_radius=1.6,
    height=0.4,
    segments=64
)
ring1.translate(0, 1.8, 0)

# Início da subida do corpo
trunk3 = Frustum(
    bottom_radius=1.8,
    top_radius=1.9,
    height=0.8,
    segments=64
)
trunk3.translate(0, 2.2, 0)

# Afunilamento principal que conecta ao pescoço
trunk4 = Frustum(
    bottom_radius=1.9,
    top_radius=1.1,
    height=1.4,
    segments=64
)
trunk4.translate(0, 3.3, 0)

# Segundo anel estético (base do pescoço)
ring2 = Tube(
    outer_radius=1.1,
    inner_radius=0.9,
    height=0.4,
    segments=64
)
ring2.translate(0, 4.0, 0)

trunk5 = Frustum(
    bottom_radius=1.1,
    top_radius=0.9,
    height=0.3,
    segments=64
)
trunk5.translate(0, 4.15, 0)

# O pescoço elegante e alongado da queen
ring3 = Tube(
    outer_radius=0.9,
    inner_radius=0.7,
    height=3.5,
    segments=64
)
ring3.translate(0, 5.75, 0)

# A Coroa: Um tronco de cone invertido (alarga para cima)
crown_base = Frustum(
    bottom_radius=0.9,
    top_radius=1.6,
    height=1.0,
    segments=64
)
crown_base.translate(0, 8.0, 0)

# Moldura/Aro superior da coroa
crown_rim = Tube(
    outer_radius=1.6,
    inner_radius=1.4,
    height=0.3,
    segments=64
)
crown_rim.translate(0, 8.5, 0)

# Pequena esfera central tradicional no topo interno da coroa
top_sphere = Sphere(
    radius=0.4,
    stacks=16,
    sectors=32
)
top_sphere.translate(0, 8.9, 0)

#-----------------------------------------#

#----------------- Queen -----------------#
queen = Mesh()

# Juntando as partes principais do corpo
queen.merge(base)
queen.merge(trunk1)
queen.merge(trunk2)
queen.merge(ring1)
queen.merge(trunk3)
queen.merge(trunk4)
queen.merge(ring2)
queen.merge(trunk5)
queen.merge(ring3)
queen.merge(crown_base)
queen.merge(crown_rim)

# Geração procedimental dos 8 picos/bicos da coroa da queen
# Espaçados uniformemente ao redor do raio do aro superior
for i in range(8):
    angle = (2 * math.pi * i) / 8
    spike = Sphere(radius=0.15, stacks=12, sectors=12)
    
    # Posicionamento circular com base nas coordenadas trigonométricas
    sx = 1.5 * math.cos(angle)
    sz = 1.5 * math.sin(angle)
    
    spike.translate(sx, 8.65, sz)
    queen.merge(spike)

# Por fim, funde a esfera do topo central
queen.merge(top_sphere)
#------------------------------------------#

# Renderização do modelo final em 3D
renderer = Renderer3D()
renderer.render_faces(queen)

