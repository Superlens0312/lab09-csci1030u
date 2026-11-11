# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    '''
     I need to find two numbers in the list that add up to the target
     and return their indices.

     # Outline (write your plan here first):

     First I use two loops to check pairs of indices.
     The second loop starts at i + 1 so that i < j.
     I add the values at those indices and compare the sum
     to the target. If they match, I return the indices.

     #Example:
     nums = [2, 7, 11, 15], target = 9
     2 + 7 = 9, so I return [0, 1].
    '''
    # TODO: return the indices [i, j] (i < j) of the two numbers in `nums` that add up
    #   to `target`. Assume there is exactly one answer.
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            result = nums[i] + nums[j]

            if result == target:
                return nums[i,j]


def max_profit(prices):
    '''
     I need to return the most profit obtainable by buying on one day and then selling on another.
     If for whatever reason profit is not possible I return 0
     
     # Outline (write your plan here first):

     First I make 2 variabes low and high so I can keep track of the highest prrofit and the lowest price
     then once I loop through the list Ill know which time to buy and which time to sell based on those values
     Lastly I return how ever much profit I make
     

     #Example:
     prices = [7, 1, 5, 3, 6, 4]
     buy on day 2(index 1) sell on day 5(index 4) for max profit
     So it returns 5
    '''
        
    # TODO: `prices[i]` is a stock price on day i. Return the most profit obtainable by
    #   buying on one day and selling on a LATER day. If no profit is possible, return 0.
    low = prices[0]
    high = 0
    for price in prices:
        if price < low:
            low = price
        if (price -  low) > high:
            high = price - low
    return high


def max_subarray(nums):
    '''
    I need to find the largest sum of any continuous section of numbers
    in the list. The numbers must be next to each other.

    # Outline:
    First I create two variables, current and high, to keep track
    of the current sum and the highest sum.

    Then I loop through the list and check if adding the current
    number to the previous sum is better than starting over.

    If starting over gives a higher sum, I reset current.
    Otherwise, I keep adding to the current sum.

    I also update high whenever I find a larger sum.

    Lastly, I return high.

    # Example:
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    The largest continuous section is [4, -1, 2, 1].

    4 + (-1) + 2 + 1 = 6

    So it returns 6.
    '''
    # TODO: return the largest sum of any contiguous (in-a-row) block of numbers in
    #   `nums`. The list has at least one number.
    
    current = nums[0]
    high = nums[0]

    for num in nums[1:]:
        current = max(num, current + num)

        if current > high:
            high = current

    return high


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    pass


if __name__ == "__main__":
    main()
