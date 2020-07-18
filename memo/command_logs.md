### create server files

- mkdir server
- cd server
- pipenv shell
- pipenv install flask flask_cors
- create main.py
  - ref https://github.com/testdrivenio/flask-vue-crud

### create client files

- yarn create nuxt-app client
  - choose all of the default settings
- cd client
- yarn dev
  - (for production) yarn build, yarn start
- yarn add @nuxtjs/axios
- edit nuxt.config.js
  - ref https://axios.nuxtjs.org/setup.html#install
- implement Read of CRUD
  - ref my repositories, portfolio, vue-go-gae

### set up a db

- create a db with TablePlus
  - with user=postgres <- postgres に user 登録するやり方よく分からんが?
- pipenv install psycopg2-binary
  - ref my repository, line-bot-lunch2
- create a python script for creating a db

### misc

- create pages
- install bootstrap-vue
  - yarn add bootstrap-vue
  - edit nuxt.cinfig.js, modules: ['bootstrap-vue/nuxt']
  - vuetify didn't work
- create an outline of a search page
- createa each-user pages
