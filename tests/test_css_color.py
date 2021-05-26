from random_tools import CSS4_ColorPicker

def test_css_color_picker():
    
    color_picker = CSS4_ColorPicker()
    
    nb_color = len(color_picker.CSS4_COLORS)
    
    # Check we have a good number of color and some we knows
    assert nb_color > 100
    assert "red" in color_picker.CSS4_COLORS
    assert "blue" in color_picker.CSS4_COLORS
    assert "pink" in color_picker.CSS4_COLORS
    assert "yellow" in color_picker.CSS4_COLORS
    
    
    # Check we get unique colors
    colors = set()
    for i in range(nb_color):
        color = color_picker.sample_color()
        assert color not in colors
        colors.add(color)
    
    # Check the pool resets
    assert color_picker.sample_color() in colors