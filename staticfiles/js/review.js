const stars = document.querySelectorAll('.star');
const ratingValue = document.getElementById('rating-value');

stars.forEach((star) => {

    star.addEventListener('click', () => {

        let value = star.getAttribute('data-value');

        ratingValue.value = value;

        // Remove active class
        stars.forEach(s => s.classList.remove('active'));

        // Add active stars
        for(let i = 0; i < value; i++){

            stars[i].classList.add('active');
        }
            });
});