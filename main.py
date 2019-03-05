from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

"""
# translation
add_edge( transform, 0, 0, 0, 200, 200, 0 )
draw_lines( transform, screen, color )

print_matrix( transform )

move = make_translate( 200, 40, 0)
matrix_mult( move, transform )

print_matrix( transform )

draw_lines( transform, screen, [255, 0, 0] )

rotX = make_rotX( 30 )
matrix_mult( rotX, transform )

print_matrix( transform )

draw_lines( transform, screen, [0, 0, 255] )
display( screen )
"""

parse_file( 'script', edges, transform, screen, color )
