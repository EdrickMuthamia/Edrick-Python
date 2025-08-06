def write_file(f_name,txt):
    with open(f_name,'a') as file:
        file.write(f"{txt}\n")
