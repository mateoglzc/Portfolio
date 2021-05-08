
const navSlide = () => {

    const burger = document.getElementsByClassName("burger").item(0);
    const nav = document.getElementsByClassName("nav").item(0);

    console.log(burger);

    burger.addEventListener('click', () => {
        nav.classList.toggle('nav-active');
        console.log("matt");
    })
    
}

navSlide();