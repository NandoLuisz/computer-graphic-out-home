from Vec3 import Vec3
from Mat4 import Mat4

class Mesh:
    def __init__(self):
        self.vertices = []
        self.faces = []
        self.face_colors = []
        self.normals = []
        self.color = (1.0, 1.0, 1.0) # Cor padrão branca

    def merge(self, other_mesh):

        offset = len(self.vertices)

        # adiciona vértices
        for v in other_mesh.vertices:

            self.vertices.append(v)

        # adiciona faces corrigindo índices
        for face in other_mesh.faces:

            new_face = (

                face[0] + offset,
                face[1] + offset,
                face[2] + offset
            )

            self.faces.append(new_face)

        # adiciona normais
        for n in other_mesh.normals:

            self.normals.append(n)

        # adiciona cores
        if hasattr(other_mesh, "face_colors"):

            if not hasattr(self, "face_colors"):

                self.face_colors = []

            self.face_colors.extend(
                other_mesh.face_colors
            )
            
    def compute_normals(self):
        self.normals = []
        for face in self.faces:
            v1 = self.vertices[face[0]]
            v2 = self.vertices[face[1]]
            v3 = self.vertices[face[2]]
            edge1 = v2 - v1
            edge2 = v3 - v1
            normal = edge1.cross(edge2).normalize()
            self.normals.append(normal)
    
    def transform(self, matrix):

        for i, v in enumerate(self.vertices):

            transformed = matrix * [v.x, v.y, v.z, 1]

            self.vertices[i] = Vec3(
                transformed[0],
                transformed[1],
                transformed[2]
            )

        self.compute_normals()

        return self
    
    def translate(self, tx, ty, tz):
        translation_matrix = Mat4.translation(tx, ty, tz)
        self.transform(translation_matrix)

    def rotate_x(self, angle):
        rotation_matrix = Mat4.rotation_x(angle)
        self.transform(rotation_matrix)
    
    def rotate_y(self, angle):
        rotation_matrix = Mat4.rotation_y(angle)
        self.transform(rotation_matrix)

    def rotate_z(self, angle):
        rotation_matrix = Mat4.rotation_z(angle)
        self.transform(rotation_matrix)

    def scale(self, sx, sy, sz):
        scaling_matrix = Mat4.scaling(sx, sy, sz)
        self.transform(scaling_matrix)
    
    def __repr__(self): 
        return f"Mesh(vertices={self.vertices}, faces={self.faces}, normals={self.normals}, color={self.color})"
    
    def clone(self):
        new_mesh = Mesh()
        new_mesh.vertices = [Vec3(v.x, v.y, v.z) for v in self.vertices]
        new_mesh.faces = [tuple(face) for face in self.faces]
        new_mesh.normals = [Vec3(n.x, n.y, n.z) for n in self.normals]
        new_mesh.color = self.color
        return new_mesh
    


