(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-61a6b611"],{"90b8":function(t,a,e){"use strict";var s=e("f7af"),n=e.n(s);n.a},a55b:function(t,a,e){"use strict";e.r(a);var s=function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("div",[e("v-content",[e("v-container",{attrs:{fluid:"","fill-height":""}},[e("v-layout",{attrs:{"align-center":"","justify-center":""}},[e("v-flex",{attrs:{xs12:"",sm8:"",md4:""}},[e("v-card",{staticClass:"elevation-12"},[e("v-toolbar",{attrs:{dark:"",color:"primary"}},[e("v-toolbar-title",[t._v("Login")])],1),e("v-card-text",[e("v-form",[e("v-text-field",{attrs:{name:"login",label:"Login",type:"text"},model:{value:t.username,callback:function(a){t.username=a},expression:"username"}}),e("v-text-field",{attrs:{id:"password",name:"password",label:"Password",type:"password"},model:{value:t.password,callback:function(a){t.password=a},expression:"password"}})],1)],1),e("v-card-actions",[e("v-spacer"),e("v-btn",{attrs:{color:"#ffa21a"},on:{click:t.handleSubmit}},[t._v("Login")])],1)],1)],1)],1)],1)],1)],1)},n=[],o={data:function(){return{username:"",password:"",submitted:!1}},computed:{loggingIn:function(){return this.$store.state.authentication.status.loggingIn}},created:function(){this.$store.dispatch("authentication/logout")},methods:{handleSubmit:function(t){this.submitted=!0;var a=this.username,e=this.password,s=this.$store.dispatch;a&&e&&s("authentication/login",{username:a,password:e})}}},r=o,i=(e("90b8"),e("2877")),c=Object(i["a"])(r,s,n,!1,null,"8cadb3e0",null);a["default"]=c.exports},f7af:function(t,a,e){}}]);
//# sourceMappingURL=chunk-61a6b611.1e65c4fd.js.map