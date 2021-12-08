# Bookito
## A book library for all books you need 
- - - - 

# Author :
  ## Mazdak Pakaghideh 🔭👨‍💻

# Descreption 
  Bookito is a web application based on Django and Nuxt.js 🔥 this app is a **portabl** book library  📕 that you can manage and read all the books you have with 
  just simple information of that book (pdf , image , author , etc ..)
## Some notes:
  I had many school exams and I didn't work as much as needed in ui/ux part of project
  
- - - -
# Screenshots 🔥


- - - -

# Tools Used to develope this web-app🎯

![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![javascript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![postgresql](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![nood.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)
![yarn](https://img.shields.io/badge/Yarn-2C8EBB?style=for-the-badge&logo=yarn&logoColor=white)
![vue.js](https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D)
![nuxt.js](https://img.shields.io/badge/nuxt.js-00C58E?style=for-the-badge&logo=nuxtdotjs&logoColor=white)
![docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white)
![nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
![django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![nuxt.js](https://img.shields.io/badge/nuxt.js-00C58E?style=for-the-badge&logo=nuxtdotjs&logoColor=white)
![chrome](https://img.shields.io/badge/Google_chrome-4285F4?style=for-the-badge&logo=Google-chrome&logoColor=white)
![firefox](https://img.shields.io/badge/Firefox_Browser-FF7139?style=for-the-badge&logo=Firefox-Browser&logoColor=white)
![macos](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=apple&logoColor=white)
![appple](https://img.shields.io/badge/Apple-laptop-999999?style=for-the-badge&logo=apple&logoColor=white)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
![tailwind.css](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)

- - - -

# How to Setup and Deploy ⚡️

- - - -

Setup Variables in code :

### 1/3 Config axios url 

Markup :  `( bookitoFronted/nuxt.config.js ~ line 62 ~ 65)`

```javascript
    axios: {
        baseURL: 'http://YOUR-BACKEND-URL-HERE/api/v1/'
    },
```

### 2/3 Config images url  

Markup :  `(bookitoFronted/plugins/django.js ~ line 4)`

```javascript
    inject('Django', Vue.observable({ url: 'http://YOUR-BACKEND-URL-HERE:8000' }))
```

### 3/3 Config env variables

Markup :  `(Create ./env in root directory of project)`

```env
    POSTGRES_USER=your-database-user
    POSTGRES_PASSWORD=your-database-password
    POSTGRES_DB=your-database-name
    SECRET_KEY="DJANGO SECRET KEY"
    DEBUG=False
```
- - - -
# Setup

RUN with docker-compose

    $ docker-compose up --build
    OR
    $ docker composer up


    
# Contributions :

  ## No one is a complete human and so am i so please eel free to give your opinion and show issues for my improvement 🌈⚡️ this will make me happy
