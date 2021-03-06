# 53% https://app.codility.com/demo/results/training4T8N3D-4NG/

def solution(A):
    result = []
    for p in range(1, len(A)):
        result.append(abs(sum(A[:p]) - sum(A[p:])))
    return min(result)

# 100% https://app.codility.com/demo/results/trainingZP4382-598/

def solution(A):
    front = 0
    rear = sum(A)
    result = None
    for p in range(1, len(A)):
        front += A[p-1]
        rear -= A[p-1]
        diff = abs(front - rear)
        
        if result == None:
            result = diff
        else:
            result = min(result, diff)
    
    return result
