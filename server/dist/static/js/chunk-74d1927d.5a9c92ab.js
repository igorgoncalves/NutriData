(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-74d1927d"],{"9c805":function(t,e,a){"use strict";a.r(e);var r=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("v-container",{attrs:{"fill-height":"",fluid:"","grid-list-xl":""}},[a("v-layout",{attrs:{wrap:""}},[a("v-flex",{attrs:{md12:"",sm12:"",lg12:""}},[a("v-card",[a("v-card-title",[a("v-flex",{attrs:{md12:"",sm12:"",lg10:""}},[a("h2",[t._v("Lista de localidades")])]),a("v-layout",{attrs:{"align-end":""}}),a("v-spacer"),a("v-flex",{attrs:{md12:"",sm12:"",lg4:"","offset-lg8":""}},[a("v-text-field",{attrs:{"append-icon":"mdi-search",label:"Buscar (Ex.: Aracaju)","single-line":"","hide-details":""},model:{value:t.search,callback:function(e){t.search=e},expression:"search"}})],1)],1),a("v-data-table",{staticClass:"elevation-1",attrs:{headers:t.headers,items:t.getLocalidades,search:t.search},scopedSlots:t._u([{key:"items",fn:function(e){return[a("td"),a("td",[t._v(t._s(e.item.codigo))]),a("td",{staticClass:"text-xs-left"},[t._v(t._s(e.item.nome))]),a("td",{staticClass:"justify-center px-0"},[a("v-tooltip",{attrs:{top:""}},[[a("v-icon",{attrs:{slot:"activator"},on:{click:function(a){return t.showMacroindicadores(e.item.codigo)}},slot:"activator"},[t._v("\n                    mdi-subdirectory-arrow-right\n                  ")])],a("span",[t._v("Gerenciar indicadores")])],2)],1)]}}])})],1)],1)],1)],1)},s=[],c=(a("8e6e"),a("ac6a"),a("456d"),a("bd86")),o=a("2f62");function i(t,e){var a=Object.keys(t);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(t);e&&(r=r.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),a.push.apply(a,r)}return a}function n(t){for(var e=1;e<arguments.length;e++){var a=null!=arguments[e]?arguments[e]:{};e%2?i(Object(a),!0).forEach((function(e){Object(c["a"])(t,e,a[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(a)):i(Object(a)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(a,e))}))}return t}var l={computed:n({},Object(o["c"])("localidades",["getLocalidades"])),methods:n(n({},Object(o["b"])("localidades",["fetchLocalidades"])),{},{showMacroindicadores:function(t){this.$router.push({path:"localidade/".concat(t,"/macroindicadores")})}}),mounted:function(){this.fetchLocalidades()},data:function(){return{search:"",headers:[{text:"#",sortable:!1},{text:"Código",value:"codigo"},{text:"Nome",value:"nome"},{text:"Ações",sortable:!1}],desserts:this.getLocalidades}}},d=l,u=a("2877"),f=Object(u["a"])(d,r,s,!1,null,null,null);e["default"]=f.exports}}]);
//# sourceMappingURL=chunk-74d1927d.5a9c92ab.js.map