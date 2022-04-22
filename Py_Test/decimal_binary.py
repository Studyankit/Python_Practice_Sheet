def decimal_to_binary(ip_val):
    if ip_val >= 1:
        print(ip_val)
        decimal_to_binary(ip_val // 2)
    print(ip_val % 2, end=" ")


decimal_to_binary(10)