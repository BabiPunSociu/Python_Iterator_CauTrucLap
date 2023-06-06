if __name__=='__main__':
    lst = [x for x in range(0,11) if x%2==0]
    # Chuyển list thành iterator
    ilst = iter(lst)
    while True:
        try:
            print(next(ilst))
        except StopIteration:
            break