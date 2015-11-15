## Pecube2catchments

This script reads the VTK output age files from Pecube HUGG (`Ages###.vtk`) and combines them with catchment data files stored in a `.csv` file format.
The catchment data includes the latitude, longitude and elevations of all points within a given catchment, and a number of other fields derived at those points, including calculations of the channel steepness index (*k*<sub>sn</sub>) or specific stream power.
The Pecube output files are probed at all points where data is given in the catchment to determine predicted ages for all catchment points using a bilinear interpolation.
The output is another `.csv` file with the merged Pecube and catchment data.

![alt text](http://i.creativecommons.org/l/by-nc/3.0/88x31.png "Creative Commons License")
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/3.0/deed.en_US">[Creative Commons Attribution-NonCommercial 3.0 Unported License](http://creativecommons.org/licenses/by-nc/3.0/deed.en_US).
