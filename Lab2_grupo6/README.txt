๐ณ๐๐ 2: ๐บ๐๐๐๐๐๐๐๐ ๐๐๐ ๐ฎ๐๐๐๐๐ ๐ฝ๐๐๐๐ ๐๐ ๐๐๐๐๐๐๐๐๐๐ ๐บ๐๐๐-๐ช๐๐ 2
๐ฎ๐๐๐๐: 6

La funciรณn findAll(S,T):
* Retorna el nรบmero de recurrencias de T encontradas en S.
* Y por cada recurrencia, devuelve la posiciรณn inicial y final de la misma dentro de S.

-- ๐๐ฬ๐ฅ๐๐ฎ๐ฅ๐จ ๐๐ข๐  ๐ -- 
El cรกlculo de la complejidad teรณrica de la funciรณn estuvo determinado de la siguiente forma:

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
  n = len(S)    # n = length of S                         # ๐(๐) --> assigns
  m = len(T)    # m = length of T                         # ๐(๐) --> assigns

  if m > n:                                               # ๐(๐) --> evaluates
    return [0]                                            # ๐(๐) --> returns

  if m == n:                                              # ๐(๐) --> evaluates
    if T == S:                                            # ๐(๐) --> evaluates
      return [1, (0,len(S)-1)]                            # ๐(๐) --> returns
    elif T == S:                                          # ๐(๐) --> evaluates
      return [0]                                          # ๐(๐) --> returns


  resultList = [0]                                        # ๐(๐) --> assigns
  incidencesCounter = 0                                   # ๐(๐) --> assigns
  for i in range(n - m + 1):                              # ๐(๐ง-๐ฆ) -- ๐๐ข๐  ๐ = ๐(๐ง) --> iterates
    word = ""                                             # ๐(๐) --> assigns
    
    if S[i] == T[0]:                                      # ๐(๐) --> evaluates
      word += T[0]                                        # ๐(๐) --> increments
      
      for j in range(1, m):                               # ๐(๐ฆ) -- ๐๐ข๐  ๐ = ๐(๐ง) --> iterates
        if S[i + j] == T[j]:                              # ๐(๐) --> evaluates
          word += T[j]                                    # ๐(๐) --> increments
        else:                                             # ๐(๐) --> evaluates
          break                                           # ๐(๐) --> breaks

      if word == T:                                       # ๐(๐) --> evaluates
        incidencesCounter += 1                            # ๐(๐) --> increments
        resultList.append((i, i + m - 1))                 # ๐(๐) --> appends (view https://wiki.python.org/moin/TimeComplexity)
  
  resultList[0]= incidencesCounter                        # ๐(๐) --> assigns
  return resultList                                       # ๐(๐) --> returns


Asรญ, la ecuaciรณn de la complejidad teรณrica estarรก dada por:
13*๐(๐) + ๐(๐ง)[6*๐(๐) + ๐(๐ง)[4*๐(๐)]] = O(1) + O(n)*O(n) = ๐(๐ง^๐)
