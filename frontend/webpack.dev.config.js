const path = require('path')
const { HotModuleReplacementPlugin } = require('webpack')
const MiniCssExtractPlugin = require('mini-css-extract-plugin')
const ReactRefreshWebpackPlugin = require('@pmmmwh/react-refresh-webpack-plugin')

module.exports = {
  mode: 'development',
  entry: ['./index.jsx'],
  output: {
    path: path.resolve(__dirname, '../static'),
    filename: 'bundle.js',
    publicPath: '/static/'
  },
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        loader: 'babel-loader',
        exclude: /node_modules/,
        options: {
          presets: ['@babel/preset-env', '@babel/preset-react'],
          plugins: ['react-refresh/babel']
        }
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader']
      },
      {
        test: /\.svg$/,
        use: [
          {
            loader: 'svg-url-loader',
            options: {
              limit: 10000
            }
          }
        ]
      }
    ]
  },
  plugins: [
    new HotModuleReplacementPlugin(),
    new MiniCssExtractPlugin({
      filename: 'bundle.css'
    }),
    new ReactRefreshWebpackPlugin({
      overlay: {
        sockPort: 8090
      }
    })
  ],
  devServer: {
    port: 8090,
    hotOnly: true,
    writeToDisk: true,
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, PATCH, OPTIONS',
      'Access-Control-Allow-Headers':
        'X-Requested-With, content-type, Authorization'
    }
  }
}
