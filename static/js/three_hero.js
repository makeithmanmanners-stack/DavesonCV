/* ==========================================================================
   THREE.JS 3D WEBGL CYBER MATRIX ENGINE
   Interactive 3D Wireframe Cyber Core & Constellation Field
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  const container = document.getElementById('three-hero-container');
  if (!container || typeof THREE === 'undefined') return;

  // Scene, Camera, Renderer
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(75, container.clientWidth / container.clientHeight, 0.1, 1000);
  camera.position.z = 5;

  const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
  renderer.setSize(container.clientWidth, container.clientHeight);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  container.appendChild(renderer.domElement);

  // 1. Create 3D Wireframe Icosahedron Core
  const geometry = new THREE.IcosahedronGeometry(2.2, 2);
  const material = new THREE.MeshBasicMaterial({
    color: 0x00D2FF,
    wireframe: true,
    transparent: true,
    opacity: 0.35
  });
  const coreMesh = new THREE.Mesh(geometry, material);
  scene.add(coreMesh);

  // 2. Create Outer Orbital Ring
  const ringGeo = new THREE.TorusGeometry(3.2, 0.02, 16, 100);
  const ringMat = new THREE.MeshBasicMaterial({
    color: 0x0066FF,
    wireframe: true,
    transparent: true,
    opacity: 0.5
  });
  const ringMesh = new THREE.Mesh(ringGeo, ringMat);
  ringMesh.rotation.x = Math.PI / 3;
  scene.add(ringMesh);

  // 3. Create Floating 3D Star / Particle Constellation Field
  const particleCount = 200;
  const particleGeo = new THREE.BufferGeometry();
  const positions = new Float32Array(particleCount * 3);

  for (let i = 0; i < particleCount * 3; i += 3) {
    positions[i] = (Math.random() - 0.5) * 12;
    positions[i + 1] = (Math.random() - 0.5) * 12;
    positions[i + 2] = (Math.random() - 0.5) * 12;
  }

  particleGeo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
  const particleMat = new THREE.PointsMaterial({
    color: 0x00D2FF,
    size: 0.06,
    transparent: true,
    opacity: 0.8
  });
  const particles = new THREE.Points(particleGeo, particleMat);
  scene.add(particles);

  // Mouse Interactivity
  let mouseX = 0;
  let mouseY = 0;
  let targetX = 0;
  let targetY = 0;

  window.addEventListener('mousemove', (e) => {
    mouseX = (e.clientX / window.innerWidth - 0.5) * 2;
    mouseY = (e.clientY / window.innerHeight - 0.5) * 2;
  });

  // Scroll Interactivity
  let scrollY = 0;
  window.addEventListener('scroll', () => {
    scrollY = window.scrollY;
  });

  // Animation Loop
  function animate() {
    requestAnimationFrame(animate);

    targetX += (mouseX - targetX) * 0.05;
    targetY += (mouseY - targetY) * 0.05;

    coreMesh.rotation.x += 0.003;
    coreMesh.rotation.y += 0.005;

    ringMesh.rotation.z += 0.004;

    particles.rotation.y += 0.001;

    scene.rotation.y = targetX * 0.4;
    scene.rotation.x = targetY * 0.4 + (scrollY * 0.0005);

    renderer.render(scene, camera);
  }

  animate();

  // Resize Handler
  window.addEventListener('resize', () => {
    const w = container.clientWidth;
    const h = container.clientHeight;
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
    renderer.setSize(w, h);
  });
});
