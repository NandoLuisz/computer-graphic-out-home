from Renderer3D import Renderer3D

from Mesh import Mesh

tower = Mesh.load_obj("tower.obj")

renderer = Renderer3D()

renderer.render_faces(tower)