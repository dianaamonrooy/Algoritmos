𝑳𝒂𝒃 2: 𝑺𝒆𝒄𝒖𝒆𝒏𝒄𝒊𝒂 𝒅𝒆𝒍 𝑮𝒆𝒏𝒐𝒎𝒂 𝑽𝒊𝒓𝒂𝒍 𝒅𝒆 𝒓𝒆𝒇𝒆𝒓𝒆𝒏𝒄𝒊𝒂 𝑺𝒂𝒓𝒔-𝑪𝒐𝒗 2
𝑮𝒓𝒖𝒑𝒐: 6


-- 𝐂𝐚́𝐥𝐜𝐮𝐥𝐨 𝐁𝐢𝐠 𝐎 -- 
El cálculo de la complejidad teórica de la función estuvo determinado de la siguiente forma:

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
  n = len(S)    # n = length of S                         # 𝐎(𝟏) --> assigns
  m = len(T)    # m = length of T                         # 𝐎(𝟏) --> assigns

  if m > n:                                               # 𝐎(𝟏) --> evaluates
    return [0]                                            # 𝐎(𝟏) --> returns

  if m == n:                                              # 𝐎(𝟏) --> evaluates
    if T == S:                                            # 𝐎(𝟏) --> evaluates
      return [1, (0,len(S)-1)]                            # 𝐎(𝟏) --> returns
    elif T == S:                                          # 𝐎(𝟏) --> evaluates
      return [0]                                          # 𝐎(𝟏) --> returns


  resultList = [0]                                        # 𝐎(𝟏) --> assigns
  incidencesCounter = 0                                   # 𝐎(𝟏) --> assigns
  for i in range(n - m + 1):                              # 𝐎(𝐧-𝐦) -- 𝐁𝐢𝐠 𝐎 = 𝐎(𝐧) --> iterates
    word = ""                                             # 𝐎(𝟏) --> assigns
    
    if S[i] == T[0]:                                      # 𝐎(𝟏) --> evaluates
      word += T[0]                                        # 𝐎(𝟏) --> increments
      
      for j in range(1, m):                               # 𝐎(𝐦) -- 𝐁𝐢𝐠 𝐎 = 𝐎(𝐧) --> iterates
        if S[i + j] == T[j]:                              # 𝐎(𝟏) --> evaluates
          word += T[j]                                    # 𝐎(𝟏) --> increments
        else:                                             # 𝐎(𝟏) --> evaluates
          break                                           # 𝐎(𝟏) --> breaks

      if word == T:                                       # 𝐎(𝟏) --> evaluates
        incidencesCounter += 1                            # 𝐎(𝟏) --> increments
        resultList.append((i, i + m - 1))                 # 𝐎(𝟏) --> appends (view https://wiki.python.org/moin/TimeComplexity)
  
  resultList[0]= incidencesCounter                        # 𝐎(𝟏) --> assigns
  return resultList                                       # 𝐎(𝟏) --> returns


Así, la ecuación de la complejidad teórica estará dada por:
13*𝐎(𝟏) + 𝐎(𝐧)[6*𝐎(𝟏) + 𝐎(𝐧)[4*𝐎(𝟏)]] = O(1) + O(n)*O(n) = 𝐎(𝐧^𝟐)
