(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-1fe6074a"],{"114c":function(a,t,e){},1434:function(a,t,e){"use strict";e.r(t);var i=function(){var a=this,t=a.$createElement,e=a._self._c||t;return e("v-container",{attrs:{"fill-height":"",fluid:"","grid-list-xl":""}},[e("v-layout",{attrs:{wrap:""}},[e("v-flex",{attrs:{md12:"",sm12:"",lg8:""}},[e("v-flex",{attrs:{md12:"",sm12:"",lg12:""}},[e("h2",[a._v(" "+a._s(a.filteredMacroindicador.nome)+" ")]),e("span",[a._v(a._s(a.filteredMacroindicador.descricao))])]),e("v-flex",{attrs:{md12:"",sm12:"",lg12:""}},[a.chart?e("v-chart",{ref:"chart",attrs:{options:a.chart,autoresize:""}}):a._e()],1),e("v-flex",{attrs:{md12:"",sm12:"",lg12:""}},[e("p",[a._v(" "+a._s(a.filteredMacroindicador.fonte)+" ")])])],1),e("v-flex",{attrs:{md12:"",sm12:"",lg4:""}},[e("v-card",[e("v-flex",{attrs:{md12:"",sm12:"",lg12:""}},[e("v-btn",{attrs:{color:"success"},on:{click:function(t){return a.updateChart()}}},[a._v("Atualizar gráfico")])],1),e("v-flex",{attrs:{md12:"",sm12:"",lg12:""}},[e("v-select",{attrs:{items:a.form[0].options,label:a.form[0].label,outline:""},on:{change:function(t){return a.changeChart()}},model:{value:a.form[0].value,callback:function(t){a.$set(a.form[0],"value",t)},expression:"form[0].value"}})],1),e("v-list",{attrs:{subheader:"","two-line":""}},[e("v-subheader",[a._v("Indicadores")]),a._l(a.filteredMacroindicador.indicadores,function(t,i){return e("v-list-tile",{key:i},[e("v-list-tile-action",[e("v-checkbox",{model:{value:a.filteredMacroindicador.indicadores[i].value,callback:function(t){a.$set(a.filteredMacroindicador.indicadores[i],"value",t)},expression:"filteredMacroindicador.indicadores[key].value"}})],1),e("v-list-tile-content",{on:{click:function(t){a.filteredMacroindicador.indicadores[i].value=!a.filteredMacroindicador.indicadores[i]}}},[e("v-list-tile-title",[a._v(a._s(t.nome))])],1)],1)})],2)],1)],1)],1)],1)},r=[],s=(e("7f7f"),e("cebc")),o=e("2f62"),n=e("9ca8"),c=(e("c037"),e("94b1"),e("ef97"),e("d28f"),e("f14c"),e("0ee7"),e("ebf9"),{title:{text:"",x:"center"},tooltip:{trigger:"item",formatter:"{b} : {c} ({d}%)"},legend:{type:"scroll",orient:"horizontal",right:20,top:20,bottom:20,data:[]},series:[{name:"",type:"pie",radius:"55%",center:["50%","60%"],data:[],itemStyle:{emphasis:{shadowBlur:10,shadowOffsetX:0,shadowColor:"rgba(0, 0, 0, 0.5)"}}}]}),d={tooltip:{trigger:"axis",axisPointer:{type:"shadow"}},legend:{data:[]},grid:{left:"3%",right:"4%",bottom:"3%",containLabel:!0},xAxis:{type:"category",data:[],boundaryGap:!0,xAxisTicks:{alignWithLabel:!0}},yAxis:{},series:[]},l={title:{text:"折线图堆叠"},tooltip:{trigger:"axis"},legend:{data:["batata","联盟广告","视频广告","直接访问","搜索引擎"]},grid:{left:"3%",right:"4%",bottom:"3%",containLabel:!0},toolbox:{feature:{saveAsImage:{}}},xAxis:{type:"category",boundaryGap:!1,data:[]},yAxis:{type:"value"},series:[]},f=e("f9b3"),u={components:{"v-chart":n["a"]},computed:Object(s["a"])({},Object(o["c"])("macroindicadores",["getMacroindicadorById"]),{filteredMacroindicador:function(){return this.getMacroindicadorById(this.$route.params.idMacroindicador)}}),data:function(){return{pie:c,bar:d,line:l,form:f,indicadores:[],chart:{},type:""}},methods:{changeChart:function(){switch(this.form[0].value){case"Pizza":this.chart=this.pie,this.type="pie";break;case"Barra":this.chart=this.bar,this.type="bar";break;case"Linha":this.chart=this.line,this.type="line";break;default:this.chart={};break}this.updateChart()},checkIndicador:function(a){return this.updateChart(),a},updateChart:function(){var a=this,t=this.filteredMacroindicador.indicadores.filter(function(a){return a.value&&0!=a.value}),e=[];switch(this.type){case"pie":e=t.map(function(a){return{name:a.nome,value:a.amostras.filter(function(a){return 0==a.codigo_localidade}).map(function(a){return a})[0].valor}}),this.chart.series[0].data=e,this.chart.series[0].name=this.filteredMacroindicador.unidade,this.chart.legend.data=t.map(function(a){return a.nome});break;case"line":case"bar":e=t.map(function(t){return{type:a.type,name:t.nome,data:t.amostras.filter(function(a){return 0==a.codigo_localidade}).map(function(a){return a.valor})}}),this.chart.xAxis={type:"category",boundaryGap:!1,data:t[0].amostras.filter(function(a){return 0==a.codigo_localidade}).map(function(a){return a.ano})},this.chart.series=e;break}this.$refs.chart.clear(),this.$refs.chart.mergeOptions(this.chart)}}},h=u,m=(e("8f17"),e("2877")),p=Object(m["a"])(h,i,r,!1,null,null,null);t["default"]=p.exports},"8f17":function(a,t,e){"use strict";var i=e("114c"),r=e.n(i);r.a},f9b3:function(a){a.exports=[{label:"Tipo de gráfico",options:["Pizza","Barra","Linha"],value:""},{label:"Lista de Indicadores",lista:[{nome:"Batata",id:"safsafsafsdafsda"},{nome:"Batata",id:"safsafsafsdafsda"},{nome:"Batata",id:"safsafsafsdafsda"},{nome:"Batata",id:"safsafsafsdafsda"},{nome:"Batata",id:"safsafsafsdafsda"}]}]}}]);
//# sourceMappingURL=chunk-1fe6074a.de5f6428.js.map