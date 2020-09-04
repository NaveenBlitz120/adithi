const navSlide=() => {
    const burger=document.querySelector('.burger');
    const nav=document.querySelector('.nav-links');
    const navLinks=document.querySelectorAll('.nav-links li');
    const contents=document.querySelector('.head');

    burger.addEventListener('click',()=>{

        //Toogle nav
        nav.classList.toggle('nav-active');

    //Animate nav link
    navLinks.forEach((link,index) => {
        if(link.style.animation) {
            link.style.animation='';
        }
        else{
            link.style.animation = `navLinkFade 0.5s ease-in forwards ${index / 7+0.2}s`;
        }
      });

      //Burger animation
      burger.classList.toggle('toggle');
      contents.classList.toggle('content-blur');


    });


}

navSlide();

$(document).ready(function(){
    $('.slider').slider();
  });

// Navbar - Footer

var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.querySelector(".nav-foot").style.bottom = "0";
    // document.querySelector(".nav-foot").style.bottom = "0";
  }
  else {
    document.querySelector(".nav-foot").style.bottom = "-50px";
  }
  prevScrollpos = currentScrollPos;
}
