## **Calculando Complejidad**
**Nota:** Para la complejidad, vamos a ignorar la creación de las gráficas.


**CONVENCIONES**

*   **gS** = genome size
*   **pS** = population size
*   **nG** = number of generations

```
def geneticAlgorithm(gS, pS, mP, nG, fO, sR): 
  
  def function(x):  ---------------------------------------------------> O(1)
    return eval(fO, {"x" : x, "math":__import__('math')}) 

  firstGeneOptions = list(range(0, sR))  ------------------------------> O(sR)
  otherGenesOptions = [0,1,2,3,4,5,6,7,8,9]  --------------------------> O(1)
  geneticPool = [firstGeneOptions, otherGenesOptions]  ----------------> O(1)
  
  population = []  ----------------------------------------------------> O(1)

  for i in range(pS):  ------------------------------------------------> O(pS)
    individual = []  ---------------------------------------------> O(1)
    individual += [np.random.choice(geneticPool[0])] -------------> O(1)
    individual += list(np.random.choice(geneticPool[1], gS-1)) ---> O(1)
    population.append(individual)    -----------------------------> O(1)
  
  for var in range(nG): -----------------------------------------------> O(nG)
    fitness =[]  -------------------------------------------------> O(1)

    for individual in population: --------------------------------> O(pS)
      x = listToDecimal(individual)  -----------------------> O(gS)
      y = function(x)   ------------------------------------> O(1)
      fitness.append(y)  -----------------------------------> O(1)

    sumFitness = sum(fitness)  -----------------------------------> O(pS)

    for i in range(len(fitness)):  -------------------------------> O(pS)
      fitness[i] = fitness[i] / sumFitness   ---------------> O(1)

    descendants = [] ---------------------------------------------> O(1)
    for i in range(pS//2): ---------------------------------------> O(pS/2)
      parents = np.random.choice(pS, 2, p = fitness) -------> O(1)
      parent1 = population[parents[0]]   -------------------> O(1)
      parent2 = population[parents[1]]   -------------------> O(1)
      splitPoint = np.random.randint(gS)  ------------------> O(1)
      desce ... + parent2[splitPoint:]]  -------------------> O(1)
      desce ... + parent1[splitPoint:]]  -------------------> O(1)

    population = descendants  ------------------------------------> O(1)

    for i in range(len(population)):   ---------------------------> O(pS)
      possibleMutant = population[i]  ----------------------> O(1)
      if np.random.random() < mP:
        mutation = np.random.choice(geneticPool[0]) --------> O(1)
        possibleMutant[0] = mutation  ----------------------> O(1)

      for j in range(1, len(possibleMutant)): --------------> O(gS)
        if np.random.random() < mP:
          mutation = np.random.choice(geneticPool[1])-> O(1)
          possibleMutant[j] = mutation  --------------> O(1)
          
      population[i] = possibleMutant   ---------------------> O(1)

```

**Complejidad Específica**
```

O[sR + pS + nG(pS*gS + 2pS + pS/2 + pS*gS)] = O[sR + pS + nG(pS*gS + 2pS + pS/2 + pS*gS)]
                                       = O[sR + pS + nG(pS*gS + pS)]
                                       = O[sR + pS + nG*pS(gS)]
                                       = O[sR + pS*nG*gS]

```
La complejidad, entonces, está dada por: **O(*searchRange + genomeSize x populationSize x numGenerations*)**

## **Preguntas Finales**

1.   **Cómo reacciona el algoritmo a variadas funciones de optimización (lineal, oscilantes (varias frecuencias), etc)?**

Al aumentar la longitud de onda en la función oscilante, se puede evidenciar que el error promedio tiende a acelerar su reducción hacia el 0, probablemente debido a la disminución del número de máximos locales.

![image.png](https://i.ibb.co/SQ0Kx3z/Captura-de-pantalla-908.png)

Por supuesto, con funciones polinómicas o lineales, la convergencia es aún más veloz:

![image.png](https://i.ibb.co/ZMwW697/Sin-t-tulo.png)


2.   **Relacion entre los parámetros de configuración y el costo (tiempo y espacio)**

La complejidad depende principalmente de tres parámetros: **genomeSize**, **populationSize** y **numGenerations**. Por lo tanto, todos influyen de manera importante en el costo del algoritmo. 

El *genomeSize* y *populationSize* se deben tener en cuenta especialmente para la memoria, pues hay que recordar que el algoritmo almacena la población mediante una matriz de tamaño populationSize x genomeSize. **Tomar grandes valores de población y/o de genoma aumentará el uso de memoria**

Por supuesto, usar un *numGenerations* muy grande **ayudará a mejorar la precisión** del valor óptimo, con más generaciones "evolucionando" hacia el valor deseado. Sin embargo, al estar multiplicada su complejidad con los otros dos parámetros, se presenta un aumento considerable en el tiempo total del algoritmo.

Por otro lado, es necesario tener en cuenta que a un mayor rango de búsqueda, se generará una lista de tamaño *searchRange*, que para rangos razonables parece no afectar el algoritmo, sin embargo en la complejidad asintótica será de importancia a nivel de espacio. 


3.   **¿Qué parámetro considera usted más relevante para acelerar la convergencia de la búsqueda?**

El tamaño del genoma de cada individuo puede ser uno de los parámetros que puede reducirse. Cuando lo disminuimos, usualmente se requieren menos generaciones para que la población se acerque a valores cercanos al óptimo. 

Finalmente, si se quiere más precisión (sacrificando la rapidez) se puede usar un número muy grande de generaciones.






## **Implementación Binaria - Análisis de Complejidad Específica:**


---




1.   **gS** = individuals_genome_size
2.   **pS** = population_size
3.   **ng** = generations
4.   **sR** = search_range

---
    
    def genetic(individuals_genome_size, population_size, mutation_prob, generations, function, search_range):

      def bin_decimal(num_binario): ----------------------------------------------------------------- O(gS)
        ans = (np.sum(num_binario)/len(num_binario))*max(search_range) ------------------------------ O(gS)
        if math.modf(ans)[1] == 0: # integer part of the number ------------------------------------- O(1)
          ans = ans + min(search_range) ------------------------------------------------------------- O(1)
        return ans ---------------------------------------------------------------------------------- O(1)

      def fx(x): ------------------------------------------------------------------------------------ O(1)
        return eval(function,{"x" : x, "math":__import__('math')}) ---------------------------------- O(1)

      def mutate(individuals, prob, pool): ---------------------------------------------------------- O(gS^2 * pS)
        for i in range(len(individuals)): ----------------------------------------------------------- O(pS)
          mutate_individual = individuals[i] -------------------------------------------------------- O(1)
          for j in range(len(mutate_individual)): --------------------------------------------------- O(gS)
              if np.random.random() < prob: --------------------------------------------------------- O(1)
                  mutation = np.random.choice(pool) ------------------------------------------------- O(1)
                  mutate_individual = mutate_individual[0:j] + [mutation] + mutate_individual[j+1:] - O(gS)
          individuals[i] = mutate_individual -------------------------------------------------------- O(1)


      population = [] ------------------------------------------------------------------------------- O(1)
      genetic_pool = [0,1] -------------------------------------------------------------------------- O(1)
      for i in range(population_size): -------------------------------------------------------------- O(pS)
          individual = list(np.random.choice(genetic_pool,individuals_genome_size)) ----------------- O(1)
          population.append(individual) ------------------------------------------------------------- O(1)

      for gen in range(generations): ---------------------------------------------------------------- O(nG)

        fitness =[] O(1)
        for individual in population: -------------------------------------------------------------- O(pS)
          x = bin_decimal(individual) -------------------------------------------------------------- O(gS)
          y = fx(x) -------------------------------------------------------------------------------- O(1)
          fitness += [y]---------------------------------------------------------------------------- O(1)

        fitness = np.array(fitness) ---------------------------------------------------------------- O(pS)
        fitness = fitness/fitness.sum() ------------------------------------------------------------ O(pS)



        offspring = []  --------------------------------------------------------------------------------- O(1)
        for i in range(population_size//2): ------------------------------------------------------------- O(pS / 2)
            parents = np.random.choice(population_size, 2, p=fitness) ----------------------------------- O(1)
            cross_point = np.random.randint(individuals_genome_size) ------------------------------------ O(1)
            offspring += [population[parents[0]][:cross_point] + population[parents[1]][cross_point:]] -- O(1)
            offspring += [population[parents[1]][:cross_point] + population[parents[0]][cross_point:]] -- O(1)

        population = offspring -------------------------------------------------------------------------- O(1)
        mutate(population,mutation_prob,genetic_pool) --------------------------------------------------- O(gS^2 * pS)

**Complejidad Específica**

```
O[pS + nG(pS*gS + 2pS + pS/2 + pS*gS^2)] = O[pS + nG(pS*gS + 2pS + pS/2 + pS*gS^2)]
                                         = O[pS + nG(pS*gS^2 + pS)]
                                         = O[pS + nG*pS(gS^2)]
                                         = O[pS*nG*gS^2]

```
La complejidad, entonces, está dada por: **O(*genomeSize^2 x populationSize x numGenerations*)**

La diferencia con la complejidad de la implementación decimal radica en dos principales cambios:
1. Al momento de inicializar el genetic pool en la implementación decimal, se requiere inicializar una lista con rango *searchRange*. Esto no se realiza en la implementación binaria, puesto que los genes serán solamente 0 y 1

2. Al momento de hacer la mutación la implementación decimal es más eficiente puesto que evita hacer slicing, cambiando directamente el gen mutado en la cadena. Ejemplificando:

En la implementación más eficiente (decimal) se realiza lo siguiente

```
cadena[j] = genMutado
```
en vez de lo siguiente

```
cadena = cadena[:j] + genMutado + cadena[j+1:]
