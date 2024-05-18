import os
import numpy as np
import pandas as pd

"""
/*****************************/
getFileName
/*****************************/
Type : function
Process : return file names in path.
Input : path, filetype, dirname
	path -> <str> directory path.
	filetype -> <str> file type. ex) .jpg, .pdf and so on.
	dirname -> <str> boolean. If True, return absolute name. In other hands, only file name if False
Output : list. This elements is string of file name.
"""
def getFileName(path, filetype, dirname = True):
	if dirname:
		return sorted([os.path.join(path, f) for f in os.listdir(path) if f.endswith(filetype)])
	else:
		return sorted([f for f in os.listdir(path) if f.endswith(filetype)])

def writeCSV(path, data, name = True):
	if type(data) == list:
		data = np.stack(data, axis = 1)
	data = pd.DataFrame(data)
	data.to_csv(path, header = name, index = False)


"""
/*****************************/
getDirName
/*****************************/
Type : function
Process : return directory names in path.
Input : path, include_top
	path -> <str> path.
	include_top -> <str> boolean. If True, return absolute name. In other hands, only dir name if False.
Output : list. This elements is string of file name.
"""
def getDirName(path, include_top = True):
	file = os.listdir(path)

	if include_top:
		return sorted([path + "\\" + f for f in file if os.path.isdir(os.path.join(path, f))])
	else:
		return sorted([f for f in file if os.path.isdir(os.path.join(path, f))])

def writeVTK(filename, shape, size, scalars = [], scalarname = []):
	if len(scalars) != len(scalarname):
		print("Error@piRichard.post.VTK.writeVTK")
		print("len(scalars) should be same with len(scalarname)")
		sys.exit()

	with open(filename, "w") as file:
		#####ジオメトリ構造の書き込み
		file.write("# vtk DataFile Version 2.0\nnumpyVTK\nASCII\n")
		file.write("DATASET STRUCTURED_GRID\n")
		file.write("DIMENSIONS "+str(shape[0])+" "+str(shape[1])+" "+str(shape[2])+"\n")
		file.write("POINTS "+str(shape[0]*shape[1]*shape[2])+" float\n")

		for k in range(shape[2]):
			for j in range(shape[1]):
				for i in range(shape[0]):
					file.write(str(i*size[0])+" "+str(j*size[1])+" "+str(k*size[2])+"\n")

		#####スカラーの書き込み
		if scalars != []:
			file.write("POINT_DATA "+str(shape[0]*shape[1]*shape[2])+"\n")
			
			for _scalar, name in zip(scalars, scalarname):
				#####微小量の丸め込み
				scalar = _scalar.copy()
				scalar[np.abs(scalar) < 1e-20] = 0.
				
				file.write("SCALARS "+name+" float\n")
				file.write("LOOKUP_TABLE default\n")

				for k in range(shape[2]):
					for j in range(shape[1]):
						for i in range(shape[0]):
							file.write(str(scalar[i,j,k])+"\n")