import textwrap

def wrap(string, max_width):
    my_wrap = textwrap.TextWrapper(width=max_width)
    wrap_list = my_wrap.wrap(text=string)
    result = '\n'.join(wrap_list)
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# este metodo da error ya que imprimimos la informacion introducida y no debemos
# def wrap(string, max_width):
#     string = string
#     my_wap = textwrap.TextWrapper(width= max_width)
#     wrap_list = my_wap.wrap(text=string)
#     for line in wrap_list:
#         print(line)
#     return string, max_width
#
# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)
#
