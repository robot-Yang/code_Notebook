import numpy as np
from ransac import *

def augment(xyzs):
    axyz = np.ones((len(xyzs), 4))
    axyz[:, :3] = xyzs
    return axyz

def estimate(xyzs):
    axyz = augment(xyzs[:3])
    return np.linalg.svd(axyz)[-1][-1, :]

def is_inlier(coeffs, xyz, threshold):
    return np.abs(coeffs.dot(augment([xyz]).T)) < threshold

if __name__ == '__main__':
    import matplotlib
    import matplotlib.pyplot as plt
    from mpl_toolkits import mplot3d
    fig = plt.figure()
    ax = mplot3d.Axes3D(fig)

    def plot_plane(a, b, c, d):
        xx, yy = np.mgrid[:10, :10]
        return xx, yy, (-d - a * xx - b * yy) / c

    

    # # test data
    # xyzs = np.random.random((n, 3)) * 10
    # xyzs[:50, 2:] = xyzs[:50, :1]

    X = []
    Y = []
    Z = []
    # with open('2d_pointcloud.txt', 'r') as f:
    with open('airplane.txt', 'r') as f:
        singleLines = f.readlines()
        for i in singleLines:
            rawLine = i.split(' ')
            X.append(rawLine[0])
            Y.append(rawLine[1])
            Z.append(rawLine[2])

    X.pop(0)
    Y.pop(0)
    Z.pop(0)

    xyzs = np.random.random((len(X), 3))
    # print (xyzs[:,0] )
    xyzs[:,0] = X
    xyzs[:,1] = Y
    xyzs[:,2] = Z



    ax.scatter3D(xyzs.T[0], xyzs.T[1], xyzs.T[2])

    # print (xyzs.T[0])

    n = len(X)
    max_iterations = 100
    goal_inliers = n * 0.1

    # RANSAC
    m, b = run_ransac(xyzs, estimate, lambda x, y: is_inlier(x, y, 0.01), 3, goal_inliers, max_iterations)
    a, b, c, d = m
    xx, yy, zz = plot_plane(a, b, c, d)
    ax.plot_surface(xx, yy, zz, color=(0, 1, 0, 0.5))

    plt.show()