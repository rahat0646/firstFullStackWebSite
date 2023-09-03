var username = document.forms['signup']['username']
var phone = document.forms['signup']['phone']
var password = document.forms['signup']['password']

var username_error = document.getElementById('username_error')
var phone_error = document.getElementById('phone_error')
var password_error = document.getElementById('password_error')

username.addEventListener('textInput',usernameVerify)
phone.addEventListener('textInput',phoneVerify)
password.addEventListener('textInput',passwordVerify)

function validateSignup() {
    if (phone.value < 6000000 || phone.value < 6599999) {
        phone_error.style.display = "block";
        phone.focus();
        return false
    }
    
    if (username.value.length <= 2 ) {
        username_error.style.display = "block";
        username.focus();
        return false
    }

    if (password.value.length <= 6 ) {
        password_error.style.display = "block";
        password.focus();
        return false
    }
}

function phoneVerify() {
    if (phone.value < 60000000 || phone.value < 65999999) {
        phone_error.style.display = 'none'
        return true
    }
}

function usernameVerify() {
    if (username.value.length <= null) {
        username_error.style.display = 'none'
        return true
    }
}


function passwordVerify() {
    if (password.value.length <= 6) {
        password_error.style.display = 'none'
        return true
    }
}