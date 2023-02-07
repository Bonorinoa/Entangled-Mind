from manim import *

# 1. 2-dimensional vector space and two vectors inside of it
# 2. show how vector addition looks like
# 3. Properties of Linear Algebra in a nice text visual
# 4. Inner Product
# 5. Norms 
# 6. Outer product
# 7. Vector to Matrix characteristics and special matrices
## such as Transpose, Identity, Diagonal, Row Echelon Form
# 8. Determinant
# 9. Matrix inversion
# 10. Characteristic equation
# DONE
class LinAlgebra(VectorScene):
    def construct(self):
        # Scene 1
        
        plane = NumberPlane()

        vec_1 = Vector([1, 2])
        vec_2 = Vector([-3, -2], color=YELLOW)
        vec_3 = Arrow(start=[-3, -2, 0], end=[1,2,0], color=RED)
        label_1 = vec_1.coordinate_label()
        label_2 = vec_2.coordinate_label(color=YELLOW)
        
        self.play(Create(plane))
        self.play(Create(vec_1), FadeIn(label_1))
        self.play(Create(vec_2), FadeIn(label_2))
        
        v1 = Tex(r"\[a = \begin{bmatrix} 1 \\ 2 \end{bmatrix}\]")
        v2 = Tex(r" \[+\begin{bmatrix} -3 \\ -2 \end{bmatrix}\]").next_to(v1, RIGHT)
        res = Tex(r" \[= \begin{bmatrix} -2 \\ 0 \end{bmatrix}\]", color=RED).next_to(v2, RIGHT)
        
        self.wait(5)

        self.next_section("Now vector addition")
        
        titulo = Title("Vector Addition")
        
        labels = VGroup(v1, v2, res)
        
        self.play(Write(titulo), Create(labels.to_corner(UL*2).scale(0.65)))
        self.play(Create(vec_3))
        
        vectores = VGroup(vec_1, vec_2, vec_3)
        
        self.wait(5)
        
        self.remove(titulo)
        
        self.next_section("Direction")
        # recrea el ejemplo del articulo
        titulo2 = Title("Direction of vector after addition")
        
        vec_4 = Arrow(start=[2, 1, 0], end=[0,0,0], color = BLUE, max_tip_length_to_length_ratio=0.4)
        vec_5 = Arrow(start=[0,0,0], end=[2, -1, 0], color = BLUE, max_tip_length_to_length_ratio=0.4)
        vec_6 = Arrow(start=[2, 1, 0], end=[2, -1, 0], color=GREEN)
        label_a = Tex("a").next_to(vec_4, UP*0.3).scale(0.8)
        label_b = Tex("b").next_to(vec_5, DOWN*0.3).scale(0.8)
        label6 = Tex("a + b").next_to(vec_6, RIGHT)
        
        vectores2a = VGroup(vec_4, vec_5, vec_6, label6, label_a, label_b)
        
        # titulo, eliminar cosas viejas
        self.play(ReplacementTransform(labels, titulo2), Uncreate(VGroup(label_1, label_2, plane)))
        # reemplazar grupo vectores por los tres nuevos ejemplos
        self.play(Uncreate(vectores), Create(vectores2a))
        self.play(vectores2a.animate.move_to(LEFT*2))
        
        vec_7 = Arrow(start=[0, 0, 0], end=[2,1,0], color = BLUE, max_tip_length_to_length_ratio=0.4)
        vec_8 = Arrow(start=[0,0,0], end=[2, -1, 0], color = BLUE, max_tip_length_to_length_ratio=0.4)
        vec_9 = Arrow(start=[2, 1, 0], end=[2, -1, 0], color=GREEN)
        label_a2 = Tex("a").next_to(vec_7, UP*0.3).scale(0.8)
        label_b2 = Tex("b").next_to(vec_8, DOWN*0.3).scale(0.8)
        label9 = Tex("b - a").next_to(vec_9, RIGHT)
        
        vectores2b = VGroup(vec_7, vec_8, vec_9, label9, label_a2, label_b2)
        
        self.play(Create(vectores2b))
        self.play(vectores2b.animate.move_to(RIGHT*2))
                
        vec_10 = Arrow(start=[0, 0, 0], end=[2,1,0], color = BLUE, max_tip_length_to_length_ratio=0.4)
        vec_11 = Arrow(start=[0,0,0], end=[2, -1, 0], color = BLUE, max_tip_length_to_length_ratio=0.4)
        vec_12 = Arrow(start=[2, -1, 0], end=[2, 1, 0], color=GREEN)
        label_a3 = Tex("a").next_to(vec_11, DOWN*0.3).scale(0.8)
        label_b3 = Tex("b").next_to(vec_10, DOWN*0.3).scale(0.8)
        label12 = Tex("a - b").next_to(vec_12, RIGHT)
        
        vectores2c = VGroup(vec_10, vec_11, vec_12, label12, label_a3, label_b3)
        
        self.play(Create(vectores2c.shift(DOWN*2)))
        self.play(vectores2c.animate.move_to(LEFT + DOWN*2))        
        
        self.wait(5)
        
        self.clear()
        
        self.next_section("List of properties") 
        
        titulo3 = Title("Properties of Vector Operations")
        
        # commutativity
        c = Tex("Commutativity: ", color = GREEN)
        cm = MathTex(r"a + b = b + a; a \cdot b = b \cdot a").next_to(c, RIGHT)
        vc = VGroup(c, cm).scale(0.75).next_to(titulo3, DOWN).shift(2*LEFT + DOWN)
        
        # Associativity
        a = Tex("Associativity: ", color = GREEN)
        am = MathTex(r"a + (b+c) = (a+b) + c; a \cdot (b \cdot c) = (a \cdot b) \cdot c").next_to(a, RIGHT)
        va = VGroup(a, am).scale(0.75).next_to(vc, DOWN)
        
        # Zero element 
        z = Tex("Zero element: ", color = GREEN).next_to(a, DOWN)
        zm = MathTex(r"a + 0 = a").next_to(z, RIGHT)
        zt = Tex("Where 0 is called a zero vector.").next_to(zm, RIGHT)
        vz = VGroup(z, zm, zt).scale(0.75).next_to(va, DOWN)        
        
        # Distributibity
        d = Tex("Distributibity: ", color = GREEN).next_to(z, DOWN)
        dm = MathTex(r"a \cdot (b + c) = (a \cdot b) + (a \cdot c)").next_to(d, RIGHT)
        vd = VGroup(d, dm).scale(0.75).next_to(vz, DOWN)        
        
        # Additive Identity
        aid = Tex("Additive Identity: ", color = GREEN).next_to(d, DOWN)
        aidm = MathTex(r"1 \cdot a = a").next_to(aid, RIGHT)
        aidt = Tex("Where 1 is the identity element.").next_to(aidm, RIGHT)
        vaid = VGroup(aid, aidm, aidt).scale(0.75).next_to(vd, DOWN)        
        
        # Additive Inverse
        ai = Tex("Additive Inverse: ", color = GREEN).next_to(aid, DOWN)
        aim = MathTex(r" a + (-a) = 0").next_to(ai, RIGHT)
        vai = VGroup(ai, aim).scale(0.75).next_to(vaid, DOWN)         
        
        self.play(Write(titulo3))
        
        properties = VGroup(vc, va, vz, vd, vaid, vai).arrange(DOWN)
        self.play(Create(properties))
        
        self.play(vc.animate.shift(LEFT), vd.animate.shift(LEFT), vai.animate.shift(LEFT*2))
        
        self.play(properties.animate.scale(1.2))
        
        self.wait(5)
        
        self.clear()
        
        self.next_section("Inner Product") 
        
        titulo4 = Title("Inner (Dot) Product")
        
        self.play(Write(titulo4))
        
        vect1 = Matrix([[1, 3, 5]]).shift(LEFT*2)
        dot = Dot().next_to(vect1, RIGHT)
        vect2 = Matrix([[2,], [4,], [6,]]).next_to(dot, RIGHT)
        
        vectGroup = VGroup(vect1, dot, vect2)
        
        self.play(FadeIn(vectGroup), run_time=4)
        
        self.wait()
        
        equal = Text(" = ").next_to(vectGroup, RIGHT)
        prod = MathTex(r"1 \cdot 2 + 3 \cdot 4 + 5 \cdot 6").next_to(equal, RIGHT)
        
        self.play(Create(equal), Write(prod))
        
        self.wait(2)
        
        text = Text("Scalar", font_size=22, color=GREEN).next_to(prod, DOWN)
        
        self.play(Create(text))
        
        self.wait(3)
        
        lenVec = MathTex(r"| a | = \sqrt{a_i \cdot a_i} = \sqrt{a^2_1 + a^2_2 + ... + a^2_i").scale(0.85)
        
        self.play(Uncreate(equal), Uncreate(prod), Uncreate(text))
        self.play(ReplacementTransform(vectGroup, lenVec))
        
        self.wait(5)
        
        cos = MathTex(r"cos(\Theta) = \frac{a \cdot b}{|a| \cdot |b|}").scale(0.85)
        
        self.play(ReplacementTransform(lenVec, cos))
        
        self.wait(5)
        
        self.clear()
        
        self.next_section("Outer product")
         
        titulo5 = Title("Outer (Matrix) Product")
               
        vect3 = Matrix([["a1",], ["a2",], ["a3",]]).shift(LEFT*2)
        tensorProd = MathTex(r"\otimes").next_to(vect3, RIGHT)
        vect4 = Matrix([["b1","b2","b3"]]).next_to(tensorProd, RIGHT)
        
        label3 = Tex(r"n X 1").next_to(vect3, DOWN)
        label4 = Tex(r"1 X n").next_to(vect4, DOWN)
        
        equal2 = Tex(" = ").next_to(vect4, RIGHT)
        
        resProd = Matrix([["a1b1", "a1b2", "a1b3"],
                          ["a2b1", "a2b2", "a2b3"],
                          ["a3b1", "a3b2", "a3b3"]]).next_to(equal2, RIGHT)
        
        labelRes = Tex(r"n X n").next_to(resProd, DOWN)
        
        labelGroup = VGroup(label3, label4, labelRes).scale(0.7).shift(LEFT*2)
        vectGroup2 = VGroup(vect3, tensorProd, vect4, equal2, resProd).shift(LEFT*2).scale(0.8)
        
        self.play(Create(titulo5))
        
        self.play(Create(vectGroup2), Write(labelGroup))
        self.play(labelGroup.animate.set_color(GREEN))
        
        self.wait(3)
        
        self.clear()
        
        self.next_section("Characteristics and Special Matrices")
        
        titulo6 = Title("Characteristics and Special Matrices")
        rank = Text("Rank = maximum number of linearly independent rows/columns in that matrix",
                    t2s={'Rank':ITALIC}, t2w={'Rank':BOLD},
                    font_size=24)
        LD = Text("Linearly Independent = cannot be represented as a linear combination of\n any other vector in the matrix",
                    t2s={'Linearly Independent':ITALIC}, t2w={'Linearly Independent':BOLD},
                    font_size=24)
        
        initGroup = VGroup(titulo6, LD.to_edge(DOWN), rank.next_to(LD, UP))
        
        scalar = Text("Scalar = Tensor of Rank 0", t2c={'Scalar':GREEN, '0':GREEN}, font_size=34)
        vector = Text("Vector = Tensor of Rank 1", t2c={'Vector':YELLOW, '1':YELLOW}, font_size=34)
        matrix = Text("Matrix = Tensor of Rank 2", t2c={'Matrix':BLUE, '2':BLUE}, font_size=34)
        tensor = Text("Tensors = Tensor of Rank n>2", t2c={'Tensors':RED, 'n>2':RED}, font_size=34)
        
        self.play(Create(initGroup))
        
        self.play(Write(scalar))
        
        self.wait(2)
        
        self.play(scalar.animate.next_to(titulo6, DOWN*2), Write(vector))

        self.wait(2)
        
        self.play(vector.animate.next_to(scalar, DOWN), Write(matrix))
        
        self.wait(2)      
        
        self.play(matrix.animate.next_to(vector, DOWN), Write(tensor))
        
        self.wait(2)
        
        ranksGroup = VGroup(scalar, vector, matrix)
        self.play(ranksGroup.animate.next_to(tensor, UP))
        
        fullGroup = VGroup(LD, rank, ranksGroup, tensor)
        
        self.wait(5) 
        
        titulo7 = Title("Special Matrices")
        
        self.play(ReplacementTransform(titulo6, titulo7))
        
        trText = Text("Transpose of A", t2c={"A":GREEN}, font_size=42, slant=ITALIC).next_to(titulo7, DOWN).to_edge(LEFT)
        
        aSymbol = MathTex(r"A = ", tex_to_color_map={"A":GREEN}).next_to(trText, DOWN).shift(DOWN)
        aMatrix = Matrix([[1, 2], [3, 4]]).next_to(aSymbol, RIGHT)
        
        trMatrix = Matrix([[1, 3], [2, 4]]).next_to(aMatrix, DOWN)
        trSymbol = MathTex(r"A^T = ", tex_to_color_map={"A":GREEN, "T":RED}).next_to(trMatrix, LEFT)
        
        transpose = VGroup(trText, aSymbol, aMatrix, trSymbol, trMatrix).shift(DOWN)
        
        self.play(ReplacementTransform(fullGroup, transpose))
        
        self.wait(4)
        
        idText = Text("Identity Matrix I", t2c={"I":GREEN}, font_size=42, slant=ITALIC).next_to(titulo7, DOWN).to_edge(LEFT)
        
        idSymbol = MathTex(r"I = ", tex_to_color_map={"I":GREEN}).next_to(idText, DOWN).shift(DOWN)
        idMatrix = Matrix([[1, 0], [0, 1]]).next_to(idSymbol, RIGHT)
        
        identity = VGroup(idText, idSymbol, idMatrix).shift(DOWN)
        
        self.play(ReplacementTransform(transpose, identity))
        
        self.wait(4)
        
        diText = Text("Diagonal Matrix Dg", t2c={"Dg":GREEN}, font_size=42, slant=ITALIC).next_to(titulo7, DOWN).to_edge(LEFT)
                
        diSymbol = MathTex(r"Dg = ", tex_to_color_map={"Dg":GREEN}).next_to(diText, DOWN).shift(DOWN)
        diMatrix = Matrix([["n", 0], [0, "m"]]).next_to(diSymbol, RIGHT)
        
        diagonal = VGroup(diText, diSymbol, diMatrix).shift(DOWN)
        
        self.play(ReplacementTransform(identity, diagonal))
        
        self.wait(4)
        
        rreText = Text("Reduced Row-Echelon Matrix RRE", t2c={"RRE":GREEN}, font_size=42, slant=ITALIC).next_to(titulo7, DOWN).to_edge(LEFT)
                
        rreSymbol = MathTex(r"RRE = ", tex_to_color_map={"RRE":GREEN}).next_to(rreText, DOWN).shift(DOWN)
        rreMatrix = Matrix([[1, 0], [0, 1]]).next_to(rreSymbol, RIGHT)
        
        rrechelon = VGroup(rreText, rreSymbol, rreMatrix).shift(DOWN)
        
        self.play(ReplacementTransform(diagonal, rrechelon))
        
        self.wait(5)
        
        self.clear()
        
        self.next_section("Determinant")
        
        titulo8 = Title("Determinant")
        
        self.play(Write(titulo8))
        
        A = Text("A = ").next_to(titulo8, DOWN).to_edge(LEFT).shift(DOWN)
        
        matrixA = Matrix([
            [2, 0],
            [-1, 1]
        ]).next_to(A, RIGHT)

        detText = Text("det A = ").next_to(A, DOWN).shift(DOWN)
        calcDet = MathTex(r"((2 \cdot 1) - (0 \cdot (-1)) = 3").next_to(detText, RIGHT)

        det = get_det_text(matrixA,
                    determinant=3,
                    initial_scale_factor=2).scale(0.8)
        
        detGroup = VGroup(A, matrixA, calcDet, detText)

        self.play(Create(detGroup))

        self.play(detGroup.animate.move_to(ORIGIN))
        self.play(detGroup.animate.scale(0.8))
        
        self.wait(3)
        self.remove(matrixA, A)
        
        self.play(VGroup(calcDet, detText).animate.shift(UP))
        
        self.play(FadeIn(matrixA.next_to(calcDet, DOWN)))
        
        self.play(FadeIn(det.next_to(calcDet, DOWN)))
        
        self.play(matrixA.animate.shift(RIGHT * 0.24))
        
        self.wait(5)
                
        self.clear()
        
        self.next_section("Matrix Inversion")
        
        titulo9 = Title("The Inverse of a Matrix")
        
        A = Tex(r"A = ", tex_to_color_map ={"A":GREEN}).move_to(ORIGIN)
        mat = Matrix([["a", "b"], ["c", "d"]]).next_to(A, RIGHT)
        
        invA = MathTex(r"A^{-1} = \frac{1}{(a \cdot d) - (b \cdot c)}", tex_to_color_map ={r"A^{-1}":RED})
        invMat = Matrix([["a", "-b"], ["-c", "a"]]).next_to(invA, RIGHT)
        
        condition = MathTex(r"A \cdot A^{-1} = ", tex_to_color_map ={"A ":GREEN, r"A^{-1}":RED}).move_to(ORIGIN).shift(DOWN)
        idMatrix = Matrix([[1, 0], [0, 1]]).next_to(condition, RIGHT)
        idSymbol = Tex(r" = I").next_to(idMatrix, RIGHT)
        
        self.play(Write(titulo9))
        
        group1 = VGroup(A, mat)
        
        self.play(Create(group1))
        self.wait(3)
        self.play(group1.animate.next_to(titulo9, DOWN).to_edge(LEFT))

        group2 = VGroup(invA, invMat)
        
        self.play(Create(group2))
        self.wait(4)
        self.play(group2.animate.next_to(mat, RIGHT).to_edge(RIGHT))
        
        group3 = VGroup(condition, idMatrix, idSymbol)
        
        self.play(Create(group3))
        self.play(group3.animate.shift(LEFT))
        
        self.wait(3)
        
        bigGroup = VGroup(group1, group2, group3)
        self.play(bigGroup.animate.shift(DOWN))
        
        self.wait(5)
        
        self.clear()
        
        self.next_section("Eigen stuff")
        
        titulo10 = Title("Some Eigen Stuff")
        
        ax = Axes()
        plane = NumberPlane()
        
        self.add(titulo10, ax)
        
        vec1 = Vector([3, 0], color=GREEN)
        vec2 = Vector([1, 2], color=RED)
        
        eigenvector = Vector([1, -1], color=YELLOW)
        
        initGroup = VGroup(plane, vec1, vec2, eigenvector).scale(0.8)
        
        self.play(Create(initGroup))
        
        line1 = Line(start=[-5,5,0], end=[5, -5, 0], color=YELLOW)
        
        line2 = Line(start=[-6,0,0], end=[6, 0, 0], color=GREEN)
        
        line3 = Line(start=[-4,-8,0], end=[4, 8, 0], color=RED)
        
        lines = VGroup(line1, line2, line3)
        
        self.play(Create(lines))
        
        matrix = [[3, 1],
                  [0, 2]]
        self.play(ApplyMatrix(matrix, initGroup))
        
        self.wait(5)

        
        
        