from manim import *

class test(VectorScene):
    def construct(self):
        
        titulo7 = Title("Special Matrices")
        self.play(Write(titulo7))

        colors = [YELLOW, BLUE, PURPLE_A]

        tr_text = Text("Transpose of A", t2c={"A":GREEN}, font_size=36, slant=ITALIC).next_to(titulo7, DOWN).to_edge(LEFT)

        a_symbol = MathTex(r"A = ", tex_to_color_map={"A":GREEN}).next_to(tr_text, DOWN).shift(DOWN)
        a_matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], left_bracket="[", right_bracket="]").next_to(a_symbol, RIGHT)
        for i in range(3):
            columns = a_matrix.get_columns()
            rect = SurroundingRectangle(columns[i], color=colors[i], fill_color=colors[i], fill_opacity=0.5).shift(DOWN)
            self.add(rect)

        tr_matrix = Matrix([[1, 4, 7], [2, 5, 8], [3, 6, 9]], left_bracket="[", right_bracket="]").next_to(a_matrix, RIGHT)
        tr_symbol = MathTex(r"A^T = ", tex_to_color_map={"A":GREEN, "T":RED}).next_to(tr_matrix, LEFT)
        for i in range(3):
            rows = tr_matrix.get_rows()
            rect = SurroundingRectangle(rows[i], color=colors[i], fill_color=colors[i], fill_opacity=0.5).shift(DR+RIGHT)
            self.add(rect)

        orig = VGroup(a_symbol, a_matrix).shift(DOWN)
        transpose = VGroup(tr_text, tr_symbol, tr_matrix).shift(DR+RIGHT)
        self.add(orig, transpose)

        self.wait(4)
        self.clear()

        idText = Text("Identity Matrix I", t2c={"I":GREEN}, font_size=42, slant=ITALIC).next_to(titulo7, DOWN).to_edge(LEFT)

        idSymbol = MathTex(r"I = ", tex_to_color_map={"I":GREEN}).next_to(idText, DOWN).shift(DOWN)
        idMatrix = IntegerMatrix([[1, 0], [0, 1]], left_bracket="[", right_bracket="]").next_to(idSymbol, RIGHT)

        identity = VGroup(idText, idSymbol, idMatrix).shift(DOWN)

        self.play(ReplacementTransform(transpose, identity))

        self.wait(4)
        self.clear()

        diText = Text("Diagonal Matrix Dg", t2c={"Dg":GREEN}, font_size=42, slant=ITALIC).next_to(titulo7, DOWN).to_edge(LEFT)
            
        diSymbol = MathTex(r"Dg = ", tex_to_color_map={"Dg":GREEN}).next_to(diText, DOWN).shift(DOWN)
        diMatrix = Matrix([["n", 0], [0, "m"]]).next_to(diSymbol, RIGHT)

        diagonal = VGroup(diText, diSymbol, diMatrix).shift(DOWN)

        self.play(ReplacementTransform(identity, diagonal))

        self.wait(4)
        self.clear()

        title = Text("Reducing a Matrix to Echelon Form", font_size=36, slant=ITALIC).to_edge(UP)
        self.add(title)

        original_matrix_text = Text("Original Matrix", t2c={"Original Matrix":GREEN}, font_size=36, slant=ITALIC).next_to(title, DOWN).to_edge(LEFT)
        original_matrix = Matrix([[3, 7, 4], [2, 8, 9], [6, 5, 7]], left_bracket="[", right_bracket="]").next_to(original_matrix_text, DOWN).to_edge(LEFT)

        original_group = VGroup(original_matrix_text, original_matrix).shift(DOWN)

        self.play(Write(original_group.shift(UP*0.7)))

        self.wait(2)

        reduced_matrix_text = Text("Echelon Matrix", t2c={"Echelon Matrix":GREEN}, font_size=36, slant=ITALIC).next_to(title, DOWN).to_edge(RIGHT)
        reduced_matrix = Matrix([[3, 7, 4], [0, 2, 5], [0, 0, 1]], left_bracket="[", right_bracket="]").next_to(reduced_matrix_text, DOWN).to_edge(RIGHT)

        reduced_group = VGroup(reduced_matrix_text, reduced_matrix).next_to(original_group, RIGHT)

        self.play(FadeIn(reduced_group.shift(DOWN*0.5)))

        self.wait(2)

        echelon_matrix_text = Text("Reduced\n Echelon Matrix", t2c={"Reduced\n Echelon Matrix":GREEN}, font_size=36, slant=ITALIC).next_to(title, DOWN).to_edge(RIGHT)
        echelon_matrix = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]], left_bracket="[", right_bracket="]").next_to(echelon_matrix_text, DOWN).to_edge(RIGHT)

        echelon_group = VGroup(echelon_matrix_text, echelon_matrix).next_to(reduced_group, RIGHT)

        self.play(Write(echelon_group.shift(DOWN*0.2)))

        self.wait(2)

        rre_group = VGroup(original_group, reduced_group, echelon_group)

        self.play(rre_group.animate.move_to(ORIGIN))

        self.wait(5)

        self.clear()

        
        
        
