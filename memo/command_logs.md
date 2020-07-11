### create server file

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
  - ref my other repositor, portfolio, vue-go-gae
