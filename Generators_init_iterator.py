# - Generator là cách tạo ra một iterator, bằng cách sử dụng 'yield'

# - Hàm sử dụng 'yield' thì bản thân nó đã tự kế thừa 2 phương thức
# __iter__() và __next__() nên ta có thể sử dụng next() mà không cần
# sử dụng hàm iter() để khởi tạo iterator

# - Cách tạo Generators trong Python:
    # 1, Tạo Generator giống như một hàm bình thường, nhưng thay vì
    # sử dụng lệnh return để trả về thì ta sử dụng lệnh yield.
    
    # 2, Sự khác nhau giữa lệnh return và yield là trong khi return
    # sẽ trả về một giá trị và kết thúc hàm, nhưng yield thì sẽ trả
    # về nhưng vẫn giữ lại trạng thái của các biến, sau đó nếu được
    # gọi tiếp thì nó sẽ tiếp tục xử lý ngay tại vị trí tạm dừng đó.

# - Sự khác nhau giữa hàm Generator và hàm bình thường:
    # 1, Generator chứa một hoặc nhiều lệnh yield.
    # 2, Khi được gọi, hàm generator sẽ trả về một đối tượng iterator
    # nhưng nó không thực thi liền.
    # 3, Hai phương thức __iter__() và __next__() được kế thừa tự động,
    # vì vậy bạn có thể sử dụng hàm next() mà không cần dùng hàm iter()
    # để tạo iterator .
    # 4, Trạng thái của các biến được lưu trữ lại giữa những lần gọi.
    # 5, Cuối cùng khi hàm kết thúc thì StopIteration sẽ bung ra cho
    # lần gọi hàm tiếp theo, đây là lỗi cho thấy iterator đã duyệt đến
    # phần tử cuối cùng.

# Ngoài ra, có thể tạo Generator bằng biểu thức Expression:
    # - Giống với list comprehension, chỉ thay '[]' thành '()'
    # - Chỉ phù hợp với trường hợp có list_data sẵn, và tạo generator
    # dựa trên list_data đó

# Ví dụ:

def InitGenerator(): # Tạo iterator 10->19
    a=10
    for i in range(10):
        print(f'Lần gọi thứ {i+1}, trả về: {a}')
        yield a # Trả về a là iterator và giữ lại các giá trị của biến
        a += 1

def GeneratorExpression():
    # List comprehension
    list_data = [x for x in range(1, 7) if x>0] # [1,2,3,4,5,6]
    # Sử dụng expression để tạo generator
    generator = (x**2 for x in list_data)
    return generator

if __name__=='__main__':
    number = InitGenerator()
    print(number) # number là một generator object
    # In các giá trị
    for i in range(15):
        # Vòng lặp thứ 11 hàm InitGenerator kết thúc, tự động lỗi 
        # StopIteration được bung ra cho lần gọi cuối này để biết là 
        # đã đến phần tử cuối
        try:
            # Khi next() hay giá trị tiếp theo được gọi thì hàm 
            # InitGenerator mới được gọi và chạy tiếp từ vị trí tạm 
            # dừng yield trước đó
            print(next(number))
        except StopIteration:
            print("Đã hết")
            break
    print("===================")
    #================================================================
    generator = GeneratorExpression()
    print(generator) # là một generator object
    # In
    for n in generator:
    # Khi duyệt các giá trị được duyệt từ next() được bỏ qua trong for()
        print('n = ' + str(n))
        print(next(generator))