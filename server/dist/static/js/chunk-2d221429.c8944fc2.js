(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d221429"],{ca1f:function(t,e,r){"use strict";r.r(e);var a=function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("v-container",{attrs:{"fill-height":"",fluid:"","grid-list-xl":""}},[r("v-layout",{attrs:{wrap:""}},[r("v-flex",{attrs:{md12:"",sm12:"",lg12:""}},[r("v-card",[r("v-card-title",[r("v-flex",{attrs:{md12:"",sm12:"",lg10:""}},[r("h2",[t._v("Lista de macroindicadores")])]),r("v-layout",{attrs:{"align-end":""}},[r("v-btn",{staticClass:"success",on:{click:function(e){return t.createNew()}}},[t._v("+ Adicionar")])],1),r("v-spacer"),r("v-flex",{attrs:{md12:"",sm12:"",lg4:"","offset-lg8":""}},[r("v-text-field",{attrs:{"append-icon":"mdi-search",label:"Buscar (Ex.: Aquisição)","single-line":"","hide-details":""},model:{value:t.search,callback:function(e){t.search=e},expression:"search"}})],1)],1),r("v-data-table",{staticClass:"elevation-1",attrs:{headers:t.headers,items:t.categorias,search:t.search},scopedSlots:t._u([{key:"items",fn:function(e){return[r("td"),r("td",[t._v(t._s(e.item.nome))]),r("td",{staticClass:"text-xs-left"},[t._v(t._s(e.item.descricao))]),r("td",{staticClass:"justify-center px-0"},[r("v-tooltip",{attrs:{top:""}},[[r("v-icon",{attrs:{slot:"activator"},on:{click:function(r){return t.editItem(e.item.id)}},slot:"activator"},[t._v("\n                    mdi-settings\n                  ")])],r("span",[t._v("Alterar")])],2),r("v-tooltip",{attrs:{top:""}},[[r("v-icon",{attrs:{slot:"activator"},on:{click:function(r){return t.deleteItem(e.item)}},slot:"activator"},[t._v("\n                    mdi-delete\n                  ")])],r("span",[t._v("Deletar")])],2)],1)]}}])})],1)],1)],1)],1)},s=[],c=(r("8e6e"),r("ac6a"),r("456d"),r("bd86")),i=r("2f62");function o(t,e){var r=Object.keys(t);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(t);e&&(a=a.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),r.push.apply(r,a)}return r}function n(t){for(var e=1;e<arguments.length;e++){var r=null!=arguments[e]?arguments[e]:{};e%2?o(Object(r),!0).forEach((function(e){Object(c["a"])(t,e,r[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(r)):o(Object(r)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(r,e))}))}return t}var l={computed:n({},Object(i["e"])("categorias",["categorias"])),methods:n(n({},Object(i["b"])("categorias",["fetchCategorias","deleteCategoria"])),{},{createNew:function(){this.$router.push({path:"/categorias/novo"})},editItem:function(t){this.$router.push({path:"/categorias/".concat(t,"/update")})},deleteItem:function(t){this.deleteCategoria(t.id)}}),mounted:function(){this.fetchCategorias()},data:function(){return{search:"",headers:[{text:"#",sortable:!1},{text:"Nome",value:"nome"},{text:"Descrição",value:"descricao"},{text:"Ações",sortable:!1}]}}},u=l,d=r("2877"),f=Object(d["a"])(u,a,s,!1,null,null,null);e["default"]=f.exports}}]);
//# sourceMappingURL=chunk-2d221429.c8944fc2.js.map