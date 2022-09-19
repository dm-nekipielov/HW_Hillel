def deepest_lake(peaks: list) -> int:
    max_left_peak = 0
    max_right_peak = 0
    valley = 0
    deep = 0
    for i in range(len(peaks)):
        if i > 0:
            if peaks[i] < peaks[i - 1]:
                valley = peaks[i]
                if peaks[i - 1] > max_left_peak:
                    max_left_peak = peaks[i - 1]
            elif peaks[i] < valley:
                valley = peaks[i]
            elif peaks[i] > valley:
                max_right_peak = peaks[i]
                current_deep = min(max_left_peak, max_right_peak) - valley
                if current_deep > deep:
                    deep = current_deep
    return deep


if __name__ == "__main__":
    assert (deepest_lake([1, 2, 5, 6, 1, 2, 2, 3, 0, 1, 5, 6, 7, 5, 5, 7, 8, 8, 2]) == 6)
    assert (deepest_lake([1, 2, 5, 7, 1, 2, 2, 3, 0, 1, 5, 6, 7, 5, 5, 7, 8, 8, 2]) == 7)
    assert (deepest_lake([5, 9, 0, 1, 5, 8, 2]) == 8)
    assert (deepest_lake([1, 2, 2, 3, 0, 1, 5, 4, 2]) == 3)
    print("Success!")
