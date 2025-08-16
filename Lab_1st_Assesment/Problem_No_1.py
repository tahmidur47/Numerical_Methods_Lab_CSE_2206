#Find the smallest number in a list using a loop.


def finding_smallest():
    try:
        nums = list(map(float, input("Enter numbers: ").split()))
        if not nums:
            print("No numbers were entered!")
            return
        
        min_num = nums[0]
        for x in nums:
            if x < min_num:
                min_num = x
        
        print(f"The smallest number is: {min_num}")
    
    except ValueError:
        print("Please enter valid numbers only")

finding_smallest()