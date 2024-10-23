# Write your solution here
def longest_series_of_neighbours(lst:list)-> int:
    longest_series = 0
    current_series = 0


    for i in range(len(lst) - 1):

        if abs(lst[i] - lst[i + 1]) == 1:
            current_series += 1
            if current_series > longest_series:
                longest_series = current_series
        else:

            current_series = 0


    return longest_series + 1

if __name__=="__main__":
    result = longest_series_of_neighbours([1, 2, 3, 5, 6, 7, 6, 5, 6, 7, 10, 11, 10])
    print(result)