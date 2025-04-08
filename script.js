// === Utility: Page Detection ===
function getPageName() {
    const path = window.location.pathname;
    return path.substring(path.lastIndexOf('/') + 1).toLowerCase();
}

// === Quantum Particle Background ===
function initParticleBackground() {
    const canvas = document.getElementById('quantum-bg');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const particles = [];
    const count = 100;

    for (let i = 0; i < count; i++) {
        particles.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            vx: (Math.random() - 0.5) * 0.5,
            vy: (Math.random() - 0.5) * 0.5,
            size: Math.random() * 2 + 1
        });
    }

    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#87cefa';

        particles.forEach(p => {
            p.x += p.vx;
            p.y += p.vy;

            if (p.x < 0 || p.x > canvas.width) p.vx *= -1;
            if (p.y < 0 || p.y > canvas.height) p.vy *= -1;

            ctx.beginPath();
            ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
            ctx.fill();
        });

        requestAnimationFrame(animate);
    }

    animate();

    window.addEventListener('resize', () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    });
}

// === Tooltip Hover for Qubits ===
function initQubitTooltips() {
    const qubits = document.querySelectorAll('.qubit');
    const tooltip = document.getElementById('tooltip');
    if (!qubits.length || !tooltip) return;

    qubits.forEach(q => {
        q.addEventListener('mouseover', () => {
            tooltip.textContent = q.dataset.info;
            tooltip.style.opacity = 1;
        });

        q.addEventListener('mousemove', e => {
            tooltip.style.left = e.pageX + 15 + 'px';
            tooltip.style.top = e.pageY + 15 + 'px';
        });

        q.addEventListener('mouseleave', () => {
            tooltip.style.opacity = 0;
        });
    });
}

// Function to copy the pip install command
function copyCommand() {
    const commandInput = document.getElementById('pipCommand');

    // Select the text field
    commandInput.select();
    commandInput.setSelectionRange(0, 99999); // For mobile devices

    // Try to copy the text
    try {
        document.execCommand('copy');
        alert('Command copied to clipboard: ' + commandInput.value); // Confirmation
    } catch (err) {
        alert('Failed to copy command');
    }
}


// === Methodology Page: Flowchart Animation ===
function initMethodologyFlowchart() {
    const flowSteps = document.querySelectorAll('.flow-step');
    if (!flowSteps.length) return;

    let delay = 0;
    flowSteps.forEach(step => {
        step.style.opacity = 0;
        setTimeout(() => {
            step.style.transition = 'opacity 0.8s ease-in';
            step.style.opacity = 1;
        }, delay);
        delay += 600;
    });
}

// === Initialization Based on Page ===
document.addEventListener('DOMContentLoaded', () => {
    const page = getPageName();

    // Global features
    initParticleBackground();
    initQubitTooltips();

    // Page-specific
    if (page === 'methodology.html') {
        initMethodologyFlowchart();
    }

    // Future feature hooks
    if (page === 'installation.html') {
        // initInstallationSteps(); // Add this when ready
    }

    if (page === 'demos.html') {
        // initNotebookViewer(); // Coming soon
    }
});

// Setting up the canvas for particle background
const canvas = document.getElementById("quantum-bg");
const ctx = canvas.getContext("2d");

// Resize the canvas to full screen
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const particles = [];
const lines = [];
const numParticles = 100; // Number of particles
const maxDistance = 150; // Maximum distance for line connections
const lineInterval = 1000; // Time in milliseconds to draw new line

// Particle class
class Particle {
    constructor(x, y) {
        this.x = x;
        this.y = y;
        this.size = Math.random() * 2 + 1;
        this.speedX = Math.random() * 0.5 - 0.25;
        this.speedY = Math.random() * 0.5 - 0.25;
    }

    update() {
        this.x += this.speedX;
        this.y += this.speedY;

        // Bounce off walls
        if (this.x > canvas.width || this.x < 0) this.speedX *= -1;
        if (this.y > canvas.height || this.y < 0) this.speedY *= -1;
    }

    draw() {
        ctx.fillStyle = "rgba(135, 206, 250, 1)";
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fill();
    }
}

// Function to generate random lines between particles
function drawRandomLine() {
    const particle1 = particles[Math.floor(Math.random() * particles.length)];
    const particle2 = particles[Math.floor(Math.random() * particles.length)];

    const distance = Math.hypot(particle1.x - particle2.x, particle1.y - particle2.y);

    if (distance < maxDistance) {
        lines.push({ startX: particle1.x, startY: particle1.y, endX: particle2.x, endY: particle2.y });
    }
}

// Function to draw lines with glowing effect
function drawLines() {
    ctx.strokeStyle = "rgba(255, 255, 255, 0.7)";
    ctx.lineWidth = 0.7;

    lines.forEach(line => {
        ctx.beginPath();
        ctx.moveTo(line.startX, line.startY);
        ctx.lineTo(line.endX, line.endY);
        ctx.stroke();
    });
}

// Create particles
function createParticles() {
    for (let i = 0; i < numParticles; i++) {
        let x = Math.random() * canvas.width;
        let y = Math.random() * canvas.height;
        particles.push(new Particle(x, y));
    }
}

// Update particles and draw background
function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Update and draw each particle
    particles.forEach(particle => {
        particle.update();
        particle.draw();
    });

    // Draw the lines
    drawLines();

    requestAnimationFrame(animate);
}

// Start animation
createParticles();
animate();

// Set interval to draw random lines between particles
setInterval(drawRandomLine, lineInterval);
