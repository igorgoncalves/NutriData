const path = require("path");

module.exports = {
	outputDir: path.resolve(__dirname, "../dist"),
	assetsDir: 'static',
  devServer: {
    proxy: 'http://localhost:5000'
	},
	transpileDependencies: [
    'vue-echarts',
    'resize-detector'
  ],
  chainWebpack: config => {
		config.module
			.rule("vue")
				.use("vue-svg-inline-loader")
					.loader("vue-svg-inline-loader")
						.options({ /* ... */ })
	}
}
