def maxArea(height) -> int:
    # height is an array
    water = 0
    for i in range(len(height)):
        for j in reversed(range(len(height))):
            if i == j:
                continue
            low = min(height[i], height[j])
            distance = j - i
            area = low * distance
            water = max(area, water)
    return water

if __name__ == "__main__":
    print(maxArea([1,8,6,2,5,4,8,3,7]))