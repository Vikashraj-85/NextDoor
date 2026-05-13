

        // Counter animation
        function animateCounters() {
            const counters = document.querySelectorAll('.counter');
            counters.forEach(counter => {
                const target = +counter.getAttribute('data-target');
                const increment = target / 100;
                let current = 0;

                const updateCounter = () => {
                    if (current < target) {
                        current += increment;
                        counter.textContent = Math.ceil(current);
                        setTimeout(updateCounter, 20);
                    } else {
                        counter.textContent = target;
                    }
                };

                if (window.scrollY > 2000) {
                    updateCounter();
                }
            });
        }

        window.addEventListener('scroll', () => {
            if (window.scrollY > 2000) {
                animateCounters();
            }
        });


        // Service card hover effects
        document.querySelectorAll('.service-card').forEach(card => {
            card.addEventListener('mouseenter', function() {
                this.style.borderColor = 'rgba(102, 126, 234, 0.3)';
            });
            
            card.addEventListener('mouseleave', function() {
                this.style.borderColor = 'rgba(102, 126, 234, 0.1)';
            });
        });

        // CTA button pulse animation
        setInterval(() => {
            const cta = document.querySelector('.cta-section .service-cta');
            cta.style.transform = 'scale(1.05)';
            setTimeout(() => {
                cta.style.transform = 'scale(1)';
            }, 300);
        }, 3000);
    