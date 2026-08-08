/* ==========================================================================
   PARTICLE EXPLOSION BURST ENGINE
   Creates glowing cyan particle explosions on click
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  document.addEventListener('click', (e) => {
    // Spawn 16 particles at click coordinates
    const count = 16;
    for (let i = 0; i < count; i++) {
      createParticle(e.clientX, e.clientY);
    }
  });

  function createParticle(x, y) {
    const particle = document.createElement('div');
    particle.className = 'click-particle';
    document.body.appendChild(particle);

    const size = Math.random() * 6 + 4;
    particle.style.width = `${size}px`;
    particle.style.height = `${size}px`;
    particle.style.background = Math.random() > 0.5 ? '#00D2FF' : '#0066FF';
    particle.style.borderRadius = '50%';
    particle.style.position = 'fixed';
    particle.style.top = `${y}px`;
    particle.style.left = `${x}px`;
    particle.style.pointerEvents = 'none';
    particle.style.zIndex = '10001';
    particle.style.boxShadow = '0 0 10px #00D2FF';

    const destinationX = x + (Math.random() - 0.5) * 160;
    const destinationY = y + (Math.random() - 0.5) * 160;
    const rotation = Math.random() * 360;

    particle.animate([
      { transform: `translate(0, 0) scale(1) rotate(0deg)`, opacity: 1 },
      { transform: `translate(${destinationX - x}px, ${destinationY - y}px) scale(0) rotate(${rotation}deg)`, opacity: 0 }
    ], {
      duration: Math.random() * 600 + 400,
      easing: 'cubic-bezier(0.16, 1, 0.3, 1)',
      fill: 'forwards'
    }).onfinish = () => {
      particle.remove();
    };
  }
});
