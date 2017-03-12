# coding=utf-8
import scipy.io as sio
from sklearn.cluster import KMeans
import numpy as np
import random
import copy
import matplotlib.pyplot as plt
import operator

def loaddata():  # 读取数据
    file = 'GaussianData.mat'
    file = 'ringData.mat'
    data = sio.loadmat(file)
    matrix = np.array(data['Dataset'])
    return matrix
def distance(p1,p2):  # 欧式距离
    return  np.linalg.norm(p1-p2)
def getWbyKNN(data,k):  # 利用KNN获得相似度矩阵
    points_num = len(data)
    dis_matrix = np.zeros((points_num,points_num))
    W = np.zeros((points_num,points_num))
    for i in range(points_num):
        for j in range(i+1,points_num):
            dis_matrix[i][j] = dis_matrix[j][i] = distance(data[i],data[j])
    for idx,each in enumerate(dis_matrix):
        index_array  = np.argsort(each)
        W[idx][index_array[1:k+1]] = 1  # 距离最短的是自己
    tmp_W = np.transpose(W)
    W = (tmp_W+W)/2  #转置相加除以2是为了让矩阵对称
    return W
def getD(W):    # 获得度矩阵
    points_num = len(W)
    D = np.diag(np.zeros(points_num))
    for i in range(points_num):
        D[i][i] = sum(W[i])
    return D
def getEigVec(L,cluster_num):  #从拉普拉斯矩阵获得特征矩阵
    eigval,eigvec = np.linalg.eig(L)
    dim = len(eigval)
    dictEigval = dict(zip(eigval,range(0,dim)))
    kEig = np.sort(eigval)[0:cluster_num]
    ix = [dictEigval[k] for k in kEig]
    return eigval[ix],eigvec[:,ix]
def randRGB():
    return (random.randint(0, 255)/255.0,
            random.randint(0, 255)/255.0,
            random.randint(0, 255)/255.0)
def plot(matrix,C,centers,k):
    colors = []
    for i in range(k):
        colors.append(randRGB())
    for idx,value in enumerate(C):
        plt.plot(matrix[idx][0],matrix[idx][1],'o',color=colors[int(C[idx])])
    for i in range(len(centers)):
        plt.plot(centers[i][0],centers[i][1],'rx')
    plt.show()
def getCenters(data,C):  # 获得中心位置
    centers = []
    for i in range(max(C)+1):
        points_list = np.where(C==i)[0].tolist()
        centers.append(np.average(data[points_list],axis=0))
    return centers
if __name__ == '__main__':
    cluster_num = 2
    KNN_k = 5
    data = loaddata()
    W = getWbyKNN(data,KNN_k)
    D = getD(W)
    L = D-W
    eigval,eigvec = getEigVec(L,cluster_num)
    # print eigval,eigvec
    clf = KMeans(n_clusters=cluster_num)
    s = clf.fit(eigvec)
    C = s.labels_
    centers = getCenters(data,C)
    plot(data,s.labels_,centers,cluster_num)