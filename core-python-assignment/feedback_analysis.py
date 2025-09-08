def positive_feedback(ratings):
    if not ratings:
        return "No ratings available"
    positives = sum(1 for r in ratings if r >= 4)
    percentage = (positives / len(ratings)) * 100
    return f"Positive Feedback: {percentage:.1f}%"

ratings = list(map(int, input("Enter ratings separated by space: ").split()))
print(positive_feedback(ratings))
