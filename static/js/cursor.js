/* ==========================================================================
   MAGNETIC CUSTOM CURSOR CONTROLLER
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  const cursor = document.getElementById('custom-cursor');
  const follower = document.getElementById('custom-cursor-follower');
  const cursorText = document.getElementById('custom-cursor-text');

  if (!cursor || !follower) return;

  let mouseX = 0, mouseY = 0;
  let followerX = 0, followerY = 0;

  // Track Mouse Position
  window.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;

    cursor.style.transform = `translate(${mouseX}px, ${mouseY}px) translate(-50%, -50%)`;
  });

  // Smooth Follower Lerp
  function animateFollower() {
    followerX += (mouseX - followerX) * 0.15;
    followerY += (mouseY - followerY) * 0.15;

    follower.style.transform = `translate(${followerX}px, ${followerY}px) translate(-50%, -50%)`;
    requestAnimationFrame(animateFollower);
  }
  animateFollower();

  // Hover Interactions for Interactive Elements
  const hoverElements = document.querySelectorAll('[data-cursor]');

  hoverElements.forEach((el) => {
    el.addEventListener('mouseenter', () => {
      const mode = el.getAttribute('data-cursor');
      cursor.classList.add('hovering');

      if (mode === 'view') {
        cursorText.textContent = 'VIEW PROJECT';
      } else if (mode === 'explore') {
        cursorText.textContent = 'EXPLORE';
      } else if (mode === 'open') {
        cursorText.textContent = 'OPEN →';
      } else {
        cursorText.textContent = 'INTERACT';
      }
    });

    el.addEventListener('mouseleave', () => {
      cursor.classList.remove('hovering');
      cursorText.textContent = '';
    });
  });

  // Magnetic Button Effect
  const magneticButtons = document.querySelectorAll('.magnetic-btn');

  magneticButtons.forEach((btn) => {
    btn.addEventListener('mousemove', (e) => {
      const rect = btn.getBoundingClientRect();
      const btnX = e.clientX - rect.left - rect.width / 2;
      const btnY = e.clientY - rect.top - rect.height / 2;

      btn.style.transform = `translate(${btnX * 0.2}px, ${btnY * 0.2}px)`;
    });

    btn.addEventListener('mouseleave', () => {
      btn.style.transform = `translate(0px, 0px)`;
    });
  });
});
