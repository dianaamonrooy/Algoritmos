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

  #If T is longer than S, it can't be inside S
  if len(T) > len(S):
    return [0]

  #If both strings are the same, there are only two options:
  if len(T) == len(S):
    if T == S:              #If T = S, T is inside S
      return [1, (0,len(S)-1)]
    else:                   #If T != S, T is not inside S
      return [0]
  
  #The default list starts with 0 occurrences
  lista = [0]
  incidencesCounter = 0
  contador = 0

  #This iterates through S, until the last index where T might start
  for i in range(len(S) - len(T) + 1): #O(N-M)
    word = ""    # O(1)
    contador += 1 # 
    if S[i] == T[0]:
      word += T[0]
      for j in range(1, len(T)): # O(M)
        contador += 1 
        if S[i + j] == T[j]:
          word += T[j]
      #Every time a new coincidence is found, the counter of
      #occurrences gets incremented and the (iniPos, finalPos)
      #tuple is added to the list
      if word == T:
        incidencesCounter += 1
        lista.append((i, i + len(T) - 1))
  #This adds the number of ocurrences at the beginning of the list
  lista[0]= incidencesCounter
  print("Contador de Juanse:",contador)
  return lista
