document.addEventListener("DOMContentLoaded", () => {

    const sliders = document.querySelectorAll(".project-slider");

    sliders.forEach(slider => {
        const slides = slider.querySelectorAll(".slide");
        const nextBtn = slider.querySelector(".next");
        const prevBtn = slider.querySelector(".prev");

        let currentIndex = 0;

        function showSlide(index) {
            slides.forEach(slide => slide.classList.remove("active"));
            slides[index].classList.add("active");
        }

        nextBtn.addEventListener("click", () => {
            currentIndex = (currentIndex + 1) % slides.length;
            showSlide(currentIndex);
        });

        prevBtn.addEventListener("click", () => {
            currentIndex = (currentIndex - 1 + slides.length) % slides.length;
            showSlide(currentIndex);
        });

        // Optional: auto slide
        setInterval(() => {
            currentIndex = (currentIndex + 1) % slides.length;
            showSlide(currentIndex);
        }, 4000);

    });

});