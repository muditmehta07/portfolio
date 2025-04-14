document.querySelectorAll("section div").forEach(div => {
    div.innerHTML = Math.floor(Math.random() * 10);

    const typeOne = Math.floor(Math.random() * 10);
    if (typeOne <= 1) {
        div.classList.add('one-1');
    } else if (typeOne <= 3) {
        div.classList.add('one-2');
    }

    const typeTwo = Math.floor(Math.random() * 10);
    if (typeTwo <= 3) {
        div.classList.add('two-1');
    } else if (typeTwo <= 6) {
        div.classList.add('two-2');
    }

    const du = Math.floor(Math.random() * 10);
    if (du <= 1) {
        div.classList.add('three-1');
    } else if (du <= 6) {
        div.classList.add('three-2');
    }
});

document.addEventListener("mousemove", function(event) {
    const x = event.pageX;
    const y = event.pageY;

    document.querySelectorAll("section div").forEach(div => {
        const dx = div.offsetLeft + 50 - x;
        const dy = div.offsetTop + 50 - y;
        const dist = Math.sqrt(dx * dx + dy * dy);

        if (dist <= 100) {
            div.style.transform = "scale(2.5)"
        } else if (dist <= 130) {
            div.style.transform = "scale(2.2)"
        } else if (dist <= 140) {
            div.style.transform = "scale(1.8)"
        } else if (dist <= 150) {
            div.style.transform = "scale(1.5)"
        } else if (dist <= 180) {
            div.style.transform = "scale(1.2)"
        } else if (dist <= 200) {
            div.style.transform = "scale(1.1)"
        } else {
            div.style.transform = "scale(1)"
        }
    })
});

document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.querySelector('.hamburger-menu');
    const footer = document.querySelector('footer');

    hamburger.addEventListener('click', function() {
        footer.classList.toggle('active');
        const spans = hamburger.querySelectorAll('span');
        
        spans[0].style.transform = footer.classList.contains('active') 
            ? 'rotate(45deg) translate(6px, 6px)' 
            : 'none';
            
        spans[1].style.opacity = footer.classList.contains('active') 
            ? '0' 
            : '1';
            
        spans[2].style.transform = footer.classList.contains('active') 
            ? 'rotate(-45deg) translate(8px, -8px)' 
            : 'none';
    });
});