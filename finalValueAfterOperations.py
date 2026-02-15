class Solution:
    def finalValueAfterOperations(self, operations) :
        val = 0
        for operation in operations :
            if operation == "++X" or operation == "X++":
                val += 1
            else:
                val -= 1
        return val