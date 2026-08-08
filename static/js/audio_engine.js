/* ==========================================================================
   SYNTHESIZED FUTURISTIC WEB AUDIO ENGINE
   Pure Web Audio API (No external asset dependencies)
   ========================================================================== */

class AudioEngine {
  constructor() {
    this.ctx = null;
    this.muted = true; // Muted by default for UX
    this.init();
  }

  init() {
    const toggleBtn = document.getElementById('sound-toggle');
    if (toggleBtn) {
      toggleBtn.addEventListener('click', () => {
        if (!this.ctx) {
          const AudioCtx = window.AudioContext || window.webkitAudioContext;
          if (AudioCtx) this.ctx = new AudioCtx();
        }
        this.muted = !this.muted;
        toggleBtn.innerHTML = this.muted 
          ? '<i data-lucide="volume-x" style="width:12px;height:12px;"></i> SOUND [OFF]' 
          : '<i data-lucide="volume-2" style="width:12px;height:12px;"></i> SOUND [ON]';
        
        if (typeof lucide !== 'undefined') lucide.createIcons();
        if (!this.muted) this.playChime();
      });
    }

    // Attach subtle sound triggers to interactive elements
    document.querySelectorAll('[data-cursor], .magnetic-btn, .skill-pill').forEach(el => {
      el.addEventListener('mouseenter', () => this.playHover());
      el.addEventListener('click', () => this.playClick());
    });
  }

  playHover() {
    if (this.muted || !this.ctx) return;
    try {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(800, this.ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(1400, this.ctx.currentTime + 0.05);

      gain.gain.setValueAtTime(0.015, this.ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.0001, this.ctx.currentTime + 0.05);

      osc.connect(gain);
      gain.connect(this.ctx.destination);

      osc.start();
      osc.stop(this.ctx.currentTime + 0.05);
    } catch (e) {}
  }

  playClick() {
    if (this.muted || !this.ctx) return;
    try {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(400, this.ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(120, this.ctx.currentTime + 0.08);

      gain.gain.setValueAtTime(0.04, this.ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.0001, this.ctx.currentTime + 0.08);

      osc.connect(gain);
      gain.connect(this.ctx.destination);

      osc.start();
      osc.stop(this.ctx.currentTime + 0.08);
    } catch (e) {}
  }

  playChime() {
    if (this.muted || !this.ctx) return;
    try {
      const freqs = [523.25, 659.25, 783.99, 1046.50];
      freqs.forEach((f, idx) => {
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sine';
        osc.frequency.value = f;

        gain.gain.setValueAtTime(0.02, this.ctx.currentTime + idx * 0.06);
        gain.gain.exponentialRampToValueAtTime(0.0001, this.ctx.currentTime + idx * 0.06 + 0.2);

        osc.connect(gain);
        gain.connect(this.ctx.destination);

        osc.start(this.ctx.currentTime + idx * 0.06);
        osc.stop(this.ctx.currentTime + idx * 0.06 + 0.2);
      });
    } catch (e) {}
  }
}

document.addEventListener('DOMContentLoaded', () => {
  window.audioEngine = new AudioEngine();
});
