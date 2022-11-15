import pandas as pd
# from  ProyectoCluster import Clusters as cl ###This is to load cluster script

#variables = ['anios_castigo','dias_mora','vlr_oblig','endeudamiento', 'porc_total_descuento'] Variables to create cluster

possibles_metric = ['distortion','silhouette','calinski_harabasz']
possibles_distances = ['cityblock', 'cosine', 'euclidean', 'l1', 'l2', 'manhattan','dados','canberra']

aux = {} # Dictionaty with the best metric and distances depends how it works
aux_2 = {} # Dictionaty with the metric doesn't work
for i in possibles_metric:
    for j in possibles_distances:
        try:
            aux2 =  cl.finding_optimal(Df_general[variables].copy(), Metric = i,distance= j) # Function o cluster script

            if i not in aux:
                aux[i] = {}
                aux[i][j] = aux2
            else:
                aux3 = [k for k in aux[i].values()]
                aux3 = float(aux3[0])
                if i != 'distortion':
                    if aux2 > aux3:
                        aux[i] = {}
                        aux[i][j] = aux2
                else:
                    if aux2 < aux3:
                        aux[i] = {}
                        aux[i][j] = aux2
        except:
            aux_2[j] = i
