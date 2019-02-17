
# MATLAB Simulation
Entering the `vredit` command in the command prompt causes a `vrworld` editor to
be opened. 
```
>> vredit
```
Alternatively, an argument can be parsed to `vredit` to open it for editing.
```
>> vredit('myVrWorld.wrl')
```
# Python Simulation
Pulsar data has been taken to create a 3D representation of pulsars in our
galaxy. 

All plotting occurs in `plots.py` and data is sourced from `newPulsarCatalogue.csv`

The `csv` file simply contains a `pandas` friendly formatted version of the data
collected here: 
[Pulsar Catalogue](http://www.atnf.csiro.au/research/pulsar/psrcat/)

A python object has been created to facilitate editing the animations
parameters. The `init` method is where these parameters can be found and edited 
by students (?). 
```
class pulsarPlot:
    def __init__(self):
        # All variables used to tune the plots
        self.dataSource = './src/newPulsarCatalogue.csv'
        self.filename   = 'run.mp4'
        self.df         = pd.read_csv(self.dataSource) 
        self.x          = self.df['XX']
        self.y          = self.df['YY']
        self.z          = self.df['ZZ']
        self.date       = self.df['DISC_DATE']
        self.luminosity = self.getLuminosity()
        self.sun        = [0, 8.5, 0]
        self.years      = self.getYears()
        self.fig        = plt.figure(facecolor='k', edgecolor='k')
        self.ax         = self.fig.add_subplot(111, projection='3d')
        self.plotOurSun = True
        self.show       = False
        self.magellanic = False
        self.drawLegend = False
        self.cloudOne   = [-55,-4.0,-25]
        self.cloudTwo   = [0,0,0]
        self.datapSize = 0.5
        self.ax.set_axis_off()
        self.ax.set_facecolor((0.0, 0.0, 0.0))
        self.year_increment = 20
        self.nbFrames = np.arange(0, 360)
        self.fig.subplots_adjust(left=0, bottom=0, right=1, top=1, 
                        wspace=None, hspace=None)
```

Animation can be found in: 
## `out` and `src` folders.

`out` is where a group of previous outputs have been saved. They are titled in
obvious ways as to what they are. I can't vouch that they are useful, but they
were made in the progress of programming.

`src` is short for 'source' and is where source data and source files were
stored. The script was meant to be run from the `pythonAnimation` folder, minor
changes can be made so that this is not the case.

# Live Data from Phones with `MATLAB` mobile app



Install the application from the Apple store or Google Play store.

In `MATLAB` enter: 
```
>> connector on
```
This will prompt you to install the correct libraries. There is one for Android,
one for iOS. 

Again, now that you have the libraries type:
```
>> connector on
```

You will then be given some output, within it you will be an IP address. 

## Conncecting to the computer via phone
You should then use the IP Address output by `connector on` to connect to the computer via the MATLAB mobile app.
This is done on the mobile app via:
1. Select the 'More' tab
2. Select 'Settings'
3. Select 'Add a Computer'
4. Input the IP Address given earlier by the `connector on` command.
5. Input your MATLAB Mathworks account password (Beware it will appear in plain
   text).
6. Navigate back to the 'More' tab landing page.
7. Select 'Sensors'
8. Tap one of the icons on the top row to begin accessing the device's sensors.
9. Ensure the 'Stream to MATLAB' box is checked.
10. Click 'Start'

## Accessing the Data in MATLAB
1. `>> m = mobiledev`
2. `>> properties(m)`
This will output the class' data type, methods and attributes. Within there will
be arrays of all the streaming data.

A simple test is to stream the angular orientation, display the array when the
phone is oriented one way, rotate the phone, then print it out again. The values
should change.

Streaming of data can then occur from the mobile to the MATLAB console via an
object.



# Possible VR Exercise -- Non-Interactive VR

## Pre-Work:

1. Download application _Mobile VR Station_ on iOS or Andriod device.
2. Navigate to: '`Browse Content...`' > '`Google Drive`'
3. Sign in to your Google Drive account. 
4. View test video. `blocks_squeezing.mp4` (?)

## In-Lab Workflow:

1. Tune the python program.
2. Run it.
3. Take output file, put it onto Google Drive.
4. Play video in Headset in `2D 360 Mode`
