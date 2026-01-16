def rowAndMaximumOnes(mat) :
        ans = [0,0]

        for i in range(len(mat)):
            no_of_ones = sum(mat[i])
            if no_of_ones > ans[1]:
                ans[1] = no_of_ones
                ans[0] = i
        
        return ans