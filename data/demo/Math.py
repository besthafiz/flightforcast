# create mean, median, mode, and standard deviation functions

# create class Math
class Math:
    def mean(x):
        return sum(x) / len(x)

    def median(v):

        n = len(v)
        sorted_v = sorted(v)
        midpoint = n // 2

        if n % 2 == 1:
            # if odd, return the middle value
            return sorted_v[midpoint]
        else:
            # if even, return the average of the middle values
            lo = midpoint - 1
            hi = midpoint
            return (sorted_v[lo] + sorted_v[hi]) / 2
    