from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    f = open(fname, "r")
    lines = f.readlines()

    count = 0
    
    while count < len(lines):
        line = lines[count].strip("\n")

        print(line)

        if line == "line":

            coords = lines[count + 1].strip("\n").split(" ")

            add_edge( points, int(coords[0]), int(coords[1]), int(coords[2]),
                      int(coords[3]), int(coords[4]), int(coords[5]) )
            print_matrix( points )
            
            
        elif line == "ident":
            ident( transform )

        elif line == "scale":
            coords = lines[count + 1].strip("\n").split(" ")

            scaled = make_scale( int(coords[0]), int(coords[1]), int(coords[2]) )
            matrix_mult( scaled, transform )
            
        elif line == "move":
            coords = lines[count + 1].strip("\n").split(" ")

            moved = make_translate( int(coords[0]), int(coords[1]), int(coords[2]) )
            matrix_mult( moved, transform )
            
            
        elif line == "rotate":
            rotations = lines[count + 1].strip("\n").split(" ")

            if rotations[0] == "x":
                rotated = make_rotX( int(rotations[1]) )
            elif rotations[0] == "y":
                rotated = make_rotY( int(rotations[1]) )
            else:
                rotated = make_rotX( int(rotations[1]) )

            print_matrix( rotated )
            matrix_mult( rotated, transform )
            print_matrix( transform )
            
        elif line == "apply":
            matrix_mult( transform, points )
            print_matrix( points )
            print_matrix( transform )
            
        elif line == "display":
            clear_screen( screen )
            draw_lines( points, screen, color )
            display( screen )
            
        elif line == "save":
            clear_screen( screen )
            draw_lines( points, screen, color )

            fname = lines[count + 1].strip("\n")
            save_extension( screen, fname )
            
        elif line == "quit":
            break;

        else:
            pass
        
        count += 1
