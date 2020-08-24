def draw_triangle(base_len=3):
    error = validate_parameter(base_len)
    if error:
        print error 
        return
    pyramid_dict = {}
    for x in range(0, base_len, 2):
        generate_x_pyramid(pyramid_dict, (base_len - x))
    style_x_pyramid(pyramid_dict, base_len)

def validate_parameter(base_len):
    error = ''
    if base_len < 3:
         error = 'ERROR: The size is too small.'
    elif not isinstance(base_len, int):
        error = 'ERROR: Invalid input!'
    return error

def generate_x_pyramid(pyramid_dict, row_len_counter):
    if row_len_counter > 0:
        pyramid_dict[row_len_counter] = 'X' * row_len_counter
    else:
        return 

def insert_divider_in_x_row(x_row):
    divider = '-' * (len(x_row) - 2)
    return 'X' + divider + 'X'

def style_x_pyramid(x_pyramid, base_len):
    space_counter = base_len / 2
    for key in sorted(x_pyramid.keys()):
        if len(x_pyramid[key]) > 2 and len(x_pyramid[key]) < base_len:
            x_pyramid[key] = insert_divider_in_x_row(x_pyramid[key])
        print ' ' * space_counter + x_pyramid[key]
        space_counter -= 1
draw_triangle(5)
