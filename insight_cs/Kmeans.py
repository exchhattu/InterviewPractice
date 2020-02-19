
# Tue Feb 18 16:11:05 2020
# ========================

import numpy as np
from numpy import random
from numpy import linalg

class KMeans: 

    def __init__(self, data =np.array([]), n_sample =100, n_dim =2):
        """
        Accepts data. If not randomly generate it 
        """
        self._num_pts = n_sample 
        self._dim = n_dim
        self._max_iter = 10
        if data:
            self._data = data
        else:
            self.generate_random_data(dim = n_dim, num_sample=n_sample)
        
    def generate_random_data(self, dim = 2, num_sample=100):
        """
        generate data, if not provided
        """
        rand_num = random.uniform(1, 1000, dim*num_sample)
        self._data = rand_num.reshape(num_sample, dim)

    def cluster(self, r = 5):
        """
        Cluster using k-means 
        """
        self._rand_idx = random.randint(0, self._data.shape[0], r)
        self._cents[i] = self._data[self._rand_idx]  

        for i in self._max_iter:
            while i < self._data.shape[1]: 
                dists = [ np.linalg.norm(self._data[i]-c) for c in self._cents ]
                min_idx = dists.index(min(dists))
                self._neighbors[min_idx].append(self._data[i]) 

            p_cents = self._cents
            for c_id in self._neighbors.keys():
                self._cents[c_id] = self.get_average(c_id)

            converged = False
            for pc, cc in zip(p_cents, self._cents):
                if np.linalg.norm(pc, cc) < 0.0000001:
                   converged = True 

            if converged:
                print("Converged before max iteration")
                return

    def get_average(self, c_id):
        return np.average(self._neighbors[c_id], axis=0) 

    def update_centeroid(self):
        for k in self._neighbors.keys():
            values   = self._neighbors[k]
            centriod = self.get_average(self._data)
            for i in self._data
                dist = np.linalg.norm(centriod - end_pts)

    def print_cluster(self):
        for k, v in self._neighbors.items():
            print("Cluster ", k, v)
         
kmeans = KMeans() 
kmeans.cluster()
kmeans.print_cluster()
kmeans.compute_centeroid()
kmeans.update_centeroid()


