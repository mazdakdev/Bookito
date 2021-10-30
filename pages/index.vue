<template>
<div class="home">

                
    <header>

            <nav class="navbar navbar-expand-lg navbar-dark mg  " style="margin-top:-20px">
      <a class="navbar-brand" href="#" >
        <h1>Book store</h1>
      </a>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarCollapse"
        aria-controls="navbarCollapse"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarCollapse">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <a class="nav-link" href="#">Home </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">About</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Contact us</a>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/auth">Login</router-link>
          </li>  <li class="nav-item">
            <router-link class="nav-link" to="/Reg">Register</router-link>
          </li>
       
          <div class="social soci-mobile">
            <a
              href="https://www.facebook.com/ewebdesigns/"
              target="blank"
              class="fa fa-facebook-square"
            ></a>
            <i class="fa fa-twitter-square" aria-hidden="true"></i>
            <i class="fa fa-github" aria-hidden="true"></i>
          </div>
        </ul>
      </div>
    </nav>

  
    <div class="container text-center">
  
      <div class="row">
        <div class="col-md-7 col-sm-12  text-white description fadeInLeft">
          <h6>Book store</h6>
          <h1>All the books you want</h1>
          <h4>
            Read all the books you want here Online !
          </h4>
          <br>
          <nuxt-link to="/" class="btn btn-light px-5 py-2 primary-btn btnh" style="border-radius:20px; color:black;">
          Shop
          </nuxt-link>
          
          <div class="btlist">
                <nuxt-link to="/auth" class="btn btn-light px-5 py-2 primary-btn btnh" style="border-radius:20px; color:black; ">
            Login
          </nuxt-link>
         
              <nuxt-link to="/Reg" class="btn btn-light px-5 py-2 primary-btn btnh" style="border-radius:20px; color:black;">
            Register
          </nuxt-link>
          </div>
        </div>
        <div class="col-md-5 col-sm-12 zoomInDown ">
          <img id="book" src="../assets/header-img.png" alt="Book" />
        </div>
      </div>
    </div>
  </header>
</div>



</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.home {

  background-image: linear-gradient(#de2772, #f8493f);
  background-size: '100% auto';



}

.btlist{
  visibility:hidden;
}

#book {
  width: 80%;
}

header .row .col-md-7 {
  padding: 22vmin 1vmin;
  padding-bottom: 35vmin;
}
header .container .col-md-7 {
  font-family: "Rubik", sans-serif;
}

header .container .col-md-7 h6 {
  padding: 1vmin;
  letter-spacing: 4px;
}

header .container .col-md-7 h1 {
  font-size: 8.5vmin;
  font-weight: bold;
  padding: 0.1em 0em;
}

header .container .col-md-7 p {
  padding: 1vmin 5vmin;
}
header a {
  font-family: var(--Sniglet-font);
  font-size: 0.9em;
  color: whitesmoke;
}
.sticky {
  position: fixed;
  top: 0;
  width: 100%;
  height: 340px;
  background: rgba(0, 0, 0, 0.815);
  z-index: 9999;
  transition: all 1.5s ease;
}

@import url("https://fonts.googleapis.com/css?family=Open+Sans&display=swap");

.navbar {
  padding-top: 80px;
}

.nav-link {
  font-family: Roboto, Helvetica Neue, sans-serif;
  font-size: 14px;
  font-weight: 600;
  color: #fff;
  min-width: 88px;
  line-height: 36px;
  padding: 0 16px;
  border-radius: 2px;
  text-align: center;
}

.nav-link:hover {
  background: rgba(255, 255, 255, 0.1);
  box-sizing: border-box;
  position: relative;
  color: #f4f4f4;
  box-sizing: border-box;
  position: relative;
  cursor: pointer;
  outline: 0;
  border: none;
}

.navbar-brand {
  font-family: Roboto, Helvetica Neue, sans-serif;
  font-size: 24px;
  font-weight: 500;
  color: #f4f4f4;
  padding: 0 16px;
}

.hero {
  height: 660px;
  background: linear-gradient(to bottom left, #77c4e3, #8176b5);
  background-size: cover;
  background-position: center;
}

.hero-heading {
  color: #fff;
  position: absolute;
  top: 220px;
  left: 0;
  right: 0;
  margin: auto;
  text-align: center;
  line-height: 1.3;
  font-weight: 300;
  font-family: "Roboto Slab", sans-serif;
  padding: 0 8px;
  max-width: 300px;
  width: 100%;
  z-index: 5;
}

.hero-sub-title {
  font-family: "Open Sans", sans-serif;
}

.hero-sub-title > a:hover {
  color: #f4f4f4;
}


/* 
=================================
--------- Media Query -----------
===============================*/

/*==============================
---------- Mobile View  --------
==============================*/
@media (min-width: 350px) and (max-width: 1024px) {
  .navbar {
    padding-top: 20px;
   
  }
 
 .btlist{
  visibility: visible;
  margin-top: 15px;
 }
 .btnh{
   
 }
  #book{
      width: 40%;
      margin-top: -100px;
  }
  .social {
    text-align: center;
  }
  .social {
    .fa {
      color: #807cb9 !important;
    }
    .fa-facebook-square {
      margin-left: 0 !important;
    }
  }
  .navbar-collapse {
    background-color: #fff;
    padding: 20px;
    z-index: 55;
    
  }


  nav {
    ul li > a {
      color: #807cb9 !important;
      &:hover {
        opacity: 0.8;
      }
    }
  }
}

/* Mobile -btn */
.navbar-dark .navbar-toggler-icon {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg viewBox='0 0 30 30' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath stroke='rgb(255, 255, 255)' stroke-width='3' stroke-linecap='round' stroke-miterlimit='10' d='M4 7h22M4 15h22M4 23h22'/%3E%3C/svg%3E");
}
.navbar-dark .navbar-toggler {
  border-color: transparent !important;
  &:focus {
    border-color: transparent !important;
  }
}

/* ========================
-------- Desktop ----------
=========================*/

@media (min-width: 1200px) {
  .navbar {
    width: 1140px;
    padding-left: 120px;
  }

  .text-white {
    font-family: "Open Sans", sans-serif;
  }
}

.social {
  .fa {
    font-size: 20px;
    min-width: 44px;
    line-height: 36px;
    color: #f4f4f4;
  }

  .fa-facebook-square {
    margin-left: 50px;
  }

  .fa:hover {
    cursor: pointer;
    color: #f4f4f4;
    opacity: 0.7;
    text-decoration: none;
  }
}
.fadeInLeft {
  -webkit-animation-name: fadeInLeft;
  animation-name: fadeInLeft;
  -webkit-animation-duration: 1s;
  animation-duration: 1s;
  -webkit-animation-fill-mode: both;
  animation-fill-mode: both;
  }
  @-webkit-keyframes fadeInLeft {
  0% {
  opacity: 0;
  -webkit-transform: translate3d(-100%, 0, 0);
  transform: translate3d(-100%, 0, 0);
  }
  100% {
  opacity: 1;
  -webkit-transform: none;
  transform: none;
  }
  }
  @keyframes fadeInLeft {
  0% {
  opacity: 0;
  -webkit-transform: translate3d(-100%, 0, 0);
  transform: translate3d(-100%, 0, 0);
  }
  100% {
  opacity: 1;
  -webkit-transform: none;
  transform: none;
  }
  } 

   .zoomInDown {
  -webkit-animation-name: zoomInDown;
  animation-name: zoomInDown;
  -webkit-animation-duration: 2s;
  animation-duration: 2s;
  -webkit-animation-fill-mode: both;
  animation-fill-mode: both;
  }
  @-webkit-keyframes zoomInDown {
  0% {
  opacity: 0;
  -webkit-transform: scale3d(.1, .1, .1) translate3d(0, -1000px, 0);
  transform: scale3d(.1, .1, .1) translate3d(0, -1000px, 0);
  -webkit-animation-timing-function: cubic-bezier(0.550, 0.055, 0.675, 0.190);
  animation-timing-function: cubic-bezier(0.550, 0.055, 0.675, 0.190);
  }
  60% {
  opacity: 1;
  -webkit-transform: scale3d(.475, .475, .475) translate3d(0, 60px, 0);
  transform: scale3d(.475, .475, .475) translate3d(0, 60px, 0);
  -webkit-animation-timing-function: cubic-bezier(0.175, 0.885, 0.320, 1);
  animation-timing-function: cubic-bezier(0.175, 0.885, 0.320, 1);
  }
  }
  @keyframes zoomInDown {
  0% {
  opacity: 0;
  -webkit-transform: scale3d(.1, .1, .1) translate3d(0, -1000px, 0);
  transform: scale3d(.1, .1, .1) translate3d(0, -1000px, 0);
  -webkit-animation-timing-function: cubic-bezier(0.550, 0.055, 0.675, 0.190);
  animation-timing-function: cubic-bezier(0.550, 0.055, 0.675, 0.190);
  }
  60% {
  opacity: 1;
  -webkit-transform: scale3d(.475, .475, .475) translate3d(0, 60px, 0);
  transform: scale3d(.475, .475, .475) translate3d(0, 60px, 0);
  -webkit-animation-timing-function: cubic-bezier(0.175, 0.885, 0.320, 1);
  animation-timing-function: cubic-bezier(0.175, 0.885, 0.320, 1);
  }
  } 
  @media only screen and (max-width: 768px) {
    .home {
  position: absolute;
  background-image: linear-gradient(#de2772, #f8493f);
  width: 100%;
  height: 100vh;
  top: 0;
  left: 0;
}
  header .navbar-brand {
    padding-left: 1rem;
  }
  .section-1 .row .col-md-6 .panel {
    position: initial;
    width: initial;
    height: initial;
  }
  .section-2 .cover {
    background-position: -25vmin -10vmin;
  }
  .numbers .rect {
    width: 10rem;
    height: 8rem;
  }
  .numbers .rect h1 {
    font-size: 2rem;
  }

  .section-3 {
    height: inherit;
    padding: 10vmin !important;
  }
  .section-3 .row h1 {
    padding: 6vmin 4vmin;
  }
  .section-3 .platform .col-md-6 {
    text-align: center !important;
  }
  .section-3 .desktop i {
    font-size: 8vmin;
  }
  .section-4 .carousel-item {
    padding-left: 0.6rem;
  }
  footer .row .col-md-2 {
    margin-top: 8vmin;
  }
}

/* screen size 375px */

@media only screen and (max-width: 375px) {
  .section-4 .card {
    width: 18em;
  }
}

@media only screen and (max-width: 320px) {
  .section-4 .carousel-inner {
    margin-left: -4vmin;
  }
}
</style>
