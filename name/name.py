from name.name_function import get_formatted_name

print("输入'q'退出")
while 1:
    first = input("\n请输入first name: ")
    if first == 'q':
        break
    last = input("\n请输入last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\t 全名是: " + formatted_name + '.')

