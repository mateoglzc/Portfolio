
const navSlide = () => {

    const burger = document.getElementsByClassName("burger").item(0);
    const nav = document.getElementsByClassName("nav").item(0);

    burger.addEventListener('click', () => {
        nav.classList.toggle('nav-active');
    })
    
}

navSlide();