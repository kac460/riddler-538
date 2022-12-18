_TARGET = 2023
def trib_contains(
    a: int, 
    b: int, 
    c: int, 
    target: int = _TARGET,
) -> bool:
    while a + b + c < target:
        next_seq = a + b + c
        a = b
        b = c
        c = next_seq
    if a + b + c == target:
        return True

def main():
    smallest_sum = float('inf')
    for a in range(1, _TARGET):
        if a >= smallest_sum:
            break
        for b in range(a, _TARGET):
            if a + b >= smallest_sum:
                break
            for c in range(b, _TARGET):
                if a + b + c >= smallest_sum:
                    break
                if trib_contains(a, b, c):
                    print(f'{a} {b} {c} contains {_TARGET}')
                    smallest_sum = a + b + c
                    smallest = (a, b, c)
    print(f'smallest: {smallest}')

if __name__ == '__main__':
    main()