/**
 * Define all of your application routes here
 * for more information on routes, see the
 * official documentation https://router.vuejs.org/en/
 */
export default [
  {
    path: '/',
    view: 'Home'
  },
  {
    path: '/login',
    name: 'Login',
    view: 'Login'
  },  
  {
    path: '/macroindicadores',
    name: 'Macroindicadores',
    view: 'Macroindicador/List'
  },
  {
    path: '/macroindicadores/novo',
    name: 'Macroindicadores/Novo',
    view: 'Macroindicador/Insert'
  },
  {
    path: '/localidades',
    name: 'Localidades',
    view: 'Localidade/List'
  },
  {
    path: '/localidade/:idLocalidade/macroindicadores',
    name: 'LocalidadeMacroindicadores',
    view: 'Localidade/Macroindicadores/List'
  },
  {
    path: '/visao',
    name: 'Visao',
    view: 'Visao/Insert'
  },
  {
    path: '/macroindicador/:idMacroindicador/visao',
    name: 'MacroindicadorVisao',
    view: 'Visao/Insert'
  }
];
