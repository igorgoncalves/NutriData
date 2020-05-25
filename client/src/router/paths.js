/**
 * Define all of your application routes here
 * for more information on routes, see the
 * official documentation https://router.vuejs.org/en/
 */
export default [
  {
    path: "/",
    name: "Home",
    view: "Home",
    type: "public",
  },
  {
    path: "/login",
    name: "Login",
    view: "Login",
    type: "public",
  },
  {
    path: "/macroindicadores",
    name: "Macroindicadores",
    view: "Macroindicador/List",
    type: "admin",
  },
  {
    path: "/macroindicadores/:idMacroindicador/update",
    name: "Macroindicadores/Update",
    view: "Macroindicador/Update",
    type: "admin",
  },
  {
    path: "/macroindicadores/novo",
    name: "Macroindicadores/Novo",
    view: "Macroindicador/Insert",
    type: "admin",
  },
  {
    path: "/localidades",
    name: "Localidades",
    view: "Localidade/List",
    type: "admin",
  },
  {
    path: "/categorias",
    name: "Categorias",
    view: "Categorias/List",
    type: "admin",
  },
  {
    path: "/categorias/novo",
    name: "Categorias/Novo",
    view: "Categorias/Insert",
    type: "admin",
  },
  {
    path: "/categorias/:idCategoria/update",
    name: "Categorias/Update",
    view: "Categorias/Update",
    type: "admin",
  },
  {
    path: "/localidade/:idLocalidade/macroindicadores",
    name: "LocalidadeMacroindicadores",
    view: "Localidade/Macroindicadores/List",
    type: "admin",
  },
  {
    path: "/visao",
    name: "Visao",
    view: "Visao/View",
    type: "admin",
  },
  {
    path:
      "/localidade/:codigoLocalidade/macroindicador/:idMacroindicador/admin",
    name: "MacroindicadorVisao",
    view: "Visao/View",
    type: "admin",
  },
  {
    path: "/localidade/:codigoLocalidade/macroindicador/:idMacroindicador",
    name: "PublicaMacroindicadorVisao",
    view: "Visao/View",
    type: "public",
  },
];
