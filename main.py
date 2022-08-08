class sort:
    @staticmethod
    def quicksort(array):
        if len(array) <= 1:
            return array

        pivot = array[0]
        left = []
        right = []
        pivots = []
        for i in array:
            if i == pivot:
                pivots.append(i)
            elif i < pivot:
                left.append(i)
            elif i > pivot:
                right.append(i)
        
        sorted_left = sort.quicksort(left)
        sorted_right = sort.quicksort(right)

        out_array = sorted_left + pivots + sorted_right

        return out_array


    @staticmethod
    def getIndexes(array, element):
        count = 0
        indexes = []
        for i in array:
            if i == element:
                indexes.append(count)
            count += 1
        return indexes


    @staticmethod
    def quicksortIndex(array):
        if len(array) <= 1:
            return [i for i in range(len(array))-1]
                
        #Criamos uma array já ordenada:
        sorted_array = sort.quicksort(array)              

        sorted_indexes = []

        #Para cada elemento da array ordenada, checamos sua posição na array desordenada.
        #Caso encontrado e o primeiro index desse elemento não estiver na array (contagem de vezes que o index foi encontrado na array = 0), adicionamos
        # TODOS os indexes relativos a esse elemento na array sorted_indexes, em ordem com a função q eu criei :)
        for sorted_element in sorted_array:
            for element in array:
                if sorted_element == element and sorted_indexes.count(array.index(element)) == 0:
                    sorted_indexes += sort.getIndexes(array, element)
        
        return sorted_indexes


if __name__ == '__main__':
    print(sort.quicksortIndex([1, 2, 3, 5, 4]))
    #print(sort.getIndexes([3, 4, 2, 5, 3], 3))




