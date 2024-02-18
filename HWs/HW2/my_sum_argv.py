from sys import argv

def my_sum_argv(*args) -> int:
    return sum(args)

if __name__ == "__main__":
    try:
        numbers = [float(arg) for arg in argv[1:]]
        result = my_sum_argv(*numbers)
        print(float(result))
    except Exception as e:
        print(e)