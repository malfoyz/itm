def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def main() -> None:
    # Пример использования
    arr = [2, 3, 4, 10, 40]
    target = 6
    result = binary_search(arr, target)
    if result != -1:
        print(f"Элемент найден на индексе {result}")
    else:
        print("Элемент не найден")


if __name__ == '__main__':
    main()
