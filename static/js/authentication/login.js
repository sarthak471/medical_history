const userNameField = document.querySelector('#usernameField')
const userNamefeedBackArea = document.querySelector(".username_invalid_feedback")
const usernameSuccessfullOutput = document.querySelector(".username_successfull_output")

const submitBtn = document.querySelector('.submit-btn')


let a = 0 , b = 0 , c = 0;

const debounce = (fu,delay)=>{
  let timeoutID;
  return function(...args){
    if(timeoutID){
      clearTimeout(timeoutID);
    }
    timeoutID = setTimeout(() =>{
      fu(...args)
    },delay);
  }
}

function getCookie() {
  var cookieArr = document.cookie.split(";");
  var cookiePair = cookieArr[0].split("=");
return cookiePair[1];
}

csrftoken = getCookie()

userNameField.addEventListener("input",debounce( e => {

    const usernameVal = e.target.value;
    usernameSuccessfullOutput.style.display = "block";
    usernameSuccessfullOutput.textContent = ''
    userNameField.classList.remove("is-invalid");
    userNamefeedBackArea.style.display = "none";

    buttonstatus();

    if (usernameVal.length > 0) {
      usernameSuccessfullOutput.textContent = `checking ${usernameVal}`;
      fetch("/auth/validateUsername/", {
        body: JSON.stringify({ username: usernameVal }),
        method: "POST",
        headers: { "X-CSRFToken": csrftoken }
      })
        .then((res) => res.json())
        .then((data) => {
            console.log("data",data)
            usernameSuccessfullOutput.style.display = "None";
            if(data.username_error){
                submitBtn.disabled = true;
                userNameField.classList.add("is-invalid");
                userNamefeedBackArea.style.display = "block";
                userNamefeedBackArea.innerHTML = `<p>${data.username_error}</p>`;
            }
            else{
              a = 1;
            }
        }); 
    }
  },1000)
  );


  const emailNameField = document.querySelector('#emailField')
  const emailfeedBackArea = document.querySelector(".email_invalid_feedback")
  const emailSuccessfullOutput = document.querySelector(".email_successfull_output")

  emailNameField.addEventListener("input", debounce ( e => {

      const emailVal = e.target.value;
      emailSuccessfullOutput.style.display = "block";
      emailSuccessfullOutput.textContent = ''
      emailNameField.classList.remove("is-invalid");
      emailfeedBackArea.style.display = "none";

      buttonstatus(); 

      if (emailVal.length > 0) {
        emailSuccessfullOutput.textContent = `checking ${emailVal}`;
        fetch("/auth/validateEmail/", {
          body: JSON.stringify({ email: emailVal }),
          method: "POST",
          headers: { "X-CSRFToken": csrftoken }
        })
          .then((res) => res.json())
          .then((data) => {
              console.log("data",data)
              emailSuccessfullOutput.style.display = "None";
              if(data.email_error){
                  submitBtn.disabled = true;
                  emailNameField.classList.add("is-invalid");
                  emailfeedBackArea.style.display = "block";
                  emailfeedBackArea.innerHTML = `<p>${data.email_error}</p>`;
              }
              else{
                b = 1;
              }
          }); 
      }
    },1000));

const showPasswordToggle= document.querySelector('.showPasswordToggle')
const passwordField= document.querySelector('#passwordField')
const passwordFeedback = document.querySelector(".password_invalid_feedback")
const passwordSuccessfullOutput = document.querySelector(".password_successfull_output")

showPasswordToggle.addEventListener("click",e =>{
  if(showPasswordToggle.textContent == "SHOW"){
    showPasswordToggle.textContent = "HIDE";
    passwordField.setAttribute("type","text")
  }
  else{
    passwordField.setAttribute("type","password")
    showPasswordToggle.textContent = "SHOW";
  }
})


passwordField.addEventListener("input",  e => {
    const p = e.target.value
    passwordSuccessfullOutput.style.display = "block";
    passwordSuccessfullOutput.textContent = ''
    passwordField.classList.add("is-invalid");
    passwordFeedback.style.display = "none";

    passwordSuccessfullOutput.textContent = `checking...................`;

    if (p.length < 8) {
      c = 0
      passwordSuccessfullOutput.style.display = "none";
      passwordFeedback.style.display = "block";
      passwordFeedback.innerHTML = `<p>Your password must be at least 8 characters</p>`;
      passwordField.classList.add("is-invalid");
    }
    if (p.search(/[a-z]/i) < 0) {
      c = 0
      passwordSuccessfullOutput.style.display = "none";
      passwordFeedback.style.display = "block";
      passwordFeedback.innerHTML = `<p>Your password must contain at least one letter.</p>`;
        passwordField.classList.add("is-invalid");

    }
    if (p.search(/[0-9]/) < 0) {
      c= 0
      passwordSuccessfullOutput.style.display = "none";
      passwordFeedback.style.display = "block";
      passwordFeedback.innerHTML = `<p>Your password must contain at least one digit.</p>`;
        passwordField.classList.add("is-invalid");
    }
    else{
            c =1;
            passwordSuccessfullOutput.style.display = "none";
            passwordField.classList.remove("is-invalid");
            passwordFeedback.style.display = "None";
    }
    buttonstatus();
  },);
      

function buttonstatus(){
  console.log(a,b,c)
  if(a == 1 && b == 1 && c == 1){
    submitBtn.removeAttribute("disabled")
  }
  else{
    submitBtn.disabled = true;
  }
}




































// const myform = document.querySelector(".myform")

// myform.addEventListener("submit", e => {
//   e.preventDefault();
//   if(userNameField.value.length == 0){
//     userNamefeedBackArea.style.display = "block";
//     userNamefeedBackArea.innerHTML = `<p>Username can not be empty </p>`;
//     userNameField.classList.add("is-invalid");
//   }
//   else{
//     userNamefeedBackArea.style.display = "none";
//     userNameField.classList.remove("is-invalid");
//   }
//   if(emailNameField.value.length == 0){
//     emailfeedBackArea.style.display = "block";
//     emailfeedBackArea.innerHTML = `<p>email can not be empty </p>`;
//     emailNameField.classList.add("is-invalid");
//   }
//   else{
//     emailfeedBackArea.style.display = "none";
//     emailNameField.classList.remove("is-invalid");
//   }
//   if(passwordField.value.length == 0){
//     passwordFeedback.style.display = "block";
//     passwordFeedback.innerHTML = `<p>Password can not be empty </p>`;
//     passwordField.classList.add("is-invalid");
//   }
//   else{
//     passwordFeedback.style.display = "none";
//     passwordField.classList.remove("is-invalid");

//   }
//   if(emailNameField.value.length > 0 && userNameField.value.length > 0  && passwordField.value.length > 0 ){
//       fetch("/auth/registor/", {
//         body: JSON.stringify({ username : userNameField.value , email:emailNameField.value , password:passwordField.value}),
//         method: "POST",
//         headers: { "X-CSRFToken": csrftoken }
//       })
//   }
// },);
