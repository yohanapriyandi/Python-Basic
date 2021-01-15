# Definsikan fungsi dengan nilai default argument kedua adalah "".
def function_with_argument(first_name, last_name=" "):
    print(first_name + " " + last_name)


# Panggil fungsi dengan memasukkan argumen nama_depan "John"
function_with_argument("John")
# Panggil fungsi dengan memasukkan argumen
# nama_depan yaitu "John" dan nama_belakang "Doe"
function_with_argument("John", "Doe")
