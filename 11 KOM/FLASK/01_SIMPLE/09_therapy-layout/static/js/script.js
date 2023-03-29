document.addEventListener('DOMContentLoaded', () => {

    document.querySelector('.menu-toggle').addEventListener('click', function() {
        document.querySelector('.menu-nav').classList.toggle('clicked');
    })
    document.querySelector('.icon').addEventListener('click', function() {
        document.querySelector('.icon').classList.toggle('clicked');
    })
})