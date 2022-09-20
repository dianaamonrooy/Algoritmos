TAREA-BT 
GRUPO 6
Descripción: 
Este programa utiliza la clase newNode y las funciones insert() e iterativeSearch() para crear un árbol binario y realizar en el una búsqueda iterativa que permita encontrar el camino hacia un nodo definido por el usuario.
La función iterativeSearch se modifica para poder imprimir el camino y el grafo del árbol solo con los nodos del camino.
Se crea además una función graphTree() que permite graficar un nodo usando como argumento su raíz. 
El cálculo de la complejidad de esta función se encuentra a continuación. 

def graphTree(root):
  if root == None:                                                        # O(1)
      return                                                              # O(1)
  # It saves the root in an array
  nodes = [root]                                                          # O(1)
  # We get the height of the tree, it will be used several times
  h = height(root)                                                        # O(n)
  # We create an array with size = maximum possible amount of nodes
  tree = ["   "]*((2**h) - 1)                                             # O(1)
  # We iterate the tree in a level-order way and for each node, we add
  # its value into the array "tree", in the corresponding index
  while len(nodes) != 0:                                                  # O(n)
      node = nodes.pop(0)                                                 # O(1) (ver: https://wiki.python.org/moin/TimeComplexity)
      tree[node.index] = f'{str(node.data):<3}'                           # O(1)
      if node.left != None:                                               # O(1) (ver: https://wiki.python.org/moin/TimeComplexity)
          nodes.append(node.left)                                         # O(1) 
      if node.right != None:
          nodes.append(node.right) 
  # Initialize the amount of formatting spaces used when printing
  initIndex = 0                                                           # O(1)
  endIndex = 1                                                            # O(1)
  begginingSpace = ((2 ** h) - 2) * " "                                   # O(1)
  middleSpaces = ((2 ** (h + 1)) - 3) * " "                               # O(1)
  # Each tree level gets turned into a String following a defined formatting
  levels = []                                                             # O(1)
  for i in range(1, h + 1):                                               # O(n), ya que en el peor caso, h = n
    levelText = begginingSpace + middleSpaces.join(tree[initIndex:endIndex])      # O(1)
    levels.append(levelText)                                              # O(1) (ver: https://wiki.python.org/moin/TimeComplexity)
    # Updating the indexes for the next level of the tree
    initIndex = endIndex                                                  # O(1)
    endIndex += 2**i                                                      # O(1)
    # Updating the spaces for the next level of the tree
    begginingSpace = ((2 ** (h - i)) - 2) * " "                           # O(1)
    middleSpaces = ((2 ** (h + 1 - i)) - 3) * " "                         # O(1)

  # Finally, when we have the list with every level 
  # turned into a String, we print each one of the levels
  for level in levels:                                                    # O(n), ya que en el peor caso, h = n
    print(level)                                                          # O(1)


Así, la complejidad de la función es de O(4n) = O(n), donde n es el número de nodos del arbol
