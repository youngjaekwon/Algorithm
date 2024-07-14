# 1174번: 줄어드는 수

N = int(input())


def search():
    arr = list(range(11))
    no = 20

    while True:
        if len(arr) >= N:
            break
        elif no > 9876543210:
            return -1

        str_no = str(no)
        tmp = int(str_no[0])
        success = True
        failed_index = 0

        for i, n in enumerate(str_no[1:]):
            int_n = int(n)
            if int_n >= tmp:
                failed_index = i + 1
                success = False
                break
            tmp = int_n

        if success:
            arr.append(no)
            no += 1
        else:
            str_no_list = list(str_no)
            str_no_list[failed_index - 1] = str(int(str_no_list[failed_index - 1]) + 1)
            for i in range(failed_index, len(str_no_list)):
                str_no_list[i] = "0"
            no = int("".join(str_no_list))

    return arr[N - 1]


print(search())
