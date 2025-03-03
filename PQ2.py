"""Q2. As a DevOps engineer, it is crucial to monitor the health and performance of servers. Write a Python program to monitor the health of the CPU. Few pointers to be noted:

●       The program should continuously monitor the CPU usage of the local machine.

●       If the CPU usage exceeds a predefined threshold (e.g., 80%), an alert message should be displayed.

●       The program should run indefinitely until interrupted.

●       The program should include appropriate error handling to handle exceptions that may arise during the monitoring process.

Hint:

●       The psutil library in Python can be used to retrieve system information, including CPU usage. You can install it using pip install psutil.

●       Use the psutil.cpu_percent() method to get the current CPU usage as a percentage.

Expected Output:

Monitoring CPU usage...

Alert! CPU usage exceeds threshold: 85%

Alert! CPU usage exceeds threshold: 90%

... (continues until interrupted) """
import psutil as ps
import keyboard as k #to take keyboard input

def cpu_health_montior():

    try:

        while True:
            cpu_usage = ps.cpu_percent(interval=1) #calculate cpu usage in percentage at an interval of 1 sec
            if(cpu_usage>80): #if the CPU usage exceeds 80%
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")  #ALert message
            else:
                print(f"CPU usage: {cpu_usage}%")
                if k.is_pressed('enter'):     
                    print("Stopped Monitoring CPU usage") #default till not stopped
                    break
    except Exception as e:
        print(f"Error occured during monitoring: {e}")


if __name__=="__main__":    


    print("Monitoring CPU usage...")
    print("Press Enter to exit!")
    cpu_health_montior()

