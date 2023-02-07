from manim import *

class test(VectorScene):
    def construct(self):
        titulo6 = Title("Characteristics and Special Matrices")
        self.add(titulo6)
        
        titulo7 = Title("Special Matrices")
        
        self.play(ReplacementTransform(titulo6, titulo7))
        
        trText = Text("Transpose of A", t2c={"A":GREEN}, font_size=42, slant=ITALIC).next_to(titulo7, DOWN).to_edge(LEFT)
        
        aSymbol = MathTex(r"A = ", tex_to_color_map={"A":GREEN}).next_to(trText, DOWN).shift(DOWN)
        aMatrix = Matrix([[1, 2], [3, 4]]).next_to(aSymbol, RIGHT)
        
        trMatrix = Matrix([[1, 3], [2, 4]]).next_to(aMatrix, DOWN)
        trSymbol = MathTex(r"A^T = ", tex_to_color_map={"A":GREEN, "T":RED}).next_to(trMatrix, LEFT)
        
        transpose = VGroup(trText, aSymbol, aMatrix, trSymbol, trMatrix).shift(DOWN)
        
        self.play(Create(transpose))
        
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
        

        
        
        
