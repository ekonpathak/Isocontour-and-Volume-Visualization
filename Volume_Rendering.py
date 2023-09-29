#2. VTK Volume Rendering and Transfer Function: [40 Points]
#Load the 3D data provided with the assignment.

from vtk import *
reader = vtkXMLImageDataReader()
reader.SetFileName('Isabel_3D.vti')
reader.Update()
data = reader.GetOutput()

#Create instances of vtkColorTransferFunction and vtkPiecewiseFunction (this will work as Opacity transfer function) 
#  and set them up with the values provided below in the tables.


color_transfer = vtkColorTransferFunction();
color_transfer.AddRGBPoint(-4931.54,0,1,1);
color_transfer.AddRGBPoint(-2508.95,0,0,1);
color_transfer.AddRGBPoint(-1873.9,0,0,0.5);
color_transfer.AddRGBPoint(-1027.16,1,0,0);
color_transfer.AddRGBPoint(-298.031,1,0.4,0);
color_transfer.AddRGBPoint(2594.97,1,1,0);

piece_wise_function = vtkPiecewiseFunction();
piece_wise_function.AddPoint(-4931.54,1.0)
piece_wise_function.AddPoint(101.815,0.002)
piece_wise_function.AddPoint(2594.97,0.0)

# By default, advanced shading feature, i.e., Phong shading will be off. Create an input parameter 
# and take input from user if the user wants to use Phong shading. If yes, then your program should 
# turn on Phong shading while rendering.

volume_p = vtkVolumeProperty()
volume_p.SetColor(color_transfer)
volume_p.SetScalarOpacity(piece_wise_function)
volume_p.SetInterpolationTypeToLinear()

#Use vtkOutlineFilter to add an outline to the volume rendered data



outline = vtkOutlineFilter()
outline.SetInputConnection(reader.GetOutputPort())


# Use vtkSmartVolumeMapper() class to perform the volume rendering


volume_mapper = vtkSmartVolumeMapper()
volume_mapper.SetInputData(data)
volume =vtkVolume()
volume.SetMapper(volume_mapper)
volume.SetProperty(volume_p)


actorVolume = vtkVolume()
actorVolume.SetMapper(volume_mapper)
actorVolume.SetProperty(volume_p)


mapper_for_outline = vtkPolyDataMapper()
mapper_for_outline.SetInputConnection(outline.GetOutputPort())
actor_for_outline = vtkActor()
actor_for_outline.SetMapper(mapper_for_outline)
actor_for_outline.GetProperty().SetColor(0,0,0)
actor_for_outline.GetProperty().SetLineWidth(10)


PHONG=input("Write ON / OFF for PHONG : ")

if (PHONG == "ON" or PHONG == "on"):
    
    volume_p.ShadeOn()
    volume_p.SetAmbient(0.5)
    volume_p.SetDiffuse(0.5)
    volume_p.SetSpecular(0.5)
else:
    volume_p.ShadeOff()
        
#Create a 1000x1000 sized render window to show the rendering result.

renderer = vtkRenderer()
renderer.SetBackground(1,1,1)
renderWindow = vtkRenderWindow()
renderWindow.SetSize(1000,1000)
renderWindow.AddRenderer(renderer)
renderWindowInteractor = vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)
renderer.AddActor(actor_for_outline)
renderer.AddVolume(actorVolume)

### Finally render the object
#############################
renderWindow.Render()
renderWindowInteractor.Start()