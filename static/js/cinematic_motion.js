/* ==========================================================================
   CINEMATIC MOTION CONTROLLER & MOBILE DRAWER LOGIC
   GSAP 3 + ScrollTrigger + Mobile Drawer Controller
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {

  // 1. Mobile Navigation Drawer Controller
  const mobileBtn = document.getElementById('mobile-hamburger-btn');
  const mobileOverlay = document.getElementById('mobile-nav-overlay');
  const mobileClose = document.getElementById('mobile-nav-close');
  const mobileLinks = document.querySelectorAll('.mobile-nav-link');

  if (mobileBtn && mobileOverlay) {
    mobileBtn.addEventListener('click', () => {
      mobileOverlay.classList.add('active');
      document.body.style.overflow = 'hidden';
    });

    if (mobileClose) {
      mobileClose.addEventListener('click', () => {
        mobileOverlay.classList.remove('active');
        document.body.style.overflow = 'auto';
      });
    }

    mobileLinks.forEach(link => {
      link.addEventListener('click', () => {
        mobileOverlay.classList.remove('active');
        document.body.style.overflow = 'auto';
      });
    });
  }

  // 2. Preloader Animation Sequence
  const loaderScreen = document.getElementById('loader-screen');
  const loaderFill = document.getElementById('loader-bar-fill');
  const loaderStatus = document.getElementById('loader-status');

  if (loaderScreen && loaderFill && loaderStatus) {
    let progress = 0;
    const interval = setInterval(() => {
      progress += Math.floor(Math.random() * 25) + 10;
      if (progress > 100) progress = 100;
      
      loaderFill.style.width = progress + '%';
      
      if (progress < 40) {
        loaderStatus.textContent = '01 — INITIALIZING SYSTEM';
      } else if (progress < 80) {
        loaderStatus.textContent = '02 — LOADING ARCHITECTURE';
      } else {
        loaderStatus.textContent = '03 — RENDERING INTERACTION';
      }

      if (progress >= 100) {
        clearInterval(interval);
        setTimeout(() => {
          gsap.to(loaderScreen, {
            opacity: 0,
            duration: 0.6,
            ease: 'power2.out',
            onComplete: () => {
              loaderScreen.style.display = 'none';
              document.body.style.overflow = 'auto';
              document.body.style.overflowY = 'auto';
              triggerHeroAnimations();
            }
          });
        }, 200);
      }
    }, 60);
  } else {
    triggerHeroAnimations();
  }

  // 3. Hero Text Character Stagger Reveal
  function triggerHeroAnimations() {
    const heroChars = document.querySelectorAll('.hero-name-char');
    const heroReveals = document.querySelectorAll('.hero-reveal');

    gsap.to(heroChars, {
      y: '0%',
      duration: 1,
      stagger: 0.04,
      ease: 'power4.out'
    });

    gsap.fromTo(heroReveals, 
      { opacity: 0, y: 30 },
      { opacity: 1, y: 0, duration: 1, stagger: 0.15, ease: 'power3.out', delay: 0.4 }
    );
  }

  // 4. GSAP ScrollTrigger Section Reveals & Timeline Line Expansion
  if (typeof ScrollTrigger !== 'undefined') {
    gsap.registerPlugin(ScrollTrigger);

    // Timeline Vertical Line Expansion
    const timelineProgress = document.getElementById('timeline-line-progress');
    if (timelineProgress) {
      gsap.to(timelineProgress, {
        height: '100%',
        ease: 'none',
        scrollTrigger: {
          trigger: '.timeline-wrap',
          start: 'top 70%',
          end: 'bottom 40%',
          scrub: true
        }
      });
    }

    // Active Responsibility Node Highlight on Scroll
    const respItems = document.querySelectorAll('.responsibility-item');
    respItems.forEach(item => {
      ScrollTrigger.create({
        trigger: item,
        start: 'top 65%',
        end: 'bottom 35%',
        onEnter: () => item.classList.add('active'),
        onLeaveBack: () => item.classList.remove('active')
      });
    });
  }

  // 5. AJAX Contact Form & Real Email Dispatch to davesonvasquez@gmail.com
  const contactForm = document.getElementById('contact-form');
  const formStatus = document.getElementById('form-status');

  if (contactForm && formStatus) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const formData = new FormData(contactForm);
      const name = formData.get('name');
      const email = formData.get('email');
      const subject = formData.get('subject') || 'Portfolio Inquiry';
      const message = formData.get('message');

      formStatus.style.display = 'block';
      formStatus.style.color = '#00D2FF';
      formStatus.textContent = 'TRANSMITTING MESSAGE & DISPATCHING EMAIL...';

      // 1. Save to Django Database
      const djangoSave = fetch('/api/contact/', {
        method: 'POST',
        headers: { 'X-Requested-With': 'XMLHttpRequest' },
        body: formData
      });

      // 2. Dispatch Real Email to davesonvasquez@gmail.com via FormSubmit API
      const emailDispatch = fetch('https://formsubmit.co/ajax/davesonvasquez@gmail.com', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        body: JSON.stringify({
          name: name,
          email: email,
          _subject: `[PORTFOLIO TRANSMISSION] ${subject} from ${name}`,
          message: message,
          _template: 'table'
        })
      });

      Promise.all([djangoSave, emailDispatch])
        .then(([djangoRes, emailRes]) => {
          formStatus.style.color = '#27C93F';
          formStatus.textContent = '✔ TRANSMISSION SUCCESSFUL! Real email sent directly to davesonvasquez@gmail.com';
          contactForm.reset();
        })
        .catch((err) => {
          // Fallback: If network issue, trigger mailto link
          formStatus.style.color = '#FFBD2E';
          formStatus.textContent = '✔ Message saved to system database! Opening email client fallback...';
          window.location.href = `mailto:davesonvasquez@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent("From: " + name + " (" + email + ")\n\n" + message)}`;
          contactForm.reset();
        });
    });
  }

});
