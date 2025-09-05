data_type = {
"integer":"numberInteger numbers (e.g., 1, 100, -50)",
"float":"decimal point number",
"chr":"Single character (e.g., 'a', 'Z')",
"double":"Double-precision floating-point numbers",
"void":"Represents absence of type (used for functions that return nothing)",
}
str_methodes ={
    "lower()":"Converts string to lowercase",
    "upper()":"Converts string to uppercase",
    "capitalize()":"Capitalizes first character",
    "title()":"Capitalizes first letter of each word",
    "replace()":"Replaces substring\n'a-b-c'.replace('-', '+') → 'a+b+c'"
}
search = input("what you want to know about ?Data type or string Methodes?  \n:")
q = input("what is your qusition ?")
if search == "data type":
    print(data_type[q])
else:
    print(str_methodes[q])    