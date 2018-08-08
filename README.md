# Ant-Camera

Ant's Camera project for Anglia Ruskin University

This projects explains how to build and develop a network camera with temperature / humidity sensor. The live stream will be displayed over a HTML file and the footage will be saved remotely over the network.

   1. Hardware : The hardware you will need for this project is a Raspberry Pi 3 Model B, minimum of 16GB Micro SD card, Camera Video Module for Raspberry Pi, Ribbon Cable, DHT11 sensor, 3x Female to Female jumper wires.
    
   2. Environment Requirement: The Raspberry Pi will need an Internet connection for the initial setup, however no Internet connection is required to run/store the stream. The Pi will just require to be connected to the same network as the server on which you wish to display/store the footage. A Laptop/Computer running your choice of Windows 10 / Ubuntu Linux with Etcher installed will be required for the initial set-up. Optionally VNC server installed on the laptop.
    
   3. OS Requirement: Latest Raspbian flashed on a Micro SD card using Etcher. Python 3 installed on the laptop.
   
   4. Installing Motioneye: Please follow the link to install motioneye on your Raspberry Pi; https://github.com/ccrisan/motioneye/wiki/Install-On-Raspbian Connect your camera module to the Pi. On the Pi navigate to Preferences / Raspberry Pi Configuration / Interfaces and enable Camera. Once your Pi has rebooted you should be able to input the Pi's IP address into any browser follower by the port 8765 and see the live feed of your camera.
    
   5. Displaying the Temperature/Humidity: The instructions below are done directly on the Pi itself. Create a Python script which collects the Temperature / Humidity then opens and writes to a file (please see DHT11.py for example) Create a executable file name monitor_1 (please see monitor_1 for example) and place it in the following directory; /etc/motioneye. Refresh the web interface and click on the camera frame. You should now see the temperature / humidity displaying.
    
   6. Setting up a Flask server to transmit the temperature / humidity to a HTML page: Install Flask / CORS for python on the Rapberry Pi. Setup at the Flask server to read the data from your specific file (file.txt) and return it (please see server.py for example). Now run the script and type the IP address of your Raspberry Pi into a web browser followed by your specific port and you should see the the temperature /  humidity.
    
   7.  Setting up a HTML for end user: To set up a simple HTML page for the end user login to the camera, select advance options and navigate to Video Streaming. From here you can use either the Streaming URL address for <img> tags or the Embed URL address for <iframe> tags. You can also include a simple JavaScript function to read the file from your Flask server. You will need to create a second function to update the the temperature / humidity every so often. (please see index.html and include jquery.min.js to run the example)
