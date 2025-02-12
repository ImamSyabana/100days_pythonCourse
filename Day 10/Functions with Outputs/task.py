def format_name(f_name, l_name):
    format_fName = f_name.title()
    format_lName = l_name.title()
    return ("fisrt name: {fname}, last name: {l_name}".format(fname = format_fName, l_name = format_lName))

print(format_name(f_name="Heri", l_name="budi"))