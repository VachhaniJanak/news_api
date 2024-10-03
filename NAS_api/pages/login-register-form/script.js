const container = document.querySelector(".container"),
  pwShowHide = document.querySelectorAll(".showHidePw"),
  pwFields = document.querySelectorAll(".password"),
  signUp = document.querySelector(".signup-link"),
  login = document.querySelector(".login-link");

// js code to show/hide password and change icon
pwShowHide.forEach((eyeIcon) => {
  eyeIcon.addEventListener("click", () => {
    pwFields.forEach((pwField) => {
      if (pwField.type === "password") {
        pwField.type = "text";

        pwShowHide.forEach((icon) => {
          icon.classList.replace("uil-eye-slash", "uil-eye");
        });
      } else {
        pwField.type = "password";

        pwShowHide.forEach((icon) => {
          icon.classList.replace("uil-eye", "uil-eye-slash");
        });
      }
    });
  });
});

// js code to appear signup and login form
signUp.addEventListener("click", (e) => {
  e.preventDefault();
  container.classList.add("active");
});

login.addEventListener("click", (e) => {
  e.preventDefault();
  container.classList.remove("active");
});

// function to login
function login_function() {
  const email = document.getElementById("email").value;
  const password = document.getElementById("pwd").value;

  if (email.trim() !== "" && password.trim() !== "") {
    const response = fetch("http://127.0.0.1:8000/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        email: email,
        password: password,
      }),
    });
    response
      .then((response) => response.json())
      .then((data) => {
        document.cookie = `tokenid=${data.token_id}; path=/`;
        window.location.href =
          "http://127.0.0.1:5500/NAS_api/pages/card-slider/index.html";
      });
  }
}

// function to create user
function signup_function() {
  const username = document.getElementById("name").value;
  const email = document.getElementById("reg_email").value;
  const password = document.getElementById("reg_pwd").value;
  const confirm_password = document.getElementById("confirm_pwd").value;

  if (
    email.trim() !== "" &&
    password.trim() !== "" &&
    confirm_password.trim() !== "" &&
    username.trim() !== "" &&
    password.trim() === confirm_password.trim()
  ) {
    const response = fetch("http://127.0.0.1:8000/create", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username: username,
        email: email,
        password: password,
      }),
    });
    response
      .then((response) => response.json())
      .then((data) => {
        console.log(data.message);
      });
  }
}
