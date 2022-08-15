from collections import Counter
def MinWindowSubstring(strArr):

  # code goes here
  N = strArr[0]
  length_N = len(N)
  k = strArr[1]
  length_k = len(set(k))
  
  for j in range(length_N):
    for i in range(length_N - length_k):
      substring = N[i: length_k+i+j]
      #print(substring)
      if contains_all(substring, k):
        #print('yesssssssss')
        return substring
      


def contains_all(string, substring):
    c1, c2 = Counter(string), Counter(substring)
    return all(c1[x] >= c2[x] for x in c2)
# keep this function call here 
print(MinWindowSubstring(input()))
