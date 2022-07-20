import time
class Execution:

    def time_wrap(fn):
        """method to perform execution time!!!"""
        start_time = time.time()
        result= fn()
        print(result)
        end_time = time.time()
        print("total execution time:",end_time- start_time)

    @time_wrap
    def arm():
        """to find armstrong number: the armstrong value is like 153 = 1^3 + 5^3 +3^3 = 1+ 125 + 27 = 153"""
        a = int(input("enter a number to find armstrong number:"))
        sum = 0
        b = a
        time.sleep(5)
        while(b>0):
            n =len(str(b))
            for i in range(n):
                rem = b % 10
                sum = sum + ((rem)**n)
                b = b // 10
        if (a==sum):
            return 'it is an armstrong number.'
        else:
            return 'it is NOT an armstrong number.'

Execution.time_wrap
