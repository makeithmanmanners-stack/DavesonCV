/* ==========================================================================
   TECHNICAL STACK INTERACTIVE ECOSYSTEM GRAPH
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  const canvas = document.getElementById('skills-canvas');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  let width = canvas.width = canvas.parentElement.clientWidth;
  let height = canvas.height = 440;

  window.addEventListener('resize', () => {
    if (!canvas.parentElement) return;
    width = canvas.width = canvas.parentElement.clientWidth;
    height = canvas.height = 440;
    initNodes();
  });

  // Nodes Definition
  let nodes = [];
  let connections = [];
  let hoverSkillName = null;

  const rawNodes = [
    { id: 'Python', label: 'PYTHON', category: 'Backend', x: 0.2, y: 0.25 },
    { id: 'Django', label: 'DJANGO', category: 'Backend', x: 0.4, y: 0.2 },
    { id: 'Backend', label: 'BACKEND', category: 'Core', x: 0.5, y: 0.45 },
    { id: 'MySQL', label: 'MYSQL', category: 'Database', x: 0.75, y: 0.25 },
    { id: 'Database', label: 'DATABASE', category: 'Core', x: 0.75, y: 0.65 },
    
    { id: 'JavaScript', label: 'JAVASCRIPT', category: 'Frontend', x: 0.2, y: 0.75 },
    { id: 'HTML5', label: 'HTML5', category: 'Frontend', x: 0.35, y: 0.82 },
    { id: 'CSS3', label: 'CSS3', category: 'Frontend', x: 0.52, y: 0.82 },
    { id: 'UI/UX', label: 'RESPONSIVE UI', category: 'Frontend', x: 0.35, y: 0.5 }
  ];

  const rawConnections = [
    { from: 'Python', to: 'Django' },
    { from: 'Django', to: 'Backend' },
    { from: 'Backend', to: 'MySQL' },
    { from: 'MySQL', to: 'Database' },
    { from: 'JavaScript', to: 'HTML5' },
    { from: 'HTML5', to: 'CSS3' },
    { from: 'CSS3', to: 'UI/UX' },
    { from: 'UI/UX', to: 'Backend' }
  ];

  function initNodes() {
    nodes = rawNodes.map(n => ({
      ...n,
      px: n.x * width,
      py: n.y * height,
      active: false
    }));

    connections = rawConnections.map(c => {
      const fromNode = nodes.find(n => n.id === c.from);
      const toNode = nodes.find(n => n.id === c.to);
      return {
        from: fromNode,
        to: toNode,
        active: false,
        pulseProgress: Math.random()
      };
    });
  }
  initNodes();

  // Listen to skill pills hover in document
  const skillPills = document.querySelectorAll('.skill-pill');
  const tooltip = document.getElementById('skill-tooltip');

  skillPills.forEach(pill => {
    pill.addEventListener('mouseenter', (e) => {
      const name = pill.getAttribute('data-skill-name');
      const specs = JSON.parse(pill.getAttribute('data-specs') || '[]');
      const connectedStr = pill.getAttribute('data-connected') || '';
      
      hoverSkillName = name;

      // Activate Nodes & Connections
      const targetIds = [name, ...connectedStr.split(',')].map(s => s.trim().toLowerCase());
      
      nodes.forEach(n => {
        n.active = targetIds.some(t => n.id.toLowerCase().includes(t) || t.includes(n.id.toLowerCase()));
      });

      connections.forEach(c => {
        c.active = c.from.active && c.to.active;
      });

      // Show Depth Tooltip
      if (tooltip && specs.length > 0) {
        document.getElementById('tooltip-title').textContent = name;
        document.getElementById('tooltip-subtitle').textContent = pill.getAttribute('data-subtitle') || 'Technical Spec';
        
        const listEl = document.getElementById('tooltip-list');
        listEl.innerHTML = specs.map(s => `<li>${s}</li>`).join('');

        tooltip.classList.add('visible');
      }
    });

    pill.addEventListener('mousemove', (e) => {
      if (tooltip) {
        tooltip.style.left = `${e.clientX + 15}px`;
        tooltip.style.top = `${e.clientY + 15}px`;
      }
    });

    pill.addEventListener('mouseleave', () => {
      hoverSkillName = null;
      nodes.forEach(n => n.active = false);
      connections.forEach(c => c.active = false);
      if (tooltip) tooltip.classList.remove('visible');
    });
  });

  // Render Loop
  function render() {
    ctx.clearRect(0, 0, width, height);

    // Draw Connections
    connections.forEach(c => {
      ctx.beginPath();
      ctx.moveTo(c.from.px, c.from.py);
      ctx.lineTo(c.to.px, c.to.py);
      
      if (c.active) {
        ctx.strokeStyle = '#00D2FF';
        ctx.lineWidth = 2.5;
        ctx.shadowColor = '#00D2FF';
        ctx.shadowBlur = 12;
      } else {
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.1)';
        ctx.lineWidth = 1;
        ctx.shadowBlur = 0;
      }
      ctx.stroke();
      ctx.shadowBlur = 0;

      // Pulse Particle
      c.pulseProgress = (c.pulseProgress + (c.active ? 0.02 : 0.005)) % 1;
      const px = c.from.px + (c.to.px - c.from.px) * c.pulseProgress;
      const py = c.from.py + (c.to.py - c.from.py) * c.pulseProgress;

      ctx.beginPath();
      ctx.arc(px, py, c.active ? 4 : 2, 0, Math.PI * 2);
      ctx.fillStyle = c.active ? '#00D2FF' : 'rgba(0, 102, 255, 0.6)';
      ctx.fill();
    });

    // Draw Nodes
    nodes.forEach(n => {
      ctx.beginPath();
      ctx.arc(n.px, n.py, n.active ? 10 : 6, 0, Math.PI * 2);
      ctx.fillStyle = n.active ? '#00D2FF' : '#0B1329';
      ctx.strokeStyle = n.active ? '#FFFFFF' : '#0066FF';
      ctx.lineWidth = n.active ? 3 : 1.5;
      if (n.active) {
        ctx.shadowColor = '#00D2FF';
        ctx.shadowBlur = 20;
      }
      ctx.fill();
      ctx.stroke();
      ctx.shadowBlur = 0;

      // Label
      ctx.font = n.active ? 'bold 11px Outfit' : '500 10px Outfit';
      ctx.fillStyle = n.active ? '#FFFFFF' : '#94A3B8';
      ctx.textAlign = 'center';
      ctx.fillText(n.label, n.px, n.py + 22);
    });

    requestAnimationFrame(render);
  }

  render();
});
