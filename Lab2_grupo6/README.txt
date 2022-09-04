
El cálculo de la complejidad teórica de nuestro código se realizó de la siguiente manera:
  def findAll(S,T):
  """
  It receives two parameters:
    S - the whole String where T needs to be found
    T - the target String to be found

  It returns a list L where:
    L[0] - N = number of times T was found inside of S
    L[1] - (initPos, finalPos) of the 1st occurrence of T
    ...
    L[n-1] - (initPos, finalPos) of the n-th occurrence of T
  """
  n = len(S)    # n = length of S                         # O(1) --> assigns
  m = len(T)    # m = length of T                         # O(1) --> assigns

  if m > n:                                               # O(1) --> evaluates
    return [0]                                            # O(1) --> returns

  if m == n:                                              # O(1) --> evaluates
    if T == S:                                            # O(1) --> evaluates
      return [1, (0,len(S)-1)]                            # O(1) --> returns
    elif T == S:                                          # O(1) --> evaluates
      return [0]                                          # O(1) --> returns


  resultList = [0]                                        # O(1) --> assigns
  incidencesCounter = 0                                   # O(1) --> assigns
  for i in range(n - m + 1):                              # O(n-m) -- Big O = O(n) --> iterates
    word = ""                                             # O(1) --> assigns
    
    if S[i] == T[0]:                                      # O(1) --> evaluates
      word += T[0]                                        # O(1) --> increments
      
      for j in range(1, m):                               # O(m) -- Big O = O(n) --> iterates
        if S[i + j] == T[j]:                              # O(1) --> evaluates
          word += T[j]                                    # O(1) --> increments
        else:                                             # O(1) --> evaluates
          break                                           # O(1) --> breaks

      if word == T:                                       # O(1) --> evaluates
        incidencesCounter += 1                            # O(1) --> increments
        resultList.append((i, i + m - 1))                 # O(1) --> appends (view https://wiki.python.org/moin/TimeComplexity)
  
  resultList[0]= incidencesCounter                        # O(1) --> assigns
  return resultList                                       # O(1) --> returns


Así, la ecuación de la complejidad teórica estará dada por:
13*O(1) + O(n)[6*O(1) + O(n)[4*O(1)]] = O(1) + O(n)*O(n) = O(n^2)
