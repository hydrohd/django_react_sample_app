const path = require("path")
const webpack = require("webpack")

module.exports = {
  entry: "./src/index.js",
  output: {
    path: path.resolve(__dirname, "./static/frontend"),
    filename: "[name].js",
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
        },
      },
    ],
  },
  optimization: {
    minimize: true,
  },
  plugins: [
    new webpack.DefinePlugin({
      "process.env": {
        // This has an effect on the react library size
        //TODO: CHANGE THIS TO PRODUCTION?? FIND A BETTER WAY TO MANAGE THIS
        NODE_ENV: JSON.stringify("development"),
      },
    }),
  ],
  stats: 'detailed'
}