const aboutUs = document.querySelector(".about-us-section");
const nav = docuent.querySelector(".nav") 

window.addEventListener("scroll", fixNav);

function fixNav() {
    if(window.scrollY > aboutUs.offsetHeight + 150) {
        nav.classList.add("active");
        console.log("dark");
    } else {
        nav.classList.remove("active");
    }
}

