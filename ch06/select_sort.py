def select_sort(my_list):
    for i in range(len(my_list)):
        # 현재 값 다음부터 비교
        for j in range(i+1, len(my_list)):
            # 자릿수 교환할 때 자바는 앞의 값을 imsi저장, 뒤에값을 앞에 넣고
            # imsi에 있는 값을 뒤에 값에 넣어서 처리
            if my_list[i] >  my_list[j]:
                my_list[i] , my_list[j] = my_list[j],  my_list[i]
li = [11,3,6,4,12, 1,2]
select_sort(li)
print(li)