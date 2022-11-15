import pandas as pd
from yellowbrick.cluster import KElbowVisualizer
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from scipy import stats
import numpy as np

def finding_optimal(Df: pd.DataFrame, Metodo = KMeans(random_state=3194), number_cluster : int =  10, Metric: str = 'distortion', distance : str = 'euclidean'):

    '''
Metricc : [silhouette , calinski_harabasz]  {Métrica que juzga la separación}
distance : Distance between samples sdfsa


'''
    Df = Df.copy()


    Df = Df[(np.abs(stats.zscore(Df)) < 3).all(axis=1)]
    constructor = MinMaxScaler().fit(Df)

    Df_transform = constructor.transform(Df)
    
    select_cluster = KElbowVisualizer(Metodo,k = number_cluster, metric = Metric, distance_metric= distance, timings = False)

    select_cluster.fit(Df_transform)

    print(Metric, distance)
    select_cluster.show()
    return select_cluster.elbow_score_




def creation_cluster(Df: pd.DataFrame, n_cluster : int ):

    Df = Df.copy()

    model = KMeans(n_cluster)

    model.fit(Df)

    Df['Cluster'] = model.labels_

    return Df


