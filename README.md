# Shooter-Plotter

This is just a rather simple setup that allows one to run a test, tether to the robot, move the log file to a given folder with winscp, and run this program to see plots of velocity over time for the current Velo PID constants. It also handles the sorting through the data to pick the right set of times to plot automatically. 


**Instructions for setup**

1. Make sure you have Python 3 installed along with matplotlib. 
2. Configure the robot to log each cycle the time, and the measured velocity of the shooter. Within the subsystem, also log a boolean that's set to true only when the command that runs the velo pid on the shooter is active. 
3. Set x_row, y_row, and bool_row to be indices of respectively the time, velocity, and boolean columns of the log file. 
4. Configure a min speed values below which are not plotted. This is sometimes helpful for trimming the plot for readability. 
5. Configure a directory (folder) on your machine to store all the log files. The program will automatically search for the last modified one of these files, so it's intended to be a bit of a dumping ground. 
6. For some given set of PID constants, with the logs configured, plug in the logging stick, start the robot, and run the shoot command. Tether to the robot, find the log file with winscp (you could also take out the logging stick, but this way is generally faster), and copy the file to the directory. 
7. Run the code and see the desired plot, repeating step 6 as neccessary for tuning. 
