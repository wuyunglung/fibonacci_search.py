def fibonacci_search(arr, x):
    """
    使用費氏搜尋算法在已排序陣列中尋找目標值。
    相比二分搜尋，此算法僅使用加減法，更適合某些嵌入式系統環境。
    """
    n = len(arr)
    fib_m2 = 0  # (m-2)th Fibonacci number
    fib_m1 = 1  # (m-1)th Fibonacci number
    fib_m = fib_m2 + fib_m1  # m-th Fibonacci number

    # 找到大於或等於 n 的最小費氏數
    while (fib_m < n):
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1

    offset = -1

    while (fib_m > 1):
        # 檢查 fib_m2 是否為有效範圍
        i = min(offset + fib_m2, n-1)

        if (arr[i] < x):
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i
        elif (arr[i] > x):
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1
        else:
            return i

    # 比較最後一個元素
    if(fib_m1 and arr[n-1] == x):
        return n-1

    return -1

# 測試範例
if __name__ == "__main__":
    data = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
    target = 85
    result = fibonacci_search(data, target)
    if result != -1:
        print(f"元素 {target} 的索引位置為: {result}")
    else:
        print("找不到該元素")
