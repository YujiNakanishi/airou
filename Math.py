import numpy as np
import copy

"""
process : shapeに合わせた座標値を返す
input :
	shape -> <tuple> 配列形状。
	size -> <tuple> 格子サイズ
	original -> <np array:float>　原点座標
"""
def GridCoordinate(shape, size, original = None):
	if original is None:
		original = np.zeros(len(shape))
	if len(shape) == 3:
		x_cor = np.stack([np.arange(shape[0])*size[0] + 0.5*size[0] for i in range(shape[1])], axis = 1)
		x_cor = np.stack([x_cor for i in range(shape[2])], axis = -1) + original[0]
		y_cor = np.stack([np.ones(shape[0])*i*size[1] + 0.5*size[1] for i in range(shape[1])], axis = 1)
		y_cor = np.stack([y_cor for i in range(shape[2])], axis = -1) + original[1]
		z_cor = np.stack([np.ones((shape[0], shape[1]))*i*size[2] + 0.5*size[2] for i in range(shape[2])], axis = -1)+original[2]

		coordinate = np.stack((x_cor, y_cor, z_cor), axis = -1)
		return coordinate
	else:
		x_cor = np.stack([np.arange(shape[0])*size[0] + 0.5*size[0] for i in range(shape[1])], axis = 1)
		y_cor = np.stack([np.ones(shape[0])*i*size[1] + 0.5*size[1] for i in range(shape[1])], axis = 1)

		coordinate = np.stack((x_cor, y_cor), axis = -1)
		return coordinate

def SparceValue(val, num):
	if len(val.shape) == 2:
		x_size = int(val.shape[0]/(num[0]+1))
		y_size = int(val.shape[1]/(num[1]+1))
		x_index = np.tile(x_size*np.arange(1, num[0]+1), num[1]).astype(int)
		y_index = np.concatenate([np.ones(num[0])*(i+1)*y_size for i in range(num[1])]).astype(int)
		sparce_val = np.copy(val[x_index, y_index])

		return x_index, y_index, sparce_val

	else:
		x_size = int(val.shape[0]/(num[0]+1))
		y_size = int(val.shape[1]/(num[1]+1))
		z_size = int(val.shape[2]/(num[2]+1))
		z_index = np.tile(z_size*np.arange(1, num[2]+1), num[0]*num[1]).astype(int)
		y_index = np.concatenate([np.ones(num[2])*(i+1)*y_size for i in range(num[1])])
		y_index = np.tile(y_index, num[0]).astype(int)
		x_index = np.concatenate([np.ones(num[2]*num[1])*(i+1)*x_size for i  in range(num[0])]).astype(int)

		sparce_val = np.copy(val[x_index, y_index, z_index])

		return x_index, y_index, z_index, sparce_val


def ref_emptyList(shape, dim, count, l):
	count += 1
	list_container = [copy.deepcopy(l) for i in range(shape[-count])]
	if dim == count:
		return list_container
	else:
		return ref_emptyList(shape, dim, count, list_container)




def emptyList(shape):
	return ref_emptyList(shape, len(shape), 0, [])