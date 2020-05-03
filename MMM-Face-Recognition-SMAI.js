Module.register("MMM-Face-Recognition-SMAI", {


defaults: {
  prompt: "Use FaceID to access profiles",
  fileUrl: "modules/MMM-Face-Recognition-SMAI/public/face.png",
  width: "200px",
  position: "left",
  refreshInterval: 2
},

start: function () {
  this.count = 0
},

getStyles: function () {
        return [
            this.file('css/mmm-style.css')
        ];
    },


getDom: function() {
  var element = document.createElement("div")
  element.className = "face-image"
  element.innerHTML = this.config.prompt
  var subElement = document.createElement("p")
  subElement.id = "COUNT"
  element.appendChild(subElement)

 
  return element
},

//Create Socket Connnection with nodehelper.js
notificationReceived: function(notification, payload, sender) {
  switch(notification) {
    case "DOM_OBJECTS_CREATED":
      var timer = setInterval(()=>{
        this.sendSocketNotification("DO_YOUR_JOB", this.count)
        this.count++
      }, 1000)
      break
  }
},

//Recieve notification from socket of Python Variables via nodehelper.js
socketNotificationReceived: function(notification, payload) {
    switch(notification) {
      case "I_DID":
    //Store Image Here

      var elem = document.getElementById("COUNT")
      elem.innerHTML = "Welcome back, " + payload

      //Creat Image Element Image
    elem.classList.add(this.config.position);
    elem.style.width = this.config.width;
    

    var img = document.createElement("img");
    img.setAttribute('src', this.config.fileUrl);
    elem.appendChild(img);
    return elem
       
    break;
    
    default:
      var elem = document.getElementById("COUNT")
      elem.innerHTML = "Welcome back, User"

        //Creat Image Element Image
    elem.classList.add(this.config.position);
    elem.style.width = this.config.width;
    

    var img = document.createElement("img");
    img.setAttribute('src', "modules/MMM-Face-Recognition-SMAI/public/guest.gif");
    elem.appendChild(img);
    return elem


  }
},

})
