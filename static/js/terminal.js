/* ==========================================================================
   INTERACTIVE COMMAND LINE TERMINAL SHOWCASE ("DAVESON ARCHITECTURE CLI")
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  const terminalInput = document.getElementById('terminal-input');
  const terminalBody = document.getElementById('terminal-body');
  if (!terminalInput || !terminalBody) return;

  const commands = {
    help: `Available Commands:
  - <span style="color:#00D2FF">whoami</span>       : Executive profile overview
  - <span style="color:#00D2FF">skills</span>       : Primary backend, database & frontend stack
  - <span style="color:#00D2FF">projects</span>     : Live deployed systems showcase
  - <span style="color:#00D2FF">exp</span>          : Internship & workflow modeling experience
  - <span style="color:#00D2FF">contact</span>      : Direct communication details
  - <span style="color:#00D2FF">clear</span>        : Clear output buffer`,

    whoami: `<span style="color:#00D2FF">[IDENTITY CONFIRMED]</span>
  Name: DAVESON CARL A. VASQUEZ
  Role: FULL-STACK WEB DEVELOPER &amp; SYSTEMS ANALYST
  Education: BS Information Systems, Northwest Samar State University (Graduated May 2026)
  Location: Las Piñas City, Philippines
  Summary: Engineering scalable digital systems through full-stack development, systems analysis, database architecture, and intelligent business process integration.`,

    skills: `<span style="color:#00D2FF">[STACK ECOSYSTEM LOADED]</span>
  Backend         : Python (Django), PHP (Laravel), MySQL Database, Query Optimization
  Frontend        : JavaScript (ES6+), HTML5, CSS3, Responsive UI/UX Design
  Systems Analysis: Business Process Analysis, Requirements Gathering, Workflow Optimization
  Tools & Support : Git, GitHub, VS Code, Enterprise IT Support, Hardware &amp; Software Troubleshooting`,

    projects: `<span style="color:#00D2FF">[LIVE PRODUCTION SYSTEMS]</span>
  01. MHCS ALUMNI PLATFORM (Django / MySQL) -> https://mhcs-alumni.com/
  02. WEB-BASED MANAGEMENT SYSTEM (PHP / Laravel / JS) -> https://violet-gnat-135298.hostingersite.com/
  03. DEVELOPER PORTFOLIO (HTML5 / CSS3 / JS) -> http://daveson-vasquez-portfolio.rf.gd`,

    exp: `<span style="color:#00D2FF">[EXPERIENCE VERIFIED]</span>
  Role: WEB DEVELOPER INTERN @ University of Perpetual Help System DALTA (UPHSD)
  Duration: JAN 2026 — MAY 2026
  Highlights:
    • Engineered & scaled web apps using Django, PHP & MySQL
    • Modeled operational workflows and business requirements
    • Refactored database indexes to reduce query latency
    • Provided enterprise IT support across internal departments`,

    contact: `<span style="color:#00D2FF">[COMMUNICATION CHANNELS]</span>
  Email    : davesonvasquez@gmail.com
  Phone    : +63 965 586 6772
  Portfolio: daveson-vasquez-portfolio.rf.gd
  Location : Las Piñas City, Philippines`
  };

  function appendLine(inputCmd, outputText) {
    const line = document.createElement('div');
    line.className = 'terminal-line';
    line.innerHTML = `<div class="terminal-cmd-prompt"><span class="prompt-user">visitor@daveson-vasquez</span>:<span class="prompt-path">~/system</span>$ ${inputCmd}</div>
                      <div class="terminal-cmd-output">${outputText}</div>`;
    terminalBody.appendChild(line);
    terminalBody.scrollTop = terminalBody.scrollHeight;
  }

  terminalInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
      const val = terminalInput.value.trim().toLowerCase();
      terminalInput.value = '';

      if (val === 'clear') {
        terminalBody.innerHTML = '';
        return;
      }

      if (commands[val]) {
        appendLine(val, commands[val]);
      } else if (val === '') {
        // Empty
      } else {
        appendLine(val, `<span style="color:#FF4D4D">Command not recognized: '${val}'. Type <span style="color:#00D2FF">help</span> for available commands.</span>`);
      }
    }
  });

  // Quick Command Pills
  document.querySelectorAll('.term-quick-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const cmd = btn.getAttribute('data-cmd');
      if (cmd === 'clear') {
        terminalBody.innerHTML = '';
      } else if (commands[cmd]) {
        appendLine(cmd, commands[cmd]);
      }
    });
  });
});
