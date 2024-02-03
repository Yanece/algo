def interpolation_search(arr, n):
    debut=0
    fin = (len(arr) )- 1
    trouve=False

    while debut < fin and not(trouve):
        
        pos = debut + (fin - debut) * (n - arr[debut]) // (arr[fin] - arr[debut])

        if arr[pos] == n:
            trouve=True   
        
        elif arr[pos] < n:
            debut = pos + 1

        else:
            fin = pos - 1
    
    if trouve :
        return print(f"La valeur cherchée est à la position {pos}")
    else:
        return print(f"La valeur cherchée n'est pas dans le tableau")


liste=[2,4,6,8,10,11,50]

interpolation_search(liste,11)
interpolation_search(liste,15)