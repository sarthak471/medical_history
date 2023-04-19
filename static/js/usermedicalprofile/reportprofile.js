const addbtn = document.querySelector(".add")

const input  = document.querySelector(".inp-group")


function removeinput(){
    this.parentElement.remove();
}

function addinput(e){
    e.preventDefault();

    
    const imgname = document.createElement("input")
    imgname.type = "text";
    imgname.placeholder = "enter the name"
    imgname.name = "medname"


    const duration = document.createElement("input")
    duration.type = "number";
    duration.placeholder = "enter the duration"
    duration.name = "duration"


    const interval = document.createElement("input")
    interval.type = "number";
    interval.placeholder = "enter the interval"
    interval.name = "interval"

    // const image = document.createElement("input")
    // image.type = "file";
    // image.placeholder ="uploadimage"
    // image.for="formFileMultiple"
    // image.name ="uploadimage"

    const btn = document.createElement("a");
    btn.className ="delete"
    btn.className ="btn"
    btn.innerHTML = "&times"

    const submitbtn = document.createElement("a");
    submitbtn.className ="delete"
    submitbtn.className ="btn"
    submitbtn.innerHTML = "submit"

    btn.addEventListener("click",removeinput)

    const flex  =document.createElement("div");
    flex.className =  "flex"

    input.appendChild(flex)
    flex.appendChild(imgname)
    flex.appendChild(duration)
    flex.appendChild(interval)
    // flex.appendChild(image)
    flex.appendChild(btn)
    // flex.appendChild(submitbtn)

    console.log("leuuuuuu")
}
addbtn.addEventListener("click",addinput)