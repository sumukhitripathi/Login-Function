const form = document.getElementById("loginForm");
const usernameInput = document.getElementById("username");
const passwordInput = document.getElementById("password");
const togglePasswordButton = document.getElementById("togglePassword");

function clearErrors() {
    document.querySelectorAll(".error").forEach(function (element) {
        element.classList.remove("show");
    });
}

function showError(id) {
    const element = document.getElementById(id);
    if (element) {
        element.classList.add("show");
    }
}

function validateForm() {
    clearErrors();

    let valid = true;

    if (usernameInput && usernameInput.value.trim() === "") {
        showError("err-username");
        valid = false;
    }

    if (passwordInput && passwordInput.value.trim() === "") {
        showError("err-password");
        valid = false;
    }

    return valid;
}

if (togglePasswordButton && passwordInput) {
    togglePasswordButton.addEventListener("click", function () {
        const showPassword = passwordInput.type === "password";
        passwordInput.type = showPassword ? "text" : "password";
        togglePasswordButton.textContent = showPassword ? "Hide" : "Show";
    });
}

if (form) {
    form.addEventListener("submit", function (event) {
        if (!validateForm()) {
            event.preventDefault();
        }
    });
}
