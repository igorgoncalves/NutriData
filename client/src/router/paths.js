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
    path: '/dashboard',
    // Relative to /src/views
    view: 'Dashboard'
  },
  {
    path: '/user-profile',
    name: 'User Profile',
    view: 'UserProfile'
  },
  {
    path: '/table-list',
    name: 'Table List',
    view: 'TableList'
  },
  {
    path: '/typography',
    view: 'Typography'
  },
  {
    path: '/icons',
    view: 'Icons'
  },
  {
    path: '/maps',
    view: 'Maps'
  },
  {
    path: '/notifications',
    view: 'Notifications'
  },
  {
    path: '/upgrade',
    name: 'Upgrade to PRO',
    view: 'Upgrade'
  },
  {
    path: 'Localidade/:id/Macroindicadores',
    name: 'Macroindicadores',
    view: 'Macroindicador/List'
  },
  {
    path: 'Localidade/:id/Macroindicador/Novo',
    name: 'Macroindicador/Novo',
    view: 'Macroindicador/Insert'
  },
  {
    path: '/Localidades',
    name: 'Localidades',
    view: 'Localidade/List'
  },
]
