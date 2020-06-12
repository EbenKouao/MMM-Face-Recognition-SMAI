# MMM-Face-Recognition-SMAI

A module for the [MagicMirror](https://github.com/MichMich/MagicMirror) project by [SmartBuilds.io](http:smartbuilds.io) adding (faceID) face recognition.

## How it works
This module allows you to access profiles using face recognition. This works on the back of OpenCV face recognition module. 

## Screenshots
| ![FaceID Guest](img/readme/face-recognition-guest-smai.png) | ![Face ID Detected](img/readme/face-recognition-stark-smai.png) | 
|---|---|
| A guest profile as default | User has been recognised |


## Preconditions

* MagicMirror<sup>2</sup> instance
* Node.js version >= 7
* npm
* [OpenCV face-recognition](https://github.com/ageitgey/face_recognition)
* Raspberry Pi 4 Camera Module


## Step 1 – Install the module
In your MagicMirror directory:

```bash cd modules
   git clone https://github.com/EbenKouao/MMM-Face-Recognition-SMAI.git
   cd MMM-face-rec
   npm install
```

## Step 2 – Add files to the Config.js
Here is an example for an entry in `config.js`

```javascript
{
  module: "MMM-Face-Recognition-SMAI",
  position: "top_right",
  config: {
    //prompt: "Put in your own text"
  }
  
  
}
```

## Step 3 – Configuring the Face Recognition Python Script
**Pre-requisite:** Ageitgey Face_recognition Library is installed:

Run the python script seen in the /MMM-Face-Recognition-SMAI. Creating an Autostart script is recommended to keep it running in the background of you MagicMirror.
```bash cd modules
sudo python3 /home/pi/MagicMirror/modules/MMM-Face-Recognition-SMAI/MMM-Face-Recognition-SMAI.py
```
You could test a successful installation by running the Python script.
From here you could program to add multiple profiles. We encourage contribution to this project.

## Download Beta image of MMM-Face-Recognition-SMAI integration
Any troubles installing, try out the already compiled Raspberry Pi (Buster) Image of [Magic Mirror with Face Recognition](https://smartbuilds.io) module.
![Face Recognition on Raspberry Pi 4](img/readme/touchscreen-ui.png)


