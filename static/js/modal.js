/* ==========================================================================
   INTERACTIVE PROJECT INSPECTOR MODAL & LIVE QUERY SIMULATOR
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  const modal = document.getElementById('project-modal');
  const closeBtn = document.getElementById('modal-close-btn');
  const modalTitle = document.getElementById('modal-title');
  const modalTech = document.getElementById('modal-tech');
  const modalDesc = document.getElementById('modal-desc');
  const modalImg = document.getElementById('modal-img');
  const modalLink = document.getElementById('modal-link');
  const simOutput = document.getElementById('modal-sim-output');
  const runSimBtn = document.getElementById('run-sim-btn');

  if (!modal) return;

  const projectDetails = {
    "PROJECT 01": {
      title: "MHCS ALUMNI PLATFORM",
      tech: "Django / MySQL / Relational Database",
      desc: "Full-stack institutional alumni tracking system with automated data verification, relational database schema optimization, and executive reporting dashboards.",
      img: "/static/images/project_mhcs.png",
      url: "https://mhcs-alumni.com/",
      simData: [
        { id: "ALU-9021", name: "Daveson Carl Vasquez", year: "2026", course: "BS IS", status: "VERIFIED" },
        { id: "ALU-9022", name: "Elena Rostova", year: "2025", course: "BS CS", status: "VERIFIED" },
        { id: "ALU-9023", name: "Marcus Brody", year: "2024", course: "BS IT", status: "PENDING" }
      ]
    },
    "PROJECT 02": {
      title: "WEB-BASED MANAGEMENT SYSTEM",
      tech: "PHP / Laravel / JavaScript / Role-Based ACL",
      desc: "Responsive business process management suite featuring automated workflow routing, role-based authorization levels, audit logging, and query performance refactoring.",
      img: "/static/images/project_mgmt.png",
      url: "https://violet-gnat-135298.hostingersite.com/",
      simData: [
        { id: "TASK-401", title: "Inventory Audit Sync", role: "Manager", latency: "14ms", status: "EXECUTED" },
        { id: "TASK-402", title: "User Role Permission Gate", role: "Admin", latency: "8ms", status: "APPROVED" }
      ]
    },
    "PROJECT 03": {
      title: "DEVELOPER PORTFOLIO",
      tech: "HTML5 / CSS3 / JavaScript / GSAP Motion",
      desc: "High-performance digital experience highlighting technical systems analysis, full-stack web applications, and live systems architecture.",
      img: "/static/images/project_portfolio.png",
      url: "http://daveson-vasquez-portfolio.rf.gd",
      simData: [
        { id: "SYS-01", module: "3D WebGL Canvas", fps: "60 FPS", status: "ACTIVE" },
        { id: "SYS-02", module: "Django API Endpoint", ping: "12ms", status: "ACTIVE" }
      ]
    }
  };

  let activeSimData = null;

  document.querySelectorAll('.inspect-project-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const code = btn.getAttribute('data-project-code');
      const data = projectDetails[code];
      if (data) {
        activeSimData = data.simData;
        if (modalTitle) modalTitle.textContent = data.title;
        if (modalTech) modalTech.textContent = data.tech;
        if (modalDesc) modalDesc.textContent = data.desc;
        if (modalImg) modalImg.src = data.img;
        if (modalLink) modalLink.href = data.url;
        if (simOutput) simOutput.innerHTML = '<span style="color: var(--text-muted);">Click "RUN LIVE QUERY SIMULATOR" to simulate backend database response.</span>';

        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
      }
    });
  });

  if (runSimBtn) {
    runSimBtn.addEventListener('click', () => {
      if (!activeSimData || !simOutput) return;

      simOutput.innerHTML = '<span style="color: var(--color-cyan-glow);">Executing MySQL Indexing Query...</span>';
      setTimeout(() => {
        let html = '<div style="display:flex; flex-direction:column; gap:0.5rem;">';
        activeSimData.forEach(row => {
          html += `<div style="padding:0.5rem 0.75rem; background:rgba(0,210,255,0.08); border:1px solid rgba(0,210,255,0.2); border-radius:6px; font-size:0.75rem; display:flex; justify-content:space-between;">`;
          for (const [k, v] of Object.entries(row)) {
            html += `<span><strong>${k.toUpperCase()}:</strong> ${v}</span>`;
          }
          html += `</div>`;
        });
        html += '</div>';
        simOutput.innerHTML = html;
      }, 400);
    });
  }

  if (closeBtn) {
    closeBtn.addEventListener('click', () => {
      modal.classList.remove('active');
      document.body.style.overflow = 'auto';
    });
  }

  modal.addEventListener('click', (e) => {
    if (e.target === modal) {
      modal.classList.remove('active');
      document.body.style.overflow = 'auto';
    }
  });
});
