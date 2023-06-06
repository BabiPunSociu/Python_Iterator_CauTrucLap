# - Iterators là những đối tượng có những hàm hoặc phương thức
# hỗ trợ lặp riêng, thường là dữ liệu dạng danh sách

# - Một số đối tượng như list, tuple, string là Iterators, sử
# dụng hàm iter() để tại thành một Iterators

# - Sử dụng hàm next() để duyệt qua các phần tử

# - Một Iterators phải implement 2 phương thức, gọi là iterator protocol:
#     __iter__(): hàm tạo
#     __next__(): truy cập đến phần tử kế tiếp

# - Sử dụng StopIteration để để thoát khỏi chương trình lặp

# Tạo iterators là danh sách các số tự nhiên nhỏ hơn 11
class natural_number:
    def __iter__(self):
        self.number = 0
        return self
    
    def __next__(self):
        a = self.number
        self.number += 1
        if (self.number<11):
            return a
        else:
            # Dừng lại -> Giá trị = None
            StopIteration

if __name__=='__main__':
    my_number = natural_number()
    iNumber = iter(my_number)
    
    i = 0
    while i<15:
        try:
            print(next(iNumber))
            i+=1
        except StopIteration:
            break
