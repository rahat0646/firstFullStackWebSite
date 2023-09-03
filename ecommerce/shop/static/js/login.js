var username = document.forms['login']['username']
var password = document.forms['login']['password']

var username_error = document.getElementById('username_error')
var password_error = document.getElementById('password_error')

username.addEventListener('textInput',usernameVerify)
password.addEventListener('textInput',passwordVerify)

function validated() {
    if (username.value.length <= 2 ) {
        username_error.style.display = "block";
        return false
    }

    if (password.value.length <= 6 ) {
        password_error.style.display = "block";
        return false
    }
}

function usernameVerify() {
    if (username.value.length <= null) {
        username_error.style.display = 'none'
        return true
    }
}

function passwordVerify() {
    if (password.value.length <= null) {
        password_error.style.display = 'none'
        return true
    }
}