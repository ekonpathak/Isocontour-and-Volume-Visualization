## Import VTK
from vtk import *

## Load data

reader = vtkXMLImageDataReader()
reader.SetFileName('Isabel_2D.vti')
reader.Update()
data = reader.GetOutput()

numCells = data.GetNumberOfCells()

## create a surface representation from 2D uniform grid data
surface = vtkGeometryFilter()
surface.SetInputData(data)
surface.Update()

## Output of geometry filter is a vtkpolydata
pdata = surface.GetOutput()
Prange = pdata.GetPointData().GetArray('Pressure').GetRange()


p=float(input("Choose Pressure isovalue  in Range ( -1434 , 630 ) :  "))

points = vtkPoints()

for i in range (62000):
    cell = data.GetCell(i)
    ## Query the 4 corner points of the cell
    #########################################
    pid1 = cell.GetPointId(0)
    pid2 = cell.GetPointId(1)
    pid3 = cell.GetPointId(3)
    pid4 = cell.GetPointId(2)
    ## Get values at each vertex
    ## First Get the array
    dataArr = data.GetPointData().GetArray('Pressure')
    val1 = dataArr.GetTuple1(pid1)
    val2 = dataArr.GetTuple1(pid2)
    val3 = dataArr.GetTuple1(pid3)
    val4 = dataArr.GetTuple1(pid4)
    
    if (p < dataArr.GetTuple1(pid1)):
        
        if (p < dataArr.GetTuple1(pid2)):
            
            if (p < dataArr.GetTuple1(pid3)):
                
                if (p < dataArr.GetTuple1(pid4)):
                    pass
                else:
                    dx=(val4-p)/(val4-val1)*(data.GetPoint(pid1)[0]-data.GetPoint(pid4)[0])+data.GetPoint(pid4)[0]
                    dy=(val4-p)/(val4-val1)*(data.GetPoint(pid1)[1]-data.GetPoint(pid4)[1])+data.GetPoint(pid4)[1]
                    
                    p1=[dx,dy,25]
                    points.InsertNextPoint(p1)
                    dx=(val4-p)/(val4-val3)*(data.GetPoint(pid3)[0]-data.GetPoint(pid4)[0])+data.GetPoint(pid4)[0]
                    dy=(val4-p)/(val4-val3)*(data.GetPoint(pid3)[1]-data.GetPoint(pid4)[1])+data.GetPoint(pid4)[1]
                    
                    p2=[dx,dy,25]
                    points.InsertNextPoint(p2)
                    
            else:
                if (p < dataArr.GetTuple1(pid4)):
                    dx=(val3-p)/(val3-val2)*(data.GetPoint(pid2)[0]-data.GetPoint(pid3)[0])+data.GetPoint(pid3)[0]
                    dy=(val3-p)/(val3-val2)*(data.GetPoint(pid2)[1]-data.GetPoint(pid3)[1])+data.GetPoint(pid3)[1]
                    
                    p1=[dx,dy,25]
                    points.InsertNextPoint(p1)
                    dx=(val3-p)/(val3-val4)*(data.GetPoint(pid4)[0]-data.GetPoint(pid3)[0])+data.GetPoint(pid3)[0]
                    dy=(val3-p)/(val3-val4)*(data.GetPoint(pid4)[1]-data.GetPoint(pid3)[1])+data.GetPoint(pid3)[1]
                    
                    p2=[dx,dy,25]
                    points.InsertNextPoint(p2)
            
                else:
                    dx=(val4-p)/(val4-val1)*(data.GetPoint(pid1)[0]-data.GetPoint(pid4)[0])+data.GetPoint(pid4)[0]
                    dy=(val4-p)/(val4-val1)*(data.GetPoint(pid1)[1]-data.GetPoint(pid4)[1])+data.GetPoint(pid4)[1]
                    
                    p1=[dx,dy,25]
                    points.InsertNextPoint(p1)
                    dx=(val3-p)/(val3-val2)*(data.GetPoint(pid2)[0]-data.GetPoint(pid3)[0])+data.GetPoint(pid3)[0]
                    dy=(val3-p)/(val3-val2)*(data.GetPoint(pid2)[1]-data.GetPoint(pid3)[1])+data.GetPoint(pid3)[1]
                    
                    p2=[dx,dy,25]
                    points.InsertNextPoint(p2)
                    
        else:
            
            if (p < dataArr.GetTuple1(pid3)):  
                if (p < dataArr.GetTuple1(pid4)):
                    dx=(val2-p)/(val2-val1)*(data.GetPoint(pid1)[0]-data.GetPoint(pid2)[0])+data.GetPoint(pid2)[0]
                    dy=(val2-p)/(val2-val1)*(data.GetPoint(pid1)[1]-data.GetPoint(pid2)[1])+data.GetPoint(pid2)[1]
                    
                    p1=[dx,dy,25]
                    points.InsertNextPoint(p1)
                    dx=(val2-p)/(val2-val3)*(data.GetPoint(pid3)[0]-data.GetPoint(pid2)[0])+data.GetPoint(pid2)[0]
                    dy=(val2-p)/(val2-val3)*(data.GetPoint(pid3)[1]-data.GetPoint(pid2)[1])+data.GetPoint(pid2)[1]
                      
                    p2=[dx,dy,25]
                    points.InsertNextPoint(p2)
                    
                else:
                    dx=(val2-p)/(val2-val1)*(data.GetPoint(pid1)[0]-data.GetPoint(pid2)[0])+data.GetPoint(pid2)[0]
                    dy=(val2-p)/(val2-val1)*(data.GetPoint(pid1)[1]-data.GetPoint(pid2)[1])+data.GetPoint(pid2)[1]
                    
                    p1=[dx,dy,25]
                    points.InsertNextPoint(p1)
                    dx=(val2-p)/(val2-val3)*(data.GetPoint(pid3)[0]-data.GetPoint(pid2)[0])+data.GetPoint(pid2)[0]
                    dy=(val2-p)/(val2-val3)*(data.GetPoint(pid3)[1]-data.GetPoint(pid2)[1])+data.GetPoint(pid2)[1]
                      
                    p2=[dx,dy,25]
                    points.InsertNextPoint(p2)
                    dx=(val4-p)/(val4-val1)*(data.GetPoint(pid1)[0]-data.GetPoint(pid4)[0])+data.GetPoint(pid4)[0]
                    dy=(val4-p)/(val4-val1)*(data.GetPoint(pid1)[1]-data.GetPoint(pid4)[1])+data.GetPoint(pid4)[1]
                    
                    p3=[dx,dy,25]
                    points.InsertNextPoint(p3)
                    dx=(val4-p)/(val4-val3)*(data.GetPoint(pid3)[0]-data.GetPoint(pid4)[0])+data.GetPoint(pid4)[0]
                    dy=(val4-p)/(val4-val3)*(data.GetPoint(pid3)[1]-data.GetPoint(pid4)[1])+data.GetPoint(pid4)[1]
                    
                    p4=[dx,dy,25]
                    points.InsertNextPoint(p4)
                
            else:
                if (p < dataArr.GetTuple1(pid4)):
                    dx=(val2-p)/(val2-val1)*(data.GetPoint(pid1)[0]-data.GetPoint(pid2)[0])+data.GetPoint(pid2)[0]
                    dy=(val2-p)/(val2-val1)*(data.GetPoint(pid1)[1]-data.GetPoint(pid2)[1])+data.GetPoint(pid2)[1]
                    
                    p1=[dx,dy,25]
                    points.InsertNextPoint(p1)
                    dx=(val3-p)/(val3-val4)*(data.GetPoint(pid4)[0]-data.GetPoint(pid3)[0])+data.GetPoint(pid3)[0]
                    dy=(val3-p)/(val3-val4)*(data.GetPoint(pid4)[1]-data.GetPoint(pid3)[1])+data.GetPoint(pid3)[1]
                    
                    p2=[dx,dy,25]
                    points.InsertNextPoint(p2)
                else:
                    dx=(val2-p)/(val2-val1)*(data.GetPoint(pid1)[0]-data.GetPoint(pid2)[0])+data.GetPoint(pid2)[0]
                    dy=(val2-p)/(val2-val1)*(data.GetPoint(pid1)[1]-data.GetPoint(pid2)[1])+data.GetPoint(pid2)[1]
                    
                    p1=[dx,dy,25]
                    points.InsertNextPoint(p1)
                    dx=(val4-p)/(val4-val1)*(data.GetPoint(pid1)[0]-data.GetPoint(pid4)[0])+data.GetPoint(pid4)[0]
                    dy=(val4-p)/(val4-val1)*(data.GetPoint(pid1)[1]-data.GetPoint(pid4)[1])+data.GetPoint(pid4)[1]
                    
                    p2=[dx,dy,25]
                    points.InsertNextPoint(p2)
    else:
        if (p < dataArr.GetTuple1(pid2)):
            
            if (p < dataArr.GetTuple1(pid3)):
                
                if (p < dataArr.GetTuple1(pid4)):
                    dx=(val1-p)/(val1-val2)*(data.GetPoint(pid2)[0]-data.GetPoint(pid1)[0])+data.GetPoint(pid1)[0]
                    dy=(val1-p)/(val1-val2)*(data.GetPoint(pid2)[1]-data.GetPoint(pid1)[1])+data.GetPoint(pid1)[1]
                    
                    p1=[dx,dy,25]
                    points.InsertNextPoint(p1)
                    dx=(val1-p)/(val1-val4)*(data.GetPoint(pid4)[0]-data.GetPoint(pid1)[0])+data.GetPoint(pid1)[0]
                    dy=(val1-p)/(val1-val4)*(data.GetPoint(pid4)[1]-data.GetPoint(pid1)[1])+data.GetPoint(pid1)[1]
                    
                    p2=[dx,dy,25]
                    points.InsertNextPoint(p2)
                    
                else:
                    dx=(val4-p)/(val4-val3)*(data.GetPoint(pid3)[0]-data.GetPoint(pid4)[0])+data.GetPoint(pid4)[0]
                    dy=(val4-p)/(val4-val3)*(data.GetPoint(pid3)[1]-data.GetPoint(pid4)[1])+data.GetPoint(pid4)[1]
                    
                    p1=[dx,dy,25]
                    points.InsertNextPoint(p1)
                    dx=(val1-p)/(val1-val2)*(data.GetPoint(pid2)[0]-data.GetPoint(pid1)[0])+data.GetPoint(pid1)[0]
                    dy=(val1-p)/(val1-val2)*(data.GetPoint(pid2)[1]-data.GetPoint(pid1)[1])+data.GetPoint(pid1)[1]
                    
                    p2=[dx,dy,25]
                    points.InsertNextPoint(p2)
                
            else:
                if (p < dataArr.GetTuple1(pid4)):
                    dx=(val3-p)/(val3-val2)*(data.GetPoint(pid2)[0]-data.GetPoint(pid3)[0])+data.GetPoint(pid3)[0]
                    dy=(val3-p)/(val3-val2)*(data.GetPoint(pid2)[1]-data.GetPoint(pid3)[1])+data.GetPoint(pid3)[1]
                    
                    p1=[dx,dy,25]
                    points.InsertNextPoint(p1)
                    dx=(val3-p)/(val3-val4)*(data.GetPoint(pid4)[0]-data.GetPoint(pid3)[0])+data.GetPoint(pid3)[0]
                    dy=(val3-p)/(val3-val4)*(data.GetPoint(pid4)[1]-data.GetPoint(pid3)[1])+data.GetPoint(pid3)[1]
                    
                    p2=[dx,dy,25]
                    points.InsertNextPoint(p2)
                    dx=(val1-p)/(val1-val2)*(data.GetPoint(pid2)[0]-data.GetPoint(pid1)[0])+data.GetPoint(pid1)[0]
                    dy=(val1-p)/(val1-val2)*(data.GetPoint(pid2)[1]-data.GetPoint(pid1)[1])+data.GetPoint(pid1)[1]
                    
                    p3=[dx,dy,25]
                    points.InsertNextPoint(p3)
                    dx=(val1-p)/(val1-val4)*(data.GetPoint(pid4)[0]-data.GetPoint(pid1)[0])+data.GetPoint(pid1)[0]
                    dy=(val1-p)/(val1-val4)*(data.GetPoint(pid4)[1]-data.GetPoint(pid1)[1])+data.GetPoint(pid1)[1]
                    
                    p4=[dx,dy,25]
                    points.InsertNextPoint(p4)
                    
                else:
                    dx=(val1-p)/(val1-val2)*(data.GetPoint(pid2)[0]-data.GetPoint(pid1)[0])+data.GetPoint(pid1)[0]
                    dy=(val1-p)/(val1-val2)*(data.GetPoint(pid2)[1]-data.GetPoint(pid1)[1])+data.GetPoint(pid1)[1]
                    
                    p1=[dx,dy,25]
                    points.InsertNextPoint(p1)
                    dx=(val3-p)/(val3-val2)*(data.GetPoint(pid2)[0]-data.GetPoint(pid3)[0])+data.GetPoint(pid3)[0]
                    dy=(val3-p)/(val3-val2)*(data.GetPoint(pid2)[1]-data.GetPoint(pid3)[1])+data.GetPoint(pid3)[1]
                    
                    p2=[dx,dy,25]
                    points.InsertNextPoint(p2)
                
        else:
            if (p < dataArr.GetTuple1(pid3)):
                
                if (p < dataArr.GetTuple1(pid4)):
                    dx=(val2-p)/(val2-val3)*(data.GetPoint(pid3)[0]-data.GetPoint(pid2)[0])+data.GetPoint(pid2)[0]
                    dy=(val2-p)/(val2-val3)*(data.GetPoint(pid3)[1]-data.GetPoint(pid2)[1])+data.GetPoint(pid2)[1]
                      
                    p1=[dx,dy,25]
                    points.InsertNextPoint(p1)
                    dx=(val1-p)/(val1-val4)*(data.GetPoint(pid4)[0]-data.GetPoint(pid1)[0])+data.GetPoint(pid1)[0]
                    dy=(val1-p)/(val1-val4)*(data.GetPoint(pid4)[1]-data.GetPoint(pid1)[1])+data.GetPoint(pid1)[1]
                    
                    p2=[dx,dy,25]
                    points.InsertNextPoint(p2)
                    
                else:
                    dx=(val4-p)/(val4-val3)*(data.GetPoint(pid3)[0]-data.GetPoint(pid4)[0])+data.GetPoint(pid4)[0]
                    dy=(val4-p)/(val4-val3)*(data.GetPoint(pid3)[1]-data.GetPoint(pid4)[1])+data.GetPoint(pid4)[1]
                    
                    p1=[dx,dy,25]
                    points.InsertNextPoint(p1)
                    dx=(val2-p)/(val2-val3)*(data.GetPoint(pid3)[0]-data.GetPoint(pid2)[0])+data.GetPoint(pid2)[0]
                    dy=(val2-p)/(val2-val3)*(data.GetPoint(pid3)[1]-data.GetPoint(pid2)[1])+data.GetPoint(pid2)[1]
                      
                    p2=[dx,dy,25]
                    points.InsertNextPoint(p2)
                
            else:
                if (p < dataArr.GetTuple1(pid4)):
                    dx=(val3-p)/(val3-val4)*(data.GetPoint(pid4)[0]-data.GetPoint(pid3)[0])+data.GetPoint(pid3)[0]
                    dy=(val3-p)/(val3-val4)*(data.GetPoint(pid4)[1]-data.GetPoint(pid3)[1])+data.GetPoint(pid3)[1]
                    
                    p1=[dx,dy,25]
                    points.InsertNextPoint(p1)
                    dx=(val1-p)/(val1-val4)*(data.GetPoint(pid4)[0]-data.GetPoint(pid1)[0])+data.GetPoint(pid1)[0]
                    dy=(val1-p)/(val1-val4)*(data.GetPoint(pid4)[1]-data.GetPoint(pid1)[1])+data.GetPoint(pid1)[1]
                    p2=[dx,dy,25]
                    points.InsertNextPoint(p2)
    
                else:
                    pass

size_of_points=points.GetNumberOfPoints()


polyLine = vtkPolyLine()
pdata=vtkPolyData()
lines = vtkCellArray()
pdata.SetPoints(points)
## Adding line segments counter clockwise
for i in range(0,size_of_points,2):
    polyLine.GetPointIds().SetNumberOfIds(2)
    polyLine.GetPointIds().SetId(0,i)
    polyLine.GetPointIds().SetId(1, i+1)
    lines.InsertNextCell(polyLine)

### Add points and cells to polydata
####################################
    #pdata.SetPoints(points)
pdata.SetLines(lines)
writer = vtkXMLPolyDataWriter()
writer.SetInputData(pdata)
writer.SetFileName('line.vtp')
writer.Write()                    




### Load Data
########################
reader = vtkXMLPolyDataReader()
reader.SetFileName('line.vtp') ## polyline.vtp
reader.Update()

### get polydata object out from reader
#######################################
pdata = reader.GetOutput()


### Setup mapper and actor
##########################
mapper = vtkPolyDataMapper()
mapper.SetInputData(pdata)
actor = vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetLineWidth(5) ## set line width
actor.GetProperty().SetColor(1,0,0) ## set line color red


### Setup render window, renderer, and interactor
##################################################
renderer = vtkRenderer()
renderer.SetBackground(1,1,1)
renderWindow = vtkRenderWindow()
renderWindow.SetSize(800,800)
renderWindow.AddRenderer(renderer)
renderWindowInteractor = vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)
renderer.AddActor(actor)


### Finally render the object
#############################
renderWindow.Render()
renderWindowInteractor.Start()       