T = int(input())
result = []
for t in range(T):
    cute = int(input())
    result.append(cute)
    
if result.count(1) > result.count(0):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")