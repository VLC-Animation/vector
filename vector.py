from manim import *

VTEX = TexTemplateLibrary.ctex
TIME_DELAY = 0

class Chieu(Scene):
    def construct(self):
        #Slide 48
        text_1 = Tex('Chiều', tex_template=VTEX).shift(UP*3)
        self.play(Write(text_1))
        self.wait(TIME_DELAY)

        #Slide 49
        text_2 = Tex('Điểm đầu bên trái', tex_template=VTEX).shift(DOWN*3)
        circle_1 = Circle(radius=0.1, color=GREY, fill_color=GREY, fill_opacity=1)
        circle_2 = circle_1.copy()
        circle_3 = circle_1.copy().shift(DOWN*0.3)
        circle_1.shift(UP*0.3)
        
        self.play(Write(circle_1), Write(circle_2), Write(circle_3), Write(text_2))
        self.wait(TIME_DELAY)

        #Slide 50
        text_2_2 = Tex('Điểm đầu bên trái, điểm cuối bên phải', tex_template=VTEX).shift(DOWN*3)
        circle_1_copy = circle_1.copy().shift(UP+RIGHT*3)
        circle_2_copy = circle_2.copy().shift(RIGHT*3)
        circle_3_copy = circle_3.copy().shift(DOWN+RIGHT*3)
        arrow_1 = Arrow(circle_1, circle_1_copy, color=GREEN, buff=0)
        arrow_2 = Arrow(circle_2, circle_2_copy, color=GREEN, buff=0)
        arrow_3 = Arrow(circle_3, circle_3_copy, color=GREEN, buff=0)
        arrow_group = VGroup(arrow_1, arrow_2, arrow_3)
        circle_group_2 = VGroup(circle_1_copy, circle_2_copy, circle_3_copy)
        circle_group_1 = VGroup(circle_1, circle_2, circle_3)
        circle_group_1_copy = circle_group_1.copy()
        
        self.play(ReplacementTransform(text_2, text_2_2), Write(arrow_group), Write(circle_group_1), ReplacementTransform(circle_group_1_copy, circle_group_2))
        self.wait(TIME_DELAY)

        #Slide 51
        text_3 = Tex('Vector có chiều từ trái sang phải', tex_template=VTEX).shift(DOWN*3)
        self.play(ReplacementTransform(text_2_2, text_3))
        self.play(FadeOut(circle_group_1, circle_group_2))
        self.wait(TIME_DELAY)

        #Slide 52
        position_arrow_group = arrow_group.get_center()
        arrow_group_2 = arrow_group.copy().flip().set_color(ORANGE).shift(-2*position_arrow_group)
        text_4 = Tex('Vector có chiều từ phải sang trái', tex_template=VTEX).shift(DOWN*3)
        self.play(Write(arrow_group_2), ReplacementTransform(text_3, text_4))
        self.wait(TIME_DELAY)

        #Slide 53, 54
        arrow_4 = Arrow(circle_1, end=UP*2, color=DARK_BLUE, buff=0)
        text_5 = Tex('Vector có chiều từ dưới lên trên', tex_template=VTEX).shift(DOWN*3)
        self.play(Write(arrow_4), ReplacementTransform(text_4, text_5))
        self.wait(TIME_DELAY)

        #Slide 55
        arrow_5 = Arrow(circle_3, end=DOWN*2, color=BLUE, buff=0)
        text_6 = Tex('Vector có chiều từ trên xuống dưới', tex_template=VTEX).shift(DOWN*3)
        self.play(Write(arrow_5), ReplacementTransform(text_5, text_6))
        self.wait(TIME_DELAY)
        pass
