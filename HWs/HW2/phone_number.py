def wrapper(f):
    def fun(l):
        phones: list[str] = []
        for phone in l:
            if phone[0] in ["0", "7", "8"]:
                phone = phone[1:]
            phones.append(f"+7 ({phone[0:3]}) {phone[3:6]}-{phone[6:8]}-{phone[8:10]}")
        return phones
    
    return fun

@wrapper
def sort_phone(l):
    return sorted(l)

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    # l = ["07895462130", "89875641230", "9195969878"]
    print(*sort_phone(l), sep='\n')
