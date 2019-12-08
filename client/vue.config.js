const path = require('path')

module.exports = {
  outputDir: path.resolve(__dirname, '../server/dist'),
  assetsDir: 'static',
  devServer: {
    proxy: 'http://localhost:4000',
    public: '192.168.1.22:4000',
    watchOptions: {
      poll: true
    }
  },
  transpileDependencies: [
    'vue-echarts',
    'resize-detector'
  ],
  chainWebpack: config => {
    config.module
      .rule('vue')      
      .use('vue-svg-inline-loader')
      .loader('vue-svg-inline-loader')      
      .options({});    
      

    config.module
      .rule('xlxs')
      .test(/\.xlsx$/)
      .use('webpack-xlsx-loader')
      .loader('webpack-xlsx-loader')
      .options({});
  }
}
