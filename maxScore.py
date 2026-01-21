def maxScore(cardPoints, k):
        n = len(cardPoints)
        if k == n:
            return sum(cardPoints)

        total = sum(cardPoints)
        window = sum(cardPoints[:n-k])
        min_window = window

        for i in range(n-k, n):
            window += cardPoints[i] - cardPoints[i-(n-k)]
            min_window = min(min_window, window)

        return total - min_window
