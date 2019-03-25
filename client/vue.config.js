const path = require("path");

module.exports = {
	outputDir: path.resolve(__dirname, "../dist"),
	assetsDir: 'static',
  devServer: {
    proxy: 'http://localhost:5000'
  },
  chainWebpack: config => {
		config.module
			.rule("vue")
				.use("vue-svg-inline-loader")
					.loader("vue-svg-inline-loader")
						.options({ /* ... */ })
	}
}
