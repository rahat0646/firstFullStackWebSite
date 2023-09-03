const scrollTop = document.getElementById('scrolltop')

// When the page is loaded, hide the scroll-to-top button
window.onload = () => {
 scrollTop.style.visibility = "hidden";
 scrollTop.style.opacity = 0;
}

// If the page is scrolled more than 200px,
// display the scroll-to-top button
// Otherwise keep the button hidden
window.onscroll = () => {
 if (window.scrollY > 200) {
 scrollTop.style.visibility = "visible";
 scrollTop.style.opacity = 1;
 } else {
 scrollTop.style.visibility = "hidden";
 scrollTop.style.opacity = 0;
 }
};

//Alerts show

document.addEventListener("DOMContentLoaded", function() {
    const alertsContainer = document.querySelector(".alerts");
    alertsContainer.style.opacity = "1";
    alertsContainer.style.visibility = "visible";
    setTimeout(function() {
      alertsContainer.style.opacity = "0";
      alertsContainer.style.visibility = "hidden";
    }, 5000);
});